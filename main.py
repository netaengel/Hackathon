import geopy
import geopandas
import os
import patients
import consts
# import DonorAddress
import random


def main():
    for i in range(consts.HOSPITAL_NUM):
        hospital_name = patients.choose_hospital()
        file_name = "{}_list.txt".format(hospital_name)
        # file_name = "patients_list.txt"
        patients_num = random.randint(10, 21)

        id_list = patients.create_id_list(patients_num)
        print(id_list)
        patients_dict = patients.create_patients_list(id_list)
        print(patients_dict)
        patients.set_patients_text(patients.patient_path, file_name, patients_dict)

if __name__ == '__main__':
    main()
