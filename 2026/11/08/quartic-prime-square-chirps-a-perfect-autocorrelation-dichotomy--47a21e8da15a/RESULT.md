# Quartic prime-square chirps: a perfect-autocorrelation dichotomy and exact ambiguity support

## Finding

For any prime \(p\ge5\), let \(R=\mathbb Z/p^2\mathbb Z\), \(N=p^2\), and \(\zeta_N=\exp(2\pi i/N)\). For the unimodular cyclic window \(g(x)=\zeta_N^{x^4}\), define its unnormalized ambiguity function by
\[
 A_g(a,b)=\sum_{x\in R}\zeta_N^{(x+a)^4-x^4-bx},\qquad (a,b)\in R^2.
\]
Write \(\chi_p\) for the quadratic character of \(\mathbb F_p\), extended by \(\chi_p(0)=0\). Its complete nonzero locus is:

1. \(a=0\): only \(b=0\) survives, and \(A_g(0,0)=p^2\).
2. \(p\nmid a\): \(A_g(a,b)\ne0\) if and only if \(\chi_p(3a(b-a^3))\in\{0,1\}\).
3. \(a=pc\ne0\) in \(R\): \(A_g(a,b)\ne0\) if and only if \(p\mid b\) and it is **not** the case that both \(b=0\) and \(p\equiv2\pmod3\).

Every coefficient excluded by this list is exactly zero; none of the included coefficients cancels. Let \(\delta_p=1\) when \(p\equiv2\pmod3\), and \(\delta_p=0\) otherwise. Then the number of nonzero coefficients is
\[
 \mathscr R_p=1+\frac{p^2(p^2-1)}2+(p-1)(p-\delta_p).
\]
The complex-linear map that sends an arbitrary complex \(N\)-by-\(N\) matrix \(H\) to the \(N^2\) values \(\operatorname{tr}(H\,\pi(u,v)gg^*\pi(u,v)^*)\), with \(\pi(u,v)\) the usual cyclic time-frequency shifts, has rank exactly \(\mathscr R_p\) and nullity \(p^4-\mathscr R_p\).

Most strikingly, the cyclic sequence \(g\) is CAZAC (perfect periodic autocorrelation with constant modulus one) if and only if \(p\equiv2\pmod3\). For \(p\equiv1\pmod3\), *every* off-peak cyclic autocorrelation is nonzero. The proportion \(\mathscr R_p/p^4\) tends to \(1/2\) along primes tending to infinity, in both congruence classes.

## Assumptions and scope

The prime is odd and at least five: characteristic three is excluded because the derivative calculation degenerates. All exponents and frequencies are taken modulo \(p^2\). The Fourier transform and ambiguity sums are **unnormalized**. The quadratic-residue criterion includes zero only where explicitly stated. The Gabor lifting map is complex-linear on the full matrix algebra; no claim of nonlinear signal phase-retrieval injectivity is made.

## Proof

