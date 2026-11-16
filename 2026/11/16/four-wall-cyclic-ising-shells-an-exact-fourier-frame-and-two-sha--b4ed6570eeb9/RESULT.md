# Four-wall cyclic Ising shells: an exact Fourier frame and two sharp extremal-mode changes

## Finding
For every integer \(n\ge5\), let \(\mathcal W_n\) consist of the spin vectors \(\sigma\in\{-1,1\}^n\) with exactly four cyclic sign changes, including the edge from the final spin back to the first. Uniformly sample \(\mathcal W_n\). For the coordinate Walsh characters \(\phi_j(\sigma)=\sigma_j\), define their probability-normalized Gram matrix \(G_n=(\mathbb E_{\mathcal W_n}\phi_i\phi_j)_{0\le i,j<n}\). The means vanish, so this is also the covariance matrix. Its eigenvectors are the cyclic Fourier modes \(v_k(j)=\exp(2\pi\mathrm i kj/n)\).

Put \(A_n=n^2-3n+8\), \(P_n=(n-1)(n-2)(n-3)\), and \(u_{n,k}=\sin^2(\pi k/n)\). **Every eigenvalue is strictly positive**, with the complete formula
\[
\boxed{\lambda_{n,0}=\frac{n-4}{5},\qquad
\lambda_{n,k}=\frac{4(A_nu_{n,k}-6)}{P_nu_{n,k}^2}\quad(1\le k<n).}
\]
The sharp largest and smallest Fourier sectors change at different exact integer thresholds:

* For \(5\le n\le11\), the largest eigenvalues are exactly the conjugate modes \(k=2,n-2\). For every \(n\ge12\), the unique largest eigenvalue is the constant spatial mode \(k=0\).
* For \(5\le n\le7\), the unique smallest eigenvalue is at \(k=0\). At \(n=8\), the minimum is shared exactly by \(k=0\) and \(k=4\), both equal to \(4/5\). For every \(n\ge9\), the smallest eigenvalue occurs exactly at the highest cyclic spatial frequencies \(k=\lfloor n/2\rfloor\) and \(k=\lceil n/2\rceil\) (one mode when \(n\) is even).

Consequently the evaluation map \(a\mapsto\sum_j a_j\phi_j\) is injective on every four-wall shell; its **sharp squared coefficient-to-observation condition number** is the ratio of the two specified extremal eigenvalues. In particular, for every even \(n\ge12\),
\[
\boxed{\kappa_n=\frac{(n-4)(n-3)}{20},}
\]
while for both parities \(\kappa_n\sim n^2/20\). The stated \(\kappa_n\) is the eigenvalue ratio (squared singular-value condition number), not the unsquared singular-value ratio.

## Assumptions and scope
The cyclic index \(j\) ranges over \(\mathbb Z/n\mathbb Z\); a domain wall is the edge at which adjacent spins disagree. Four domain walls are possible for \(n\ge5\), and each choice of four wall edges and one starting spin specifies one configuration; hence \(|\mathcal W_n|=2\binom n4\). The probability measure gives all these configurations equal weight. No independent normalization of individual Walsh columns is required because each has squared norm one. The formulas use the unitary discrete Fourier eigenvectors, whose eigenvalues are those of the raw \(n\times n\) probability Gram matrix, not a matrix divided by \(n\).

## Proof
**1. Fourier-diagonalizable two-point law.** Global spin flip shows \(\mathbb E\phi_j=0\). Cyclic shifts preserve the ensemble, hence \(G_n\) is real symmetric circulant. For \(0\le t<n\), the product \(\sigma_0\sigma_t\) equals \((-1)^J\), where \(J\) is the number of wall edges among the \(t\) consecutive edges from zero to \(t\). Conditional on exactly four walls, \(J\) is hypergeometric, and therefore
\[
C_n(t)=\mathbb E(\sigma_0\sigma_t)
=\frac{\sum_{j=0}^4(-1)^j\binom tj\binom{n-t}{4-j}}{\binom n4}.
\]
Binomial coefficients with an inadmissible lower index are zero. Setting \(q_n(t)=t(n-t)\) and expanding the numerator gives the polynomial identity
\[
C_n(t)=1-\frac{8(n^2-3n+4)}{nP_n}q_n(t)
+\frac{16}{nP_n}q_n(t)^2.
\]
This identity includes the endpoints \(t=0\) and \(t=n\). It also makes the \(n\)-periodic symmetry \(C_n(t)=C_n(n-t)\) explicit.

