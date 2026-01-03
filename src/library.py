# argparse helps turn terminal input into structured data
import argparse


def main():
    # Set up the main command-line interface for the program
    parser = argparse.ArgumentParser(
        # the name of the program
        prog="library",
        #decription of program
        description="Personal Library Manager"
    )

    # Allow the program to have multiple commands
    sub = parser.add_subparsers(dest="cmd", required=True)

    # Define the command used to add a book
    add = sub.add_parser("add")

    # Information needed to describe a book
    add.add_argument("--title", required=True)
    add.add_argument("--author", required=True)

    # Extra labels that help group or search for books, the tags argument doesn't require a value nor is it required
    add.add_argument("--tags", nargs="*", default=[])

    # Define the command used to show all books
    sub.add_parser("list")

    # Read the users input and store it
    args = parser.parse_args()

    # Decide what to do based on the chosen command
    if args.cmd == "add":
        print(f"Added: {args.title} by {args.author}")
        print(f"Tags: {args.tags}")

    elif args.cmd == "list":
        print("Listing books")


# Only start the program when this file is run directly
if __name__ == "__main__":
    main()
