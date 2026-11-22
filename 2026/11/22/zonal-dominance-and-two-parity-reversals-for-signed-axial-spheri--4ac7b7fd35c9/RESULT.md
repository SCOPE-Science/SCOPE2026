# Zonal dominance and two parity reversals for signed axial spherical heat covariances

## Finding
Let \(\mathbb S^2\) carry normalized surface measure, put \(z(x)=x_3\), and let \(H_t(x,y)\) be the spherical heat kernel, normalized to have harmonic eigenvalue \(e^{-t\ell(\ell+1)}\) on degree \(\ell\). For \(t,s>0\) and \(\lambda\ge0\), define the nonstationary real symmetric kernel
\[
K_{t,s,\lambda}(x,y)=H_t(x,y)-\lambda z(x)z(y)H_s(x,y).
\]
For \(s\le t\), positivity of all finite Gram matrices holds exactly at \(\lambda=0\). For \(s>t\), let \(C_{t,s}\) be the compact operator on \(\ell^2(\mathbb N_0)\) with only the following nonzero entries (columns indexed by \(\ell\ge0\)):
\[
(C_{t,s})_{\ell+1,\ell}=\frac{\ell+1}{\sqrt{(2\ell+1)(2\ell+3)}}
\exp\!\left(\frac{t(\ell+1)(\ell+2)-s\ell(\ell+1)}2\right),
\]
\[
(C_{t,s})_{\ell-1,\ell}=\frac{\ell}{\sqrt{(2\ell-1)(2\ell+1)}}
\exp\!\left(\frac{t(\ell-1)\ell-s\ell(\ell+1)}2\right)\quad(\ell\ge1).
\]
Then the **sharp all-configuration positivity threshold** is
\[
K_{t,s,\lambda}\succeq0\quad\Longleftrightarrow\quad
0\le\lambda\le\Lambda(t,s):=\|C_{t,s}\|^{-2}.
\]
No nonzero azimuthal spherical-harmonic order controls this norm: the controlling singular vector always has order \(m=0\). The zonal operator splits into *even-input* and *odd-input* blocks, each with a simple top squared singular value \(E(t,s)\), respectively \(O(t,s)\), and \(\|C_{t,s}\|^2=\max\{E(t,s),O(t,s)\}\).

The controlling parity changes **at least twice** as the second heat time increases, even with the first fixed. Precisely, for \(t=\log 2\), write \(s=\log b\). Rigorous rational certificates establish
\[
\begin{array}{c|cc|c}
b&E(t,\log b)&O(t,\log b)&\text{winner}\\\hline
13/5&>16/5&<3&\text{even}\\
3&<8/5&>9/5&\text{odd}\\
5&>6/5&<4/5&\text{even}
\end{array}
\]
so continuity gives distinct parity-tie parameters in \((\log(13/5),\log 3)\) and \((\log3,\log5)\). They are isolated, and at each tie the spectral nullspace of the sharp covariance operator has dimension two.

For every \(s>t\), all Gram matrices on pairwise distinct finite sites are **strictly positive definite**, even at \(\lambda=\Lambda(t,s)\). Nevertheless the associated reproducing-kernel Hilbert space is dense in \(C(\mathbb S^2)\) exactly when \(\lambda<\Lambda(t,s)\). Thus at the sharp endpoint finite-site nonsingularity survives but uniform universality fails.

## Assumptions and scope
The heat semigroup is \(e^{t\Delta_{\mathbb S^2}}\) with \(-\Delta_{\mathbb S^2}Y_{\ell m}=\ell(\ell+1)Y_{\ell m}\). Here \(Y_{\ell m}\) are orthonormal under normalized surface measure; the coordinate multiplication recurrence, the coefficients of \(C_{t,s}\), and its norm do not depend on which standard complex spherical-harmonic phase convention is chosen. Positivity means a nonnegative quadratic form for every finite configuration, including repeated positions. Strict positivity concerns pairwise distinct positions with nonzero real or complex weights. The claim concerns nonnegative subtraction weights only. The three parity certificates use exactly the rational values displayed, and assert at least two crossings, not an exhaustive census.

## Proof

