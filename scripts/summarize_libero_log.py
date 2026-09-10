#!/usr/bin/env python3
"""Summarize task-level LIBERO results from an OpenPI evaluation log."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import OrderedDict
from pathlib import Path


TASK_RE = re.compile(r"Task:\s*(.+?)\s*$")
SUCCESS_RE = re.compile(r"Success:\s*(True|False)\s*$")
ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")


def parse_log(path: Path) -> OrderedDict[str, list[bool]]:
    results: OrderedDict[str, list[bool]] = OrderedDict()
    current_task: str | None = None

    with path.open(encoding="utf-8", errors="replace") as stream:
        for raw_line in stream:
            line = ANSI_RE.sub("", raw_line).strip()
            if match := TASK_RE.search(line):
                current_task = match.group(1)
                results.setdefault(current_task, [])
                continue
            if match := SUCCESS_RE.search(line):
                if current_task is None:
                    raise ValueError("Found a success result before any task name")
                results[current_task].append(match.group(1) == "True")

    if not results:
        raise ValueError("No LIBERO task results found in the log")
    return results


def write_csv(results: OrderedDict[str, list[bool]], output) -> None:
    writer = csv.writer(output)
    writer.writerow(["task", "episodes", "successes", "success_rate_percent"])
    for task, outcomes in results.items():
        successes = sum(outcomes)
        writer.writerow([task, len(outcomes), successes, f"{100 * successes / len(outcomes):.1f}"])

    all_outcomes = [outcome for outcomes in results.values() for outcome in outcomes]
    total_successes = sum(all_outcomes)
    writer.writerow(["TOTAL", len(all_outcomes), total_successes, f"{100 * total_successes / len(all_outcomes):.1f}"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path, help="OpenPI LIBERO evaluation log")
    parser.add_argument("-o", "--output", type=Path, help="CSV output path (default: stdout)")
    args = parser.parse_args()

    try:
        results = parse_log(args.log)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    if args.output:
        with args.output.open("w", encoding="utf-8", newline="") as output:
            write_csv(results, output)
    else:
        write_csv(results, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

