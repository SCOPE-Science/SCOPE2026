#!/usr/bin/env python3
"""Independent set-based evaluation of one-letter bilateral team meanings."""
V=(0,1)
teams=(frozenset(),frozenset({0}),frozenset({1}),frozenset({0,1}))
def U(bits):
    return frozenset(t for i,t in enumerate(teams) if bits & (1 << i))
def code(fam):
    return sum(1 << i for i,t in enumerate(teams) if t in fam)
def mpair(f,g):return code(f),code(g)
atoms={
mpair(frozenset({frozenset()}),frozenset(teams)),
mpair(frozenset(t for t in teams if t),frozenset({frozenset()})),
mpair(frozenset(t for t in teams if all(v==1 for v in t)),frozenset(t for t in teams if all(v==0 for v in t)))
}
def fuse(x,y):
    return frozenset(a|b for a in x for b in y)
def op_neg(t):return (t[1],t[0])
def op_and(t,s):
    return mpair(U(t[0]) & U(s[0]),fuse(U(t[1]),U(s[1])))
def op_or(t,s):
    return mpair(fuse(U(t[0]),U(s[0])),U(t[1]) & U(s[1]))
def op_diamond(t):
    return mpair(frozenset(T for T in teams if any(S and S<=T for S in U(t[0]))),U(t[1]))
def close(S):
    S=set(S)
    while True:
        T=set(S)
        T.update(op_neg(t) for t in S)
        for t in S:
            for u in S:
                T.add(op_and(t,u))
                T.add(op_or(t,u))
        if T==S:return T
        S=T
S=close(atoms)
assert len(S)==39
sizes=[len(S)]
for _ in range(3):
    S=close(S|{op_diamond(t) for t in S})
    sizes.append(len(S))
assert sizes==[39,64,66,66],sizes
assert sum(1 for t in S if t==(10,12))==1
print("INDEPENDENT_SET_SEMANTICS_OK", sizes)
