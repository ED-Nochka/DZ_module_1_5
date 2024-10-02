immutable_var = "pion", "rose", "phlox", 1, 2
print(immutable_var)
#immutable_var[0] = "x"  # при изменении элемента кортежа по индексу элемента,
#                       на консоле мы видим ошибку о том, что кортеж не поддерживает
#                       обращение по элементам.
#print(immutable_var)
mutable_list = ["pion", "rose", 1, 2]
print(mutable_list)
mutable_list.remove(1)
print(mutable_list)
# или по индексу:
mutable_list [0] = "x"
print(mutable_list)