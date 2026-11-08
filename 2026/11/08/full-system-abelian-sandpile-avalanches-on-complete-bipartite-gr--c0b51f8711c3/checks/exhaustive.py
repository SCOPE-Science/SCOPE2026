"""Independent exact finite enumeration for a rooted complete-bipartite sandpile.
Run with python3 checks/exhaustive.py. Standard library only.
"""
from fractions import Fraction
from itertools import product


def graph(a,b):
    # vertices A[0..a-2], B[0..b-1], the deleted A vertex is the sink.
    m=a-1; n=m+b
    neighbors=[list(range(m,n)) for _ in range(m)]
    neighbors += [list(range(m)) for _ in range(b)]
    deg=[b]*m+[a]*b
    return neighbors,deg


def recurrent_fsc(h,neighbors):
    # Dhar's forbidden-subconfiguration test, NOT the stabilization test.
    n=len(h)
    for mask in range(1,1<<n):
        witness=False
        for v in range(n):
            if mask>>v & 1:
                interior=sum((mask>>w)&1 for w in neighbors[v])
                if h[v]>=interior:
                    witness=True
                    break
        if not witness:
            return False
    return True


def stabilize(x,neighbors,degree):
    x=list(x); top=[0]*len(x)
    while True:
        # Reverse vertex priority, independent of a standard forward queue.
        unstable=next((v for v in range(len(x)-1,-1,-1)
                       if x[v]>=degree[v]),None)
        if unstable is None:
            return tuple(x),tuple(top)
        x[unstable]-=degree[unstable];top[unstable]+=1
        for j in neighbors[unstable]:x[j]+=1


def run(a,b):
    N=a+b-1; nbr,deg=graph(a,b); t=a-1
    rec=0; mx=0; sum_top=0; max_number=0
    for h in product(*(range(d) for d in deg)):
        if not recurrent_fsc(h,nbr):
            continue
        rec+=1
        x=list(h);x[t]+=1
        _,top=stabilize(x,nbr,deg)
        total=sum(top);sum_top+=total
        assert max(top)<=1
        if total>mx:
            mx=total; max_number=1
        elif total==mx:
            max_number+=1
    expected_rec=a**(b-1)*b**(a-1)
    expected_max=b**(a-2)*(a-1)**(b-1)
    expected_mean=Fraction(a+b-1,b)
    assert rec==expected_rec,(a,b,'rec',rec,expected_rec)
    assert mx==N,(a,b,'max',mx,N)
    assert max_number==expected_max,(a,b,'count',max_number,expected_max)
    assert Fraction(sum_top,rec)==expected_mean,(a,b,'mean',Fraction(sum_top,rec),expected_mean)
    return a,b,rec,max_number,expected_mean


if __name__=='__main__':
    tests=[(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,3)]
    for a,b in tests:
        print('PASS',run(a,b))
    print('EXHAUSTIVE_FSC_OK',len(tests))
