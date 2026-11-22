# The two-path parity criterion and final shattering coefficient for even derangements

## Finding

For each integer \(n\ge4\), put \(X_n=\{(i,j)\in[n]^2:i\ne j\}\), and let \(\mathcal E_n\) consist of the incidence sets \(\{(i,\pi(i)):i\in[n]\}\) of all **even, fixed-point-free** permutations \(\pi\) of \([n]\). Every Boolean query asks whether the corresponding off-diagonal assignment cell occurs. The **new result** is the sharp criterion at size \(n-2\), the last possible shattered-support rank, and its previously undetermined exact coefficient. For clarity, the entire family is stated below: the smaller-rank cases and the dimension had already been established in a preceding near-top analysis, while the rank-\(n-2\) theorem completes the classification.

A nonempty support must be a partial permutation (a set of cells with pairwise distinct first coordinates and pairwise distinct second coordinates). Regard its cells as arcs \(i\to j\) on \([n]\). Because loops are absent, its components are directed paths, including singleton paths, and directed cycles of lengths at least two. A support with \(k\) arcs has exactly \(n-k\) path components; write \(c\) for its number of cycle components.

1. Every partial permutation of size at most \(n-4\) is shattered.
2. At size \(n-3\), precisely those supports are **not** shattered that consist of three singleton paths together with an **odd** derangement on their complementary \(n-3\) labels. Equivalently, the only failures have three singleton paths and even \(n-c\).
3. At size \(n-2\), let the two path components have vertex lengths \(a\le b\). The support is shattered **if and only if**
   \[
   (a,b)\ne(1,1)\quad\text{and}\quad
   \bigl(a\ge3\ \text{or}\ n-c\text{ is odd}\bigr).
   \]
4. No support of size \(n-1\) or more is shattered.

For context, the previously known dimension, with the direct four-symbol boundary, is
\[
\operatorname{VCdim}(\mathcal E_4)=1,\qquad
\operatorname{VCdim}(\mathcal E_n)=n-2\quad(n\ge5).
\]

Combining the new rank-\(n-2\) count with the previously established lower-rank results gives the **entire** shattered-support polynomial. Define
\[
R_{n,k}=\sum_{j=0}^k(-1)^j\binom nj\binom{n-j}{k-j}^{\!2}(k-j)!,
\qquad 0\le k\le n,
\]
the ordinary off-diagonal rook numbers; let \(D_{m,c}\) be the number of permutations on \(m\) labels with precisely \(c\) cycles, all of length at least two, with \(D_{0,0}=1\) and other impossible indices zero. Define
\[
T_n=\frac{n!}{2}\sum_{\substack{a,b\ge1\\m=n-a-b\ge0}}\frac1{m!}
\sum_{c=0}^{m}D_{m,c}\,
\mathbf1_{\{(a,b)\ne(1,1)\}}
\mathbf1_{\{\min(a,b)\ge3\ \text{or}\ n-c\text{ odd}\}}.
\]
The first indicator excludes two singleton paths; the second requires two path lengths at least three, or an odd value of \(n-c\). Then
\[
\boxed{\displaystyle
\Phi_n(z)=\sum_{k=0}^{n-4}R_{n,k}z^k
+\left(R_{n,n-3}-\binom n3D^-_{n-3}\right)z^{n-3}
+T_nz^{n-2},}
\]
where \(D^-_m=\sum_{c:(m-c)\text{ odd}}D_{m,c}\) counts odd derangements of \(m\) labels. In particular, the first nontrivial polynomials are
\[
\Phi_4(z)=1+12z,\quad
\Phi_5(z)=1+20z+120z^2+240z^3,
\]
\[
\Phi_6(z)=1+30z+315z^2+1420z^3+1140z^4.
\]
For reproducibility, the cycle-refined integers satisfy the finite recurrence
\[
D_{m,c}=\sum_{\ell=2}^{m}\binom{m-1}{\ell-1}(\ell-1)!D_{m-\ell,c-1}.
\]
Equivalently, with \(P(x)=x/(1-x)\), \(Q(x)=x^3/(1-x)\), and \(C(x)=-\log(1-x)-x\), the top coefficient has the exponential generating expression
\[
T_n=\frac{n!}{2}[x^n]Q(x)^2e^{C(x)}
+\frac{n!}{4}[x^n]\bigl(P(x)^2-Q(x)^2-x^2\bigr)
\bigl(e^{C(x)}-(-1)^n e^{-C(x)}\bigr).
\]
The correction is not simply halving the unrestricted count: at order six it retains \(1140\) of \(2715\) top-dimensional partial matchings, whereas at order seven it retains \(15750\) of \(25494\).

## Assumptions and scope

