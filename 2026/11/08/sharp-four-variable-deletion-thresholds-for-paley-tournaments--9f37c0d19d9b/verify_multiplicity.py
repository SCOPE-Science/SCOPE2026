"""Exhaustive certificate for low-order Paley tournament three-pattern witnesses.

No external dependencies. Uses explicit arithmetic in F_27 = F_3[X]/(X^3+2X+1).
"""
from itertools import combinations

ORDERS = (3,7,11,19,23,27,31,43,47,59)
EXPECTED = {3:0,7:0,11:0,19:1,23:1,27:2,31:2,43:3,47:4,59:5}

class Field:
    def __init__(self,q):
        self.q=q
        if q != 27:
            assert all(q%i for i in range(2,int(q**.5)+1)),q
            self.diff = [[(x-y)%q for y in range(q)] for x in range(q)]
            self.squares = {i*i%q for i in range(1,q)}
        else:
            # Polynomial T^3+2T+1 has no root in F3 and is irreducible.
            def digits(a):return (a%3,(a//3)%3,(a//9)%3)
            def val(v):return v[0]+3*v[1]+9*v[2]
            def mul(a,b):
                aa,bb=digits(a),digits(b);c=[0]*5
                for i in range(3):
                    for j in range(3): c[i+j]=(c[i+j]+aa[i]*bb[j])%3
                for deg in (4,3):
                    t=c[deg];c[deg]=0
                    c[deg-2]=(c[deg-2]+t)%3
                    c[deg-3]=(c[deg-3]+2*t)%3
                return val(c[:3])
            self.diff=[[val(tuple((a-b)%3 for a,b in zip(digits(x),digits(y))))
                        for y in range(q)] for x in range(q)]
            self.squares={mul(i,i) for i in range(1,q)}
            assert all((t*t*t+2*t+1)%3!=0 for t in range(3))
            assert len(self.squares)==13
        assert len(self.squares)==(q-1)//2
        assert 0 not in self.squares
        assert all(((x in self.squares) != (self.diff[0][x] in self.squares)) for x in range(1,q))
        self.bit=[[int(self.diff[x][a] in self.squares) for a in range(q)] for x in range(q)]

    def min_witness(self):
        q=self.q;best=q;best_trip=None;best_mask=None
        considered=0
        for a,b,c in combinations(range(q),3):
            counts=[0]*8
            for x in range(q):
                if x==a or x==b or x==c: continue
                mask=self.bit[x][a] | (self.bit[x][b]<<1) | (self.bit[x][c]<<2)
                counts[mask]+=1
            assert sum(counts)==q-3
            value=min(counts)
            if value<best:
                best=value;best_trip=(a,b,c)
                best_mask=counts.index(value)
            considered+=1
        assert considered == q*(q-1)*(q-2)//6
        return best,best_trip,best_mask,considered

if __name__=='__main__':
    for q in ORDERS:
        best,t,mask,n=Field(q).min_witness()
        assert best==EXPECTED[q],(q,best)
        print('q=%d minimum=%d triple=%s mask=%d triples=%d PASS'%(q,best,str(t),mask,n))
    print('ALL_LOW_ORDER_EXHAUSTIVE_CHECKS_PASS')
