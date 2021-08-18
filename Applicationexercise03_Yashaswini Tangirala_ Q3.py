data = int(input("Enter the number of countries to be be entered: "))

print()

cnt_dict = dict()

for i in range(data):
    x = input("Enter the country name: ")
    y = input("Enter the capital: ")
    print()
    cnt_dict[x] = y
print(cnt_dict)
print("Countries")
countries = []
for i in cnt_dict:
    m = i.isalpha()
    if m:
        countries.append(i)
print(f'{countries}')
print("Capitals")
capital = []
for i in cnt_dict:
    n = cnt_dict[i].isalpha()
    if n:
        capital.append(cnt_dict[i])
print(f'{capital}')