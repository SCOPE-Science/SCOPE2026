import numpy as np

def sinkhorn_C(mu, nu, xs, ys, cmat, eps, niter=20000, tol=1e-12):
    # C_eps = inf <c,pi> + eps KL(pi | mu x nu)
    # Dual: sup_f,g <f,mu>+<g,nu> - eps*( sum_{ij} (exp((f_i+g_j-c_ij)/eps)-1) mu_i nu_j )
    # K_ij = exp(-c_ij/eps)
    K = np.exp(-cmat/eps)
    # Sinkhorn in scaling form: a_i, b_j with pi_ij = a_i K_ij b_j mu_i nu_j, a=exp(f/eps), b=exp(g/eps)
    a = np.ones_like(mu); b = np.ones_like(nu)
    for it in range(niter):
        Kb = K @ (b*nu)
        anew = 1.0/np.maximum(Kb,1e-300)
        Ka = K.T @ (anew*mu)
        bnew = 1.0/np.maximum(Ka,1e-300)
        if np.max(np.abs(anew-a))<tol and np.max(np.abs(bnew-b))<tol:
            a,b = anew,bnew; break
        a,b = anew,bnew
    pi = (a*mu)[:,None]*K*(b*nu)[None,:]
    # primal objective
    # KL(pi|mu x nu) = sum pi log(pi/(mu nu))
    ratio = pi/np.maximum(np.outer(mu,nu),1e-300)
    kl = np.sum(pi*np.log(np.maximum(ratio,1e-300)))
    cost = np.sum(pi*cmat)
    return cost + eps*kl, pi

def W2sq_half_1d(mu, nu, xs, ys):
    # quantile coupling
    cmu = np.cumsum(mu); cnu = np.cumsum(nu)
    cmu/=cmu[-1]; cnu/=cnu[-1]
    u = np.linspace(0.0005,0.9995,20001)
    qm = np.interp(u, cmu, xs); qn = np.interp(u, cnu, ys)
    return 0.5*np.mean((qm-qn)**2)

if __name__=="__main__":
    L=8.0; N=801
    xs=np.linspace(-L,L,N); dx=xs[1]-xs[0]
    def gauss(s2):
        p=np.exp(-xs**2/(2*s2)); p/=p.sum()
        return p
    def kink(kap=1.0,A=2.0):
        p=np.exp(-kap*xs**2/2 - A*np.abs(xs)); p/=p.sum()
        return p
    X,Y=np.meshgrid(xs,xs,indexing='ij')
    cmat=(X-Y)**2/2
    mu=gauss(1.0); nu=gauss(2.0)
    w=W2sq_half_1d(mu,nu,xs,xs)
    print("W2^2/2 gauss",w)
    for eps in [0.3,0.2,0.15,0.1,0.07,0.05]:
        C,_=sinkhorn_C(mu,nu,xs,xs,cmat,eps)
        Cmm,_=sinkhorn_C(mu,mu,xs,xs,cmat,eps)
        Cnn,_=sinkhorn_C(nu,nu,xs,xs,cmat,eps)
        S=C-0.5*(Cmm+Cnn)
        print(f"eps={eps} S={S:.7f} diff={S-w:.3e} diff/eps={(S-w)/eps:.4f}")
    print("---kink---")
    mu=kink(1.0,2.0); nu=kink(0.5,1.0)
    # normalize check moments/fisher roughly
    w=W2sq_half_1d(mu,nu,xs,xs)
    print("W2^2/2 kink",w)
    for eps in [0.3,0.2,0.15,0.1,0.07,0.05]:
        C,_=sinkhorn_C(mu,nu,xs,xs,cmat,eps)
        Cmm,_=sinkhorn_C(mu,mu,xs,xs,cmat,eps)
        Cnn,_=sinkhorn_C(nu,nu,xs,xs,cmat,eps)
        S=C-0.5*(Cmm+Cnn)
        print(f"eps={eps} S={S:.7f} diff={S-w:.3e} diff/eps={(S-w)/eps:.4f}")
