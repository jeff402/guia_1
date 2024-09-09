def metros_a_pulgadas(metros):
    return metros *39.37

def pulgadas_a_pies(pulgadas):
    return pulgadas /12


# if name == "_main_":

    metros = int(input("ingrese su la cantidad de metros"))
    pulgadas = metros_a_pulgadas(metros)
    print(f"{metros}metros equibalen a {pulgadas:.f2}pulgadas. ")