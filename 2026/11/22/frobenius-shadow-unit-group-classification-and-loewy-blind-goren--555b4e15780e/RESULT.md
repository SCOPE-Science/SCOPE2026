# Frobenius-shadow unit-group classification and Loewy-blind Gorenstein pairs

## Finding

**Theorem (Frobenius-shadow classification).** Fix a prime \(p\), an integer \(f\ge 1\), and \(q=p^f\). Let \(I\) be an Artinian monomial ideal in \(k[x_1,\ldots,x_d]\), with \(k=\mathbb F_q\), and let \(B\subset\mathbb N^d\) be its finite down-set of standard monomial exponent vectors. Put \(A=k[x_1,\ldots,x_d]/I\) and let \(\mathfrak m\) be its maximal ideal. For every \(s\ge0\), define
\[
r_s=\#\{\alpha\in B\setminus\{0\}:p^s\alpha\in B\}.
\]
Then \(r_s=0\) for sufficiently large \(s\), and the complete abstract unit group is
\[
A^\times\cong C_{q-1}\times\prod_{s\ge1}\bigl(C_{p^s}\bigr)^{f(r_{s-1}-2r_s+r_{s+1})}.
\]
All exponents in this expression are nonnegative integers. Here \(C_1\) denotes the trivial group, so the first factor is harmless when \(q=2\). For a monomial complete intersection \(I=(x_1^{a_1},\ldots,x_d^{a_d})\), the shadow counts simplify to
\[
r_s=\prod_{i=1}^d\left\lceil\frac{a_i}{p^s}\right\rceil-1.
\]

**Theorem (uniform unit-group collision).** For every odd prime \(p\) and every \(f\ge1\), consider the two complete intersections
\[
R=k[x,y]/(x^{p-1},y^{2p}),\qquad
S=k[x,y]/(x^p,y^{2p-2}),\qquad k=\mathbb F_{p^f}.
\]
They have isomorphic full unit groups,
\[
R^\times\cong S^\times\cong
C_{p^f-1}\times(C_p)^{f(2p(p-1)-3)}\times(C_{p^2})^f,
\]
but are not isomorphic as rings: their Loewy lengths are respectively \(3p-2\) and \(3p-3\). Both rings are local, commutative, Artinian, Gorenstein complete intersections of the same \(k\)-dimension \(2p(p-1)\), the same embedding dimension \(2\), and the same one-dimensional socle dimension. Thus even within this restricted class, the full abstract unit group does not determine Loewy length.

For \(p=3\), the pair \(k[x,y]/(x^2,y^6)\) and \(k[x,y]/(x^3,y^4)\) has dimension \(12\), respective Loewy lengths \(7\) and \(6\), and over \(\mathbb F_3\) common full unit group \(C_2\times C_3^9\times C_9\).

## Assumptions and scope

The monomial ideal \(I\) contains a positive power of every variable, so its quotient is a finite-dimensional local algebra and every standard exponent vector is a member of a finite coordinatewise down-set \(B\). Variables may be absent if \(d=0\); the empty product gives the expected unit group of a field. The coefficient field is finite of characteristic \(p\), including all extension degrees \(f\ge1\). The group isomorphisms in the assertions are **abstract**, not canonical algebra maps. The collision rings require odd \(p\), since the indicated embeddings and shadow counts do not have the same properties at \(p=2\).

The Loewy length of a finite local ring is the smallest positive integer \(L\) for which \(\mathfrak m^L=0\). The embedding dimension is \(\dim_k\mathfrak m/\mathfrak m^2\), and the socle is \(\operatorname{Ann}_A(\mathfrak m)\).

## Proof

**Step 1: split the units.** Every unit in a local monomial algebra has nonzero constant term. Therefore multiplication gives \(A^\times\cong k^\times\times U\) where \(U=1+\mathfrak m\) is an abelian \(p\)-group of size \(q^{|B|-1}\). The field unit group is cyclic of order \(q-1\).

**Step 2: calculate every power image, not only its kernel.** For \(u\in\mathfrak m\), commutativity and characteristic \(p\) imply
\[
(1+u)^{p^s}=1+u^{p^s}.
\]
Write \(u=\sum_{\alpha\in B\setminus\{0\}}c_\alpha x^\alpha\). The same identity gives
\[
u^{p^s}=\sum_{\substack{\alpha\in B\setminus\{0\}\\p^s\alpha\in B}}c_\alpha^{p^s}x^{p^s\alpha}.
\]
The monomials on the right are pairwise distinct. Frobenius \(c\mapsto c^{p^s}\) is bijective on the finite field \(k\), so each surviving coefficient is arbitrary. Consequently the image \(U^{p^s}=\{g^{p^s}:g\in U\}\) has exactly \(q^{r_s}\) elements. Nilpotence of \(\mathfrak m\) ensures \(r_s=0\) eventually.

