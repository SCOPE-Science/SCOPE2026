"""Independent exact fourth/sixth spectral moment check by additive-energy counting.
Uses integer convolution counts on the 4096-element colour-configuration group.
Run with: python3 additive_energy.py
"""
from itertools import product

EDGES=((0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5))
N=6
Q=4
COLOURS=[x for x in product(range(4),repeat=N)
         if all(x[i]!=x[j] for i,j in EDGES)]
assert len(COLOURS)==264

def encode(x):
    return sum(v<<(2*i) for i,v in enumerate(x))

def add(a,b,group):
    if group=='klein':
        return a^b
    out=0
    for i in range(N):
        out |= (((a>>(2*i))+(b>>(2*i)))&3) <<(2*i)
    return out

def main():
    colors=[encode(x) for x in COLOURS]
    for group in ['cyclic','klein']:
        d2=[0]*4096
        for x in colors:
            for y in colors:
                d2[add(x,y,group)]+=1
        assert sum(d2)==264**2
        fourth=sum(v*v for v in d2)
        d3=[0]*4096
        for s,num in enumerate(d2):
            if num:
                for x in colors:
                    d3[add(s,x,group)]+=num
        assert sum(d3)==264**3
        sixth=sum(v*v for v in d3)
        expected=(2044416,87824400384) if group=='cyclic' else (2044416,87789010944)
        assert (fourth,sixth)==expected,(group,fourth,sixth)
        print(group,'pair and triple sum energy',(fourth,sixth))
    print('PASS: independent additive-energy enumeration')

if __name__=='__main__':main()
