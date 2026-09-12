import numpy as np

# Recovery test 1: projection w -> w/|w| can strictly increase Dirichlet energy.
# Domain (-1,1), w(x) = (x, eps), n = w/|w| in S^1. E(w)=int |w'|^2, E(n)=int |n'|^2.
for eps in [0.5, 0.2, 0.1, 0.05]:
    xs = np.linspace(-1, 1, 200001)
    dx = xs[1]-xs[0]
    Ew = 2.0  # int_{-1}^1 1 dx
    En = np.sum((eps**2/(xs**2+eps**2)**2))*dx
    print(f"eps={eps}: E(w)={Ew:.4f} E(n)={En:.4f} ratio={En/Ew:.2f}")

print("---")
# Recovery test 2: coarse 3D gap hunt for axial datum f(alpha)=A sin(alpha)

def energies(A, Nr=24, Na=48, Nt=32):
    r = np.linspace(0, 1, Nr+1)[1:]
    alpha = np.linspace(0, np.pi, Na)
    theta = np.linspace(0, 2*np.pi, Nt, endpoint=False)
    dr = r[1]-r[0]; da = alpha[1]-alpha[0]; dt = theta[1]-theta[0]
    R, AL, TH = np.meshgrid(r, alpha, theta, indexing='ij')
    f = A*np.sin(AL)
    g = R*f
    dgdr = f
    dgdalpha = R*A*np.cos(AL)
    Rsafe = np.maximum(R,1e-9); Ssafe = np.maximum(np.sin(AL),1e-9)
    grad_g2 = dgdr**2 + (1.0/Rsafe**2)*dgdalpha**2
    dens_sym = grad_g2 + np.sin(g)**2/(Rsafe**2*Ssafe**2)
    W = R**2*np.sin(AL)
    E_sym = np.sum(dens_sym*W)*dr*da*dt
    s = 0.8
    gradTH2 = 1.0/(Rsafe**2*Ssafe**2)
    cross = -np.sin(TH)/(Rsafe*Ssafe)
    gradp2 = gradTH2 + 2*s*cross + s**2*1.0
    dens_nonsym = grad_g2 + np.sin(g)**2*gradp2
    E_nonsym = np.sum(dens_nonsym*W)*dr*da*dt
    return E_sym, E_nonsym

for A in [1.0, 2.0, np.pi]:
    Es, En = energies(A)
    print(f"A={A:.4f}: E_sym={Es:.4f} E_nonsym(s=0.8)={En:.4f} diff={En-Es:.4f}")
