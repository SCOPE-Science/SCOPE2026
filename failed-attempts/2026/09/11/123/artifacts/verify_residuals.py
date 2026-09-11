import sys
sys.setrecursionlimit(100000)
from compute_invariant import make_engine
_, call = make_engine(4)
print("target:", call(4,[4]*7), flush=True)

def wdvv(d, ins, ch):
    ia,ib,ic,idd = ch
    al,be,ga,de = ins[ia],ins[ib],ins[ic],ins[idd]
    S=[ins[i] for i in range(len(ins)) if i not in (ia,ib,ic,idd)]
    m=len(S); lhs=rhs=0
    for mask in range(1<<m):
        S1=[S[i] for i in range(m) if (mask>>i)&1]
        S2=[S[i] for i in range(m) if not (mask>>i)&1]
        for d1 in range(d+1):
            d2=d-d1
            for e in range(5):
                A=call(d1,[al,be]+S1+[e])
                if A: lhs+=A*call(d2,[4-e,ga,de]+S2)
                C=call(d1,[al,ga]+S1+[e])
                if C: rhs+=C*call(d2,[4-e,be,de]+S2)
    return lhs-rhs

# dimension-valid tuples only: sum == 1+5d+n
tests=[(4,[4]*7,(0,1,2,3)),(4,[4]*7,(0,1,5,6)),(4,[4]*7,(3,4,0,6)),
       (2,[4,4,3,3,2],(0,1,2,3)),(2,[4,4,3,3,2],(0,2,1,4)),
       (3,[4,4,4,4,3,3],(0,1,2,5)),(1,[4,2,2,2],(0,1,2,3)),
       (3,[4,4,4,3,3,3,2],(0,1,2,5))]
ok=0; n=0
for d,ins,ch in tests:
    assert sum(ins)==1+5*d+len(ins),(d,ins)
    r=wdvv(d,ins,ch); n+=1; ok+=(r==0)
    print(f"d={d} n={len(ins)} ch={ch} residual={r}", flush=True)
print(f"RESIDUAL {ok}/{n}", flush=True)
print("divisor check:", call(2,[1,4,4,3,3]), 2*call(2,[4,4,3,3]), flush=True)
assert call(2,[1,4,4,3,3])==2*call(2,[4,4,3,3])
assert ok==n
print("ALL_PASS", flush=True)
