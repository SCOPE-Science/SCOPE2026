# Four exact residue obstructions to half-factoriality of a heptagonal self-map

## Finding

Let \(\mathcal P_7=\{P_7(n):n\geq1\}\), where \(P_7(n)=n(5n-3)/2\), and write
\[
E_{7,x}(t)=x^2t+\frac{9(x^2-1)}{40}
\qquad(x\geq1,\ x\equiv1\pmod{10}).
\]
The parameterization of the affine self-maps of \(\mathcal P_7\) by such integers \(x\) and the composition rule \(E_{7,x}\circ E_{7,y}=E_{7,xy}\) are established in [1]. In particular, the identity is \(E_{7,1}\). For every admissible \(x\), let \(\mathsf L_7(x)\) be the set of numbers of nonidentity *irreducible* self-maps in factorizations of \(E_{7,x}\), with \(\mathsf L_7(1)=\{0\}\).

Let \(a\), \(b\) and \(c\) count, with multiplicity, rational prime divisors of \(x\) congruent respectively to \(3\), \(7\) and \(9\pmod {10}\). The prime factors congruent to \(1\pmod{10}\) are unrestricted. Then \(|\mathsf L_7(x)|>1\) if and only if **at least one** of the following four coordinatewise conditions holds:
\[
\begin{array}{ll}
\text{(I)}&a\geq2,\ b\geq2,\ c\geq2;\\
\text{(II)}&a\geq2,\ b\geq4,\ c\geq1;\\
\text{(III)}&a\geq4,\ b\geq2,\ c\geq1;\\
\text{(IV)}&a\geq4,\ b\geq4.
\end{array}
\]
These four patterns are minimal: no pattern dominates another, and each is realized by factorizations with different lengths.

The **least** admissible parameter with unequal factorization lengths is
\[
\boxed{x=75411=3^4\cdot7^2\cdot19=81\cdot931=21\cdot21\cdot171.}
\]
The factors \(81\), \(931\), \(21\) and \(171\) are irreducible in the multiplicative monoid \(H_{10}=\{x\geq1:x\equiv1\pmod{10}\}\). Thus the least non-half-factorial heptagonal self-map has lengths exactly \(\mathsf L_7(75411)=\{2,3\}\). In contrast, the example in [1, Example 7.9] has parameter \(194481\) and lengths \(2\) and \(4\).

## Assumptions and scope

All primes below are ordinary positive rational primes, counted with multiplicity. Any integer \(x\in H_{10}\) is coprime to \(10\), and every prime factor of \(x\) lies in \(1,3,7,9\pmod{10}\). All factorization lengths are counted in the monoid of self-maps under composition, or equivalently in the multiplicative monoid \(H_{10}\). The criterion applies to every admissible positive parameter, without a size or squarefreeness restriction. The result concerns *lengths*, not uniqueness of the irreducible factors.

## Proof

**1. Reduction to minimal zero-sum sequences.** The isomorphism in [1, Theorem D / Theorem 7.8] reduces the question to irreducible factorizations of \(x\) in \(H_{10}\). Prime factors \(p\equiv1\pmod{10}\) contribute exactly one irreducible factor \(p\) each to every such factorization: any product containing \(p\) and other primes can be split off by \(p\), because its cofactor remains congruent to \(1\pmod{10}\). Thus they shift every factorization length by the same amount and do not affect whether two lengths differ.

The residue group \((\mathbb Z/10\mathbb Z)^\times\) is cyclic of order four. Its nonzero residues \(3,7,9\) have additive weights \(1,-1,2\) modulo four. The six and only six nonempty, minimal zero-sum residue multisets, displayed as triples of multiplicities \((a,b,c)\), are
\[
A=(4,0,0),\quad B=(0,4,0),\quad C=(1,1,0),
\quad D=(0,0,2),\quad E=(2,0,1),\quad F=(0,2,1).
\]
For completeness, a minimal zero-sum multiset of length at most four (by the pigeonhole argument for partial sums in a group of order four) either contains a weight-\(2\) element, in which case its remaining weights yield one of \(D,E,F\), or contains only weights \(1,-1\), in which case it is one of \(A,B,C\). Any prime multiset of each of these types yields an irreducible \(H_{10}\) element; any other zero-sum multiset has a proper zero-sum submultiset and yields a reducible element. Prime labels of the same residue may always be allocated arbitrarily to the prescribed slots.

**2. A length formula.** Let a factorization of \(x\), after removing all residue-\(1\) prime factors, use \(u,v,w,z,e,f\) atoms of types \(A,B,C,D,E,F\), respectively. Then
\[
a=4u+w+2e,\qquad b=4v+w+2f,\qquad c=2z+e+f.
\]
Its length excluding the fixed residue-\(1\) contribution is \(\ell=u+v+w+z+e+f\), so
\[
\boxed{\ell=\frac{a+b+2c+2w}{4}.}
\]
Since \(a-w\) and \(b-w\) must be even, admissible values of \(w\) have a fixed parity. Two different lengths therefore require factorizations with type-\(C\) counts \(w_0\) and \(w_1\) satisfying \(w_1\geq w_0+2\).

