# Exact arithmetic-progression spectra at ternary Motzkin nondivisibility indices

## Finding

Let \(M_n\) be the Motzkin numbers, and for each integer \(r\ge1\) define
\[
N_r=\frac{3^{r+1}-1}{2},\qquad E_r=\{0\le n<N_r:3\nmid M_n\}.
\]
For \(\ell\ge3\) and positive integer \(d\), write \(P_{\ell,r}(d)\) for the number of integers \(a\ge0\) for which all \(\ell\) numbers \(a,a+d,\ldots,a+(\ell-1)d\) belong to \(E_r\). Put \(d_j^-=(3^j-1)/2\) and \(d_j^+=(3^j+1)/2\). Then the **complete step-by-step progression spectrum** is:

- \(P_{3,r}(1)=2^{r+1}-2\), \(P_{3,r}(2)=2^r-2\), and \(P_{3,r}(d_j^-)=P_{3,r}(d_j^+)=2^{r-j+1}-1\) for \(2\le j\le r\).
- \(P_{4,r}(1)=3\cdot2^{r-1}-2\), and \(P_{4,r}(d_j^-)=2^{r-j}-1\) for \(2\le j\le r\).
- \(P_{5,r}(1)=2^r-2\), and \(P_{6,r}(1)=2^{r-1}-1\).
- Every other \(P_{\ell,r}(d)\) is zero for \(\ell\ge3\).

Values zero in these formulas represent absent progressions, not possible differences. In particular, the total numbers of length-three through length-six progressions are, respectively,
\[
5\cdot2^r-2r-6,\quad 2^{r+1}-r-2,\quad 2^r-2,\quad 2^{r-1}-1.
\]
No seven-term arithmetic progression occurs among *any* indices \(n\ge0\) for which \(3\nmid M_n\), while six-term progressions occur. Hence the sharp global maximum length is six.

## Assumptions and scope

The Motzkin numbers are the integers counting Motzkin paths, characterized by \(M_0=M_1=1\) and \(M_n=M_{n-1}+\sum_{i=0}^{n-2}M_iM_{n-2-i}\) for \(n\ge2\). All progressions in this theorem are strictly increasing, with integral positive step, and **every member** lies within the finite set \(E_r\). An index may be used by multiple progressions, each counted once by its first term and step. The formulas apply to all integers \(r\ge1\) without an asymptotic proviso.

The input congruence (not new here) is Deutsch and Sagan's 2004/2005 ternary characterization: the indices with \(3\nmid M_n\) are precisely the nonnegative elements of \(3T+\{0,-1,-2\}\), where \(T\) consists of nonnegative integers having only digits zero or one in base three. Its derivation from central trinomial coefficients appears in their Corollaries 4.9--4.10.

## Proof

**1. Digit model and boundary.** For \(r\ge0\), let
\[
T_r=\left\{\sum_{i=0}^{r-1}\varepsilon_i3^i:\varepsilon_i\in\{0,1\}\right\},\qquad
B_r=3T_r+\{0,1,2\}.
\]
Each \(T_r\) is free of nonconstant three-term arithmetic progressions: the equality \(u+w=2v\) entails equality at each ternary digit, because both sides have digitwise contributions at most two and therefore no carry. Thus \(u=v=w\).

The greatest element of \(T_r\) is \((3^r-1)/2\); the next element of the infinite set \(T\) is \(3^r\). Consequently the cited Motzkin congruence gives the exact identity
\[
E_r+2=B_r\setminus\{0,1\},\qquad |E_r|=3\cdot2^r-2.
\]
Indeed the largest nondivisible index from \(T_r\) is \(3(3^r-1)/2=N_r-1\), and the next is \(3^{r+1}-2>N_r-1\). Translating a set preserves arithmetic progressions and their differences.

**2. Cross-block classification.** For \(r\ge1\), \(B_r=B_{r-1}\cup(3^r+B_{r-1})\), disjoint. For \(r\ge2\), abbreviate \(q=3^r\), \(X=B_{r-1}\), and \(L=(q+1)/2\). Then \(X\subseteq[0,L]\) and contains \(0,1,L-1,L\). Every nonconstant three-term progression crossing the two blocks \(X\) and \(q+X\) is exactly one of
\[
(0,L,q+1),\quad (1,L,q),\quad (L-1,q,q+L),\quad (L,q,q+L-1).
\]
To prove exhaustiveness, if the first two members lie in \(X\), put the first member \(v\ge0\), the middle member \(L-u\), and the last member \(q+w\); the arithmetic-progression equation becomes \(v+2u+w=1\), forcing the first two displayed solutions. If the first member lies in \(X\) and the other two in \(q+X\), write them \(L-u,q+v,q+L-w\); then \(u+2v+w=1\), giving the other two solutions. The required boundary elements are all in \(X\).

