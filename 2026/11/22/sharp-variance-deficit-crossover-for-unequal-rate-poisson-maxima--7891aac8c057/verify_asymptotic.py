import mpmath as mp
mp.mp.dps = 65
for aa,bb in [(2,1),(3,1),(1,mp.mpf('0.25'))]:
 a=mp.mpf(aa); b=mp.mpf(bb); q=mp.sqrt(b/a); c=(mp.sqrt(a)-mp.sqrt(b))**2
 coeff=a**mp.mpf('.75')*b**mp.mpf('.25')/(mp.sqrt(mp.pi)*(mp.sqrt(a)-mp.sqrt(b)))
 for t in (20,50,100,200):
  t=mp.mpf(t); z=2*t*mp.sqrt(a*b)
  ed=mp.fsum(k*mp.exp(-(a+b)*t)*q**k*mp.besseli(k,z) for k in range(1,250))
  tie=mp.sqrt(a*b)*t*mp.exp(-(a+b)*t)*mp.besseli(1,z)
  deficit=tie+ed*((a-b)*t+ed)
  pred=coeff*mp.sqrt(t)*mp.exp(-c*t)
  print(float(a),float(b),float(t),float(deficit),float(deficit/pred))
