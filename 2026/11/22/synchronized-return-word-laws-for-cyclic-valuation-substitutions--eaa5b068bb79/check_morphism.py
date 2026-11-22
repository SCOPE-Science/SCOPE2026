"""Second implementation: block transduction and exact arithmetic cell probabilities."""
from fractions import Fraction

def val(t,b):
    ans=0
    while not t%b:
        t//=b
        ans+=1
    return ans


def substitution(s,b,q):
    return tuple([0]*(b-1)+[(s+1)%q])


def code(s,b,q):
    return tuple([0]*(b-2)+ ([0,0] if s==q-1 else [s+1]))

case_count=0
prefix_positions=0
for b in range(2,8):
    for q in range(2,7):
        u=(0,)
        for _ in range(7):
            u=tuple(a for t in u for a in substitution(t,b,q))
            if len(u)>300000: break
        U=tuple(val(t,b)%q for t in range(1,len(u)+1))
        assert U==u, (b,q)
        g=tuple(a for s in U for a in code(s,b,q))
        positions=[t for t in range(1,len(U)+1) if U[t-1]==0]
        direct=tuple(0 if nxt-prev==1 else U[prev] for prev,nxt in zip(positions,positions[1:]))
        assert g[:len(direct)]==direct, (b,q)
        probability=[1-sum(Fraction(1,b**s) for s in range(1,q))]+[Fraction(1,b**s) for s in range(1,q)]
        assert sum(probability)==1 and all(p>0 for p in probability)
        for r in range(q):
            d=Fraction(b-1,b**(r+1))*1/(1-Fraction(1,b**q))
            avg=b**r*sum(probability[s]*(1 if s==0 else 2) for s in range(q))
            assert avg*d==1, (b,q,r)
        case_count+=1
        prefix_positions += len(direct)
print('PASS independent morphism / density checker')
print('base-modulus pairs:',case_count)
print('derived sequence symbols compared:',prefix_positions)
print('exact probability normalization and reciprocal-density identities verified')
