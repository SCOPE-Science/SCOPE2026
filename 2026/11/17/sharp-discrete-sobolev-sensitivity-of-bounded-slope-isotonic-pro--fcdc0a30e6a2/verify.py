"""Exact-rational checks for discrete-gradient stability of bounded-slope regression.
Standard library only. Finite calculations corroborate, but do not replace, the proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def partitions(n):
    for mask in range(1 << (n - 1)):
        blocks = []
        start = 0
        for j in range(n - 1):
            if mask & (1 << j):
                blocks.append(tuple(range(start, j + 1)))
                start = j + 1
        blocks.append(tuple(range(start, n)))
        yield blocks


def edge_matrix(blocks, n):
    # Difference of consecutive block means as a function of the n-1 original differences.
    rows = []
    for left, right in zip(blocks, blocks[1:]):
        rows.append(tuple(
            sum((F(i > j, len(right)) for i in right), F(0)) -
            sum((F(i > j, len(left)) for i in left), F(0))
            for j in range(n - 1)))
    return rows


def grad_energy(x):
    return sum(((b-a)**2 for a,b in zip(x,x[1:])), F(0))


def cap_projection(x,caps):
    n=len(x)
    for states in product((0,1,2),repeat=n-1):
        # States: 0 lower equality, 1 slack, 2 upper equality.
        if any(z==2 and caps[i] is None for i,z in enumerate(states)): continue
        y=[None]*n
        groups=[]
        start=0
        for i,z in enumerate(states):
            if z==1:
                groups.append((start,i));start=i+1
        groups.append((start,n-1))
        for a,b in groups:
            offsets={a:F(0)}
            for i in range(a,b):
                offsets[i+1]=offsets[i]+(F(0) if states[i]==0 else caps[i])
            level=sum((x[i]-offsets[i] for i in range(a,b+1)),F(0))/(b-a+1)
            for i in range(a,b+1):y[i]=level+offsets[i]
        feasible=True
        for i in range(n-1):
            d=y[i+1]-y[i]
            if d<0 or (caps[i] is not None and d>caps[i]):feasible=False;break
        if not feasible:continue
        for a,b in groups:
            residue=F(0)
            for i in range(a,b):
                residue+=x[i]-y[i]
                if states[i]==0 and residue<0: feasible=False;break
                if states[i]==2 and residue>0: feasible=False;break
            if not feasible:break
        if feasible:return tuple(y)
    raise AssertionError(('QP KKT enumeration failed', x,caps))


def run():
    cut_count=0
    for n in range(2,11):
        target = F(1) if n==2 else (F(5,4) if n==3 else (F(14,9) if n==4 else F(n-1,2)))
        for blocks in partitions(n):
            rows=edge_matrix(blocks,n)
            m=len(blocks)
            if m==1:continue
            assert all(z>=0 for row in rows for z in row)
            colmax=max((sum(row[j] for row in rows) for j in range(n-1)),default=F(0))
            assert colmax<=1
            if m>=3:
                assert all(sum(row)==F(len(a)+len(b),2) for row,a,b in zip(rows,blocks,blocks[1:]))
                assert max(sum(row) for row in rows)*colmax<=target
            else:
                a,b=map(len,blocks)
                squared=sum(z*z for z in rows[0])
                assert squared == F(n,3)+(F(1,a)+F(1,b))/6
                assert squared<=target
            cut_count+=1
        # Exact equality from an attainable locally pooled partition.
        if n==2: blocks=[(0,),(1,)]; d=tuple(F(1) for _ in range(n-1))
        elif n in (3,4):
            blocks=[(0,),tuple(range(1,n))]
            d=edge_matrix(blocks,n)[0]
        else:
            blocks=[(0,),tuple(range(1,n-1)),(n-1,)]
            d=tuple(F(1) for _ in range(n-1))
        rows=edge_matrix(blocks,n)
        assert sum((sum(a*b for a,b in zip(row,d))**2 for row in rows),F(0)) == target*sum((v*v for v in d),F(0))
    print('EXACT_ALL_COMPOSITIONS_GRADIENT_ESTIMATES_PASSED',cut_count)
    rng=Random(63129)
    qps=0;pairs=0
    for n in range(2,7):
        for _ in range(40):
            caps=tuple((F(rng.randint(1,4)) if rng.randrange(3) else None) for _ in range(n-1))
            x=tuple(F(rng.randint(-7,7)) for _ in range(n))
            y=cap_projection(x,caps)
            z=tuple(x[i]+F(rng.randint(-4,4),3) for i in range(n))
            w=cap_projection(z,caps)
            target = F(1) if n==2 else (F(5,4) if n==3 else (F(14,9) if n==4 else F(n-1,2)))
            assert grad_energy(tuple(yi-wi for yi,wi in zip(y,w))) <= target*grad_energy(tuple(xi-zi for xi,zi in zip(x,z)))
            qps+=2;pairs+=1
    print('EXACT_ACTIVE_SET_KKT_PROJECTIONS_PASSED',qps)
    print('EXACT_NONLINEAR_TWO_INPUT_BOUNDS_PASSED',pairs)
    for n in range(2,35):
        cap=F(3)
        if n==2: blocks=[(0,),(1,)]; d=(F(1),)
        elif n<=4: blocks=[(0,),tuple(range(1,n))];d=edge_matrix(blocks,n)[0]
        else: blocks=[(0,),tuple(range(1,n-1)),(n-1,)];d=(F(1),)*(n-1)
        y=[F(0)]*n; c=F(1)
        for b in blocks[1:]:
            for i in b:y[i]=c
            c+=1
        # Select strictly positive Lagrange multipliers on pooled edges.
        x=y[:]
        for block in blocks:
            for i in block[:-1]:
                x[i]+=F(1,20)
                x[i+1]-=F(1,20)
        h=[F(0)]
        for v in d:h.append(h[-1]+v)
        tiny=F(1,10000*n)
        z=[xi+tiny*hi for xi,hi in zip(x,h)]
        # Explicitly verify strict feasibility and positive KKT multipliers for both points.
        assert all((F(0)<y[i+1]-y[i]<cap) if any(i==block[-1] for block in blocks[:-1]) else (y[i+1]==y[i]) for i in range(n-1))
        f=tuple(y)
        g=[]
        for block in blocks:
            shift=sum((h[i] for i in block),F(0))/len(block)
            g.extend(y[i]+tiny*shift for i in block)
        g=tuple(g)
        for xx,yy in [(x,f),(z,g)]:
            assert all(F(0)<=yy[i+1]-yy[i]<=cap for i in range(n-1))
            for block in blocks:
                r=F(0)
                for i in block[:-1]:
                    r+=xx[i]-yy[i]
                    assert r>0
                assert sum((xx[i]-yy[i] for i in block),F(0))==0
        t=F(1) if n==2 else F(5,4) if n==3 else F(14,9) if n==4 else F(n-1,2)
        assert grad_energy(tuple(a-b for a,b in zip(f,g))) == t*grad_energy(tuple(a-b for a,b in zip(x,z)))
    print('EXACT_STRICTLY_COMPLEMENTARY_TWO_INPUT_SHARPNESS_PASSED',33)
    print('ALL_BOUNDED_SLOPE_GRADIENT_CHECKS_PASSED')
if __name__=='__main__':run()
