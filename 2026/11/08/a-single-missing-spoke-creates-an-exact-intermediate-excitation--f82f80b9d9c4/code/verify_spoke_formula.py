"""Independent integer matrix evaluation of the missing-spoke three-rate census."""
T=((1,1,1),(1,1,0),(1,0,1))
B=((0,1,1),(1,0,2),(1,2,0))
A=((1,0,0),(0,1,0),(0,0,1))
Q=[2,2]
for k in range(2,51):Q.append(2*Q[-1]+Q[-2])
for n in range(4,31):
    A=tuple(tuple(sum(A[i][k]*T[k][j] for k in range(3)) for j in range(3)) for i in range(3)) if n==4 else A
    # matrix currently at exponent n-3 for n>4, multiply once
    if n>4:A=tuple(tuple(sum(A[i][k]*T[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    # For n=4, current exponent 1, need exponent2
    if n==4:A=tuple(tuple(sum(A[i][k]*T[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    s=sum(map(sum,A));r=sum(A[i][j]*B[i][j] for i in range(3) for j in range(3))
    m=n-2
    assert 2*s==Q[m]+2*Q[m+1],(n,s,Q[m],Q[m+1])
    assert r==Q[m+1]-2,(n,r,Q[m+1])
    n0=9*s-3*r;np=3*r;nh=3**(n+1)-9*s
    assert (n0,np,nh)==(9*Q[m]//2+6*Q[m+1]+6,3*Q[m+1]-6,3**(n+1)-9*Q[m]//2-9*Q[m+1])
    assert n0+np+nh==3**(n+1) and min(n0,np,nh)>0
    if n<=9 or n in (15,30):print('n',n,'counts',(n0,np,nh))
print('PASS symbolic recurrence and transfer census for all n=4..30')
