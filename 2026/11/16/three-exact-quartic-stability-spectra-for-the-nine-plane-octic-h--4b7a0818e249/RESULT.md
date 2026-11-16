# Three exact quartic stability spectra for the nine-plane octic harmonic fusion frame

## Finding
Let \(F=\mathbb F_3[u]/(u^2+1)\), write \(g=1+u\), and let \(\chi_e:F^\times\to\mathbb C\) be defined by \(\chi_e(g)=e^{2\pi i e/8}\) for \(e\in\{1,3,5,7\}\). Let \(\psi(t)=e^{2\pi i\operatorname{Tr}_{F/\mathbb F_3}(t)/3}\). For every \(a\in F\), define two orthonormal columns in \(\mathbb C^{F^\times}\):
\[
\Phi_{a,e}(x,0)=\frac{\psi(ax)}{\sqrt8},\qquad
\Phi_{a,e}(x,1)=\frac{\chi_e(x)\psi(ax)}{\sqrt8},\quad x\in F^\times.
\]
For each four-element \(S\subset F\), let \(G_{S,e}=\Phi_{S,e}^{*}\Phi_{S,e}\) be the \(8\times8\) Gram matrix of the concatenated eight columns, ordered with the two columns of each plane adjacent. Define
\[
\begin{aligned}
Q_{72}(t)&=t^4-32t^3+324t^2-1134t+972,\\
Q_{18}(t)&=t^4-32t^3+324t^2-1080t+972,\\
Q_{36}(t)&=t^4-32t^3+324t^2-1080t+486.
\end{aligned}
\]
For **all four odd multiplicative characters**, the characteristic polynomial of \(8G_{S,e}\) is exactly one of \(Q_{72}(t)^2,Q_{18}(t)^2,Q_{36}(t)^2\), occurring respectively for \(72,18,36\) unordered four-point sets \(S\). The sets with each polynomial are exactly one affine \(F\rtimes F^\times\) orbit, represented respectively by
\[
\begin{split}
S_{72}&=\{0,u,-u,1\},\\
S_{18}&=\{0,u,1,1+u\},\\
S_{36}&=\{0,u,1,1-u\}.
\end{split}
\]
Thus all four selected planes span \(\mathbb C^8\), and the sharp *worst-case four-plane lower frame bound* is \(\alpha_4=\rho/8\), where \(\rho\in(0.52,0.54)\) is the smallest root of \(Q_{36}\):
\[
\alpha_4=0.0662379483456\ldots.
\]
Equality holds for precisely the \(36\) affine images of \(S_{36}\). The sharp upper frame bound is \(\beta_4=\sigma/8=1.9694184303\ldots\), where \(\sigma\in(15.75,15.76)\) is the largest root of \(Q_{72}\), attained precisely on the \(72\) affine images of \(S_{72}\). Consequently any five of the nine entire two-dimensional planes may be erased while retaining unique reconstruction, and fewer than four surviving planes cannot span the eight-dimensional space.

## Assumptions and scope
\(F\) has nine elements and \(F^\times\) has eight; the character exponents \(1,3,5,7\) are exactly the odd characters. Each \(\Phi_{a,e}\) has orthonormal columns since \(\sum_{x\in F^\times}\chi_e(x)=0\). The full nine-plane family is the harmonic \(\operatorname{EITFF}(8,9,2)\) construction of Fickus, Iverson, Jasper, and Mixon, Theorem 4.1. No finding here asserts a new construction or newly discovers its four-block full rank: this was established in the earlier finite-field block-rank classification cited below. The result here is the **three exact Gram spectral polynomials, the complete orbit incidence, and the sharp extremal frame bounds** for all odd characters.

## Proof
**Affine reduction.** Translating labels \(a\mapsto a+b\) multiplies each row of all concatenated columns by \(\psi(bx)\), leaving Gram eigenvalues unchanged. Dilating labels by \(c\in F^\times\) permutes the eight rows by \(x\mapsto c^{-1}x\), up to unit-modulus scalar changes in the second column of every block. Hence the spectrum depends only on the affine orbit of the four-set. An exhaustive orbit construction on \(\binom94=126\) four-sets shows precisely the three disjoint orbits represented above, of sizes \(72,18,36\). This is a finite exact orbit calculation, with all field operations and orbit coverage implemented by the standalone checker.

**Even spectral multiplicities.** Because \(\chi_e(-1)=-1\), the antilinear operator \((Jv)(x)=\chi_e(x)\overline{v(-x)}\) on \(\mathbb C^{F^\times}\) satisfies \(J^2=-I\). It exchanges the two columns of each \(\Phi_{a,e}\) up to sign: \(J\Phi_{a,e}(:,0)=\Phi_{a,e}(:,1)\) and \(J\Phi_{a,e}(:,1)=-\Phi_{a,e}(:,0)\). Therefore the positive self-adjoint operator \(\Phi_{S,e}\Phi_{S,e}^*\) commutes with \(J\), so every eigenspace has even complex dimension (the vectors \(v,Jv\) are linearly independent). It follows that the eight-by-eight Gram characteristic polynomial is a perfect square.

