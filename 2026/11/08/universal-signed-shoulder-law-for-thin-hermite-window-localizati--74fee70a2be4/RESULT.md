# Universal signed shoulder law for thin Hermite-window localization annuli

## Finding
For each fixed nonnegative Hermite order \(k\), write \(h_k\) for the unit-norm Hermite function and set \(T_{s,L}^{(k)}=V_{h_k}^{*}\mathbf 1_{E_{s,L}}V_{h_k}\), where \(L>0\) is fixed, \(E_{s,L}=\{(y,\xi):s\leq\pi(y^2+\xi^2)\leq s+L\}\), and \(R=s+L/2\to\infty\). Let \(H_k(x)=\operatorname{He}_k(-x)\), where \(\operatorname{He}_k\) is the probabilists' Hermite polynomial, and put
\[
G_k(x)=\frac{e^{-x^2/2}H_k(x)^2}{k!}.
\]
At any nonzero \(a>0\) such that \(\pm a\) are isolated, nondegenerate local maxima of \(G_k\) and \(G_k(a)>0\), choose sufficiently small fixed disjoint neighborhoods of \(\pm a\), and let \(M_{k,-}\) and \(M_{k,+}\) be the maxima of the Hermite eigenvalues over indices with \((n-R)/\sqrt R\) in those neighborhoods. Then
\[
M_{k,\pm}=\frac{L G_k(a)}{\sqrt{2\pi R}}\left(1\mp\frac{a}{6\sqrt R}+O_{k,L,a}(R^{-1})\right),
\qquad M_{k,-}-M_{k,+}=\frac{L aG_k(a)}{3\sqrt{2\pi}\,R}+O_{k,L,a}(R^{-3/2}).
\]
Each local maximizing index is \(n=R\pm a\sqrt R+O_{k,L,a}(1)\). The coefficient \(-a/6\) is **independent of Hermite order**: it arises from an exact cancellation in the first Poisson–Charlier correction at any nonzero critical point of the leading envelope.

For the **second Hermite window** \(k=2\), the two outer maxima at \(a=\sqrt5\) are the only global maxima of the leading envelope and exceed its central peak. Every globally maximizing Hermite index therefore satisfies \(n=R-\sqrt{5R}+O_L(1)\), and the operator norm and two outer shoulder gap satisfy
\[
\|T_{s,L}^{(2)}\|=\frac{8Le^{-5/2}}{\sqrt{2\pi R}}\left(1+\frac{\sqrt5}{6\sqrt R}+O_L(R^{-1})\right),
\quad
M_{2,-}-M_{2,+}=\frac{8L\sqrt5e^{-5/2}}{3\sqrt{2\pi}\,R}+O_L(R^{-3/2})>0.
\]
The higher-index outer peak remains a distinct inferior local maximum for sufficiently large \(s\).

## Assumptions and scope
The short-time Fourier transform uses \(V_gf(y,\xi)=\int_{\mathbb R} f(t)\overline{g(t-y)}e^{-2\pi i\xi t}\,dt\), with \(\|h_j\|_2=1\), and symplectic phase-space area \(\pi(y^2+\xi^2)\). All constants in the error terms may depend on the **fixed** Hermite order, fixed positive annulus area, selected shoulder, and fixed isolation neighborhoods; the estimates are not uniform in increasing \(k\) or \(L\). The universal statement compares paired nondegenerate local shoulders; it does not assert that every such shoulder is globally optimal. The global claim is given only for the second-Hermite window.

## Proof
**Exact spectrum.** By the radial symmetry of the mask and the Hermite–Laguerre STFT formula, the Hermite basis diagonalizes \(T_{s,L}^{(k)}\). For \(n\geq0\) define the degree-\(k\) Poisson–Charlier polynomial
\[
C_k(n;u)=k![v^k]e^{uv}(1-v)^n
=\sum_{j=0}^{\min(k,n)}(-1)^j\binom{k}{j}(n)_j u^{k-j},
\]
where \((n)_j=n!/(n-j)!\) and \([v^k]\) denotes coefficient extraction. The **exact eigenvalues**, valid also when \(n<k\), are
\[
\lambda_{n,k}(R,L)=\int_{R-L/2}^{R+L/2}e^{-u}\frac{u^n}{n!}\frac{C_k(n;u)^2}{k!u^k}\,du.
\tag{1}
\]
For \(n\geq k\), \(C_k(n;u)=(-1)^k k!L_k^{(n-k)}(u)\), giving the standard Laguerre expression. The other case follows from the symmetric associated-Laguerre identity; in particular (1) has no singularity on our annuli for large \(s\).

