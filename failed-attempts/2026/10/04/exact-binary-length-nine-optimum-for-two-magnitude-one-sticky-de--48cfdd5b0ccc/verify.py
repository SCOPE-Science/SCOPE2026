#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent


def runs(word):
    out = []
    start = 0
    for i in range(1, len(word) + 1):
        if i == len(word) or word[i] != word[start]:
            out.append((start, i, word[start]))
            start = i
    return out


def delete_one_from_runs(word, run_indices):
    rr = runs(word)
    chosen = set(run_indices)
    pieces = []
    for j, (a, b, bit) in enumerate(rr):
        length = b - a - (1 if j in chosen else 0)
        if length <= 0:
            raise AssertionError("a sticky deletion may not erase an entire run")
        pieces.append(bit * length)
    return ''.join(pieces)


def ball(word):
    rr = runs(word)
    eligible = [j for j, (a, b, _) in enumerate(rr) if b - a >= 2]
    out = {word}
    for k in (1, 2):
        for S in combinations(eligible, k):
            out.add(delete_one_from_runs(word, S))
    return out


def ball_by_positions(word):
    # Independent formulation: mark each original position by its maximal-run index,
    # choose at most one position from each of at most two runs, and delete them.
    rr = runs(word)
    run_of = [None] * len(word)
    eligible_runs = set()
    for j, (a, b, _) in enumerate(rr):
        for i in range(a, b):
            run_of[i] = j
        if b - a >= 2:
            eligible_runs.add(j)
    out = {word}
    eligible_positions = [i for i, j in enumerate(run_of) if j in eligible_runs]
    for k in (1, 2):
        for positions in combinations(eligible_positions, k):
            selected_runs = [run_of[i] for i in positions]
            if len(set(selected_runs)) != k:
                continue
            deleted = set(positions)
            y = ''.join(bit for i, bit in enumerate(word) if i not in deleted)
            out.add(y)
    return out


def load_code():
    words = [s.strip() for s in (ROOT / "artifacts" / "codewords.txt").read_text().splitlines() if s.strip()]
    assert len(words) == 120 and len(set(words)) == 120
    assert all(len(w) == 9 and set(w) <= {"0", "1"} for w in words)
    return words


def load_weights():
    weights = {}
    with (ROOT / "artifacts" / "weights.csv").open(newline='') as f:
        for row in csv.DictReader(f):
            w = row["word"]
            q = Fraction(row["weight"])
            assert w not in weights and len(w) in (7, 8, 9) and set(w) <= {"0", "1"}
            assert q >= 0
            weights[w] = q
    return weights


def main():
    code = load_code()
    weights = load_weights()

    # Cross-check the channel definition in two independent implementations on all sources.
    for bits in product("01", repeat=9):
        x = ''.join(bits)
        assert ball(x) == ball_by_positions(x), x

    # Direct lower certificate: the 120 listed source balls are pairwise disjoint.
    owner = {}
    union = set()
    for x in code:
        bx = ball(x)
        for y in bx:
            assert y not in owner, f"collision: {x} and {owner[y]} both reach {y}"
            owner[y] = x
        union |= bx
    assert len(owner) == len(union)

    # Exact rational upper certificate. Every length-nine source ball has weight >= 1.
    total_weight = sum(weights.values(), Fraction(0))
    assert total_weight == 120, total_weight
    ball_weights = {}
    for bits in product("01", repeat=9):
        x = ''.join(bits)
        s = sum((weights.get(y, Fraction(0)) for y in ball(x)), Fraction(0))
        assert s >= 1, (x, s)
        ball_weights[x] = s

    # Independent structural checks on the channel: outputs have lengths 7, 8, or 9,
    # and selecting two runs is possible only when two eligible runs exist.
    all_outputs = set()
    for bits in product("01", repeat=9):
        x = ''.join(bits)
        bx = ball(x)
        assert all(len(y) in (7, 8, 9) for y in bx)
        all_outputs |= bx

    tight = sum(1 for s in ball_weights.values() if s == 1)
    print(f"CODE_SIZE={len(code)}")
    print(f"CODE_BALL_UNION={len(union)}")
    print(f"NONZERO_WEIGHTS={len(weights)}")
    print(f"TOTAL_WEIGHT={total_weight}")
    print(f"MIN_BALL_WEIGHT={min(ball_weights.values())}")
    print(f"TIGHT_SOURCE_BALLS={tight}")
    print(f"MAX_BALL_WEIGHT={max(ball_weights.values())}")
    print("POSITION_CROSSCHECK=512")
    print(f"ALL_CHANNEL_OUTPUTS={len(all_outputs)}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