**Exact characteristic polynomials.** Choose \(\xi=e^{2\pi i/24}\), so that \(\zeta_3=\xi^8\), \(\zeta_8=\xi^3\), and \(\Phi_{24}(X)=X^8-X^4+1\). Multiplying the normalized Gram by eight removes denominators; its entries are precisely
\[
H_{(a,r),(b,s)}=\sum_{x\in F^\times}\xi^{\,8\operatorname{Tr}(x(b-a))+3e(s-r)\log_g x},
\qquad r,s\in\{0,1\}.
\]
For each of the three orbit representatives and four values of \(e\), compute these entries in the exact integer quotient ring \(\mathbb Z[X]/(X^8-X^4+1)\). Newton's trace identities \(kc_k=-\sum_{j=1}^k c_{k-j}\operatorname{tr}(H^j)\), starting from \(c_0=1\), give all nine characteristic coefficients. The checker verifies, as identities of eight integer coordinates for each coefficient, that the characteristic polynomials are exactly the three stated squared quartics. This is an exhaustive, exact finite proof; no floating-point eigensolver or unjustified conversion of modular rank is involved.

**Sharp extrema.** Rational sign changes isolate the four positive roots of each quartic in the intervals listed in the verifier. The first-root intervals for \(Q_{36},Q_{72},Q_{18}\) are respectively \((0.52,0.54)\), \((1.25,1.26)\), and \((1.42,1.44)\), so the first is strictly smallest. The last-root intervals are respectively \((15.30,15.32)\), \((15.75,15.76)\), and \((14.19,14.20)\), so the \(Q_{72}\) root is strictly largest. Each quartic has four disjoint rational sign-change intervals; being degree four, each interval contains precisely one root and all roots are positive. This establishes positivity, sharp lower/upper constants, and complete equality-orbit descriptions. Any three two-planes span at most dimension six, while every four span dimension eight.

## Verification
Run `python3 verify_f9.py` with the Python 3 standard library. It checks all \(126\) four-set partitions under the affine group, and for each of four odd characters and three orbit representatives checks the complete squared characteristic polynomial by exact cyclotomic arithmetic. It additionally verifies the required rational root-isolation sign changes, positivity, and separation of extreme roots. The output ends in a `PASS` line. The finite enumeration is exhaustive by the transitive affine-orbit proof; it is not a sample of matrices. The printed decimal approximations are illustrative only; the exact claims are the quartics and rational isolations.

## Relationship to prior work
Fickus, Iverson, Jasper, and Mixon (first public 2021) establish the harmonic EITFF construction used here. The earlier *square-orbit block-rank dichotomy for order-nine harmonic fusion frames* establishes full block-spark for its eight-dimensional family and explicitly does **not** claim smallest-positive-singular-value bounds; that result subsumes the present rank-only consequence but not the quartic spectral census or exact sharp frame constants. A real quadratic-character fusion-plane theorem treats a different, real construction (with a universal triple spectrum and a four-plane census for field order thirteen). It does not imply the order-nine primitive-octic spectral polynomials. General erasure-robust frame theory develops stability metrics, rather than these exact finite-field eigenvalue classifications. More recent totally symmetric EITFF constructions have equivalent spectra for every fixed-size index subset, in contrast with the three distinct orbits here.

## Limitations
The three exact spectra concern the specific normalized harmonic construction over \(\mathbb F_9\) with odd multiplicative characters, not arbitrary equi-isoclinic fusion frames or all field orders. The enumeration and characteristic identities are finite exact computations supported by the supplied complete checker. Stability under additive perturbations is controlled through the stated frame bounds; no stochastic noise model, nonlinear decoding theorem, or infinite-family claim is established. The historical-priority comparison is made against identifiable sources and does not rule out obscure equivalent calculations. Independent verification is not yet performed.

## References
1. M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267v1, December 28, 2021, Theorem 4.1: https://arxiv.org/abs/2112.14267.
2. *The square-orbit block-rank dichotomy for order-nine harmonic fusion frames*, public exact-result record (2026), particularly the Finding, Scope, Proof, and Limitations: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-square-orbit-block-rank-dichotomy-for-order-nine-harmonic-fu--601f40ffaaeb.
3. *Three-block rigidity and the four-block spectral profile of real Paley harmonic fusion planes*, public exact-result record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-block-rigidity-and-the-four-block-spectral-profile-of-real--e1ffd8f9e8e9.
4. M. Fickus, J. Jasper, D. G. Mixon, J. Peterson, *Group-theoretic constructions of erasure-robust frames*, arXiv:1210.0139 (2012): https://arxiv.org/abs/1210.0139.
5. M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Totally symmetric Grassmannian codes*, arXiv:2406.19542v2 (2026), first public 2024: https://arxiv.org/abs/2406.19542.
