from itertools import combinations_with_replacement,product
from collections import Counter
rows=[]
for i,j in combinations_with_replacement(range(3),2):
 r=[0]*3;r[i]+=1;r[j]+=1;rows.append(r)
blocks=list(product(rows,repeat=3))
counts=Counter()
for B in blocks:
 for C in blocks:
  W=[[sum(B[i][k]*C[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
  tr=sum(W[i][i] for i in range(3))
  S=4-tr
  if S<3:continue
  e2=sum(W[i][i]*W[j][j]-W[i][j]*W[j][i] for i in range(3) for j in range(i+1,3))
  P=e2+4*S
  det=(W[0][0]*(W[1][1]*W[2][2]-W[1][2]*W[2][1])-W[0][1]*(W[1][0]*W[2][2]-W[1][2]*W[2][0])+W[0][2]*(W[1][0]*W[2][1]-W[1][1]*W[2][0]))
  if P>0 and S*S>4*P and det==4*P:
   counts[(S,P)]+=1
print(dict(sorted(counts.items())))
assert counts=={(3,1):72,(3,2):360,(4,2):72}
