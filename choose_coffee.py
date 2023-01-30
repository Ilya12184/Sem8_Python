ingredients = list(map(int, input('Количество ингредиентов по вашим предпочтениям? ').split()))
print(f'ingredients = {ingredients}')

def choose_coffee(*preference):
    for choose in preference:
            if choose == 'Эспрессо' and ingredients[0] >= 1:
                ingredients[0] -= 1
                return choose
            elif choose == 'Маккиато' and ingredients[0] >= 2 and ingredients[1] >= 1:
                ingredients[0] -= 2
                ingredients[1] -= 1
                return choose
            elif choose == 'Капучино' and ingredients[0] >= 1 and ingredients[1] >= 3:
                ingredients[0] -= 1
                ingredients[1] -= 3
                return choose
            elif choose == 'Кофе по-венски' and ingredients[0] >= 1 and ingredients[2] >= 2:
                ingredients[0] -= 1
                ingredients[2] -= 2
                return choose
            elif choose == 'Латте Маккиато' and ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[1] -= 2
                ingredients[2] -= 1
                return choose
            elif choose == 'Кон Панна' and ingredients[0] >= 1 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[2] -= 2
                return choose
    return 'К сожалению, не можем предложить Вам напиток'

print(choose_coffee('Капучино', 'Маккиато', 'Эспрессо'))
print(choose_coffee('Капучино', 'Маккиато', 'Эспрессо'))
print(choose_coffee('Капучино', 'Маккиато', 'Эспрессо'))


# print(choose_coffee('Эспрессо', 'Капучино', 'Маккиато', 'Кофе по-венски', 'Латте Маккиато', 'Кон Панна'))
# print(choose_coffee('Эспрессо', 'Капучино', 'Маккиато', 'Кофе по-венски', 'Латте Маккиато', 'Кон Панна'))