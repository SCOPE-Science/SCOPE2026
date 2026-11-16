# Sharp mode staircase and asymptotic stability for Gaussian concentration on anisotropic bidiscs

## Finding
Fix an integer \(m\ge1\), radii \(a,b>0\), and the total-degree-\(m\) holomorphic Gaussian Fock subspace in two complex variables. For concentration on the product of discs \(\{|z_1|^2\le a,\ |z_2|^2\le b\}\), the eigenvalues in the normalized monomial basis are
\[
\lambda_{m,k}(a,b)=Q_k(a)Q_{m-k}(b),\qquad 0\le k\le m,\qquad Q_j(x)=\frac1{j!}\int_0^x e^{-t}t^j\,dt.
\]
The diagonalization and incomplete-gamma formula are instances of the **previously established** quasi-radial Toeplitz calculus. The new assertion is the following complete sharp extremal and stability classification.

**Theorem.** For every fixed \(m\ge1\) and \(b>0\), there exist exactly \(m\) distinct positive thresholds
\[
0<a_0(b,m)<a_1(b,m)<\cdots<a_{m-1}(b,m)<\infty
\]
defined without numerical ambiguity by
\[
\frac{Q_{k+1}(a_k)}{Q_k(a_k)}=\frac{Q_{m-k}(b)}{Q_{m-k-1}(b)},\qquad k=0,\ldots,m-1.
\]
As \(a\) increases, the **unique largest concentration mode** visits every monomial index \(k=0,1,\ldots,m\) in order: it equals \(0\) before \(a_0\), equals \(k\) on \((a_{k-1},a_k)\) for \(1\le k<m\), and equals \(m\) beyond \(a_{m-1}\). At \(a=a_k\) exactly the two neighboring monomials \(k,k+1\) share the largest eigenvalue. There are no triple top ties and no skipped maximizing indices. Every crossing is transverse: the largest-eigenvalue envelope has a strictly positive right-minus-left slope jump there. For any fixed \(b>0\) and \(0<s<1\), the thresholds additionally obey \[\lim_{m\to\infty}a_{\lfloor sm\rfloor}(b,m)=\frac{bs}{1-s}.\] All eigenvalues are strictly positive.

The least eigenvalue is exactly
\[
\lambda_{\min}=Q_m(h)Q_0(v),\qquad h=\min(a,b),\quad v=\max(a,b).
\]
It occurs solely at index \(k=m\) for \(a<b\), solely at \(k=0\) for \(a>b\), and at both endpoint indices for \(a=b\) (the two endpoints coincide only when \(m=0\), which is outside our scope).

Write \(\kappa_m(a,b)=\lambda_{\max}/\lambda_{\min}\) for the **squared-energy** restriction-frame condition ratio. For every fixed \(a,b>0\), as \(m\to\infty\),
\[
\boxed{\displaystyle
\kappa_m(a,b)\sim \frac{v}{(e^v-1)\sqrt{2\pi}}\left(\frac{(a+b)^2}{ab}\right)^{3/2}m^{-3/2}\left(\frac{a+b}{h}\right)^m.}
\]
Thus the instability has both a sharp exponential base and a sharp nonzero polynomial prefactor. Every maximizing index \(k_m\), including indices in a two-mode tie, satisfies
\[
k_m=\frac{a}{a+b}m+O_{a,b}(1).
\]

## Assumptions and scope
The normalized Gaussian Fock measure is
\[
d\gamma_2(z_1,z_2)=\pi^{-2}e^{-|z_1|^2-|z_2|^2}\,dA(z_1)dA(z_2).
\]
Set \(\mathcal H_m=\operatorname{span}\{e_{m,k}:0\le k\le m\}\) with \(e_{m,k}(z)=z_1^kz_2^{m-k}/\sqrt{k!(m-k)!}\). This is an orthonormal subspace of the analytic Fock space. The observation set is the **solid bidisc**, not a torus or a sphere:
\[
E_{a,b}=\{(z_1,z_2)\in\mathbb C^2:|z_1|^2\le a,\ |z_2|^2\le b\}.
\]
The concentration matrix is \(G_{k\ell}=\int_{E_{a,b}}e_{m,k}(z)\overline{e_{m,\ell}(z)}\,d\gamma_2(z)\). Its Rayleigh quotient equals the observed squared-energy fraction. The ordinary (unsquared) singular-value condition number is \(\sqrt{\kappa_m}\); the theorem consistently uses the **eigenvalue** ratio \(\kappa_m\). All radius and degree quantifiers are explicit above. The asymptotic holds for *fixed positive* \(a,b\), not radii that vary with \(m\).

