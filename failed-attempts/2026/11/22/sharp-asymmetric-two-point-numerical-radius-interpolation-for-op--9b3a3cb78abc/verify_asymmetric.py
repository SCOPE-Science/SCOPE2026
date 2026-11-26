import mpmath as m
m.mp.dps=55
count=0
for aa,bb,tt in [(1,1,m.mpf('0.8')),(m.mpf('0.4'),m.mpf('1.5'),m.mpf('0.3')),(m.mpf('1.7'),m.mpf('0.3'),m.mpf('0.65')),(m.mpf('0.2'),m.mpf('2'),m.mpf('0.93')),(m.mpf('1.2'),m.mpf('1.8'),m.mpf('0.07'))]:
 M=(aa+bb+m.sqrt((aa+bb)**2-4*tt**2*aa*bb))/(4*tt)
 u=aa/(2*M);v=-bb/(2*M)
 assert m.almosteq((u-v)/(1-u*v),tt);count+=1
 A=u+1/u;C=v+1/v
 x=1/(A-C);c=-C/(A-C)
 H=lambda y:c+x*(y+1/y)
 B=lambda z:(u-z)/(1-u*z)
 f=lambda z:2*M*(c*B(z)+x*(B(z)**2+1))
 g=lambda z:2*M*((c-1)*B(z)+x*(B(z)**2+1))
 assert m.almosteq(f(0),aa);count+=1
 assert m.almosteq(g(0),0);count+=1
 assert m.almosteq(f(tt),0);count+=1
 assert m.almosteq(g(tt),bb);count+=1
 assert c-2*x>=0 and c+2*x<=1;count+=1
 for j in range(90):
  z=m.exp(2j*m.pi*j/90)
  assert abs((abs(f(z))+abs(g(z)))/(2*M)-1)<m.mpf('1e-45')
  count+=1
print('ASYMMETRIC_NUMERICAL_RADIUS_EXACT_OK',count)
