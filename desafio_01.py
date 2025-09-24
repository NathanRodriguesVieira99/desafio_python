class N:
    typed_numbers = set()

# função que recebe o(s) número(s) informados como parâmetro
    def is_happy(self, typed_number: int) -> bool:

        #  se o(s) números for(em) infeliz(es) retorna False
        if typed_number in N.typed_numbers:
            N.typed_numbers.clear()
            return False

        N.typed_numbers.add(typed_number)

        sum_function = sum(int(digito)**2 for digito in str(typed_number))

# se o(s) números for(em) feliz(es) retorna True
        if sum_function == 1:
            N.typed_numbers.clear()
            return True

        return self.is_happy(sum_function)


n = N()

# informa o(s) número(s)
input_value = input("Digite um  número: ")


# pega o(s) número(s) e valida se o cálculo está correto (feliz ou infeliz)

for valor in input_value.split():
    try:
        typed_number = int(valor)
        if n.is_happy(typed_number):
            print(f"Feliz: {typed_number}")
        else:
            print(f"Infeliz: {typed_number}")
    except ValueError:
        print(f"Ignorado (não é número válido): {valor}")

"""
Usamos de referência uma pergunta de um usuário no Stack Overflow

link de referência: https://stackoverflow.com/questions/63751186/happy-number-string-python-function
"""
