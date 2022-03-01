import connection_manager


def main():
    print("Welcome to a socket example.\nType quit or exit to end the process.")
    manager = connection_manager.ConnectionManager("127.0.0.1", 7171)
    manager.start()
    while True:
        message = str(input("Digit message:"))
        if(message == "exit" or message == "quit"):
            manager.close();
        else:
            manager.broadcast(message)

if __name__ == "__main__":
    main()
