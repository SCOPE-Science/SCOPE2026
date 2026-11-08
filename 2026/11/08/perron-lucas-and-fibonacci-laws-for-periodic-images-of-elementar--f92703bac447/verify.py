"""Exact integer certificate for one-step cyclic Rule 126 image counts.
Run with Python 3, standard library only.
"""
from collections import Counter

RULE = 126
# D(z) coefficients (constant to degree eleven), Q(0)=1.
Q = (1, -4, 6, -5, 1, 5, -7, 6, -2, -1, 1, -1)
# H(z) numerator, constant to degree twelve.
P = (1, -3, 4, -5, 6, -4, 1, -2, 2, -1, 1, 1, 1)

def relations():
    result=[]
    for label in (0,1):
        rows=[0]*4
        for a in (0,1):
            for b in (0,1):
                for c in (0,1):
                    if ((RULE>>(4*a+2*b+c))&1)==label:
                        rows[2*a+b] |= 1<<(2*b+c)
        result.append(tuple(rows))
    return tuple(result)

def compose(a,b):
    out=[]
    for mask in a:
        newmask=0
        for j in range(4):
            if mask>>j&1:
                newmask |= b[j]
        out.append(newmask)
    return tuple(out)

def closure():
    gens=relations()
    eye=(1,2,4,8)
    states=[eye]; ids={eye:0}; edges=[]
    for s in states:
        row=[]
        for gen in gens:
            t=compose(s,gen)
            if t not in ids:
                ids[t]=len(states);states.append(t)
            row.append(ids[t])
        edges.append(tuple(row))
    assert len(states)==45 and len(edges)==45
    return states,edges

def mat_apply(vec,edges):
    return [vec[a]+vec[b] for a,b in edges]

def brute(n):
    result=set()
    for x in range(1<<n):
        y=0
        for i in range(n):
            a=(x>>((i-1)%n))&1
            b=(x>>i)&1
            c=(x>>((i+1)%n))&1
            y |= ((RULE>>(4*a+2*b+c))&1)<<i
        result.add(y)
    return len(result)

def main():
    states,edges=closure()
    accept=[int(any((s[j]>>j)&1 for j in range(4))) for s in states]
    values=[accept]
    for _ in range(15):
        values.append(mat_apply(values[-1],edges))
    w=[sum(Q[j]*values[11-j][k] for j in range(12)) for k in range(45)]
    # Complete 45-coordinate integer certificate. This establishes
    # every coefficient beyond degree twelve is zero, without
    # extrapolation from a finite initial sequence.
    assert [(k,v) for k,v in enumerate(w) if v] == [(0,1),(2,1)]
    assert [(k,v) for k,v in enumerate(mat_apply(w,edges)) if v] == [(0,1)]
    assert mat_apply(mat_apply(w,edges),edges)==[0]*45
    a=[v[0] for v in values[:13]]
    assert a[:12]==[1,1,2,2,6,12,23,37,66,119,217,387]
    pp=[sum(Q[j]*a[n-j] for j in range(min(n,11)+1)) for n in range(13)]
    assert pp==list(P),(pp,P)
    for n in range(1,13):
        assert brute(n)==a[n],(n,brute(n),a[n])
    # Independent evaluation of the rational recurrence against transfers.
    for n in range(13,80):
        a.append(-sum(Q[j]*a[n-j] for j in range(1,12)))
    v=values[0]
    for n in range(80):
        assert v[0]==a[n],n
        v=mat_apply(v,edges)
    assert (a[12],a[16],a[20]) == (693,6986,69161)
    print('VERIFY_OK states=45, vector_annihilation=M^2, brute=1..12, recurrence=0..79')

if __name__=='__main__':
    main()