**3. Necessity of the four thresholds.** Remove \(w_0\) copies of \(C\) from the residue pattern of *both* factorizations, an operation at the residue-multiset level. The remaining pattern has coordinates \(a'=a-w_0\geq2\), \(b'=b-w_0\geq2\), \(c'=c\). The factorization arising from the smaller type-\(C\) count now contains no \(C\), and its coordinates satisfy
\[
a'=4u+2e,\quad b'=4v+2f,\quad c'=2z+e+f.
\]
If \(u,v\geq1\), then \(a',b'\geq4\), giving (IV). If \(u\geq1,v=0\), positivity of \(b'\) forces \(f\geq1\), giving (III). If \(u=0,v\geq1\), then \(e\geq1\), giving (II). If \(u=v=0\), positivity of both \(a'\) and \(b'\) forces \(e,f\geq1\), giving (I). Since \(a\geq a'\) and \(b\geq b'\), the original parameter dominates the corresponding threshold.

**4. Sufficiency.** Each of the four minimal residue vectors supports the following distinct-length atom partitions:
\[
\begin{array}{c|c|c}
(a,b,c)&\text{first factorization}&\text{second factorization}\\\hline
(2,2,2)&E+F&2C+D\\
(2,4,1)&B+E&2C+F\\
(4,2,1)&A+F&2C+E\\
(4,4,0)&A+B&4C
\end{array}
\]
The first three compare two atoms against three, and the last compares two against four. If the prime multiset of \(x\) dominates one of these patterns, remove primes of that pattern. The remaining multiset has product congruent to \(1\pmod{10}\), because both \(x\) and the removed subproduct do. It therefore factors into monoid atoms; append any fixed such factorization to both distinct-length partitions. This yields unequal lengths for \(x\), proving the equivalence for every admissible \(x\).

**5. Numerical minimality.** The least ordinary prime in residue classes \(3,7,9\pmod{10}\) is respectively \(3,7,19\). Thus parameters dominating the four thresholds (I)–(IV) are bounded below respectively by
\[
3^2 7^2 19^2=159201,\quad
3^2 7^4 19=410571,\quad
3^4 7^2 19=75411,\quad
3^4 7^4=194481.
\]
Their minimum is \(75411\), which is realized by the (III) partition \(A+F=2C+E\), yielding \(81\cdot931=21^2\cdot171\). All displayed factors correspond to minimal zero-sum multisets and are irreducible. At the vector \((4,2,1)\), the displayed two and three are the only lengths, since the formula in step 2 forces \(w\in\{0,2\}\). The result follows.

## Verification

The standalone standard-library program `verify.py` enumerates the six atom patterns by a recurrence on residue-multiplicity vectors of total weight at most \(24\) and checks the threshold criterion in all \(735\) admissible vectors. Separately, it enumerates exact factorizations of all \(19{,}999\) nonidentity elements of \(H_{10}\) at most \(200{,}000\) and confirms the first unequal-length parameter and its two lengths. It checks the four minimal integer bounds and the explicit irreducible witness. Run using `python3 verify.py`. No numerical bound is used in the unrestricted proof.

## Relationship to prior work

[1] proves that the self-map monoid of the heptagonal numbers is \(H_{10}\), establishes the global half-factoriality classification for all polygonal families, and gives an unequal-length example at \(194481\). The four-pattern **individual-element criterion** and the least parameter \(75411\) do not occur in the inspected theorem, proof, examples or surrounding discussion. [2] and [3] give the general arithmetic-congruence-monoid framework. In particular, [2, Theorem 3.4] supplies the general transfer to a block monoid over the residue unit group, so the reduction to zero-sum sequences is established background; it does not state the four thresholds or the least heptagonal parameter. [3] studies length density and other global factorization invariants, not this elementwise zero-versus-positive length defect classification. The result is a specific finite-class-group structural specialization, not a new general transfer theorem.

## Limitations

This is a statement about heptagonal self-maps and the monoid \(H_{10}\); it neither classifies every polygonal family nor describes all possible sets of factorization lengths beyond detecting whether their sizes exceed one. The proof relies on the polygonal self-map parameterization from [1]; the zero-sum classification and numerical minimality are proved here. Broad general theorems on zero-sum sequences and factorization may make the specialization accessible, so historical priority of its explicit four-threshold formula and least parameter is not independently certified.

## References

[1] Mateo Matijasevick, *Retriangular numbers and affine maps between polygonal numbers*, arXiv:2610.36284v1 (first posted 2026-10-26), Theorem D, Theorem 7.8, Example 7.9, section 7.5. https://arxiv.org/abs/2610.36284

[2] M. Banister, J. Chaika, S. T. Chapman and W. Meyerson, *On the arithmetic of arithmetical congruence monoids*, Colloquium Mathematicum 108 (2007), 105–118, DOI:10.4064/cm108-1-9; also P. Baginski and S. T. Chapman, *Arithmetic Congruence Monoids: A Survey*, section 3, Theorem 3.4 (2014). https://geodesic.mathdoc.fr/articles/10.4064/cm108-1-9/

[3] S. T. Chapman, C. Liu, A. Ma and A. Zhang, *On the factorization invariants of arithmetical congruence monoids*, arXiv:2210.01224 (first posted 2022-10-03), especially section 4 on length density. https://arxiv.org/abs/2210.01224
