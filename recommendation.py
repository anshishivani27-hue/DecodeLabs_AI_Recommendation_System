while True:

    print("=" * 50)
    print("         AI RECOMMENDATION SYSTEM")
    print("=" * 50)

    print("\nChoose your area of interest:")
    print("1. Artificial Intelligence")
    print("2. Web Development")
    print("3. Cyber Security")
    print("4. Data Science")
    print("5. Cloud Computing")
    print("6. Mobile App Development")

    choice = input("\nEnter your choice (1-6): ")

    print("\nChoose your learning level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    level = input("Enter your level (1-3): ")

    print("\nHow much time can you study daily?")
    print("1. Less than 1 hour")
    print("2. 1-2 hours")
    print("3. More than 2 hours")

    time = input("Enter your choice (1-3): ")

    print("\n" + "=" * 50)

    if choice == "1":
        print("🤖 Artificial Intelligence Recommendations\n")

        if level == "1":
            print("Recommended Courses:")
            print("✔ Python Basics")
            print("✔ Introduction to AI")
            print("✔ Machine Learning Basics")

        elif level == "2":
            print("Recommended Courses:")
            print("✔ Machine Learning")
            print("✔ Deep Learning")
            print("✔ Computer Vision")

        elif level == "3":
            print("Recommended Courses:")
            print("✔ Natural Language Processing")
            print("✔ Generative AI")
            print("✔ Reinforcement Learning")

    elif choice == "2":
        print("💻 Web Development Recommendations\n")
        print("✔ HTML & CSS")
        print("✔ JavaScript")
        print("✔ React")
        print("✔ Node.js")

    elif choice == "3":
        print("🔐 Cyber Security Recommendations\n")
        print("✔ Ethical Hacking")
        print("✔ Network Security")
        print("✔ Penetration Testing")
        print("✔ Digital Forensics")

    elif choice == "4":
        print("📊 Data Science Recommendations\n")
        print("✔ Python for Data Science")
        print("✔ Pandas")
        print("✔ Data Visualization")
        print("✔ SQL")

    elif choice == "5":
        print("☁ Cloud Computing Recommendations\n")
        print("✔ AWS Fundamentals")
        print("✔ Microsoft Azure")
        print("✔ Google Cloud")
        print("✔ Docker Basics")

    elif choice == "6":
        print("📱 Mobile App Development Recommendations\n")
        print("✔ Java")
        print("✔ Kotlin")
        print("✔ Flutter")
        print("✔ React Native")

    else:
        print("❌ Invalid category selected!")

    print("\n" + "=" * 50)

    print("📚 Recommended Learning Platforms")
    print("✔ Coursera")
    print("✔ Udemy")
    print("✔ freeCodeCamp")
    print("✔ Kaggle")
    print("✔ YouTube")

    print("\n" + "=" * 50)

    if time == "1":
        print("📅 Suggested Study Plan")
        print("Study 45 minutes daily.")
        print("Complete one course in about 2 months.")

    elif time == "2":
        print("📅 Suggested Study Plan")
        print("Study 2 hours daily.")
        print("Complete one course in about 1 month.")

    elif time == "3":
        print("📅 Suggested Study Plan")
        print("Study 3+ hours daily.")
        print("Complete one course in 2-3 weeks.")

    else:
        print("Invalid study time selected.")

    print("=" * 50)

    again = input("\nDo you want another recommendation? (yes/no): ").lower()

    if again != "yes":
        print("\n" + "=" * 50)
        print("Thank you for using the AI Recommendation System!")
        print("Keep Learning • Keep Growing • Happy Coding! 🚀")
        print("=" * 50)
        break