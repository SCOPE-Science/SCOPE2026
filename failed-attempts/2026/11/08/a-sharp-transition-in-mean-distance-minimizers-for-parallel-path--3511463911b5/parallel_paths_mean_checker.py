"""Exact independent integration checks for multiedge network mean-distance formula.

Standard library only. Ordered pairs are integrated with rational polygon clipping.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def clip_polygon(poly, h):
    a, b, c = h
    def val(pt): return a*pt[0] + b*pt[1] + c
    ans = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        vp, vq = val(p), val(q)
        if vp <= 0: ans.append(p)
        if (vp < 0 < vq) or (vq < 0 < vp):
            ans.append(((vq*p[0] - vp*q[0])/(vq-vp),
                        (vq*p[1] - vp*q[1])/(vq-vp)))
    return ans


def integrate_affine(poly, f):
    if len(poly) < 3: return F(0)
    u, v, w = f
    s = F(0)
    for p, q in zip(poly, poly[1:] + poly[:1]):
        cross = p[0]*q[1] - p[1]*q[0]
        s += cross * (u*(p[0]+q[0])+v*(p[1]+q[1])+3*w)/6
    return abs(s)


def exact_different(i, j, k):
    """Integral of four shortest-route affine functions on an i-by-j rectangle."""
    base = [(F(0),F(0)),(i,F(0)),(i,j),(F(0),j)]
    routes = [(F(1),F(1),F(0)), (-F(1),-F(1),i+j),
              (F(1),-F(1),j+k),(-F(1),F(1),i+k)]
    answer = F(0)
    for p, r in enumerate(routes):
        poly = base[:]
        for q, other in enumerate(routes):
            if p != q:
                poly = clip_polygon(poly, tuple(r[t]-other[t] for t in range(3)))
                if len(poly) < 3: break
        answer += integrate_affine(poly, r)
    return answer


def exact_same(i, k):
    """Direct elementary integral of min(t, i+k-t) against 2(i-t)dt."""
    if i <= k: return i**3/3
    z = (i+k)/2
    left = i*z*z/2 - z**3/3
    right = i*(i+k)*(i-z)-(2*i+k)*(i*i-z*z)/2+(i**3-z**3)/3
    return 2*(left+right)


def integrate_routes(lengths):
    out = F(0)
    for i, x in enumerate(lengths):
        out += exact_same(x, min(lengths[j] for j in range(len(lengths)) if j != i))
    for i,j in combinations(range(len(lengths)),2):
        out += 2*exact_different(lengths[i],lengths[j],
                    min(lengths[t] for t in range(len(lengths)) if t not in (i,j)))
    return out


def derived_formula(lengths):
    x = sorted(lengths)
    m = len(x); a = x[0]; other = x[1:]
    S = sum(other); Q = sum(y*y for y in other); R = sum(y**3 for y in other)
    return ((2*S+a)*Q-R)/4 + a*S*S/2 + F(7-2*m,4)*a*a*S + F(2*m*m-7*m+9,12)*a**3


def balanced_at_smallest(a, L, m):
    return derived_formula([a]+[(L-a)/F(m-1)]*(m-1))


def main():
    r = Random(20261106)
    count = 0
    for m in range(3,8):
        cases = [[F(z) for z in range(1,m+1)],
                 [F(1)]*m, [F(1)]*(m-1)+[F(19)],
                 [F(1)]+[F(5)]*(m-1),
                 [F(z,z+2) for z in range(1,m+1)]]
        for _ in range(12):
            cases.append([F(r.randint(1,14),r.randint(1,9)) for _ in range(m)])
        for xs in cases:
            assert integrate_routes(xs) == derived_formula(xs), (m,xs)
            L = sum(xs); a = min(xs)
            assert derived_formula(xs)>=balanced_at_smallest(a,L,m)
            bound = F(5,27)*L**3 if m == 3 else F(2*m-3,4*(m-1)**2)*L**3
            assert derived_formula(xs) >= bound
            count += 1
        L = F(1)
        equal = derived_formula([L/m]*m)
        limit = F(2*m-3,4*(m-1)**2)
        if m==3: assert equal == F(5,27) and equal < limit
        else: assert equal > limit
        for t in range(1,30):
            a = F(t,30*m)
            assert balanced_at_smallest(a,L,m) >= (equal if m==3 else limit)
    print('PARALLEL_PATHS_EXACT_INTEGRAL_AND_PHASE_TRANSITION_OK',count)

if __name__=='__main__': main()
