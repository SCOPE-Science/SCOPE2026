# A minimal-node first-jet Parseval rule for spherical quadrupoles and unique tight latitude design

## Finding

Let \(d\ge3\), let \(\sigma\) be probability-normalized surface measure on \(S^{d-1}\subset\mathbb R^d\), and let \(\mathcal H_2\) be the real or complex exact-degree-two spherical-harmonic space. Define the first-jet form for a positive probability measure \(\mu\) on the sphere by
\[
J_{\mu,\alpha}(f,g)=\int\left[\alpha f\overline g+\frac{1-\alpha}{2d}\langle\nabla_S f,\nabla_S g\rangle\right]d\mu,\qquad 0\le\alpha\le1.
\]
Here the gradient pairing is linear in the first argument and conjugate-linear in the second, and \(\int |\nabla_S f|^2d\sigma=2d\int|f|^2d\sigma\) for \(f\in\mathcal H_2\).

**Theorem A (exact isotropic first-jet equivalence).** At the fixed positive mixing coefficient \(\alpha_d=2/(d+2)\), the identity
\[
J_{\mu,\alpha_d}(f,g)=\int_{S^{d-1}}f\overline g\,d\sigma\quad\text{for every }f,g\in\mathcal H_2
\]
holds if and only if the second-moment matrix satisfies
\[
\int xx^{\mathsf T}\,d\mu(x)=I_d/d.
\]
Thus no fourth-moment exactness is needed. In particular, \(d\) equally weighted, pairwise orthogonal sphere points give an exact Parseval first-jet sampling rule. Any *positive atomic* measure realizing this identity at the stipulated mixing coefficient has at least \(d\) support points, and equality forces equal weights and an orthonormal basis, up to signs, permutation, and a global orthogonal transformation.

**Theorem B (rigid latitude design).** Fix the last coordinate as polar axis. Let \(\mu_t\) be the uniform probability distribution on the single latitude \(x_d=\sqrt t\), with \(0<t<1\), where the remaining coordinates form the uniform sphere of radius \(\sqrt{1-t}\). Among **all** \((t,\alpha)\in(0,1)\times[0,1]\), the form \(J_{\mu_t,\alpha}\) is a multiple of the global \(L^2\) inner product on \(\mathcal H_2\) if and only if
\[
\boxed{t=1/d,\qquad \alpha=2/(d+2).}
\]
The multiple is then exactly \(1\). More explicitly, the three eigenvalue branches \(\lambda_0,\lambda_1,\lambda_2\) (zonal, mixed, transverse-traceless) obey the *exact quantitative anisotropy identity*
\[
\boxed{2(\lambda_0-\lambda_1)+(d+1)(\lambda_1-\lambda_2)
=\frac{(1+\alpha)(d+2)}2(dt-1).}
\]
Each \(\lambda_j\) uses the normalization in the displayed definition of \(J\). In particular, the uniquely tight rule simultaneously maximizes the smallest frame eigenvalue and minimizes the condition number among this family, because the trace-normalized mean eigenvalue is always \(1\).

## Assumptions and scope

The space is \(\mathcal H_2=\{f_A(x)=x^{\mathsf T}Ax:\ A=A^{\mathsf T}\in\mathbb C^{d\times d},\ \operatorname{tr}A=0\}\), with real matrices for real harmonics. The identification with trace-free matrices is injective. Its dimension is \((d-1)(d+2)/2\). All measures have total mass one and all atomic weights are strictly positive; the minimum-node statement concerns only measures satisfying Theorem A at its specified coefficient, not unrestricted first-jet measurements or other weight models. At the polar-latitude endpoints \(t=0,1\) no uniqueness assertion is made. The gradient is **intrinsic tangential**, not an ambient or normal derivative; it is measured as a full vector with the canonical tangent metric. The analysis makes no assertion for spherical-harmonic degrees other than two or for non-round spheres.

## Proof

