import os, json

# traverse through folders recursively and find all files with .dart ext
def find_files(directory, ext):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                yield os.path.join(root, file)


# find word in file and replace it with new word
def replace_word(file, word, new_word):
    with open(file, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if word in line:
                lines[i] = line.replace(word, new_word)
    with open(file, "w") as f:
        f.writelines(lines)


# find word in file
def find_word(file, word):
    with open(file, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if word in line:
                return True
    return False


def read_from_json_file_and_convert_to_python_object(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)


def convert_json_object_keys_to_snake_case(json_object):
    new_json_object = {}
    old_object_keys_with_new_values = {}
    for key, value in json_object.items():
        new_key = snake_case(key)
        new_json_object[new_key] = value
        old_object_keys_with_new_values[key] = new_key
    return new_json_object, old_object_keys_with_new_values


def snake_case(word):
    snake_case_string = ""
    for i in range(len(word)):
        if i == 0:
            snake_case_string += word[i].lower()
        elif word[i].isupper() and word[i - 1].islower():
            snake_case_string += "_" + word[i].lower()
        elif word[i] == ' ' and word[i - 1].islower():
            snake_case_string += "_"
        else:
            snake_case_string += word[i].lower()
    return snake_case_string


def write_json_object_to_disk(json_object, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)


def sort_object_by_key(object):
    return dict(sorted(object.items()))


def write_set_to_disk_as_json_array(set, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(list(set), f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    files = find_files(
        "E:\\Programing\\projects\\flutter\\smith_flutter\\lib\\presentation", ".dart"
    )
    json_object = read_from_json_file_and_convert_to_python_object(
        "E:\\Programing\\projects\\flutter\\smith_flutter\\assets\\lang\\en.json"
    )

    snake_case, old_object = convert_json_object_keys_to_snake_case(json_object)

    write_json_object_to_disk(sort_object_by_key(snake_case), "en.json")

    key_not_used = set()
    for key, _ in old_object.items():
        key_not_used.add(key)

    for file in files:
        for key, val in old_object.items():
            if find_word(file, f"'{key}'"):
                if key in key_not_used:
                    key_not_used.remove(key)
                replace_word(file, f"'{key}'", f"'{val}'")

    write_set_to_disk_as_json_array(key_not_used, "key_not_used.json")
