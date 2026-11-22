# Three exact cap-spectrum crossings on real Grassmannians

## Finding
Fix integers \(n\ge4\) and \(2\le k\le n-2\). Let \(\mathcal G_{n,k}\) be the real Grassmannian of rank-\(k\) orthogonal projections \(P\) on \(\mathbb R^n\), with normalized orthogonally invariant measure. On its first nonconstant harmonic representation
\[
\mathcal V_{n,k}=\{f_A(P)=\operatorname{tr}(AP): A=A^{\mathsf T},\ \operatorname{tr}A=0\},
\]
concentrate energy on the one-coordinate principal-angle cap
\[
\Omega_t=\{P\in\mathcal G_{n,k}: P_{11}\ge t\},\qquad 0<t<1.
\]
The concentration operator \(T_t=\Pi_{\mathcal V}\,\mathbf1_{\Omega_t}\,\Pi_{\mathcal V}\), acting in the full-measure \(L^2\) inner product, has exactly three eigenvalue **branches** (which may coincide). Define \(a=k/2\), \(b=(n-k)/2\), and the normalized incomplete-beta tails
\[
J_r(t)=\frac{(a)_r}{(a+b)_r}\bigl[1-I_t(a+r,b)\bigr],\qquad r=0,1,2,
\]
where \((a)_r\) is a rising factorial and \(I_t\) the regularized incomplete beta function. The eigenvalues are
\[
\lambda_{\mathrm A}=\frac{n+2}{2k(n-k)}\bigl(n^2J_2-2nkJ_1+k^2J_0\bigr),
\]
\[
\lambda_{\mathrm V}=\frac{n(n+2)}{k(n-k)}(J_1-J_2),
\]
\[
\lambda_{\mathrm T}=\frac{n(n+2)}{k(n-k)(n-2)(n+1)}\bigl(k(n-k-1)J_0+2(k-n+1)J_1+(n-2)J_2\bigr).
\]
Their respective multiplicities are \(1\), \(n-1\), and \((n-2)(n+1)/2\). All three eigenvalues lie strictly between zero and one.

Every pair changes order at exactly one cap height. The three **sharp crossing heights** are
\[
t_{\mathrm{AT}}=\frac{k(n+2)-2n}{n(n-2)},\qquad
t_{\mathrm{AV}}=\frac{k}{n},\qquad
t_{\mathrm{VT}}=\frac{n-k-1}{n-2}.
\]
For \(k<n/2\), these satisfy \(0<t_{\mathrm{AT}}<t_{\mathrm{AV}}<t_{\mathrm{VT}}<1\) and the strict spectral ordering, as \(t\) increases, is
\[
\mathrm V>\mathrm T>\mathrm A;\quad
\mathrm V>\mathrm A>\mathrm T;\quad
\mathrm A>\mathrm V>\mathrm T;\quad
\mathrm A>\mathrm T>\mathrm V.
\]
For \(k>n/2\), the thresholds occur in reverse order and the four successive orderings are
\[
\mathrm V>\mathrm T>\mathrm A;\quad
\mathrm T>\mathrm V>\mathrm A;\quad
\mathrm T>\mathrm A>\mathrm V;\quad
\mathrm A>\mathrm T>\mathrm V.
\]
At a crossing, the two named sectors tie. In the middle rank \(n=2k\), all three thresholds coalesce at \(t=1/2\), and \(T_{1/2}=\tfrac12 I\) on the **whole** first-harmonic space.

Let \(\kappa_{n,k}(t)=\lambda_{\max}(t)/\lambda_{\min}(t)\) denote the sharp **squared-energy** restriction condition number. Its thin-cap singularity is exactly
\[
\boxed{\displaystyle\lim_{t\uparrow1}(1-t)\kappa_{n,k}(t)=\frac{(n-k)(n-k+2)}{2n}.}
\]
This is a spectral-energy ratio, not a singular-value ratio; the corresponding norm-level condition number is its square root.

## Assumptions and scope
The Grassmannian is **real and unoriented**; \(P\) is a symmetric idempotent matrix of trace \(k\). Haar-uniform means the unique \(O(n)\)-invariant probability. All coefficient matrices are real symmetric and trace-free, and \(\mathcal V_{n,k}\) is considered over \(\mathbb R\) (complexifying does not alter the eigenvalues or multiplicities). The cap is a threshold on the squared cosine of the angle between a fixed coordinate line and a random \(k\)-plane, **not** a geodesic ball or a Schubert cell. The operator compares cap energy to full-space energy, without dividing by the cap measure. The limits hold for each fixed admissible integer pair, not uniformly in growing dimension.