**2. Exact Fourier transform.** Write \(\Delta f(t)=f(t+1)-2f(t)+f(t-1)\) with indices interpreted cyclically and \(\delta_0\) for the Kronecker mass at the origin. Direct polynomial differences, including the cyclic wrap at zero, yield
\[
\Delta q_n=-2+2n\delta_0,\qquad
\Delta(q_n^2)=-12q_n+2(n^2+1)-4n\delta_0.
\]
For a nonzero Fourier mode, \(\widehat\Delta=-4u_{n,k}\), so
\[
\widehat q_n(k)=-\frac{n}{2u_{n,k}},\qquad
\widehat{q_n^2}(k)=\frac{n}{u_{n,k}}-\frac{3n}{2u_{n,k}^2}.
\]
Substituting into the polynomial expression for \(C_n\) proves the displayed nonzero-mode eigenvalues. For the zero mode use the elementary exact sums
\[
\sum_{t=0}^{n-1}q_n(t)=\frac{n(n^2-1)}6,\qquad
\sum_{t=0}^{n-1}q_n(t)^2=\frac{n(n^4-1)}{30},
\]
which give \(\lambda_{n,0}=(n-4)/5\). This also verifies the trace normalization \(\sum_{k=0}^{n-1}\lambda_{n,k}=n\).

**3. Strict positivity and the shape of the spectrum.** Write \(f_n(u)=4(A_nu-6)/(P_nu^2)\) for \(0<u\le1\). Its derivative has the sign of \(12-A_nu\), so the nonconstant branch rises once and then falls. The inequalities \(A_nu_{n,1}>6\) for all \(n\ge5\) follow at \(n=5\) from \(18\sin^2(\pi/5)>6\), and thereafter by the monotonicity of \(n\sin(\pi/n)\) and the nondecreasing integer sequence \(A_n/n^2\). Since \(u_{n,k}\ge u_{n,1}\), every nonzero eigenvalue is positive; the zero mode is positive as well. Moreover \(A_nu_{n,1}<\pi^2<12\) and \(A_nu_{n,2}>12\) for every \(n\ge5\). Thus the largest nonconstant eigenvalue is one of the modes \(k=1,2\), and its smallest is one of \(k=1,\lfloor n/2\rfloor\).

**4. Sharp extremal switches.** The exact pairwise comparison is
\[
f_n(u)-f_n(v)=\frac{4(v-u)[A_nuv-6(u+v)]}{P_nu^2v^2}.
\]
For \(n\ge12\), the elementary Taylor inequality \(\sin x\ge x(1-x^2/6)\), together with \(3.14<\pi<22/7\), gives
\[
\frac{6}{n^2}\left(\frac1{u_{n,1}}+\frac1{u_{n,2}}\right)
<0.78977<\frac{29}{36}\le\frac{A_n}{n^2}.
\]
Hence \(\lambda_{n,1}>\lambda_{n,2}\) for all \(n\ge12\). For \(n\ge14\), use \(u_{n,1}<\pi^2/n^2<12/A_n\), the increasing branch of \(f_n\), and \(\pi<22/7\) to reduce \(\lambda_{n,0}>f_n(u_{n,1})\) to positivity of
\[
(n-4)P_n(22/7)^4-20n^2 A_n(22/7)^2+120n^4.
\]
Substitution \(n=14+h\) makes this a polynomial in \(h\ge0\) with every coefficient strictly positive. The two remaining lengths \(n=12,13\) satisfy the same comparison by exact rational trigonometric intervals.

For \(n\ge9\), the inequalities \(\sin(\pi/n)>3/n\), \(1/u_{n,\lfloor n/2\rfloor}<26/25\), and \(A_n>2n^2/3+156/25\) show from the pairwise comparison that \(f_n(u_{n,1})>f_n(u_{n,\lfloor n/2\rfloor})\). Since the branch is unimodal, the highest-frequency mode is then the least among nonzero modes. It is also below the zero mode because \(u_{n,\lfloor n/2\rfloor}\ge3/4\), the branch decreases there, and
\[
 f_n(u_{n,\lfloor n/2\rfloor})\le f_n(3/4)
=\frac{16n}{3(n-1)(n-2)}<\frac{n-4}{5}\quad(n\ge9).
\]
The remaining finitely many comparisons, \(5\le n\le13\), are established by the reproducible **rational interval certificate** in `verify.py`. It derives rigorous bounds on \(\pi\) from Machin's arctangent identity and alternating rational Taylor bounds for all sines, and compares disjoint rational eigenvalue intervals. Thus the exact switches, including the equality at \(n=8\), are not inferred from floating-point experiments.

