"""Reproduce the exact parallel-edge metric graph median calculations.
Run with Python 3; no third-party packages are required.
"""
import math
import random


def integrate_min_rays(length, a, b):
    # Integral over [0,length] of min(y+a, length-y+b).
    t = (length+b-a)/2
    if t <= 0:
        return length*length/2+b*length
    if t >= length:
        return length*length/2+a*length
    return t*t/2+a*t+(length*length/2-length*t+t*t/2)+b*(length-t)


def arc_integral(z, circle_length):
    # Integral_0^z min(s,circle_length-s) ds.
    if z <= circle_length/2:
        return z*z/2
    return circle_length*z-z*z/2-circle_length**2/4


def exact_potential(lengths, edge, x):
    l = lengths[edge]
    b = min(lengths[k] for k in range(len(lengths)) if k != edge)
    s = arc_integral(x,l+b)+arc_integral(l-x,l+b)
    for k, lk in enumerate(lengths):
        if k == edge:
            continue
        h = min((lengths[j] for j in range(len(lengths)) if j not in (edge,k)),default=math.inf)
        s += integrate_min_rays(lk,min(x,l-x+h),min(l-x,x+h))
    return s/sum(lengths)


def vertex_formula(lengths):
    a=min(lengths); L=sum(lengths); m=len(lengths)
    return (sum(l*l for l in lengths)+2*a*L-m*a*a)/(4*L)


def lower_bound(lengths, edge, x):
    l=lengths[edge]; other=[k for k in range(len(lengths)) if k != edge]
    j=min(other,key=lambda k:lengths[k]); L=sum(lengths)
    return min(x,l-x)*sum(min(l,lengths[k]) for k in other if k!=j)/(4*L)


def sampled_integral(lengths, edge, x, n=2500):
    # Midpoint integration of actual shortest-path expressions, not the exact integral formula.
    L=sum(lengths); l=lengths[edge]
    h0=min(lengths[k] for k in range(len(lengths)) if k!=edge)
    sm=0.0
    for k,lk in enumerate(lengths):
        dy=lk/n
        if k==edge:
            for q in range(n):
                y=(q+.5)*dy; delta=abs(x-y)
                sm += min(delta,l+h0-delta)*dy
        else:
            h=min((lengths[j] for j in range(len(lengths)) if j not in (edge,k)),default=math.inf)
            for q in range(n):
                y=(q+.5)*dy
                sm += min(x+y,l-x+lk-y,x+h+lk-y,l-x+h+y)*dy
    return sm/L


def main():
    rng=random.Random(52120261108)
    count=0; max_gap_err=0.; max_quad_err=0.
    for m in range(2,10):
        for j in range(100):
            lengths=[math.exp(rng.uniform(-2,2)) for _ in range(m)]
            if j%3==0: lengths[0]=lengths[1]
            f0=vertex_formula(lengths)
            assert abs(exact_potential(lengths,0,0)-f0)<1e-11
            for i,l in enumerate(lengths):
                for t in (.03,.17,.46,.79,.97):
                    x=t*l; gap=exact_potential(lengths,i,x)-f0
                    b=lower_bound(lengths,i,x)
                    if m==2: assert abs(gap)<1e-11
                    else: assert gap+1e-11>=b>0
                    max_gap_err=max(max_gap_err,b-gap)
                    count+=1
            if j in (0,29,57):
                i=j % m; x=0.313*lengths[i]
                quad=sampled_integral(lengths,i,x)
                max_quad_err=max(max_quad_err,abs(quad-exact_potential(lengths,i,x)))
    assert max_quad_err<1e-5, max_quad_err
    assert abs(vertex_formula([1,1,1])-1/2)<1e-12
    print('PARALLEL_GRAPH_ARCLENGTH_MEDIAN_OK',count,
          'max_bound_excess',f'{max_gap_err:.3e}',
          'max_midpoint_error',f'{max_quad_err:.3e}')

if __name__=='__main__': main()
