import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import eu, es, B, Binv
# Sharp per-k bound via the ACTUAL sinusoidal structure (not generic L2):
# r(y)=1+0.04 sin(2pi y1)+0.03 cos(2pi y2). For mode-1 (x1 only): Q^(1)(y) = 0.04[sin(2pi(y1+u1+v1))-sin(2pi(y1+u1))-sin(2pi(y1+v1))+sin(2pi y1)]
# = 0.04*(e(2pi u1)-1)(e(2pi v1)-1) sin/cos factor: |Q| <= 0.04*|e(u1)-1|*|e(v1)-1| <= 0.04*min(2,2pi|u1|)*min(2,2pi|v1|).
# grad: dQ/dy1 = 0.04*2pi*(e(u1)-1)(e(v1)-1)*trig, |dQ/dy1|<=0.04*2pi*Fu*Fv; mode-2 similar with 0.03.
# Then |grad_x S_k| <= ||B^k|| times |grad Q| but SHARPER: (B^k)^T g with g=(g1,g2): use |.|<= lam^k (|g1|+|g2|)? Since B symmetric, ||(B^k)^T g|| <= lam^k|g|. Keep lam^k but with tight |g|.
# u = a lam^k eu (lift, exact), v = b mu^k es.
e1=np.abs(eu); e2=np.abs(es)
print("eu",eu,"es",es)
def bounds(h,K1,a_sign=1.0):
    tot=0.0
    for k in range(K1+1):
        u=np.abs(h)*lam**k*e1; v=np.abs(h)*mu**k*e2
        Fu=np.minimum(2,2*np.pi*u); Fv=np.minimum(2,2*np.pi*v)
        g1=0.04*2*np.pi*Fu[0]*Fv[0]; g2=0.03*2*np.pi*Fu[1]*Fv[1]
        tot+=lam**k*(g1+g2)
    for j in range(1,K1+1):
        u=np.abs(h)*lam**j*e1; v=np.abs(h)*mu**j*e2  # backward: roles swap? Bi: u'=a mu^j eu (contracting), v'=b lam^j es (expanding)
        u=np.abs(h)*mu**j*e1; v=np.abs(h)*lam**j*e2
        Fu=np.minimum(2,2*np.pi*u); Fv=np.minimum(2,2*np.pi*v)
        g1=0.04*2*np.pi*Fu[0]*Fv[0]; g2=0.03*2*np.pi*Fu[1]*Fv[1]
        tot+=lam**j*(g1+g2)
    return tot
lam=(3+np.sqrt(5))/2; mu=(3-np.sqrt(5))/2
for h in [0.05,0.03,0.015]:
    for K1 in [8,12,16]:
        print("h",h,"K1",K1,"sharp-L",round(float(bounds(h,K1)),4))
