# Sharp square-root length of the absorbing element in type-A \(0\)-Hecke monoids

## Finding
For every integer \(n\ge 2\), the minimum Coxeter length of a square root of the absorbing longest element in the type-A \(0\)-Hecke monoid is
\[
\min\{\ell(w): w\star w=w_0\}=\left\lceil\frac{n(n-1)}4\right\rceil.
\]
If \(n\equiv 0\) or \(1\pmod 4\), every minimum-length square root is also an ordinary permutation square root of the reversal permutation \(w_0\); conversely every ordinary group square root is minimum-length. The exact number is
\[
\frac{(2k)!}{k!},\qquad k=\lfloor n/4\rfloor.
\]
For either remaining congruence class, the construction below gives a minimum-length root whose ordinary permutation square differs from \(w_0\) by one central adjacent transposition. These last two congruence classes are **not** asserted to have a complete root-multiplicity classification.

## Assumptions and scope
Let \(n\ge2\) be an integer, let \(S_n\) act on \(\{1,\ldots,n\}\), and let \(s_i=(i,i+1)\), \(1\le i<n\). The Coxeter length \(\ell(w)\) is the number of inversions in the one-line notation of \(w\). The Demazure product \(u\star s_i\) equals \(us_i\) when \(\ell(us_i)>\ell(u)\), and equals \(u\) otherwise; associativity defines \(u\star v\). Identify the indexed elements of \(H_0(S_n)\) with permutations in \(S_n\). The reversal \(w_0(i)=n+1-i\) is the absorbing element, and \(L=\ell(w_0)=n(n-1)/2\). Ordinary permutation multiplication is denoted by juxtaposition and is distinct from \(\star\).

## Proof
**Lower bound.** Every Coxeter generator in the concatenation of two reduced expressions for \(w\) increases Demazure length by at most one. Hence \(\ell(w\star w)\le2\ell(w)\). Because \(\ell(w_0)=L\), every square root satisfies \(\ell(w)\ge\lceil L/2\rceil\).

**Construction.** For every odd \(j\in\{1,3,\ldots,2\lfloor n/4\rfloor-1\}\), use the permutation four-cycle
\[
(j,\ j+1,\ n+1-j,\ n-j).
\]
The supports of these four-cycles are disjoint; let \(w_n\) equal their product together with the following disjoint central factor, according to the residue of \(n\) modulo four: no factor for residue zero; the central fixed point for residue one; the transposition \((n/2,n/2+1)\) for residue two; and the three-cycle \(((n-1)/2,(n+1)/2,(n+3)/2)\) for residue three. All cycles are specified in ordinary cycle notation, and the omitted points are fixed.

The construction satisfies the one-line recursion
\[
w_{n+4}=(2,\ n+4,\ w_n(1)+2,\ldots,w_n(n)+2,\ 1,\ n+3).
\]
There are exactly \(2n+3\) new inversions: \(n\) between the second entry and the inner block, \(n\) between the inner block and the penultimate entry, and three among the four outer entries. Consequently \(\ell(w_{n+4})=\ell(w_n)+2n+3\). Directly, the four initial lengths for \(n=2,3,4,5\) are \(1,2,3,5\). The number \(\lceil n(n-1)/4\rceil\) obeys the same four-step recursion and initial values, establishing \(\ell(w_n)=\lceil L/2\rceil\) in every degree.

**Square identity.** Each four-cycle \((j,j+1,n+1-j,n-j)\) squares to the pair of reversal transpositions \((j,n+1-j)(j+1,n-j)\). If \(n\equiv0,1\pmod4\), the central factor contributes exactly the central action of \(w_0\), so \(w_n^2=w_0\). Since the ordinary group product is bounded above by the Demazure product in Bruhat order and \(w_0\) is maximal, \(w_n\star w_n=w_0\).