**Step 3: recover cyclic multiplicities uniquely.** Write \(U\cong\prod_{j\ge1}(C_{p^j})^{c_j}\) by the elementary-divisor theorem for finite abelian groups. Raising to the \(p^s\)-th power yields
\[
f r_s=\log_p|U^{p^s}|=\sum_{j>s}(j-s)c_j.
\]
Subtract consecutive equalities twice to obtain
\[
c_s=f(r_{s-1}-2r_s+r_{s+1})\quad(s\ge1).
\]
The formula proves the claimed group structure and nonnegativity, because each \(c_s\) is a genuine cyclic multiplicity. For a rectangular monomial down-set, the number of exponents \(0\le\alpha_i<a_i\) satisfying \(p^s\alpha_i<a_i\) is \(\lceil a_i/p^s\rceil\); remove the all-zero exponent to obtain the displayed complete-intersection formula.

**Step 4: compute the two shadow profiles.** For both collision rings, \(\dim_kA=2p(p-1)\) and therefore \(r_0=2p(p-1)-1\). Since \(p\ge3\), the only nonconstant standard monomial that remains after multiplying every exponent coordinate by \(p\) is \(y\), whose image is \(y^p\). Thus \(r_1=1\). Since their truncation exponents are smaller than \(p^2+1\) and \(p^2\) exceeds both highest permitted exponents, \(r_s=0\) for \(s\ge2\). Hence \(c_1=f(2p(p-1)-3)\), \(c_2=f\), and all higher multiplicities vanish. Step 1 gives the common full unit group.

**Step 5: prove the rings differ structurally.** In \(k[x,y]/(x^a,y^b)\) with \(a,b\ge2\), the socle is exactly the line spanned by \(x^{a-1}y^{b-1}\). The maximal ideal has square-independent classes \(x,y\), so its embedding dimension is \(2\). Its highest nonzero total-degree monomial has degree \(a+b-2\); therefore its Loewy length is \(a+b-1\). The two specified exponent pairs have Loewy lengths \(3p-2\) and \(3p-3\), respectively. Loewy length is invariant under ring isomorphism, proving nonisomorphism, while both algebras remain Gorenstein complete intersections.

## Verification

The included standalone `verify_units.py` implements polynomial multiplication in finite truncated monomial algebras independently of the theoretical elementary-divisor formula. It exhaustively checks orders for all principal units in three small prime-field examples of dimensions \(6\) or \(8\), samples direct powers in both characteristic-three collision algebras, independently enumerates **all** \(3^{11}=177147\) principal units for each collision ring using their Frobenius monomial support, and checks their exact order histograms:
\[
\#\{g:\operatorname{ord}(g)=1,3,9\}=(1,59048,118098).
\]
It also compares the predicted unit cyclic factors for primes \(3,5,7,11\), field extension degree \(2\), and a nonrectangular Artinian monomial down-set. Run `python3 verify_units.py` with Python 3 using only the standard library. These finite checks support the algebra; the all-characteristics and all-dimensions assertions are established by the proof, **not** by the finite tests.

## Relationship to prior work

Chebolu, Corry, Grimm and Hatfield classify rings whose entire unit group is an elementary abelian group of fixed prime exponent, including certain quotients of truncated polynomial algebras. Their Theorems 1.1 and 1.3 address that restrictive exponent-one property rather than the full list of cyclic elementary divisors of arbitrary finite monomial quotients or the two presented Loewy-blind Gorenstein rings. Their 2021 preprint motivates treating the unit group as a ring invariant.

Angeltveit, Gerhardt, Hill and Lindenstrauss study the multivariate truncated complete-intersection family in higher, multi-relative algebraic \(K\)-theory through generalized Witt vectors. Their paper has deeper general machinery, but its inspected main theorems do not state either the present elementary-divisor census for ordinary principal units or the explicit nonisomorphic collision family. In particular, a multivariate truncated-algebra \(K\)-theory calculation should not be conflated with an asserted classification of its entire abstract unit group. Classical Frobenius and finite abelian group theory are essential inputs, not claimed as new.

## Limitations

The group isomorphism in the collision is abstract and does not identify the rings, their additive-multiplicative interactions, or their maximal-ideal filtrations. The theorem does not address arbitrary nonmonomial Artinian quotients or infinite coefficient fields. No assertion is made about the smallest possible collision dimension in any characteristic. Although targeted source and database comparisons found no explicit equivalent collision in the inspected materials, unpublished, inaccessible and differently formulated literature remains a priority risk; independent external mathematical validation has not been performed.

## References

- S. K. Chebolu, J. Corry, E. Grimm and A. Hatfield, *Rings with an elementary abelian \(p\)-group of units*, arXiv:2112.03853 (first posted 2021-12-07), https://arxiv.org/abs/2112.03853. See Theorems 1.1 and 1.3 and Section 3.
- V. Angeltveit, T. Gerhardt, M. A. Hill and A. Lindenstrauss, *On the algebraic \(K\)-theory of truncated polynomial algebras in several variables*, arXiv:1206.0247 (2012), https://arxiv.org/abs/1206.0247. See Sections 1–2 and 4–5.
