# Exact Gabor lifting ranks and fourth ambiguity moments of quartic prime-field chirps

## Finding
For every prime \(p\ge5\), put \(\zeta_p=e^{2\pi i/p}\) and let the unit window on \(\mathbb F_p\) be
\[
g_p(x)=p^{-1/2}\zeta_p^{x^4}.
\]
Define translations and modulations by \(T_a h(x)=h(x+a)\), \(M_bh(x)=\zeta_p^{bx}h(x)\), and the normalized self-ambiguity function
\[
A_p(a,b)=\langle g_p,M_bT_a g_p\rangle
=p^{-1}\sum_{x\in\mathbb F_p}\zeta_p^{(x+a)^4-x^4+bx}.
\]
Then its *entire zero set* is
\[
\{(0,b):b\ne0\}\ \cup\
\begin{cases}
\varnothing,&p\equiv1\pmod3,\\
\{(a,-a^3):a\ne0\},&p\equiv2\pmod3.
\end{cases}
\]
For the complex-linear full Gabor intensity lifting operator
\[
\mathcal Q_{g_p}(X)(u,v)=\operatorname{tr}\!\left(X\,P_{u,v}\right),\quad
P_{u,v}=(M_vT_ug_p)(M_vT_ug_p)^*,\quad X\in\mathbb C^{p\times p},
\]
its rank over \(\mathbb C\) is exactly
\[
\operatorname{rank}\mathcal Q_{g_p}=\begin{cases}
p^2-p+1,&p\equiv1\pmod3,\\
p^2-2p+2,&p\equiv2\pmod3.
\end{cases}
\]
The exact *normalized fourth ambiguity moment* is
\[
\sum_{a,b\in\mathbb F_p}|A_p(a,b)|^4
=3-\frac3p+\frac1{p^2}.
\]
Among all unit windows of constant pointwise modulus \(p^{-1/2}\), the fourth moment is at least \(2-p^{-1}\), with equality for the cubic chirp \(p^{-1/2}\zeta_p^{x^3}\). The quartic window therefore has the **exact moment excess** \((1-p^{-1})^2\). The first rank branch attains the maximum lifted rank permitted for any constant-modulus unit window; the second branch has an additional \(p-1\) invisible Weyl directions.

## Assumptions and scope
All indices, polynomial powers and congruences are taken in the prime field \(\mathbb F_p\); \(p\) ranges over **all primes at least five**, not arbitrary prime powers. The Hilbert inner product is \(\langle f,h\rangle=\sum_x\overline{f(x)}h(x)\). The complex rank concerns the linear map \(X\mapsto\mathcal Q_{g_p}(X)\) on **all** complex matrices, not nonlinear injectivity on rank-one positive matrices. Nonvanishing on all Weyl directions is not asserted.

## Proof
**1. Exact cyclotomic criterion.** If \(P:\mathbb F_p\to\mathbb F_p\), then \(\sum_{x}\zeta_p^{P(x)}=0\) if and only if \(P\) is a permutation polynomial on \(\mathbb F_p\). Indeed, if \(n_j=|P^{-1}(j)|\), the polynomial \(\sum_{j=0}^{p-1}n_jz^j\) vanishes at the primitive \(p\)-th root \(\zeta_p\). Its degree is at most \(p-1\), so it is a rational multiple of \(\Phi_p(z)=1+\cdots+z^{p-1}\). As its coefficients are nonnegative integers summing to \(p\), every \(n_j=1\). The converse is immediate.

**2. Cubic permutation lemma.** For \(p\ge5\), the polynomial \(y^3+cy\) permutes \(\mathbb F_p\) if and only if \(c=0\) and \(p\equiv2\pmod3\). The case \(c=0\) follows from cyclicity of \(\mathbb F_p^*\). If \(c\ne0\), the collision equation for distinct \(x,y\) is \(x^2+xy+y^2=-c\). Let \(\chi\) be the quadratic character with \(\chi(0)=0\). Completing the square, and using \(\sum_y\chi(y^2+t)=-1\) for nonzero \(t\), gives exactly \(p-\chi(-3)\) ordered solutions to this equation. At most two have \(x=y\). Since \(p-\chi(-3)-2\ge p-3>0\), a non-diagonal collision exists. For completeness, the displayed character sum identity follows by counting the \(p-1\) factor pairs \((u,v)\) with \(uv=t\) and changing variables \(u=z-y,v=z+y\).

**3. Complete ambiguity-zero classification.** For \(a=0\), \(A_p(0,b)=\mathbf1_{\{b=0\}}\). For \(a\ne0\), substitute \(y=x+a/2\) in the exponent to obtain
\[
(x+a)^4-x^4+bx=4ay^3+(a^3+b)y-ab/2.
\]
Multiplying by \((4a)^{-1}\), removing the constant phase, and applying Steps 1–2 proves that this sum vanishes exactly when \(b=-a^3\) and \(p\equiv2\pmod3\). Thus there are \(p-1\) zeros in the first congruence class and \(2(p-1)\) in the second.

