"""Exact finite FO2-type refinement on once-marked directed cycles.

No external dependencies. For every rank, finite partitions encode all Boolean
combinations of first-order formulas with at most x,y free, including quantifiers.
They provide exhaustive finite tests but do not prove unbounded ranks or sizes.
"""

def flatten_compact(rows):
    palette = {}
    result = []
    for row in rows:
        new = []
        for item in row:
            if item not in palette:
                palette[item] = len(palette)
            new.append(palette[item])
        result.append(new)
    return result


def ranks(max_n=20, max_rank=7):
    zero = [0] * max_n
    one_x = flatten_compact([[(a == 0,) for a in range(n)] for n in range(1, max_n+1)])
    one_y = flatten_compact([[(a == 0,) for a in range(n)] for n in range(1, max_n+1)])
    pair = flatten_compact([[(a == 0, b == 0, a == b, b == (a+1)%n, a == (b+1)%n)
                             for a in range(n) for b in range(n)] for n in range(1,max_n+1)])
    out = []
    for q in range(max_rank+1):
        groups = {}
        for n, cls in enumerate(zero, 1):
            groups.setdefault(cls, []).append(n)
        out.append(list(groups.values()))
        if q == max_rank:
            break
        zero_new = []
        x_new = []
        y_new = []
        both_new = []
        for j in range(max_n):
            n=j+1
            u=one_x[j]; v=one_y[j]; p=pair[j]
            zero_new.append((zero[j],tuple(sorted(set(u))),tuple(sorted(set(v)))))
            x_new.append([(u[a],tuple(sorted({p[a*n+b] for b in range(n)})),
                           tuple(sorted(set(u)))) for a in range(n)])
            y_new.append([(v[b],tuple(sorted({p[a*n+b] for a in range(n)})),
                           tuple(sorted(set(v)))) for b in range(n)])
            both_new.append([(p[a*n+b],
                              tuple(sorted({p[t*n+b] for t in range(n)})),
                              tuple(sorted({p[a*n+t] for t in range(n)})))
                             for a in range(n) for b in range(n)])
        zero = flatten_compact([[v] for v in zero_new]);zero=[v[0] for v in zero]
        one_x = flatten_compact(x_new)
        one_y = flatten_compact(y_new)
        pair = flatten_compact(both_new)
    return out


def ball(n, r):
    return {(d % n) for d in range(-r,r+1)}

def cutoff(n, k):
    # Evaluate the explicit rank-bounded formulas of the proof on C_n.
    if k==1: return n==1
    if k==2: return all(((b==(a+1)%n)==(a==(b+1)%n)) for a in range(n) for b in range(n))
    if k%2==1:
        r=(k-1)//2
        return len(ball(n,r)) == n
    r=(k-4)//2
    b=ball(n,r)
    return any(len(b | {(x-1)%n,x,(x+1)%n})==n for x in range(n))


def main():
    nmax=20
    Q=7
    results=ranks(nmax,Q)
    for q, groups in enumerate(results):
        if q==0: expected=[list(range(1,nmax+1))]
        elif q==1: expected=[[1],list(range(2,nmax+1))]
        else: expected=[[n] for n in range(1,min(2*q,nmax)+1)] + ([list(range(2*q+1,nmax+1))] if 2*q<nmax else [])
        assert groups==expected,(q,groups,expected)
        print(f'FO2 exact type-refinement rank {q}: {len(groups)} classes; PASS')
    for k in range(1,15):
        for n in range(1,35):
            assert cutoff(n,k) == (n<=k),(k,n)
    print('Explicit threshold formulas, cutoffs k=1..14, cycles n=1..34: PASS')

if __name__=='__main__': main()
