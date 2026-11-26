from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal

def dsqrt(x):
    return D(x).sqrt()

def factor(n,k):
    n=D(n); k=D(k)
    return (n-D(1)).sqrt()*(k-D(1))/(D(2)*k.sqrt())

# Boundary identity for several dimensions.
for n in [2,3,4,10,100]:
    sn=D(n).sqrt()
    k=(sn+D(1))/(sn-D(1))
    assert abs(factor(n,k)-D(1)) < D("1e-55")

# Equality construction on the two-dimensional (u,v) plane:
# trace=1+k, determinant=k, and h=c v.
for k0 in [D("1.5"),D(2),D(4),D(10)]:
    c=(k0-D(1))/(D(2)*k0.sqrt())
    a=D(2)*k0/(k0+D(1))
    off=-a*c
    d=(k0*k0+D(1))/(k0+D(1))
    assert abs((a+d)-(D(1)+k0)) < D("1e-55")
    assert abs(a*d-off*off-k0) < D("1e-55")
    alpha=D(1)/a
    h_v=-alpha*off
    assert abs(h_v-c) < D("1e-55")

# Explicit n=3, kappa=4 witness.
s2=D(2).sqrt()
A=[
    [(D(14)-D(4)*s2)/D(5), -(D(3)+s2)/D(5), -(D(3)+s2)/D(5)],
    [-(D(3)+s2)/D(5), (D(8)+D(2)*s2)/D(5), (D(3)+D(2)*s2)/D(5)],
    [-(D(3)+s2)/D(5), (D(3)+D(2)*s2)/D(5), (D(8)+D(2)*s2)/D(5)]
]
g=[D(1),D(1),D(1)]
Ag=[sum(A[i][j]*g[j] for j in range(3)) for i in range(3)]
gg=sum(x*x for x in g)
gAg=sum(g[i]*Ag[i] for i in range(3))
alpha=gg/gAg
assert abs(alpha-D(5)/D(8)) < D("1e-55")
gp=[g[i]-alpha*Ag[i] for i in range(3)]
target=[D(3)*s2/D(4),-D(3)*s2/D(8),-D(3)*s2/D(8)]
for x,y in zip(gp,target):
    assert abs(x-y) < D("1e-55")

norm2=(sum(x*x for x in gp)/sum(x*x for x in g)).sqrt()
norminf=max(abs(x) for x in gp)/max(abs(x) for x in g)
assert abs(norm2-D(3)/D(4)) < D("1e-55")
assert abs(norminf-D(3)*s2/D(4)) < D("1e-55")
assert norminf > D(1)

# The two-plane representation at kappa=4 has trace 5 and determinant 4,
# hence eigenvalues 1 and 4; the orthogonal complement is assigned eigenvalue 1.
a=D(8)/D(5); off=-D(6)/D(5); d=D(17)/D(5)
assert a+d == D(5)
assert a*d-off*off == D(4)

print("VERIFY_OK")
print("alpha", alpha)
print("euclidean_ratio", norm2)
print("maxnorm_ratio", norminf)
print("dimension3_boundary", (D(3).sqrt()+D(1))/(D(3).sqrt()-D(1)))
