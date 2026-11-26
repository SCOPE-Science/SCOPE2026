#!/usr/bin/env python3
"""Direct exact factor-multiplicity verification for finite dyadic period-doubling prefixes."""
from collections import Counter

def shortest_unique(s):
    for length in range(1,len(s)+1):
        mult=Counter(s[j:j+length] for j in range(len(s)-length+1))
        places=[j for j in range(len(s)-length+1) if mult[s[j:j+length]]==1]
        if places:
            return (length,places)
    raise AssertionError("A whole word is unique")

def run():
    s='0'
    for k in range(1,10):
        s=''.join('01' if c=='0' else '00' for c in s)
        if k<4:continue
        starts=[2**(k-2)-1,3*2**(k-3)-1,2**(k-1)-1,3*2**(k-2)-1]
        predicted=(2**(k-2)+1,starts)
        assert shortest_unique(s)==predicted,(k,'complete')
        assert shortest_unique(s[:-1])==(predicted[0],starts[:3]),(k,'truncated')
        print(f'k={k}, size={len(s)}, first_unique_length={predicted[0]}, complete_starts={starts}, truncated_starts={starts[:3]}')
    print('PASS: exact exhaustive substring occurrence comparisons for k=4,...,9 (both prefixes).')
if __name__=='__main__':run()
