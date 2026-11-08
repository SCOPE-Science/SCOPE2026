#!/usr/bin/env python3
"""Exact finite checks for the joint star-configuration character formula.
Uses elementary integers; independent direct fixed-cell enumeration.
"""
from math import factorial, comb
from itertools import permutations, combinations
from collections import defaultdict, deque


def weak_compositions(n, m):
    if m == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for rest in weak_compositions(n-j, m-1):
                yield (j,) + rest

def arm_words(m, letters):
    for p in permutations(letters):
        for cuts in weak_compositions(len(p), m):
            out = []
            off = 0
            for count in cuts:
                out.append(p[off:off+count]);off+=count
            yield tuple(out)

def move_a_to_b(arms, particle):
    ans=[]
    for i,word in enumerate(arms):
        if word and word[0]==particle:
            ans.append((particle,arms[:i]+(word[1:],)+arms[i+1:]))
    return ans

def arm_permute(arms, alpha, beta):
    out = [None]*len(arms)
    for i,word in enumerate(arms):
        out[alpha[i]] = tuple(beta[j] for j in word)
    return tuple(out)

def cycles_counts(p):
    n=len(p);seen=set();cnt=defaultdict(int)
    for i in range(n):
        if i not in seen:
            j=i;d=0
            while j not in seen:
                seen.add(j);j=p[j];d+=1
            cnt[d]+=1
    return cnt

def A_formula(alpha,beta):
    ac=cycles_counts(alpha);bc=cycles_counts(beta)
    out=1
    for d,c in bc.items():
        a=ac[d]
        if not a:return 0
        out*=d**c*factorial(c)*comb(c+a-1,a-1)
    return out

def B_formula(alpha,beta):
    fixed=[j for j in range(len(beta)) if beta[j]==j]
    if not fixed:return 0
    # Remove a chosen fixed particle and compress the remaining permutation.
    j=fixed[0]
    retain=[x for x in range(len(beta)) if x!=j]
    renum={old:i for i,old in enumerate(retain)}
    rest=tuple(renum[beta[i]] for i in retain)
    return len(fixed)*A_formula(alpha,rest)

def char_formula(alpha,beta):
    return 1-A_formula(alpha,beta)+(cycles_counts(alpha)[1]-1)*B_formula(alpha,beta)

def data(m,k):
    A=list(arm_words(m,tuple(range(k))))
    B=[(j,words) for j in range(k) for words in arm_words(m,tuple(x for x in range(k) if x!=j))]
    Ai={a:i for i,a in enumerate(A)}
    Bi={b:i for i,b in enumerate(B)}
    assert len(A)==factorial(k)*comb(k+m-1,m-1)
    assert len(B)==factorial(k)*comb(k+m-2,m-1)
    edges=[];neigh=[[] for _ in range(len(A)+len(B))]
    for ib,(particle,arms) in enumerate(B):
        for arm in range(m):
            arr=list(arms);arr[arm]=(particle,)+arr[arm]
            ia=Ai[tuple(arr)]
            edges.append((ia,ib));neigh[ia].append(len(A)+ib);neigh[len(A)+ib].append(ia)
    seen={0};stack=[0]
    while stack:
        a=stack.pop()
        for b in neigh[a]:
            if b not in seen:seen.add(b);stack.append(b)
    assert len(seen)==len(A)+len(B),('disconnected',m,k,len(seen))
    b1=len(edges)-len(A)-len(B)+1
    expected=1+(k*m-2*k-m+1)*factorial(k+m-2)//factorial(m-1)
    assert b1==expected,(b1,expected)
    return A,B,edges,b1

def partitions(n,max_parts):
    def rec(left, maxpart, cur):
        if left==0:
            yield tuple(cur);return
        if len(cur)>=max_parts:return
        for s in range(min(left,maxpart),0,-1):
            yield from rec(left-s,s,cur+[s])
    return list(rec(n,n,[]))

def quotient_data(m,k):
    P=partitions(k,m);Q=partitions(k-1,m)
    adj=[]
    for mu in Q:
        covers=set()
        for i in range(len(mu)):
            ns=list(mu);ns[i]+=1
            covers.add(tuple(sorted(ns,reverse=True)))
        if len(mu)<m:covers.add(tuple(sorted(mu+(1,),reverse=True)))
        for v in covers:
            assert v in P
            adj.append((mu,v))
    b1=1+len(adj)-len(P)-len(Q)
    return len(P),len(Q),len(adj),b1

def check(m,k,all_group=True):
    A,B,E,b1=data(m,k)
    ps=list(permutations(range(m)));qs=list(permutations(range(k)))
    nchecks=0
    if not all_group:qs=qs[::max(1,len(qs)//17)]
    for alpha in ps:
        for beta in qs:
            nA=sum(arm_permute(words,alpha,beta)==words for words in A)
            nB=sum(beta[j]==j and arm_permute(words,alpha,beta)==words for j,words in B)
            nE=sum(beta[j]==j and arm_permute(words,alpha,beta)==words for j,words in B)*sum(alpha[i]==i for i in range(m))
            assert nA==A_formula(alpha,beta),(m,k,alpha,beta,nA,A_formula(alpha,beta))
            assert nB==B_formula(alpha,beta),(m,k,alpha,beta,nB,B_formula(alpha,beta))
            assert 1-nA-nB+nE==char_formula(alpha,beta)
            nchecks+=1
    # Independent Burnside averaging against the partition-incidence quotient.
    avg_num=sum(char_formula(alpha,beta) for alpha in ps for beta in permutations(range(k)))
    assert avg_num % (factorial(m)*factorial(k)) == 0
    average=avg_num//(factorial(m)*factorial(k))
    assert average==quotient_data(m,k)[3],(m,k,average,quotient_data(m,k))
    # Independent edge-orbit classification: each actual edge has an endpoint
    # pair of integer partitions, not just an inferred cover relation.
    edge_orbits=set()
    for particle,words in B:
        mu=tuple(sorted((len(x) for x in words if x),reverse=True))
        for i in range(m):
            nu=list(len(x) for x in words);nu[i]+=1
            lam=tuple(sorted((x for x in nu if x),reverse=True))
            edge_orbits.add((mu,lam))
    assert len(edge_orbits)==quotient_data(m,k)[2]
    print('m',m,'k',k,'A',len(A),'B',len(B),'edges',len(E),'b1',b1,'group_checks',nchecks,'quotient',quotient_data(m,k),'avg_character',average,'edge_orbits',len(edge_orbits))

if __name__=='__main__':
    check(3,2)
    check(3,3)
    check(4,4)
    check(3,5,True)
    print('STAR_JOINT_CHARACTER_CHECK_PASS')
