"""Independent finite-dimensional checks for balanced-gain/loss weighted star spectra."""
import itertools
import numpy as np
import sympy as sp

z=sp.symbols('z'); g,t,w=sp.symbols('g t w', positive=True, real=True)
H4=sp.Matrix([[sp.I*g,0,0,t], [0,-sp.I*g,0,t], [0,0,0,w], [t,t,w,0]])
assert sp.expand(H4.charpoly(z).as_expr() - (z**4 + (g**2-2*t**2-w**2)*z**2 - w**2*g**2)) == 0
H3=sp.Matrix([[sp.I*g,0,t],[0,-sp.I*g,t],[t,t,0]])
assert sp.factor(H3.charpoly(z).as_expr()) == z*(z*z+g*g-2*t*t)
assert H3.subs(g,sp.sqrt(2)*t).rank()==2
assert (H3.subs(g,sp.sqrt(2)*t)**2).rank()==1
assert H3.subs(g,sp.sqrt(2)*t)**3==sp.zeros(3)
# Deterministic finite checks on general neutral spokes; build without using the symbolic block.
checks=0
for n in range(3,12):
  for tt,gg in ((0.3,0.2),(1.,0.1),(1.7,2.6),(2.2,0.95)):
    for seq in range(3):
      couplings = np.array([tt,tt]+[0.31+0.07*((5*j+3*seq)%11) for j in range(n-2)])
      W=float(np.sum(couplings[2:]**2))
      H=np.zeros((n+1,n+1),dtype=complex)
      H[0,0]=1j*gg;H[1,1]=-1j*gg
      H[:n,n]=couplings;H[n,:n]=couplings
      eig=np.linalg.eigvals(H)
      S=2*tt**2+W
      rad=np.sqrt((S-gg**2)**2+4*W*gg**2)
      yp=(S-gg**2+rad)/2
      ym=(S-gg**2-rad)/2
      exp=np.array([np.sqrt(yp),-np.sqrt(yp),1j*np.sqrt(-ym),-1j*np.sqrt(-ym)]+[0]*(n-3))
      assert max(np.min(abs(a-exp)) for a in eig)<1e-8, (n,tt,gg,seq)
      assert np.sqrt(-ym)<gg
      checks+=1
print('PT_STAR_CHECKS_PASSED',checks,'symbolic_charpoly_and_Jordan_passed')
