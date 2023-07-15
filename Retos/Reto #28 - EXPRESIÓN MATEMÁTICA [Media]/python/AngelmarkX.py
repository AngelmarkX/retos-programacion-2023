''' 
* Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */'''

def funcion(expMath):
    simbols = "+-*/%"
    expSplit = expMath.split()
    print(expSplit)

    for elemento in expSplit:
        if elemento not in simbols and not elemento.isdigit():
            return False

    
    return True


expresion = input("Ingrese la expresion matematica: ")

print(funcion(expresion))
