#!/usr/bin/env python3
"""Verify exhaustive forward and reverse enumeration against packaged tables."""
import csv
import json
import sys
from collections import Counter
from pathlib import Path


def main():
    if len(sys.argv) != 5:
        raise SystemExit('usage: check_outputs.py FORWARD.json REVERSE.txt JOINT.csv WORD.csv')
    forward = json.loads(Path(sys.argv[1]).read_text(encoding='utf8'))
    reverse_lines = Path(sys.argv[2]).read_text(encoding='utf8').splitlines()
    assert reverse_lines[0].startswith('classes 670608 nonreset 6928 peak 110592 peak_count 1 peak_length 30 ')
    assert reverse_lines[1] == 'joint_groups 648 count_groups 121'
    reverse = [tuple(map(int, line.split(','))) for line in reverse_lines[2:]]
    with open(sys.argv[3], newline='', encoding='utf8') as f:
        records = list(csv.DictReader(f))
    joint = sorted((int(r['reset_length']), int(r['shortest_word_count']),
                    int(r['rotation_classes'])) for r in records)
    assert len(joint) == 648
    assert joint == sorted(map(tuple, forward['joint']))
    assert joint == sorted(reverse)
    assert sum(c for _, _, c in joint) == 670608
    expected_words = Counter()
    expected_lengths = Counter()
    for length, words, classes in joint:
        expected_words[words] += classes
        expected_lengths[length] += classes
        assert (length == -1) == (words == 0)
    with open(sys.argv[4], newline='', encoding='utf8') as f:
        words = [(int(r['shortest_word_count']), int(r['rotation_classes']))
                 for r in csv.DictReader(f)]
    assert len(words) == 121
    assert words == sorted(expected_words.items())
    assert words == sorted(map(tuple, forward['multiplicities']))
    assert sorted(expected_lengths.items()) == sorted(map(tuple, forward['thresholds']))
    assert forward['classes'] == 670608
    assert forward['nonsync'] == 6928
    assert forward['max_words'] == 110592 and forward['max_count'] == 1
    assert forward['max_examples'] == ['12345120']
    assert forward['max_threshold'] == 36
    assert expected_words[1] == 388869
    assert joint[-1] == (36, 8, 1)
    assert (30, 110592, 1) in joint
    assert (35, 8, 1) in joint
    assert (29, 55296, 1) in joint
    def image_after(word, b):
        states = set(range(8))
        for ch in word:
            states = {((s + 1) % 8) if ch == 'a' else b[s] for s in states}
        return states
    witness_peak = 'baaaabaaabaaaaabaaaabaaaabaaab'
    witness_slow = 'baaaaabaaaabaaaaaabaaaaabaaaaabaaaab'
    assert len(witness_peak) == 30 and image_after(witness_peak, (1, 2, 3, 4, 5, 1, 2, 0)) == {1}
    assert len(witness_slow) == 36 and len(image_after(witness_slow, (0, 1, 2, 3, 4, 0, 1, 7))) == 1
    print('VERIFY_OK: 670608 classes, 648 joint cells, 121 multiplicities, unique 110592 peak')


if __name__ == '__main__':
    main()
