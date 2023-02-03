## 함수 선언 부분 ##
def print_Poly(px):
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_Str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수

        # if coef >= 0:
        #     poly_Str = poly_Str + "+"

        if i > 0 and coef > 0:
            poly_Str = poly_Str + "+"
        elif coef == 0:
            term = term - 1
            continue
        poly_Str = poly_Str + f'{coef}x^{term}'
        term = term - 1

    return poly_Str


def calc_poly(xVal, p_x):
    ret_value = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        coef = p_x[i]
        ret_value = ret_value + coef * xVal ** term
        term -= 1

    return ret_value



px = [3, -4, 0, 6]

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = print_Poly(px)
    print(pStr)

    x_value = int(input("X 값-->"))

    px_value = calc_poly(x_value, px)
    print(px_value)


