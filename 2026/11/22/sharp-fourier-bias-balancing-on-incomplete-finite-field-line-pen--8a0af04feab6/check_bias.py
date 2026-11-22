"""Standalone numerical cross-check of the finite-field pencil Fourier-bias theorem.

Runs on Python 3 standard library; direct DFTs are supplementary checks,
not a replacement for the analytic minimax argument.
"""
from itertools import combinations
from math import cos, sin, pi

class Field:
    def __init__(self, p, m, modulus):
        self.p, self.m, self.modulus = p, m, modulus
        self.q = p ** m
        assert len(modulus) == m + 1 and modulus[-1] == 1

    def digits(self, a):
        return [(a // self.p**i) % self.p for i in range(self.m)]

    def encode(self, d):
        return sum((x % self.p)*self.p**i for i, x in enumerate(d))

    def add(self, a, b):
        x, y = self.digits(a), self.digits(b)
        return self.encode([(x[i] + y[i]) % self.p for i in range(self.m)])

    def mul(self, a, b):
        x, y = self.digits(a), self.digits(b)
        z = [0]*(2*self.m-1)
        for i in range(self.m):
            for j in range(self.m):
                z[i+j] = (z[i+j]+x[i]*y[j]) % self.p
        for i in range(2*self.m-2, self.m-1, -1):
            coeff = z[i]
            for j in range(self.m):
                z[i-self.m+j] = (z[i-self.m+j] - coeff*self.modulus[j]) % self.p
        return self.encode(z[:self.m])

    def character(self, a):
        theta = 2*pi*(a%self.p)/self.p
        return complex(cos(theta), sin(theta))


def test_field(F):
    q = F.q
    # Verify basic field arithmetic, irreducibility of each chosen modulus.
    assert all(F.mul(a,b)!=0 for a in range(1,q) for b in range(1,q))
    dirs = [(1,t) for t in range(q)] + [(0,1)]
    all_points = [(a,b) for a in range(q) for b in range(q)]
    checks = 0
    ks = sorted(set(k for k in (2,3,q//2,q-1,q) if 2<=k<=q))
    for k in ks:
        choices = [tuple(range(k))]
        if q <= 7:
            choices += list(combinations(range(q+1),k))[:5]
        else:
            choices += [tuple(range(q+1-k,q+1))]
        for ids in set(choices):
            points = {(0,0)}
            for id in ids:
                vx,vy = dirs[id]
                points.update((F.mul(t,vx),F.mul(t,vy)) for t in range(1,q))
            assert len(points) == 1+k*(q-1)
            if q >= 2*k:
                alpha,beta = 0.0,1.0/(k*(q-1))
                expected = (q-k)/(k*(q-1))
            else:
                alpha = (2*k-q)/(q*(2*k-1))
                beta = 2/(q*(2*k-1))
                expected = 1/(2*k-1)
            assert alpha >=0 and beta >0
            assert abs(alpha+(len(points)-1)*beta-1)<1e-12
            measure = {x:alpha if x==(0,0) else beta for x in points}
            amplitudes=[]
            for xi,eta in all_points:
                val = sum(m*F.character(F.add(F.mul(x,xi), F.mul(y,eta))).conjugate()
                          for (x,y),m in measure.items())
                if (xi,eta)!=(0,0):
                    amplitudes.append(abs(val))
                else:
                    assert abs(val-1)<1e-11
            observed=max(amplitudes)
            assert abs(observed-expected)<5e-10, (q,k,ids,observed,expected)
            # The two frequency magnitudes are expected to be abs(alpha-k*beta)
            # and abs(alpha+(q-k)*beta), with the latter repeated k(q-1) times.
            low=abs(alpha-k*beta); high=abs(alpha+(q-k)*beta)
            assert sum(abs(v-high)<5e-10 for v in amplitudes)>=k*(q-1)
            assert sum(abs(v-low)<5e-10 for v in amplitudes)>=(q+1-k)*(q-1)
            checks+=len(amplitudes)
    return len(ks),checks

if __name__=='__main__':
    configs=[(2,1,[0,1]),(3,1,[0,1]),(5,1,[0,1]),(7,1,[0,1]),
             (11,1,[0,1]),(2,2,[1,1,1]),(2,3,[1,1,0,1]),(3,2,[1,0,1])]
    total=0
    for p,m,mod in configs:
        F=Field(p,m,mod)
        ks,n=test_field(F)
        total+=n
        print('q=%d: %d pencil sizes, %d tested nonzero Fourier coefficients, PASS' % (F.q,ks,n))
    print('TOTAL:',total,'nonzero Fourier-coefficient comparisons; all PASS')
