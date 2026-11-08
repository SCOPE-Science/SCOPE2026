# Harmonic cross-ratios force a sharp modular quartic multiplication-rank jump

## Finding

Let \(p\ge 7\) be a prime and \(k\) any field of characteristic \(p\). In the standard graded Artinian complete intersection
\[
R_p=k[x,y]/(x^p,y^p),
\]
put \(f_\lambda=xy(x-y)(x-\lambda y)\), where \(\lambda\in k\). Its third power defines a square linear map
\[
\mu_{p,\lambda}:(R_p)_{p-7}\longrightarrow (R_p)_{p+5},\qquad h\longmapsto f_\lambda^3h,
\]
whose source and target both have dimension \(p-6\).

**Theorem.** Let \(\Delta_p(\lambda)\) be the determinant of this map in the monomial bases specified below. It is a polynomial in \(\mathbb F_p[\lambda]\) of degree **exactly** \(3(p-6)\), with constant coefficient and leading coefficient both \((-1)^{p-6}=-1\). Its nonvanishing locus is therefore a nonempty Zariski-open subset of the four-distinct-root parameter line \(\mathbb A^1\setminus\{0,1\}\). At each harmonic cross-ratio
\[
\lambda\in\{-1,2,1/2\}
\]
(the three values are distinct since \(p\ge7\)), the rank of \(\mu_{p,\lambda}\) is **exactly \(p-7\)**, so its corank is exactly one. The full multiplication operator \(m_{f_\lambda}^3\) on \(R_p\) has generic rank \((p-6)^2\), while at a harmonic value its rank is at most \((p-6)^2-1\). Thus even among binary quartics with four distinct linear roots, the Jordan type of multiplication by the quartic is not constant.

The claim does **not** assert that the harmonic values are the entire zero set of \(\Delta_p\); extra geometric zeroes may occur, especially over field extensions.

## Assumptions and scope

All statements concern ordinary associative multiplication in \(R_p\), not differentiation or classical Waring rank. The field is arbitrary of prime characteristic at least seven (thus includes prime-power finite fields and algebraic closures). Each \((R_p)_j\) denotes the degree-\(j\) homogeneous piece. The multiplication maps and determinant are defined by the actual residue classes of homogeneous polynomials. For \(\lambda\notin\{0,1\}\), the four projective roots of \(f_\lambda\) are distinct; \(\lambda=-1,2,1/2\) are the harmonic cross-ratios. Genericity is Zariski-generic over the algebraic closure, not a claim about every rational parameter in every finite field.

## Proof

**1. Matrix and determinant degree.** Write \(d=p-7\), \(n=d+1=p-6\), and take the source basis
\[
u_i=x^iy^{d-i}\quad(0\le i<n)
\]
and target basis
\[
v_j=x^{6+j}y^{p-1-j}\quad(0\le j<n).
\]
Let \(c_s(\lambda)\) be the coefficient of \(x^sy^{12-s}\) in \(f_\lambda^3\), and set it to zero for \(s\notin[0,12]\). The matrix entry in row \(j\), column \(i\) is exactly \(c_{6+j-i}(\lambda)\). Every entry has degree at most three in \(\lambda\), so the determinant degree is at most \(3n\).

At \(\lambda=0\), \(f_0^3=x^6y^3(x-y)^3\), and the matrix is triangular: only entries with \(0\le j-i\le3\) can be nonzero, and each diagonal entry is \(-1\). Consequently \(\Delta_p(0)=(-1)^n\). The coefficient of \(\lambda^3\) in \(f_\lambda^3\) is \(-x^3y^6(x-y)^3\). Its multiplication matrix is triangular in the opposite direction, with diagonal entries \(-1\); it is the coefficient of \(\lambda^{3n}\) in the determinant. Hence the leading coefficient is \((-1)^n\) and the degree is exactly \(3n\).

**2. Upper bound at the harmonic parameter.** Take \(\lambda=-1\) and \(f=xy(x^2-y^2)\). On \((R_p)_d\), consider the symmetric pairing
\[
B(g,h)=[x^{p-1}y^{p-1}](gh f^3).
\]
The ring's perfect socle pairing identifies its rank with that of \(\mu_{p,-1}\). Since \(f^3=x^3y^3(x^2-y^2)^3\) contains only odd powers of \(x\), an entry of \(B\) between monomials \(x^iy^{d-i}\) and \(x^jy^{d-j}\) can be nonzero only if \(i+j\) is odd. Since \(d=2m\) with \(m=(p-7)/2\), the basis has \(m+1\) even-indexed and \(m\) odd-indexed monomials. The pairing matrix is therefore off-diagonal in these two blocks, giving rank at most \(2m=p-7\).

**3. Matching lower bound.** Take the \(m\) even basis monomials indexed \(i=2a\), \(0\le a<m\), and the \(m\) odd monomials indexed \(j=2b+1\), \(0\le b<m\). Their pairing block has entries
\[
Q_{a,b}=(-1)^{3-s}\binom3s,\qquad s=m+1-a-b,
\]
interpreted as zero unless \(0\le s\le3\). Reverse its columns. The resulting \(m\times m\) Toeplitz matrix has diagonal \(-3\), first superdiagonal \(1\), first subdiagonal \(3\), and second subdiagonal \(-1\). For \(m=0\), its determinant is the empty determinant \(1\). For \(m\ge1\), expansion along the first row (and the resulting band minors) gives the continuant recurrence
\[
D_m=-3D_{m-1}-3D_{m-2}-D_{m-3},\quad D_0=1,\ D_1=-3,\ D_2=6.
\]
Elementary induction yields
\[
D_m=(-1)^m\binom{m+2}{2}.
\]
As \(m=(p-7)/2\), the binomial coefficient is congruent to \(15/8\) modulo \(p\), nonzero for every prime \(p\ge7\). The off-diagonal block therefore has rank \(m\); the whole pairing has rank \(2m=p-7\). This also covers \(p=7\), when \(m=0\) and the one-dimensional middle map vanishes.

