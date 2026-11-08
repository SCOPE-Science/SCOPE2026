#!/usr/bin/env python3
"""Finite consistency checks for the minimal-absent-factor theorem.

Only the mathematical proof establishes the unbounded result. The finite
prefix used here is factor-complete through the selected cutoff by the
surrounding-zero and consecutive-gap bounds described in RESULT.md.
"""

def gaps(b, n):
    arr=[]
    v=b-1
    while v<=n+2:
        arr.append(v)
        v*=b
    return arr


def predicted_words(b, n):
    G=gaps(b,n)
    s=set()
    for t in range(1,n):
        if t not in G:
            s.add('1'+'0'*(t-1)+'1')
    for j,d in enumerate(G):
        left=1 if j==0 else G[j-1]-1
        right=(b*d)-1
        s.add('0'*(left+1)+'1'+'0'*(d-1)+'1')
        s.add('1'+'0'*(d-1)+'1'+'0'*(right+1))
        if d<=2:
            s.add('1'+'0'*(d-1)+'1'+'0'*(b-2)+'1')
    return {v.encode() for v in s if len(v)<=n}


def finite_complete_factors(b,n):
    # For a length <= n factor with >= 2 ones, some consecutive marker
    # distance is <= n-1. All such pairs occur before the chosen endpoint.
    # A lone marker with n zeros on both sides occurs at b**j.
    j=1
    while (b-1)*b**(j-1)-1<n:
        j+=1
    last=b**(j+1)+n+2
    word=bytearray(b'0'*last)
    k=0
    while b**k<last:
        word[b**k]=49
        k+=1
    v=bytes(word)
    facts={b''}
    for length in range(1,n+1):
        facts.update(v[i:i+length] for i in range(len(v)-length+1))
    return facts


def direct_maws(factors,n):
    result=set()
    for length in range(2,n+1):
        for prefix in (v for v in factors if len(v)==length-1):
            for bit in [b'0',b'1']:
                w=prefix+bit
                if w not in factors and w[1:] in factors:
                    result.add(w)
    return result


def count_formula(b,n):
    g=b-1
    absent_gaps=n-1
    while g<=n-1:
        absent_gaps-=1
        g*=b
    result=absent_gaps+int(n>=b+2)
    v=b*b-1
    while v+1<=n:
        result+=2
        v*=b
    if b==2:
        result+=int(n>=3)+int(n>=4)
    if b==3:
        result+=int(n>=5)
    return result


def main():
    total_cases=total_factors=total_maws=0
    for b in range(2,9):
        for n in (8,12,18,24,32,40):
            factors=finite_complete_factors(b,n)
            actual=direct_maws(factors,n)
            expected=predicted_words(b,n)
            assert actual==expected,(b,n,sorted(actual-expected),sorted(expected-actual))
            assert len(expected)==count_formula(b,n),(b,n)
            total_cases+=1
            total_factors+=len(factors)
            total_maws+=len(actual)
    for b in range(2,21):
        for n in range(1,701):
            assert len(predicted_words(b,n))==count_formula(b,n),(b,n)
    print('VERIFY_OK complete_prefix_cases=%d factor_sets=%d minimal_absent_words=%d formula_ranges=2..20,1..700' % (total_cases,total_factors,total_maws))

if __name__=='__main__':
    main()