**Uniform two-term expansion.** Fix any compact interval of real \(x\), treat \(n=R+x\sqrt R\) as an integer parameter, and put \(\epsilon=R^{-1/2}\). Uniform Stirling expansion yields
\[
e^{-R}\frac{R^n}{n!}=\frac{e^{-x^2/2}}{\sqrt{2\pi R}}\left[1+\epsilon\left(\frac{x^3}{6}-\frac{x}{2}\right)+O(R^{-1})\right].
\tag{2}
\]
The polynomial generating function at \(v/\sqrt R\) gives
\[
 e^{\sqrt R v}(1-v/\sqrt R)^n
=e^{-xv-v^2/2}\left[1+\epsilon\left(-\frac{xv^2}{2}-\frac{v^3}{3}\right)+O(R^{-1})\right].
\tag{3}
\]
Coefficient extraction at fixed \(k\), with \(H=H_k(x)\), yields
\[
R^{-k/2}C_k(n;R)=H+\epsilon D+O(R^{-1}),\qquad D=-\frac{x}{2}H''+\frac13H'''.
\tag{4}
\]
Combining (1)–(4), write \(F_0=H^2/k!\) and
\[
F_1=\left(\frac{x^3}{6}-\frac x2\right)F_0+\frac{2HD}{k!}.
\]
For \(u=R+t\), fixed \(|t|\le L/2\), the corresponding expansion has additional terms linear in \(t\) at order \(\epsilon\). They integrate to zero over the symmetric annulus. Smoothness and fixed-degree coefficient extraction make the error and its first two derivatives in \(x\) uniform on compact sets. Thus
\[
\lambda_{n,k}(R,L)=\frac{Le^{-x^2/2}}{\sqrt{2\pi R}}\left(F_0(x)+\epsilon F_1(x)+O(R^{-1})\right).
\tag{5}
\]

**Universal cancellation.** The Hermite polynomial identity \(H''-xH'+kH=0\) and its derivative imply the exact polynomial factorization
\[
F_1(x)=-\frac{x}{6}F_0(x)
-\frac{(x^2+2k-2)H(x)\,[2H'(x)-xH(x)]}{6k!}.
\tag{6}
\]
At a positive-height stationary point of \(G_k=e^{-x^2/2}F_0\), differentiation forces \(2H'(x)=xH(x)\), and (6) becomes \(F_1(x)=-xF_0(x)/6\). The odd correction changes sign between \(a\) and \(-a\), as \(G_k\) is even. Each nondegenerate critical point persists as an isolated maximizer under the smooth \(O(\epsilon)\) perturbation of (5), shifted in \(x\) by \(O(\epsilon)\). Rounding to the nearest permitted lattice index changes the **normalized** maximum by only \(O(\epsilon^2)\), because the leading peak has vanishing first derivative and strictly negative second derivative. This proves both paired-shoulder formulas and the \(O(1)\) index localization.

**Global maximum for \(k=2\).** Here \(H_2(x)=x^2-1\), and \(G_2(x)=\frac12e^{-x^2/2}(x^2-1)^2\). Its only positive-height local maxima are \(0\) and \(\pm\sqrt5\), with heights respectively \(1/2\) and \(8e^{-5/2}>1/2\). Uniform Poisson large-deviation bounds from (1), using that the fixed-degree Charlier factor grows at most polynomially in \(1+|n-u|/\sqrt u\), show that eigenvalues with \(|n-R|>B\sqrt R\) have arbitrarily small normalized size for sufficiently large fixed \(B\). More precisely, within \(n\in[R/2,2R]\) the exponential factor is \(O(R^{-1/2}e^{-c(n-R)^2/R})\) and the Charlier factor is \(O((1+|n-R|/\sqrt R)^4)\); outside this range exponential tails dominate all polynomial factors. Therefore no remote index competes with the outer peaks, and no central index competes because of the strict envelope-height gap. Applying the paired-shoulder comparison at \(a=\sqrt5\) establishes the stated global norm and index claim.

## Verification
The standalone \`checker.py\` is part of this package. With Python, SymPy, and mpmath installed, run \`python checker.py\`. It verifies identity (6) symbolically for the first thirteen Hermite orders, compares the exact Charlier and associated-Laguerre formulas in 81 small-index cases, checks the second-Hermite two-shoulder asymptotics at four increasing radii, and checks four integrals against an independent high-precision Laguerre expression. Expected terminal marker: \`UNIVERSAL_HERMITE_ANNULUS_PASS\`. These finite tests are corroboration only; the infinite-order asymptotics and global conclusion follow from the proof.

## Relationship to prior work
The established Hermite–Laguerre formula and radial diagonalization occur in Abreu–Gröchenig–Romero (arXiv:1704.03042; 2017 public preprint). Keller–Luef (arXiv:1905.07741) treat polyanalytic Toeplitz symbolic calculus; Knutsen (arXiv:1907.00848) treats radial Gaussian-window localization; Nilsson (2021) proves a locally uniform leading Charlier-to-Hermite transition with a sharp \(O(R^{-1/2})\) bound, without identifying the present coefficient or selecting annular spectral shoulders. General polynomial asymptotic techniques alone are not claimed original. The new point is the exact critical-point cancellation (6), its **all-fixed-orders** consequence and the global second-Hermite shoulder selection. A previously established first-Hermite thin-annulus calculation gives the \(k=1\) special case, hence is not independently new here.

## Limitations
The main result is a large-radius, fixed-width asymptotic; it supplies no explicit finite onset radius and no uniqueness assertion for a maximizing **integer** index. Other fixed Hermite orders can have several peaks of unequal height; only paired positive-height nondegenerate maxima are compared. The proof does not cover simultaneously growing order and radius, rapidly changing annulus width, nonsymmetric masks, or non-Hermite windows. Equivalence to an earlier specialist higher-order Charlier/Laguerre extremum analysis remains a bibliographic risk, notwithstanding the specific full-text comparisons.

## References
1. L. D. Abreu, K. Gröchenig and J. L. Romero, *Harmonic analysis in phase space and finite Weyl–Heisenberg ensembles*, arXiv:1704.03042, first posted 2017-04-10; Journal of Statistical Physics 174 (2019), 1104–1136. https://arxiv.org/abs/1704.03042
2. J. Keller and F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741, 2019. https://arxiv.org/abs/1905.07741
3. H. Knutsen, *Daubechies' time–frequency localization operator on Cantor type sets I*, arXiv:1907.00848, 2019; Journal of Fourier Analysis and Applications 26 (2020). https://arxiv.org/abs/1907.00848
4. M. N. P. Nilsson, *On the transition of Charlier polynomials to the Hermite function*, Constructive Approximation 56 (2022), 479–504; online 2021-10-23. https://doi.org/10.1007/s00365-021-09559-w