**4. The other harmonic parameters.** The six anharmonic transformations of a four-point cross-ratio carry \(-1\) to precisely \(\{-1,2,1/2\}\). The corresponding binary quartics are carried into scalar multiples of one another by invertible linear changes of variables. Every such change induces a graded automorphism of \(R_p\), because in characteristic \(p\), \((ax+by)^p=a^px^p+b^py^p\). Multiplication-map ranks are therefore identical for all three harmonic parameters.

**5. Generic full multiplication rank.** At \(\lambda=0\), multiplication by \(f_0^3=x^6y^3(x-y)^3\) from degree \(t\) to degree \(t+12\) is injective for each \(0\le t\le p-7\). Indeed, in the monomial bases the coefficient of \(x^6y^6\) gives a triangular square submatrix with diagonal \(-1\), and all its monomials survive the truncation. For \(t>p-7\), the perfect socle pairing of \(R_p\) identifies the map as the transpose of a corresponding injection in a complementary degree, hence it is surjective whenever its target is nonzero. Therefore every graded map at \(\lambda=0\) has maximal rank. Summing the symmetric Hilbert-function minima gives
\[
\operatorname{rank}(m_{f_0}^3)=1+2+\cdots+(p-6)+\cdots+2+1=(p-6)^2.
\]
Maximal rank in each graded piece is an open condition in \(\lambda\). Their finite intersection is a nonempty open set (it contains \(0\)), which also meets \(\mathbb A^1\setminus\{0,1\}\) over an algebraic closure. At any harmonic point the middle map drops rank by exactly one, and no other graded map can exceed its maximal rank; hence the total rank is at most \((p-6)^2-1\). Since the ranks of powers determine the Jordan partition of a nilpotent linear operator, the Jordan type varies even in the squarefree quartic locus. \(\square\)

## Verification

Run `python3 verify.py` using Python 3 with no external packages. The program directly expands the quartic cube in characteristic \(p\), constructs its actual middle multiplication matrices, performs finite-field elimination, computes the harmonic Toeplitz minor and checks maximal rank of every graded map at the \(\lambda=0\) witness. Prime fields \(p=7,11,13,17,19,23,29,31\) were checked; the recorded output appears in `verification_output.txt`. These finite checks do not establish the theorem for all primes: that comes from the preceding proof and the exact continuant determinant.

## Relationship to prior work

Cook's 2011 study of Lefschetz properties of monomial complete intersections concerns powers of linear forms and characteristic-dependent general Lefschetz behavior. Lundqvist and Nicklasson (2016) further classify strong/weak Lefschetz behavior for such algebras. Glasby, Praeger and Xia (2014) study modular tensor products and Jordan partitions for tensor products of Jordan blocks, again involving linear nilpotent operators. None of those inspected results directly determines the \(\lambda\)-dependent rank divisor for multiplication by the third power of a binary quartic.

Dimca and Sticlaru (2020) identify harmonic cross-ratios through a **different invariant**, the classical complex Waring rank of a binary quartic. That is a noteworthy parallel, not the present characteristic-\(p\) truncated-algebra multiplication result. Classical catalecticant and modular Lefschetz techniques are acknowledged; no novelty is claimed for them individually. Published-priority assessment remains provisional: an unknown theorem about generalized multiplication determinants could imply the specialized divisor and corank statement.

## Limitations

The complete factorization or geometric zero set of \(\Delta_p\) is not determined; its zeros need not be only the three harmonic parameters. The theorem treats the third power of a split quartic with four distinct roots, in characteristic \(p\ge7\), and a specific middle graded map. It does not classify all Jordan blocks at every exceptional parameter, nonhomogeneous quartics, or characteristic two, three, or five. The argument proves generic full rank over an algebraic closure, not existence of a non-harmonic full-rank parameter over every finite field. No independent mathematical audit has been performed.

## References

1. D. Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979v1 (first posted 2011-11-21), https://arxiv.org/abs/1111.4979.
2. S. Lundqvist and L. Nicklasson, *On the structure of monomial complete intersections in positive characteristic*, arXiv:1604.06820v1 (first posted 2016-04-22), https://arxiv.org/abs/1604.06820.
3. S. P. Glasby, C. E. Praeger and B. Xia, *Decomposing modular tensor products: Jordan partitions, their parts and p-parts*, arXiv:1403.4685v1 (first posted 2014-03-19), https://arxiv.org/abs/1403.4685.
4. A. Dimca and G. Sticlaru, *Waring rank of binary forms, harmonic cross-ratio and golden ratio*, arXiv:2002.05617v1 (first posted 2020-02-13), https://arxiv.org/abs/2002.05617. Discussed solely as later closely related context, not as the archive date anchor.
