pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


def insert_data(index, pokemon):
    if index < 0 or index > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, index, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[index] = pokemon  # 지정한 위치에 추가

def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return


    len_pokemons = len(pokemons)
    pokemons[idx] = None

    for _ in range(len_pokemons - idx):
        pokemons.pop()

    #self 3-1
    # for i in range(idx + 1, len_pokemons):
    #     pokemons[i] = None
    #
    # for i in range(idx, 5):
    #     pokemons.pop()

def add_data(pokemon):

    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon

pokemons = []
menu = -1

if __name__ == "__main__":

    while True:

        menu = input("1: 추가, 2: 삽입, 3: 삭제, 4: 종료--> ")

        if (menu == '1'):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif (menu == '2'):
            idx = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(idx, data)
            print(pokemons)
        elif (menu == '3'):
            idx = int(input("삭제할 위치--> "))
            delete_data(idx)
            print(pokemons)
        elif (menu == '4'):
            print(pokemons)
            exit()
            #break
        else:
            print("menu에서 고르시오")
            continue
