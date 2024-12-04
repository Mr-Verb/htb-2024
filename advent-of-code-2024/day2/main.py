# Inputs
# 1 report per line, which are "levels" (ints) separated by spaces. Eg:
    # 7 6 4 2 1
    # 1 2 7 8 9
    # 9 7 6 2 1
    # 1 3 2 4 5
    # 8 6 4 4 1
    # 1 3 6 7 9

# Data manipulation
# In order for a report to be "safe", the levels must:
# - Be all increasing or all decreasing
# - Any two adjacent levels differ by at least one and at most 3

# Output
# How many reports are safe? Sum safe reports

def get_data():
    if TEST:    
        with open("test_data.txt", 'r') as file:
            data = file.readlines()
    else:
        with open("data.txt", 'r') as file:
            data = file.readlines()
    return data

def check_increasing(report: list) -> bool:
    for level in report[0:-1]:
        a: int = report[report.index(level)]
        b: int = report[report.index(level)+1]
        if a < b:
            continue
        else:
            return False
    return True

def check_decreasing(report: list) -> bool:
    for level in report[0:-1]:
        a: int = report[report.index(level)]
        b: int = report[report.index(level)+1]
        if a > b:
            continue
        else:
            return False
    return True

def check_adjacent(report: list) -> bool:
    for level in report[0:-1]:
        a: int = report[report.index(level)]
        b: int = report[report.index(level)+1]
        if abs(a-b) >= 1 and abs(a-b) <= 3:
            continue
        else:
            return False
    return True
    

def determine_safe(report: list) -> int:
    """Determines if report is safe

    Args:
        report (list): array of levels

    Returns:
        int: 1 if safe, 0 if not safe
    """
    if check_increasing(report) and check_adjacent(report):
        return 1
    elif check_decreasing(report) and check_adjacent(report):
        return 1
    else:
        return 0

PART_TWO = True
DEBUG = True
TEST = False
  
if __name__ == "__main__":
    data = get_data()
    sum: int = 0
    for row in data:
        report = row.split(" ")
        report = [int(item) for item in report]
        if PART_TWO:
            problem_dampener = determine_safe(report)
            if problem_dampener == 1:
                sum += 1
            else:
                if DEBUG:
                    print("-"*30)
                    print(f"starting report: {report}")
                    print(f"problem dampener with starting report: {problem_dampener}")
                for i, level in enumerate(report):
                    temp_report = report.copy()
                    temp_report.pop(i)
                    problem_dampener = problem_dampener + determine_safe(temp_report)
                    if DEBUG:
                        print("-"*10)
                        print(f"report iteration: {i}\n{temp_report}")
                        print(f"problem_dampener: {problem_dampener}")
                    if problem_dampener == 1:
                        sum += 1
                        break
                    del temp_report
        else:
            sum = sum + determine_safe(report)
    print(sum)