def retorna_mmc(numero):
    mmc = []
    for num in range(2, abs(numero)+1):
        while True:
            if numero % num == 0:
                mmc.append(num)
                numero /= num
            else:
                break
    return mmc

def mult(lista):
    holder = 1
    for i in lista:
        holder *= i 
    return holder 

def cortes(lista_maior, lista_menor):
    for _ in range(2):
        for i in lista_maior:
            for j in lista_menor:
                if i == j:
                    lista_maior.remove(j)
                    lista_menor.remove(j)

def simplificar(numerador, denominador):
    if numerador != denominador:
        numer_is_neg = numerador < 0
        denom_is_neg = denominador < 0
        numerador_mmc = retorna_mmc(numerador)
        denominador_mmc = retorna_mmc(denominador)
        if len(numerador_mmc) >= len(denominador_mmc):
            cortes(numerador_mmc, denominador_mmc)
        else:
            cortes(denominador_mmc, numerador_mmc)
        numerador_smp = mult(numerador_mmc)
        denominador_smp = mult(denominador_mmc)
        if numer_is_neg:
            numerador_smp = -numerador_smp
        if denom_is_neg:
            denominador_smp = -denominador_smp
        return numerador_smp, denominador_smp
    return '1'