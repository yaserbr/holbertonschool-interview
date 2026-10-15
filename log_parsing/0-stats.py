#!/usr/bin/python3
"""Reads log lines from stdin and prints file size and status code stats."""
import sys


def print_stats(total_size, status_counts):
    """Print the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Parse stdin and print stats every 10 lines and on interruption."""
    total_size = 0
    line_count = 0
    status_counts = {code: 0 for code in
                     ["200", "301", "400", "401",
                      "403", "404", "405", "500"]}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = parts[-2]
                if code in status_counts:
                    status_counts[code] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
