#!/usr/bin/env python3
"""Exact rational certificate for higher-even distance energies of a regular hexagon.

Only Python's standard library is needed.  Usage:
    python hex_certifier.py certificate.json

The coefficient of t_i*t_j in a second-order jet is stored for i<=j.
For i=j, the Hessian entry equals twice this coefficient.
All integrations and matrix operations use rational arithmetic.
"""
import sys, json, hashlib
from math import comb, factorial
from fractions import Fraction as Q
from collections import defaultdict

DIM = 8
EXPONENTS = tuple(range(8, 25, 2))

class Jet:
    __slots__ = ("c", "lin", "quad")

    def __init__(self, c=0, lin=None, quad=None):
        self.c = Q(c)
        self.lin = lin if lin is not None else {}
        self.quad = quad if quad is not None else {}

    def __add__(self, other):
        if not isinstance(other, Jet):
            other = Jet(other)
        lin = defaultdict(Q, self.lin)
        quad = defaultdict(Q, self.quad)
        for k, v in other.lin.items():
            lin[k] += v
        for k, v in other.quad.items():
            quad[k] += v
        return Jet(self.c + other.c, dict(lin), dict(quad))

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.c, {i: -v for i, v in self.lin.items()},
                   {i: -v for i, v in self.quad.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Jet) else Jet(-other))

    def __mul__(self, other):
        if not isinstance(other, Jet):
            return Jet(self.c * other,
                       {i: v * other for i, v in self.lin.items()},
                       {i: v * other for i, v in self.quad.items()})
        lin = defaultdict(Q)
        quad = defaultdict(Q)
        for i, v in self.lin.items():
            lin[i] += v * other.c
        for i, v in other.lin.items():
            lin[i] += v * self.c
        for i, v in self.quad.items():
            quad[i] += v * other.c
        for i, v in other.quad.items():
            quad[i] += v * self.c
        for i, v in self.lin.items():
            for j, w in other.lin.items():
                quad[(min(i, j), max(i, j))] += v * w
        return Jet(self.c * other.c, dict(lin), dict(quad))

    __rmul__ = __mul__

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        out = Jet(1)
        x = self
        while power:
            if power & 1:
                out = out * x
            power //= 2
            if power:
                x = x * x
        return out

    def gradient(self):
        return [self.lin.get(i, Q(0)) for i in range(DIM)]

    def hessian(self):
        return [[self.quad.get((min(i, j), max(i, j)), Q(0)) *
                 (2 if i == j else 1) for j in range(DIM)] for i in range(DIM)]


def vertex_coordinate(const, free_index=None):
    return Jet(const, {} if free_index is None else {free_index: Q(1)})

BASE_VERTICES = ((2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1))
FREE_VERTICES = (1, 2, 4, 5)
VERTICES = []
for vertex_no, (u, v) in enumerate(BASE_VERTICES):
    if vertex_no in FREE_VERTICES:
        j = FREE_VERTICES.index(vertex_no)
        VERTICES.append((vertex_coordinate(u, 2*j), vertex_coordinate(v, 2*j+1)))
    else:
        VERTICES.append((vertex_coordinate(u), vertex_coordinate(v)))


def all_moments(degree):
    """Integral of u**a * v**b over the moving hexagon, for a+b<=degree.

    The origin-to-edge triangle with vertices 0,U,V contributes
    det(U,V)*sum_{p,q} binom(a,p)binom(b,q)
    U_u**p V_u**(a-p) U_v**q V_v**(b-q)
    *(p+q)!*(a+b-p-q)!/(a+b+2)!.
    This follows from the two-simplex beta integral.
    """
    index = [(a, b) for a in range(degree+1) for b in range(degree+1-a)]
    M = {(a, b): Jet() for a, b in index}
    fac = factorial
    for i in range(6):
        Uu, Uv = VERTICES[i]
        Vu, Vv = VERTICES[(i+1) % 6]
        det = Uu * Vv - Uv * Vu
        pow_u = [[z**p for p in range(degree+1)] for z in (Uu, Uv, Vu, Vv)]
        for a, b in index:
            s = Jet()
            denom = fac(a+b+2)
            for p in range(a+1):
                for q in range(b+1):
                    coeff = Q(comb(a,p)*comb(b,q)*fac(p+q)*fac(a+b-p-q), denom)
                    s += (coeff * pow_u[0][p] * pow_u[2][a-p]
                          * pow_u[1][q] * pow_u[3][b-q])
            M[(a, b)] += det * s
    return M


