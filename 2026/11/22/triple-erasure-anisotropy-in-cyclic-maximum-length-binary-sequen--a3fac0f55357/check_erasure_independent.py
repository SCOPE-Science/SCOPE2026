#!/usr/bin/env python3
"""Independent recurrence/bit-pattern census for eroded maximum-length cycles."""
import itertools, math
PRIMITIVE={3:0b1011,4:0b10011,5:0b100101}

def words(m):
    p=PRIMITIVE[m]
    # A nonzero initial state, use all-ones here independently of trace.
    seq=[1]*m
    L=(1<<m)-1
    for i in range(m,L):
        v=0
        for j in range(m):
            if (p>>j)&1: v^=seq[i-m+j]
        seq.append(v)
    # Check that the m-bit states are all nonzero and pairwise distinct.
    states=[sum(seq[(i+j)%L]<<j for j in range(m)) for i in range(L)]
    assert set(states)==set(range(1,1<<m))
    rows=[sum(seq[(t+j)%L]<<j for j in range(L)) for t in range(L)]
    # Map the t-th phase to its LFSR state vector: addition is bitwise XOR.
    return states,rows

def independent_count(m,k):
    return math.prod((1<<m)-(1<<j) for j in range(k))//math.factorial(k)

def bitsupport_masks(rows,coords):
    # Encode output masks for each retained cyclic phase (directly, no linear algebra).
    result=[]
    for row in rows:
        sig=0
        for a,j in enumerate(coords):sig+=((row>>j)&1)<<a
        result.append(sig)
    return result

def direct(m,rows,removed,k):
    total=0; allvalues=set(range(1<<k)); L=len(rows)
    for coords in itertools.combinations(range(L),k):
        observed={bitsupport_masks([rows[t]],coords)[0] for t in range(L) if t not in removed}
        total+=(observed==allvalues)
    return total

def predicted(m,deleted):
    sums={a^b for a,b in itertools.combinations(deleted,2)}
    B=independent_count(m-1,m-1)
    top=B*((1<<m)-1-len(set(deleted)|sums))
    low=independent_count(m,m-2)
    if len(deleted)==3 and deleted[0]^deleted[1]^deleted[2]==0:
        low-=independent_count(m-2,m-2)
    return top,low

def run():
    for m in (3,4):
        states,rows=words(m);L=len(rows)
        tests=list(itertools.combinations(range(L),3))
        for T in tests:
            pt,pl=predicted(m,[states[i] for i in T])
            ot=direct(m,rows,set(T),m-1)
            ol=direct(m,rows,set(T),m-2)
            assert (ot,ol)==(pt,pl),(m,T,ot,ol,pt,pl)
        print('m=',m,'ALL',len(tests),'three-phase deletions verified, both final degrees',flush=True)
    m=5
    states,rows=words(m)
    tests=[(0,1,2),(0,1,3),(0,1,4),(0,1,5),(0,2,8),(0,1,states.index(states[0]^states[1]))]
    for T in tests:
        pt,pl=predicted(m,[states[i] for i in T]);ot=direct(m,rows,set(T),m-1);ol=direct(m,rows,set(T),m-2)
        assert (ot,ol)==(pt,pl),(m,T,ot,ol,pt,pl)
    print('m=5',len(tests),'independently generated recurrence samples passed')
    print('INDEPENDENT RECURRENCE CHECK PASSED')
if __name__=='__main__':run()
