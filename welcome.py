"""Welcome script for the Python Remote Debugger project.

Prints a welcome statement including contributor names and confirms the remote debugger is working.
"""

def main():
    names = [
        "Leela Sai Surya Veer Pedarla",
        "Sai Niranjan Chitturi",
    ]

    print("Welcome to the Python Remote Debugger!\n")
    print("Contributors:")
    for n in names:
        print(f" - {n}")

    print("\nRemote debugger status: The remote debugger is working")


if __name__ == "__main__":
    main()
