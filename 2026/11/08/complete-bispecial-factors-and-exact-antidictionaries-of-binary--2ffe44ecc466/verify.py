#!/usr/bin/env python3
"""Independent finite checks for a four-run circular-word theorem.

Uses only Python's standard library. Finite checks are not the general proof.
"""
from itertools import product
from random import Random


def cyclic_word(t):
    return '0'*t[0]+'1'*t[1]+'0'*t[2]+'1'*t[3]


def factor_sets(s):
    p=len(s)
    # The repeated string contains every circular factor up to period+1.
    t=s*3
    return [set([''])] + [set(t[i:i+n] for i in range(p)) for n in range(1,p+2)]


def brute_maw(s):
    f=factor_sets(s)
    out=set()
    for n in range(2,len(s)+2):
        for left in f[n-1]:
            for x in '01':
                w=left+x
                if w not in f[n] and w[1:] in f[n-1]:
                    out.add(w)
    return out


def brute_bispecial(s):
    p=len(s)
    triple=s*3
    out=set()
    for n in range(p+1):
        extensions={}
        for i in range(p):
            w=triple[p+i:p+i+n]
            pair=(triple[p+i-1],triple[p+i+n])
            extensions.setdefault(w,set()).add(pair)
        for w,pairs in extensions.items():
            if {a for a,b in pairs}=={'0','1'} and {b for a,b in pairs}=={'0','1'}:
                out.add(w)
    return out


def theoretical_bispecial(t):
    a,b,c,d=t
    A=max(a,c);B=max(b,d)
    ans={''}|{'0'*j for j in range(1,A)}|{'1'*j for j in range(1,B)}
    if a!=c and b!=d:
        u=min(a,c);v=min(b,d)
        ans.update(('0'*u+'1'*v, '1'*v+'0'*u))
    elif a==c and b!=d:
        v=min(b,d)
        ans.add('1'*v+'0'*a+'1'*v)
    elif a!=c and b==d:
        u=min(a,c)
        ans.add('0'*u+'1'*b+'0'*u)
    return ans


def theoretical_length_and_count(t):
    a,b,c,d=t
    A=max(a,c);B=max(b,d)
    count=A+B+int(a!=c)+int(b!=d)
    longest=max(A,B)+1
    if a!=c and b!=d:
        longest=max(longest,min(a,c)+min(b,d)+2)
    elif a==c and b!=d:
        longest=max(longest,a+2*min(b,d)+2)
    elif a!=c and b==d:
        longest=max(longest,2*min(a,c)+b+2)
    return count,longest


def main():
    checked=0; nonprimitive=0
    for t in product(range(1,7),repeat=4):
        s=cyclic_word(t)
        bis=brute_bispecial(s)
        assert bis==theoretical_bispecial(t),('bispecial',t,bis^theoretical_bispecial(t))
        observed=brute_maw(s)
        pred=theoretical_length_and_count(t)
        assert (len(observed),max(map(len,observed)))==pred,('maw',t,pred)
        checked+=1
        nonprimitive+=int(t[0]==t[2] and t[1]==t[3])
    rng=Random(20261106)
    samples=0
    for _ in range(200):
        t=tuple(rng.randint(1,40) for _ in range(4))
        s=cyclic_word(t)
        m=brute_maw(s)
        assert (len(m),max(map(len,m)))==theoretical_length_and_count(t),('large',t)
        samples+=1
    print('PASS profiles=',checked,'nonprimitive=',nonprimitive,'random_larger=',samples)

if __name__=='__main__':main()
