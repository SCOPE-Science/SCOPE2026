import sympy as s,sys
sys.path.insert(0,'/tmp')
import kkcore as k
x,y,z=s.symbols('x y z')
i=s.I;r=s.sqrt(5)
def CV(q):return q[0]+q[1]*i+q[2]*r+q[3]*i*r
F=x**4+y**4+z**4+3*(x*x*y*y+x*x*z*z+y*y*z*z)
for n,line in enumerate(k.L,1):
 a,b,c=map(CV,line)
 if c!=0:V=s.together(F.subs(z,-(a*x+b*y)/c))
 elif b!=0:V=s.together(F.subs(y,-a*x/b))
 else:V=s.together(F.subs(x,-b*y/a))
 num=s.together(V).as_numer_denom()[0]
 fac=s.factor_list(num,gens=(x,y) if c!=0 else (x,z),extension=[i,r])[1]
 print(n,[(s.total_degree(h),m) for h,m in fac],flush=True)
 assert all(m%2==0 for _,m in fac)
print('ALL 28 BITANGENTS VERIFIED')
