# Universal four-atom dependencies and the sharp phase alphabet for Klein-group Gabor systems

## Finding

Let \(G=(\mathbb Z/2\mathbb Z)^2\) and let \(g\in\mathbb C^G\) be a window. For \(t,m\in G\), set
\[
(\pi(t,m)g)(x)=(-1)^{m\cdot x}g(x+t),\qquad x\in G.
\]
Write \(V=G\times G\), and for \(u=(t,m)\), \(v=(s,n)\) define the binary symplectic form
\[
\Omega(u,v)=t\cdot n+s\cdot m\pmod 2.
\]
For every four-element set \(S=\{u_0,u_1,u_2,u_3\}\subset V\), form the square matrix with columns \(\pi(u_j)g\).

**Universal-dependence theorem.** Its determinant is the zero polynomial in the four coordinates of \(g\), equivalently the four atoms are dependent for **every** complex window, if and only if the three binary vectors \(a=u_1-u_0\), \(b=u_2-u_0\), \(c=u_3-u_0\) are linearly independent and
\[
\Omega(a,b)=\Omega(a,c)=\Omega(b,c)=1.
\]
This criterion does not depend on the ordering or choice of \(u_0\). Exactly **240** of the \(\binom{16}{4}=1820\) index sets satisfy it. Each of the other **1580** determinants is nonzero as a polynomial, and the single integer window \(g=(1,2,3,5)\), in lexicographic coordinate order, makes all 1580 simultaneously nonsingular.

**Sharp phase-alphabet theorem.** Restrict to flat windows whose four coordinates belong to the \(q\)-th roots of unity, with one common primitive \(q\)-th root and no arbitrary continuously varying phases. For \(q=1,2,3,4,5,6\), the *minimum*, over all such windows, of the number of extra singular four-atom sets beyond the unavoidable 240 is, respectively,
\[
1324,\quad1324,\quad12,\quad24,\quad4,\quad12.
\]
Thus **seven phases are necessary and sufficient** to avoid every additional four-atom failure. In fact, with \(\zeta_7=\exp(2\pi i/7)\),
\[
\boxed{g=(1,\zeta_7,\zeta_7^2,\zeta_7^4)}
\]
realizes exactly the 240 unavoidable rank-three four-atom sets and 1580 rank-four sets. All \(\binom{16}{3}=560\) three-atom sets are independent for this window.

## Assumptions and scope

Coordinates of \(G\) are pairs of bits with addition modulo two and dot product modulo two. Enumerate \(0,1,2,3\) by the two-bit encodings \((0,0),(0,1),(1,0),(1,1)\), respectively. The sixteen phase-space labels are \(4t+m\), with \(t,m\in\{0,1,2,3\}\). Every four-subset is unordered, but determinant columns may be placed in increasing label order without affecting singularity. The ring \(\mathbb Z[\zeta_q]\) uses the exact cyclotomic polynomial \(\Phi_q\). No generic-window assumption is made for the universal-dependence assertion. The phase-alphabet minimization allows repeated phases and fixes only the common alphabet of \(q\)-th roots.

These statements concern complex linear dependence, **not** numerical conditioning or positive reconstruction bounds. Multiplying the entire window by a common nonzero phase does not change any dependence, so for the finite phase search the first phase exponent is normalized to zero.

## Proof

**1. Exact determinant expansion, with complete finite coverage.** The entry of the Gabor matrix at row \(x\in G\) and column \((t,m)\in V\) equals \((-1)^{m\cdot x}g(x+t)\). For any fixed four-set \(S\), expand the determinant into all \(4!=24\) permutation terms. Each term is a signed monomial of total degree four in the independent variables \(g(0),g(1),g(2),g(3)\). Represent it by its exponent four-tuple and its integral coefficient. Combine like exponent tuples. The determinant is identically zero if and only if **every** resulting integer coefficient vanishes. The provided `verify_klein_gabor.py` implements exactly these operations with integers, visits every one of the 1820 four-sets, and for each checks equivalence with the displayed symplectic criterion. The exhaustive result is 240 identically zero polynomials, with no unclassified set. This is a finite exhaustive proof of the particular four-dimensional identity, not an inference from a sample of windows.

**2. Structural count and generic attainability.** Fix the anchor \(u_0\) in 16 ways. There are 15 choices of nonzero \(a\); there are eight \(b\) with \(\Omega(a,b)=1\). For these independent \(a,b\), exactly four vectors \(c\) solve the two independent equations \(\Omega(a,c)=\Omega(b,c)=1\). Of these four, precisely one, \(c=a+b\), is dependent on \(a,b\), leaving three. Each unordered four-set is counted \(4\cdot 3!=24\) times. Therefore
\[
\frac{16\cdot15\cdot8\cdot3}{24}=240.
\]
Changing the anchor replaces the differences by invertible affine combinations and preserves the independence condition and the all-one symplectic pairings; hence the criterion is well defined. For each other set the symbolic determinant is a nonzero polynomial, so its zero locus is a proper algebraic subset. More constructively, the verifier evaluates all determinants by exact integer Bareiss elimination at \(g=(1,2,3,5)\) and finds none of these 1580 zero. Thus every one of the 240 is an unavoidable failure, while simultaneous success on all others is attained.

