#!/usr/bin/env python3
"""Finite consistency checks for a rational frequency-shift marker; not an infinite proof."""
from math import gcd

def allowed(a,b,word):
    h=0
    for i,letter in enumerate(word):
        if i and word[i-1]=='1':
            if (h>=0 and letter!='1') or (h<0 and letter!='0'):
                return False
        h += a if letter=='0' else -b
    return True

def level_extensions(a,b,max_len):
    states=[('',0)]
    marker='0'*b+'1'*(a+1)+'0'
    tests=0
    for n in range(1,max_len+1):
        nxt=[]
        for word,h in states:
            for char in ('0','1'):
                if word.endswith('1') and char != ('1' if h>=0 else '0'):
                    continue
                s=word+char
                h2=h+(a if char=='0' else -b)
                assert marker not in s[1:], (a,b,s,marker)
                nxt.append((s,h2))
                tests+=1
        states=nxt
    witness=marker+'0'*8
    assert allowed(a,b,witness)
    return tests,len(states)

def main():
    pairs=[(2,1),(3,1),(5,2),(7,3),(8,3),(9,4),(11,4),(13,5)]
    checks=0
    for a,b in pairs:
        assert gcd(a,b)==1 and a>=2*b
        n=min(len('0'*b+'1'*(a+1)+'0')+7,22)
        count,states=level_extensions(a,b,n)
        checks+=count
        print(f'(a,b)=({a},{b}), prefixes={count}, final={states}, depth={n}: verified')
    print(f'PASS: {checks} admissible finite prefixes checked; infinite statement proved separately.')
if __name__=='__main__': main()