**4. Rank of the complete intensity lifting.** The normalized Weyl operators \(p^{-1/2}M_bT_a\), indexed by \((a,b)\in\mathbb F_p^2\), are an orthonormal Hilbert–Schmidt basis for all complex matrices. Conjugation by any time-frequency shift multiplies each Weyl coefficient by a corresponding character on \(\mathbb F_p^2\). Taking the unitary two-dimensional Fourier transform of the output of \(\mathcal Q_{g_p}\) therefore diagonalizes the operator: its multiplier at \((a,b)\) is \(\sqrt p\) times a unit phase times \(\overline{A_p(a,b)}\). Consequently its rank is exactly the number of nonzero ambiguity coefficients. Insert the zero counts from Step 3 to obtain the displayed rank formula. Independently, for any constant-modulus unit window \(h\), \(A_h(0,b)=0\) for every \(b\ne0\), so its lifted rank is at most \(p^2-p+1\).

**5. Fourth moment.** Put \(P_a(x)=(x+a)^4-x^4\), \(F_a(b)=\sum_x\zeta_p^{P_a(x)+bx}\), so \(A_p=p^{-1}F_a\). The finite Fourier autocorrelation identity yields
\[
\sum_b|F_a(b)|^4=p\sum_{h\in\mathbb F_p}
\left|\sum_x\zeta_p^{P_a(x+h)-P_a(x)}\right|^2.
\]
If \(a\ne0\), at \(h=0\) the inner sum is \(p\); for every \(h\ne0\) its phase is a quadratic polynomial with nonzero leading coefficient \(12ah\). The elementary quadratic Gauss-sum calculation gives squared magnitude exactly \(p\). Hence the sum on the left is \(p[p^2+(p-1)p]=2p^3-p^2\). The \(a=0\) ambiguity row contributes exactly \(1\) to the normalized fourth moment. Summing the remaining \(p-1\) rows and dividing by \(p^4\) proves \(3-3/p+1/p^2\).

**6. Sharp constant-modulus comparison.** For any unit constant-modulus window \(h\), Parseval gives \(\sum_b|A_h(a,b)|^2=1\) for every \(a\), and \(A_h(0,b)=\mathbf1_{\{b=0\}}\). Cauchy–Schwarz gives \(\sum_b|A_h(a,b)|^4\ge p^{-1}\) for each \(a\ne0\); hence the universal bound \(2-p^{-1}\). For \(h(x)=p^{-1/2}\zeta_p^{x^3}\), the phase difference at every \(a\ne0\) is nondegenerate quadratic, so its entire nonzero-translation ambiguity row has constant magnitude \(p^{-1/2}\), attaining the bound. Subtraction yields the claimed exact quartic excess.

## Verification
Run `python3 CHECK.py` with the Python standard library. For every prime in the explicitly listed thirteen-element set from \(5\) through \(47\), the script checks each ambiguity-zero decision using exact integer cyclotomic histograms. It independently checks every nonzero translation and shift quadratic Gauss-magnitude identity by reducing an exact integer autocorrelation polynomial modulo the prime cyclotomic polynomial; it verifies the integer numerator of the fourth moment and all rank counts. The successful execution prints `ALL_EXACT_QUARTIC_CHECKS_PASSED`. Finite tests corroborate, but do not replace, Steps 1–6.

## Relationship to prior work
Li's September 9, 2026 preprint, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations* (arXiv:2609.09614), proves general ambiguity-diagonalized lifting stability and uses the cubic Alltop chirp as a seed. Its Section 3.2 provides the Weyl-diagonalization ingredient used in Step 4; its full available text does not state the quartic ambiguity-zero congruence classification, rank dichotomy, or exact fourth moment. Bojarovska–Flinth (arXiv:1503.05800) establishes finite Gabor phase-retrieval criteria, not the specified quartic lifting rank or its fourth moment. Price–Hall–Bartlett (DOI:10.1007/s10801-022-01187-2) studies Alltop monomials and the difference-polynomial framework; it does not assert this rank-and-moment profile. The prime-field cubic permutation criterion and quadratic Gauss sums are classical ingredients. The isolated smallest-prime instance is also encompassed by general results on one-coordinate Gabor windows; no novelty is claimed for that special case alone. The claim is the joint all-prime quartic profile and sharp comparison.

## Limitations
The theorem is restricted to prime moduli at least five, full Gabor intensity lifting, and the one prescribed quartic phase window. It does not establish nonlinear phase retrieval failure for arbitrary signals from a deficient lifting rank, nor does it give the complete singular-value spectrum or a universal result for all quartic polynomials. Publication originality is assessed only relative to accessible primary literature and mathematical database records; an equivalent formula could appear under radar ambiguity, polyphase sequence or permutation-polynomial terminology. Independent external mathematical validation has not been performed.

## References
1. Dongwei Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614, first public September 9, 2026. https://arxiv.org/abs/2609.09614
2. Irena Bojarovska and Axel Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first public March 19, 2015. https://arxiv.org/abs/1503.05800
3. Aiden Price, Joanne Hall and Harry Bartlett, *Refining the search space of Alltop monomials*, *Journal of Algebraic Combinatorics* 57 (2023), 709–725, first published November 7, 2022, DOI:10.1007/s10801-022-01187-2. https://link.springer.com/article/10.1007/s10801-022-01187-2
