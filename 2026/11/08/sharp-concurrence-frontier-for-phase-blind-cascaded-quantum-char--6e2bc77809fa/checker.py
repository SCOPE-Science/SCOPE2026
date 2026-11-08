"""Independent finite-dimensional checks for concurrence/phase-span bounds in a two-qubit charger plus qubit battery."""
import numpy as np
from scipy.linalg import expm

I=np.eye(2,dtype=complex)
lower=np.array([[0,1],[0,0]],dtype=complex)
num=lower.conj().T@lower
sy=np.array([[0,-1j],[1j,0]],dtype=complex)
sx=np.array([[0,1],[1,0]],dtype=complex)
sz=np.array([[1,0],[0,-1]],dtype=complex)

def k3(a,b,c):return np.kron(np.kron(a,b),c)
def unitary(D,g,tau):
    H=(1-D)*(k3(num,I,I)+k3(I,num,I))+k3(I,I,num)
    for term in (k3(lower,I,lower.conj().T),k3(I,lower,lower.conj().T)):
        H=H+g*(term+term.conj().T)
    return expm(-1j*H*tau)

def pop(U,psi,e,phase):
    bat=np.array([np.sqrt(1-e),np.sqrt(e)*np.exp(1j*phase)])
    res=U@np.kron(psi,bat)
    return np.vdot(res[1::2],res[1::2]).real

def analytic(psi,e,phase,D,g,tau):
    a,b,c,d=psi
    s=(b+c)/np.sqrt(2)
    Om=np.sqrt(D**2+8*g**2)
    L=8*g*g/Om**2*np.sin(Om*tau/2)**2
    xi=-1j*(2*np.sqrt(2)*g/Om)*np.sin(Om*tau/2)
    ch=np.cos(Om*tau/2)-1j*D/Om*np.sin(Om*tau/2)
    E0=L*(abs(s)**2+abs(d)**2)
    E1=1-L*(abs(a)**2+abs(s)**2)
    Z=np.conj(xi)*ch*(np.conj(s)*a+np.conj(d)*s)
    return (1-e)*E0+e*E1+2*np.sqrt(e*(1-e))*np.real(np.exp(1j*phase)*Z),Z,L

def concurrence(psi):
    a,b,c,d=psi
    return 2*abs(a*d-b*c)

def product_basis(psi,U,e,phase):
    """Return a local product basis balancing all conditional battery energies.
    Uses two Bloch-vector perpendicularity operations, not a general 4x4 Schur-Horn basis.
    """
    bat=np.array([np.sqrt(1-e),np.sqrt(e)*np.exp(1j*phase)])
    out=(U@np.kron(psi,bat)).reshape(4,2)
    v0,v1=out[:,0],out[:,1]
    P0=np.vdot(v0,v0).real;P1=np.vdot(v1,v1).real
    T=P0*np.outer(v1,v1.conj())-P1*np.outer(v0,v0.conj())
    X=T.reshape(2,2,2,2)
    Tr2=np.einsum('ij kj->ik',X)
    bx=np.trace(Tr2@sx).real; bz=np.trace(Tr2@sz).real
    n1=np.array([bz,0,-bx])
    if np.linalg.norm(n1)<1e-12:n1=np.array([1.,0.,0.])
    n1=n1/np.linalg.norm(n1)
    M1=n1[0]*sx+n1[1]*sy+n1[2]*sz
    _,V1=np.linalg.eigh(M1)
    blocks=[]
    for j in range(2):
        v=V1[:,j]
        blocks.append(np.einsum('i,ijkl,k->jl',v.conj(),X,v))
    bloch=np.array([[np.trace(B@q).real for q in (sx,sy,sz)] for B in blocks])
    n2=np.cross(bloch[0],bloch[1]);
    if np.linalg.norm(n2)<1e-12:
        n2=np.cross(bloch[0],[1,0,0])
    if np.linalg.norm(n2)<1e-12:
        n2=np.cross(bloch[0],[0,1,0])
    if np.linalg.norm(n2)<1e-12:n2=np.array([0.,0.,1.])
    n2=n2/np.linalg.norm(n2)
    M2=n2[0]*sx+n2[1]*sy+n2[2]*sz
    _,V2=np.linalg.eigh(M2)
    B=np.kron(V1,V2)
    charged=B.conj().T@v1
    uncharged=B.conj().T@v0
    probs=abs(charged)**2+abs(uncharged)**2
    means=np.divide(abs(charged)**2,probs,out=np.full(4,np.nan),where=probs>1e-12)
    return means,probs,P1

