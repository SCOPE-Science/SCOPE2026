"""Exact Walsh sampling check for the 14 Dyck words of semilength four.
Requires Python 3 and SymPy; no external data files.
"""
from itertools import combinations
from sympy import Matrix, Symbol, factor

N=8
paths=[]
for mask in range(1<<N):
    if mask.bit_count()!=4:
        continue
    height=0
    for i in range(N):
        height += 1 if (mask>>i)&1 else -1
        if height<0:
            break
    else:
        if height==0:
            paths.append(mask)
assert len(paths)==14

z=Symbol('z')
expect2=z*(z-64)**3*(z-52)*(z-32)**3*(z-12)**3*(z**3-142*z**2+5576*z-58112)
expect3=(z-104)*(z-96)**3*(z-64)*(z**2-184*z+8192)**3*(z**3-294*z**2+28528*z-912896)
for degree,expect,rank in [(2,expect2,13),(3,expect3,14)]:
    frequencies=[sum(1<<i for i in s) for k in range(degree+1) for s in combinations(range(N),k)]
    M=Matrix([[(-1)**((p & f).bit_count()) for f in frequencies] for p in paths])
    gram=M*M.T
    assert gram.rank()==rank
    assert factor(gram.charpoly(z).as_expr()-expect)==0
    assert all(gram[i,i]==sum(__import__('math').comb(N,k) for k in range(degree+1)) for i in range(14))
    if degree==2:
        # The three disjoint adjacent swaps are at positions (2,3), (4,5), (6,7).
        # All eight outcomes lie among the 14 ballot words.
        sign=[]
        cube={}
        for t in range(8):
            w='U'+''.join('DU' if (t>>i)&1 else 'UD' for i in range(3))+'D'
            m=sum(1<<i for i,a in enumerate(w) if a=='U')
            assert m in paths
            cube[m]=(-1)**(t.bit_count())
        vec=Matrix([cube.get(p,0) for p in paths])
        assert M.T*vec == Matrix.zeros(len(frequencies),1)
        assert sum(1 for a in vec if a) == 8 and sum(vec) == 0
print('DIRECT_DYCK_WALSH_SPECTRA_PASS')
