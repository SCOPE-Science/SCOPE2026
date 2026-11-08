# Uniform adversarial indicator doping of prime quadratic chirps for full Gabor tomography

## Finding
For any odd prime \(p\ge5\), any nonzero \(a\in\mathbb F_p\), and any nonempty subset \(U\subseteq\mathbb F_p\), let \(k=|U|\), \(\zeta=\exp(2\pi i/p)\), and
\[
g(x)=\zeta^{ax^2}+\mathbf 1_U(x), \qquad A_g(u,v)=\sum_{x\in\mathbb F_p}g(x+u)\overline{g(x)}\zeta^{-vx}.
\]
Set \(C_u=|U\cap(U-u)|\), and \(L_u=2k+C_u\). **Sufficient modular certificate:** If \(p\nmid L_u\) for every \(u\), then \(A_g(u,v)\ne0\) for all \((u,v)\in\mathbb F_p^2\). In particular **every** adversarial set \(U\) with \(3k<p\) satisfies this certificate. Thus its full finite Gabor intensity system determines arbitrary complex signals up to global phase, and the linear lifting from Hermitian matrices to intensities is injective.

Under \(3k<p\), the exact measurement lifting has smallest singular value bounded by
\[
\sigma_{\min}\ge \sqrt p(3k)^{-(p-2)},\qquad
\kappa_2\le(p+3k)(3k)^{p-2}.
\]
The bounds refer to the unnormalized window \(g\), the unnormalized rank-one measurement projectors, Hilbert--Schmidt input norm and Euclidean output norm. They are conservative, not asserted to be sharp.

The upper density condition cannot be omitted indiscriminately: for \(a=1\), there are exactly vanishing ambiguity values for \((p,U,u,v)=(5,\{2,3\},1,3)\), \((7,\{0,3,4\},1,0)\), and \((11,\{4,5,6,7\},1,7)\). These examples do not prove asymptotic optimality of the one-third density.

## Assumptions and scope
All operations on indices and exponents are in the prime field \(\mathbb F_p\). The impulse amplitude is exactly the positive real number one and is applied at an arbitrary set of locations, with no spacing, regularity or randomness assumption. The unnormalized Gabor shifts are \((\pi(u,v)g)(x)=\zeta^{vx}g(x-u)\); changing this shift convention changes only harmless phases and permutations in the ambiguity values. The measured data are \(|\langle f,\pi(u,v)g\rangle|^2\), for all \((u,v)\in\mathbb F_p^2\). Injective lifting implies recovery of any vector up to its unavoidable global phase, but does not assert recovery from a proper measurement subset.

## Proof
**Exact cross-term identity.** Expand the ambiguity of \(g=c+\mathbf 1_U\), where \(c(x)=\zeta^{ax^2}\):
\[
\begin{aligned}
A_g(u,v)={}&p\zeta^{au^2}\mathbf 1_{\{v=2au\}}\\
&+\sum_{x\in U}\zeta^{a(x+u)^2-vx}
+\sum_{y\in U}\zeta^{-a(y-u)^2-v(y-u)}
+\sum_{\substack{x\in U\\x+u\in U}}\zeta^{-vx}.
\end{aligned}
\]
The first term follows by summing the character \(x\mapsto\zeta^{(2au-v)x}\). The remaining terms are precisely \(L_u=2k+C_u\) unit positive-coefficient \(p\)-th roots of unity, counted with multiplicities.

**Cyclotomic obstruction.** If \(\zeta\) is primitive of prime order \(p\), a sum of \(m\) (not necessarily distinct) \(p\)-th roots of unity with nonnegative integer coefficients can vanish only when \(p\mid m\). Indeed, its nonnegative-coefficient residue polynomial must be divisible by \(\Phi_p(t)=1+t+\cdots+t^{p-1}\), so its \(p\) residue counts coincide. For \(v\ne2au\), a zero of \(A_g(u,v)\) would force \(p\mid L_u\). For \(v=2au\), the displayed formula is a sum of \(p+L_u\) roots and hence a zero again requires \(p\mid L_u\). Therefore the modular certificate implies zero-free ambiguity. Since \(0\le C_u\le k\), the hypothesis \(3k<p\) ensures \(0<L_u\le3k<p\), for every \(u\), proving the uniform assertion.

**Stability.** On the chirp line \(v=2au\), the displayed identity and the triangle inequality yield \(|A_g(u,v)|\ge p-L_u\ge p-3k\ge1\). Off that line, \(A_g(u,v)\) is a nonzero algebraic integer in \(\mathbb Q(\zeta)\), with exactly \(L_u\) positive root summands. Its field norm is a nonzero rational integer, and each of the other \(p-2\) conjugates has modulus at most \(L_u\). Hence \(|A_g(u,v)|\ge L_u^{-(p-2)}\ge(3k)^{-(p-2)}\). Because \(3k\ge3\), this lower bound also holds on the chirp line. The standard Weyl-operator diagonalization of the Gabor intensity-lifting map gives its singular values as \(\sqrt p|A_g(u,v)|\). Further, \(\|g\|_2^2\le p+3k\), since each inserted impulse increases the squared modulus by at most three; this gives the stated condition-number bound.

**Boundary counterexamples.** For the three listed configurations, the chirp-line condition \(v=2au\) is false, and the residue polynomial of the cross terms contains **one copy of each of the \(p\) roots**. Therefore the ambiguity vanishes identically by \(1+\zeta+\cdots+\zeta^{p-1}=0\). The standalone exact checker computes these residue counts without floating-point arithmetic.

## Verification
Run `python3 verify.py` (Python standard library only). It enumerates all location subsets and nonzero chirp parameters in the claimed size range for primes \(5,7,11\), and seeded nonexhaustive further cases for \(13,17,19\). It checks the exact cyclotomic residue condition and the three displayed boundary examples. Recorded output is `SPARSE_CHIRP_CYCLOTOMIC_PASS cases= 331112` and `SPARSE_CHIRP_BOUNDARY_PASS examples=3`. The proof for all primes is symbolic; exhaustive finite checks do not imply its infinite quantifiers. The code is a corroboration and supplies exact counterexample certificates.

## Relationship to prior work
Lam--Leung's vanishing-sum theorem (1995) gives the prime-root obstruction, and Bojarovska--Flinth's finite Gabor phase-retrieval criterion (2015) gives the operator-reconstruction implication. These underlying results are not claimed as new. The finding is the support-independent one-third-density window design, its modular pair-overlap certificate, uniform (though coarse) noise bound, and explicit failure examples beyond the guaranteed range. Existing single-impulse chirp results do not establish safety under arbitrarily located multiple unit pulses. Results for nonnegative rational windows do not subsume this complex chirped construction. Historical priority is not independently certified.

## Limitations
The modular condition is sufficient, not necessary; examples with larger \(U\) may still have zero-free ambiguity. The guarantee requires a prime cyclic group, chirp coefficient \(a\ne0\), real positive impulse amplitude exactly one, and \(3k<p\). It makes no optimality claim for the one-third constant across all primes, and the stability bound may be exponentially loose. Independent mathematical audit has not been performed.

## References
1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1 (submitted 1995-11-13), https://arxiv.org/abs/math/9511209 .
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (submitted 2015-03-19), https://arxiv.org/abs/1503.05800 .
3. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (2026), https://arxiv.org/abs/2609.09614 ; subsequent relevant context only, not the motivating-source date.
