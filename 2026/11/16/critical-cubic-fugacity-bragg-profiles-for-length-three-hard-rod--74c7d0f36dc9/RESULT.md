# Critical cubic-fugacity Bragg profiles for length-three hard rods on a cycle

## Finding

Let \(n=3m\) with \(m\to\infty\). On the labelled cycle \(\mathbb Z/n\mathbb Z\), sample a zero-one vector \(X=(X_0,\ldots,X_{n-1})\) with no two occupied positions at cyclic distance one or two, assigning each admissible vector probability proportional to \(z_m^{\sum_a X_a}\). Fix \(c>0\) and take \(z_m=c(3m)^3\). Let \(K_m\) be the covariance matrix of the occupation indicators. Its spatial Fourier eigenvalue at frequency \(\ell\) is \(\lambda_{m,\ell}\).

For every **fixed integer** \(j\), the near-Bragg Fourier mode \(\ell=m+j\) has the nonzero, finite critical-scale limit

\[
\lim_{m\to\infty}\frac{\lambda_{m,m+j}}{3m}
=\mathcal B_j(c)
=\frac{2}{9H_0(u)}\operatorname{Re}\int_0^1(1-t)e^{2\pi ijt}
 H_0\bigl(u(1-t+t\omega)\bigr)\,dt,
\]

where \(u=(27c)^{-1/3}\), \(\omega=e^{2\pi i/3}\), and the entire function \(H_0(w)=\sum_{r=0}^{\infty}w^{3r}/(3r)!\). In particular the central Bragg harmonic has the **closed form**

\[
\boxed{\mathcal B_0(c)=\frac{H_1(u)}{9H_0(u)},\qquad
H_1(u)=\sum_{r=0}^{\infty}\frac{u^{3r}}{(3r+1)!}.}
\]

The two endpoint regimes of the limiting central profile are sharp:

\[
\mathcal B_0(c)=\frac19-\frac{1}{1944c}+O(c^{-2})\quad(c\to\infty),
\qquad \mathcal B_0(c)\sim\frac{c^{1/3}}3\quad(c\downarrow0).
\]

For any fixed nonzero \(j\), \(\mathcal B_j(c)>0\) for \(c>0\) and \(\mathcal B_j(c)\to0\) as \(c\to\infty\). At fixed \(c\), all these limits describe the Fourier peak on the order-one frequency-index scale around \(n/3\); the conjugate peak at \(2n/3\) has the same spectrum by reality.

## Assumptions and scope

The cyclic exclusion is strict: if \(X_a=1\), then \(X_{a\pm1}=X_{a\pm2}=0\) modulo \(n\). Every admissible labelled vector is included (including the empty vector). The weight is a grand-canonical monomial \(z_m^k\), where \(k=\sum_aX_a\); no kinetic or quantum interactions are assumed. The Fourier transform here is the **unnormalized** sum \(T_{m,\ell}=\sum_{a=0}^{n-1}X_ae^{2\pi i\ell a/n}\). The covariance eigenvalues use the standard unit-norm Fourier vectors \(n^{-1/2}(e^{2\pi i\ell a/n})_{a=0}^{n-1}\). Therefore for any nonzero frequency \(\ell\), \(\lambda_{m,\ell}/n=\mathbb E|T_{m,\ell}/n|^2\). The theorem requires fixed \(c\) and fixed \(j\) as \(m\to\infty\); it does not assert uniformity in a growing offset or in a varying \(c\).

## Proof

**1. Exact finite-cycle counting and critical defect law.** For \(1\le k\le\lfloor n/3\rfloor\), mark one of the \(k\) occupied sites and list the forward gaps. Each gap has length \(3+s_a\), with \(s_a\ge0\) and \(\sum_{a=1}^k s_a=n-3k\). Double-counting marked labelled configurations gives

\[
A_{n,k}=\frac nk\binom{n-2k-1}{k-1},\qquad A_{n,0}=1.
\]

Write the occupation deficit as \(R_m=m-k\). For \(0\le r\le m\), relative to the three perfect packings of size \(m\), the grand-canonical weight of deficit \(r\) is

\[
w_m(r)=\frac{m}{m+2r}\binom{m+2r}{3r}\bigl(27cm^3\bigr)^{-r}.
\]

This formula also holds at \(r=m\) (the empty configuration). For each fixed \(r\), \(w_m(r)\to u^{3r}/(3r)!\). Since \(m+2r\le3m\),

\[
0\le w_m(r)\le\frac{c^{-r}}{(3r)!},
\]

so dominated convergence for the finite sums, extended by zero for \(r>m\), proves

\[
\mathbb P(R_m=r)\longrightarrow
\frac{u^{3r}}{(3r)!H_0(u)}.
\]

This derives, rather than assumes, the cubic activity scale.

**2. Fixed-deficit geometry.** Conditional on \(R_m=r<m\), choose an occupied vertex as a uniformly marked origin. The cyclic slack vector \((s_1,\ldots,s_k)\), with \(k=m-r\), is uniform over all weak compositions of \(S=3r\) into \(k\) parts. For fixed \(S\), the chance that any part is at least two is \(O_S(k^{-1})\), by a union bound and the ratio of stars-and-bars counts. On the complement, the \(S\) slack-unit positions are a uniform subset of the \(k\) gaps; after division by \(k\), they converge jointly to the order statistics of \(S\) independent uniform points on \([0,1]\). Let \(M_S(t)\) count these limiting points in \([0,t]\).

If the occupied vertices in cyclic order are \(x_a\), their successive gaps are \(3+s_a\). At mode \(m+j\), the factor from a length-three gap is \(e^{2\pi i j/m}\), and each excess unit contributes \(\omega\) up to a factor tending uniformly to one for fixed \(r,j\). Consequently, up to a harmless unit complex phase from the marked origin,

