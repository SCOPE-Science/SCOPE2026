"""Independent finite checks of the penultimate-level criterion.
Run: python check_level.py
"""
from itertools import product, combinations_with_replacement

def membership(m, ks, x):
    if x < 0:
        return False
    residue=x % m
    return x>= (0 if residue==0 else residue+m*ks[residue-1])

def generators(m,ks):
    # At fixed multiplicity, all atoms other than m lie among Apéry representatives.
    ap=[r+m*ks[r-1] for r in range(1,m)]
    return [m]+[x for x in ap if not any(y!=x and membership(m,ks,x-y) for y in ap)]

def test():
    n_cases=0
    for m in range(3,8):
        count=0
        for ks in product(range(1,5),repeat=m-1):
            if not all(membership(m,ks,(i+m*ks[i-1])+(j+m*ks[j-1])) for i in range(1,m) for j in range(1,m)):
                continue
            count+=1
            atoms=generators(m,ks)
            ap=[r+m*ks[r-1] for r in range(1,m)]
            # An arbitrary positive semigroup element is m or an Apéry element plus a multiple of m;
            # a failing tuple can be reduced to the Apéry representatives without loss.
            failure=[]
            for tup in combinations_with_replacement(ap,m-1):
                if not membership(m,ks,sum(tup)-m):
                    failure.append(tup)
            if len(atoms)==2:
                assert failure==[(atoms[1],)*(m-1)],(m,ks,atoms,failure)
            else:
                assert not failure,(m,ks,atoms,failure)
            n_cases+=1
        print('multiplicity',m,'semigroups_tested',count)
    print('VERIFY_OK',n_cases)
if __name__=='__main__': test()
