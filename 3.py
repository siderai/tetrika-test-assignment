from operator import itemgetter
from typing import Dict, List, Tuple


IntervalsList = List[Tuple[int, int]]


def appearance(intervals: Dict[str, List[int]]) -> int:
    """Принимает на вход словарь с сессиями ученика, учителя а также временными рамками урока.
    Сессии представлены в виде списка чисел, где под четными индексами - время начала сессии,
    а под нечетными - время ее завершения. Возвращает общее время в секундах, когда учитель и ученик
    вместе присутствовали на уроке."""
    p_data, t_data, l_data = intervals["pupil"], intervals["tutor"], intervals["lesson"]
    pupil_periods = list(zip(p_data[0::2], p_data[1::2]))
    tutor_periods = list(zip(t_data[0::2], t_data[1::2]))
    lesson_period = list(zip(l_data[0::2], l_data[1::2]))

    pupil_and_tutor = _find_common_intervals(pupil_periods, tutor_periods)

    pupil_and_tutor_during_lesson = _find_common_intervals(
        pupil_and_tutor, lesson_period
    )

    pure_common_intervals = _remove_duplicates(pupil_and_tutor_during_lesson)

    productive_time = 0
    for period in pure_common_intervals:
        productive_time += period[1] - period[0]
    return productive_time


def _remove_duplicates(common_periods: IntervalsList) -> IntervalsList:
    periods = sorted(common_periods, key=itemgetter(0))
    i = 0
    while i < len(periods) - 1:
        a, b = periods[i], periods[i + 1]
        if _do_intersect(a, b):
            periods[i] = (min(a[0], b[0]), max(a[1], b[1]))
            periods.pop(i + 1)
        else:
            i += 1
    return periods


def _find_common_intervals(
    first: IntervalsList, second: IntervalsList
) -> IntervalsList:
    common_intervals: IntervalsList = []
    for period1 in first:
        for period2 in second:
            if _do_intersect(period1, period2):
                common_intervals.append(
                    (max(period1[0], period2[0]), min(period1[1], period2[1]))
                )
    return common_intervals


def _do_intersect(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    start_a, start_b, end_a, end_b = a[0], b[0], a[1], b[1]
    if start_a <= start_b or (start_b < start_a <= end_b):
        if end_b <= end_a or (start_b < end_a <= end_b):
            return True
    return False


tests = [
    {
        "data": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "data": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "data": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]


if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["data"])
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
        print(f"Testcase {i} passed")
