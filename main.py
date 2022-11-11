import glob
import sys, os


def main():
    file = sys.argv[0]
    pathname = os.path.dirname(file)

    listOtvetov = []

    while True:
        print('Введите: "вариант", "задание 1", "задание 4", "задание 5", "задание 6" по форме -')
        print('---**вариант(пробел)12345(пробел)12345(пробел)12345(пробел)12345(Enter)**---')
        v = input().split()
        listOtvetov.append(v)
        print("Желаете продолжить ввод('y' - да), или ('n' - нет)")
        ChtoDalee = input()
        if ChtoDalee.lower() == "y":
            continue
        else:
            break

    targetPattern = pathname + r"\***\**\*.ans"
    list_ans = glob.glob(targetPattern)

    listDate = []

    for i in range(len(list_ans)):
        i = list_ans[i]

        with open(i, 'r') as fl_yes:
            g = fl_yes.readline()
            g = g.split('Data')
            g = g[-1].split('VarNo')
            g = g[0].split('')
            g = g[1:]
            z1 = str(g[0][:5]) #  1 -ое задание - готово
            z4 = str(g[1][:5]) #  4 -ое задание - готово
            z5 = str(g[2][:5]) # 5
            z6 = str(g[3][:5]) # 6
            id_r = str(i.split("\\")[-2])
            variant = str(g[3][8:9])
            listDate.append([id_r, variant, z1, z4, z5, z6])

    list_end = []

    for i in listDate:
        perenos = []
        for j in listOtvetov:
            if i[1] == j[0]:
                perenos.append(i[0])
                perenos.append(i[1])
                g = i[2:]
                h = j[1:]
                for l in range(0, 4):
                    countS = 0
                    for l1 in range(0, 5):
                        if g[l][l1] == h[l][l1]:
                            countS += 1
                    perenos.append(countS)
        if len(perenos) > 0:
            list_end.append(perenos)

    for i in list_end:
        print(f"id- {i[0]}||в-{i[1]}|| 1)- {i[2]} || 4)- {i[3]} || 5)- {i[4]} || 6)- {i[5]} ||")

    m = input()

if __name__ == '__main__':
    main()