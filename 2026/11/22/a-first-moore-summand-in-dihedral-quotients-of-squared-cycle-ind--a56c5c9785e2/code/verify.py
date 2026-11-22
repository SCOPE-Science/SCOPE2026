"""Exact, standard-library verification of the listed dihedral orbit complexes.

Run from this directory with: python3 verify.py
The finite enumeration and symbolic integer operations cover every n in [6,20].
"""
import sys
import os
from quot import qcomplex,modrank
from collapse import collapse
from reduce import reduce
from pi import pi

EXPECTED = {
 6:(1,),7:(1,),8:(1,),9:(1,),10:(1,),11:(1,),
 12:(1,0,1),13:(1,),14:(1,),15:(1,),
 16:(1,0,0,1),17:(1,0,0,2),18:(1,0,0,2),
 19:(1,0,0,2),20:(1,0,0,2,1),
}
# The residual ranks for n=20 are CHAIN GROUP ranks, not Betti ranks:
# the residual degree-four -> degree-three differential has sole nonzero entry 2.
CONTRACTIBLE = set(range(6,12)) | {13,14,15}
if len(sys.argv)==2 and sys.argv[1]=="mod20":
    START=21; END=20
else:
    START=int(sys.argv[1]) if len(sys.argv)>1 else 6
    END=int(sys.argv[2]) if len(sys.argv)>2 else 20
    assert 6<=START<=END<=20
MODE=os.environ.get("CHECK_MODE","all")
assert MODE in ("all","pi","reduction")
if MODE=="pi":
    for n in range(START,END+1):
        if n not in CONTRACTIBLE:
            group=pi(n)
            assert group["stuck"] is None and group["remaining_gens"]==0
            assert group["eliminations"]==group["edges"]
            print(n,"fundamental_group_trivial_OK",flush=True)
    print("SQUARED_CYCLE_DIHEDRAL_ORBIT_MOORE20_OK")
    sys.exit(0)
for n in range(START,END+1):
    result=reduce(n)
    chain=tuple(result['residual'])
    want=EXPECTED[n]
    assert chain[:len(want)]==want and all(x==0 for x in chain[len(want):]),(n,chain)
    nz=[(degree,columns,nonzero,values) for degree,columns,nonzero,values in result['nonunit'] if nonzero]
    if n==20:
        assert nz==[(4,1,1,[2])],nz
        assert result['cells']==[74,926,3717,6267,4662,1260]
        assert result['collapse_remaining']==[36,297,851,962,372,0]
        assert result['collapse_pairs']==7194
        assert result['unit_pivots']==[35,262,589,371,0]
    else:
        assert not nz,(n,nz)
    if n in CONTRACTIBLE:
        assert result['collapse_remaining']==[1]+[0]*(len(result['cells'])-1)
    else:
        if MODE=="all":
            group=pi(n)
            assert group['stuck'] is None and group['remaining_gens']==0,(n,group)
            assert group['eliminations']==group['edges'],(n,group)
    # Every elementary collapse removes one cell of each neighboring dimension.
    assert sum(result['cells'])-sum(result['collapse_remaining'])==2*result['collapse_pairs']
    # The integer chain differential determines this Euler characteristic.
    chi=sum((-1)**d*c for d,c in enumerate(result['cells']))
    after=sum((-1)**d*c for d,c in enumerate(result['residual']))
    assert chi==after,(n,chi,after)
    print(n,'chain_reduction',chain,('collapsible' if n in CONTRACTIBLE else ('pi1_trivial' if MODE=='all' else 'pi1_verified_separately')),'OK',flush=True)
# Independent modular ranks, computed from the original quotient orbit boundaries
# after certified elementary free-face collapses, corroborate the 2-primary defect.
if len(sys.argv)==2 and sys.argv[1]=="mod20":
 n=20
 B,D=qcomplex(n)
 A,_=collapse(B,n)
 for p,expected_ranks in [(2,[35,262,589,371,0]),(3,[35,262,589,372,0])]:
     ranks=[modrank([{i:v for i,v in col.items() if A[d-1][i]}
                    for j,col in enumerate(D[d-1]) if A[d][j]],p)
           for d in range(1,len(B))]
     assert ranks==expected_ranks,(p,ranks)
print('SQUARED_CYCLE_DIHEDRAL_ORBIT_MOORE20_OK')
