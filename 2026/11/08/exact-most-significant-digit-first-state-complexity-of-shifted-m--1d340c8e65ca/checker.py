#!/usr/bin/env python3
"""Independent checks for exact MSDF shifted modular ruler-word complexity.
Only uses Python's standard library. No external files are required.
"""
from itertools import product
from random import Random


def valuation(x, base):
    assert x > 0 and base >= 2
    out = 0
    while x % base == 0:
        x //= base
        out += 1
    return out


def data(base, modulus, shift):
    """Finite formula: produce all output signatures and integer witnesses."""
    assert base >= 2 and modulus >= 2 and shift >= 0
    d = shift + 1
    q = [d]
    while q[-1] != 1:
        q.append((q[-1] + base - 1) // base)
    K = len(q) - 1
    H = 0 if K == 0 else 1 + max(valuation(abs(x-y), base) for x in q for y in q if x != y)
    # Trie nodes are low-order radix residues. For a node (depth,residue),
    # the represented q_i are those with -q_i == residue mod base**depth.
    missing = []
    frontier = [(0, 0, tuple(range(len(q))))]
    for depth in range(H):
        new_frontier = []
        for _, residue, ix in frontier:
            for digit in range(base):
                new_res = residue + digit * base ** depth
                matching = tuple(i for i in ix if (-q[i] - new_res) % (base ** (depth + 1)) == 0)
                if matching:
                    new_frontier.append((depth + 1, new_res, matching))
                else:
                    missing.append(new_res)
        frontier = new_frontier
    signatures = set()
    witnesses = {}
    for n in missing:
        sig = tuple(valuation(n + x, base) % modulus for x in q)
        signatures.add(sig)
        witnesses.setdefault(sig, n)
    # Every leaf has one exceptional coordinate with arbitrary valuation mod m.
    for i in range(len(q)):
        for target in range(modulus):
            vec = [valuation(abs(q[j]-q[i]), base) % modulus if j != i else target for j in range(len(q))]
            sig = tuple(vec)
            t = H
            while t % modulus != target or base ** t <= q[i]:
                t += 1
            n = base ** t - q[i]
            signatures.add(sig)
            witnesses.setdefault(sig, n)
    return signatures, witnesses, q, H, len(missing)


def direct_signature(n, q, base, modulus):
    return tuple(valuation(n + x, base) % modulus for x in q)


def moore_minimize(outputs, transitions):
    classes = outputs[:]
    while True:
        mapping = {}
        replacement = []
        for i, row in enumerate(transitions):
            signature = (outputs[i], tuple(classes[t] for t in row))
            if signature not in mapping:
                mapping[signature] = len(mapping)
            replacement.append(mapping[signature])
        if len(set(classes)) == len(mapping):
            return len(mapping)
        classes = replacement


def check():
    rng = Random(20261103)
    tests = 0
    witness_checks = 0
    direct_checks = 0
    minimizations = 0
    for base in range(2, 6):
        for modulus in range(2, 6):
            for shift in range(0, 56):
                formula, witnesses, q, H, missing = data(base, modulus, shift)
                assert len(formula) == len(witnesses)
                for sig, n in witnesses.items():
                    assert direct_signature(n, q, base, modulus) == sig
                    witness_checks += 1
                # Directly evaluate arbitrary numbers; those may be in very deep
                # congruence classes not sampled in the finite signature formula.
                candidates = list(range(80)) + [rng.randrange(0, 10**9) for _ in range(40)]
                for n in candidates:
                    assert direct_signature(n, q, base, modulus) in formula
                    direct_checks += 1
                # Construct an automaton independently: prefix integer n,
                # equivalent if its vector of residual outputs is identical.
                states = {direct_signature(0, q, base, modulus): 0}
                work = [(0, states.keys().__iter__().__next__())]
                trans = []
                outputs = []
                pos = 0
                while pos < len(work):
                    representative, signature = work[pos]
                    assert states[signature] == pos
                    outputs.append(signature[0])
                    row = []
                    for digit in range(base):
                        nxt = base * representative + digit
                        vs = direct_signature(nxt, q, base, modulus)
                        if vs not in states:
                            states[vs] = len(work)
                            work.append((nxt, vs))
                        row.append(states[vs])
                    trans.append(row)
                    pos += 1
                    assert pos <= len(formula)
                assert set(states) == formula, (base, modulus, shift, len(states), len(formula))
                assert moore_minimize(outputs, trans) == len(formula)
                minimizations += 1
                tests += 1
    print('VERIFY_OK')
    print('parameter_cases', tests)
    print('signature_witnesses', witness_checks)
    print('direct_arithmetic_checks', direct_checks)
    print('independent_automaton_minimizations', minimizations)

if __name__ == '__main__':
    check()
