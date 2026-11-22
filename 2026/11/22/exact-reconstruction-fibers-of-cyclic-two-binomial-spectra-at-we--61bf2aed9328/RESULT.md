# Exact reconstruction fibers of cyclic two-binomial spectra at weight three

## Finding

Let \(n\ge3\) be an integer, and let \(\mathcal N_{n,3}\) be the oriented binary necklaces of length \(n\) with exactly three ones: words are identified under cyclic rotation, but not under reversal. For each of the \(n\) indexed rotations \(R_i(w)\), set
\[
 I(R_i(w))=\#\{(p,q):0\le p<q<n,\ (R_i(w))_p=0,\ (R_i(w))_q=1\}.
\]
The **cyclic two-binomial spectrum** is the multiset \(\mathcal S(w)=\{\!\{I(R_i(w)):0\le i<n\}\!\}\), with multiplicity from all \(n\) starting positions, including repeated rotations of a periodic word. For fixed length and weight this is precisely the multiset of full two-binomial equivalence signatures of the rotations: the other scattered counts of length at most two are determined by the number of zeros, the number of ones, and \(I\).

**Theorem.** All fibers of \(\mathcal S:\mathcal N_{n,3}\to\{\text{multisets}\}\) have cardinality at most two. If \(3\nmid n\), every fiber is a singleton. If \(3\mid n\), write \(n=3(h+1)\), where \(h\ge0\). Then exactly \(\binom h2\) fibers are doubletons (with \(\binom h2=0\) for \(h<2\)), and the number of distinct attainable spectra is exactly \((h+1)^2\). Equivalently the spectrum-count function is
\[
 \#\mathcal S(\mathcal N_{n,3})=
 \begin{cases}
 (n-1)(n-2)/6,&3\nmid n,\\
 n^2/9,&3\mid n.
 \end{cases}
\]
The first nontrivial collision occurs at \(n=9\): the nonconjugate words `110001000` and `101010000` both have spectrum \(\{\!\{3,6,6,9,9,9,12,12,15\}\!\}\).

More precisely, encode a necklace by its cyclic triple \((a,b,c)\) of zero gaps between successive ones, with \(a+b+c=n-3\). When \(3\mid n\) set \(h=(n-3)/3\). Its **only possible distinct source mate having the same spectrum** is represented by
\[
 (2h-c,\ 2h-b,\ 2h-a).
\]
Such a mate exists precisely when every original gap is at most \(2h\) and the displayed triple is not cyclically equivalent to the original. The word ``mate'' here means a distinct *source with the same* spectrum; no claim about equal spectra under reflection is made.

## Assumptions and scope

The alphabet symbols are labeled \(0\) and \(1\). Scattered occurrences choose ordered positions, not necessarily adjacent ones. A necklace is oriented: rotations alone are quotiented, not reversals or complements. Every indexed starting position is recorded in the spectrum; this matters for periodic words. The theorem covers all integers \(n\ge3\), with zero-length gaps permitted. This is a reconstruction result for unlabeled multisets of two-binomial observations of *all* rotations, not a statement about the number of different observations within one rotation orbit.

## Proof

**1. Compression to the three one-root observations.** Write a representative as \(w=1\,0^a1\,0^b1\,0^c\), with \(m=a+b+c=n-3\). Starting immediately before each of the three ones, the values of \(I\) are respectively
\[
 t_1=2a+b,\qquad t_2=2b+c,\qquad t_3=2c+a.
\]
When the initial symbol of a rotation moves to the end, \(I\) increases by \(m\) if that symbol is one and decreases by three if it is zero. Thus, following the one-root with value \(t_j\) through the next zero gap of length \(g_j\), the \(g_j\) rotations beginning with zeros have values
\[
 t_j+m,\quad t_j+m-3,\quad\ldots,\quad t_j+m-3(g_j-1).
\]
Here \((g_1,g_2,g_3)=(a,b,c)\), and \(t_{j+1}=t_j+m-3g_j\), with indices modulo three.

Set \(P_w(X)=\sum_{i=0}^{n-1}X^{I(R_i(w))}\) and \(Q_w(X)=X^{t_1}+X^{t_2}+X^{t_3}\). Summing the preceding geometric progressions and including the three one-root rotations gives the polynomial identity
\[
 \boxed{(X^3-1)P_w(X)=(X^n-1)Q_w(X).}
\]
The formula remains valid when a gap is zero, since its progression is empty. For fixed \(n\), the polynomial ring over the integers has no zero divisors. Consequently two necklaces have the same full cyclic spectrum if and only if their *unordered triples* \(\{\!\{t_1,t_2,t_3\}\!\}\) agree.

**2. Inverting the unordered triple.** Let \(g=(a,b,c)^{\mathsf T}\) and \(t=(t_1,t_2,t_3)^{\mathsf T}\). Then
\[
 t=Mg,\qquad M=\begin{pmatrix}2&1&0\\0&2&1\\1&0&2\end{pmatrix},
 \qquad\det M=9.
\]
Cyclically permuting the three coordinates of \(t\) corresponds exactly to rotating the cyclic zero gaps, so does not change the necklace. Since every permutation of three coordinates is either a cyclic permutation or a cyclic permutation followed by swapping the last two, the only potential *different* gap orbit is obtained by interchanging \(t_2\) and \(t_3\). Direct inversion of \(M\) gives
\[
 M^{-1}(t_1,t_3,t_2)^{\mathsf T}
 =\left(\frac{2m}{3}-c,\ \frac{2m}{3}-b,\ \frac{2m}{3}-a\right)^{\mathsf T}.
\]
Every entry must be a nonnegative integer. Because \(a,b,c\) are integers, integrality is impossible unless \(3\mid m\), which is equivalent to \(3\mid n\). If \(m=3h\), the candidate is \((2h-c,2h-b,2h-a)\) and is admissible exactly when \(\max\{a,b,c\}\le2h\). This transformation is an involution on admissible cyclic triples and sends cyclic rotations of a triple to cyclic rotations of its image. Hence every fiber has at most two necklaces, and outside lengths divisible by three there are no collisions.

