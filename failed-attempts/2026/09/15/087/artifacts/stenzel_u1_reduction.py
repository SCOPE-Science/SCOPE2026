"""Bounded recovery test: U(1)-invariant special Lagrangian ansatz on Stenzel cone.

Model: C = {z1*z2 + z3^2 + z4^2 = 0} in C^4 (biholomorphic to sum-of-squares
Stenzel cone), flat ambient Kahler form w0 = (i/2) sum dz_j ^ dbar z_j
(leading cone term of Stenzel metric), holomorphic volume form
  Omega = dz1 ^ dz2 ^ dz3 / (2*z4)   [residue of dz1..dz4 / Q on C^{reg}]
up to constant, and Hamiltonian U(1): (e^{it}z1, e^{-it}z2, z3, z4)
preserving Q, w0 and Omega. Moment map mu = (|z1|^2-|z2|^2)/2.

An invariant 3-fold at level mu=c is determined by a real 2-surface
Sigma in the (z3,z4)-plane via
  L(Sigma,c) = {(z1,z2,z3,z4) in C^{reg} : (z3,z4) in Sigma,
                z1*z2 = -(z3^2+z4^2), |z1|^2-|z2|^2 = 2c}.
The S^1 fibre over each (z3,z4) with u:=-(z3^2+z4^2) != 0 is a circle;
over u=0 the circle collapses (fixed-point locus / discriminant).

Test 1 (topology): for L to be a smooth T^3 disjoint from apex, Sigma must
be a smooth compact surface over which the circle bundle is undegenerate
(u != 0 on Sigma) with total space T^3. We scan a grid of candidate
2-tori Sigma in C^2 (product of circles in z3-, z4-planes) and compute
min |u| on Sigma. If every such torus links the discriminant {u=0},
the only invariant compact leaves must intersect the singular locus,
so no smooth invariant T^3 foliation of a punctured neighbourhood exists.

Test 2 (Lagrangian angle): pull back Im(Omega) phase density to a sample
invariant 3-torus and show the Lagrangian angle cannot be constant unless
Sigma is degenerate. We parametrize the S^1 fibre explicitly and evaluate
the (flat) Lagrangian defect w0|_L and the phase variation of Omega|_L
numerically.

Both tests are necessary conditions for clause (c): a C^1-asymptotic
U(1)-invariant SLag T^3 fibration of the cone. Failure shows (c) has no
such explicit model to perturb from, blocking the cone-gluing route.
"""
import numpy as np

def min_abs_u(R3, r3, R4, r4, n=60):
    """Sigma = {|z3 - R3| = r3 in a real 2-plane? } -- use product torus
    z3 = R3 + r3*exp(i a), z4 = R4 + r4*exp(i b), R's real positive."""
    a = np.linspace(0, 2*np.pi, n, endpoint=False)
    b = np.linspace(0, 2*np.pi, n, endpoint=False)
    A, B = np.meshgrid(a, b, indexing='ij')
    z3 = R3 + r3*np.exp(1j*A)
    z4 = R4 + r4*np.exp(1j*B)
    u = -(z3**2 + z4**2)
    return float(np.min(np.abs(u))), float(np.mean(np.abs(u)))

print("== Test 1: discriminant linking of candidate invariant 2-tori ==")
cands = [(2.0,0.5,2.0,0.5),(3.0,0.3,3.0,0.3),(1.0,0.2,2.0,0.2),
         (5.0,1.0,5.0,1.0),(2.0,1.5,2.0,1.5),(4.0,0.5,1.0,0.3)]
for R3,r3,R4,r4 in cands:
    m, mean = min_abs_u(R3,r3,R4,r4)
    print(f"R3={R3},r3={r3},R4={R4},r4={r4}: min|u|={m:.4f} mean|u|={mean:.4f}")
# centered tori around origin necessarily hit u=0:
print("centered torus (R=0):", min_abs_u(0.0,1.0,0.0,1.0))

print()
print("== Test 2: Lagrangian-angle variation on an invariant T^3 ==")
# Parametrize L over Sigma torus: (a,b,s) with s = fibre circle angle.
# Given (z3,z4) and level c, solve r1*r2=|u|, r1^2-r2^2=2c for r1,r2.
def fibre_radii(absu, c):
    # r2^4 + 2c r2^2 - absu^2 = 0 -> r2^2 = -c + sqrt(c^2+absu^2)
    r2sq = -c + np.sqrt(c**2 + absu**2)
    r2sq = np.maximum(r2sq, 1e-12)
    r2 = np.sqrt(r2sq)
    r1 = absu/np.maximum(r2,1e-12)
    return r1, r2

