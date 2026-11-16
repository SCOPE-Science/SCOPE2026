# A ternary-prime-power spectral resonance for the nine-point Lee cross

## Finding
Let \(q\) be an odd prime and \(k\geq1\). On \(G=(\mathbb Z/q^k\mathbb Z)^4\), define the radius-one Lee cross \(B=\{0,\pm e_1,\ldots,\pm e_4\}\) and the averaging convolution \(Tf(x)=\frac19\sum_{b\in B}f(x-b)\). The convolution is invertible whenever \(q\neq3\). For \(q=3\), its exact complex kernel dimension is
\[
\boxed{\dim\ker T=192\cdot3^{k-1}-160.}
\]
Every vanished character is one of the following two, disjoint types. Set \(m=3^{k-1}\), \(N=3m\). **Type A:** exactly one Fourier coordinate is zero and the remaining three belong to \(\{m,2m\}\); there are exactly 32. **Type B:** exactly one Fourier coordinate is in \(\{m,2m\}\), and the other three, after independently changing their signs, are the three distinct elements of \(\{r,r+m,r+2m\}\) for some \(r\not\equiv0\pmod m\). There are exactly \(192(m-1)\) Type B characters. The class is empty when \(k=1\).

Consequently, for ternary moduli the rank is \(3^{4k}-192\cdot3^{k-1}+160\), and the fraction of invisible characters is \((192\cdot3^{k-1}-160)/3^{4k}\).

## Assumptions and scope
The group is a product of four cyclic groups of **prime-power** order \(q^k\), where \(q\) is an odd prime, \(k\) is any positive integer, and complex functions on \(G\) carry counting measure. A Fourier coordinate \(u_j\) denotes its canonical residue modulo \(q^k\). The operators and kernel dimensions are complex-linear. The assertion does not classify arbitrary composite moduli or higher Lee radii.

The complex characters \(\chi_u(x)=e^{2\pi i(u\cdot x)/N}\), with \(N=q^k\), constitute an orthogonal basis. Their multipliers are real:
\[
\lambda_u=\frac19\left(1+\sum_{j=1}^{4}(e^{2\pi i u_j/N}+e^{-2\pi i u_j/N})\right)
=\frac19\left(1+2\sum_{j=1}^{4}\cos(2\pi u_j/N)\right).
\]
All statements about injectivity and rank refer exactly to these multipliers.

## Proof
**Step 1: prime-power obstruction.** For a fixed Fourier vector \(u\), let \(c_h\) count occurrences of residue \(h\) in the multiset \(\{0,\pm u_1,\ldots,\pm u_4\}\), and form \(F_u(X)=\sum_{h=0}^{N-1}c_h X^h\). Then \(9\lambda_u=F_u(\zeta_N)\), where \(\zeta_N\) is a primitive \(N\)-th root of unity. If this vanishes, the irreducible polynomial \(\Phi_{q^k}(X)\) divides \(F_u(X)\) over \(\mathbb Q[X]\). Since \(\Phi_{q^k}(1)=q\), evaluating the divisibility at one gives \(q\mid F_u(1)=9\); thus \(q=3\). Rational divisibility suffices: the quotient of two monic integer polynomials, when polynomial, has integer coefficients, although only its value at one is used here. Hence all other odd prime powers yield invertible convolution.

**Step 2: coefficient fibers at the exceptional prime.** Write \(N=3m\), \(m=3^{k-1}\), and note \(\Phi_{3^k}(X)=1+X^m+X^{2m}\). Because \(\deg F_u<N\), the relation \(F_u(\zeta_N)=0\) is **equivalent** to
\[
 c_r=c_{r+m}=c_{r+2m}\qquad(0\le r<m).
\]
Indeed, divisibility forces \(F_u=(1+X^m+X^{2m})H\) with \(\deg H<m\), making these three coefficients equal; the converse follows directly by factoring out \(\Phi_{3^k}\).

**Step 3: the zero-residue fiber.** Let \(a\) count coordinates with \(u_j=0\), and \(b\) count coordinates with \(u_j\in\{m,2m\}\). Since \(N\) is odd, the coefficients at \(0,m,2m\) are exactly \((1+2a,b,b)\), so equality forces \(b=1+2a\). As \(a+b\le4\), only \((a,b)=(1,3)\) and \((a,b)=(0,1)\) are possible. The first case gives Type A: choose the zero coordinate in four ways and independently choose the signs of the other three, totaling \(4\cdot2^3=32\).

