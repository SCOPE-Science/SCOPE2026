from itertools import product
for m in range(1,8):
 def f(s):
  out=list(s);h=s[0];sm=sum(s[1:]);out[0]=int(sm<m) if sm!=m else h
  for i in range(m):
   a,b=s[2*i+1],s[2*i+2]
   if a==h and b==h:out[2*i+1]=out[2*i+2]=1-h
  return tuple(out)
 fixed=period2=0
 for s in product((0,1),repeat=2*m+1):
  t=f(s)
  if t==s:fixed+=1
  elif f(t)==s:period2+=1
 assert fixed==2*3**m and period2==2*(3**m-2**m),(m,fixed,period2)
 print(m,fixed,period2)

print("PASS")
