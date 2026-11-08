#!/usr/bin/env python3
"""Self-contained exact integer certificate for cyclic Rule 54 singleton fibres.

Only the Python standard library is used.  No tables or external files required.
"""
from collections import deque

RULE = 54
DEN = (1,-4,6,-4,-1,6,-7,2,3,-3,1,1,-2,2,-1)
NUM = (0,0,0,3,0,-15,24,-8,-10,12,-10,-7,17,-23,12,-3,2)
FIRST = (0,0,0,3,12,15,24,49,96,162,270,462,806,1378,2366,4105,7176)


def generators():
    out=[]
    for value in (0,1):
        entries=[0]*16
        for ab in range(4):
            for bit in range(2):
                triple=2*ab+bit
                if ((RULE >> triple) & 1)==value:
                    entries[4*ab + (triple&3)]+=1
        out.append(tuple(entries))
    return out


def truncated_product(a,b):
    """Compute product over N capped at 2; exact for 0/1/excess tests."""
    return tuple(min(2,sum(a[4*i+k]*b[4*k+j] for k in range(4)))
                 for i in range(4) for j in range(4))


def construct():
    start=tuple(1 if i==j else 0 for i in range(4) for j in range(4))
    index={start:0}
    queue=deque([start]); transition=[]; generators_=generators()
    while queue:
        cur=queue.popleft()
        targets=[]
        for g in generators_:
            successor=truncated_product(cur,g)
            if successor not in index:
                index[successor]=len(index)
                queue.append(successor)
            targets.append(index[successor])
        transition.append(tuple(targets))
    acceptance=tuple(int(sum(mat[5*j] for j in range(4))==1)
                     for mat in index)
    assert len(index)==len(transition)==410
    assert len(set(index.values()))==410
    # Enumerating all closure successors, including previously seen states,
    # proves the set is the complete reachable product semigroup.
    assert all(0<=u<len(transition) and 0<=v<len(transition)
               for u,v in transition)
    return transition,acceptance


def right_action(T,v):
    return tuple(v[i]+v[j] for i,j in T)


def main():
    T,f=construct()
    # Coefficient c_n = (T^n f)_0.  Compute T^0 f through T^17 f.
    vectors=[f]
    for _ in range(17): vectors.append(right_action(T,vectors[-1]))
    coeffs=tuple(v[0] for v in vectors)
    assert coeffs[:17]==FIRST
    # 17th coefficient is determined by the recurrence.
    assert sum(DEN[k]*coeffs[17-k] for k in range(15))==0
    # The finite vector identity T^3 p(T) f=0 proves this relation
    # for *all* n >=17, not just for the displayed coefficients.
    w=tuple(sum(DEN[j]*vectors[14-j][i] for j in range(15))
            for i in range(len(T)))
    for _ in range(3):w=right_action(T,w)
    assert all(q==0 for q in w), ('annihilator_nonzero',[(i,q) for i,q in enumerate(w) if q][:5])
    # Exact rational-series numerator, including transient initial terms.
    for n in range(17):
        assert NUM[n]==sum(DEN[j]*FIRST[n-j]
                           for j in range(min(14,n)+1))
    # Check more coefficients independently against the recurrence.
    for n in range(18,90):
        vectors.append(right_action(T,vectors[-1]))
        assert sum(DEN[j]*vectors[n-j][0] for j in range(15))==0
    print('CERTIFICATE_OK', 'states=410', 'annihilator_degree=14',
          'transient=3', 'checked_through=89')
    print('unique_image_counts_n1_to16=',','.join(map(str,FIRST[1:])))
    print('den=',DEN)
    print('numerator=',NUM)

if __name__=='__main__':main()