\[
\frac{T_{m,m+j}}{3m}\ \xrightarrow{\ \mathrm{law}\ }
\frac13I_{S,j},\qquad
I_{S,j}:=\int_0^1 e^{2\pi ijt}\omega^{M_S(t)}\,dt.
\]

The absolute values on the left are bounded by \(1/3\). Hence the squared moduli converge in expectation for fixed \(r\). The bound, together with the summable defect-weight majorant in step 1, permits mixing over all \(r\) by dominated convergence. For \(r=m\), the configuration is empty and its Fourier amplitude is zero, so no marked origin is needed.

**3. Exact near-Bragg line shape.** For \(S\) independent uniform defect locations and \(0\le s<t\le1\), the number between \(s\) and \(t\) is binomial, giving

\[
\mathbb E\omega^{M_S(t)-M_S(s)}
=\bigl(1-(t-s)+(t-s)\omega\bigr)^S.
\]

Integrating over \((s,t)\) yields

\[
\mathbb E|I_{S,j}|^2
=2\operatorname{Re}\int_0^1(1-t)e^{2\pi ijt}
 (1-t+t\omega)^S\,dt.
\]

Weight this identity by \(u^{3r}/((3r)!H_0(u))\), set \(S=3r\), and interchange the absolutely convergent sum and integral. The resulting formula is exactly \(\mathcal B_j(c)\). At nonzero Fourier modes spatial translation invariance forces \(\mathbb ET_{m,m+j}=0\), so the limit is a limit of covariance eigenvalues, not merely uncentered Fourier energies.

**4. Closed central profile.** For \(j=0\), let \(D_0,\ldots,D_S\) be the lengths of the \(S+1\) random subintervals cut out by the \(S\) uniform defects. This vector is Dirichlet with all parameters one; \(I_{S,0}=\sum_{a=0}^S\omega^aD_a\). Its moments are \(\mathbb ED_aD_b=(1+\mathbf1_{a=b})/((S+1)(S+2))\). Because \(S=3r\) and \(\sum_{a=0}^{S}\omega^a=1\),

\[
\mathbb E|I_{3r,0}|^2
=\frac{(3r+1)+|1|^2}{(3r+1)(3r+2)}
=\frac1{3r+1}.
\]

Mixing this with the defect law gives \(H_1(u)/(9H_0(u))\). The first two Taylor terms are \(H_0(u)=1+u^3/6+O(u^6)\) and \(H_1(u)=1+u^3/24+O(u^6)\), which give the stated large-\(c\) expansion. As \(u\to\infty\), root-of-unity filtering of \(e^u\) gives \(H_0(u)\sim e^u/3\) and \(uH_1(u)\sim e^u/3\), giving the small-\(c\) asymptotic.

For fixed nonzero \(j\), the defect-free contribution is \(I_{0,j}=\int_0^1e^{2\pi ijt}\,dt=0\). At least one positive-weight defect count produces a nondegenerate random Fourier integral, proving strict positivity for any finite \(c\). As \(c\to\infty\), the limiting defect count tends to zero, forcing \(\mathcal B_j(c)\to0\).

## Verification

The attached standard-library script `check.py` compares the exact composition count against independent exhaustive enumeration, checks weighted pair-correlation Fourier intensities for cyclic lengths 6 through 15, and numerically checks finite-length convergence to the independently evaluated limiting formulas at three activities and three frequency offsets. Its final status is `PASS 111 finite assertions`. These tests are **not** substituted for the infinite-family proof above. Example: at \(c=1\), the computed central limit is approximately \(0.110599684288\); the finite values at \(n=36,72,144\) approach it.

## Relationship to prior work

Classical one-dimensional hard-rod counting, joint distributions, and thermodynamics are not claimed as new. Bakhti, Müller and Maass (2013) give a general Markov-based lattice-rod density-functional treatment; Benmessabih, Bakhti and Chellali (2021) derive isobaric thermodynamics. Jauslin and Lebowitz (2017) explain high-fugacity expansions and explicitly discuss fractional-power behavior in one-dimensional exclusion models. Their results motivate the close-packing scaling but do **not** state this finite periodic cubic-activity diffraction window or the explicit all-fixed-offset Fourier covariance limits. The distinct step here is the joint mesoscopic limit of cyclic gaps, a Poisson/Dirichlet phase-slip law, and its closed near-Bragg profile. Possible equivalent results elsewhere in exact lattice-gas diffraction literature remain a priority risk.

## Limitations

This is a self-contained mathematical derivation, not independently audited. The theorem addresses the subsequence of lengths divisible by three and fixed Fourier-index offsets, not every cycle length or the whole Fourier spectrum. It makes no claim about uniformity for \(j\) growing with \(m\), about dynamical scattering, or about arbitrary rod lengths. The limiting function is **not** a thermodynamic phase transition at fixed positive activity: the activity itself grows cubically with the system size. No claim of first-ever historical priority is made.

## References

1. I. Jauslin and J. L. Lebowitz, *Crystalline ordering and large fugacity expansion for hard core lattice particles*, first posted 2017-05-04, arXiv:1705.02032, https://arxiv.org/abs/1705.02032 .
2. B. Bakhti, G. Müller and P. Maass, *Interacting hard rods on a lattice: Distribution of microstates and density functionals*, 2013, arXiv:1312.4142, https://arxiv.org/abs/1312.4142 .
3. T. Benmessabih, B. Bakhti and R. Chellali, *Thermodynamics of interacting hard rods on a lattice*, first posted 2021-03-10, arXiv:2103.06348, https://arxiv.org/abs/2103.06348 .
