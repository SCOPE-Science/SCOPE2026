#!/usr/bin/env python3
"""Exact-arithmetic verifier for an 8-to-9 bit two-deletion list-size-two threshold.
Usage: python3 checker.py certificate.json
No third-party packages are required.
"""
import json, sys
from fractions import Fraction
from itertools import combinations

def shadow(w):
    n=len(w)
    return {''.join(w[k] for k in range(n) if k not in (i,j)) for i,j in combinations(range(n),2)}

def valid(code):
    seen={}
    for w in code:
        for out in shadow(w):
            seen[out]=seen.get(out,0)+1
            if seen[out]>2:return False
    return True

words=[f'{i:08b}' for i in range(256)]
outs=[f'{i:06b}' for i in range(64)]
ix={s:i for i,s in enumerate(outs)}
columns=[set(ix[s] for s in shadow(w)) for w in words]
assert len(words)==256 and len(outs)==64

def check_tree(tree):
    leaves=[0]
    def rec(node,fixed):
        if 'split' in node:
            assert set(node)=={'split','zero','one'}
            j=node['split'];assert isinstance(j,int) and 0<=j<256 and j not in fixed
            fixed[j]=0;rec(node['zero'],fixed)
            fixed[j]=1;rec(node['one'],fixed)
            del fixed[j]
            return
        assert ('dual' in node)!=('over' in node)
        ones={j for j,v in fixed.items() if v==1}
        if 'over' in node:
            row=node['over'];assert isinstance(row,int) and 0<=row<64
            assert sum(row in columns[j] for j in ones)>=3
        else:
            assert set(node)=={'dual'}
            y=[Fraction(0)]*64; prev=-1
            for i,a,b in node['dual']:
                assert isinstance(i,int) and prev<i<64 and isinstance(a,int) and isinstance(b,int) and a>0 and b>0
                prev=i;y[i]=Fraction(a,b)
            residual=[2-sum(i in columns[j] for j in ones) for i in range(64)]
            assert min(residual)>=0
            free=(j for j in range(256) if j not in fixed)
            ub=Fraction(len(ones))+sum((y[i]*residual[i] for i in range(64)),Fraction(0))
            for j in free:
                cost=sum((y[i] for i in columns[j]),Fraction(0))
                if cost<1:ub+=1-cost
            assert ub<16,('dual failed',float(ub))
        leaves[0]+=1
    rec(tree,{})
    return leaves[0]

CODE8=['00000000','00000111','00001000','00011111','00110110','01000011','01010010','01110011','10001100','10111100','11001001','11100000','11110111','11111000','11111111']
CODE9=['000000000','000000111','000001000','000011111','000110110','001000011','001010010','001110011','010001100','010111100','011001001','011100000','011110111','011111000','011111111','101001101']

def main():
    c=json.load(open(sys.argv[1],encoding='utf8'))
    assert c['n']==8 and c['target']==16
    leaves=check_tree(c['tree'])
    assert len(CODE8)==15 and len(set(CODE8))==15 and all(len(w)==8 for w in CODE8)
    assert len(CODE9)==16 and len(set(CODE9))==16 and all(len(w)==9 for w in CODE9)
    assert valid(CODE8) and valid(CODE9)
    print('PASS: complete exact-rational branch tree for n=8; leaves',leaves)
    print('PASS: 15 valid n=8 words; 16 valid n=9 words')
    print('PASS: minimum binary length for 16 codewords is n=9')
if __name__=='__main__':main()
