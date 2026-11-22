# A sharp one-disagreement extremal law and complete matching fibres for generic two-order types

## Finding
Let \(\Pi\) be the countable homogeneous structure with two independent dense linear orders. Name an arbitrary finite parameter set \(A\) of size \(n\geq 2\), and let \(\pi\in S_n\) be its pattern: in first-order increasing position \(k\), the parameter has second-order rank \(\pi(k)\). Every complete nonalgebraic one-point type is specified by one insertion gap in each order. A type *disagrees* with a named parameter when the two orders place its new point on opposite sides of that parameter. Write \(c_r(\pi)\) for the number of types disagreeing with exactly \(r\) named parameters and \(P_\pi(z)=\sum_{r=0}^{n}c_r(\pi)z^r\).

**Theorem.** For every \(n\geq2\) and \(\pi\in S_n\),
\[
c_1(\pi)\leq 2n,
\]
with equality **if and only if** \(\pi\) is a product of pairwise disjoint adjacent transpositions, equivalently \(|\pi(k)-k|\leq1\) for every \(k\). If that product has \(s\) transpositions, its *entire* type-disagreement spectrum is
\[
P_\pi(z)=n+1+2\sum_{r=1}^{n}(n+1-r)z^r+s(z^2-1).
\]
Conversely, the exact fibre of this polynomial among \(S_n\) consists solely of the products of exactly \(s\) disjoint adjacent transpositions, and has cardinality
\[
\binom{n-s}{s},\qquad 0\leq s\leq\lfloor n/2\rfloor.
\]
In particular, the full disagreement spectrum remembers the **number** but not the **locations** of independent neighboring swaps. Its maximum-one-disagreement extremizers altogether number \(F_{n+1}\), the path-matching/Fibonacci count with \(F_1=F_2=1\).

## Assumptions and scope
The two orders are named, separate, irreflexive linear relations; the parameter points are individually named but ordered in each relation. Only complete **nonalgebraic** one-point types (new point distinct from every parameter) are counted. The parameters may induce any permutation pattern \(\pi\); no assumption of randomness of the finite base is made. Every pair of insertion gaps is realized in \(\Pi\), and different pairs give different types, by the free amalgamation of the two orders and homogeneity. Thus there are exactly \((n+1)^2\) types.

For gap indices \(i,j\in\{0,\ldots,n\}\), the new point follows exactly the first \(i\) parameters in the first order and exactly the first \(j\) ranks in the second. Denote the corresponding type by \(p_{i,j}\). For a pattern \(\pi\), set
\[
C_\pi(i,j)=\#\{k:1\leq k\leq i,\ \pi(k)\leq j\}.
\]

## Proof
**1. Prefix-disagreement identity.** The old points below the new point in the first and second orders respectively have position sets \(A_i=\{1,\ldots,i\}\) and \(B_j=\{k:\pi(k)\leq j\}\). Their symmetric difference comprises precisely the parameters that disagree. Hence
\[
d_\pi(i,j)=|A_i\mathbin{\triangle}B_j|=i+j-2C_\pi(i,j),\qquad P_\pi(z)=\sum_{i,j=0}^{n}z^{d_\pi(i,j)}.
\]
Because \(|A_i|=i\) and \(|B_j|=j\), \(d_\pi(i,j)\geq |i-j|\); also \(d_\pi(i,j)\equiv i+j\pmod2\).

**2. Sharp bound and equality characterization.** A disagreement count of exactly one is possible only at the \(2n\) cells \((k,k+1)\) or \((k+1,k)\), \(0\leq k<n\). The first cell has disagreement one exactly when \(\pi(\{1,\ldots,k\})\subseteq\{1,\ldots,k+1\}\). All such first-kind cells have disagreement one if and only if \(\pi(k)\leq k+1\) for every \(k\). Similarly all second-kind cells have disagreement one if and only if \(\pi^{-1}(k)\leq k+1\) for every \(k\), equivalently \(\pi(k)\geq k-1\). Thus \(c_1(\pi)\leq 2n\), with equality precisely when every displacement lies in \(\{-1,0,1\}\).

