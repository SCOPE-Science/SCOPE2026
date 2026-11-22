"""Symbolic certificate for the eight-orbit KMP covariance identities.
Requires Python 3 and SymPy. Run: python verify_symbolic.py
"""
import sympy as s
n,g=s.symbols('n g',positive=True)
h,p,q=s.symbols('h p q')
a,b,c,d,e,f,k,z=s.symbols('a b c d e f k z')
mean=s.solve([
 n*(q-h)/2+g*(1-h),
 n*(q-p)/2-g*p,
 (h+(n-1)*p-n*q)/2-g*q], (h,p,q))
E=[
 n*(-2*a+2*e+c)/3+g*(2-a),
 n*(-2*b+2*k+c)/3-g*b,
 (-2*n*c+2*e+2*(n-1)*k+a+(n-1)*b)/3-g*c,
 n*(k+e-2*d)/2+g*mean[p]-2*g*d,
 (a+c-4*e)/6+(n-1)*(z+d-2*e)/2+g*mean[q]-2*g*e,
 n*(k-f)-2*g*f,
 (b+c-4*k)/6+((n-1)*(z-k)+(d-k)+(n-2)*(f-k))/2-2*g*k,
 e+(n-1)*k-(n+2*g)*z]
unknown=[a,b,c,d,e,f,k,z]
M,rhs=s.linear_eq_to_matrix(E,unknown)
assert s.cancel(M.det()-(g*(g+n)*(2*g+n)*(4*g+3*n)*(6*g*g+(8*n-1)*g+2*n*n)*(12*g*g+(11*n-2)*g+2*n*n)/18))==0
sol=dict(zip(unknown,M.inv()*rhs))
R=n**3*(2*n-1)+n*n*(8*n-3)*g+n*(6*n+1)*g*g-4*(n-1)*g**3-4*g**4
D=4*(g+n)**2*(2*g+n)**2*(6*g*g+(8*n-1)*g+2*n*n)
S=(128*g**6+(476*n-88)*g**5+(740*n*n-164*n)*g**4
 +(638*n**3-131*n*n+2*n)*g**3
 +(332*n**4-85*n**3+10*n*n)*g*g
 +(98*n**5-39*n**4+6*n**3)*g+12*n**6-6*n**5)
F=(4*(g+n)**2*(2*g+n)*(4*g+3*n)
 *(6*g*g+(8*n-1)*g+2*n*n)
 *(12*g*g+(11*n-2)*g+2*n*n))
assert s.cancel(sol[z]-mean[q]**2-R/D)==0
assert s.cancel(sol[k]-mean[p]*mean[q]-S/F)==0
assert s.cancel((sol[f]-mean[p]**2)-n/(2*g+n)*(sol[k]-mean[p]*mean[q]))==0
print('BIPARTITE_KMP_SYMBOLIC_CERTIFICATE_PASSED')
