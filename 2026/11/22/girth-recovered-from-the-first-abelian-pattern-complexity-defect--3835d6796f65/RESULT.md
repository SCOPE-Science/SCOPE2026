# Girth recovered from the first Abelian pattern-complexity defect

## Finding
Let \(D\subseteq\mathbb N_0\) be infinite and have arbitrarily long intervals containing no elements of \(D\). Write \(x=\mathbf1_D\). For every positive integer \(k\), define its Abelian maximal pattern complexity by
\[
P_D(k)=\max_{S\subseteq\mathbb N_0,\ |S|=k}\left|\left\{\sum_{s\in S}x_{n+s}: n\in\mathbb N_0\right\}\right|,
\]
and define the universal aperiodic lower envelope
\[
f(k)=\min\{m\in\mathbb N:\binom m2\ge k\},\qquad T_r=\binom{r+1}{2}.
\]
Let \(\Gamma_D\) be the bipartite *sum-incidence graph*, with distinct left and right vertices \(L_i,R_j\) for \(i,j\in\mathbb N_0\) and edge \(L_iR_j\) precisely when \(i+j\in D\). Set its girth to infinity when it has no finite cycle. Define the **first complexity defect**
\[
K(D)=\min\{k\ge1:P_D(k)>f(k)\},
\]
with \(K(D)=\infty\) if this set is empty.

**Girth-to-first-defect theorem.** For every integer \(r\ge2\),
\[
\boxed{\operatorname{girth}(\Gamma_D)=2r\quad\Longleftrightarrow\quad T_{r-1}<K(D)\le T_r.}
\]
Moreover, \(\Gamma_D\) is a forest if and only if \(K(D)=\infty\). In particular, the *single integer* \(K(D)\) determines the girth of this infinite additive incidence graph.

**Sharp unicyclic refinement.** If \(\Gamma_D\) has exactly one finite simple cycle, of length \(2r\), then
\[
\boxed{K(D)=T_r,\qquad P_D(T_r)=r+2.}
\]
Both equalities are achieved, for every integer \(r\ge2\), by the explicit infinite supports
\[
D_r=\{0,r-1,r\}\cup\{(2r+1)3^j:j\ge1\}.
\]
Thus the first failure of minimal complexity can occur arbitrarily late, and its exact location detects the length of the unique cycle.

## Assumptions and scope
All supports and pattern positions are subsets of the nonnegative integers. The two bipartite vertex copies are disjoint even for equal indices; cycles are finite simple cycles. Every \(D\) covered in the first theorem is infinite with arbitrarily long zero gaps; this makes \(x\) aperiodic and puts \(0^\infty\) in its shift-orbit closure. The maximum defining \(P_D(k)\) exists because the possible cardinalities lie in \(\{1,\dots,k+1\}\). A finite graph is unicyclic when its cycle-space dimension is exactly one; for the infinite graph this means exactly one finite simple cycle. We make no assertion for periodic characteristic words or supports with bounded zero gaps.

## Proof
**1. A finite certificate for a large degree spectrum.** Fix a pattern \(S\) of cardinality \(k\), and suppose \(q\ge1\) different values of \(c_S(n)=\sum_{s\in S}\mathbf1_D(n+s)\) are at least two. Select distinct translates \(n_1,\ldots,n_q\) realizing these values, and arrange the values increasingly. They are at least \(2,3,\ldots,q+1\). In the finite bipartite subgraph \(H\) induced by left vertices \(L_{n_1},\ldots,L_{n_q}\) and right vertices \(R_s\) for \(s\in S\), the number of edges therefore satisfies
\[
|E(H)|\ge2+3+\cdots+(q+1)=T_q+q,
\]
where \(T_q=q(q+1)/2\). There are exactly \(q+k\) vertices. Consequently the cycle-space dimension satisfies
\[
\beta_1(H)=|E(H)|-|V(H)|+\kappa(H)\ge T_q-k+1,
\]
where \(\kappa(H)\ge1\) is the component count. In particular, \(k\le T_q\) forces a cycle of length at most \(2q\), and \(k<T_q\) forces at least two independent cycles.

