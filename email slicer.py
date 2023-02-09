def main():
    print(" Welcome ot the email slicer ")
    print("")

    email_input = input("Input your email adress: ")
    (username, domain) = email_input.split("@")

    print("Username : ", username)
    print("Domain : ", domain)


main()
