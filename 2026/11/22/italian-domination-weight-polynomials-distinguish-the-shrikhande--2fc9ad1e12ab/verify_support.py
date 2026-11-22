"""Exact positive-support computation of Italian-domination weight polynomials.
No nonstandard packages are required.
"""
from math import comb
from itertools import combinations

EXPECTED_DIFFERENCE = {4:8,5:224,6:1184,7:1408,8:1176,9:832,10:640,11:256}

def neighborhoods(kind):
    vertices=[(i,j) for i in range(4) for j in range(4)]
    ans=[]
    deltas={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    for a,b in vertices:
        mask=0
        for idx,(c,d) in enumerate(vertices):
            if kind=='rook':
                adjacent=((a==c) != (b==d))
            else:
                adjacent=(((c-a)%4,(d-b)%4) in deltas)
            if adjacent:mask|=1<<idx
        assert mask.bit_count()==6
        ans.append(mask)
    return ans

def poly(kind):
    nb=neighborhoods(kind)
    coeff=[0]*33
    # Each positive support S is processed exactly once. All zero vertices must
    # see at least one positive neighbor; a unique such neighbor must be 2.
    for S in range(1<<16):
        outside=((1<<16)-1)^S
        forced=0
        feasible=True
        while outside:
            v=(outside & -outside).bit_length()-1
            outside &= outside-1
            defended=nb[v]&S
            if not defended:
                feasible=False;break
            if defended.bit_count()==1:
                forced |= defended
        if not feasible:continue
        size=S.bit_count()
        k=forced.bit_count()
        # Forced labels are 2; other selected vertices have label 1 or 2.
        for twos in range(size-k+1):
            w=size+k+twos
            coeff[w] += comb(size-k,twos)
    return coeff

def four_cocliques(kind):
    nb=neighborhoods(kind)
    sets=[]
    for combo in combinations(range(16),4):
        mask=sum(1<<i for i in combo)
        if all((nb[v]&mask)==0 for v in combo):
            # Parameters (16,6,2,2) imply that each outsider has 2 neighbors.
            assert all((nb[v]&mask).bit_count()==2 for v in range(16) if v not in combo)
            sets.append(combo)
    return sets

if __name__=='__main__':
    rook=poly('rook');shri=poly('shrikhande')
    expected=[0]*33
    for k,delta in EXPECTED_DIFFERENCE.items(): expected[k]=delta
    assert [a-b for a,b in zip(rook,shri)] == expected
    assert rook[4]==24 and shri[4]==16
    assert len(four_cocliques('rook'))==24
    assert len(four_cocliques('shrikhande'))==16
    assert all(a==b for a,b in zip(rook[12:],shri[12:]))
    print('ROOK_COEFFICIENTS',rook)
    print('SHRIKHANDE_COEFFICIENTS',shri)
    print('DIFFERENCE',expected)
    print('MINIMUM_COUNTS',rook[4],shri[4])
    print('SUPPORT_ENUMERATION_OK')