**2. Quantitative converse to short-cycle obstruction.** If \(\Gamma_D\) contains no cycle of length at most \(2r\), let \(1\le k\le T_r\), and set \(q=f(k)-1\le r\). If \(P_D(k)\ge f(k)+1=q+2\), then a witnessing pattern has at least \(q\) distinct count values at least two (at most two distinct values can be zero or one). Since \(k\le T_q\) by the definition of \(f\), Step 1 yields a cycle of length at most \(2q\le2r\), a contradiction. Hence \(P_D(k)\le f(k)\). The aperiodic lower bound of Zeng–Xue–Zeng (2026, their aperiodicity criterion) gives \(P_D(k)\ge f(k)\) for every \(k\). Therefore
\[
\operatorname{girth}(\Gamma_D)>2r\quad\Longrightarrow\quad P_D(k)=f(k)\text{ for all }1\le k\le T_r.
\]

**3. Detection of a shortest cycle.** Suppose the shortest graph cycle has length \(2r\). By Step 2 applied with \(r-1\), there is no defect at any \(k\le T_{r-1}\) (for \(r=2\), this is also immediate at \(k=1\)). On the other hand, Theorem 6.4 of Zeng–Xue–Zeng (2026) states, under exactly the present hypotheses that \(D\) is infinite and \(0^\infty\) lies in the shift-orbit closure, that a cycle of length \(2r\) forces
\[
P_D(T_r)\ge r+2>f(T_r)=r+1.
\]
Thus \(T_{r-1}<K(D)\le T_r\). Conversely, if this inequality holds for \(K(D)\), Step 2 rules out girth greater than \(2r\), while the cited cycle obstruction rules out any cycle of length \(2s\) with \(2\le s<r\), which would have forced a defect by \(T_s\le T_{r-1}\). Hence the girth must be \(2r\). If there is no cycle, Step 2 for all \(r\) gives \(K(D)=\infty\); if there is a cycle, the cited obstruction makes \(K(D)\) finite. This proves the complete inverse statement.

**4. Unicyclic rigidity.** Now suppose \(\Gamma_D\) has precisely one finite cycle of length \(2r\). For any \(T_{r-1}<k<T_r\), if a pattern had \(P_D(k)>f(k)=r+1\), Step 1 with \(q=r\) would give \(\beta_1(H)\ge T_r-k+1\ge2\), impossible in a graph with only one independent cycle. Together with Step 2 below \(T_{r-1}\), this proves \(P_D(k)=f(k)\) for every \(k<T_r\). Step 3 gives \(P_D(T_r)\ge r+2\). If it were at least \(r+3\), there would be \(r+1\) distinct degrees at least two, and Step 1 would give \(\beta_1(H)\ge T_{r+1}-T_r+1=r+2>1\), also impossible. Hence \(P_D(T_r)=r+2\), and \(K(D)=T_r\).

**5. Exact one-cycle supports of every even girth.** Let \(a=r-1\), and first consider the three-weight graph for \(E=\{0,a,a+1\}\). Edges of sum \(a\) and \(a+1\) form a single path (their matchings alternate) from \(L_{a+1}\) to \(R_{a+1}\). The extra edge \(L_0R_0\) closes exactly one simple cycle, whose route from \(L_0\) to \(R_0\) through the two matchings has \(2a+1\) edges. Thus the unique cycle has length \(2a+2=2r\).

Suppose a larger allowed sum \(M\) is added, with \(M>2B\), where \(B\) is the previous largest sum. If a new cycle uses an edge \(L_iR_j\) of sum \(M\), the other edge at each of its endpoints has a smaller sum, at most \(B\), since each sum forms a matching. Hence \(i\le B\), \(j\le B\), and \(M=i+j\le2B\), a contradiction. Adding the sums \((2r+1)3^j\) successively therefore creates no further cycle. Any hypothetical cycle in the infinite union uses only finitely many sums and would appear at a finite stage. Thus \(\Gamma_{D_r}\) is unicyclic of girth \(2r\), proving the asserted realization for every \(r\ge2\).

