#!/usr/bin/env python3
"""Exact finite verification for binary (1,7)-overlap-free codes.
Run: python3 verify.py. No third-party dependencies.
"""

def relations(k, reverse_sides=False):
    m = 1 << (k - 1)
    # P consists of all k-bit words beginning with 0, S of all ending with 1.
    ps = range(m)
    ss = [2*j+1 for j in range(m)]
    allbits=(1<<m)-1
    allow=[]
    for p in ps:
        mask=0
        for j,s in enumerate(ss):
            # All nonempty proper or full overlaps of the boundary blocks
            if not any((p >> (k-t)) == (s & ((1<<t)-1)) for t in range(1,k+1)):
                mask |= 1<<j
        allow.append(mask)
    if reverse_sides:
        dual=[]
        for j in range(m):
            dual.append(sum(1<<i for i in range(m) if allow[i]>>j&1))
        allow=dual
    return allow


def closed_concepts(allow):
    n=len(allow)
    full=(1<<n)-1
    adj_back=[]
    for j in range(n):
        back=0
        for i,row in enumerate(allow):
            if row>>j&1:back |= 1<<i
        adj_back.append(back)

    def closure(start):
        common=full
        todo=start
        while todo:
            bit=todo & -todo
            common &=allow[bit.bit_length()-1]
            todo -=bit
        result=full
        todo=common
        while todo:
            bit=todo & -todo
            result &=adj_back[bit.bit_length()-1]
            todo-=bit
        assert not (start & ~result)
        return result,common

    current=closure(0)[0]
    seen=0
    high=(0,0,0)
    bysize={}
    while True:
        extent,intent=closure(current)
        assert extent==current
        a=current.bit_count();b=intent.bit_count()
        seen+=1
        score=a*b
        if score>high[0]:high=(score,a,b)
        if a not in bysize or b>bysize[a]:bysize[a]=b
        new=None
        for j in range(n-1,-1,-1):
            bit=1<<j
            if not current & bit:
                smaller=(1<<j)-1
                candidate=closure((current&smaller)|bit)[0]
                if candidate&smaller==current&smaller:
                    new=candidate
                    break
        if new is None:break
        assert new != current
        current=new
    return seen,high,bysize


def direct_check(allow):
    # Brute-force all 2^16 subsets, independent of lectic traversal.
    n=len(allow);assert n==16
    full=(1<<n)-1
    feasible=[full]*(1<<n)
    maxprod=0
    for mask in range(1,1<<n):
        bit=mask & -mask
        feasible[mask]=feasible[mask-bit] & allow[bit.bit_length()-1]
        maxprod=max(maxprod,mask.bit_count()*feasible[mask].bit_count())
    return maxprod


def verify():
    for k in (5,6,7):
        a=relations(k)
        forward=closed_concepts(a)
        reverse=closed_concepts(relations(k,True))
        assert forward[0]==reverse[0]
        assert forward[1][0]==reverse[1][0]
        if k==5: assert forward[1][0]==direct_check(a)==64
        if k==6: assert forward[1][0]==216
        if k==7:
            assert forward[0]==1944
            assert forward[1][0]==744
            # Explicit construction P={0,...,23}; all permitted S.
            forbidden=0
            for p in range(24):forbidden |= ((1<<64)-1)^a[p]
            s_mask=((1<<64)-1)^forbidden
            assert s_mask.bit_count()==31
            for p in range(24):assert a[p]&s_mask==s_mask
            # Check every maximal closed pair's product via the independent traversal.
            assert max(i*j for i,j in forward[2].items())==744
            print('CERTIFICATE k=7 concepts=',forward[0],
                  ' max_prod=',forward[1][0],
                  ' witness_P=24 witness_S=31',
                  ' dual_concepts=',reverse[0],sep='')
        else:
            print('BASELINE k=',k,' concepts=',forward[0],' max=',forward[1][0],sep='')
    print('VERIFY_OK')

if __name__=='__main__':verify()
