import re


def _get_total_number():
    found = 0
    with open("output.txt", encoding="utf8") as f:
        for line in f:
            if found == 2:
                return line.strip()
            if found == 1:
                found += 1
            if "<td> 合計</td>" in line.strip():
                found += 1


def extract_total_num():
    line_with_num = _get_total_number()
    num_list = re.findall(r"\d+", str(line_with_num))

    actual_num = "".join(str(elem) for elem in num_list)
    return int(actual_num)