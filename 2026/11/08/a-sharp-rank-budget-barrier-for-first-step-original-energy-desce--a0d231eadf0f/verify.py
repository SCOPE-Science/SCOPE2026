import numpy as np
rng=np.random.default_rng(20261106)
checks=0
for d in range(1,9):
  for trial in range(125):
    M=rng.normal(size=(d,d));H=M.T@M+np.eye(d)*.05
    R=rng.normal(size=(d,d));L=(R.T@R)*(rng.random()**2)
    E=np.linalg.eigvalsh(H-2*L).max()
    hs=[0.01,0.5,1.0,2.0,20.0]
    if E>0: hs += [2/E*.999,2/E,2/E*1.001]
    for h in hs:
      Aw=np.eye(d)+h*L
      vals,U=np.linalg.eigh(H)
      Hhalf=(U*np.sqrt(vals))@U.T
      B=h*Hhalf@np.linalg.solve(Aw,Hhalf)
      B=(B+B.T)/2
      vmax=np.linalg.eigvalsh(B).max()
      pred=(h*E<=2+1e-10)
      assert ((vmax<=2+1e-8) == pred) or abs(vmax-2)<2e-8
      if pred:
       for _ in range(3):
        x=rng.normal(size=d)*10**rng.uniform(-5,3)
        C=10**rng.uniform(-3,3)
        f0=x@H@x/2;g=H@x
        fac=1+h*(g@np.linalg.solve(Aw,g))/(2*(f0+C))
        x1=x-h/fac*np.linalg.solve(Aw,g)
        f1=x1@H@x1/2
        assert f1<=f0*(1+5e-12)
        checks+=1
      else:
       v,vec=np.linalg.eigh(B)
       z=vec[:,-1]
       x0=(U*(1/np.sqrt(vals)))@U.T@z
       C=1.0
       # small x, alpha approximately 1
       x=x0*1e-9
       g=H@x
       f0=x@H@x/2
       fac=1+h*(g@np.linalg.solve(Aw,g))/(2*(f0+C))
       x1=x-h/fac*np.linalg.solve(Aw,g)
       f1=x1@H@x1/2
       assert f1>f0*(1+1e-8),(h,E,vmax,f0,f1)
       checks+=1
for d in range(2,11):
 for trial in range(50):
  vals=np.sort(rng.uniform(0.01,20,size=d))[::-1]
  Q,_=np.linalg.qr(rng.normal(size=(d,d)))
  H=(Q*vals)@Q.T
  for rank in range(d):
   L=(Q*(np.r_[vals[:rank]*0.5,np.zeros(d-rank)]))@Q.T
   assert abs(np.linalg.eigvalsh(H-2*L).max()-vals[rank])<1e-8
   checks+=1
print('VALIDATED',checks)
