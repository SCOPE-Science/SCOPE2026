#!/usr/bin/env python3
"""Independent square-block BFS, exhaustively bounded by length 96.
No third-party modules. Run: python3 verify_by_blocks.py
"""
from pathlib import Path

def avoids_overlap(w):
    n=len(w)
    for p in range(1,(n-1)//2+1):
        for start in range(n-2*p):
            if all(w[start+j]==w[start+p+j] for j in range(p+1)):
                return False
    return True

def main():
    expected={}
    for line in Path(__file__).with_name('census_96.tsv').read_text().splitlines()[1:]:
        n,w,parts=line.split('\t');expected[w]=(int(n),tuple(map(int,parts.split(','))))
    roots=['']
    squareblocks=[]
    # At least eight other nonempty squares require 16 positions, so
    # no constituent square in a nine-block product of length <=96 can
    # exceed 80 positions (root length <=40).
    for h in range(1,41):
        roots=[w+c for w in roots for c in '01' if avoids_overlap(w+c)]
        squareblocks.extend(w+w for w in roots if avoids_overlap(w+w))
    assert len(squareblocks)==154
    squareblocks=sorted(set(squareblocks),key=lambda w:(len(w),w))
    assert len(squareblocks)==154
    state={'':{()}}
    levels=[]
    for k in range(1,10):
        nxt={}
        for w,recipes in state.items():
            for b in squareblocks:
                if len(w)+len(b)+2*(9-k)>96:break
                z=w+b
                if not avoids_overlap(z):continue
                for recipe in recipes:
                    nxt.setdefault(z,set()).add(recipe+(len(b)//2,))
        state=nxt
        levels.append((len(state),sum(map(len,state.values()))))
    assert levels==[(154,154),(104,104),(120,120),(146,146),(82,82),(60,60),(70,70),(60,60),(12,12)],levels
    assert set(state)==set(expected)
    assert all(len(paths)==1 and (len(w),next(iter(paths)))==expected[w] for w,paths in state.items())
    print('BY_BLOCKS_PASS squares=154 levels=',levels)
if __name__=='__main__':main()
