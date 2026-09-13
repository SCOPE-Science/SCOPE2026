# Bounded test: E8(at inf)+D6(at 0)+I5(at 1) ansatz over F7.
# A=t^2*Atilde, B=t^3*Btilde; Atilde quad, Btilde quartic. F=4A^3-B^2 (char7 scalar assoc. to disc).
# G=4*Atilde^3 - Btilde^2; need v0(G)>=2, v1(G)>=5, a0!=0, b4!=0, Atilde(1)!=0, Btilde(1)!=0.
p=7
sols=[]
# precompute cubes/squares
for a0 in range(7):
 for a1 in range(7):
  for a2 in range(7):
    if a0==0: continue
    rhs=(4*pow(a0,3,p))%p
    # b0^2=rhs
    b0s=[b for b in range(7) if (b*b)%p==rhs]
    if not b0s: continue
    for b0 in b0s:
      if b0==0: continue
      # G'(0)=5*a0^2*a1-2*b0*b1=0 -> b1 = 5*a0^2*a1*inv(2*b0)
      inv=pow((2*b0)%p,-1,p)
      b1=(5*a0*a0%p*a1%p*inv)%p
      for b2 in range(7):
       for b3 in range(7):
        for b4 in range(7):
          if b4==0: continue
          At=[a0,a1,a2]
          Bt=[b0,b1,b2,b3,b4]
          # Atilde(1),Btilde(1)
          if sum(At)%p==0 or sum(Bt)%p==0: continue
          # coeffs of G=4*At^3-Bt^2 up to deg8
          # At^3: conv
          # At^2
          A2=[0]*5
          for i in range(3):
            for j in range(3):
              A2[i+j]=(A2[i+j]+At[i]*At[j])%p
          A3=[0]*7
          for i in range(5):
            for j in range(3):
              A3[i+j]=(A3[i+j]+A2[i]*At[j])%p
          B2=[0]*9
          for i in range(5):
            for j in range(5):
              B2[i+j]=(B2[i+j]+Bt[i]*Bt[j])%p
          G=[0]*9
          for i in range(9):
            a=(4*A3[i])%p if i<7 else 0
            G[i]=(a-B2[i])%p
          if G[0]!=0 or G[1]!=0: continue
          # derivatives at 1: evaluate G and first 4 derivs at t=1
          # value
          v=sum(G)%p
          if v!=0: continue
          # G'(t)=sum i*G[i]t^{i-1}; at 1: sum i*G[i]
          d1=sum(i*G[i] for i in range(9))%p
          if d1!=0: continue
          d2=sum(i*(i-1)*G[i] for i in range(9))%p
          if d2!=0: continue
          d3=sum(i*(i-1)*(i-2)*G[i] for i in range(9))%p
          if d3!=0: continue
          d4=sum(i*(i-1)*(i-2)*(i-3)*G[i] for i in range(9))%p
          if d4!=0: continue
          # exactness: G''(0)=2*G[2]!=0 ; d5 at 1 !=0
          if (2*G[2])%p==0: continue
          d5=sum(i*(i-1)*(i-2)*(i-3)*(i-4)*G[i] for i in range(9))%p
          if d5==0: continue
          sols.append((tuple(At),tuple(Bt),tuple(G)))
print("NSOL",len(sols))
for s in sols[:20]:
  print(s)