**1. Harmonic factorization.** Put \(E_\ell=\ell(\ell+1)\), \(D_rY_{\ell m}=e^{-rE_\ell}Y_{\ell m}\), and let \(M\) multiply functions by \(z\). The heat kernel defines the trace-class operator \(D_r\). The signed kernel defines \(A=D_t-\lambda MD_sM\). The normalized spherical-harmonic three-term recurrence is
\[
zY_{\ell m}=a_{\ell,m}Y_{\ell+1,m}+a_{\ell-1,m}Y_{\ell-1,m},\qquad
a_{\ell,m}=\sqrt{\frac{(\ell+1)^2-m^2}{(2\ell+1)(2\ell+3)}}.
\]
The missing downward term at \(\ell=|m|\) is zero. For \(s>t\), \(C=D_t^{-1/2}MD_s^{1/2}\), first defined on finite harmonic sequences, extends to a compact operator: its nonzero entries decrease as \(\exp[-(s-t)\ell^2/2+O_{s,t}(\ell)]\). Consequently
\[
A=D_t^{1/2}(I-\lambda CC^*)D_t^{1/2}.
\]
The dense-range factorization shows that positivity on finite harmonic sequences is equivalent to \(\lambda\|C\|^2\le1\); positivity on all finite site configurations is equivalent by continuity and approximation of surface-integrable test functions by finite signed atomic measures. If \(s\le t\) and \(\lambda>0\), the degree-\(\ell\), order-zero diagonal form obeys
\[
e^{-tE_\ell}-\lambda\bigl[a_{\ell-1,0}^2e^{-sE_{\ell-1}}+a_{\ell,0}^2e^{-sE_{\ell+1}}\bigr]<0
\]
for sufficiently large \(\ell\), since \(tE_\ell-sE_{\ell-1}\to+\infty\). This proves the zero-only regime.

**2. Zonal dominance.** Decompose \(C\) over fixed azimuthal orders \(m\in\mathbb Z\). For each \(|m|>0\), the resulting nonnegative band matrix is, after natural identification of its indices, a restriction of the order-zero matrix with strictly smaller positive entries (because \(a_{\ell,m}<a_{\ell,0}\) on every admissible upper link). Norm monotonicity for matrices with nonnegative entries gives \(\|C_m\|\le\|C_0\|\). In fact the inequality is strict: \(C_m\) is compact, attains its nonzero norm, and replacing a maximizing vector by its coordinatewise modulus and embedding it in the order-zero block increases its image norm strictly. As \(|m|\to\infty\), these norms tend to zero by Gaussian decay. Therefore the global maximum is attained only at \(m=0\).

The order-zero operator exchanges even and odd harmonic degrees, so \(C_0^*C_0\) has two independent Jacobi blocks with positive off-diagonals. Their top eigenvalues \(E(t,s)\), \(O(t,s)\) are simple: compactness, strict connectivity, and the positive-eigenvector comparison (or compact Perron theory) exclude a second top eigenvector. Entries depend real-analytically on \(s>t\), locally uniformly in operator norm; hence the two simple top eigenvalues are real-analytic, and their nonidentical difference has isolated zeros.

**3. Exact even–odd–even certificate.** Set \(t=\log2\), \(s=\log b\), \(b>2\), and truncate **input columns** at \(\ell=0,\ldots,15\), retaining both output neighbors \(\ell\pm1\). For \(m=0\), define rational squared links
\[
u_\ell=\frac{(\ell+1)^2}{(2\ell+1)(2\ell+3)}
\frac{2^{(\ell+1)(\ell+2)}}{b^{\ell(\ell+1)}},\qquad
v_\ell=\frac{\ell^2}{(2\ell-1)(2\ell+1)}
\frac{2^{(\ell-1)\ell}}{b^{\ell(\ell+1)}}
\]
with \(v_0=0\). The truncated squared-norm Jacobi block on columns of parity \(p\in\{0,1\}\) has diagonal \(u_\ell+v_\ell\) and squared off-diagonal \(u_\ell v_{\ell+2}\). Thus every leading-principal-minor test for \(rI-C_p^*C_p\) reduces to exact rational LDL pivots \(d_0=r-u_p-v_p\), \(d_i=r-u_{p+2i}-v_{p+2i}-u_{p+2i-2}v_{p+2i}/d_{i-1}\). The accompanying standalone checker verifies all eight pivots are positive for the finite **upper** comparisons \((b,p,r)=(13/5,1,14/5),(3,0,3/2),(5,1,7/10)\).

For the **lower** comparisons, \((b,p,r)=(13/5,0,16/5)\) has the exact negative two-by-two leading minor
\[
\det\!\left(\frac{16}{5}I-(C_0^*C_0)_{\{0,2\}}\right)
=-\frac{48529856}{120670225}<0.
\]
The cases \((3,1,9/5)\) and \((5,0,6/5)\) already fail their one-by-one leading minor tests. For the infinite tail, set \(U_\ell=2^{(\ell+1)(\ell+2)}b^{-\ell(\ell+1)}\). The discarded squared Hilbert–Schmidt norm is at most \(2\sum_{\ell\ge16}U_\ell\); because \(U_{\ell+1}/U_\ell=(16/b^2)(4/b^2)^\ell\) decreases and is below \(1/2\) at \(\ell=16\), this is bounded by \(4U_{16}<10^{-18}\) for all three \(b\). Therefore the infinite operator norm differs from the truncated one by less than \(10^{-9}\). Since the upper certificate thresholds are all below four, this changes their squared bounds by less than \(4\cdot10^{-9}+10^{-18}\), giving the strict rational full-operator bounds in the finding. These are exact finite rational checks plus an analytic infinite-tail estimate, not numerical spectral guesses.