If \(n\equiv2\pmod4\), put \(i=n/2\). If \(n\equiv3\pmod4\), put \(i=(n+1)/2\). The central factor now shows \(w_n^2=w_0s_i\), and direct reading of the central one-line entries gives \(\ell(w_ns_i)=\ell(w_n)-1\). Hence
\[
w_n^{-1}w_0=w_ns_i\le_{\mathrm{Bruhat}} w_n.
\]
The subword characterization of Bruhat order supplies a subword of any reduced expression for \(w_n\) whose group product is \(w_ns_i\). Apply that subword after an initial factor \(w_n\): its ordinary product is \(w_n(w_ns_i)=w_0\). The Demazure product using the entire second reduced word is at least this product in Bruhat order, because omitting generators from a sequence of monotone Demazure steps cannot increase the result. Therefore \(w_n\star w_n=w_0\). This completes the sharpness proof.

**Multiplicity in the even-length cases.** When \(L\) is even, any \(w\star w=w_0\) with \(\ell(w)=L/2\) must increase length at all \(2\ell(w)\) steps of two concatenated reduced expressions. Thus its ordinary square equals \(w_0\). Conversely any \(w^2=w_0\) is automatically a Demazure square root. Such group roots exist exactly when \(n\equiv0,1\pmod4\), because \(w_0\) then has an even number \(2k\) of disjoint transpositions (plus at most one fixed point). To square to \(w_0\), an ordinary permutation must pair those \(2k\) transpositions into \(k\) unordered pairs, replacing each pair with a four-cycle; each pair admits two choices of direction. This gives \((2k)!/(2^k k!)\cdot2^k=(2k)!/k!\) roots. Every such root has length exactly \(L/2\): it has fourth power the identity, so \(w_0w=w^{-1}\), while \(\ell(w_0w)=L-\ell(w)\) and \(\ell(w^{-1})=\ell(w)\). The central point is fixed in the odd-degree case. For \(n\equiv2,3\pmod4\), the odd number of disjoint transpositions of \(w_0\) precludes an ordinary permutation square root, consistent with the necessary one-step Demazure slack.

## Verification
The accompanying standalone `checker.py` independently builds the canonical witnesses, applies the Demazure product using reduced words, checks ordinary squares and inversion lengths for every \(2\le n\le100\), and exhaustively enumerates all length-minimizing permutations for \(2\le n\le8\). It also tests the exact group-root multiplicities in the degrees where the theorem states them. Run `python3 checker.py` with Python 3 and no third-party dependencies. The resulting standard output is included in `checker_output.txt`. These finite checks are consistency checks; the unrestricted result follows from the proof above.

## Relationship to prior work
Denton, Hivert, Schilling and Thiéry establish the finite \(0\)-Hecke monoid framework and its Bruhat-order conventions; their representation-theoretic theorems do not state the shortest identical two-pass factorization of \(w_0\). Kosuda classifies Coxeter-element products whose prescribed higher powers afford the longest permutation. Those Coxeter-element statements do not give the unrestricted minimum length of one element whose **Demazure square** is \(w_0\); the distinguished element here normally uses repeated generators and has length quadratic rather than linear in \(n\). The subword characterization and length bound are standard tools; the claimed contribution is the sharp all-degree paired-four-cycle construction, its mod-four transition, and the exact minimal-root count in the even-length regimes.

## Limitations
A complete count of minimizing roots in the two odd-length congruence classes is not established. No uniqueness of the exhibited witnesses is asserted. Existing results about involution atoms, sorting networks or repeated 0-Hecke products might imply this optimization theorem indirectly; the historical-priority comparison is provisional.

## References
- T. Denton, F. Hivert, A. Schilling and N. M. Thiéry, *On the representation theory of finite J-trivial monoids*, arXiv:1010.3455v1 (2010-10-17), especially Section 2.4. https://arxiv.org/abs/1010.3455
- M. Kosuda, *Coxeter elements of the symmetric groups whose powers afford the longest*, arXiv:1411.5761v1 (2014-11-21), especially Theorems 2.1 and 4.3. https://arxiv.org/abs/1411.5761

