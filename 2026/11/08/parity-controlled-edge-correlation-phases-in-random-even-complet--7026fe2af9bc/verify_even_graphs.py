"""Exact finite tests of the edge-covariance phase law for even random graphs.

Uses independent direct enumeration of cycle-space words and a character-sum
formula for source-sector partition functions. No floating point arithmetic.
"""
from fractions import Fraction
from itertools import combinations


def cycle_space_counts(n):
    edges=list(combinations(range(n),2))
    edge_index={e:i for i,e in enumerate(edges)}
    triangles=[]
    for a,b in combinations(range(1,n),2):
        triangles.append(sum(1<<edge_index[e] for e in [(0,a),(0,b),(a,b)]))
    assert len(triangles)==(n-1)*(n-2)//2
    masks=[0]
    for tri in triangles:
        masks += [x^tri for x in masks]
    assert len(set(masks))==len(masks)
    e=1<<edge_index[(0,1)];a=1<<edge_index[(0,2)];d=1<<edge_index[(2,3)]
    m=len(edges)
    counts=[[0]*(m+1) for _ in range(4)]
    for mask in masks:
        k=mask.bit_count()
        x=bool(mask&e); y=bool(mask&a); z=bool(mask&d)
        for idx,ok in enumerate([True,x,x and y,x and z]):
            if ok:counts[idx][k]+=1
    return counts


def direct_cov(n,p,counts):
    m=n*(n-1)//2
    wt=[p**k*(1-p)**(m-k) for k in range(m+1)]
    normal=sum(c*w for c,w in zip(counts[0],wt))
    avg=[sum(c*w for c,w in zip(row,wt))/normal for row in counts]
    return avg[2]-avg[1]**2,avg[3]-avg[1]**2


def character_sectors(n,p):
    # Fourier inversion: Z_A(t)=2^{-n} sum_sign sigma_A prod_edges(1+t sigma_e).
    t=p/(1-p)
    z=[Fraction(0)]*3
    for mask in range(1<<n):
        sz=mask.bit_count();cut=sz*(n-sz)
        w=(1+t)**(n*(n-1)//2-cut)*(1-t)**cut
        z[0]+=w
        z[1]+=(-1 if ((mask&3).bit_count()%2) else 1)*w
        z[2]+=(-1 if ((mask&15).bit_count()%2) else 1)*w
    z=[x/(1<<n) for x in z]
    assert z[0]>0
    r2=z[1]/z[0];r4=z[2]/z[0]
    # At t=1 this expression has removable 0/0. Handle separately.
    if t==1:return Fraction(0),Fraction(0)
    scale=t*t/(1-t*t)**2
    return scale*r2*(1-r2),scale*(r4-r2*r2)


def run():
    checks=0
    ps=[Fraction(1,8),Fraction(1,4),Fraction(2,5),Fraction(1,2),
        Fraction(3,5),Fraction(3,4),Fraction(7,8)]
    for n in range(4,8):
        rows=cycle_space_counts(n)
        for p in ps:
            c_adj,c_dis=direct_cov(n,p,rows)
            f_adj,f_dis=character_sectors(n,p)
            assert c_adj==f_adj and c_dis==f_dis,(n,p,c_adj,c_dis,f_adj,f_dis)
            assert c_dis>0 if p!=Fraction(1,2) else c_dis==0,(n,p,c_dis)
            if n%2==0:
                expected=1 if p<Fraction(1,2) else (0 if p==Fraction(1,2) else -1)
            else:
                expected=0 if p==Fraction(1,2) else 1
            assert (c_adj>0)-(c_adj<0)==expected,(n,p,c_adj)
            checks+=4
    print(f'PASS: {checks} exact identities/sign assertions across n=4..7 and 7 rational p values')

if __name__=='__main__':run()
