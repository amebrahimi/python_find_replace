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


def read_from_json_file_and_convert_to_python_object(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)


def convert_json_object_keys_to_snake_case(json_object):
    new_json_object = {}
    old_object_keys = {}
    for key, value in json_object.items():
        new_key = snake_case(key)
        new_json_object[new_key] = value
        old_object_keys[key] = new_key
    return new_json_object, old_object_keys


def snake_case(word):
    new_word = ""
    for i, letter in enumerate(word):
        if letter.isupper() and i != 0:
            new_word += "_" + letter.lower()
        else:
            new_word += letter.lower()
    return new_word


def write_json_object_to_disk(json_object, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)

def sort_object_by_key(object):
    return dict(sorted(object.items()))


if __name__ == "__main__":
    files = find_files(
        "E:\\Programing\\projects\\flutter\\smith_flutter\\lib\\presentation", ".dart"
    )
    json_object = read_from_json_file_and_convert_to_python_object(
        "E:\\Programing\\projects\\flutter\\smith_flutter\\assets\\lang\\en.json"
    )

    snake_case, old_object = convert_json_object_keys_to_snake_case(json_object)

    write_json_object_to_disk(sort_object_by_key(snake_case), "en.json")

    # for file in files:
    #     for key, val in old_object.items():
    #         replace_word(
    #             file, f"context.translate('{key}')", f"context.translate('{val}')"
    #         )
