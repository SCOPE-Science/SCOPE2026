#!/usr/bin/env python3
"""Exact finite-state certificate for the image of a single Rule-110 sweep.

Run with Python 3 (standard library only). The finite certificate proves the
all-length recurrence using Cayley--Hamilton, not extrapolation from data.
"""
import json
from collections import deque
from pathlib import Path

RULE = 110

def rule(left, middle, right):
    return (RULE >> (4 * left + 2 * middle + right)) & 1


def initial_state(first):
    mask = 0
    for last in (0, 1):
        for second in (0, 1):
            if any(rule(last, start, second) == first for start in (0, 1)):
                mask |= 1 << (2 * last + second)
    return (first, first, mask)


def extend(state, emitted):
    first, previous, mask = state
    nxt = 0
    for last in (0, 1):
        for current in (0, 1):
            if mask & (1 << (2 * last + current)):
                for following in (0, 1):
                    if rule(previous, current, following) == emitted:
                        nxt |= 1 << (2 * last + following)
    return (first, emitted, nxt)


def final_count(state):
    first, previous, mask = state
    choices = {rule(previous, last, first) for last in (0, 1)
               if mask & (1 << (2 * last + last))}
    return len(choices)


def build_table():
    initial = [initial_state(first) for first in (0, 1)]
    states = list(initial)
    seen = set(states)
    todo = deque(states)
    while todo:
        current = todo.popleft()
        for bit in (0, 1):
            following = extend(current, bit)
            if following not in seen:
                seen.add(following)
                states.append(following)
                todo.append(following)
    index = {state: i for i, state in enumerate(states)}
    table = {
        "local_rule": RULE,
        "state_encoding": "[first_output, preceding_output, four-bit mask of (last_old_bit, current_old_bit)]",
        "states": [list(state) for state in states],
        "initial_indices": [index[state] for state in initial],
        "next_on_0": [index[extend(state, 0)] for state in states],
        "next_on_1": [index[extend(state, 1)] for state in states],
        "terminal_weights": [final_count(state) for state in states],
    }
    return table


def row_times_transfer(row, table):
    result = [0] * len(row)
    for i, count in enumerate(row):
        if count:
            result[table["next_on_0"][i]] += count
            result[table["next_on_1"][i]] += count
    return result


def coefficients(table, limit):
    row = [0] * len(table["states"])
    for index in table["initial_indices"]:
        row[index] += 1
    values = []
    for _ in range(limit):
        values.append(sum(a * b for a, b in zip(row, table["terminal_weights"])))
        row = row_times_transfer(row, table)
    return values


def run():
    table = build_table()
    assert len(table["states"]) == 26
    path = Path(__file__).with_name("transfer_table.json")
    assert json.loads(path.read_text(encoding="utf-8")) == table, "Table differs from regenerated construction"
    # c_k counts n=k+2 output words (the theorem uses n>=3).
    c = coefficients(table, 31)
    assert c[:10] == [4, 5, 11, 20, 39, 75, 143, 274, 522, 996]
    # Q(z) = (1-z)(1-z-2z^2+z^4)
    q = [1, -2, -1, 2, 1, -1]
    # 26 consecutive residuals vanish. By Cayley--Hamilton on the 26-state
    # transition matrix, all later ones vanish as well.
    residuals = [sum(q[j] * c[k - j] for j in range(6)) for k in range(5, 31)]
    assert residuals == [0] * 26, residuals
    # The numerator of sum c_k z^k is
    # 4 - 3z - 3z^2 + z^3 + 2z^4, with Q as above.
    numerator = [sum(q[j] * c[k - j] for j in range(min(5, k) + 1))
                 for k in range(5)]
    assert numerator == [4, -3, -3, 1, 2], numerator
    # The 26-state matrix always satisfies its characteristic equation;
    # therefore the zero residuals for k=5..30 prove every k>=5.
    print("Rule 110 finite-state transfer: PASS")
    print("states:", len(table["states"]))
    print("initial indices:", table["initial_indices"])
    print("length-3..16 image counts:", c[1:15])
    print("Q coefficients:", q)
    print("numerator of c-series:", numerator)
    print("zero residual indices:", "k=5..30 inclusive")
    print("Cayley--Hamilton recurrence certified for all k>=5")
    print("generating function n>=3: z^3(5+z-7z^2-2z^3+4z^4)/((1-z)(1-z-2z^2+z^4))")

if __name__ == "__main__":
    run()
