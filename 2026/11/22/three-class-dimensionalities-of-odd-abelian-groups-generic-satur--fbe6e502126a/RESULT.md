# Three-class dimensionalities of odd abelian groups: generic saturation and a sharp threshold

## Finding

Let \(G\) be a finite abelian group of odd order \(n\ge3\), written additively, and let \(D_3(G)\) be the number of unordered partitions \(\{\{0\},A,B\}\) with \(A,B\ne\varnothing\) which are dimensionalities in the sense of Jenča. Put \(k=(n-3)/2\) and \(\varepsilon_n=2n(3/4)^k+n(1/2)^k\). Then

\[
2^{n-2}(1-\varepsilon_n)\le D_3(G)\le 2^{n-2}-1.
\]

Consequently, uniformly over all odd-order abelian groups, \(D_3(G)/2^{n-2}\to1\) as \(n\to\infty\). In fact almost all partitions counted by \(D_3(G)\) satisfy the stronger three equations

\[
A+A=A+B=B+B=G.
\]

Such a *fully saturated* partition exists for an odd-order abelian group \(G\) **if and only if** \(|G|\ge13\). All fully saturated partitions produce the same three-element relational monoid: its identity is \(\{0\}\), and every product of two nonidentity classes is the full three-element set. This is not a hypergroup, since the identity belongs both to \(A\ast A\) and to \(A\ast B\), contradicting uniqueness of inverse. At most \(2^{(n-1)/2}-1\) of all three-class partitions preserve inverses; thus almost every three-class dimensionality is also inverse-incompatible and is not an automorphism-orbit partition.

## Assumptions and scope

All group orders in this theorem are odd, with no restriction on the invariant factors. A three-class partition means three nonempty classes including the singleton identity \(\{0\}\), and \(A\) and \(B\) are *unlabeled*. For class subsets \(X,Y\), their sumset \(X+Y\) is \(\{x+y:x\in X,y\in Y\}\). The dimensionality condition is the original universally quantified lifting axiom (D2): whenever \(x+y\) is in a class \(C\), every \(z\in C\) is representable as \(x'+y'=z\) with \(x'\) in the class of \(x\) and \(y'\) in the class of \(y\). Equivalently, each product of two classes is a union of whole classes. The same condition applied to the identity gives the singleton identity axiom.

A quotient hypergroup is understood in the inverse-unique sense in Jenča's framework; no claim is made about alternative broader uses of the word “hypergroup.” The estimate becomes quantitatively useful once \(\varepsilon_n\) is small; no positive bound is asserted for the finitely many smaller orders when the displayed lower bound is negative.

## Proof

**Random-colouring bound.** Independently colour every nonzero element with \(A\) or \(B\), each with probability \(1/2\). Fix a target \(t\in G\). Among decompositions \(t=x+y\) with \(x\) and \(y\) nonzero and distinct, there are at least \(k=(n-3)/2\) disjoint unordered pairs \(\{x,y\}\): for \(t\ne0\), exclude \(x=0,t\) and the unique diagonal solution \(2x=t\); for \(t=0\) there are \((n-1)/2\) such pairs. The pairs use disjoint elements, hence their colour-pattern events are independent.

For any pair, the probability of being monochromatic in \(A\) is \(1/4\), monochromatic in \(B\) is \(1/4\), and mixed is \(1/2\). Thus the probability that \(t\) is missing from \(A+A\), from \(B+B\), or from \(A+B\) is at most \((3/4)^k,(3/4)^k,(1/2)^k\), respectively. A union bound over all \(n\) targets proves the failure probability is no greater than \(\varepsilon_n\). The fully saturated event makes both colours nonempty. There are \(2^{n-1}\) labeled colourings and \(2^{n-2}-1\) unordered three-class partitions. Dividing successful labeled colourings by two establishes the stated lower bound; the total number establishes the upper bound. Since \(n(3/4)^{(n-3)/2}\to0\), almost all such partitions are fully saturated. Their six class products are then \(\{0\}+X=X\) and \(X+Y=G\) for \(X,Y\in\{A,B\}\), so they satisfy the original dimensionality axiom.

**Sharp threshold.** For odd \(n\le7\), if both nonzero colours have at most \((n-1)/2\) elements, their self-sumsets cannot cover \(G\), since \(|A+A|\le |A|(|A|+1)/2\), or the analogous inequality for \(B\). More precisely, at least one colour has size at most \((n-1)/2\), yielding an upper bound less than \(n\) for \(n=3,5,7\). The only abelian groups of orders 9 and 11 are \(C_9,C_3\times C_3,C_{11}\). All \(256,256,1024\) labeled nonidentity two-colourings, respectively, were exhaustively evaluated by the standalone `check.py`, none satisfying the three full-sumset equalities. (The finite enumeration is exhaustive for these three orders, not an extrapolation.)