**3. Counting the doubletons.** For \(m=3h\), let \(A_h\) be the set of cyclic triples of nonnegative gaps summing to \(3h\) and satisfying the bound \(\max\{a,b,c\}\le2h\). Among ordered triples their number is
\[
 \binom{3h+2}{2}-3\binom{h+1}{2}=3h^2+3h+1.
\]
The three forbidden events \(g_i\ge2h+1\) cannot overlap, which justifies the subtraction. Only the triple \((h,h,h)\) is fixed by a nonidentity cyclic permutation, so Burnside's lemma gives \(\lvert A_h\rvert=(3h^2+3h+1+2)/3=h^2+h+1\).

The involution fixes a cyclic triple precisely when one gap equals \(h\) and the other two sum to \(2h\). Indeed, equality with a cyclic permutation of \((2h-c,2h-b,2h-a)\) is a reflection equation with one fixed coordinate \(h\); the other two are complementary. Every such cyclic orbit has a unique representative with the middle coordinate equal to \(h\), except \((h,h,h)\), which also gives just one orbit. The fixed-orbit count is therefore \(2h+1\). All other orbits of \(A_h\) pair under the involution, giving exactly
\[
 \frac{h^2+h+1-(2h+1)}2=\binom h2
\]
nontrivial two-source fibers.

**4. Counting distinct spectra.** The total number of oriented three-one necklaces follows by applying Burnside's lemma to all nonnegative three-gap triples: it is \(\binom{n-1}{2}/3\) when \(3\nmid n\), and \((\binom{n-1}{2}+2)/3\) when \(3\mid n\). Each doubleton reduces the number of different observations by exactly one. Subtracting the preceding count \(\binom h2\) yields \((h+1)^2=n^2/9\) when \(3\mid n\), and proves the displayed spectrum formula in every case. At \(n=3\) and \(n=6\), the binomial doubleton count is zero as required.

## Verification

Run `python3 verify.py` from the directory containing this document and the verifier. The code independently enumerates all binary necklaces of length up to eighteen with exactly three ones, constructs all cyclic rotations literally, and counts scattered `01` pairs without the gap formula. It checks the polynomial compression identity at all those lengths. Separately, it enumerates all cyclic gap triples through length eighty-four and checks the claimed inverse partner, fiber-size bound, number of doubletons, and number of distinct spectra. Its observed result is:

`VERIFY_OK: independently evaluated 276 binary necklace spectra at n<=18; checked 31780 gap necklaces at n<=84; exact fiber law, direct trace identity, rational partner, and the n=9 example all passed.`

These finite checks are diagnostics, not substitutes for the all-length proof by polynomial cancellation, linear inversion, and Burnside counting.

## Relationship to prior work

Rigo and Salimov introduced binomial equivalence for words and investigated its factor complexity, not the multiset of two-binomial signatures across the rotations of a single finite necklace. Brunetti, Del Lungo and Del Ristoro gave the basic cyclic inversion increment and congruence/equidistribution results; those do not determine when two *different necklaces* have exactly the same complete integer-valued inversion spectrum. The previously published result *Sharp cyclic 2-binomial fingerprint bounds at fixed binary weight* gives the sharp minimum and maximum **number of distinct fingerprints within one necklace's orbit**; it does not determine the inverse fibers of the full multiplicity-valued spectrum. Similarly, the published weight-three three-deck collision classification concerns linear words with their **length-three scattered subsequence counts**, not the rotation-indexed multiset of length-two counts. Their stated conclusions do not imply the theorem's specific partner involution or doubleton census. Searches under inversion spectra, circular binomial equivalence, necklace reconstruction and three-one aliases found no known exact equivalent, but that is not proof of historical priority.

## Limitations

The explicit inverse classification and census are for exactly three ones, though the polynomial-compression method extends algebraically to other weights. At higher weight, the unordered root inversion observations need not determine the gap order up to only two choices. The theorem assumes the observation includes multiplicities from all starting positions. It makes no statement about noisy observation, partial sampling, orientation-free bracelets, or larger scattered-subsequence lengths. The priority assessment is based on accessible published literature and indexed comparisons; an earlier unindexed equivalent may exist. 

## References

- M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013; author preprint publicly available by 2013-05-27, https://orbi.uliege.be/handle/2268/149313 .
- S. Brunetti, A. Del Lungo and F. Del Ristoro, *A cycle lemma for permutation inversions*, Discrete Mathematics **257** (2002), 1–13, https://doi.org/10.1016/S0012-365X(02)00254-6 .
- M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (2020), https://arxiv.org/abs/2001.11732 .
- *Sharp cyclic 2-binomial fingerprint bounds at fixed binary weight*, publicly available mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-cyclic-2-binomial-fingerprint-bounds-at-fixed-binary-weigh--4ff94afd6c61 .
- *All binary three-deck collisions at weight three*, publicly available mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-all-binary-three-deck-collisions-at-weight-three--f95f52cd118b .
