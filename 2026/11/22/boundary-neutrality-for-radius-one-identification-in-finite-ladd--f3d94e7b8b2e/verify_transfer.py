"""Exact integer min-plus certificate for identifying codes on finite two-row ladders.

Run: python3 verify_transfer.py. No external modules are required.
The program exhausts a fixed 256-state transition system, not all graph codes.
The accompanying mathematical proof establishes why that transition system is exact.
"""
from itertools import product
import json
from pathlib import Path

INF = 10**12
MASKS = range(4)
STATES = tuple(product(MASKS, repeat=4))
INDEX = {state: index for index, state in enumerate(STATES)}


def window_valid(n, centre, window):
    """Domination and pairs with leftmost column centre, in five-column window."""
    def fingerprint(col, row):
        present = set()
        for j, t in ((col, row), (col, 1-row), (col-1, row), (col+1, row)):
            if 0 <= j < n and (window[j-centre+1] & (1 << t)):
                present.add(2*j+t)
        return frozenset(present)
    for row in (0, 1):
        signature = fingerprint(centre, row)
        if not signature:
            return False
        for other_col in range(centre, min(n-1, centre+2)+1):
            for other_row in (0, 1):
                if (other_col, other_row) <= (centre, row):
                    continue
                if signature == fingerprint(other_col, other_row):
                    return False
    return True


def build_transitions():
    edges = []
    first = []
    final = []
    for s in STATES:
        first.append(sum(x.bit_count() for x in s)
                     if window_valid(4, 0, (0,) + s) else INF)
        edges.append(tuple((INDEX[s[1:]+(b,)], b.bit_count())
                           for b in MASKS if window_valid(5, 1, s+(b,))))
        t = s
        permitted = True
        for next_col in (8, 9, 10):
            centre = next_col-3
            q = t+(0,)
            if not window_valid(8, centre, q):
                permitted = False
                break
            t = q[1:]
        final.append(permitted)
    return first, edges, final


def transition(vec, edges):
    out = [INF] * 256
    for start, cost in enumerate(vec):
        if cost == INF:
            continue
        for finish, weight in edges[start]:
            out[finish] = min(out[finish], cost+weight)
    return out


def calculate():
    initial, edges, terminal = build_transitions()
    assert len(initial) == len(edges) == len(terminal) == 256
    vectors = {4: initial}
    for n in range(5, 21):
        vectors[n] = transition(vectors[n-1], edges)
    assert all(vectors[6][i] == 3 + int(state[0] == 3) + sum(x.bit_count() for x in state[1:])
               for i, state in enumerate(STATES))
    assert all(x < INF for x in vectors[6])
    assert all(x < INF for x in vectors[13])
    assert all(vectors[13][i] == vectors[6][i]+6 for i in range(256)), (
        'The required 256-component min-plus identity failed')
    # Repeat periodicity as an optional consequence test, not a substitute for proof.
    for n in range(6, 14):
        assert all(vectors[n+7][i] == vectors[n][i]+6 for i in range(256))
    observed = {n: min(v for v, accepted in zip(vec, terminal) if accepted)
                for n, vec in vectors.items()}
    expected = {4:4, 5:5, 6:6, 7:6, 8:8, 9:9, 10:9, 11:10, 12:11,
                13:12, 14:12, 15:14, 16:15, 17:15, 18:16, 19:17, 20:18}
    assert observed == expected, (observed, expected)
    certificate_path = Path(__file__).with_name("certificate.json")
    data = json.loads(certificate_path.read_text(encoding="utf-8"))
    assert data["v6"] == vectors[6] and data["v13"] == vectors[13]
    assert data["terminal"] == terminal
    assert data["base_optima"] == {str(n): observed[n] for n in range(6,13)}
    return vectors, observed, edges, terminal


if __name__ == '__main__':
    v, optima, edges, terminal = calculate()
    print('VERIFY_OK')
    print('state_count=256 transitions=%d terminal_states=%d' %
          (sum(map(len, edges)), sum(terminal)))
    print('v_6=', v[6])
    print('v_13=', v[13])
    print('minima=', optima)
    print('periodic_minplus_identity=v_13=v_6+6 componentwise')