## Proof
**1. Global Hilbert normalization and symmetry.** The standard traceless-symmetric \(O(n)\)-module has dimension \((n-1)(n+2)/2\), and the invariant full-measure covariance is
\[
\int f_A(P)f_B(P)\,d\mu(P)=c_{n,k}\operatorname{tr}(AB),\qquad
c_{n,k}=\frac{2k(n-k)}{n(n-1)(n+2)}.
\]
This follows by invariance and \(\|P-kI/n\|_F^2=k(n-k)/n\), or directly from the beta variance below. Fixing the first coordinate reduces the symmetry to \(O(n-1)\). There is an orthogonal and multiplicity-free decomposition of the coefficient space: the axial line \(\operatorname{diag}(n-1,-1,\ldots,-1)\); the \((n-1)\)-dimensional matrices with only first-row/first-column off-diagonal entries; and the traceless symmetric matrices supported in the remaining \((n-1)\)-block. The last sector has dimension \((n-2)(n+1)/2\). Orthogonal invariance forces one scalar eigenvalue on each sector.

**2. Conditional projector moments.** Put \(S=P_{11}\). A Haar-random \(k\)-plane is obtained from \(k\) columns of a Haar orthogonal matrix, hence
\[
S\sim\operatorname{Beta}(k/2,(n-k)/2).
\]
Conditional on \(S=s\), choose a unit vector \(v\) uniformly in \(e_1^\perp\cong\mathbb R^{n-1}\), and then a Haar-uniform rank-\((k-1)\) projection \(R\) on \(v^\perp\subset e_1^\perp\). In the decomposition \(\mathbb Re_1\oplus e_1^\perp\), the random projection has blocks
\[
P=\begin{pmatrix}s&\sqrt{s(1-s)}v^{\mathsf T}\\
\sqrt{s(1-s)}v&(1-s)vv^{\mathsf T}+R\end{pmatrix}.
\]
For a traceless symmetric \((n-1)\)-matrix \(B\), the conditional mean of \(\operatorname{tr}(BP)\) given \((s,v)\) is
\[
\left(1-s-\frac{k-1}{n-2}\right)v^{\mathsf T}Bv.
\]
The conditional rank-\((k-1)\) projector variance in dimension \(n-2\), together with the spherical moments
\[
\mathbb E_v(v^{\mathsf T}Bv)^2=\frac{2\operatorname{tr}(B^2)}{(n-1)(n+1)},\qquad
\mathbb E_v(v^{\mathsf T}B^2v)=\frac{\operatorname{tr}(B^2)}{n-1},
\]
yields the **complete** conditional second moment
\[
\frac{\mathbb E[f_B(P)^2\mid S=s]}{\operatorname{tr}(B^2)}
=\frac{2}{(n-1)(n+1)}\left(1-s-\frac{k-1}{n-2}\right)^2
+\frac{2(k-1)(n-k-1)}{(n-2)^2(n+1)}.
\]
To verify the variance term directly, write \(D=n-2\), \(r=k-1\), and \(B_v=(I-vv^{\mathsf T})B(I-vv^{\mathsf T})\). The invariant rank-\(r\) projector covariance on \(v^\perp\) is
\[
\operatorname{Var}_R(\operatorname{tr}(RB_v))
=\frac{2r(D-r)}{D(D-1)(D+2)}\left(\operatorname{tr}(B_v^2)-\frac{(\operatorname{tr}B_v)^2}{D}\right).
\]
Integrating this formula in \(v\) gives the displayed constant. The axial and vector conditional moments follow immediately from \(s-k/n\) and \(\sqrt{s(1-s)}v\).

**3. Polynomial densities and exact spectrum.** After dividing by the full covariance coefficient \(c_{n,k}\), the conditional squared energies per unit coefficient Hilbert-Schmidt norm become
\[
q_{\mathrm A}(s)=\frac{(n+2)(ns-k)^2}{2k(n-k)},\qquad
q_{\mathrm V}(s)=\frac{n(n+2)s(1-s)}{k(n-k)},
\]
\[
q_{\mathrm T}(s)=\frac{n(n+2)}{k(n-k)(n-2)(n+1)}
\left[k(n-k-1)+2(k-n+1)s+(n-2)s^2\right].
\]
Each \(q\) integrates to \(1\) over the full beta probability law. Therefore \(\lambda_j(t)=\mathbb E[q_j(S)\mathbf1_{S\ge t}]\), giving the three incomplete-beta formulas in the finding and all multiplicities. Positivity and strict upper bounds follow because any nonzero real-analytic \(f_A\) has positive squared mass on both nonempty open regions.