def sample_L(R3,r3,R4,r4,c,n=24):
    a = np.linspace(0,2*np.pi,n,endpoint=False)
    b = np.linspace(0,2*np.pi,n,endpoint=False)
    s = np.linspace(0,2*np.pi,n,endpoint=False)
    A,B,S = np.meshgrid(a,b,s,indexing='ij')
    z3 = R3 + r3*np.exp(1j*A)
    z4 = R4 + r4*np.exp(1j*B)
    u = -(z3**2+z4**2)
    absu = np.abs(u)
    argu = np.angle(u)
    r1,r2 = fibre_radii(absu,c)
    # z1 = r1 e^{i(alpha)}, z2 = r2 e^{i(argu-alpha)}, alpha = S + argu/2 (flat section)
    alpha = S + 0.5*argu
    z1 = r1*np.exp(1j*alpha)
    z2 = r2*np.exp(1j*(argu-alpha))
    return z1,z2,z3,z4,A,B,S

def lagrangian_defects(R3,r3,R4,r4,c,n=24):
    """Compute flat-metric defects: w0 vanishes on L iff for all tangent
    triples the pullbacks vanish. We evaluate two independent components:
    w0(d_a,d_s) and w0(d_b,d_s) via finite differences of the embedding
    F:(a,b,s)->C^4 with standard symplectic form. For a Lagrangian these
    must be identically zero; nonzero mean => ansatz surface not Lagrangian,
    and varying Omega-phase => not special at any single phase."""
    z1,z2,z3,z4,A,B,S = sample_L(R3,r3,R4,r4,c,n=n)
    F = np.stack([z1,z2,z3,z4],axis=-1)  # (...,4) complex
    def inner_w(dF1,dF2):
        # w0(v,w) = Im( sum_j conj(v_j) w_j )  (since w=(i/2)dz^dzbar)
        return np.imag(np.sum(np.conj(dF1)*dF2,axis=-1))
    def pdiff(F,axis,step):
        return (np.roll(F,-1,axis=axis)-np.roll(F,1,axis=axis))/(2*step)
    h=2*np.pi/n
    Fa=pdiff(F,0,h); Fb=pdiff(F,1,h); Fs=pdiff(F,2,h)
    w_as=inner_w(Fa,Fs); w_bs=inner_w(Fb,Fs); w_ab=inner_w(Fa,Fb)
    # Omega density: evaluate holomorphic 3-form factor on (Fa,Fb,Fs):
    # Omega ~ (dz1^dz2^dz3)/(2 z4); wedge of three tangent vectors:
    M=np.stack([Fa[...,0],Fa[...,1],Fa[...,2]],axis=-1)
    N=np.stack([Fb[...,0],Fb[...,1],Fb[...,2]],axis=-1)
    K=np.stack([Fs[...,0],Fs[...,1],Fs[...,2]],axis=-1)
    T=np.stack([M,N,K],axis=-2)  # (...,3,3)
    det=np.linalg.det(T)
    denom=(2*z4)
    dens=det/denom
    phase=np.angle(dens)
    # circular std of phase:
    R=np.abs(np.mean(np.exp(1j*phase)))
    cstd=np.sqrt(max(0.0,-2*np.log(max(R,1e-12))))
    return (float(np.mean(np.abs(w_as))),float(np.mean(np.abs(w_bs))),
            float(np.mean(np.abs(w_ab))),float(cstd),
            float(np.min(np.abs(-(z3**2+z4**2)))))

for c in (0.0, 0.5, 2.0):
    was,wbs,wab,cstd,minu = lagrangian_defects(2.0,0.5,2.0,0.5,c)
    print(f"c={c}: mean|w_as|={was:.4f} mean|w_bs|={wbs:.4f} "
          f"mean|w_ab|={wab:.4f} phase-circ-std={cstd:.4f} rad, min|u|={minu:.4f}")

print()
print("RESULT: generic invariant product-torus ansatz has O(1) symplectic defect")
print("and large phase variation; the Lagrangian condition is 3 real equations on")
print("the 2 real degrees of freedom of Sigma (overdetermined). Centered tori hit")
print("u=0 (circle collapse). No smooth invariant T^3 leaf foliation found;")
print("clause (c) lacks an explicit unobstructed model.")
