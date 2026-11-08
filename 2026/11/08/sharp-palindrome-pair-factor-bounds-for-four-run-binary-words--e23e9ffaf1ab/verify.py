"""Independent direct factor checks and integer four-run extremum checks.
Standard-library only; run with: python verify.py
"""
from itertools import product


def palindrome_pair(s):
    return any(s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1] for i in range(len(s) + 1))


def direct_count(w):
    factors = {""}
    for i in range(len(w)):
        for j in range(i + 1, len(w) + 1):
            s = w[i:j]
            if palindrome_pair(s):
                factors.add(s)
    return len(factors)


def count3(a, b, c):
    return 1 + max(a, c) + b + a*b + b*c + a*c


def count4(a, b, c, d):
    total = 1 + max(a,c) + max(b,d)
    total += a*b + c*d - min(a,c)*min(b,d)
    total += b*c + a*c + b*d
    total += (d if c <= a else 0) + (a if b <= d else 0)
    total -= int(c <= a and b <= d)
    return total


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for a in range(1, n-k+2):
            for rest in compositions(n-a, k-1):
                yield (a,) + rest


def as_word(seq):
    return ''.join(str(i % 2)*r for i, r in enumerate(seq))


def opt4(n):
    small = {4:8, 5:12, 6:16, 7:21}
    return small[n] if n < 8 else (n*n+n+10)//3


def global4(n):
    return 1+((n+1)*(n+1))//3


def balanced(v):
    return max(v)-min(v) <= 1


def main():
    checked_direct=0
    for n in range(1,15):
        best=0
        for k in range(1,min(4,n)+1):
            for runs in compositions(n,k):
                word=as_word(runs)
                actual=direct_count(word)
                checked_direct+=1
                if k==3:
                    assert actual==count3(*runs),(runs,actual,count3(*runs))
                if k==4:
                    assert actual==count4(*runs),(runs,actual,count4(*runs))
                best=max(best,actual)
        assert best==global4(n),('global',n,best,global4(n))
    checked_param=0
    checked_eq=0
    for n in range(4,58):
        best=0
        eq=[]
        for runs in compositions(n,4):
            a,b,c,d=runs
            val=count4(*runs)
            checked_param+=1
            if val>best:
                best=val;eq=[runs]
            elif val==best:
                eq.append(runs)
        assert best==opt4(n),('opt4',n,best,opt4(n))
        if n>=8:
            for a,b,c,d in eq:
                assert a<c and b>d and (a==1 or d==1) and balanced((a+d+2,b,c)), (n,(a,b,c,d))
                checked_eq+=1
            # Every tuple of the predicted form is an equality case.
            for a,b,c,d in compositions(n,4):
                if a<c and b>d and (a==1 or d==1) and balanced((a+d+2,b,c)):
                    assert count4(a,b,c,d)==best
    print(f'VERIFY_OK direct_words={checked_direct} run_quadruples={checked_param} extremizers={checked_eq} range_n=1..57')

if __name__=='__main__':
    main()
