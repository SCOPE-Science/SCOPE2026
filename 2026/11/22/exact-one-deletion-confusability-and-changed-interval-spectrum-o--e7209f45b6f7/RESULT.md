# Exact one-deletion confusability and changed-interval spectrum of Kautz words

## Finding
Let \(q\ge 2\) and \(n\ge 1\) be integers. Let \(\Sigma\) be a labeled alphabet of \(q\) symbols, and let \(K_{q,n}\) comprise the length-\(n\) words in which consecutive symbols are unequal. Form an **undirected single-deletion confusability graph** \(G_{q,n}\): its vertices are \(K_{q,n}\), and distinct words are adjacent if deleting exactly one (arbitrary) symbol from each produces a common length-\(n-1\) word. The received word need not satisfy the adjacent-unequal constraint.

The number of unordered confusable pairs is exactly
\[
|E(G_{q,n})|=\frac{q(q-1)^{n-2}}{2}\bigl(n^2(q-2)^2+3n(q-2)-(q-3)\bigr).
\]
This expression also applies at \(n=1\), with \((q-1)^{-1}\) interpreted in the ordinary rational sense. Equivalently, the generating function with zero constant coefficient is
\[
\sum_{n\ge1}|E(G_{q,n})|z^n=\frac{q(q-1)z(1-z)(1+(q-3)z)}{2(1-(q-1)z)^3}.
\]

A stronger *location-resolved* assertion holds. Fix nonnegative integers \(a,b\) and a positive integer \(L\) such that \(a+L+b=n\). Let \(E_{a,L,b}\) be the number of edges for which the first and last differing positions are \(a+1\) and \(a+L\). Put \(C_0=1\) and, for \(t\ge1\),
\[
C_t=(q-2)(q-1)^{t-1}.
\]
Then
\[
E_{a,1,b}=\frac{q(q-1)}2 C_a C_b,\qquad
E_{a,L,b}=\left(q(q-1)^L-\frac{q(q-1)}2\right)C_aC_b\quad(L\ge2).
\]
In particular, the mean vertex degree is exactly
\[
\overline d(G_{q,n})=\frac{n^2(q-2)^2+3n(q-2)-(q-3)}{q-1}.
\]
The elementary average-degree bound for independent sets also gives the explicit, generally nonsharp, guaranteed one-deletion code size
\[
A_1(q,n)\ge \left\lceil\frac{q(q-1)^n}{n^2(q-2)^2+3n(q-2)+2}\right\rceil.
\]
For \(q=2\) the graph is a single edge at every length. For fixed \(q\ge3\), the mean degree is quadratic in \(n\), with leading coefficient \((q-2)^2/(q-1)\).

## Assumptions and scope
All words are **linear**, not cyclic. Their symbols are ordered and drawn from a common labeled alphabet. The adjacency constraint is imposed only on transmitted words. The channel deletes *exactly one* symbol, at any position, without revealing the position. Two distinct inputs are confusable when their sets of deletion descendants intersect; distinct deletion choices giving the same descendant do not create multiple graph edges. Confusability is not ordinary Kautz shift-graph adjacency. This study counts pairs; it does not determine maximum independent-set (codebook) sizes.

## Proof
**1. Canonical unequal interval.** If distinct equal-length words \(x\) and \(y\) share a one-deletion descendant, take the first and last positions \(i\le j\) at which they differ. If a common descendant comes from deleting the same position from both, then \(i=j\). Otherwise, if the deletion in \(x\) precedes the deletion in \(y\), equality of the remaining words gives a left-shift condition on the interval between the deletions. Whenever the original left deletion precedes \(i\), agreement of the two words forces a constant segment, so that deletion may be shifted to \(i\) without changing its descendant. The analogous right deletion may be shifted to \(j\). Therefore one of the two conditions
\[
y_i\cdots y_{j-1}=x_{i+1}\cdots x_j,\qquad
x_i\cdots x_{j-1}=y_{i+1}\cdots y_j
\]
holds for \(i<j\), with equality of \(x\) and \(y\) outside \([i,j]\). Conversely, either condition produces a common descendant by deleting the left endpoint from one word and the right endpoint from the other. For \(i=j\), any two distinct letters at position \(i\) suffice.

**2. Boundary factors.** In every case \(x_i\ne y_i\) and \(x_j\ne y_j\). To retain the adjacent-unequal constraint in both words, a shared nonempty prefix before \(i\) must end in a letter distinct from both unequal symbols at \(i\). For prefix length \(a\), there are \(C_a\) possibilities: first select its last letter from \(q-2\) choices, then choose preceding letters from \(q-1\) choices apiece. A shared suffix of length \(b\) has independently \(C_b\) possibilities. Empty boundaries contribute one. Thus the boundary count is \(C_aC_b\).

**3. One-position differences.** If \(L=1\), the changed pair of symbols has \(\binom q2=q(q-1)/2\) unordered choices. Multiplying the boundary factors gives the claimed \(E_{a,1,b}\).

