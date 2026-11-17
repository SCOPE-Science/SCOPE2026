"""Exact Boolean-relation monoid certificate for sequential Rule 30."""

ZERO = (1, 0, 0, 0)  # a OR b = 0
ONE = (0, 1, 1, 1)   # a OR b = 1
IDENTITY = (1, 0, 0, 1)


def boolean_comp(A, B):
    return tuple(int(any(A[2*i+k] and B[2*k+j] for k in range(2)))
                 for i in range(2) for j in range(2))


def score(P):
    a = P[0]
    b = int(bool(P[1] or P[3]))
    c = int(bool(P[0] or P[1] or P[2]))
    return a+b+c


def mv(T, v):
    return tuple(sum(v[j] for j in dest) for dest in T)


def sub(*vv):
    return tuple(vv[0][i]-2*vv[1][i]+vv[2][i]-vv[3][i]
                 for i in range(len(vv[0])))


def main():
    states = [IDENTITY]
    pos = {IDENTITY: 0}
    for state in states:
        for E in (ZERO, ONE):
            target = boolean_comp(state, E)
            if target not in pos:
                pos[target] = len(states)
                states.append(target)
    assert len(states) == 12
    T = [tuple(pos[boolean_comp(P, E)] for E in (ZERO, ONE)) for P in states]
    v0 = tuple(score(P) for P in states)
    v1, v2, v3 = mv(T,v0), None, None
    v2 = mv(T,v1)
    v3 = mv(T,v2)
    # Matrix identity T^2 * (T^3 - 2 T^2 + T - I) v = 0.
    cert = sub(mv(T,mv(T,mv(T,v2))), mv(T,mv(T,v2)), mv(T,v2), v2)
    assert cert == (0,)*12, cert
    m_values = []
    v = v0
    for m in range(91):
        m_values.append(v[0])
        v = mv(T,v)
    assert m_values[:7] == [3,4,8,14,25,44,77]
    for m in range(2, 88):
        assert m_values[m+3] == 2*m_values[m+2]-m_values[m+1]+m_values[m]
    for i, (state, (a,b)) in enumerate(zip(states,T)):
        print(f'{i:02d} {"".join(map(str,state))} -> ({a:02d},{b:02d}), weight={score(state)}')
    print('coefficient list n=3..22:',m_values[1:21])
    print('matrix certificate T^2(T^3-2T^2+T-I)w=0: PASS')
    print('rational generating function z^3(4+2z^2+z^3)/(1-2z+z^2-z^3): PASS')

if __name__ == '__main__':
    main()
