styp = 50  # стипендія
vytraty = 80  # загальні витрати
months = 10
zag_borg = 0  # загальний борг

for month in range(1, months + 1):
    debt = vytraty - styp
    zag_borg += debt
    vytraty *= 1.02  # збільшення витрат на 2%

print("Загальний борг студента зa",months,"місяців:",zag_borg,": грн")