**4. Larger unequal intervals and their sole double count.** Let \(L\ge2\). Count *oriented left-shift realizations* with \(y_i\cdots y_{j-1}=x_{i+1}\cdots x_j\). The length-\(L\) block of \(x\) is adjacent-unequal, hence has \(q(q-1)^{L-1}\) choices. The last symbol \(y_j\) can be any of \(q-1\) symbols distinct from \(x_j\); this both enforces the last difference and makes the adjacent pair \(y_{j-1}y_j\) valid. The first difference follows from \(x_i\ne x_{i+1}\). So there are \(q(q-1)^L C_aC_b\) oriented realizations.

An unordered edge is represented once unless both opposite shift conditions hold. If both do, the two conditions imply \(x_k=x_{k+2}\) for each \(i\le k\le j-2\), so \(x_i\cdots x_j\) alternates between two different letters; the last symbol of \(y\) is then forced to be the opposite alternating phase. Conversely, every such opposite-phase alternating pair supports both shifts. There are \(q(q-1)C_aC_b\) oriented double-mode realizations, representing \(q(q-1)C_aC_b/2\) unordered pairs. Subtracting this duplication once gives
\[
E_{a,L,b}=\left(q(q-1)^L-\frac{q(q-1)}2\right)C_aC_b.
\]
There is no other duplication because \(i,j\) are the intrinsic first and last differing positions.

**5. Summation.** The boundary generating function is
\[
C(z)=\sum_{t\ge0}C_tz^t=1+\frac{(q-2)z}{1-(q-1)z}=\frac{1-z}{1-(q-1)z}.
\]
Summing the span spectrum over all \(a,b,L\) gives
\[
\sum_{n\ge1}|E(G_{q,n})|z^n=C(z)^2\left(\frac{q(q-1)}2z+\frac{q(q-1)^2z^2}{1-(q-1)z}-\frac{q(q-1)z^2}{2(1-z)}\right).
\]
Elementary cancellation yields the rational function in the finding. Its coefficient is the displayed all-length formula. Since \(|K_{q,n}|=q(q-1)^{n-1}\), dividing twice the edge count by the vertex count gives the mean-degree formula. All steps remain valid when \(q=2\); the boundary factor vanishes for every nonempty boundary, leaving one confusable pair.

## Verification
Two supplied Python 3 standard-library programs are reproducible independently of symbolic software:

- `python3 verify/direct_deletion_graph.py` enumerates every allowed word, constructs its deletion-descendant set directly, compares all unordered pairs, and checks **each** \((a,L,b)\) cell, not just total counts. It checks 24 parameter cases: \(q=2\) through \(n=8\); \(q=3\) through \(n=7\); \(q=4\) through \(n=5\); and \(q=5\) through \(n=4\).
- `python3 verify/interval_construction.py` generates the candidate edges from literal changed-interval operations without making deletion-shadow sets, checks their total counts for \(q=2,3,4,5\) and the stated lengths, and confirms that any doubled orientation has a fully alternating differing interval.

Both programs completed successfully. Sample counts \((q,n,|K_{q,n}|,|E|)\) are \((2,6,2,1)\), \((3,4,24,168)\), \((3,6,96,1296)\), \((4,4,108,1566)\), and \((5,4,320,7120)\). Their finite checks are diagnostic; the all-parameter result follows from the symbolic proof above.

## Relationship to prior work
Kulkarni and Kiyavash (first preprint 2012-11-13) developed upper bounds for deletion-correcting codes on constrained sources, including **binary** run-length restrictions. Cullina, Kulkarni and Kiyavash (first preprint 2012-11-16) gave the general deletion-confusability graph formulation and average-degree *bounds* in the unrestricted binary setting. Neither of those inspected arguments states the exact induced one-deletion edge law for the adjacent-unequal \(q\)-ary language, or its changed-interval distribution. A Kautz graph uses the same admissible word labels but shift arcs, which are a different edge relation. Existing two-read deletion-reconstruction graphs require *two distinct* common reads and are strictly different from the one-read collision relation here. The present derivation provides the induced graph's exact edge and mean-degree counts; these do not follow merely by restricting an unrestricted total-edge count or a code-size bound.

## Limitations
No exact maximum single-deletion-correcting code size, maximum-degree spectrum, or independent validation is claimed. Priority against unindexed or inaccessible earlier work is not settled. The structural proof and finite verifications concern exactly one deletion and adjacent-unequal **linear** transmitted words, not circular words, substitutions, or two deletions. The simplicity of the final rational function does not make it a direct corollary of the inspected general deletion-code bounds; nonetheless it may admit other unlocated derivations.

## References
1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, submitted 2012-11-13. https://arxiv.org/abs/1211.3128
2. D. Cullina, A. A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056, submitted 2012-11-16. https://arxiv.org/abs/1211.4056
3. SageMath, *Common digraphs: Kautz digraph*, reference documentation (word-label convention and shift-arc definition). https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/digraph_generators.html
