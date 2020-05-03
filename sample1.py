def warikan(amount, number_of_people):
    quotient = amount // number_of_people
    remainber = amount % number_of_people

    return f"1人あたり: {quotient}円, 端数: {remainber}円"


if __name__ == "__main__":
    print(warikan(1500, 3) == "1人あたり: 500円, 端数: 0円")
