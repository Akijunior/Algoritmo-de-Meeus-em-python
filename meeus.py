def meeus(ano):
    X = 0
    Y = 0

    if (ano >= 1582 and ano <= 1699):
        X = 22
        Y = 2
    if (ano >= 1700 and ano <= 1799):
        X = 23
        Y = 3
    if (ano >= 1800 and ano <= 1899):
        X = 23
        Y = 4
    if (ano >= 1900 and ano <= 2099):
        X = 24
        Y = 5
    if (ano >= 2100 and ano <= 2199):
        X = 24
        Y = 6
    if (ano >= 2200 and ano <= 2299):
        X = 25
        Y = 7

    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = ((19 * a) + X) % 30
    e = (((2 * b) + (4 * c) + (6 * d) + Y)) % 7

    dia = ""
    mes = ""

    if ((d + e) < 10):
        dia = d + e + 22
        mes = 3
    else:
        dia = d + e - 9
        mes = 4
        
    if (dia == 26 and mes == 4):
        dia = 19

    if (dia == 25 and mes == 4 and d == 28 and a > 10):
        dia = 18

    return datetime.datetime.strptime(f"{ano}/{mes}/{dia}", '%Y/%m/%d')