Such a permutation is a matching product: if \(\pi(1)=1\), restrict to positions \(2,\ldots,n\); if \(\pi(1)=2\), the displacement bound for the preimage of \(1\) forces \(\pi(2)=1\), and one restricts to positions \(3,\ldots,n\). Inductively the permutation splits into singleton fixed points and adjacent swaps, with no overlapping swaps. Conversely every such product has displacement at most one.

**3. Exact spectrum.** For the identity permutation, \(C(i,j)=\min(i,j)\), hence \(d(i,j)=|i-j|\), giving
\[
P_{\mathrm{id}}(z)=n+1+2\sum_{r=1}^{n}(n+1-r)z^r.
\]
A swap of the adjacent entries in positions \(k,k+1\) of an otherwise increasing block changes the prefix intersection \(C(i,j)\) from the identity value only at \((i,j)=(k,k)\), decreasing it by one. For pairwise disjoint such swaps, their effects have distinct cells and add. Each cell's disagreement changes from zero to two, and no other coefficient changes. This proves \(P_\pi=P_{\mathrm{id}}+s(z^2-1)\).

**4. Exact fibre and enumeration.** If an arbitrary permutation has that polynomial, its linear coefficient is \(2n\), so step 2 forces it to be a matching product with, say, \(t\) swaps. Comparing the constant coefficient with step 3 gives \(t=s\). Conversely every \(s\)-swap matching has that polynomial. Choosing \(s\) nonconsecutive swap start positions among the \(n-1\) possible positions gives \(\binom{n-s}{s}\) choices. Summing over \(s\) yields the number of matchings in a path on \(n\) vertices, namely \(F_{n+1}\).

## Verification
A standalone Python 3 program, `check_insertion_spectrum.py`, directly computes each gap type's discordant-parameter count from order comparisons, independently of the prefix-sum proof. It exhaustively checks **all 46,232 permutations** across sizes \(2\) through \(8\), verifying the bound, exact equality cases, polynomial formula, and every matching-fibre cardinality. Its captured output is `check_output.txt`, ending with `ALL_EXHAUSTIVE_INSERTION_CHECKS_PASS`. These finite checks are corroboration; the preceding proof establishes the theorem for unbounded \(n\).

For example, the two different parameter patterns \(1243\) and \(1324\) both have \(P(z)=4+8z+7z^2+4z^3+2z^4\). The theorem explains this collision for every \(n\) and every set of independent adjacent swaps.

## Relationship to prior work
Cameron's *Homogeneous permutations* (2002) treats the two-linear-order representation and establishes its Fraïssé classification and unrestricted amalgamation. Linman and Pinsker's *Permutations on the random permutation* (arXiv 2014, published 2015) classifies reducts; its parameter-orbit analysis identifies the \((n+1)^2\) gap rectangles. These background facts establish the type indexing but **do not themselves state** the sharp one-disagreement extremal classification, the location-blind full polynomial, or its exact fibres in the inspected relevant portions. The classical characterization/enumeration of bandwidth-one permutations as path matchings is used as elementary supporting combinatorics, not claimed as new. Searches for permutation insertion-disagreement statistics and exact one-point type spectra found no equivalent published assertion; an older alternative terminology may have been missed.

## Limitations
The disagreement statistic counts logical types uniformly, not sampled elements or a probability law on a dense order. Only new singleton types and the fixed two-order language are covered; the result is not a reconstruction theorem for arbitrary permutations. Although the result has an all-size proof and finite checker, historical priority is provisional and no independent mathematical review has occurred.

## References
1. P. J. Cameron, *Homogeneous permutations*, Electronic Journal of Combinatorics **9**(2) (2002), R2, published 2002-10-31, https://doi.org/10.37236/1674 ; open PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i2r2/pdf/ .
2. J. Linman and M. Pinsker, *Permutations on the random permutation*, arXiv:1405.4297 (first posted 2014-05-16), Electronic Journal of Combinatorics **22**(2) (2015), P2.54, https://doi.org/10.37236/4910 ; open PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p54/pdf/ .
