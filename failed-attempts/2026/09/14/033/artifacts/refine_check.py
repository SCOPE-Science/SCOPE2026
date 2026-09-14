"""Refinement + identity cross-check for the rotational-stripe disproof."""
import numpy as np

c = 0.5
gamma2 = 1 - c*c
gamma = float(np.sqrt(gamma2))
m = 0.5
nu = 1.0/(gamma*np.sqrt(m))

def agm(a, b, it=80):
    for _ in range(it):
        a, b = (a+b)/2.0, float(np.sqrt(a*b))
    return a

K = np.pi/(2.0*agm(1.0, float(np.sqrt(1-m))))
L = 2.0*K*gamma*np.sqrt(m)

def rhs(Y):
    U, V = Y
    return np.array([V, float(np.sin(U))/gamma2])

def rk4_step(Y, h):
    k1 = rhs(Y); k2 = rhs(Y+0.5*h*k1)
    k3 = rhs(Y+0.5*h*k2); k4 = rhs(Y+h*k3)
    return Y + h*(k1+2*k2+2*k3+k4)/6.0

# dense integration over one period
h2 = L/200000
ts=[0.0]; Urec=[np.pi]; Vrec=[2*nu]
Y=np.array([np.pi,2*nu]); t=0.0
while t < L:
    Y=rk4_step(Y,h2); t+=h2
    ts.append(t); Urec.append(Y[0]); Vrec.append(Y[1])
ts=np.array(ts); Urec=np.array(Urec); Vrec=np.array(Vrec)

print("N: Hill_min, k0_maxRe, k0.5_maxRe")
for N in [200, 400, 800]:
    xs=np.linspace(0,L,N,endpoint=False); dx=L/N
    Ug=np.interp(xs,ts,Urec)
    q=np.cos(Ug)
    e=np.ones(N)
    D2=(np.diag(e[1:],1)+np.diag(e[1:],-1)+np.diag([1.0],N-1)+np.diag([1.0],-(N-1))-2*np.eye(N))/dx**2
    L0=-gamma2*D2+np.diag(q)
    ev=np.linalg.eigvalsh(L0)
    D1=(np.roll(np.eye(N),-1,axis=1)-np.roll(np.eye(N),1,axis=1))/(2*dx)
    I=np.eye(N); Z=np.zeros((N,N))
    def maxre(k):
        M=np.block([[Z,I],[-(L0+k*k*I),2*c*D1]])
        return float(np.abs(np.linalg.eigvals(M).real).max())
    print(f"{N}: {ev[0]:.3e}  {maxre(0.0):.3e}  {maxre(0.5):.3e}")

# identity check at N=400, k=0.5: pick eigenvalue with largest |Im|
N=400
xs=np.linspace(0,L,N,endpoint=False); dx=L/N
Ug=np.interp(xs,ts,Urec)
q=np.cos(Ug)
e=np.ones(N)
D2=(np.diag(e[1:],1)+np.diag(e[1:],-1)+np.diag([1.0],N-1)+np.diag([1.0],-(N-1))-2*np.eye(N))/dx**2
L0=-gamma2*D2+np.diag(q)
D1=(np.roll(np.eye(N),-1,axis=1)-np.roll(np.eye(N),1,axis=1))/(2*dx)
I=np.eye(N); Z=np.zeros((N,N)); k=0.5
M=np.block([[Z,I],[-(L0+k*k*I),2*c*D1]])
ew, evc=np.linalg.eig(M)
idx=int(np.argmax(np.abs(ew.imag)))
lam=ew[idx]; V=evc[:N,idx]
S=float((V.conj()@(L0@V)).real); Nn=float((V.conj()@V).real)
J=complex(V.conj()@(D1@V))
sig=lam.real; tau=lam.imag
print("lambda =",lam)
print("imag identity 2*sig*(tau*N-c*j) =",2*sig*(tau*Nn-c*(-J.imag)))
print("real identity S+2c*tau*j+(sig^2-tau^2+k^2)*N =",
      S+2*c*tau*(-J.imag)+(sig**2-tau**2+k**2)*Nn, "  S =",S," N =",Nn)