## Proof
**1. Diagonalization and known radial integral.** Independent phase rotations in both complex coordinates preserve \(E_{a,b}\) and the measure; integrating distinct monomials against the angular variables makes \(G\) diagonal. Polar integration with \(t=|z_j|^2\) gives
\[
G_{kk}=\left[\frac1{k!}\int_0^ae^{-t}t^kdt\right]\left[\frac1{(m-k)!}\int_0^be^{-s}s^{m-k}ds\right]=Q_k(a)Q_{m-k}(b).
\]
This is the elementary two-block specialization of the previously known quasi-radial Fock Toeplitz eigenvalue formula (Dewage–Ólafsson, Theorem 2.12); it is not a novel independent spectral-diagonalization claim. Each \(Q_j(x)\) lies strictly between zero and one for \(x>0\), proving injectivity on \(\mathcal H_m\).

**2. Strict ratio law.** For nonnegative integers \(j\), define the consecutive incomplete-gamma ratio \(r_j(x)=Q_{j+1}(x)/Q_j(x)\). The elementary identity
\[
Q_j(x)=e^{-x}\sum_{t=j+1}^{\infty}\frac{x^t}{t!}
\]
shows
\[
r_j(x)=1-\frac{1}{F_j(x)},\qquad
F_j(x)=1+\sum_{s=1}^{\infty}\frac{x^s}{(j+2)(j+3)\cdots(j+s+1)}.
\]
All denominators are positive. Thus \(F_j(x)\), and hence \(r_j(x)\), is **strictly increasing** in \(x>0\) and **strictly decreasing** in the integer \(j\ge0\). At fixed \(j\), \(r_j(x)\) tends to zero as \(x\downarrow0\) and to one as \(x\to\infty\). Moreover, as \(j\to\infty\) with \(x\) fixed,
\[
r_j(x)=\frac{x}{j+2}\big(1+O_x(j^{-1})\big),
\quad Q_j(x)=e^{-x}\frac{x^{j+1}}{(j+1)!}\big(1+O_x(j^{-1})\big).
\]
Indeed \(F_j(x)=1+x/(j+2)+O_x(j^{-2})\) from the absolutely convergent positive series, which proves the first expansion; the second follows by factoring the leading term of the Poisson tail.

