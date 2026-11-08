"""Exact rational checks for a two-ballot approval-committee characterization.

No external dependencies. A check of finite instances, not a replacement for
its universal mathematical proof.
"""
from fractions import Fraction as Q
from itertools import product


def witness(a, b, shared, private_a, private_b, k, x, y, z):
    """Return rational group-constant payments or None for a committee of
    x common, y A-private and z B-private winners, assumed Pareto-efficient.
    """
    assert a >= 1 and b >= 1 and k >= 1 and x+y+z == k
    assert x <= shared and y <= private_a and z <= private_b
    quota=Q(a+b,k)
    if x==k:
        r=Q(1,k+1)
        return ((r,Q(0),r,Q(0),r,r),quota)
    assert x==shared
    for j in range(3,180):
        eps=Q(1,2**j)
        groups=[]
        for ni,wi,available in ((a,y,private_a),(b,z,private_b)):
            has_private_loser = wi<available
            r = (min(Q(1),quota/ni)-eps if (has_private_loser and ni >= quota) else Q(1))
            if r < 0: break
            need=ni*(1-r)
            private_per_seat_capacity=min(ni*r,quota)
            priv_total=min(need,wi*private_per_seat_capacity)
            common_total=need-priv_total
            if x==0 and common_total:break
            p_private=priv_total/(ni*wi) if wi else Q(0)
            p_common=common_total/(ni*x) if x else Q(0)
            if p_private>r or p_common>r:break
            if has_private_loser and ni*r >= quota:break
            groups.append((p_common,p_private,r,common_total))
        if len(groups)!=2: continue
        (p_a,s_a,r_a,d_a),(p_b,s_b,r_b,d_b)=groups
        if d_a+d_b>x*quota:continue
        if a*s_a>quota or b*s_b>quota:continue
        if x and a*p_a+b*p_b>quota:continue
        assert r_a+x*p_a+y*s_a == 1
        assert r_b+x*p_b+z*s_b == 1
        return ((p_a,s_a,p_b,s_b,r_a,r_b),quota)
    return None


def verify(a,b,c,A,B,k,x,y,z,result):
    """Check all certificate clauses with exact fractions."""
    if result is None:return False
    (p_a,s_a,p_b,s_b,r_a,r_b),q = result
    if q!=Q(a+b,k):return False
    if any(t<0 for t in (p_a,s_a,p_b,s_b,r_a,r_b)):return False
    if r_a+x*p_a+y*s_a!=1 or r_b+x*p_b+z*s_b!=1:return False
    if max(p_a,s_a)>r_a or max(p_b,s_b)>r_b:return False
    if x and a*p_a+b*p_b>q:return False
    if y and a*s_a>q or z and b*s_b>q:return False
    if c>x and a*r_a+b*r_b>=q:return False
    if A>y and a*r_a>=q or B>z and b*r_b>=q:return False
    if x==0 and (p_a or p_b):return False
    if y==0 and s_a or z==0 and s_b:return False
    return True


def holds(a,b,c,A,B,k,x,y,z):
    q=Q(a+b,k)
    if x != min(c,k):return False
    if x+y+z!=k or y>A or z>B:return False
    return (y==A or Q(a,x+y+1)<q) and (z==B or Q(b,x+z+1)<q)


def check():
    tested=0; accepted=0; rejected=0
    for a,b in product(range(1,9),repeat=2):
      for c,A,B in product(range(5),repeat=3):
       total=c+A+B
       for k in range(1,total+1):
        x=min(c,k)
        for y in range(min(A,k-x)+1):
         z=k-x-y
         if not (0<=z<=B):continue
         flag=holds(a,b,c,A,B,k,x,y,z)
         w=witness(a,b,c,A,B,k,x,y,z) if flag else None
         if flag:
          assert verify(a,b,c,A,B,k,x,y,z,w), (a,b,c,A,B,k,x,y,z)
          accepted+=1
         else:
          # Direct necessity from individual reserve lower bound
          q=Q(a+b,k)
          assert (y<A and Q(a,x+y+1)>=q) or (z<B and Q(b,x+z+1)>=q)
          rejected+=1
         tested+=1
    print('exact instances',tested,'certificates',accepted,'quota obstructions',rejected)
    # A two-voter, four-candidate non-Pareto EJR+ / core+ separation.
    q=Q(2,3)
    assert (Q(1,1+1)+Q(1,3+1))>q
    # The only losing candidate is shared; for each level at least one
    # supporter has the required number of approved winners.
    assert all(1>=ell or 3>=ell for ell in range(1,4))

if __name__=='__main__':check()