For a four-term progression crossing both blocks, distributions of three members in one block and one in the other are impossible: they would force a step \(d\ge q-L=L-1\) and simultaneously \(2d\le L\), contradictory for \(q\ge9\). Thus exactly two consecutive members must be in each block. Writing the first as \(a\), the next as \(a+d\le L\), and the third as \(a+2d\ge q\) gives \(a\le 2L-q=1\). If \(a=0\), then \(d=L\), but the fourth member lies beyond \(q+L\). If \(a=1\), necessarily \(d=L-1\), and all four members occur. Hence the unique cross-block four-term progression is
\[
(1,L,q,q+L-1).
\]
It extends neither to the left nor to the right within \(B_r\). Every cross-block progression of at least five terms would contain a cross-block four-term subprogression; therefore there are no cross-block progressions of five or more terms when \(r\ge2\).

**3. Complete step counts.** At level \(r=1\), \(B_1=\{0,1,2,3,4,5\}\). Its three-term step counts are four at step one and two at step two; its four-term step count is three at step one; five-term and six-term counts are two and one, respectively, both at step one. At every later level, each old progression occurs in each of the two translated blocks, doubling its step count. Four new three-term progressions have step differences \(d_r^-\) (twice) and \(d_r^+\) (twice), while exactly one new four-term progression has difference \(d_r^-\); no new longer progressions occur. This proves the complete step counts for \(B_r\).

Pass from \(B_r\) to \(B_r\setminus\{0,1\}\). At level one, this removes two of the four step-one three-term progressions and both step-two ones, two of the three four-term progressions, both five-term progressions, and the unique six-term progression. At each new level \(r\ge2\), the lower block retains the previously deleted points, the upper block is complete, and precisely the first two of the four listed cross-block triples and the unique cross-block quadruple use a deleted point. Thus at every old step the surviving count equals the previous surviving count plus the complete previous-block count; new differences \(d_r^-\) and \(d_r^+\) contribute one surviving triple each, but no surviving quadruple. Solving these explicit recurrences gives every displayed \(P_{\ell,r}(d)\), and summing over differences gives the four total formulas.

**4. Sharp length bound.** In any hypothetical seven-term progression in \(B_r\), the first, fourth, and seventh terms have the same residue modulo three. Their quotients after removing that residue form a nonconstant three-term arithmetic progression in \(T_r\), which is impossible by Step 1. Every finite progression in the infinite Motzkin nondivisibility set is contained in a sufficiently large \(E_r\), so there is no global seven-term progression. At \(r=2\), the six consecutive nondivisible Motzkin indices \(7,8,9,10,11,12\) give a six-term progression, proving sharpness.

## Verification

The self-contained Python checker `check.py` independently evaluates Motzkin numbers by their integer recurrence for the first 130 indices and compares their nondivisibility with the ternary digit criterion. It enumerates progressions and compares every step-count spectrum for levels \(1\le r\le8\), independently checks the number of progressions of each length, and enumerates the cross-block families for levels \(2\le r\le8\). Its last execution passed 189 grouped assertions. These finite tests **do not establish** the all-level theorem; the full proof is in the preceding section.

Run from the extracted directory with `python3 check.py` (Python 3 standard library only).

## Relationship to prior work

Deutsch and Sagan, arXiv:math/0407326, Corollary 4.10, establish the Motzkin index digit characterization; the present claim begins with that known criterion and evaluates a different invariant: every arithmetic-progression step count and the sharp possible progression lengths. Krattenthaler and Müller, arXiv:1308.2856, Section 7, establish stronger prime-power **congruence** descriptions but not these evaluated additive progression counts. Moy and Rolnick, arXiv:1502.06013, study progression-free Stanley sequences, including the digit set underlying \(T_r\); the nondivisibility set here is its threefold thickening with a boundary deletion, and is emphatically *not* progression-free. An earlier published result on exact progressions in such thickenings could nevertheless imply the theorem; publication priority has not been independently certified.

## Limitations

The theorem counts ordinary integral progressions entirely contained in specified finite prefixes; it does not classify arbitrary non-arithmetic finite patterns, weighted progressions, or prime-power divisibility beyond the prime three. It uses a previously published Motzkin congruence. The proof and finite checker have been reviewed together, not independently audited. Search-based literature comparison is fallible, particularly for unindexed theses or older additive-combinatorics work.

## References

1. E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326 (first version July 19, 2004); *Journal of Number Theory* 117 (2006), 191--215, Corollaries 4.9--4.10. https://arxiv.org/abs/math/0407326
2. C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(3^k\) behaviour of recursive sequences*, arXiv:1308.2856 (August 13, 2013), Section 7. https://arxiv.org/abs/1308.2856
3. R. A. Moy and D. Rolnick, *Novel structures in Stanley sequences*, arXiv:1502.06013 (February 20, 2015), Sections 1--2. https://arxiv.org/abs/1502.06013
