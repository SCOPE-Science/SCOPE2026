"""Direct ambiguity enumeration for odd abelian coordinate crosses."""
import cmath
from itertools import product
from math import pi

def trial(a_moduli,b_moduli):
    moduli=tuple(a_moduli)+tuple(b_moduli)
    k=len(a_moduli)
    apts=list(product(*[range(m) for m in a_moduli]))
    bpts=list(product(*[range(m) for m in b_moduli]))
    group=list(product(*[range(m) for m in moduli]))
    zA=(0,)*len(a_moduli)
    zB=(0,)*len(b_moduli)
    S={tuple(a)+zB for a in apts}|{zA+tuple(b) for b in bpts}
    zeros=0
    for a in group:
        inter=[x for x in S if tuple((x[i]-a[i])%moduli[i] for i in range(len(moduli))) in S]
        for freq in group:
            val=sum(cmath.exp(2j*pi*sum(freq[i]*x[i]/moduli[i] for i in range(len(moduli)))) for x in inter)
            if abs(val)<1e-8:
                zeros+=1
    m=len(apts); n=len(bpts)
    expect=n*(m-1)**2+m*(n-1)**2
    assert zeros==expect,(moduli,zeros,expect)
    print('factors',a_moduli,b_moduli,'dimension',len(group),'nullity',zeros,'rank',len(group)**2-zeros)

trial((3,),(5,))
trial((3,3),(3,))
trial((9,),(3,))
print('ALL_ODD_GROUP_CROSS_RANK_CHECKS_OK')
