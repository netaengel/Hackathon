import os
import random

import consts

patient_path = input("please enter the path")


def choose_area():
    area = int(random.randint(1, 3))
    if area == 1 and len(consts.NORTH_HOSPITALS) > 0:
        return "North"
    elif area == 2 and len(consts.CENTER_HOSPITALS) > 0:
        return "Center"
    if len(consts.SOUTH_HOSPITALS) > 0:
        return "South"


def choose_hospital():
    ret_hospital = ""
    for hospital in consts.ALL_HOSPITALS:
        ret_hospital = consts.ALL_HOSPITALS.pop(-1)
    return ret_hospital
    # area = choose_area()
    # if area == "North":
    #     hospital = consts.NORTH_HOSPITALS.pop(-1)
    # elif area == "Center":
    #     hospital = consts.CENTER_HOSPITALS.pop(-1)
    # else:
    #     hospital = consts.SOUTH_HOSPITALS.pop(-1)
    # return hospital


def create_id_list(patients_num):
    id_list = []
    # for i in patients_num:
    i = 0
    while i <= patients_num:
        id = ""
        for digit in range(9):
            rnd_num = random.randint(0, 9)
            id += str(rnd_num)
        if id not in id_list:
            id_list.append(id)
            i += 1
    return id_list


def create_patients_list(id_list):
    patients_dict = {}
    for person in id_list:
        organ = consts.ORGAN_LIST[random.randint(0, len(consts.ORGAN_LIST) - 1)]
        blood_type = consts.BLOOD_TYPE_LIST[random.randint(0, len(consts.BLOOD_TYPE_LIST) - 1)]
        urgency_level = random.randint(1, 10)
        patients_dict[person] = [organ, blood_type, urgency_level]
    return patients_dict


def set_patients_text(patient_path, file_name, patients_dict):
    # patient_path = r"{}".format(file_name)
    # patient_file = open(patient_path, "r")
    patient_file = open(patient_path, "w+")  # Opens a file for reading only
    patient_file = open(patient_path, "w")  # Opens a file for writing , overwriting the text
    # f= patient_file.readlines()
    # print(f, file_name)
    for patient in patients_dict:
        patient_file.write(str(patient) + ": " + str(
            patients_dict[patient]))  # Write in the existed file or open a new file and write in it.
        patient_file.write("\n")
    patient_file.close()
