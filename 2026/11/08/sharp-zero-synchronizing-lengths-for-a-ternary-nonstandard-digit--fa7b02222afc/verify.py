"""Exact finite verification of a ternary carry synchronization theorem.
Run with Python 3 standard library. Assertions are finite checks, not the proof.
"""
from itertools import product


def params(k):
    B=3**(k+1)
    return B,(B-1)//2,(3**k-1)//2

def h(c,a,B):
    z=a+c
    digit=(0,1,B-1)[z%3]
    assert (z-digit)%3==0
    return (z-digit)//3

def zero_sync(word,k):
    B,M,H=params(k)
    for c0 in range(-M,1):
        c=c0
        for a in word:
            c=h(c,a,B)
        if c:
            return False
    return True

def ternary_digits(n,l):
    a=[]
    for _ in range(l):
        a.append(n%3)
        n//=3
    assert n==0
    return tuple(a)

def represented(l,k):
    B,M,H=params(k)
    S={0}
    for j in range(l):
        step=3**j
        S={x+d*step for x in S for d in (0,1,B-1)}
    assert len(S)==3**l
    return S

def check(k):
    B,M,H=params(k)
    assert B%3==0 and (B-1)%3==2
    for l in range(1,2*k+2):
        S=represented(l,k)
        # An interval of M+1 represented values means exact synchronization.
        sorted_S=sorted(S)
        run=best=1
        sync_candidates=set()
        for n in range(1,len(sorted_S)):
            run=(run+1) if sorted_S[n]==sorted_S[n-1]+1 else 1
            best=max(best,run)
            if run>=M+1:
                # input number must be between 0 and 3^l-1
                A=sorted_S[n]
                for end in range(A-M,A+1):
                    if 0<=end<3**l and all(end-c in S for c in range(M+1)):
                        sync_candidates.add(end)
        if l<=2*k:
            assert best<M+1,(k,l,best)
        else:
            assert best>=M+1
        if l==2*k+1:
            good=[]
            for v in range(3**l):
                if all(v-c in S for c in range(M+1)):
                    good.append(v)
                    if k<=3: assert zero_sync(ternary_digits(v,l),k)
            assert len(good)>=H+1
            expected={3**k*M+v for v in range(H+1)}
            assert expected<=set(good)
            print('SHORTEST_CHECK',k,'states',M+1,'length',l,'optimal_words',len(good),'constructed',H+1)

for k in range(1,5):
    check(k)
print('EXHAUSTIVE_SMALL_CASES_OK')
for k in range(5,9):
    B,M,H=params(k)
    choices=[0,1,H//2,H]
    for v in choices:
        word=ternary_digits(v,k)+(1,)*(k+1)
        assert zero_sync(word,k)
    print('DIRECT_CARRY_WITNESSES',k,'states',M+1,'length',2*k+1,'sampled',len(choices))
print('FINITE_REPLAY_OK; proof of universal k is separate')
