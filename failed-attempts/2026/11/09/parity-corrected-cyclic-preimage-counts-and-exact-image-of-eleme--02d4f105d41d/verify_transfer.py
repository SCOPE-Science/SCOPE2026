#!/usr/bin/env python3
"""Independent four-state de Bruijn transfer check for cyclic Rule 126."""
import random

def matmul(A,B):
    C=[[0]*4 for _ in range(4)]
    for i in range(4):
        for k in range(4):
            if A[i][k]:
                for j in range(4):C[i][j]+=A[i][k]*B[k][j]
    return C

def transfer_matrices():
    matrices=[[[0]*4 for _ in range(4)] for _ in range(2)]
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                z=(126>>((a<<2)|(b<<1)|c))&1
                matrices[z][2*a+b][2*b+c]+=1
    return matrices

def count_transfer(bits):
    T=transfer_matrices()
    M=[[int(i==j) for j in range(4)] for i in range(4)]
    for b in bits:M=matmul(M,T[b])
    return sum(M[i][i] for i in range(4))

def path_sign(k,sign):
    if k<1:return 1
    a,b=1,1+sign
    for _ in range(2,k+1):a,b=b,b+sign*a
    return b

def formula_alternate(y):
    n=len(y)
    # Entirely independent from the other program's polynomial implementation:
    # force vertices touching output zeros to one; enforce positive output
    # no-adjacent-ones by exhaustive parity DP on the remaining vertices.
    forced=0
    for i in range(n):
        if y[i]==0:
            forced|=1<<i
            forced|=1<<((i-1)%n)
    if not forced:
        # One-pass parity DP on a circular 2-state hard-core constraint.
        count=0
        for first in (0,1):
            dp={(first,first%2):1}
            for _ in range(1,n):
                nd={}
                for (prev,p),v in dp.items():
                    for bit in (0,1):
                        if bit and prev:continue
                        key=(bit,p^bit)
                        nd[key]=nd.get(key,0)+v
                dp=nd
            for (last,p),v in dp.items():
                if (first and last) or p!=n%2:continue
                count+=v
        return 2*count
    # Enumerate free vertices via two-state parity DP; support any n,
    # using forced-one and forbidden-adjacent-one constraints for output ones.
    count=0
    for first in (0,1):
        if (forced&1) and first==0:continue
        dp={(first,first%2):1}
        for i in range(1,n):
            nd={}
            for (prev,p),v in dp.items():
                for bit in (0,1):
                    if ((forced>>i)&1) and bit==0:continue
                    if y[i]==1 and prev and bit:continue
                    key=(bit,p^bit)
                    nd[key]=nd.get(key,0)+v
            dp=nd
        for (last,p),v in dp.items():
            if y[0]==1 and first and last:continue
            if p!=n%2:continue
            count+=v
    return 2*count

def run():
    rng=random.Random(126)
    for n in range(1,13):
        for w in range(1<<n):
            y=[(w>>i)&1 for i in range(n)]
            a=count_transfer(y)
            b=formula_alternate(y)
            assert a==b,(n,w,a,b)
        print('n=',n,'transfer_and_parity_DP_agree')
    for n in (15,21,32,47,64):
        for _ in range(250):
            y=[rng.randrange(2) for _ in range(n)]
            assert count_transfer(y)==formula_alternate(y),(n,y)
    print('TRANSFER_VERIFY_OK')

if __name__=='__main__':run()
