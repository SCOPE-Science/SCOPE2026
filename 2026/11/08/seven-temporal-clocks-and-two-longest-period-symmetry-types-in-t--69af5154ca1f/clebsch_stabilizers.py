from clebsch_symmetry import *

def orbit_states(x,p):
    res=[x]
    for _ in range(p-1):res.append(successor(res[-1]))
    assert successor(res[-1])==x
    return res
for x,p in [(95477,16),(94517,16),(7766,13)]:
    states=orbit_states(x,p)
    sym=[]
    for perm in itertools.permutations(range(5)):
        for shift in range(16):
            gm=graph_automorphism_affine(perm,shift)
            y=apply(x,gm)
            if y in states:
                sym.append((shift,perm,states.index(y)))
    print('REP',x,'period',p,'stabilizer_size',len(sym),'shifts',sym)
    # Check uniform excitation over vertices
    exc=[0]*16
    for a in states:
        for j in range(16):exc[j]+= (a//pow3[j])%3==1
    print('EXC_PER_VERTEX',exc)
