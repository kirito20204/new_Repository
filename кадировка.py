'''def search_substr(subst, st):
    if subst.lower() in st.lower():
        print('Есть контакт!')
    else:
        print('Мимо!')


(search_substr('Кол', 'коЛокОл'))
(search_substr('Колобок', 'колобоК'))
(search_substr('Кол', 'Плов'))'''

def first_last(letter, st):
    first=st.find(letter)
    if first== -1:
        return None, None
    last=st.rfind(letter)
    return first, last


print(first_last('a', 'abba'))
print(first_last('a', 'abbaaaab'))
print(first_last('a', 'a'))
print(first_last('a', 'spring'))