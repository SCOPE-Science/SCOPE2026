#!/usr/bin/env python3
"""Independent finite-prefix cross-check for two Rule-22 synchronous updates."""
from itertools import product

def step(bits):
    # Rather than consulting the Wolfram truth-table bits, count ones directly.
    return tuple(int(bits[j]+bits[j+1]+bits[j+2]==1) for j in range(len(bits)-2))

def all_outputs(n,t):
    outputs=set()
    for incoming in product((0,1),repeat=n+2*t):
        x=incoming
        for _ in range(t):x=step(x)
        outputs.add(x)
    return outputs

def main():
    first=[2,4,8,16,32,64,128,254,500,981,1917,3732]
    second=[2,4,8,16,32,64,126,246,477,926,1788,3428]
    for n in range(1,13):
        S1=all_outputs(n,1); S2=all_outputs(n,2)
        assert len(S1)==first[n-1] and len(S2)==second[n-1]
        assert S2 <= S1
        print('length',n,'one',len(S1),'two',len(S2))
    print('PASS: independently enumerated all input blocks through output length 12')
if __name__=='__main__':main()