**4. Exactly three pairwise spectral crossings.** Write
\[
F_{n,k}(t)=\frac{t^{k/2}(1-t)^{(n-k)/2}}{B(k/2,(n-k)/2)}>0.
\]
Integrating the differences of the preceding quadratic densities by parts against the beta density gives the exact identities
\[
\lambda_{\mathrm A}-\lambda_{\mathrm V}
=F_{n,k}(t)\frac{n(n+2)}{k(n-k)}(t-t_{\mathrm{AV}}),
\]
\[
\lambda_{\mathrm A}-\lambda_{\mathrm T}
=F_{n,k}(t)\frac{n(n-1)(n+2)}{k(n-k)(n+1)}(t-t_{\mathrm{AT}}),
\]
\[
\lambda_{\mathrm V}-\lambda_{\mathrm T}
=F_{n,k}(t)\frac{2n(n+2)}{k(n-k)(n+1)}(t_{\mathrm{VT}}-t).
\]
The crossing heights are all strictly between \(0\) and \(1\). Moreover,
\[
t_{\mathrm{AV}}-t_{\mathrm{AT}}=\frac{2(n-2k)}{n(n-2)},\quad
t_{\mathrm{VT}}-t_{\mathrm{AV}}=\frac{(n-1)(n-2k)}{n(n-2)}.
\]
The signs give every strict ordering stated above, including the equality multiplicities. When \(n=2k\), complementing \(P\mapsto I-P\) preserves Haar measure, replaces \(S\mapsto1-S\), and sends every \(f_A\mapsto-f_A\). Hence the two half-caps at threshold \(1/2\) carry precisely equal energy for **every** \(f_A\), establishing \(T_{1/2}=I/2\), not just a numerical triple crossing.

**5. Thin-cap sharp condition number.** As \(t\uparrow1\), the scalar branch is largest and the vector branch smallest, by the crossing identities. The beta tail \(\int_t^1s^{a-1}(1-s)^{b-1}ds\) is asymptotic to \((1-t)^b/b\). The axial density approaches \(q_{\mathrm A}(1)=(n+2)(n-k)/(2k)\) while \(q_{\mathrm V}(s)\sim n(n+2)(1-s)/[k(n-k)]\). Their tail quotient therefore has the asserted simple-pole constant \((n-k)(n-k+2)/(2n)\). No large-dimension interchange of limits is used.

## Verification
Run `python3 VERIFY.py` with the dependencies named in `requirements.txt`. Exact SymPy identities reconstruct the conditional tensor-sector second moment, normalize all beta densities, factor all three gap identities, check threshold ordering identities, and verify the sharp thin-cap coefficient. Independently, seeded Gaussian-QR sampling constructs Haar-random projections and compares entire finite Gram spectra against the three beta-tail branches for \((n,k,t)=(4,2,0.38),(6,2,0.41),(7,3,0.53)\), with the random experiment explicitly subordinate to the analytic proof. The checker does not prove that unrelated historical literature lacks an equivalent theorem.

## Relationship to prior work
Faifman, *Quasianalyticity, uncertainty, and integral transforms on higher Grassmannians* (first public arXiv version 27 January 2022), studies restrictions on the support and spectral types of Grassmannian distributions and cosine-transform images, but does not classify the first-harmonic energy concentration operator of the present principal-angle cap. Rubin, *On the Injectivity of the Shifted Funk-Radon Transform and Related Harmonic Analysis* (18 November 2022), develops Jacobi-polynomial harmonics and transform multipliers for Stiefel/Grassmannian spaces; its shifted transforms are not the squared-energy cap projection evaluated here. Classical spherical Slepian theory provides the optimization framework but not this real-Grassmannian spectrum. General orthogonal-Haar moment formulas give tools for the conditional computation, but do not by themselves supply the paired crossing identities or sharp rank-dependent ordering.

Related first-harmonic results on real Grassmannians establish an invariant minimum-norm **projection in the uniform norm** or global \(L^4\) moment extremizers. Those solve different operator problems and do not determine the present **conditional** \(L^2\) cap spectrum. A finite-field Grassmannian point-star sampling result concerns a different discrete domain and a different observation mask. The contribution asserted here is the all-integer rank/ambient-dimension three-branch cap law, the distinct ordering regimes, the exact middle-rank half-energy isotropy, and the thin-cap constant, rather than the beta marginal or covariance itself.

## Limitations
The theorem covers only the first nonconstant harmonic representation and only one-coordinate angle-threshold regions. Higher harmonics, arbitrary Schubert masks, joint principal-angle constraints, nonreal Grassmannians, and uniform asymptotics with growing \(n\) are outside its scope. Full-text primary comparison excludes the identified articles' statements, not every possible implicit corollary of general integration formulas. Historical priority is provisional pending broader independent literature review. The verification and scientific review described here are not independent mathematical audits.

## References
1. D. Faifman, *Quasianalyticity, uncertainty, and integral transforms on higher Grassmannians*, arXiv:2201.11734, first posted 2022-01-27; *Advances in Mathematics* 435 (2023), 109348. https://arxiv.org/abs/2201.11734
2. B. Rubin, *On the Injectivity of the Shifted Funk-Radon Transform and Related Harmonic Analysis*, arXiv:2211.10348, first posted 2022-11-18. https://arxiv.org/abs/2211.10348
3. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424, 2004; *SIAM Review* 48 (2006), 504–536. https://arxiv.org/abs/math/0408424
4. S. Matsumoto, *Weingarten calculus for matrix ensembles associated with compact symmetric spaces*, arXiv:1301.5401, 2013, Section 4.2. https://arxiv.org/abs/1301.5401
