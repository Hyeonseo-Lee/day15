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

    for i in range(idx + 1, len_pokemons):
        pokemons[i] = None

    for i in range(idx, 5):
        pokemons.pop()


if __name__ == "__main__":

    print(pokemons)
    #insert_data(2, '거북왕')
    delete_data(1)
    print(pokemons)
    #insert_data(6, '어니부기')
    print(pokemons)

