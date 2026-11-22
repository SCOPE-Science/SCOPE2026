"""Finite-group sanity checks for the shift-power theorem.

This tests representative nonabelian groups of orders eight and 27.
The infinite-configuration conclusion uses the proof, not these finite tests.
"""
from itertools import product
from random import Random

class FiniteGroup:
    def __init__(self,name,elements,mul,unit,generators):
        self.name=name; self.E=list(elements);self.mul=mul;self.e=unit;self.generators=generators
        self.power=lambda x,n:self._power(x,n)
        self.inv={x: next(y for y in self.E if mul(x,y)==unit and mul(y,x)==unit) for x in self.E}
        self.center={x for x in self.E if all(mul(x,y)==mul(y,x) for y in self.E)}
    def _power(self,x,n):
        y=self.e
        for _ in range(n): y=self.mul(y,x)
        return y
    def homs(self):
        # Propagate the chosen images along the complete Cayley graph.
        results=[]; gens=self.generators
        for im in product(self.E, repeat=len(gens)):
            h={self.e:self.e}; stack=[self.e]; good=True
            while stack and good:
                x=stack.pop()
                for g,v in zip(gens,im):
                    y=self.mul(x,g); z=self.mul(h[x],v)
                    if y in h:
                        if h[y]!=z:good=False;break
                    else:h[y]=z;stack.append(y)
            if not good or len(h)!=len(self.E):continue
            if any(h[self.mul(x,y)]!=self.mul(h[x],h[y]) for x in self.E for y in self.E):raise ValueError('not hom')
            results.append(h)
        return results

def make_groups():
    D4=FiniteGroup('D4',product(range(4),range(2)),lambda x,y:((x[0]+(-1)**x[1]*y[0])%4,(x[1]+y[1])%2),(0,0),[(1,0),(0,1)])
    Q8=FiniteGroup('Q8',product(range(4),range(2)),lambda x,y:((x[0]+(-1)**x[1]*y[0]+2*x[1]*y[1])%4,(x[1]+y[1])%2),(0,0),[(1,0),(0,1)])
    H3=FiniteGroup('H3(F3)',product(range(3),repeat=3),lambda x,y:((x[0]+y[0])%3,(x[1]+y[1])%3,(x[2]+y[2]+x[0]*y[1])%3),(0,0,0),[(1,0,0),(0,1,0)])
    M27=FiniteGroup('M27',product(range(9),range(3)),lambda x,y:((x[0]+pow(4,x[1],9)*y[0])%9,(x[1]+y[1])%3),(0,0),[(1,0),(0,1)])
    return [D4,Q8,H3,M27]

def iter_F(G,alpha,chars,offsets,x):
    N=len(x); m=G.mul
    return tuple(_prod(G,[alpha[x[(i+offsets[0])%N]]] + [h[x[(i+shift)%N]] for h,shift in zip(chars,offsets[1:])]) for i in range(N))

def _prod(G,lst):
    x=G.e
    for y in lst:x=G.mul(x,y)
    return x

def test():
    rng=Random(177)
    totals={}
    for G in make_groups():
        homs=G.homs();auts=[h for h in homs if len(set(h.values()))==len(G.E)]
        central=[h for h in homs if set(h.values())<=G.center]
        commutators={G.mul(G.mul(G.mul(x,y),G.inv[x]),G.inv[y]) for x in G.E for y in G.E}
        assert len(G.center)==(2 if len(G.E)==8 else 3)
        assert G.center==commutators
        assert all(h[z]==G.e for h in central for z in G.center)
        assert all(all(G.mul(x,y)==G.mul(y,x) for x in set(h.values()) for y in set(h.values())) for h in homs if h not in auts)
        assert all(all(G.mul(x,y)==G.mul(y,x) for x in G.E for y in set(c.values())) for c in central)
        p=len(G.center)
        # Count surjective commuting-image two-site local maps independently
        # of the automorphism/central decomposition formula.
        classes={}
        for h in homs:
            image=frozenset(h.values())
            classes[image]=classes.get(image,0)+1
        two_site_onto=0
        for A,weight_A in classes.items():
            for B,weight_B in classes.items():
                if any(G.mul(a,b)!=G.mul(b,a) for a in A for b in B):
                    continue
                if len({G.mul(a,b) for a in A for b in B})==len(G.E):
                    two_site_onto+=weight_A*weight_B
        assert two_site_onto==2*len(auts)*p*p, (G.name,two_site_onto)
        count=0;maxL=0
        # Multiple independent offsets and central perturbations.
        for _ in range(75):
            alpha=rng.choice(auts)
            c1=rng.choice(central);c2=rng.choice(central)
            ord_alpha=1; h={x:alpha[x] for x in G.E}
            while any(h[x]!=x for x in G.E):
                h={x:alpha[h[x]] for x in G.E};ord_alpha+=1
            L=p*ord_alpha;maxL=max(maxL,L)
            k=rng.choice([-2,-1,0,1,2]); j1,j2=k+2,k-1
            x=tuple(rng.choice(G.E) for _ in range(7))
            fx=x
            for n in range(L):fx=iter_F(G,alpha,[c1,c2],[k,j1,j2],fx)
            shift=tuple(x[(i+k*L)%len(x)] for i in range(len(x)))
            assert fx==shift,(G.name,k,L)
            count+=1
        totals[G.name]={'order':len(G.E),'endos':len(homs),'automorphisms':len(auts),'central_homs':len(central),'two_site_surjective_rules':two_site_onto,'verified_shift_powers':count,'max_tested_exponent':maxL}
    for name,record in totals.items():print(name,record)
    print('All checks passed')
if __name__=='__main__':test()