**3. Exhaustive phase-alphabet lower bound.** For each \(q\in\{1,\ldots,6\}\), normalize the first phase exponent to zero and enumerate the remaining \(q^3\) ordered exponent triples. For each choice, substitute \(g(x)=\zeta_q^{e_x}\) into all 1580 nonuniversal four-determinants. Evaluate the 24 determinant terms exactly as an integer polynomial in \(\zeta_q\), reduce by \(\Phi_q\), and count zeros precisely when every coefficient of the reduced remainder is zero. The cyclotomic-reduction table used by the verifier is explicit for all six values of \(q\). Exhaustion of all \(\sum_{q=1}^6q^3=441\) normalized candidate windows yields the six claimed minima, all strictly positive. The normalizing phase does not alter any matrix rank, so the search covers *all* \(q\)-phase windows. No floating-point zero test enters this argument.

**4. Seven-phase upper bound and independent lifting certificate.** Taking phase exponents \((0,1,2,4)\) and \(q=7\), exact reduction modulo \(\Phi_7(z)=1+z+\cdots+z^6\) gives zero for precisely the 240 sets described above. All 560 triples are checked by their four possible three-row determinant minors in the same cyclotomic ring: each has at least one nonzero minor. The separate `verify_klein_modular.py` gives a second, independent exact certificate. The element \(4\) in \(\mathbb F_{43}\) has multiplicative order seven. Substituting \(\zeta_7\mapsto4\) therefore defines a ring homomorphism \(\mathbb Z[\zeta_7]\to\mathbb F_{43}\). Gaussian elimination on all 1820 four-sets and 560 triples gives four-set rank counts \(240\) at rank three and \(1580\) at rank four, and all triples rank three. Any nonzero determinant over \(\mathbb F_{43}\) must have been nonzero in \(\mathbb Z[\zeta_7]\), hence in \(\mathbb C\). The universally zero determinants vanish over every ring. Together, this gives the asserted **exact complex ranks**. Combining steps 3 and 4 proves seven is the smallest root-of-unity alphabet size with no avoidable four-set failures.

## Verification

Running `python3 verify_klein_gabor.py` requires only the Python standard library. Its recorded output in `verify_klein_gabor.out` confirms complete polynomial/geometry agreement over 1820 cases, integer-window evaluation, all six alphabet minima, the explicit seventh-root witness and all 560 triple checks. The independently implemented `python3 verify_klein_modular.py` uses finite-field elimination rather than symbolic cyclotomic determinants; its recorded output in `verify_klein_modular.out` confirms the complete rank profile and lifting argument.

Each script generates the entire index collection internally, not a selected or random sample. The first script's zero tests are over exact integer polynomial coefficients; the second script's nonzero certificates are in the exact prime field \(\mathbb F_{43}\), and the ring homomorphism makes their implication for complex nonvanishing rigorous.

## Relationship to prior work

The prime-cyclic full-spark theorem of Lawrence, Pfander and Walnut establishes generic maximal independence for cyclic prime dimensions, a different setting. Krahmer, Pfander and Rashkov analyze general finite-group short-time Fourier support and erasure recovery, but their all-group bounds do not enumerate the 1820 four-atom Klein-group dependencies. Pfander's *Gabor frames in finite dimensions*, Theorem 11, gives a **specific** universally dependent quartet over the Klein group and concludes that full spark is impossible there. Malikiosis' *Spark deficient Gabor frames*, Section 3, generalizes this obstruction to noncyclic finite abelian groups. These results already imply nonexistence of a full-spark Klein-group Gabor frame; that implication is not new here. What is separately established is the **complete symplectic classification and exact count of all universally dependent quartets**, an explicit simultaneous attainability witness for the other 1580, and the **sharp flat phase-alphabet threshold seven** with full three-atom independence. Relevant published research-record searches concerning Gabor dependence, symplectic rank obstructions and phase-alphabet designs did not uncover the same combined finite classification. This bounded search does not guarantee historical priority.

## Limitations

This is a finite, four-coordinate theorem for the Klein group only. It does not classify Gabor matroids over all noncyclic groups, prove that seven-phase windows optimize singular values, or give stability bounds under noise. The finite phase count applies to a common root-of-unity alphabet; unconstrained phase choices are not covered by its minimality statement. Historical priority remains conditional on available literature indexing and examination; no independent mathematical audit has been performed.

## References

1. J. Lawrence, G. E. Pfander, D. Walnut, *Linear Independence of Gabor Systems in Finite Dimensional Vector Spaces*, Journal of Fourier Analysis and Applications **11** (2005), 715–726; freely accessible full text: https://webhomes.maths.ed.ac.uk/~v1ranick/gabor.pdf ; DOI 10.1007/s00041-005-5017-6.
2. G. E. Pfander, *Gabor frames in finite dimensions*, in *Finite Frames: Theory and Applications*, 2013, pp. 193–239, Theorem 11; freely accessible author-hosted chapter: https://www.mathematik.uni-marburg.de/~pfander/pubs/FiniteGaborFramesChapter.pdf ; DOI 10.1007/978-0-8176-8373-3_6.
3. R.-D. Malikiosis, *Spark deficient Gabor frames*, arXiv:1602.09012 (first posted 2016-02-29), especially Section 3 and Theorem 3.2: https://arxiv.org/abs/1602.09012 .
4. F. Krahmer, G. E. Pfander, P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493 (first posted 2006-11-16), especially Sections 4 and 5: https://arxiv.org/abs/math/0611493 .
