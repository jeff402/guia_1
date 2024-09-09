def kilogramos_a_libras(kilogramos):
    return kilogramos * 2.20462

def libras_a_gramos(libras):
    return libras * 453.592

#if _name  == "_main_":

kilogramos = 5
libras = kilogramos_a_libras(kilogramos)
print(f"{kilogramos}kilogramos equibale a {libras:.2f} libras. ")