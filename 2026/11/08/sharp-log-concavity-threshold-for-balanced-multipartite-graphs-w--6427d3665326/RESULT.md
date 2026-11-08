# Sharp log-concavity threshold for balanced multipartite graphs with five vertices per part

## Finding
For every integer \(t\ge2\), let \(G_t=K_{5,\ldots,5}\) be the complete \(t\)-partite graph with five vertices in each part. Let \(\psi(G_t;z)=\sum_{k=0}^{\max\{5,t\}}a_k(t)z^k\) count general-position vertex sets by size. Then its entire positive coefficient sequence is **strictly log-concave if and only if \(t\ge4\)**. For every \(t\ge2\), including the two exceptional non-log-concave cases, that sequence is unimodal.

More explicitly, for \(t=2\), log-concavity fails at index \(3\) with defect \(a_3^2-a_2a_4=-50\). For \(t=3\), it fails at index \(4\) with defect \(a_4^2-a_3a_5=-240\). For every \(t\ge4\), all interior defects are strictly positive.

This determines the first previously unclassified part size immediately beyond the \(1\)-through-\(4\)-vertex-part theorem of Rather (2026), which explicitly asks for a finer classification of the part-size/number-of-parts log-concavity region.

## Assumptions and scope
All graphs are finite, simple, connected and undirected. A set \(S\subseteq V(G)\) is in *general position* if no three distinct vertices of \(S\) have one lying on a shortest path joining the other two. The coefficient \(a_k(t)\) is the number of such sets of cardinality \(k\), with \(a_k(t)=0\) for \(k<0\) or \(k>\max\{5,t\}\). Strict log-concavity means \(a_k(t)^2>a_{k-1}(t)a_{k+1}(t)\) for every interior index \(1\le k<\max\{5,t\}\).

For integer \(t\ge2\), with binomial coefficients outside their ordinary range interpreted as zero, the full coefficient formula is
\[
a_0(t)=1,\qquad a_1(t)=5t,\qquad
 a_k(t)=5^k\binom tk+t\binom5k\quad(k\ge2).
\]
The formula is restated for context, not claimed as new: it appears in the motivating source's complete-multipartite enumeration.

## Proof
**General-position structure and coefficient formula.** Two vertices in one part have distance two, and every vertex outside that part forms the middle of a length-two geodesic between them. Hence a general-position set that contains two vertices of one part cannot contain a vertex of any other part. Conversely, any set entirely within one part and any set having at most one vertex from each part are in general position. For size at least two these two types are disjoint and counted, respectively, by \(t\binom5k\) and \(5^k\binom tk\). Singletons and the empty set are counted separately as above.

**Exact positivity certificates.** Put \(D_k(t)=a_k(t)^2-a_{k-1}(t)a_{k+1}(t)\). Direct expansion gives
\[
D_1(t)=\frac{5t(5t+1)}2>0.
\]
For each of \(k=2,3,4,5\), set \(u=t-4\). The following table is an exact polynomial identity
\[
D_k(t)=t^2\lambda_k\sum_{j=0}^{d_k}c_{k,j}u^j.
\]
The displayed lists consist of the integer coefficients \((c_{k,0},\ldots,c_{k,d_k})\) in **ascending** order of exponent:

| \(k\) | \(\lambda_k\) | \((c_{k,0},\ldots,c_{k,d_k})\) |
|---|---|---|
| 2 | \(25/12\) | \((759,320,25)\) |
| 3 | \(25/144\) | \((60858,72015,31525,6625,625)\) |
| 4 | \(5/576\) | \((2979828,8200500,8925725,5037500,1563750,250000,15625)\) |
| 5 | \(1/3456\) | \((3456,73642500,275730000,427720625,354945625,169156250,46093750,6640625,390625)\) |