**4. Critical Gram strictness.** Let \(s>t\) and suppose a finite atomic measure \(\mu=\sum c_j\delta_{x_j}\) has zero energy under an admissible \(K\). The positive-kernel Cauchy–Schwarz inequality implies \(K\mu=0\), or \(D_t\mu=\lambda MD_sM\mu\). The degree-\(\ell\) harmonic coefficient vector of an atomic measure has norm \(O(\sqrt{\ell+1})\) by the addition theorem. Multiplication twice by \(z\) shifts degree by at most two, so the coefficient vector of \(MD_sM\mu\) in degree \(\ell\) is \(O(\sqrt{\ell+3}\,e^{-sE_{\ell-1}})\). Therefore
\[
\|\widehat\mu_\ell\|=O\!\left(\sqrt{\ell+3}\,e^{tE_\ell-sE_{\ell-1}}\right),
\]
which is Gaussian-decaying as \(\ell\to\infty\). Thus \(\mu\) has a smooth density, impossible for a nonzero finite combination of distinct point masses. This proves strict finite-site positivity, including at the sharp endpoint.

**5. Universality and critical nullity.** When \(\lambda<\Lambda(t,s)\), the factor \(I-\lambda CC^*\) is uniformly positive. For any nonzero finite signed measure \(\mu\), the heat-smooth harmonic vector \(D_t^{1/2}\mu\) is nonzero, so its kernel energy is positive. By the Riesz representation theorem and Hahn–Banach, the reproducing-kernel space is dense in \(C(\mathbb S^2)\). At \(\lambda=\Lambda(t,s)\), compactness yields a nonzero top eigenvector \(h\in\ker(I-\Lambda CC^*)\). The banded matrix \(CC^*\) has entries \(O(e^{-(s-t)\ell^2+O(\ell)})\) along \(\ell,\ell\pm2\), so iterating \(h=(\Lambda CC^*)^j h\) for arbitrary fixed \(j\) gives Gaussian decay faster than any prescribed \(e^{-c\ell^2}\). Hence \(u=D_t^{-1/2}h\) is a nonzero smooth \(L^2\) function and \(Au=0\). Integration against \(u\) annihilates every kernel section, so uniform density fails. Only the two zonal parity blocks can attain the maximum; their top eigenspaces are each one-dimensional, making the critical nullity one away from parity ties and two at each tie.

## Verification
Run `python3 EXACT_CHECK.py` using Python 3 with its standard library. The program verifies the exact rational Jacobi LDL inequalities at the three specified parameters, the negative principal minors giving lower bounds, and the infinite-tail geometric estimate. Expected final line: `All exact rational certificates passed.` Its output is supplementary to the full analytic proof above; it does not attempt to enumerate all parity crossings or replace infinite-dimensional arguments with finite numerics.

## Relationship to prior work
Buhmann and Jäger's 2021 preprint and 2022 open-access paper characterize positive definiteness for axially symmetric spherical coefficient matrices (notably Theorem 2 and Proposition 1) and provide structural sufficient criteria for strictness. This furnishes the coefficient-matrix language, but neither the two-temperature latitude-subtraction law, zonal extremizer domination nor the certified even–odd–even top-eigenvalue reversals is stated there. Jäger's 2020 study analyzes block structure for general non-isotropic kernels, not this heat-semigroup spectral comparison. Emery, Jäger and Porcu's 2024 work considers axially symmetric spatiotemporal covariance representations; the available abstract does not resolve the present exact static heat-difference model, but its complete contents were not available during the comparison. Related positive axial Poisson tilts, two-scale Poisson circle covariances, and sum-modulated circle heat covariances use different coefficient decay or spatial multipliers; no implication to the displayed spherical three-point parity certificates was established. This is a best-knowledge priority assessment, not a declaration that all possible literature has been exhausted.

## Limitations
The threshold for general times is a precisely defined compact-operator eigenvalue, not an elementary closed-form function. Exactly two *distinct* parity crossings are guaranteed by the certificate; the total number of crossings is not classified. The family uses one latitude coordinate on \(\mathbb S^2\) and nonnegative subtraction weights. Neither higher spheres nor arbitrary axial multipliers are claimed. Historical priority and independent mathematical validation remain open.

## References
1. M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, arXiv:2105.02586, first submitted 6 May 2021; *Journal of Fourier Analysis and Applications* 28 (2022), article 40. https://arxiv.org/abs/2105.02586 ; https://doi.org/10.1007/s00041-022-09913-x
2. J. Jäger, *Strictly positive definite kernels on the 2-sphere: beyond radial symmetry*, arXiv:2005.02798, 6 May 2020. https://arxiv.org/abs/2005.02798
3. X. Emery, J. Jäger, E. Porcu, *Positive semidefinite kernels that are axially symmetric on the sphere and stationary in time: spectral and semi-spectral theory, and constructive approaches*, *Stochastic Environmental Research and Risk Assessment* 38 (2024), 2315–2329. https://doi.org/10.1007/s00477-024-02681-8
