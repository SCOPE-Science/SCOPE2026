# Exact witness multiplicities and sharp ambiguity for inverse-dependence disjunctions

## Finding

Consider the two-variable dependence-logic formula
\[
\varphi=\operatorname{dep}(x,y)\lor\operatorname{dep}(y,x).
\]
For a finite team \(T\subseteq P\times Q\), define an **irredundant ordered splitting witness** to be a disjoint ordered pair \((T_1,T_2)\) with \(T=T_1\sqcup T_2\), \(T_1\models\operatorname{dep}(x,y)\), and \(T_2\models\operatorname{dep}(y,x)\). Let \(W(T)\) be the number of these witnesses. This deliberately counts disjoint witnesses, not overlapping pairs permitted by lax disjunction. Every team satisfying \(\varphi\) has at least one disjoint witness because dependence atoms are downward closed.

Construct the simple bipartite graph \(G_T\) with a left vertex for each element of \(P\), a right vertex for each element of \(Q\), and one edge for each pair in \(T\), with two disjoint copies even if \(P=Q\). For any connected component \(C\), write \(v_C=|V(C)|\) and \(e_C=|E(C)|\). Then the exact witness number is
\[
W(T)=\begin{cases}
0,&\text{if some component has }e_C>v_C,\\
\displaystyle\prod_{C:e_C=v_C-1}v_C\,\cdot\,2^{\#\{C:e_C=v_C\}},&\text{otherwise}.
\end{cases}
\]
In the second line the product includes isolated vertices, each with factor one. All connected components must be trees or unicyclic for a positive number. In particular, the number is determined by component orders and cycle ranks, not by detailed tree shapes.

For \(P=Q=[d]\), with \(d\ge1\), the maximum across **all** \(2^{d^2}\) teams is exactly
\[
\max_{T\subseteq[d]^2}W(T)=
\begin{cases}
3^{2d/3},&d\equiv0\pmod3,\\
2\cdot3^{(2d-2)/3},&d\equiv1\pmod3,\\
4\cdot3^{(2d-4)/3},&d\equiv2\pmod3.
\end{cases}
\]
An attaining team is always a forest. Its component orders are optimal integer-break parts: pairs of oppositely balanced three-vertex paths, plus a two-vertex edge or a four-vertex path when required.

More generally, for \(|P|=p\ge0\) and \(|Q|=q\ge0\), the **total** number of irredundant ordered witnesses across all teams is
\[
Z_{p,q}:=\sum_{T\subseteq P\times Q}W(T)
=\sum_{k=0}^{\min(p,q)}(-1)^k
\binom pk\binom qk k!\,(q+1)^{p-k}(p+1)^{q-k}.
\]
For positive \(d=1,2,3,4\), the respective maximum witness counts are \(2,4,9,18\), and the total witness counts on \(d\times d\) domains are \(3,47,2074,183249\). The corresponding numbers of teams satisfying \(\varphi\) are \(2,16,460,33959\).

There is also a structural bivariate exponential generating identity. Let \(L=L(x,y)\) and \(R=R(x,y)\) be the unique formal power series with zero constant terms satisfying
\[L=x\exp R,\qquad R=y\exp L.\]
Then
\[
\boxed{\sum_{p,q\ge0}\frac{Z_{p,q}}{p!q!}x^p y^q
=\frac{\exp(L+R-LR)}{1-LR}.}
\]
Thus the local component law and the global inclusion-exclusion formula encode the same entire two-parameter witness spectrum.

## Assumptions and scope

The domain sets \(P,Q\) are finite labelled sets of values, and the team is a **set** of assignments, not a bag with repeated tuples. Each dependence atom is the usual functional-dependence condition: \(T_1\models\operatorname{dep}(x,y)\) means any two assignments in \(T_1\) with equal \(x\)-values have equal \(y\)-values. The other atom swaps the coordinates. Disjunction uses standard lax team semantics (subteams may overlap); witness multiplicity is explicitly restricted to the canonical disjoint representation. The empty team has one witness, namely two empty subteams. Isolated graph vertices are retained to make global coefficient formulas uniform.

## Proof

**1. Witnesses are functional orientations.** Choose a disjoint witness \(T_1\sqcup T_2=T\). Direct each edge of \(G_T\) from left to right exactly when its assignment belongs to \(T_1\), and from right to left exactly when it belongs to \(T_2\). The two functional-dependence conditions hold precisely when each left vertex has at most one outgoing edge to the right and each right vertex at most one outgoing edge to the left. Conversely, every orientation with outdegree at most one determines exactly one such disjoint ordered splitting. The orientation and splitting sets are therefore bijective. This is the qualitative graph reduction of Fröhlich--Kolaitis--Meier; the count below is the additional quantitative statement.

**2. Count orientations componentwise.** Suppose a connected component has \(v\) vertices and \(e\) edges. The total outdegree of any orientation equals \(e\), so outdegree at most one at each vertex forces \(e\le v\). Connectivity gives \(e\ge v-1\). If \(e=v-1\), it is a tree. Precisely one vertex has outdegree zero and all others outdegree one; directing the unique path of every nonroot vertex toward the root produces the unique such orientation for that root. There are \(v\) choices. If \(e=v\), it is unicyclic. Every vertex must have outdegree exactly one; every tree branch is forced toward the cycle, which has exactly two possible cyclic directions. Thus there are exactly two choices. Components contribute independently, giving the displayed product and zero otherwise.

**3. Sharp maximum.** Set \(P=Q=[d]\), so there are \(2d\) graph vertices. A component of order \(v\) contributes at most \(v\) (including a unicyclic component, whose factor two is at most its order, since a simple bipartite cycle has at least four vertices). Hence \(W(T)\) is at most the maximum product of positive integers whose sum is \(2d\). In such a maximizing integer partition there are no parts of size one for \(2d\ge2\), and every part of size at least five can be split to increase the product. Three is preferable to three twos once a sum of six is available, and a remainder of one is replaced by two parts of size two. The resulting exact maxima are the three displayed residue formulas.

To attain these bounds with **equal** left and right vertex sets, write \(2d=6a+r\) with \(r\in\{0,2,4\}\). For each of the \(a\) groups of six vertices, take two disjoint three-vertex paths, one with two left and one right vertex, the other with one left and two right vertices. The residual two vertices, if present, form an edge; the residual four, if present, form a four-vertex alternating path. Each group is balanced between left and right, so the construction embeds in \(K_{d,d}\). The tree components provide exactly the integer-break product, proving sharpness. The construction also covers \(d=1,2\).

**4. Total number across teams.** A disjoint witness is the same as a pair of partial functions \(f:P\rightharpoonup Q\) and \(g:Q\rightharpoonup P\), whose graphs are disjoint: \(f\) specifies \(T_1\) and \(g\), with reversed coordinates, specifies \(T_2\). There are initially \((q+1)^p(p+1)^q\) pairs, including undefined values. A common graph edge can lie in both partial functions only along a matching. By inclusion-exclusion, choosing \(k\) forced common edges contributes \((-1)^k\binom pk\binom qk k!\). For each forced matching the remaining \(p-k\) left values and \(q-k\) right values have independently \(q+1\) and \(p+1\) options, respectively. Summation gives \(Z_{p,q}\). Each disjoint witness corresponds to one and only one union team, so this also equals \(\sum_T W(T)\).

**5. Generating function.** Classical labelled-species decompositions can be applied with left and right vertex markers. The series \(L=x e^R\) and \(R=y e^L\) enumerate bipartite trees rooted at a left or right vertex, respectively. Unrooted bipartite trees have series \(L+R-LR\); connected bipartite unicyclic graphs have series \(U=\tfrac12\sum_{j\ge2}(LR)^j/j=\tfrac12(-\log(1-LR)-LR)\). Each tree carries \(v\) witnesses (choose its root), so its witness-weighted connected series is \(L+R\). Each unicyclic component carries two witnesses, hence its weighted connected series is \(2U\). The exponential formula for sets of labelled connected components gives
\[
\exp(L+R+2U)=\exp(L+R-LR)/(1-LR),
\]
which is the stated bivariate identity. All arguments are identities of formal power series; no convergence assumption is needed.

## Verification

The standalone `verify_split.py` uses a second description for each witness: it independently chooses a binary assignment for every team row, then checks the two functional-dependence conditions directly. It compares this brute count against the component formula for **all** teams with \(1\le p,q\le3\) (682 teams in total). For each such rectangle it also checks that summing the component formula agrees with the inclusion-exclusion formula. For square rectangles through \(4\times4\), it computes the component formula for **every** team, verifies the exact global sum and maximum, and independently checks 200 pseudorandom four-by-four teams against the brute split count. The tested \(4\times4\) layer has \(65536\) teams. Execution prints `PASS`. Exhaustive finite checks are consistency tests; the five preceding mathematical steps, not extrapolation, establish every quantified statement.

## Relationship to prior work

Fröhlich, Kolaitis and Meier (2025/2026), Lemma 15, prove the qualitative equivalence between \(\varphi\), existence of an outdegree-at-most-one orientation, and a pseudoforest component condition, and establish a logspace model-checking classification. These qualitative statements and the existence of disjoint splittings are *prior work*. The present theorem asks a different quantitative question: how many **disjoint satisfying explanations** does each team have, what is the sharp maximum over a fixed product alphabet, and what is their sum over all teams? The displayed formulas and sharp balanced attainment are not asserted by the inspected qualitative reduction or complexity statements. Barlag et al. (2026) study coherence, rewritability and complexity of deciding coherence, not these witness multiplicities. The underlying rooted-tree and cycle-species identities, integer-break optimization, and inclusion-exclusion are standard combinatorial methods; their separate graph-theoretic statements are not claimed as new.

## Limitations

The witness count is **not** the number of all overlapping pairs allowed by lax splitting disjunction. The result treats two unary dependence atoms sharing two variables, and ordinary set-valued teams. The maximum assumes equal finite alphabet sizes for the two variables; the exact per-team law and global sum allow unequal alphabet sizes. The generating identity uses labelled vertex sets, and its unicyclic term assumes ordinary simple bipartite graphs. No new complexity-class separation is claimed. No exhaustive historical novelty certification is available, and a mathematically equivalent counting identity could exist in unindexed enumeration literature. No independent mathematical audit has been performed.

## References

1. N. Fröhlich, P. G. Kolaitis, and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146v1, first submitted 2025-08-22. Open text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html ; DOI: 10.4230/LIPIcs.CSL.2026.10. Especially Lemma 15, Theorem 16, Theorem 25 and Appendix A.
2. T. Barlag et al., *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269v1, 2026-05-29. Full manuscript: https://pdfs.assets.alphaxiv.org/2605.31269v1.pdf .
3. E. W. Weisstein, *Pseudoforest*, MathWorld, https://mathworld.wolfram.com/Pseudoforest.html . Standard equivalence between pseudoforests and connected components of cyclomatic number at most one.
4. A. Haak, J. Kontinen, F. Müller, H. Vollmer, and F. Yang, *Counting of Teams in First-Order Team Logics*, arXiv:1902.00246v1 (2019); journal publication ACM Transactions on Computational Logic 27(1), Article 5 (2025), DOI: 10.1145/3771721. Open full text: https://research-portal.uu.nl/ws/files/280122104/3771721.pdf . This counts satisfying teams and logical counting complexity classes, not the disjoint splitting-witness multiplicities here.
