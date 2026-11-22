#!/usr/bin/env python3
"""Direct small-field check for commuting algebra-retraction pairs on symmetric jets.
Uses only integer bitmasks and the defining truncated polynomial product.
"""
from itertools import combinations
from math import comb

basis=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]
mon_index={b:i for i,b in enumerate(basis)}
mul_table=[[0]*len(basis) for _ in basis]
for i,(a,b) in enumerate(basis):
    for j,(c,d) in enumerate(basis):
        if a+b+c+d<=3:
            mul_table[i][j]=1<<mon_index[(a+c,b+d)]

def multiply(a,b):
    out=0
    while a:
        bit=a&-a;i=bit.bit_length()-1;a-=bit
        row=mul_table[i]
        x=b
        while x:
            bit2=x&-x;j=bit2.bit_length()-1;x-=bit2
            out ^= row[j]
    return out

def apply_poly(poly, images):
    out=0
    while poly:
        bit=poly&-poly;j=bit.bit_length()-1;poly-=bit
        out ^= images[j]
    return out

def matrix_rank2(a,b,c,d):
    if (a*d-b*c)&1:return 2
    return 1 if a or b or c or d else 0

def enumerate_idempotents():
    all_imgs=[2*i for i in range(1<<9)]
    sq=[multiply(v,v) for v in all_imgs]
    cube=[multiply(v,sq[i]) for i,v in enumerate(all_imgs)]
    items=[]
    for i,x in enumerate(all_imgs):
        x2=sq[i];x3=cube[i]
        for j,y in enumerate(all_imgs):
            y2=sq[j];y3=cube[j]
            xy=multiply(x,y)
            im=[1,x,y,x2,xy,y2,x3,multiply(x2,y),multiply(x,y2),y3]
            if apply_poly(x,im)==x and apply_poly(y,im)==y:
                a=(x>>1)&1;b=(y>>1)&1;c=(x>>2)&1;d=(y>>2)&1
                items.append((x,y,im,(a,b,c,d),matrix_rank2(a,b,c,d)))
    return items

def galois_joint_count(n,d,q,k=2):
    # Summation over all 4^n assignments of eigenspace labels to an ordered
    # basis, deduplicated by orbit type; for n=2, partition types are simple.
    def gl(n):
        z=1
        for j in range(n):z*=q**n-q**j
        return z
    # n=2, all n_eta in {0,1,2} and sum=2.
    M2=sum(j+1 for j in range(2,d+1))
    total=0
    for a in range(4):
        for b in range(a,4):
            if a==b:
                # One weight space of dimension 2; one orbit, singleton tuple.
                count=1
            else:
                M=[0]*4
                for degree in range(2,d+1):
                    for ix in range(degree+1):
                        iy=degree-ix
                        eta=(a if ix>0 else 3)&(b if iy>0 else 3)
                        M[eta]+=1
                exponent=2*M2-(M[a]+M[b])
                count=gl(2)//((q-1)**2)*q**exponent
            total+=count
    return total

def main():
    retracts=enumerate_idempotents()
    hist=[sum(1 for x in retracts if x[4]==r) for r in range(3)]
    assert hist==[1,768,1],hist
    total=0
    buckets={}
    # Compare the *original substitution operators* on both generators.
    for F in retracts:
        for G in retracts:
            FG=(apply_poly(G[0],F[2]),apply_poly(G[1],F[2]))
            GF=(apply_poly(F[0],G[2]),apply_poly(F[1],G[2]))
            if FG!=GF:continue
            total+=1
            a,b,c,d=F[3];e,f,g,h=G[3]
            # Tangent matrix product of F after G.
            u=(a*e+b*g)&1;v=(a*f+b*h)&1
            w=(c*e+d*g)&1;z=(c*f+d*h)&1
            rankproduct=matrix_rank2(u,v,w,z)
            key=(F[4],G[4],rankproduct)
            buckets[key]=buckets.get(key,0)+1
    expected=galois_joint_count(2,3,2)
    assert total==expected==9988,(total,expected)
    print('F2[x,y]/(x,y)^4: idempotent maps by tangent rank',hist)
    print('F2[x,y]/(x,y)^4: commuting ordered pairs',total)
    print('Joint (rank F, rank G, rank FG) histogram:',sorted(buckets.items()))
    print('ALL_COMMUTING_JET_RETRACTIONS_VERIFIED')
if __name__=='__main__':main()
