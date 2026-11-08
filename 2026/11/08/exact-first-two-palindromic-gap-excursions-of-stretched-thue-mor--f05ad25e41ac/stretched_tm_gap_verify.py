#!/usr/bin/env python3
"""Reproduce exact gap-context arithmetic and independent small-case factor counts."""
from collections import Counter, defaultdict


def thue_morse_morphism(word):
    return ''.join('01' if ch == '0' else '10' for ch in word)


def gap_contexts():
    # Every factor of the Thue--Morse word of length <= 32 occurs
    # in one of these four permitted pairs of 32-blocks.
    b = {'0': '0', '1': '1'}
    for _ in range(5):
        b = {key: thue_morse_morphism(val) for key, val in b.items()}
    contexts = defaultdict(lambda: defaultdict(set))
    for a in '01':
        for c in '01':
            s = b[a] + b[c]
            ones = [i for i, ch in enumerate(s) if ch == '1']
            gaps = [ones[i+1]-ones[i]-1 for i in range(len(ones)-1)]
            for k in range(1, 7):
                for j in range(len(gaps)-k):
                    g = tuple(gaps[j:j+k+1])
                    contexts[k][g[1:-1]].add((g[0],g[-1]))
    return contexts


def signatures(contexts, max_k=5):
    # Derive a signed step-function expression for p(n+1)-p(n)
    # from inclusion--exclusion on the admissible endpoint gaps.
    steps = Counter()
    pal = Counter()
    for k in range(1, max_k+1):
        for internal, boundary in contexts[k].items():
            total = sum(internal)
            pairs = sorted(boundary)
            for mask in range(1, 1 << len(pairs)):
                chosen = [pair for i, pair in enumerate(pairs) if mask & (1 << i)]
                a = min(pair[0] for pair in chosen)
                b = min(pair[1] for pair in chosen)
                sign = 1 if len(chosen) % 2 else -1
                # h_{a,b}(d)=(d+1)_+-(d-M-a)_+-(d-M-b)_+
                #            +(d-2M-a-b-1)_+.
                steps[(k-1, total)] += sign
                steps[(k, total+a)] -= sign
                steps[(k, total+b)] -= sign
                steps[(k+1, total+a+b)] += sign
            if internal == internal[::-1]:
                bmax = max(min(a, b) for a, b in pairs)
                pal[(k, total, bmax)] += 1
    return {key: val for key, val in steps.items() if val}, dict(pal)


def direct_context_counts(C, M, n):
    p = int(n <= M+2)  # a^n, one if it exists
    pal = p
    for k in range(1, 7):
        for internal, ends in C[k].items():
            d = n-1-(k-1)*(M+1)-sum(internal)
            if d < 0:
                continue
            for left in range(max(0, d-M-2), min(d,M+2)+1):
                right = d-left
                if any(left <= M+a and right <= M+b for a,b in ends):
                    p += 1
                    if left == right and internal == internal[::-1]:
                        pal += 1
    return p, pal


def main():
    C=gap_contexts()
    assert [len(C[k]) for k in range(1,7)] == [1,3,6,10,12,16]
    assert [sum(map(len,C[k].values())) for k in range(1,7)] == [6,10,12,16,20,22]
    assert min(sum(u) for u in C[6]) == 4
    # A factor containing six b's has length >= 5(M+1)+4+1=5M+10.
    steps, pals = signatures(C, 5)
    full_steps, full_pals = signatures(C, 6)
    expected_steps = {
        (0,0):1, (1,0):1, (1,1):1, (1,2):-1,
        (2,1):2, (2,2):-1, (3,1):-1, (3,2):2,
        (4,3):-2, (5,4):-2, (5,5):-8,
        (5,6):-4, (6,6):8, (6,7):4
    }
    assert steps==expected_steps, (steps,expected_steps)
    expected_pal = {(1,0,1):1,(2,0,2):1,(2,1,0):1,(2,2,1):1,
                    (4,2,1):1,(4,2,2):1,(4,4,0):1,(4,4,1):1}
    assert pals==expected_pal, (pals,expected_pal)
    assert full_steps[(5,4)] == 2
    assert full_pals[(6,4,1)] == 1 and full_pals[(6,4,2)] == 1
    def dp_from_steps(M,n):
        return sum(coef for (alpha,beta),coef in steps.items()
                   if n>=alpha*(M+1)+beta)
    def pal_from_terms(M,n):
        result=0
        for (k,s,b),multiplicity in pals.items():
            d=n-1-(k-1)*(M+1)-s
            if d>=0 and d%2==0 and d<=2*(M+b):
                result+=multiplicity
        return result
    # Independent direct construction of the finite word checks both
    # the context formula and the claimed threshold spectrum.
    t='0'
    for _ in range(13):
        t=thue_morse_morphism(t)
    checked=0
    for M in range(1,10):
        u=''.join('a' if c=='0' else 'a'*M+'b' for c in t)
        max_n=5*M+10
        sets=[set(u[i:i+n] for i in range(len(u)-n+1)) for n in range(1,max_n+2)]
        for n in range(1,5*M+10):
            p=len(sets[n-1]);p1=len(sets[n]);
            q=sum(x==x[::-1] for x in sets[n-1])
            q1=sum(x==x[::-1] for x in sets[n]);
            x=(p1-p,p1-p+2-q-q1)
            expected_T = 0 if n<=2*M+2 else 2 if n<=4*M+6 else 0 if n<=5*M+8 else 2
            assert x[1] == expected_T, (M,n,x,expected_T)
            if n>=2*M+3 and n<=5*M+8:
                if n==2*M+3: expected_dp=4
                elif n<=3*M+3: expected_dp=3
                elif n==3*M+4: expected_dp=2
                elif n<=4*M+6: expected_dp=4
                else: expected_dp=2
                assert x[0]==expected_dp, (M,n,x)
                assert p1-p==dp_from_steps(M,n)
                assert q+q1==pal_from_terms(M,n)+pal_from_terms(M,n+1)
            assert (p,q)==direct_context_counts(C,M,n)
            checked+=1
        n=5*M+9
        p=len(sets[n-1]);p1=len(sets[n]);
        q=sum(x==x[::-1] for x in sets[n-1]);q1=sum(x==x[::-1] for x in sets[n]);
        assert p1-p==4 and q+q1==4
        assert (p1,q1)==direct_context_counts(C,M,n+1)
    # Additional unbounded-parameter arithmetic smoke test: these evaluations
    # are not used as a substitute for the symbolic interval proof.
    for M in (20,51,100,1000):
        for n in range(2*M+3,5*M+9):
            dp=dp_from_steps(M,n)
            ps=pal_from_terms(M,n)+pal_from_terms(M,n+1)
            if n==2*M+3: expected=(4,4)
            elif n<=3*M+3: expected=(3,3)
            elif n==3*M+4: expected=(2,2)
            elif n<=4*M+6: expected=(4,4)
            else: expected=(2,4)
            assert (dp,ps)==expected,(M,n,dp,ps,expected)
    print('STRETCHED_TM_GAP_VERIFY_OK',checked,'cases; symbolic signatures',len(steps),len(pals))

if __name__=='__main__':main()