For odd \(13\le n\le31\), explicit fully saturated witnesses for every abelian isomorphism type occur in the `WITNESSES` dictionary of `check.py`: invariant factor tuples are ordered lexicographically, and a mask bit \(i-1\) places the \(i\)-th nonzero tuple in \(A\); every other nonzero element belongs to \(B\). The program verifies each full sumset and independently applies the universally quantified (D2) test. There are 13 needed group types (cyclic types of odd orders 13 through 31 together with \(C_5^2\), \(C_3\times C_9\), and \(C_3^3\)), and two additional witness types at orders 33, 35. Finally, at \(n=33\),

\[
\varepsilon_{33}=474054603/536870912<1.
\]

For odd \(n\ge33\), each of the positive terms \(2n(3/4)^{(n-3)/2}\) and \(n(1/2)^{(n-3)/2}\) decreases strictly when \(n\) is replaced by \(n+2\). Thus \(\varepsilon_n<1\), and the random-colouring lower bound guarantees at least one fully saturated partition on *every* abelian group of each such order. This completes the if-and-only-if statement.

**Inverse obstruction.** Since \(G\) has odd order, inversion \(x\mapsto-x\) partitions the \(n-1\) nonidentity elements into \(m=(n-1)/2\) two-element orbits. For inversion to permute the two classes \(A,B\), either every orbit must be monochromatic, giving \(2^m-2\) labeled nonempty colourings, or every orbit must be bichromatic, giving \(2^m\). Dividing by two to forget the class labels gives exactly \(2^m-1\) inversion-preserving three-class partitions. In view of the lower bound for \(D_3(G)\), the inverse-preserving fraction tends to zero. Since inversion commutes with every automorphism of an abelian group, an automorphism-orbit partition is inversion-preserving. For a fully saturated quotient, the identity occurs in both \(A\ast A\) and \(A\ast B\), precluding a unique inverse and hence a hypergroup in the stated sense.

## Verification

Run `python3 check.py` in the directory containing this file. A successful invocation prints `THREE_CLASS_DIMENSIONALITY_OK 15 finite witnesses 1536 small-colourings checked` followed by the exact rational value of \(\varepsilon_{33}\). The program implements direct group tables for all invariant-factor tuples, checks the 15 explicit masks against all original quantified (D2) instances, exhaustively rules out the three small-order types, and checks the rational tail estimate. These finite checks support the explicit cases; the random-pair and monotonicity proofs establish the unbounded range.

## Relationship to prior work

Jenča, *Dimensionalities on monoids*, defines the lax equivalences and proves the associated relational quotient and inverse-preserving hypergroup result; it does not enumerate three-class dimensionalities on odd abelian groups or prove this saturation threshold. Earlier structural work by Jenčová and Jenča on monoids in sets and relations does not establish the counting law. Misseldine's enumeration of cyclic Schur rings concerns a stricter partition requirement: preservation of inversion and group-algebra multiplication coefficients, not merely support-level class-sum closure. The known overlap with an earlier finite-group minimal inverse-incompatibility calculation concerns small-group minimality, not the present all-odd-order asymptotic or sharp fully saturated cutoff. The present theorem does **not** claim to originate the elementary random sumset-cover technique itself.

## Limitations

Only odd-order finite abelian groups are covered. The exact value of \(D_3(G)\) at a fixed \(G\) is generally not determined, merely bounded asymptotically; the exact count of fully saturated partitions is not given. The non-hypergroup statement uses inverse uniqueness, and no classification of other relational quotients is claimed. An unindexed equivalent enumeration or probabilistic argument could affect historical priority. Independent review has not been undertaken.

## References

1. Gejza Jenča, *Dimensionalities on monoids*, arXiv:2611.18000v1, first public 2026-11-13, https://arxiv.org/html/2611.18000v1.
2. Anna Jenčová and Gejza Jenča, *On monoids in the category of sets and relations*, arXiv:1703.03728, https://arxiv.org/abs/1703.03728.
3. Andrew Misseldine, *Enumeration Techniques on Cyclic Schur Rings*, arXiv:2112.03422v1, https://arxiv.org/html/2112.03422v1.