All entries are strictly positive. Thus \(D_k(t)>0\) for \(2\le k\le5\) whenever \(t\ge4\) and the index is interior. For \(k=6\) and \(t\ge6\), set \(v=t-6\). A separate exact identity is
\[
D_6(t)=\frac{15625t^2}{145152}\sum_{j=0}^{10}b_jv^j,
\]
where
\[
(b_0,\ldots,b_{10})=(63000000,233682720,372068044,337220100,193569635,73775340,18954231,3247500,355625,22500,625).
\]
Again all coefficients are strictly positive. This establishes positivity at index six whenever the index is interior (which requires \(t\ge7\)). Finally, for every \(k\ge7\), the three consecutive coefficients at indices \(k-1,k,k+1\) are exactly \(5^{k-1}\binom t{k-1}\), \(5^k\binom tk\), and \(5^{k+1}\binom t{k+1}\). Their strict log-concavity at any interior index follows from the strict log-concavity of binomial coefficients in their positive range.

The displayed identities follow by substituting the coefficient formula and expanding the falling-factorial polynomials \(\binom tk=t(t-1)\cdots(t-k+1)/k!\). The included standalone standard-library verifier checks these as **exact polynomial identities** in the indeterminate \(t\), not merely at sampled integer values. Taken with \(D_1(t)>0\), they show strict log-concavity for every \(t\ge4\).

**Sharpness and unimodality.** At \(t=2\) the coefficient sequence is \((1,10,45,20,10,2)\), and \(20^2-45\cdot10=-50\). At \(t=3\) the sequence is \((1,15,105,155,15,3)\), and \(15^2-155\cdot3=-240\). Neither sequence is log-concave, but both visibly rise and then fall. For \(t\ge4\), every coefficient between degrees zero and \(\max\{5,t\}\) is positive, so strict log-concavity implies unimodality. This proves both assertions for every integer \(t\ge2\).

## Verification
Run `python3 verify.py` using Python 3 and only its standard library. The verifier constructs the binomial/falling-factorial polynomials by exact rational polynomial arithmetic, checks the identity for every displayed positivity coefficient, checks boundary failures, and separately enumerates all vertex subsets and tests shortest-path triples on the graphs with \(t=2,3\). It additionally checks log-concavity numerically for all integer \(4\le t\le200\); those finite spot checks are not used to justify the infinite theorem. Its expected final line is `VERIFY_OK`.

## Relationship to prior work
Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930, establishes the coefficient formula for arbitrary balanced complete multipartite graphs and proves log-concavity for part sizes at most four. It exhibits failure for \(K_{5,5}\), without resolving the parameter line of five-vertex parts; in Section 4 it explicitly identifies precise classification of part-size/part-count pairs as a future problem. The present result establishes that complete line, including the second exceptional part count and the sharp threshold at four parts. Iršič, Klavžar, Rus and Tuite, *General Position Polynomials* (2024), introduces the polynomial and addresses numerous graph families, including nonunimodal complete bipartite examples, but not this five-vertex-part threshold.

Related indexed findings concern spiders, complete-graph coronas, generalized windmills, and **dual** general-position variants on complete multipartite graphs. Different graph families or a different position predicate do not imply this ordinary-polynomial log-concavity cutoff. The source comparisons support provisional originality rather than exhaustive historical priority.

## Limitations
This is an exact statement for equal part size five and an arbitrary integer number of parts at least two, not a classification for other part sizes or unequal parts. The coefficient formula is previously known; the new content is the sharp strict-log-concavity threshold and the all-part-count unimodality consequence. The positivity certificate and exhaustive small-graph verification were checked in the same review process; no independent mathematical audit has been performed. As with any literature search, unindexed or inaccessible historical work may remain.

## References
1. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930, first submitted 2026-03-06, Sections 3–4. https://arxiv.org/abs/2603.06930 and https://arxiv.org/pdf/2603.06930
2. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics 79, article 110 (2024). https://doi.org/10.1007/s00025-024-02133-3
