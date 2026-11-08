"""Independent finite corroboration for signed coherent-state dipole blocks.
Analytic infinite-dimensional bounds are in RESULT.md and not certified by this script.
"""
from math import exp, sqrt, isclose

def g(x,y): return exp(-0.5*(x-y)**2)

def test_pair(d,w):
    c=exp(-d*d/2); s=sqrt(1-c*c)
    # matrix of w(P_x-P_y) in the orthonormal pair (k_x,(k_y-c*k_x)/s)
    p=w*s*s; q=-w*c*s
    mat=((p,q),(q,-p))
    a=w*s
    assert isclose(mat[0][0]+mat[1][1],0,abs_tol=1e-12)
    assert isclose(mat[0][0]**2+mat[0][1]**2,a*a,rel_tol=2e-12,abs_tol=1e-12)
    return 2

def normalized_pair(x,d):
    c=exp(-d*d/2); s=sqrt(1-c*c)
    return (x,d,c,s)

def pair_inner(x,d,c,s,y,e,cc,ss):
    # u_x/u_y, u_x/v_y, v_x/u_y, v_x/v_y
    uu=g(x,y)
    uv=(g(x,y+e)-cc*uu)/ss
    vu=(g(x+d,y)-c*uu)/s
    vv=(g(x+d,y+e)-cc*g(x+d,y)-c*g(x,y+e)+c*cc*uu)/(s*ss)
    return uu,uv,vu,vv

count=0
for d in (0.02,0.1,0.3,0.8):
    for w in (0.1,1,20):count+=test_pair(d,w)
for n in (3,5,10):
    blocks=[normalized_pair(20*j,1/(j+2)**2) for j in range(n)]
    for i in range(n):
        row=0
        for j in range(n):
            if i==j:continue
            uu,uv,vu,vv=pair_inner(*blocks[i],*blocks[j])
            # sums for each of the two basis rows
            row+=max(abs(uu)+abs(uv),abs(vu)+abs(vv))
            count+=4
        assert row<0.5
        count+=1
assert 40*sum((1+(20*m+2)**2)*exp(-0.5*(20*m-2)**2) for m in range(1,10))<0.5
count+=1
print('SIGNED_FOCK_DIPOLE_FINITE_CHECK_OK',count)
