# An exact residue-phase law for marker bias in finite-type covers of periodic gap shifts

## Finding
Let \(D\subset\mathbb N\) be an eventually periodic set of allowed return distances between successive symbols \(1\) in a binary gap shift. Suppose its eventual membership pattern has at least one allowed and one forbidden distance. For each \(n\ge1\), let \(X_D^{(n)}\) be the canonical length-\(n\) finite-type cover of the bilateral shift \(X_D\). Let \(\nu_n\) and \(\nu\) be their measures of maximal entropy, and set \(\rho_n=\nu_n([1])\), \(\rho=\nu([1])\). For all sufficiently large \(n\), the cover marker density approaches the limit **from below**, with an explicit polynomial-times-exponential leading term whose coefficient depends on the residue of \(n\).

Write \(a_d=\mathbf1_{\{d\in D\}}\), and choose \(N_0\) and \(m\ge2\) such that \(a_{d+m}=a_d\) for every \(d\ge N_0\). Let \(q\in(1/2,1)\) be the unique solution of
\[
\sum_{d\in D}q^d=1,
\qquad M=\sum_{d\in D}d q^d.
\]
For each residue class \(r\in\mathbb Z/m\mathbb Z\), define
\[
H_r(z)=\frac{\sum_{j=0}^{m-1}(1-a_{n+j})z^j}{1-z^m}
\quad\text{for any }n\ge N_0\text{ with }n\equiv r\pmod m.
\]
This definition does not depend on the chosen \(n\); every \(H_r(q)\) is strictly positive. Then, uniformly over all residues as \(n\to\infty\),
\[
\boxed{\displaystyle
\rho-\rho_n=\frac{nq^nH_{n\bmod m}(q)}{M^2}+O_D(q^n).}
\]
The accompanying entropy excess is
\[
\boxed{\displaystyle
h_{\mathrm{top}}(X_D^{(n)})-h_{\mathrm{top}}(X_D)
=\frac{q^nH_{n\bmod m}(q)}{M}+O_D(nq^{2n}).}
\]
Therefore
\[
\lim_{n\to\infty}\frac{\rho-\rho_n}{n\left(h_{\mathrm{top}}(X_D^{(n)})-h_{\mathrm{top}}(X_D)\right)}=\frac1M=\rho,
\]
and the complete accumulation set of \((\rho-\rho_n)/(nq^n)\) is exactly the finite set
\[
\left\{H_r(q)/M^2:0\le r<m\right\}
\]
(with duplicate values counted only once).

For the classical **even shift**, where \(D=\{1,3,5,\ldots\}\), put \(\varphi=(1+\sqrt5)/2\). Here \(q=\varphi^{-1}\), \(M=\sqrt5\), and
\[
\rho-\rho_n\sim \begin{cases}
(\varphi/5)n\varphi^{-n},&n\text{ even},\\
(1/5)n\varphi^{-n},&n\text{ odd}.
\end{cases}
\]
Thus the equilibrium one-cylinder marginal converges by an extra factor of \(n\) more slowly than the corresponding entropy excess, with two genuinely different parity constants.

## Assumptions and scope
All systems are two-sided binary shifts under left translation. A return distance \(d\) is the distance from one occurrence of \(1\) to the next, including the terminal \(1\), so the intervening zero-run length is \(d-1\). The shift \(X_D\) is the closure of bi-infinite concatenations of allowed return blocks \(10^{d-1}\), including zero-tail configurations in the closure. Its canonical length-\(n\) cover consists of all configurations whose every contiguous length-\(n\) block belongs to the language of \(X_D\). Its entropy is measured in natural logarithms. We assume the eventually periodic tail of \(a_d\) contains both digits, so both allowed and forbidden distances occur infinitely often. The eventual period \(m\) need not be minimal; distinct residue coefficients may coincide. The constants in \(O_D\) depend on the fixed set \(D\) only.

The primary motivating problem is to make the qualitative convergence of finite-type covers and their maximal-entropy measures quantitative at the level of a natural cylinder observable. The theorem is not a statement about arbitrary nonperiodic gap sets or arbitrary observables.

## Proof
**1. Canonical covers are exact renewal systems.** A finite binary word belongs to the language of \(X_D\) exactly when every distance between successive \(1\)'s within the word lies in \(D\). Necessity is immediate. For sufficiency, extend each finite list of admissible distances using a fixed allowed distance in both directions; isolated leading or trailing zeros do not obstruct extension. Hence the minimal forbidden words are precisely \(10^{d-1}1\) for \(d\notin D\), each of length \(d+1\). The length-\(n\) cover consequently allows exactly the distances
\[
D_n=(D\cap\{1,\ldots,n-1\})\cup\{n,n+1,\ldots\}.
\]
This includes all possible zero-tail limit configurations, and gives equality of the two subshifts, not merely of their entropies. For \(n\) beyond the periodicity threshold, \(D_n\) is cofinite and its shift is a finite-type mixing renewal system, since all sufficiently large return distances occur.