**Step 4: every other fiber.** In the second case three coordinates remain, all nonzero modulo \(m\). For \(m=1\), this is impossible, so only Type A occurs. For \(m>1\), each such coordinate contributes one occurrence to a residue class \(r\ne0\pmod m\) and one to its distinct negative class \(-r\pmod m\). Each occupied three-position fiber must contain at least three occurrences by Step 2; hence all three remaining coordinates share the same unordered pair \(\{r,-r\}\) of nonzero residue classes. For a fixed choice of one representative \(r\) of this pair, independently negating the three coordinates makes them all lie in the fiber \(\{r,r+m,r+2m\}\). Equality then demands one occurrence at each of its three positions, and automatically gives the conjugate balancing in the negative fiber. This is precisely Type B.

There are \((m-1)/2\) unordered nonzero residue pairs \(\{r,-r\}\); four choices of distinguished coordinate, two signs for that coordinate, \(3!\) assignments of the three fiber positions to the other coordinates, and \(2^3\) independent sign choices. Thus the Type B count is
\[
\frac{m-1}{2}\cdot4\cdot2\cdot3!\cdot2^3=192(m-1).
\]
Types A and B are disjoint. The two counts sum to the claimed nullity, since the character basis diagonalizes convolution. Subtracting from \(|G|=N^4\) gives the rank. This establishes the claim for every odd prime and every positive exponent, with no finite-cutoff assumption.

## Verification
The included standalone `checker.py` uses integer coefficient-bin equality, not floating trigonometry, to determine exactly which primitive-root character multipliers vanish. For each \(N\in\{3,9,27\}\) it exhaustively compares this cyclotomic test with the two explicit structural patterns over all \(N^4\) Fourier vectors. It finds respective Type A counts 32,32,32, Type B counts 0,384,1536, and total nullities 32,416,1568. These finite calculations are supplemental; Steps 1–4 are the all-exponent mathematical proof.

Reproduce with `python checker.py` using Python 3 and its standard library.

## Relationship to prior work
The radius-one Lee neighborhood is the first radius-one Lee ball with composite cardinality: the three- and two-dimensional balls have seven and five points, whereas this four-dimensional ball has nine. Fourier diagonalization of abelian convolution and the cyclotomic prime-power divisibility criterion are standard. The specific simultaneous classification of all invisible characters, the two distinct geometric mechanisms, and their exact all-exponent multiplicities are the additional assertions here.

Xu and Zhou (arXiv:2210.03361v1, 2022) develop group-ring and Lee-ball techniques for almost-perfect **radius-two** code packings. Their main theorem is about dimensions admitting such packings, not the Fourier rank of the radius-one nine-point torus convolution. Mesnager, Tang, and Qi (2018) establish spectral criteria for **two-error-correcting** Lee codes and study associated Cayley graphs, rather than an all-depth nullity census for the present operator. Classical Fourier/cyclotomic facts are used directly and not claimed as novel.

## Limitations
The result covers only four-dimensional radius-one Lee crosses on prime-power cyclic tori. The classification does not assert a stable inverse at moduli for which the operator is invertible, or classify vanishing eigenvalues on general composite moduli. Finite computations check only three ternary exponents; the infinite statement relies on the supplied proof. Historical priority with respect to less accessible specialized work on Lee-neighborhood Cayley spectra remains a risk; independent validation has not been performed.

## References
1. X. Xu and Y. Zhou, *On almost perfect linear Lee codes of packing radius 2*, arXiv:2210.03361v1, first public 2022-10-07, https://arxiv.org/html/2210.03361v1 .
2. S. Mesnager, C. Tang and Y. Qi, *2-Correcting Lee Codes: (Quasi)-Perfect Spectral Conditions and Some Constructions*, IEEE Transactions on Information Theory **64** (2018), 3031–3041, DOI: 10.1109/TIT.2018.2789921 .
3. Standard cyclotomic factorization: \(\Phi_{p^k}(X)=(X^{p^k}-1)/(X^{p^{k-1}}-1)\) for prime \(p\) and \(k\ge1\); Fourier diagonalization of convolution on finite abelian groups.
