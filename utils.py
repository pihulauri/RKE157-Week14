import random


def clean_my_list(some_list):
    """
    Puhastab nimekirja elementide algusest ja lõpust tühikud
    ning reavahetused.
    """

    cleaned_list = []

    for element in some_list:
        cleaned_element = element.strip()  # Eemaldab tühikud ja \n märgid
        cleaned_list.append(cleaned_element)  # Lisab puhastatud elemendi nimekirja

    return cleaned_list


def read_from_file(file_path):
    """
    Loeb tekstifailist kõik read ja tagastab puhastatud nimekirja.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        data = file.readlines()  # Loeb kõik faili read nimekirja

    cleaned_data = clean_my_list(data)  # Puhastab reavahetused ja tühikud

    return cleaned_data


def get_random_item(file_path):
    """
    Loeb faili ja tagastab sellest ühe juhusliku väärtuse.
    """

    data = read_from_file(file_path)  # Loeb faili sisu nimekirja

    random_item = random.choice(data)  # Valib nimekirjast juhusliku elemendi

    return random_item