def energy(moment, k):
    """J=double integral ((u-u')**2+3(v-v')**2)**(k/2)."""
    assert k >= 2 and k % 2 == 0
    m = k//2
    J = Jet()
    for h in range(m+1):
        for i in range(2*h+1):
            for j in range(2*m-2*h+1):
                w = (comb(m,h)*3**(m-h)*(-1)**(2*m-i-j)*
                     comb(2*h,i)*comb(2*m-2*h,j))
                J += w*moment[(i,j)]*moment[(2*h-i,2*m-2*h-j)]
    return J


def hessian_certificate(k):
    moments = all_moments(k)
    A = moments[(0,0)]
    J = energy(moments,k)
    a,j = A.c,J.c
    b = (k+4)//2
    assert a == 6 and j > 0
    ga,gj = A.gradient(),J.gradient()
    assert all(a*gj[i] == b*j*ga[i] for i in range(DIM)), 'Stationarity failed'
    HA,HJ = A.hessian(),J.hessian()
    # The Hessian of J/A**b at a critical point is K/A**(b+2),
    # K=a*a*HJ-b*j*a*HA+b*(1-b)*j*ga*ga^T.
    K = [[a*a*HJ[i][j0] - b*j*a*HA[i][j0] +
          b*(1-b)*j*ga[i]*ga[j0] for j0 in range(DIM)] for i in range(DIM)]
    assert all(K[i][j0] == K[j0][i] for i in range(DIM) for j0 in range(DIM))
    # Exact rational LDL^T decomposition, with all pivots strictly positive.
    L = [[Q(0) for _ in range(DIM)] for _ in range(DIM)]
    D = [Q(0)]*DIM
    for i in range(DIM):
        D[i] = K[i][i] - sum(L[i][h]**2*D[h] for h in range(i))
        assert D[i] > 0, f'Exponent {k}, pivot {i+1} is not positive'
        L[i][i] = Q(1)
        for t in range(i+1,DIM):
            L[t][i] = (K[t][i]-sum(L[t][h]*D[h]*L[i][h]
                                   for h in range(i)))/D[i]
    assert all(sum(L[i][h]*D[h]*L[j0][h] for h in range(DIM)) == K[i][j0]
               for i in range(DIM) for j0 in range(DIM))
    return {'exponent':k,'area':str(a),'energy_numerator':str(j),
            'hessian_K':[[str(v) for v in row] for row in K],
            'ldl_pivots':[str(v) for v in D]}


def run(cert_path):
    with open(cert_path,'r',encoding='utf8') as f:
        expected=json.load(f)
    assert expected['coordinate_chart']=='(u,v)->(u/2,sqrt(3)*v/2)'
    assert expected['fixed_vertices']==[0,3]
    assert expected['free_vertices']==[1,2,4,5]
    assert [c['exponent'] for c in expected['certificates']]==list(EXPONENTS)
    for entry in expected['certificates']:
        result=hessian_certificate(entry['exponent'])
        assert result==entry, f"Certificate mismatch at k={entry['exponent']}"
        print('k=%d: stationary; 8 positive exact pivots; certificate matches' % entry['exponent'],flush=True)
    print('PASS: 9 powers, 72 positive rational pivots, 576 matrix comparisons')

if __name__=='__main__':
    assert len(sys.argv)==2
    run(sys.argv[1])