**3. All \(m\) mode transitions.** The ratio of neighboring eigenvalues is
\[
R_k(a,b)=\frac{\lambda_{m,k+1}}{\lambda_{m,k}}=\frac{r_k(a)}{r_{m-k-1}(b)},\qquad 0\le k<m.
\]
For each \(a,b>0\), the numerator strictly decreases with \(k\) and the denominator strictly increases, so \(R_k\) strictly decreases with \(k\). In particular, the eigenvalue sequence is strictly log-concave, hence its largest value can be attained at only one position or at two **adjacent** positions. At fixed \(b,m,k\), the continuous strictly increasing function \(a\mapsto r_k(a)\) runs from zero to one, while \(r_{m-k-1}(b)\) lies strictly between them. There is therefore precisely one solution \(a_k\) to \(R_k=1\). If \(k\) increases then \(R_k(a,b)\) decreases at every common \(a\), forcing \(a_{k+1}>a_k\). As \(a\) passes each successive root, the number of ratios above one increases one at a time. This proves the complete no-skipping staircase and precisely two equal top eigenvalues at each root. Their two eigenspaces are the corresponding monomials, with no further degeneracy. Moreover, differentiating \(\lambda_{m,k+1}-\lambda_{m,k}=\lambda_{m,k}(R_k-1)\) at \(a=a_k\) gives the strictly positive slope jump \[\lambda_{m,k}(a_k,b)\,\frac{r_k'(a_k)}{r_k(a_k)}>0,\] because the preceding positive-term series has \(r_k'(a)>0\). For \(k=\lfloor sm\rfloor\) with fixed \(s\in(0,1)\), the ratio estimates in Step 2 at any fixed \(a>0\) show \(mR_k(a,b)\) is unnecessary: directly \(R_k(a,b)\to a(1-s)/(bs)\). Comparing the signs on either side of \(a=bs/(1-s)\) and using the uniqueness of \(a_k\) proves the asserted continuum threshold limit.

**4. The exact least-observable mode.** Strict log-concavity implies \(\lambda_{m,k}\ge\min(\lambda_{m,0},\lambda_{m,m})\) at every internal index, strictly for \(m\ge2\). The endpoints satisfy
\[
\frac{\lambda_{m,m}}{\lambda_{m,0}}
=\frac{Q_m(a)/Q_0(a)}{Q_m(b)/Q_0(b)}
=\prod_{j=0}^{m-1}\frac{r_j(a)}{r_j(b)}.
\]
By strict increase of \(r_j(x)\) in \(x\), this ratio is less than, equal to, or greater than one according as \(a<b\), \(a=b\), or \(a>b\). This identifies the minimizing endpoint(s) and yields the exact least eigenvalue. The proof also covers \(m=1\), where only the two endpoint eigenvalues exist.

**5. Location of the strongest mode at large degree.** Fix \(a,b>0\) and put \(p=a/(a+b)\), \(q=1-p\). In any fixed interior fraction of \(0\le k\le m\), the large-index ratio estimate in Step 2 gives uniformly
\[
R_k(a,b)=\frac{a(m-k+1)}{b(k+2)}\big(1+O_{a,b}(m^{-1})\big).
\]
For any fixed \(\varepsilon>0\), this is above one at \(k\le(p-\varepsilon)m\) and below one at \(k\ge(p+\varepsilon)m\), for all sufficiently large \(m\). Hence a maximizing index is \(pm+o(m)\). Substituting \(k=pm+o(m)\) into the ratio equation and using the uniform estimates yields \(k=pm+O_{a,b}(1)\). This argument also applies to either index in the adjacent-mode tie.

**6. Sharp squared-energy conditioning.** By Step 4 and symmetry of the two coordinates, assume \(a=h\le b=v\); then \(\lambda_{\min}=Q_m(a)Q_0(b)\). In Step 5 let \(k_m=pm+O_{a,b}(1)\), with \(p=a/(a+b)\), \(q=b/(a+b)\). The gamma-tail expansion from Step 2 gives
\[
\frac{\lambda_{m,k_m}}{\lambda_{\min}}
=\frac{b}{e^b-1}\frac{(m+1)!}{(k_m+1)!(m-k_m+1)!}\left(\frac ba\right)^{m-k_m}\big(1+O_{a,b}(m^{-1})\big).
\]
The combinatorial fraction factors as
\[
\frac{(m+1)!}{(k+1)!(m-k+1)!}
=\binom{m}{k}\frac{m+1}{(k+1)(m-k+1)}.
\]
Uniform Stirling asymptotics for \(k=pm+O(1)\) (where shifting the integer maximum by a bounded amount changes the saddle-point weight only by \(1+O_{a,b}(m^{-1})\)) now yield
\[
\binom{m}{k_m}\left(\frac ba\right)^{m-k_m}
=\frac{p^{-m}}{\sqrt{2\pi mpq}}\big(1+O_{a,b}(m^{-1})\big),
\]
\[
\frac{m+1}{(k_m+1)(m-k_m+1)}=\frac1{mpq}\big(1+O_{a,b}(m^{-1})\big).
\]
Consequently
\[
\kappa_m(a,b)=\frac{b}{(e^b-1)\sqrt{2\pi}(pq)^{3/2}}
 m^{-3/2}p^{-m}\big(1+O_{a,b}(m^{-1})\big).
\]
Substituting the definitions of \(p,q\) and reinstating \(h,v\) gives the boxed asymptotic, including the identical-radii case where the least eigenvalue has two endpoint realizations.

## Verification
The standalone `verify.py` independently evaluates the gamma-tail eigenvalues at 70-digit precision and compares them with the neighboring-ratio formula. It checks strict log-concavity, the correct minimizing endpoint and exact dependence on radius across multiple small degrees. A bisection solver for a degree-five example with \(b=2\) verifies the five strictly ordered thresholds, each two-way maximum and every intervening maximizing mode. Additional numerical checks compare the exact condition ratio against its sharp prefactor through degree 220 at three unequal/equal radius pairs, and independently integrate the Gaussian radial moments. Output is in `check_output.txt` and is reproducible with Python 3 plus `mpmath`. The proof above, **not** those finite tests, establishes the all-degree and all-radius statements.

## Relationship to prior work
Dewage and Ólafsson (arXiv:2107.01465, first publicly posted 2021-07-03), especially Theorem 2.12 and the subsequent product/quasi-radial special cases, prove the applicable **diagonalization and integral spectrum formula** for general bounded quasi-radial Fock Toeplitz symbols. That result covers the formula for \(\lambda_{m,k}\); this paper makes no originality assertion for it. The present proposed increment is the complete **strictly ordered sequence of all fixed-degree maximizing-mode transitions** with precise equality spaces, exact weakest mode, and the sharp large-degree concentration condition ratio including its \(m^{-3/2}\) prefactor. These conclusions are not stated in the examined quasi-radial treatment.

Knutsen's arXiv:2204.03068 (first posted 2022-04-06) develops Gaussian short-time Fourier localization and Gabor-multiplier uncertainty estimates for porous sets, not exact restrictions of one total-Hermite-degree sector to two independent Gaussian discs. Classical single-annulus Gaussian localization has a Hermite-mode staircase, but uses one radial index with a *difference* of incomplete-gamma tails and does not imply the present constrained two-index **product** optimization or conditioning constant. A published harmonic-analysis record entitled *Exact Gaussian-annulus eigenmode crossings and a Bernoulli second-order concentration law* was inspected in full for that comparison. Another published record on anisotropic Gaussian Fock projections treats geometric-product singular spectra of integral Gaussian kernels, whereas this indicator-bidisc problem has **incomplete-gamma tail products**. A published product-cap result on complex spheres uses Dirichlet distributions and a product inequality, not independent truncated gamma variables. No statement-to-statement implication establishing the present mode/conditioning result was found in these inspected works. The elementary Poisson-tail ratio inequalities and Stirling asymptotics remain standard ingredients, not independent claims of novelty.

## Limitations
The method uses the exact Gaussian weight, the indicator of an axis-aligned product of two centered discs, and one *fixed total-degree* holomorphic polynomial sector. It does not cover unequal or translated Fock weights, arbitrary nonproduct masks, arbitrary finite bands, or radii varying with degree. The result concerns the eigenvalue condition ratio; the usual singular-value condition number is its square root. The novelty assessment is a best-knowledge literature comparison, not a proof of priority; classical incomplete-gamma, Poisson-tail, and Fock localization sources may contain equivalent specialized optimization statements. No independent audit has been performed.

## References
1. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465v1 (2021-07-03), especially Theorem 2.12, https://arxiv.org/abs/2107.01465.
2. H. Knutsen, *A Fractal Uncertainty Principle for the Short-Time Fourier Transform and Gabor multipliers*, arXiv:2204.03068v1 (2022-04-06), https://arxiv.org/abs/2204.03068.
3. I. Daubechies, *Time-frequency localization operators: A geometric phase space approach*, IEEE Transactions on Information Theory **34** (1988), 605–612, DOI 10.1109/18.9761, for the classical Gaussian localization framework.
4. *Exact Gaussian-annulus eigenmode crossings and a Bernoulli second-order concentration law*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-gaussian-annulus-eigenmode-crossings-and-a-bernoulli-secon--57fcc645d909.
5. *Anisotropic Gaussian Fock projections: exact singular spectra and a rational–irrational counting transition*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-anisotropic-gaussian-fock-projections-exact-singular-spectra-and--1cedacd12a18.
6. *Balanced extremizers and a parity-dependent spectral-gap transition for holomorphic product caps*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-balanced-extremizers-and-a-parity-dependent-spectral-gap-transit--6fabf57d9095.