The two copies of \([n]\) are distinguished as row and column coordinates; the parity of a permutation is the parity of its inversion number. Each concept is a full fixed-point-free permutation, not a partial matching. A support is shattered only when **every** labeling, including the all-positive and all-negative labelings, can be realized by an even derangement. All cells in a support are distinct, and all vertices of a directed component are labeled. Singleton paths are isolated vertices. The conclusions concern all integers \(n\ge4\); no statement about the empty even-derangement class at order two is needed. Formula coefficients count labeled supports, not graph-isomorphism types.

## Proof

**1. Completion of directed partial permutations.** Any partial permutation \(S\subseteq X_n\) decomposes into directed cycles and paths, because its directed indegree and outdegree are at most one. A directed cycle is already a complete cycle of any extending permutation. A path has one terminal vertex with no outgoing arc and one initial vertex with no incoming arc. Completing the support to a permutation is equivalent to bijectively matching the path terminals to path initials; this is a permutation \(\sigma\) of the path components. A singleton path may not be fixed by \(\sigma\), because that would introduce a forbidden fixed point. Every other path can be closed, and every nontrivial cycle of \(\sigma\) joins paths into a larger directed cycle. If the original support has \(c\) complete cycles and \(\sigma\) has \(t\) cycles, the resulting full permutation has exactly \(c+t\) cycles and therefore sign \((-1)^{n-c-t}\). This is valid even when some paths have one vertex.

**2. Parity-robust completion with four spare assignments.** Let \(S\) be a partial permutation with \(|S|\le n-2\), and choose a desired set \(A\subseteq S\) of positive cells. If \(|A|\le n-4\), there are \(r=n-|A|\ge4\) unassigned rows and columns. Forbid the residual diagonal matching, and also the cells of \(S\setminus A\), a second residual matching of size at most \(|S|-|A|\le r-2\). We claim that the residual board has perfect matchings of **both** parities. The parity of the combined permutation differs from the residual matching parity by a fixed sign, so a completion of even total parity exists.

For \(r\ge6\), each residual row and column has at least \(r-2\) allowed neighbors. Any two rows share at least \(r-4\ge2\) allowed columns. Choose two common columns. Upon removing these two rows and two columns, the remaining \((r-2)\)-by-\((r-2)\) bipartite graph has minimum degree at least \(r-4\ge(r-2)/2\), so Hall's theorem supplies a perfect matching. In the original graph, the chosen two rows can be matched to their two common columns in both orders; the two completions differ by a transposition and hence have opposite parity.

For \(r=5\), extend both forbidden partial matchings to full matchings, put the first on the diagonal by relabeling columns, and let the other be the graph of \(\tau\in\mathfrak S_5\). Direct enumeration of the seven cycle types of \(\tau\), namely \((1^5),(2,1^3),(3,1^2),(2^2,1),(4,1),(3,2),(5)\), gives respectively \((24,20),(12,12),(12,7),(8,8),(8,8),(6,6),(8,5)\) allowed even/odd permutation pairs. Every pair has both entries positive. A relabeling may interchange which residual parity is called even, but cannot remove either. Deleting fewer forbidden cells can only increase the available matchings.

For \(r=4\), there are at most two cells in the second forbidden matching. Extend the diagonal matching to a full matching and normalize it to the identity. Its complement has three even derangements (the three double transpositions) and six odd derangements (the six four-cycles). Each off-diagonal cell occurs in exactly one of these even derangements and in exactly two of the odd derangements. Forbidding at most two more cells therefore leaves at least one even and at least two odd residual perfect matchings. This establishes the claim at every \(r\ge4\), independent of the positions of the prescribed positive cells.

It follows at once that every matching support of size at most \(n-4\) is shattered. At the next two ranks, **only** labelings with \(n-3\) or \(n-2\) positive cells can possibly fail.

**3. The three-path rank.** If \(|S|=n-3\), the support has three paths. Only the all-positive labeling has more than \(n-4\) positives. A three-cycle on its three paths always gives a valid derangement completion, with one added cycle. If at least one path is nontrivial, a transposition of the other two paths fixing that nontrivial path gives a second valid completion with two added cycles. These completions have opposite permutation parities, so the all-positive labeling is realizable by an even derangement.

If all three paths are singleton vertices, the only permitted path permutations are the two three-cycles; both have one cycle. The all-positive labeling has even completion exactly when \(n-c-1\) is even, equivalently when \(n-c\) is odd. The already completed cycles then form an odd derangement precisely in the failing case. This reconstructs the already known rank-\(n-3\) criterion, which is included so that the new top-rank proof is self-contained.

