import itertools

def step(state,n):
 a=state[:n];b=state[n:]
 ca=sum(v==1 for v in a);cb=sum(v==1 for v in b)
 return tuple(2 if v==1 else 0 if v==2 else int(cb-(b[i]==1)>0) for i,v in enumerate(a))+tuple(2 if v==1 else 0 if v==2 else int(ca-(a[i]==1)>0) for i,v in enumerate(b))
for n in range(3,7):
 c=0
 for p in itertools.product(range(3),repeat=2*n):
  s=step(p,n);s2=step(s,n);s3=step(s2,n);s4=step(s3,n)
  if s4==p and s2!=p:
   c+=1
 assert c==(2*(2**n-2)*(2**n-2-2*n)+24*(n==4)),(n,c)
 print(f'n={n}: primitive_four_states={c}; formula=PASS')
