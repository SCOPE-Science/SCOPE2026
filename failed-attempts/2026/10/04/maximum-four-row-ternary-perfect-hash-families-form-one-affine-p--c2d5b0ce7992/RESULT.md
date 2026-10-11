# Maximum four-row ternary perfect hash families form one affine-plane class
## Finding
Let \(C\subseteq\{0,1,2\}^4\) be a set of columns with the perfect-hash property of strength three: for every three distinct columns of \(C\), some coordinate contains all three symbols \(0,1,2\). Then
\[
|C|\le 9.
\]
Equality is attained by
\[
C_0=\{(i,j,i+j,i+2j):i,j\in\mathbb F_3\},
\]
with arithmetic in \(\mathbb F_3\). Moreover, every equality case is equivalent to \(C_0\) under a permutation of the four coordinates and independent permutations of the three symbols in each coordinate. With coordinate positions and symbols labeled, there are exactly \(72\) maximum nine-column sets. The full equivalence group has order \(31{,}104\), the unique maximum orbit has size \(72\), and the stabilizer of a maximum set has order \(432\).

## Assumptions and scope
A ternary \(\operatorname{PHF}(4;k,3,3)\) is represented as a set \(C\subseteq\{0,1,2\}^4\) of \(k\) distinct columns. A triple is separated when one row takes three pairwise distinct symbols on that triple. Equivalence allows arbitrary row permutations and an independent permutation of \(\{0,1,2\}\) in each row; columns are an unordered set. The result is the exact finite four-row, three-symbol, strength-three case and does not assert a formula for larger alphabets or more rows.

## Proof
Take any two distinct columns \(x,y\in C\). Independent symbol permutations normalize \(x\) to \((0,0,0,0)\). After a row permutation, \(y\) becomes \((1,\ldots,1,0,\ldots,0)\), with exactly \(d=d_H(x,y)\) initial ones, where \(1\le d\le4\).

For each \(d\), enumerate all ternary columns \(z\) for which the triple \(\{x,y,z\}\) is separated, and perform a complete include/exclude search subject to separation of every triple. The four normalized cases contain respectively \(27,45,57,65\) candidate third columns. The exhaustive search visits respectively \(155,774,282,1610\) recursion nodes and proves that a nine-column family containing \(x,y\) exists exactly when \(d=3\). Thus, in any family of size at least nine, every pair of columns has Hamming distance exactly \(3\).

Now project such a family onto any two coordinates. If two columns had the same projection, they would agree in those two coordinates and hence have Hamming distance at most \(2\), impossible. Therefore every two-coordinate projection is injective into the \(3^2=9\) ordered symbol pairs. Hence \(|C|\le9\). A direct affine-plane check, replayed by `verify.py`, shows that every triple of the displayed set \(C_0\) is separated, so equality is attained.

For \(|C|=9\), projection onto the first two coordinates is bijective. Hence the columns can be written uniquely as
\[
(i,j,L_1(i,j),L_2(i,j)),\qquad i,j\in\mathbb F_3.
\]
Pairwise distance \(3\) forces each \(L_r\) to be a Latin square of order three, while the pair \((L_1,L_2)\) is orthogonal. There are exactly \(12\) Latin squares of order three and \(72\) ordered orthogonal pairs. Direct enumeration of these pairs yields \(72\) distinct labeled nine-column sets. Independently applying all \(24\cdot6^4=31{,}104\) allowed row/symbol transformations to \(C_0\) produces exactly the same \(72\) sets. Therefore all maxima form one equivalence class, and orbit-stabilizer gives stabilizer order \(31{,}104/72=432\).

## Verification
Run `python verify.py`. The verifier constructs all \(81\) ternary four-tuples, replays the complete normalized-pair searches, enumerates all order-three Latin squares and ordered orthogonal pairs, and traverses the full equivalence group. Its terminal certificate is:

`VERIFY_OK maximum=9 labeled_maxima=72 orbits=1 stabilizer=432 pair_distance=3`

The file `certificate.json` records the exact case counts and verifier output. No timeout, randomized search, or external solver is used.

## Relationship to prior work
Bshouty's 2014 perfect-hash-family work supplies an archive-era algorithms-and-complexity source for the standard object. Walker and Colbourn's construction survey gives a \(\operatorname{PHF}(4;9,3,3)\) among the best families found for these parameters, and an earlier design-theoretic treatment obtains the same parameters from the affine plane of order three. The inspected sources provide the nine-column construction, but not the no-ten upper bound, the forced distance-three structure, the exact count of labeled maxima, or the one-orbit classification proved here.

## Limitations
The classification is finite and parameter-specific. Its universal content is only for four rows over a ternary alphabet at strength three. The originality search cannot exclude an unindexed or differently phrased small-parameter classification in older design literature; this remains the main literature risk. The proof itself is self-contained once the four finite normalized-pair searches are replayed.

## References
1. N. H. Bshouty, *Linear time Constructions of some d-Restriction Problems*, arXiv:1406.2108v1, first public version 2014-06-09.
2. R. A. R. Walker and C. J. Colbourn, *Perfect Hash Families: Constructions and Existence*, Journal of Mathematical Cryptology 1 (2007), DOI:10.1515/JMC.2007.008.
3. Waterloo thesis treatment of affine-plane perfect hash families, Example giving \(\operatorname{PHF}(4;9,3,3)\) from the affine plane of order three.