For an explicit lower-bound witness, put \(S_0=\{0,1,\ldots,r-1\}\), and use distinct distant spikes \(N_j=(2r+1)3^j\) to add, for each \(i=1,\ldots,r-1\), exactly \(i\) new positions \(N_j-i\), never reusing a spike. This produces a pattern \(S\) of size \(r+\sum_{i=1}^{r-1}i=T_r\). At translate \(n=i\) (\(0\le i<r\)), the base positions hit exactly two elements of \(\{0,r-1,r\}\), while the distant positions add exactly \(i\) further hits: the counts are \(2,3,\ldots,r+1\). The arbitrarily long zero gaps give additional translates with counts zero and one (align the largest pattern position with the first spike after a sufficiently long gap). This exhibits the \(r+2\) distinct counts directly; Step 4 proves there are no more.

## Verification
`check_girth.py` constructs the finite bipartite graph independently from each allowed sum and computes both cycle-space rank and girth by graph traversal. Its 40 finite tests (parameters \(2\le r\le11\) and zero through three distant additions) all return rank one and girth \(2r\). `check_witness.py` independently builds explicit tagged patterns for \(2\le r\le12\), checks all 77 prescribed translate counts and exhibits translates of counts zero and one. Both scripts use only the Python standard library. Run `python3 check_girth.py` and `python3 check_witness.py` from the extracted package; expected outputs are included. These finite tests corroborate the structural steps but are not substitutes for the quantified proofs.

## Relationship to prior work
Zeng, Xue and Zeng (2026), arXiv:2609.28059, introduced the sum-incidence forest characterization and proved the **forward** obstruction that any \(2r\)-cycle forces a complexity excess at arity \(T_r\), as well as the universal aperiodic lower envelope. Those theorems are explicitly used above. The contribution here is the quantitative **inverse**: absence of cycles of length up to \(2r\) forces all pattern complexities through arity \(T_r\) to equal their minimum, which identifies the girth from the first defect, and the exact unicyclic first-defect and excess formulas. This is not an assertion that the qualitative forest criterion or the cycle-to-excess direction is new.

A published 2026 classification of three-element supports gives a general cycle-rank formula encompassing \(\{0,r-1,r\}\), and a separate classification determines the girth of shifted geometric supports. Those results concern graph structure and particular support families; neither inspected full result gives the inverse relation between graph girth and the first Abelian pattern-complexity defect. The 2013 work of Kamae, Widmer and Zamboni introduced the statistic and treats recurrent aperiodic words, not this sparse cycle-girth inverse problem.

## Limitations
The inverse applies to infinite supports with arbitrarily long gaps, and the exact endpoint and excess apply to unicyclic graphs. For an arbitrary graph with multiple independent cycles, the first defect may occur strictly between \(T_{r-1}\) and \(T_r\); the theorem does not claim a fixed exact arity there. The cycle-to-complexity implication and the global lower envelope are established published premises, not independently reproved here. The explicit computational checks are finite. Historical priority of an unindexed quantitative converse remains a residual risk.

## References
1. Qingcheng Zeng, Yumei Xue, Cheng Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059 (first public version 2026-09-23), especially the aperiodicity criterion, Theorem 6.4 and the incidence-forest theorem. https://arxiv.org/abs/2609.28059 and https://arxiv.org/html/2609.28059 .
2. Teturo Kamae, Steven Widmer, Luca Q. Zamboni, *Abelian maximal pattern complexity of words*, arXiv:1301.5113 (2013). https://arxiv.org/abs/1301.5113 .
3. *Exact girth trichotomy for shifted geometric supports and Abelian pattern Sturmian words*, public research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-girth-trichotomy-for-shifted-geometric-supports-and-abelia--fd19a03eea19 .
4. *Exact cycle rank and admissible three-spike prefixes for Abelian pattern Sturmian words*, public research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cycle-rank-and-admissible-three-spike-prefixes-for-abelian--e3a97eafa17a .
