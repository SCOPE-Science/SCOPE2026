"""Independent cyclic-Fano construction and rational Gaussian rank check."""
import math


def rank_exact(rows):
    rows = [dict(row) for row in rows]
    ncol = 232
    r = 0
    for j in range(ncol):
        k = next((k for k in range(r, len(rows)) if j in rows[k]), None)
        if k is None:
            continue
        rows[r], rows[k] = rows[k], rows[r]
        a = rows[r][j]
        for k in range(r + 1, len(rows)):
            b = rows[k].get(j, 0)
            if not b:
                continue
            g = math.gcd(a, b)
            u, v = a//g, b//g
            new = {i: u*x for i,x in rows[k].items() if i != j}
            for i,x in rows[r].items():
                if i == j: continue
                y = new.get(i,0)-v*x
                if y: new[i]=y
                else: new.pop(i,None)
            if new:
                gg = 0
                for x in new.values():gg=math.gcd(gg,x)
                if gg>1:new={i:x//gg for i,x in new.items()}
            rows[k]=new
        r+=1
        if r == len(rows):break
    return r


def main():
    # A cyclic difference-set representation of the Fano plane,
    # inequivalent as a labeling to the binary-coordinate verifier.
    line_sets = [{(j+k)%7 for k in (0,1,3)} for j in range(7)]
    nbr=[0]*14
    for j,L in enumerate(line_sets):
        for i in L:
            nbr[i]|=1<<(7+j)
            nbr[7+j]|=1<<i
    allowed=[]
    for mask in range(1<<14):
        if all(not ((mask>>i)&1) or not(mask&nbr[i]) for i in range(14)):
            allowed.append(mask)
    evens=[s for s in allowed if s.bit_count()%2==0]
    odds=[s for s in allowed if s.bit_count()%2]
    assert len(allowed)==458 and len(evens)==232 and len(odds)==226
    E={s:i for i,s in enumerate(evens)}
    for t, expected in [(0,155),(1,216),(2,225),(-1,216),(-2,225)]:
        rows=[]
        for s in odds:
            row={}
            for j in range(14):
                ss=s^(1<<j)
                if ss in E:
                    weight=t if j<7 else 1
                    if weight:row[E[ss]]=weight
            rows.append(row)
        r=rank_exact(rows)
        assert r==expected, (t,r,expected)
    print('PASS: independent graph construction and exact ranks at 0, +/-1, +/-2')

if __name__=='__main__': main()
