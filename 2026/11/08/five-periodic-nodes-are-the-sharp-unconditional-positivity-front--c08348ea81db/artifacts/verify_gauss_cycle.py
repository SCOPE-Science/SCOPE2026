"""Exact symbolic and finite rational checks for the periodic heat Padé theorem.

Requires Python 3 and SymPy. All-dimensional claims require the proof in RESULT.md;
finite checks are not substitutes for their quantified arguments.
"""
import sympy as sp

h = sp.symbols('h', nonnegative=True)
checks = 0

def check(x, label):
    global checks
    if x is not True and x != sp.S.true:
        raise AssertionError(label)
    checks += 1

def cycle_laplacian(n):
    A = 2*sp.eye(n)
    for j in range(n):
        A[j, (j-1) % n] -= 1
        A[j, (j+1) % n] -= 1
    return A

def pade_matrices(n, x):
    A = cycle_laplacian(n)
    den = sp.eye(n) + x*A/2 + x*x*A*A/12
    num = sp.eye(n) - x*A/2 + x*x*A*A/12
    return den, num

def centered_cycle_kernel(n, j):
    k = j % n
    return sp.Rational(n*n - 1,12*n) - sp.Rational(k*(n-k),2*n)

D3 = 3*h**2+6*h+4
D4 = (h**2+3*h+3)*(4*h**2+6*h+3)
D5 = 25*h**4+150*h**3+360*h**2+360*h+144
short = {
    3: [(3*h**2-2*h+4)/D3, 4*h/D3],
    4: [(4*h**4+3*h**3+6*h**2+9*h+9)/D4, 3*h/(4*h**2+6*h+3), 9*h**2*(h+1)/D4],
    5: [(25*h**4+30*h**3+72*h**2+72*h+144)/D5, 72*h*(h+2)/D5, 12*h**2*(5*h+6)/D5],
}

# Verify all polynomial/rational entries of the infinite-step classification's finite side.
for n, row in short.items():
    T = sp.Matrix(n, n, lambda i,j: row[min((i-j) % n,(j-i) % n)])
    den,num = pade_matrices(n,h)
    for i in range(n):
        for j in range(n):
            check(sp.cancel((den*T-num)[i,j]) == 0, 'symbolic Padé identity')
    for i in range(n):
        check(sp.cancel(sum(T[i,j] for j in range(n))-1) == 0, 'symbolic row sum')

# The cycle Green function is the zero-mean solution of the Poisson equation.
for n in range(3,36):
    A = cycle_laplacian(n)
    G = sp.Matrix(n,n,lambda i,j:centered_cycle_kernel(n, i-j))
    J = sp.ones(n,n)/n
    E = A*G - (sp.eye(n)-J)
    for v in E:
        check(v == 0, 'Green identity')
    for i in range(n):
        check(sum(G[i,j] for j in range(n)) == 0, 'Green zero mean')
    check(sp.simplify(G[0,1]-sp.Rational((n-1)*(n-5),12*n))==0,'adjacent Green coefficient')

# Exact rational Padé matrices and finite demonstration of the sign transition.
for n in range(3,15):
    for step in [sp.Rational(1,100),sp.Rational(1,2),sp.Rational(3,2),sp.Rational(8),sp.Rational(64)]:
        den,num = pade_matrices(n,step)
        T = den.inv()*num
        for j in range(n):
            check(sum(T[j,k] for k in range(n))==1,'mass conservation')
        if n <= 5:
            for entry in T:
                check(entry >= 0,'finite-cell nonnegativity')

n=6
x=sp.symbols('x')
A=cycle_laplacian(n)
D,N=pade_matrices(n,x)
t01=sp.factor((D.inv()*N)[0,1]); expected=-2*x*(5*x**4-12*x**3-102*x**2-144*x-72)/((x**2+6*x+12)*(3*x**2+6*x+4)*(4*x**2+6*x+3))
check(sp.cancel(t01-expected)==0,'six-cycle adjacent entry')
check(t01.subs(x,8)==-sp.Rational(6584,580537),'six-cycle exact sign witness')

# Scalar Padé factor has strictly positive numerator and denominator for x>=0;
# positivity of each eigenvalue does not imply entrywise positivity.
z=sp.symbols('z', nonnegative=True)
check(sp.expand(12*(1-z/2+z*z/12)-((z-3)**2+3))==0, 'scalar numerator positivity identity')
check(sp.expand(12*(1+z/2+z*z/12)-((z+3)**2+3))==0, 'scalar denominator positivity identity')

print('GAUSS_CYCLE_VERIFY_OK', checks, 'exact symbolic/rational assertions')
print('six-cycle adjacent entry at dimensionless step 8: -6584/580537')
print('NOTE: all n>=6 follows from the proved Green-function expansion, not testing')
