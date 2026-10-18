from fractions import Fraction as F

mu=F(1)
a=F(1)
b=F(11,20)
c=F(3,2)
s=a+b+c

# Circulant determinant and nondegeneracy.
det=s*(a*a+b*b+c*c-a*b-b*c-c*a)
sq=s*((a-b)**2+(b-c)**2+(c-a)**2)/2
assert det==sq and det>0

M=mu/s
assert a*M+b*M+c*M==mu
assert c*M+a*M+b*M==mu
assert b*M+c*M+a*M==mu
assert M==F(20,61)
assert 3*M==F(60,61)

# Pointwise residual identities at an exact rational state.
X1=F(2,7); X2=F(3,8); X3=F(5,9)
Q1=b*X2+c*X3
Q2=b*X3+c*X1
Q3=b*X1+c*X2
r1=mu-a*X1-Q1
r2=mu-a*X2-Q2
r3=mu-a*X3-Q3
S=X1+X2+X3
assert Q1-(mu-a*X1)==-r1
assert Q2-(mu-a*X2)==-r2
assert Q3-(mu-a*X3)==-r3
assert r1+r2+r3==3*mu-s*S

# Abstract conditional-orthogonality algebra.
EX=F(2,5); EX2=F(7,10)
ER=F(0); ER2=F(3,11); EXR=F(0)
varX=EX2-EX*EX
EQ=mu-a*EX-ER
EQ2=(mu*mu + a*a*EX2 + ER2
     -2*mu*a*EX -2*mu*ER +2*a*EXR)
varQ=EQ2-EQ*EQ
assert varQ==a*a*varX+ER2
EXQ=mu*EX-a*EX2-EXR
cov=EXQ-EX*EQ
assert cov==-a*varX

print("VERIFY_OK")