**1. An exact cancellation identity.** For a complex symmetric trace-free matrix \(A\), set \(f_A(x)=x^{\mathsf T}Ax\). On the unit sphere,
\[
\nabla_Sf_A(x)=2\bigl(Ax-f_A(x)x\bigr),\qquad
|\nabla_Sf_A(x)|^2=4\bigl(\|Ax\|^2-|f_A(x)|^2\bigr).
\]
The first equality follows by orthogonally projecting the ambient gradient \(2Ax\) to \(x^\perp\). Since \(x\) is real with norm one, \(x^*Ax=f_A(x)\); this yields the stated Hermitian squared-norm identity, including for complex coefficients. Polarization gives, for trace-free symmetric \(A,B\),
\[
J_{\mu,\alpha_d}(f_A,f_B)
=\frac{2}{d+2}\int\langle Ax,Bx\rangle\,d\mu(x)
=\frac{2}{d+2}\operatorname{tr}(B^*A\,M_\mu),
\]
where \(M_\mu=\int xx^{\mathsf T}d\mu(x)\). The cancellation is exact because \(\alpha_d=2(1-\alpha_d)/d\). The standard sphere fourth-moment identity
\[
\int x_ix_jx_kx_l\,d\sigma
=\frac{\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}}{d(d+2)}
\]
gives
\[
\int f_A\overline{f_B}\,d\sigma
=\frac{2}{d(d+2)}\operatorname{tr}(B^*A)
\]
when both traces vanish. Consequently, \(M_\mu=I_d/d\) implies the claimed Parseval identity.

Conversely assume Parseval for all such \(A\). Put \(H=M_\mu-I_d/d\). Then \(\operatorname{tr}(A^*A H)=0\) for every symmetric trace-free \(A\). Using real diagonal choices with entries \(+1,-1\) in any two distinct positions shows \(H_{ii}+H_{jj}=0\) for every pair. Since \(d\ge3\), all diagonal entries of \(H\) vanish. For distinct \(i,j\), choose \(k\) different from both and the real symmetric trace-free \(A=E_{ii}-E_{kk}+E_{ij}+E_{ji}\). Its square has only one relevant off-diagonal pair, \((A^2)_{ij}=(A^2)_{ji}=1\), hence \(\operatorname{tr}(A^2H)=2H_{ij}=0\). Thus \(H=0\), proving the converse.

For an atomic measure \(\mu=\sum_{r=1}^Nw_r\delta_{x_r}\), isotropy gives \(I_d/d=\sum_rw_rx_rx_r^{\mathsf T}\), a full-rank sum of \(N\) rank-one matrices, so \(N\ge d\). If \(N=d\), the square matrix with columns \(\sqrt{d w_r}\,x_r\) has product with its transpose equal to the identity, so is orthogonal. Thus \(w_r=1/d\) and the nodes form an orthonormal basis. Conversely these nodes satisfy isotropy and therefore Parseval.

**2. Exact latitude spectrum.** Write \(x=(\sqrt{1-t}\,y,\sqrt t)\) with \(y\) uniform on \(S^{d-2}\). Restriction of \(\mathcal H_2\) to rotations fixing the polar axis splits orthogonally into: (0) the zonal line represented by \(dt-1\); (1) the \((d-1)\)-dimensional mixed sector represented by \(\sqrt{t(1-t)}y_j\); and (2) the \((d-2)(d+1)/2\)-dimensional transverse trace-free quadratic sector represented by \((1-t)H_2(y)\). No cross terms survive latitude averaging. For the separate value and Dirichlet-normalized gradient measurements, the eigenvalues are

| Sector | Value \(V_j\) | Gradient \(G_j\) |
|---|---|---|
| \(0\) | \(\frac{(d+2)(dt-1)^2}{2(d-1)}\) | \(\frac{d(d+2)t(1-t)}{d-1}\) |
| \(1\) | \(\frac{d(d+2)t(1-t)}{d-1}\) | \(\frac{(d+2)[1+(d-6)t+4t^2]}{2(d-1)}\) |
| \(2\) | \(\frac{d(d+2)(1-t)^2}{(d-1)(d+1)}\) | \(\frac{(d+2)(1-t)(d-1+2t)}{(d-1)(d+1)}\) |

