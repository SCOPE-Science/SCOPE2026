"""Exact rational supplementary tests for a sharp weighted-variation isotonic bound.

Python 3 standard library only. The theorem for all sizes is proved analytically.
"""
from fractions import Fraction as F
from itertools import product


def edges_of(part, n):
    # part is a bitmask: break after vertex j iff bit j is set
    blocks = []
    left = 0
    for j in range(n-1):
        if part & (1 << j):
            blocks.append((left, j))
            left = j+1
    blocks.append((left, n-1))
    return blocks


def average_projection(v, a, blocks):
    out = list(v)
    for left, right in blocks:
        avg = sum((a[j]*v[j] for j in range(left, right+1)), F(0))/sum(a[left:right+1])
        for j in range(left, right+1):
            out[j] = avg
    return out


def variation(v, w):
    return sum((w[j]*abs(v[j+1]-v[j]) for j in range(len(w))), F(0))


def chord_coefficient(a, w):
    n = len(a)
    q = [F(0)]
    for mass in a:
        q.append(q[-1]+mass)
    ww = [F(0)] + list(w) + [F(0)]
    val = F(1)
    for i in range(1,n):
        for p in range(i+1):
            for r in range(i,n+1):
                if p == r:
                    continue
                chord = ((q[r]-q[i])*ww[p]+(q[i]-q[p])*ww[r])/(q[r]-q[p])
                val = max(val, chord/ww[i])
    return val


def local_operator_coefficient(a,w,blocks):
    n=len(a)
    best=F(0)
    for i in range(n-1):
        step=[F(int(j>i)) for j in range(n)]
        projected=average_projection(step,a,blocks)
        best=max(best,variation(projected,w)/w[i])
    return best


def pava(v,a):
    blocks=[]
    for i in range(len(a)):
        blocks.append((i,i,a[i]*v[i],a[i]))
        while len(blocks)>1 and blocks[-2][2]*blocks[-1][3]>blocks[-1][2]*blocks[-2][3]:
            x=blocks.pop(); z=blocks.pop()
            blocks.append((z[0],x[1],z[2]+x[2],z[3]+x[3]))
    result=list(v)
    for l,r,total,mass in blocks:
        result[l:r+1]=[total/mass]*(r-l+1)
    return result


def run():
    tests=0
    mass_sets=[[F(x) for x in values] for values in [(1,2,1,3,2,4,1),(3,1,4,1,5,2,2),(1,1,1,1,1,1,1)]]
    weight_sets=[[F(x) for x in values] for values in [(1,2,4,1,3,2),(2,1,1,4,1,5),(1,1,1,1,1,1),(1,4,1,4,1,4)]]
    for n in range(2,8):
        for base_a in mass_sets:
            a=base_a[:n]
            for base_w in weight_sets:
                w=base_w[:n-1]
                target=chord_coefficient(a,w)
                norms=[local_operator_coefficient(a,w,edges_of(part,n)) for part in range(1<<(n-1))]
                assert max(norms)==target, (n,a,w,target,max(norms))
                tests+=len(norms)*(n-1)
                # The concavity criterion exactly matches target == 1.
                ww=[F(0)]+w+[F(0)]
                concave=all((ww[i]-ww[i-1])/a[i-1] >= (ww[i+1]-ww[i])/a[i] for i in range(1,n))
                assert (target==1)==concave
                tests+=1
    # Explicit attainment at a three-block face.
    a=[F(1)]*4; w=[F(1),F(1,4),F(1)]
    y=[F(0),F(3),F(1),F(5)]
    y2=[F(0),F(3),F(3,2),F(11,2)]
    assert pava(y,a)==[F(0),F(2),F(2),F(5)]
    assert pava(y2,a)==[F(0),F(9,4),F(9,4),F(11,2)]
    delta=[y2[j]-y[j] for j in range(4)]
    delta_out=[pava(y2,a)[j]-pava(y,a)[j] for j in range(4)]
    assert variation(delta_out,w)==4*variation(delta,w)
    assert chord_coefficient(a,w)==4
    tests+=4
    # Independently test sampled pairs, including data where pooling changes.
    for n in range(2,7):
        for a0 in [(1,2,1,3,2,4),(3,1,2,1,4,1)]:
            a=[F(v) for v in a0[:n]]
            w=[F(v) for v in (1,3,1,2,5)[:n-1]]
            L=chord_coefficient(a,w)
            pool=[-2,-1,0,1,3]
            for seed in range(90):
                x=[F(pool[(seed*3+j*7+j*j)%5]) for j in range(n)]
                z=[F(pool[(seed*11+j*3+2*j*j+1)%5]) for j in range(n)]
                assert variation([u-v for u,v in zip(pava(x,a),pava(z,a))],w)<=L*variation([u-v for u,v in zip(x,z)],w)
                tests+=1
    print('PASS: %d exact rational comparisons'%tests)

if __name__=='__main__':
    run()