**4. The two-path rank.** Let \(|S|=n-2\). Its two paths have lengths \(a\le b\), and it has \(c\) completed cycles. The all-positive labeling always admits the cross-joining completion, with one added cycle. If both paths are nontrivial, their separate closure is also valid and has two added cycles, giving both parities. If at least one path is singleton, the cross-joining completion is the only possible one; it is even exactly when \(n-c\) is odd.

For a labeling with exactly one negative cell \(e\in S\), there are three paths after removing \(e\) from the forced positive set. A three-cycle on these paths, chosen so that it does not restore the forbidden arc \(e\), always exists and has one added cycle.

If \(e\) lies on one of the original directed cycles, removing it turns that cycle into a nontrivial third path. The original arc \(e\) would be restored by fixing this third path, so such a fixed point of the path permutation is forbidden. A transposition fixing either original nontrivial path is nevertheless valid; it supplies the opposite parity. Thus both parities are available unless **both** original paths are singleton. In that exceptional case, only three-cycles can complete the three paths, and the resulting sign is \((-1)^{n-c}\) because the broken cycle decreases the original cycle count by one. If \(a=b=1\), the all-positive requirement instead needs \((-1)^{n-c-1}=+1\); the two requirements contradict one another. Since \(n\ge4\), these two singleton paths necessarily coexist with at least one directed cycle. Therefore no support with \((a,b)=(1,1)\) is shattered.

If \(e\) lies in one of the original paths, removing it splits that path into two paths \(A,B\) of positive vertex lengths, with \(e\) joining the terminal of \(A\) to the initial of \(B\). The third path \(C\) is the other original path. A path-permutation three-cycle sending \(A\to C\to B\to A\) avoids \(e\) and has one added cycle. If \(A\) or \(B\) is nontrivial, a transposition fixing that component and exchanging the other two is also valid and has two added cycles, giving both parities. When \(A\) and \(B\) are singletons, \(e\) was the *only* edge of a two-vertex path. No transposition can be used: the transposition fixing \(A\) or \(B\) would create a fixed point on a singleton, and the transposition fixing \(C\) would restore \(e\). Every admissible completion thus has one added cycle, with even sign precisely when \(n-c\) is odd.

All remaining labelings have at most \(n-4\) positives and work by Step 2. Combining the all-positive test and the one-negative tests proves the NEW rank-\(n-2\) criterion: two singleton paths never shatter; if either path has length one or two (but not both length one), parity \(n-c\) must be odd; if both lengths are at least three, all labelings work.

**5. Upper bound, dimension, and existence.** The all-positive labeling forces every shattered support to be a partial permutation. A support of size \(n-1\) cannot be shattered even by *all* derangements: if its unique unused row and column agree, its all-positive labeling cannot be completed; otherwise, omitting its edge whose row equals the unused column while keeping all other support edges positive forces either that omitted edge or a diagonal fixed point. This two-row obstruction is independent of permutation parity. Heredity rules out larger supports.

The top coefficient is positive for all \(n\ge5\). If \(n\ge5\) is odd, start with the single directed \(n\)-cycle and delete two arcs separated so that the resulting path lengths are \((n-1)/2\) and \((n+1)/2\). For \(n=5\), their lengths are two and three and \(n-c\) is odd; for \(n\ge7\), both lengths are at least three. If \(n\ge6\) is even, start with a disjoint three-cycle and \((n-3)\)-cycle and delete two consecutive arcs from the three-cycle. The resulting paths have lengths one and two and \(c=1\), so \(n-c\) is odd. Both constructions meet the top-rank shattering criterion. When \(n=4\), the two-path criterion admits no shattered rank-two support, while all single cells are shattered. This re-establishes the dimension statement for completeness; it is not claimed new.

**6. Exact enumeration.** There are \(R_{n,k}\) size-\(k\) partial permutations with no diagonal cells, by elementary rook inclusion-exclusion. At size \(n-3\), a failure is determined uniquely by the choice of three singleton labels and an odd derangement of the other \(n-3\) labels. Hence exactly \(\binom n3D^-_{n-3}\) supports must be subtracted, as already determined in the prior near-top classification.

At size \(n-2\), the partial functional digraph has exactly two unlabeled directed path components, of lengths \(a,b\ge1\), and an arbitrary collection of \(c\) directed cycles of lengths at least two on the other \(m=n-a-b\) labels. For ordered path components, the number of arrangements is \(n!D_{m,c}/m!\), independent of the individual path lengths, because each path has as many linear orders as the factorial of its vertex count. Divide by two for the unordered pair. Filtering these arrangements by the two-path criterion gives precisely \(T_n\). The recurrence for \(D_{m,c}\) follows by choosing the directed cycle containing one distinguished label, its other \(\ell-1\) labels and their cyclic ordering. Equivalently, the exponential generating function of derangement cycles is \(\exp(uC(x))\), and the functions \(P,Q\) enumerate paths of lengths at least one or three; filtering the cycle-count parity gives the displayed second expression for \(T_n\). Thus every coefficient is established for every \(n\ge4\).

