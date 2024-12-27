import data, logo, random


print(logo.logo)

score = 0
compute_1 = random.randint(0, len(data.data) - 1)
compute_2 = random.randint(0, len(data.data) - 1)
if compute_1 == compute_2:
    compute_2 = random.randint(0, len(data.data) - 1)


def game(one, two, count):

    print(
        f"compare 1: {data.data[one]["name"]}, {data.data[one]["description"]}, {data.data[one]["country"]}"
    )
    print(logo.vs)
    print(
        f"compare 2: {data.data[two]["name"]}, {data.data[two]["description"]}, {data.data[two]["country"]}"
    )

    choose = input(
        f"Who has more follower: type 'A' for {data.data[one]["name"]} 'B' for {data.data[two]["name"]}: "
    )

    user_choose = data.data[one]["name"] if choose == "A" else data.data[two]["name"]

    higher_follower = ""
    if data.data[one]["follower_count"] > data.data[two]["follower_count"]:
        higher_follower = data.data[one]["name"]
        two = random.randint(0, len(data.data) - 1)
        if one == two:
            two = random.randint(0, len(data.data) - 1)
    elif data.data[one]["follower_count"] < data.data[two]["follower_count"]:
        higher_follower = data.data[two]["name"]
        one = two
        two = random.randint(0, len(data.data) - 1)
        if one == two:
            two = random.randint(0, len(data.data) - 1)

    if higher_follower == user_choose:
        print("You Add 1 point.")
        count += 1

        game(one, two, count)
    else:
        print("Sorry. That is Wrong!!")
        print(f"Your Score: {count}")


game(compute_1, compute_2, score)
