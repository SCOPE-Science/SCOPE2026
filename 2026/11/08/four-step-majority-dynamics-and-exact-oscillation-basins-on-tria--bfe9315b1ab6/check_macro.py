"""Exact macrostate proof-check and integer multinomial audit for clique windmills.

Use: python3 check_macro.py. Each count-class is verified by a symbolic
transition on its four blade types and its exact combinatorial weight.
"""
from math import comb

def weight(r,z,o,p,q):
    return comb(r,z)*comb(r-z,o)*comb(r-z-o,p)*3**(p+q)

def update(count,h,r):
    z,o,p,q=count
    K=3*o+p+2*q
    next_h = int(2*K>3*r or (2*K==3*r and h==1))
    if h==0:
        return (z+p,o,q,0),next_h
    return (z,o+q,0,p),next_h

def classify_symbolic(r,count,h):
    # By the elementary blade truth table, macrotype transitions preserve
    # the identity of every occupied singleton position under a two-step return.
    states=[(count,h)]
    for j in range(7):
        c,h=states[-1];states.append(update(c,h,r))
    for i in range(5):
        if states[i]==states[i+1]:return i,1
        if states[i]==states[i+2]:return i,2
    raise AssertionError((r,count,h,states))

def formula_type(r,z,o,p,q):
    T=3*r
    K=2*(3*o+p+2*q)
    L=2*(3*o+q)
    U=2*(3*o+2*q)
    if K<=T:
        return (2,1) if q else ((1,1) if p else (0,1))
    if L>=T:
        return (3,1) if q else (1,1)
    if U>T:
        return (1,2) if p else (0,2)
    return (4,1) if q else (2,1)

def main():
    for r in range(1,61):
        classes={(t,per):0 for t in range(5) for per in (1,2)}
        fixed_formula=2*sum(comb(r,b) for b in range(r//2+1))
        cycles_formula=0;basin_formula=0
        for o in range(r+1):
            for q in range(r-o+1):
                if 2*(3*o+q)<3*r<2*(3*o+2*q):
                    c=comb(r,o)*comb(r-o,q)*3**q
                    cycles_formula+=c
                    basin_formula+=c*4**(r-o-q)
        for z in range(r+1):
            for o in range(r-z+1):
                for p in range(r-z-o+1):
                    q=r-z-o-p
                    counts=(z,o,p,q)
                    actual=classify_symbolic(r,counts,0)
                    expected=formula_type(r,*counts)
                    assert actual==expected,(r,counts,actual,expected)
                    classes[actual]+=2*weight(r,*counts)
        assert sum(classes.values())==2*8**r
        assert classes[(0,1)]==fixed_formula
        assert classes[(0,2)]==2*cycles_formula
        assert sum(classes[(t,2)] for t in range(5))==2*basin_formula
        assert all(classes[(t,2)]==0 for t in (2,3,4))
        maxdepth=max(t for t in range(5) for per in (1,2) if classes[(t,per)])
        assert maxdepth==(1 if r==1 else 3 if r==2 else 4)
        if r<=16 or r in (32,60):
            print(f'r={r} fixed={fixed_formula} primitive_2_cycles={cycles_formula} '
                  f'two_cycle_basin={2*basin_formula} max_entry={maxdepth} '
                  f'depth_period_counts='+ ';'.join(f'{t}:{classes[t,1]},{classes[t,2]}' for t in range(5)))
    print('MACRO_SYMBOLIC_PASS r=1..60')
if __name__=='__main__':main()