**5. Stability.** The condition-number assertions follow by dividing the extremal eigenvalues. When \(n\) is even, \(u_{n,n/2}=1\) and \(f_n(1)=4/(n-3)\). For \(n\ge12\), the maximum is \((n-4)/5\), giving the displayed exact even-size condition number. For odd \(n\), \(u_{n,\lfloor n/2\rfloor}=\cos^2(\pi/(2n))\to1\). Therefore both parities have \(\kappa_n\sim n^2/20\).

## Verification
Execute `python3 verify.py` with Python 3.10 or later and SymPy installed. The script independently expands the hypergeometric polynomial and proves the cyclic-difference identities symbolically; it derives exact rational enclosures for all small-length trigonometric comparisons by the Machin arctangent identity and alternating Taylor bounds; it verifies the positivity of the coefficients in the two general integer inequalities; and it checks the predicted eigenvalues against direct covariance Fourier sums for \(5\le n\le13\). All checks passed on the supplied source. No finite computation is substituted for the all-integer inequalities in the proof.

## Relationship to prior work
Rao's 2021 Fourier analysis on fixed-weight Boolean slices [1] concerns harmonic representations of a different, fully permutation-symmetric constraint; the present sampling shell fixes **cyclic edge transitions**, not Hamming weight, and the sharp spatial Fourier conditioning does not follow from the slice restriction identity. Sitarachu, Zia, and Bachmann's microcanonical Ising study [2] gives exact finite-ring broken-bond state counts and energy statistics, supplying the natural four-wall ensemble; it does not compute its conditional coordinate-character Gram spectrum or its two sharp extremal-mode changes. General Ising domain statistics [3] provide a physical precedent, but are concerned with free-boundary domain distributions, not the cyclic Fourier frame theorem.

The most closely related accessible harmonic-frame statements are the exact Fourier spectra of proper colourings of cycles [4] and of Lucas cubes [5]. Their observation supports respectively forbid every equal adjacent colour, or forbid adjacent ones; neither is the fixed-four-wall energy shell. Their formulas and limiting condition numbers cannot imply the present polynomial Krawtchouk covariance, integer-size switches or quadratic conditioning growth. The comparison does not claim that every older microcanonical two-point formula has been ruled out: such a formula could implicitly recover individual eigenvalues without identifying the sharp extremal classifications.

## Limitations
This is a first-degree coordinate-Walsh sampling theorem on the **exactly four-domain-wall** cyclic level set; it does not cover arbitrary wall counts, higher Walsh degrees, noisy reconstruction algorithms, or nonuniform Gibbs weights. Full historical priority remains provisional because older physical structure-factor computations may encode parts of the transform under another normalization. The sharp two-switch theorem and its proof are new assertions here, not claimed to have independent mathematical validation. No independent audit has been performed.

## References
1. S. Rao, *The Fourier Transform of Restrictions of Functions on the Slice*, arXiv:2111.03213v1, first public 2021-11-05, https://arxiv.org/abs/2111.03213 (full HTML, introduction and Theorems 1.1–1.2, basis and restriction definitions inspected).
2. K. Sitarachu, R. K. P. Zia, M. Bachmann, *Exact microcanonical statistical analysis of transition behavior in Ising chains and strips*, J. Stat. Mech. (2020) 073204, public 2020-07-07, doi:10.1088/1742-5468/ab97bc; freely accessible later author version arXiv:2306.16994v1, https://arxiv.org/html/2306.16994v1 (sections 1–4.1 and broken-bond counting inspected).
3. S. I. Denisov, P. Hänggi, *Domain statistics in a finite Ising chain*, Phys. Rev. E 71 (2005), 046137, doi:10.1103/PhysRevE.71.046137 (abstract only).
4. *Sharp universal Fourier sampling stability on proper colourings of cycles*, published mathematical research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-universal-fourier-sampling-stability-on-proper-colourings--8dc8f90856db/RESULT.md (complete mathematical result and proof inspected).
5. *Exact Lucas-cube Fourier precision and parity-split sharp frame conditioning*, published mathematical research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-exact-lucas-cube-fourier-precision-and-parity-split-sharp-frame--159f7c631a3c/RESULT.md (complete mathematical result and proof inspected).
