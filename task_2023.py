
def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
    illumination_list = []
    last_street_light = (road_length / 20) + 1

    if len(not_working_street_lights) == 1:
        answer = not_working_street_lights[0]
        return answer

    for street_light in not_working_street_lights:
        distance = 20
        index = not_working_street_lights.index(street_light)
        if street_light == 0:
            for number in range(int(road_length / 20)):
                if number == not_working_street_lights[1]:
                    distance = number * 20
                    illumination = 3 ** (-(distance / 90) ** 2)
                    illumination_list.append(illumination)

        # if first element is not 0 then this street light has working light to the left so max distance is 20m
        elif index == 0:
            illumination = 3 ** (-(distance / 90) ** 2)
            illumination_list.append(illumination)

        # checking last element. Calculating nearest light to the left. If lamp is last street light only left side
        # counts, if not it means there is a lamp to the right which is the nearest.
        elif index == len(not_working_street_lights) - 1:
            left_num = 1
            for number in range(int(road_length / 20)):
                if street_light - (number + 1) in not_working_street_lights:
                    left_num += 1
                else:
                    break

            if street_light == last_street_light:
                right_num = left_num
            else:
                right_num = 1

            multiply = min(left_num, right_num)
            distance = multiply * 20
            illumination = 3 ** (-(distance / 90) ** 2)
            illumination_list.append(illumination)

        # if element doesn't have -1 or +1 neighbored elements in the list, that means distance is 20m
        elif street_light - 1 not in not_working_street_lights:
            illumination = 3 ** (-(distance / 90) ** 2)
            illumination_list.append(illumination)

        elif street_light + 1 not in not_working_street_lights:
            illumination = 3 ** (-(distance / 90) ** 2)
            illumination_list.append(illumination)

        # for every other element check to which side is nearest street light that works, and by that calculate distance
        else:
            left_num = 1
            right_num = 1

            for number in range(int(road_length / 20)):
                if street_light - (number + 1) in not_working_street_lights:
                    left_num += 1
                else:
                    break

            for number in range(int(road_length / 20)):
                if street_light + (number + 1) != last_street_light:
                    if street_light + (number + 1) in not_working_street_lights:
                        right_num += 1
                    else:
                        break
                else:
                    right_num = last_street_light

            multiply = min(left_num, right_num)
            distance = multiply * 20
            illumination = 3 ** (-(distance / 90) ** 2)
            illumination_list.append(illumination)

    illumination_list_2 = []
    for number in illumination_list:
        # number 100 is just a random high number so it doesn't have any influence to correct answer
        if number < 0.01:
            number = 100
        illumination_list_2.append(number)

    value = min(illumination_list_2)
    index = illumination_list_2.index(value)
    answer = not_working_street_lights[index]
    return answer

if __name__ == "__main__":
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6]) == 5
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[1,2,5,6,7,8,10,11]) == 6
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[1,2,5,6,7,8,9,10,11]) == 11
    print("ALL TESTS PASSED")
