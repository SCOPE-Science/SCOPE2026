"""Construct and independently check shortest identifying sensor layouts on ladders.

Run: python3 construct_witnesses.py. Pure Python, no external libraries.
"""
from itertools import product


def valid_window(n, centre, window):
    def seen(i, row):
        return frozenset(2*j+r for j,r in
                         ((i,row),(i,1-row),(i-1,row),(i+1,row))
                         if 0 <= j < n and (window[j-centre+1] >> r)&1)
    for row in (0,1):
        src=seen(centre,row)
        if not src:
            return False
        for j in range(centre, min(n-1, centre+2)+1):
            for r in (0,1):
                if (j,r)>(centre,row) and src==seen(j,r):
                    return False
    return True


def optimum(n):
    paths={(0,0,0,0):(0,())}
    for position in range(n+3):
        new={}
        for state,(cost,seq) in paths.items():
            for mask in (range(4) if position<n else (0,)):
                q=state+(mask,)
                centre=position-3
                if centre>=0 and not valid_window(n,centre,q):
                    continue
                after=q[1:]
                proposal=(cost+mask.bit_count(), seq+((mask,) if position<n else ()))
                if after not in new or proposal<new[after]:
                    new[after]=proposal
        paths=new
    return min(paths.values())


def verify(n, word):
    S={2*i+row for i,mask in enumerate(word) for row in (0,1) if mask & (1<<row)}
    signature=[]
    for i in range(n):
        for row in (0,1):
            near={(i,row),(i,1-row),(i-1,row),(i+1,row)}
            signature.append(frozenset(2*j+r for j,r in near if 0<=j<n and 2*j+r in S))
    return all(signature) and len(set(signature))==2*n


if __name__=='__main__':
    expected = {2:3,3:3,4:4,5:5,6:6,7:6,8:8,9:9,10:9,11:10,12:11,13:12}
    for n, claimed in expected.items():
        size, word=optimum(n)
        assert size==claimed and verify(n,word)
        print(n, size, ''.join(str(x) for x in word))
    print('WITNESSES_OK')
