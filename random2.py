import json

def main():
    while True:
        with open("storage_file.json", "r") as file:
            data=json.load(file)
        query=input("Enter what you want to view:\n")
        if query in data:
            print(f"your response is {data[query]}")
        else:
            print("The requested resource is not present\n")
            break


if __name__=="__main__":
    main()