def run():
    rng=np.random.default_rng(101104)
    total=0
    for j in range(75):
        D=rng.uniform(-1.5,1.5);g=rng.uniform(.05,1.5);tau=rng.uniform(.05,8)
        e=rng.uniform(.01,.99);phi=rng.uniform(-np.pi,np.pi)
        psi=rng.normal(size=4)+1j*rng.normal(size=4);psi/=np.linalg.norm(psi)
        U=unitary(D,g,tau)
        exact=pop(U,psi,e,phi)
        theory,Z,L=analytic(psi,e,phi,D,g,tau)
        assert abs(exact-theory)<5e-13,(j,exact,theory)
        total+=1
        C=concurrence(psi)
        span=4*np.sqrt(e*(1-e))*abs(Z)
        bound=2*np.sqrt(2*e*(1-e)*L*(1-L))*np.sqrt(max(0,1-C*C))
        assert span<=bound+1e-13,(j,span,bound)
        total+=1
        vals=np.array([pop(U,psi,e,phi) for phi in np.linspace(0,2*np.pi,13)])
        assert vals.max()-vals.min()<=bound+1e-12
        total+=1
        means,probs,P1=product_basis(psi,U,e,phi)
        assert np.max(abs(means-P1))<4e-12,(means,P1)
        total+=1
        # local Schmidt family and simultaneous rotation attains every fraction of bound
        targetC=rng.random()
        r=np.sqrt(1-targetC**2); lam=(1+r)/2
        sch=np.array([np.sqrt(lam),0,0,np.sqrt(1-lam)],dtype=complex)
        for theta in (0,np.pi/6,np.pi/2):
            rot=expm(-.5j*theta*sy)
            psi2=np.kron(rot,rot)@sch
            _,Z2,L2=analytic(psi2,e,phi,D,g,tau)
            target=bound*0 # computed for targetC
            top=2*np.sqrt(2*e*(1-e)*L2*(1-L2))*r
            assert abs(4*np.sqrt(e*(1-e))*abs(Z2)-top*abs(np.sin(theta)))<2e-12
            total+=1
    print(f'PASS: {total} independent checks; 75 random full-Hamiltonian comparisons, 75 local measurement equalizations, concurrence sharpness at 3 angles each')
    D=.7;g=.05;tau=np.pi/np.sqrt(D*D+8*g*g);e=.4
    psi=np.array([1,1j,1j,1],complex)/2
    U=unitary(D,g,tau)
    vals=[pop(U,psi,e,phi) for phi in np.linspace(0,2*np.pi,31)]
    print('maximally-entangled non-Bell example concurrence=',concurrence(psi),'energy range=', max(vals)-min(vals),'one step=',vals[0]);
    assert max(vals)-min(vals)<1e-13
    Omega=np.sqrt(D*D+8*g*g); L=8*g*g/Omega**2*np.sin(Omega*tau/2)**2
    for n in range(8):
        ep=0.5+(1-1.5*L)**n*(0.0-0.5)
        exact=ep
        # Given the current excitation, the next step must match the closed recurrence for any phase.
        for ph in (0.1, 1.7, 3.8):
            next_p=pop(U,psi,ep,ph)
            expected=0.5+(1-1.5*L)**(n+1)*(0.0-0.5)
            assert abs(next_p-expected)<2e-13
            total+=1
    print('PASS: 24 additional maximally-entangled closed-recursion checks; non-Bell charger converges to half-charge')
if __name__=='__main__':run()