**2. Entropy and the unique maximal-entropy renewal measure.** Let \(E\subset\mathbb N\) be either \(D\) or \(D_n\). The renewal partition function \(F_E(z)=\sum_{d\in E}z^d\) rises strictly from zero to infinity as \(z\uparrow1\). Its unique solution \(q_E\in(0,1)\) to \(F_E(q_E)=1\) yields the entropy \(-\log q_E\), by the first-return word generating function (equivalently, the positive spectral radius of the standard return-state presentation). Here \(q_D=q\), and \(q_{D_n}=q_n\). Since \(D\) is an infinite proper subset of positive integers, \(q\in(1/2,1)\).

There is a unique invariant measure of maximal entropy for both systems. One direct argument uses the first-return transformation induced on the cylinder \([1]\): a positive-marker-frequency ergodic invariant measure induces a stationary gap process with mean return length \(L\), marker frequency \(L^{-1}\) by Kac's formula, and entropy at most \(L^{-1}H(p)\) by Abramov's formula and the one-symbol entropy bound, where \(p\) is its single-gap distribution. The relative-entropy inequality for \(p\) versus \(p_E(d)=q_E^d\) gives \(H(p)\le-L\log q_E\), with equality exactly for the independent and identically distributed gap process having law \(q_E^d\). The only zero-marker invariant measure is the all-zero atom, with zero entropy; both systems have positive entropy. Thus the maximal-entropy process is the stationary renewal measure whose Palm return gaps are independent with distribution \(q_E^d\); its marker frequency is
\[
\nu_E([1])=\left(\sum_{d\in E}d q_E^d\right)^{-1}.
\]
This argument does not require the allowed distances to have greatest common divisor one.

**3. Exact periodic-tail perturbation.** With \(r=n\bmod m\), the periodic complement of the allowed distances gives the identity
\[
F_n(z):=\sum_{d\in D_n}z^d
=F(z)+z^nH_r(z),\qquad n\ge N_0.
\]
In particular \(H_r(q)>0\), uniformly over finitely many residues, and \(F_n(q)>1\). Hence \(q_n<q\). Put \(u=-\log q\), \(u_n=-\log q_n\). The derivative of \(F(e^{-u})\) at \(u\) is \(-M\ne0\). Both \(F\) and the finitely many rational functions \(H_r\) have uniformly bounded derivatives near \(q\). The implicit-root estimate first gives \(u_n-u=O_D(q^n)\), and Taylor expansion with the derivative of \(q^nH_r(q)\) gives
\[
u_n-u=\frac{q^nH_r(q)}M+O_D(nq^{2n}).
\]
This is the entropy excess formula.

