import argparse
from .hash import sha256_file


def main():
    parser = argparse.ArgumentParser(prog="sb-sim")
    subparsers = parser.add_subparsers(dest="command")

    hash_cmd = subparsers.add_parser("hash", help="Compute SHA256 of a firmware binary")
    hash_cmd.add_argument("file", help="Path to firmware binary")

    args = parser.parse_args()

    if args.command == "hash":
        digest = sha256_file(args.file)
        print(f"SHA256: {digest}")
    else:
        parser.print_help()