## Verification

Run `python3 verify_even_derangements.py` using Python 3 without third-party dependencies. It exhaustively tests all 52,160 off-diagonal partial-permutation supports through seven labels against the **actual traces** of all even derangements, including all Boolean labels. It checks the independent rook-number and directed-cycle recurrences, produces coefficients through fourteen labels, checks all 55 critical four-row forbidden configurations and 120 five-row full-matching deletion configurations, and supplies concrete even-derangement completions for the constructed extremal supports through fourteen labels. It reproduces the previously available order-six finite coefficient sequence without treating it as proof of higher orders. The proof above, including the four-spare lemma and the three-path completion analysis, is the all-order argument.

## Relationship to prior work

Chase and Freitag (2018) establish the foundational link between Boolean concept-class VC dimension, model theory and learnability; their abstract framework specifies neither fixed-point-free permutation concepts nor even-permutation incidence traces. Bucić, Devlin, Hendon, Horne and Lund (2019) study intersecting perfect matchings and graph derangements; their Theorems 1–7 concern matching intersection proportions and graph-based counting, not incidence shattering by **even** derangements. Alexandersson and Kebede (2021) study sign imbalance and excedance statistics of even/odd derangements, not Boolean traces. Plantholt, Habibi and Mussell (2022) study avoidance of a forbidden functional assignment and asymptotic counts, not parity-constrained trace realization.

The published *Perfect-matching trace universality and the shattering polynomial of derangements* (2026) proves that **unrestricted** derangements shatter exactly the off-diagonal partial permutations of size at most \(n-2\); the present parity restriction is a strict subclass and changes the coefficients at two critical ranks, so the earlier unrestricted theorem supplies an upper bound but not the claimed parity classification. A prior finite treatment, *A nonpure shattering complex for even derangements on six symbols*, supplies the six-letter polynomial and finite topology. That case is an explicitly credited **special case**, not the new claim. The preceding analysis *Parity-exceptional near-top shattering of even derangements* (2026) already established all coefficients through rank \(n-3\) and the VC dimension for \(n\ge5\), but explicitly left the rank-\(n-2\) coefficient open. The present contribution is the previously missing all-order **two-path top-rank criterion and exact top coefficient**, yielding the complete polynomial when combined with that prior classification. Its lower ranks are not reasserted as novel. The comparison-query theorem for even permutation words addresses a different query domain (order comparisons rather than row–image membership), and its forest criterion does not imply the current one. The classical derangement rook numbers and signed derangement counts are used as established ingredients, not rebranded as new theorems.

## Limitations

Only ordinary (static) Boolean VC shattering is addressed; no exact adaptive/Littlestone dimension or shattering-complex homotopy type is asserted. The result depends on the diagonal being the only globally prohibited matching and on the even sign condition; arbitrary bipartite matching boards and other permutation subgroups may behave differently. The lower-rank coefficients, including the parity-sensitive rank-\(n-3\) correction, are covered by preceding work. The previously unclassified highest rank requires the new two-path parity proof and exact counting expression. The computational checks end at the stated finite boundaries and do not substitute for the universal argument. Publication priority under alternative terminology is not independently certified.

## References

1. H. Chase and J. Freitag, *Model Theory and Machine Learning*, first public January 19, 2018, arXiv:1801.06566v1; arXiv lists MSC 03C95, 03C98, 03C45. https://arxiv.org/html/1801.06566v1
2. M. Bucić, P. Devlin, M. Hendon, D. Horne and B. Lund, *Perfect matchings and derangements on graphs*, first public June 13, 2019, arXiv:1906.05908v1. https://arxiv.org/html/1906.05908v2
3. P. Alexandersson and F. G. Kebede, *An involution on derangements preserving excedances and right-to-left minima*, first public May 18, 2021, arXiv:2105.08455v1. https://arxiv.org/abs/2105.08455
4. M. Plantholt, H. Habibi and B. Mussell, *On f-Derangements and Decomposing Bipartite Graphs into Paths*, first public January 7, 2022, arXiv:2201.02332v1. https://arxiv.org/abs/2201.02332
5. *Perfect-matching trace universality and the shattering polynomial of derangements*, public result dated November 8, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-perfect-matching-trace-universality-and-the-shattering-polynomia--d84d57a040aa/RESULT.md
6. *Derangement incidence shattering: exact static dimension and the first adaptive gap*, public result dated November 2, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-derangement-incidence-shattering-exact-static-dimension-and-the--951015b97f7a/RESULT.md
7. *Parity-exceptional near-top shattering of even derangements*, previously documented mathematical research note (2026); no public access URL asserted.
