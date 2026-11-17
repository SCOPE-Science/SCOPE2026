#!/usr/bin/env python3
"""Exhaustive finite simplicial Morse verification for antipodal punctures of the five-cube Rips complex.
All faces and every oriented face-cover edge are constructed from the Hamming metric.
"""
from collections import Counter, deque
N=32; ALL=(1<<N)-1
BAD=[sum(1<<j for j in range(N) if (i^j).bit_count()>=4) for i in range(N)]
FULL=[21,8,4,6,24,10,3,2,12,25,11,31,19,30,1,14,22,16,28,17,18,29,9,5,15,20,0,13,23,7,26,27]
ONE=[26,0,5,23,10,25,13,21,28,7,8,29,3,12,1,15,22,19,31,16,20,4,14,9,30,11,17,24,2,6,18,27]
TWO=[20,14,31,24,12,3,1,13,15,8,22,16,10,4,19,5,29,25,23,18,9,27,26,0,11,30,28,7,6,21,17,2]

def faces(mask):
    f=[0]
    for v in range(N):
        if mask>>v&1:
            f.extend([s|(1<<v) for s in f if not(s&BAD[v])])
    return f

def matching(f,order):
    unmatched=set(f); pair={}
    for v in order:
        bit=1<<v
        for s in f:
            if s not in unmatched or (s&bit):continue
            t=s|bit
            if t in unmatched:
                unmatched.remove(s); unmatched.remove(t); pair[s]=t
    return unmatched,pair

def verify_acyclic(f,pair):
    ids={s:i for i,s in enumerate(f)}
    deg=[0]*len(f); edges=[[] for _ in f]; count=0
    for t in f:
        j=ids[t]; bits=t
        while bits:
            bit=bits&-bits;bits-=bit
            s=t^bit;i=ids[s]
            if pair.get(s)==t:edges[i].append(j);deg[j]+=1
            else:edges[j].append(i);deg[i]+=1
            count+=1
    queue=deque(i for i,d in enumerate(deg) if d==0); seen=0
    while queue:
        i=queue.popleft();seen+=1
        for j in edges[i]:
            deg[j]-=1
            if not deg[j]:queue.append(j)
    assert seen==len(f),('directed cycle',seen,len(f))
    return count

def main():
    examples=[
        ('full',ALL,FULL,{4:1,7:10},84297,494304),
        ('one_removed',ALL^1,ONE,{4:1,7:5},68850,399227),
        ('antipodal_pair_removed',ALL^1^(1<<31),TWO,{4:1},53403,304150),
        ('full_vertex_link',ALL&~(1|BAD[0]),list(range(N)),{6:5},15447,79630),
    ]
    for label,mask,order,want,facecount,covercount in examples:
        f=faces(mask);assert len(f)==facecount
        remaining,pair=matching(f,order)
        critical=dict(Counter(s.bit_count()-1 for s in remaining))
        assert critical==want,(label,critical)
        assert len(pair)*2+len(remaining)==len(f)
        covers=verify_acyclic(f,pair);assert covers==covercount
        print(f'{label}: augmented_faces={len(f)} pairs={len(pair)} critical={sorted(critical.items())} covers={covers} acyclic=PASS')
    print('PASS: all four complete finite Morse verifications')
if __name__=='__main__':main()
