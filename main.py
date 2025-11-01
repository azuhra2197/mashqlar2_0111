# 1
satrlar = input('satrlarni vergul b-n ajratib kiriting: ').split(',')
katta_harf = list(map(str.upper, satrlar))
print('katta harfli satrlar royhati:')
for x in katta_harf:
    print(x)

# 2
sonlar = [1, 46, 8, 12, 8, 9]

uchga_bolinadiganlar = []
for son in sonlar:
    if son % 3 == 0:
        uchga_bolinadiganlar.append(son)

print(uchga_bolinadiganlar)

# 3
satrlar = ['salom', 'dunyo']

uzunliklar = list(map(len, satrlar))
print(uzunliklar)

# 4
sonlar = [1, 2, -5, 3, 2, -9]

m_sonlar = list(filter(lambda x: x > 0, sonlar))
i_barobar = list(map(lambda x: x * 2, m_sonlar))

print('musbat sonlar', m_sonlar)
print('oshirilgan sonlar', i_barobar)
