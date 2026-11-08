"""Deterministic numerical checks of the stated finite-dimensional mode formulas.
Requires Python 3 and mpmath. These tests do not constitute a proof.
"""
import mpmath as mp

mp.mp.dps = 48
checks = 0

def close(x, y, atol='1e-29', rtol='1e-25'):
    global checks
    checks += 1
    if abs(x-y) > mp.mpf(atol) + mp.mpf(rtol)*max(abs(x),abs(y)):
        raise AssertionError(f'mismatch {x} != {y}, err {abs(x-y)}')

def aof(beta, r, omega):
    return mp.mpc(0,beta*omega)/(r+mp.mpc(0,omega))

def hyp(beta,r,omega,t):
    return mp.hyp1f1(aof(beta,r,omega),beta,-(r+mp.mpc(0,omega))*t)

def euler(beta,r,omega,t):
    a=aof(beta,r,omega)
    c=mp.gamma(beta)/(mp.gamma(a)*mp.gamma(beta-a))
    m=16
    def core(u):
        return mp.exp(-(r+mp.mpc(0,omega))*t*u)*u**(a-1)*(1-u)**(beta-a-1)
    return c*(mp.quad(lambda x: core(mp.mpf('0.5')*x**m)*mp.mpf('0.5')*m*x**(m-1),[0,1]) + mp.quad(lambda x: core(1-mp.mpf('0.5')*x**m)*mp.mpf('0.5')*m*x**(m-1),[0,1]))

def lead(beta,r,omega):
    a=aof(beta,r,omega)
    return mp.gamma(beta)*mp.power(r+mp.mpc(0,omega),-a)/mp.gamma(beta-a)

def response(beta,r,omega):
    return (beta-1)/(-r+mp.mpc(0,(beta-1)*omega))

for r,omega in [(mp.mpf('1.2'),mp.mpf('0.8')),(mp.mpf('1'),mp.mpf('2')),(mp.mpf('2.4'),mp.mpf('0.9'))]:
    for beta in [mp.mpf('0.9'),mp.mpf('1.5'),mp.mpf('3.5'),mp.mpf('8')]:
        a=aof(beta,r,omega)
        close(mp.re(a),beta*omega**2/(r*r+omega**2))
        close(mp.im(a),beta*r*omega/(r*r+omega**2))
        close(hyp(beta,r,omega,mp.mpf('0')),1)
        close(hyp(beta,r,omega,mp.mpf('0.1')),euler(beta,r,omega,mp.mpf('0.1')),'1e-24','1e-22')
        close(hyp(beta,r,omega,mp.mpf('1.7')),euler(beta,r,omega,mp.mpf('1.7')),'1e-23','1e-21')
        # Initial short-time derivative and Kummer ODE.
        f=lambda t:hyp(beta,r,omega,t)
        close(mp.diff(f,0),-mp.mpc(0,omega),'1e-25','1e-23')
        t=mp.mpf('0.6')
        ode=t*mp.diff(f,t,2)+(beta+(r+mp.mpc(0,omega))*t)*mp.diff(f,t)+mp.mpc(0,beta*omega)*f(t)
        close(ode,0,'1e-25','1e-23')
        # Complex conjugate pairing preserves density-matrix Hermiticity.
        close(hyp(beta,r,-omega,mp.mpf('2.2')),mp.conj(hyp(beta,r,omega,mp.mpf('2.2'))),'1e-25','1e-23')
        # Gamma/Beta primitive identity applies only in the absolute-integrability domain.
        if mp.re(a)>mp.mpf('1.01'):
            integral_by_euler = mp.gamma(beta)/(mp.gamma(a)*mp.gamma(beta-a))/(r+mp.mpc(0,omega))*mp.beta(a-1,beta-a)
            close(integral_by_euler,response(beta,r,omega),'1e-25','1e-23')
            close(mp.re(response(beta,r,omega)),-r*(beta-1)/(r*r+(beta-1)**2*omega**2),'1e-25','1e-23')

# Direct numerical time integral: safely inside convergent regime (beta=7, r=1, omega=2).
beta=mp.mpf(7); r=mp.mpf(1); omega=mp.mpf(2)
fun=lambda t:hyp(beta,r,omega,t)
integral=mp.quad(fun,[0,1,5,20,100,mp.inf],maxdegree=7)
close(integral,response(beta,r,omega),'1e-11','1e-10')

# Leading asymptotic slope and the crossing of the decay exponent through one.
for r,omega in [(mp.mpf('1'),mp.mpf('2')),(mp.mpf('0.8'),mp.mpf('1.5'))]:
    bc=1+(r/omega)**2
    for beta in [bc*mp.mpf('0.8'),bc,bc*mp.mpf('1.4')]:
        a=aof(beta,r,omega)
        if beta==bc:
            close(mp.re(a),1)
            close(mp.im(a),r/omega)
        for t in [mp.mpf('300'),mp.mpf('600')]:
            scaled=mp.power(t,a)*hyp(beta,r,omega,t)
            err=abs(scaled/lead(beta,r,omega)-1)
            checks+=1
            if err > mp.mpf('0.08'):
                raise AssertionError(f'failure of large-t asymptotics: {err}')

# Nondegenerate three-level example: the geometric critical curve is a circle.
energies=[mp.mpf('0'),mp.mpf('2'),mp.mpf('4')]
entries={(1,0):mp.mpf('0.07'),(2,1):mp.mpf('0.045'),(2,0):mp.mpf('0.03')}
r=mp.mpf('1'); delta=mp.mpf('2'); bc=1+(r/delta)**2
a=aof(bc,r,delta)
coefficient=lead(bc,r,delta)/(1-a)
# A only has lower-diagonal entries; A^2 diagonal is zero.
A=[[mp.mpc(0) for _ in range(3)] for _ in range(3)]
for (j,k),v in entries.items():
    if energies[j]-energies[k]==delta:
        A[j][k]=coefficient*v
radius_sq=2*sum(abs(A[j][k])**2 for j in range(3) for k in range(3))
for theta in [mp.pi*i/13 for i in range(27)]:
    Q=[[mp.exp(-1j*theta)*A[j][k]+mp.exp(1j*theta)*mp.conj(A[k][j]) for k in range(3)] for j in range(3)]
    close(sum(abs(Q[j][k])**2 for j in range(3) for k in range(3)),radius_sq,'1e-24','1e-23')
close(sum(A[j][k]*A[k][j] for j in range(3) for k in range(3)),0)
print('PASS:',checks,'deterministic scalar, integral, asymptotic, and critical-circle checks')
