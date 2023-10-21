# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, sep=','):
    result = []
    first_group_list = list(map(str, first_group.split(sep)))
    second_group_list = list(map(str, second_group.split(sep)))
    for i in first_group_list:
        if i in second_group_list:
            result.append(i)
    result.sort()
    return(result)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,
                               participants_second_group, '|'))
