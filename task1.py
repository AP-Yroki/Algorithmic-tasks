digit = int(input("Введите ваше число: "))

def is_simple(digit):
  if digit <= 1:
      return f"Число {digit} не простое"
  for i in range(2, digit):
    if digit % i == 0:
        return f"Число {digit} не простое"
  return f"Число {digit} простое"

print(is_simple(digit))