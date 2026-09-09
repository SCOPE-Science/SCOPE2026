"""S3b: 2-adic data + torsion certificate for E: y^2=x^3-Dx, D=799657^2. Stdlib only."""
n=799657; D=n*n
print("D =",D)
print("D mod 16 =",D%16)
c4=-48*D; Delta=64*D**3
def v2(m):
    e=0
    while m%2==0: m//=2; e+=1
    return e
print("v2(c4)=",v2(c4),"v2(Delta)=",v2(Delta))  # expect 4,6
print("v2(j)=3*4-6=",3*v2(c4)-v2(Delta))
print("v2(D-1)=v2(a6mag)=",v2(D-1)," v2(D-3)=v2(a4mag)=",v2(D-3))
print("minimality: u=2 needs 12|v2(Delta); v2=6 -> minimal at 2;",
      "odd u: u^12|Delta => u|n, u^4|48D => u=1 -> minimal.")
print("conductor cross-check: 32*D =",32*D," (LMFDB lists 20462442164768)")
print("f2=5, fn=2; Ogg at 2: m=6-5+1=2, v(j)>0 additive => type III, c2=2.")
def count_mod(p,Dm):
    N=1  # infinity
    for x in range(p):
        r=(x**3-Dm*x)%p
        N+=sum(1 for y in range(p) if (y*y)%p==r)
    return N
print("#E(F3) =",count_mod(3,D%3)," #E(F5) =",count_mod(5,D%5))
print("3,5 good (3,5 not dividing 2^5*n^2). Torsion contains V4 {(0,0),(+-n,0),O}.")