**Exact stationary phase at length two.** For a polynomial \(f\in\mathbb Z[X]\), write any residue as \(x=u+pt\) with \(u,t\in\{0,\ldots,p-1\}\). Taylor expansion modulo \(p^2\) gives
\[
\sum_{x\bmod p^2}\zeta_{p^2}^{f(x)}
 =p\sum_{\substack{u\bmod p\\f'(u)\equiv0\ (\mathrm{mod}\ p)}}\zeta_{p^2}^{f(u)}.
\]
Indeed the inner \(t\)-sum is a geometric character sum, equal to \(p\) precisely at a stationary residue and zero otherwise.

For the ambiguity polynomial \(f_{a,b}(x)=(x+a)^4-x^4-bx\), its derivative reduces modulo \(p\) to
\[
 f'_{a,b}(x)=12ax^2+12a^2x+4a^3-b,
 \qquad \Delta=48a(b-a^3).
\]
If \(p\nmid a\), the leading quadratic coefficient is nonzero (as \(p\ge5\)). The stationary polynomial has one or two roots exactly when \(\Delta\) is zero or a quadratic residue. Multiplication by the square \(16\) shows that this is equivalent to \(\chi_p(3a(b-a^3))\in\{0,1\}\). One critical residue contributes a single nonzero \(p\)-multiple of a \(p^2\)-th root of unity. Two distinct critical residues contribute the sum of two such roots, which cannot vanish: the ratio of two \(p^2\)-th roots cannot be \(-1\), since \(p\) is odd. Hence the stated criterion is both necessary and sufficient.

When \(a=0\), ordinary character orthogonality gives \(A_g(0,b)=p^2\mathbf 1_{\{b=0\}}\). When \(a=pc\ne0\), the derivative modulo \(p\) is \(-b\), so \(p\nmid b\) forces zero. For \(b=pd\), direct expansion gives
\[
 A_g(pc,pd)=p\sum_{u\in\mathbb F_p}\zeta_p^{4cu^3-du}.
\]
A sum of exactly \(p\) (not necessarily distinct) \(p\)-th roots of unity vanishes precisely when each of the \(p\) roots occurs once: the coefficient polynomial is a rational multiple of \(1+T+\cdots+T^{p-1}\). Therefore this sum vanishes precisely when the cubic \(u\mapsto4cu^3-du\) permutes \(\mathbb F_p\).

**Permutation-cubic lemma.** If \(p\ge5\) and \(c\ne0\), the polynomial \(4cu^3-du\) permutes \(\mathbb F_p\) if and only if \(d=0\) and \(p\equiv2\pmod3\). Dividing by \(4c\), consider \(h(u)=u^3+\alpha u\). When \(\alpha=0\), this is a permutation exactly if \(\gcd(3,p-1)=1\). For \(\alpha\ne0\), the collision equation \(h(x)=h(y)\) for \(x\ne y\) is \(x^2+xy+y^2=-\alpha\). This nondegenerate binary quadratic form has exactly \(p-\chi_p(-3)\) solutions for every nonzero target, because it is split or anisotropic according as \(-3\) is a square or nonsquare. There are at most two diagonal pairs \(x=y\); since \(p-\chi_p(-3)\ge4\), a pair with \(x\ne y\) exists. Thus no \(\alpha\ne0\) is permissible. This completes the nonunit case.

**Counting.** There are \(p(p-1)\) unit shifts. For each, exactly \((p+1)/2\) residue classes of \(b\bmod p\) satisfy the discriminant criterion, and each has \(p\) lifts. This contributes \(p^2(p^2-1)/2\) frequencies. The \(p-1\) nonzero shifts in \(pR\) each contribute \(p-\delta_p\) frequencies, and \(a=0\) contributes one. Adding proves \(\mathscr R_p\).

**CAZAC dichotomy.** At an invertible shift \(a\) and modulation \(b=0\), the discriminant criterion is \(\chi_p(-3a^4)\in\{0,1\}\), hence \(\chi_p(-3)=1\). As \(p\ne3\), the latter holds exactly when \(\mathbb F_p\) contains nontrivial cube roots of unity, i.e. \(p\equiv1\pmod3\). At nonzero shifts divisible by \(p\), the preceding cubic calculation gives zero autocorrelation exactly for \(p\equiv2\pmod3\). Therefore all off-peak coefficients vanish precisely in that class, and none vanish in the other. Constant modulus is immediate from the definition of \(g\).

**Gabor-lifting rank.** The time-frequency Weyl matrices \(\pi(a,b)/\sqrt N\) form an orthonormal Hilbert–Schmidt basis of \(M_N(\mathbb C)\). Pairing their conjugacy orbit projectors with this basis produces, up to phases, the character table of \(R^2\) multiplied by the diagonal ambiguity multipliers \(A_g(a,b)\). The character table is invertible, so the lifting rank equals the number of nonzero multipliers, namely \(\mathscr R_p\). This is the standard Weyl-basis diagonalization; the content here is the exact support classification of those multipliers.

## Verification

The accompanying standalone `check_quartic.py` certifies the entire ambiguity support for \(p\in\{5,7,11,13\}\) by integer cyclotomic arithmetic, without floating-point tolerance. For a primitive \(p^2\)-th root \(\zeta\), a polynomial with coefficients supported in exponents \(0,\ldots,p^2-1\) vanishes at \(\zeta\) precisely when, for each residue \(r\bmod p\), its coefficients at \(r,r+p,\ldots,r+(p-1)p\) are all equal. This follows from \(\Phi_{p^2}(T)=1+T^p+\cdots+T^{(p-1)p}\). The checker compares this exact test at every \((a,b)\) to the theorem and asserts the total counts. Expected support sizes for \(p=5,7,11,13\) are respectively \(317,1219,7361,14353\). It prints `QUARTIC_PRIME_SQUARE_EXACT_CYCLOTOMIC_PASS` upon success.

## Relationship to prior work

Blake and Tirkel (2012) give a perfect polyphase construction based on two-column array orthogonality; the constructed lengths are even, whereas the present sequence has odd length \(p^2\). Mercer (2016) presents a unified block-quadratic construction encompassing Frank, Chu and Milewski sequences, but its stated theorem does not classify the quartic prime-square ambiguity coefficients. Bojarovska and Flinth (2015, Theorems 2.2–2.3) establish the general relationship between Gabor measurement injectivity, Weyl multipliers and projector frame bounds. Their result supplies the structural Gabor bridge, not the arithmetic zero criterion here. Earlier CAZAC sequences such as Chu sequences, and Mow's broader perfect-sequence construction, are important antecedents. No claim is made that perfect autocorrelation alone is new or that a general Gabor diagonalization is new.

## Limitations

The formulas concern the special quartic phase on cyclic *prime-square* rings and primes at least five; other exponents, characteristic three and higher prime powers are not covered. They classify exact zeros and lifting rank, not every positive singular-value magnitude or the nonlinear injectivity status of the resulting phase-retrieval measurements. An older, broader polyphase construction, notably the 1995 unified construction of Mow, could imply the CAZAC part after an unexamined equivalence; the exact all-frequency classification has not been established to be historically first. Independent mathematical validation is not included.

## References

- S. T. Blake and A. Z. Tirkel, *A Construction for Perfect Periodic Autocorrelation Sequences*, arXiv:1212.0277v1, first public 2012-12-03, https://arxiv.org/abs/1212.0277.
- I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first public 2015-03-19, https://arxiv.org/abs/1503.05800.
- I. Mercer, *A Unified Approach to Autocorrelation of Frank, Chu, and Milewski Sequences*, arXiv:1608.05098v1, first public 2016-08-17, https://arxiv.org/abs/1608.05098.
- W. H. Mow, *A Unified Construction of Perfect Polyphase Sequences*, IEEE ISIT 1995, DOI: 10.1109/ISIT.1995.550446 (bibliographic abstract only inspected).
