def count_words(text):
    return len(text.split())


def count_characters(text):
    res = {}

    for i in text:
        lower_i = i.lower()
        if lower_i > 'z' or lower_i < 'a':
            continue
        if lower_i in res:
            res[lower_i] += 1
        else:
            res[lower_i] = 1

    return res


def sort_on(dict):
    return dict["num"]


def print_report(stats, count):
    header = "--- Begin report of books/frankenstein.txt ---"
    footer = "--- End report ---"
    stats_list = []

    for item in stats:
        stats_list.append({"name": item, "num": stats[item]})
    stats_list.sort(reverse=True, key=sort_on)

    print(header)
    print(f"{count} words found in the document\n")
    
    for i in stats_list:
        print(f"The '{i["name"]}' character was found {i["num"]} times")

    print(footer)


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)
    count = count_words(file_contents)
    # print(count)
    stats = count_characters(file_contents)
    # print(stats)
    print_report(stats, count)


main()