**4. The marker bias and normalization.** Write \(M_n=q_nF'_n(q_n)\). Differentiating the exact perturbation identity yields
\[
qF'_n(q)=M+nq^nH_r(q)+q^{n+1}H'_r(q).
\]
The shift of the root by \(O_D(q^n)\) changes the right-hand side by \(O_D(q^n)\): indeed, the unperturbed second derivative is bounded and the derivative of the perturbation is \(O_D(n^2q^n)\), so its change over the root shift is \(O_D(n^2q^{2n})=O_D(q^n)\). It follows that
\[
M_n=M+nq^nH_r(q)+O_D(q^n).
\]
As \(\rho_n=M_n^{-1}\), the identity
\[
\frac1M-\frac1{M_n}=\frac{M_n-M}{MM_n}
\]
gives the stated \(nq^n\) expansion. Positivity of the leading coefficients ensures \(\rho_n<\rho\) for all sufficiently large \(n\). Dividing the marker formula by \(n\) times the entropy formula gives \(1/M\). Along \(n\equiv r\pmod m\) the normalized limit equals \(H_r(q)/M^2\); every residue occurs infinitely often, and no further limit is possible because the error tends uniformly to zero. This proves the cluster-set claim.

**5. Even-shift constants.** For odd return distances, \(F(q)=q/(1-q^2)=1\), so \(q=(\sqrt5-1)/2=1/\varphi\), and \(M=qF'(q)=\sqrt5\). Forbidden distances are even, giving \(H_0(z)=1/(1-z^2)\) for even \(n\), and \(H_1(z)=z/(1-z^2)\) for odd \(n\). At \(z=q\) these are respectively \(\varphi\) and \(1\), proving the two positive parity coefficients.

## Verification
The standalone `check.py` uses only the Python standard library. Execute `python check.py` from the directory containing this file and `RESULT.md`. It constructs the finite return-state presentations and checks exact short languages, compares the renewal Perron roots with the graph spectral radii, solves finite-cover and limiting renewal equations at 125 decimal-digit working precision, and compares the measured entropy and marker biases against the predicted residue coefficients on five eventually periodic gap sets. The checker finishes with `All finite-language, graph-spectral, asymptotic and parity checks passed.`. A sample output is included in `check_output.txt`.

The numerical tests are independent diagnostics on finitely many parameter choices and lengths. The proof above, not the experiments, establishes the result for all eventually periodic gap sets of the stated kind and all sufficiently large \(n\).

## Relationship to prior work
Coles, Cyr, Kra, and Pavlov [1] study stabilization of canonical finite-type covers in entropy and periodic-point terms; the qualitative framework does not imply an explicit maximal-entropy marker-frequency error with a polynomial prefactor. Chazottes, Ramirez, and Ugalde [2] prove exponential convergence of Gibbs measures for finite-type approximations of specified sofic shifts, including entropy convergence; neither their general exponential bound nor the mere convergence of equilibrium measures determines the present positive leading constants, eventual period-by-period phases, or the extra factor of \(n\). The entropy/renewal return-equation technique is standard and not claimed new [3,4]. García-Ramos and Pavlov [8, Theorem 3.19] moreover explicitly proved the general maximal-entropy marker-frequency identity \(\nu([1])=(\sum_{d\in D}d\exp(-d h_{\mathrm{top}}))^{-1}\). That identity is a prerequisite here, not a new claim. Their theorem is about an individual gap shift; it does not analyze the difference of marker frequencies across canonical finite-type covers, nor the uniform \(nq^n\)-order bias and its residue constants. Cheriyath [5] treats the opposite operation of excluding an additional word from an existing gap shift and bounds the entropy loss; it does not calculate canonical-cover maximal-entropy cylinder bias.

The published *A countable entropy-phase spectrum in finite-type covers of geometric gap shifts* [6] also analyzes canonical covers through renewal equations. It concerns the **entropy of nonperiodic, geometrically spaced gap sets**; its stated limitations exclude maximal-entropy measures and their convergence. The present claim instead quantifies **a cylinder of the equilibrium measures** in the eventually periodic, sofic setting, with a finite residue-phase set and an extra factor of \(n\). These are different hypotheses and different invariants, not simply a reparameterization. The published *Complete radius-one factors and entropy spectrum of the binary even shift* [7] addresses sliding-block factor images, not canonical covers or their equilibrium measures.

## Limitations
The claim concerns fixed eventually periodic return-distance sets having both allowed and forbidden distances in the periodic tail. It does not cover sparse nonsofic return sets or arbitrary finite-time perturbations. Only the maximal-entropy **one-cylinder marker frequency**, and its relationship to topological entropy, are quantified; no sharp convergence statement is asserted for all cylinder observables or arbitrary Gibbs potentials. The proof supplies an asymptotic result, not a numerical exact formula for every small cover length. Known general Gibbs measure convergence theorems are acknowledged, and an earlier specialized calculation of these constants in uncatalogued work cannot be excluded without further historical verification. Independent mathematical audit has not been performed.

## References
1. S. Coles, V. Cyr, B. Kra, R. Pavlov, *Stable covers of subshifts*, arXiv:2602.04097v1, first public 2026-02-04. https://arxiv.org/abs/2602.04097
2. J.-R. Chazottes, L. Ramirez, E. Ugalde, *Finite type approximations of Gibbs measures on sofic subshifts*, arXiv:math/0402144v1, first public 2004-02-09; subsequently *Nonlinearity* 18 (2005). https://arxiv.org/abs/math/0402144
3. D. Ahmadi Dastjerdi, S. Jangjoo, *Computations on Sofic S-gap Shifts*, arXiv:1108.3414. https://arxiv.org/abs/1108.3414
4. T. Dillon, *Dynamics and entropy of S-graph shifts*, arXiv:2010.06031. https://arxiv.org/abs/2010.06031
5. H. Cheriyath, *A note on the perturbations of subshifts*, arXiv:2506.20750v1, first public 2025-06-25. https://arxiv.org/abs/2506.20750
6. *A countable entropy-phase spectrum in finite-type covers of geometric gap shifts*, published research record 2026-10-18. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-countable-entropy-phase-spectrum-in-finite-type-covers-of-geom--1fd88ee11f52/RESULT.md
7. *Complete radius-one factors and entropy spectrum of the binary even shift*, published research record 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-complete-radius-one-factors-and-entropy-spectrum-of-the-binary-e--0234835f8973
8. F. García-Ramos, R. Pavlov, *Extender sets and measures of maximal entropy for subshifts*, Theorem 3.19, *J. London Math. Soc.* 100 (2019), 1013–1033; first public arXiv:1808.09486v1 (2018). https://arxiv.org/abs/1808.09486