For example, the gradient entries follow from the exact separation formula
\[
|\nabla_S(p(z)Y_k(y))|^2=(1-z^2)|p'(z)|^2|Y_k(y)|^2+\frac{|p(z)|^2}{1-z^2}|\nabla_yY_k(y)|^2,
\]
using the degree-\(k\) transverse eigenvalue \(k(k+d-3)\), then dividing by \(2d\) times the global squared norm. Each mixed eigenvalue is \(\lambda_j=\alpha V_j+(1-\alpha)G_j\). Substituting and simplifying proves the boxed gap identity in the Finding section. Its right side vanishes for \(\lambda_0=\lambda_1=\lambda_2\) only if \(t=1/d\), since \(1+\alpha>0\). At this latitude,
\[
\lambda_0-\lambda_1=-\frac{d+2}{d^2}\bigl((d+2)\alpha-2\bigr),
\]
so equality requires \(\alpha=2/(d+2)\), which indeed gives all three eigenvalues exactly one by Theorem A (the latitude second moment is then isotropic). This proves uniqueness.

**3. Optimality and quantitative defect.** The addition theorem and the gradient addition theorem, or direct weighted summation of the three rows with multiplicities, show \(\operatorname{tr}J_{\mu_t,\alpha}=\dim\mathcal H_2\) for every \(t,\alpha\); in particular the mean eigenvalue is one. Thus \(\lambda_{\min}\le1\) and \(\lambda_{\max}/\lambda_{\min}\ge1\) wherever the form is positive definite. Both inequalities are sharp only at a tight spectrum, which step 2 shows has exactly the asserted parameters. The displayed gap identity gives an exact linear certificate for latitude displacement, not merely a local Taylor approximation.

## Verification

The standalone `verify.py` (Python 3 plus SymPy) checks both symbolic parameter identities, normalization and multiplicity traces, and 1,480+ independently assembled **exact rational** bilinear tests on orthonormal-axis nodes for dimensions three through six; it also tests that an explicitly anisotropic measure is not falsely declared tight. Run `python verify.py` from a directory containing the file; it prints the assertion total. All infinite-parameter and necessity statements follow from the analytic proof above and are *not* inferred from the finite tests. The independent tests calculate ambient quadratic gradients and tangent projections directly from matrices rather than using the latitude spectral table.

## Relationship to prior work

Nafees, Khalid, Kennedy and McEwen (first public preprint September 8, 2017) investigate conditioning of value-only spherical-harmonic transforms based on iso-latitude rings and improve ring placement using finite matrix condition numbers. Wieczorek and Meschede (first published May 12, 2018) document spherical-harmonic transforms and derivative/gradient operations on spherical grids. These provide motivation for using latitude measurements and derivatives. Their inspected descriptions and relevant full-text sections do not state the quadrupole-specific, positive value-and-gradient Parseval identity at a single latitude, the all-measure isotropy equivalence, or its sharp minimal-node classification. Existing neighboring mathematical results for degree-three derivative-assisted cubature concern different harmonic degree and higher moment constraints. In particular the present identity is not a claim that value-only latitude samples are tight.

## Limitations

The result assumes exact noiseless values plus full intrinsic gradient vectors with a fixed explicit relative normalization, not scalar derivative components or arbitrary noisy measurements. It does not optimize physical cost per gradient component, nor guarantee that the mixed-noise covariance matches this weighting. The minimal-node assertion is relative to the stated fixed mixing coefficient; no minimality is claimed among all possible measurement schemes. Literature searching and inspected sources cannot rule out all unindexed equivalent earlier results; independent expert priority and proof validation have not been performed.

## References

1. W. Nafees, Z. Khalid, R. A. Kennedy and J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497 (first submitted 2017-09-08), https://arxiv.org/abs/1709.02497.
2. M. A. Wieczorek and M. Meschede, *SHTools: Tools for Working with Spherical Harmonics*, *Geochemistry, Geophysics, Geosystems* 19 (2018), 2574–2592, first published 2018-05-12, https://doi.org/10.1029/2018GC007529.
