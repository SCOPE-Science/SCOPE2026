"""Exact finite Boolean-relation certificate for the cyclic Rule 232 image count.

Run with Python 3.9+ and no external packages. The routine builds every reachable
Boolean relation; no precomputed transition tables are trusted.
"""

def multiply(a, b):
    """Composition of 4 by 4 Boolean relations stored as 16-bit integers."""
    out = 0
    for i in range(4):
        for j in range(4):
            if (a >> (4*i+j)) & 1:
                for k in range(4):
                    if (b >> (4*j+k)) & 1:
                        out |= 1 << (4*i+k)
    return out


def matrices():
    mats = [0, 0]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                source, target = 2*a+b, 2*b+c
                letter = int(a+b+c >= 2)
                mats[letter] |= 1 << (4*source+target)
    return mats


def certificate():
    b0, b1 = matrices()
    assert (b0, b1) == (323, 49792)
    ident = sum(1 << (5*i) for i in range(4))
    states, indices, transitions = [ident], {ident:0}, []
    for state in states:
        outgoing = []
        for mat in (b0, b1):
            nxt = multiply(state, mat)
            if nxt not in indices:
                indices[nxt] = len(states)
                states.append(nxt)
            outgoing.append(indices[nxt])
        transitions.append(tuple(outgoing))
    assert len(states) == 120
    assert len(transitions) == 120
    assert len(set(states)) == len(states)
    diag_mask = ident
    accept = [int(bool(s & diag_mask)) for s in states]
    assert sum(accept) == 75
    # Acting on column vectors, (T v)_j = v_{delta(j,0)}+v_{delta(j,1)}.
    def apply(v):
        return [v[x] + v[y] for x,y in transitions]
    v = [accept]
    for _ in range(10):
        v.append(apply(v[-1]))
    # P(T) v_0, with P(X)=X^10-2 X^9+2 X^7-2 X^6
    # -2 X^5+3 X^4-2 X^2+1. Exact sparse obstruction.
    coeff = [1,-2,0,2,-2,-2,3,0,-2,0,1]
    defect = [sum(coeff[j] * v[10-j][i] for j in range(11))
              for i in range(len(states))]
    assert defect == [-9] + [0] * 119
    assert apply(defect) == [0] * 120
    first = [v[n][0] for n in range(1,11)]
    assert first == [2,4,2,8,22,34,58,96,182,334]
    # The logarithmic derivative of D reproduces these initial values.
    d = [1,-2,0,2,-2,-2,3,0,-2,0,1]
    a = [0] * 11
    for n in range(1,11):
        numerator = -n*d[n]
        a[n] = numerator - sum(d[j]*a[n-j] for j in range(1,n+1))
    assert a[1:] == first
    # Therefore sum_{n>=1} a_n z^n=-z D'(z)/D(z) for every n.
    return states, transitions, accept, first


if __name__ == '__main__':
    st, tr, ac, first = certificate()
    print('TRANSFER_CERTIFICATE_PASS states=%d accept=%d first=%s' %
          (len(st), sum(ac), first))
