from task1 import filter_strings
from task2 import first_non_repeating_letter
from task3 import digital_root
from task4 import count_pairs
from task5 import meeting
from task6 import nextBigger
from task7 import int32_to_ip

# Task 1
assert filter_strings(['hello', 123, 'world', True, '']) == [123], "Test case 1 failed"
assert filter_strings([]) == [], "Test case 2 failed"
assert filter_strings(['a', 'b', 'c']) == [], "Test case 3 failed"

# Task 2
def test_first_non_repeating_letter():
    assert first_non_repeating_letter("stress") == "t", "Test case 1 failed"
    assert first_non_repeating_letter("aaabbbccc") == "", "Test case 2 failed"
    assert first_non_repeating_letter("sTreSS") == "T", "Test case 3 failed"

# Task 3
assert digital_root(0) == 0, "Test case 1 failed"
assert digital_root(12345) == 6, "Test case 2 failed"
assert digital_root(987654321) == 9, "Test case 3 failed"

# Task 4
assert count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 5) == 4
assert count_pairs([1, 2, 3, 4, 5], 7) == 2
assert count_pairs([1, 2, 3, 4, 5], 10) == 0

# Task 5
assert meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull") == "(CORWILL, FRED)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)", "Test case 1 failed"
assert meeting("Bobby:Jones;Alice:Jones") == "(JONES, ALICE)(JONES, BOBBY)", "Test case 2 failed"
assert meeting("Andrew:Smith;John:Smith;Paul:Brown;David:Brown") == "(BROWN, DAVID)(BROWN, PAUL)(SMITH, ANDREW)(SMITH, JOHN)", "Test case 3 failed"

# Task 6
assert nextBigger(12) == 21
assert nextBigger(513) == 531
assert nextBigger(2017) == 2071
assert nextBigger(9) == -1
assert nextBigger(111) == -1
assert nextBigger(531) == -1

# Task 7
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(32) == "0.0.0.32"
assert int32_to_ip(0) == "0.0.0.0"
