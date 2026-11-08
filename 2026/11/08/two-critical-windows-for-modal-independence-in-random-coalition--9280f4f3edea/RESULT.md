# Two critical windows for modal independence in random coalition games

## Finding

In a two-agent concurrent game with two terminal outcomes, the independence-of-agents **modal axiom** can hold under every valuation even when the actual action availability relation is not independent. Under a natural independent random-action model, these two notions admit exact finite descriptions and different limiting laws, and the modal axiom exhibits two distinct critical scales.

For each integer \(m\ge1\), let each agent have the action set \(\{1,\ldots,m\}\). For each complete action pair \((i,j)\), independently set its outcome to \(\varnothing\), \(\{u\}\), or \(\{v\}\) with probabilities \(1-p_m\), \(p_m/2\), \(p_m/2\), respectively. The states \(u,v\) are distinct. Write \(A_m\) for the event that every pair of separately available agent actions has an available joint completion (action-level independence), and \(M_m\) for validity at the root, under *every* valuation, of the independence axiom scheme
\[
([\{a\}]\varphi\land[\{b\}]\psi)\longrightarrow[\{a,b\}](\varphi\land\psi).
\]
The analogous disjoint-coalition instances involving the empty coalition are automatically valid. If needed as a global pointed-frame formulation, equip \(u\) and \(v\) with deterministic, total, self-looping action tables; their independence axiom instances then hold identically.

**Deterministic characterization.** Let \(R_u,R_v\) count rows containing a nonempty entry of just the indicated color and no entry of the opposite color; let \(C_u,C_v\) count analogous columns. Then
\[
\boxed{M_m\quad\Longleftrightarrow\quad (R_u=0\ \lor\ C_v=0)\ \land\ (R_v=0\ \lor\ C_u=0).}
\]
Action-level independence holds exactly when the support of nonempty entries is a Cartesian rectangle \(I\times J\) (including the empty rectangle). Its **exact finite probability** is
\[
\boxed{\Pr(A_m)=(1-p_m)^{m^2}+\sum_{r=1}^m\sum_{s=1}^m
 {m\choose r}{m\choose s}p_m^{rs}(1-p_m)^{m^2-rs}.}
\]
Always \(A_m\subseteq M_m\).

**Sparse critical scale.** If \(m^2p_m\to c\in(0,\infty)\), then
\[
\boxed{\Pr(M_m)\to 2e^{-c/2}-e^{-c},\qquad
\Pr(A_m)\to e^{-c}(1+c).}
\]
The limiting probability of *modal validity without action independence* is therefore
\[
\boxed{2e^{-c/2}-(2+c)e^{-c}>0.}
\]

**Logarithmic critical scale.** If \(mp_m=2\log m+t+o(1)\) for fixed real \(t\), define \(\lambda=e^{-t/2}\). Then
\[
(R_u,R_v,C_u,C_v)\ \xrightarrow{\mathrm d}\
 (X_1,X_2,X_3,X_4),\qquad X_i\overset{\mathrm{iid}}\sim\operatorname{Poisson}(\lambda),
\]
so the *exact critical-window limiting probability* is
\[
\boxed{\Pr(M_m)\longrightarrow
 \bigl(2e^{-\lambda}-e^{-2\lambda}\bigr)^2,
 \quad\lambda=e^{-t/2}.}
\]
In particular, if \(m^2p_m\to\infty\) and \(mp_m\le2\log m-\omega(1)\), then \(\Pr(M_m)\to0\), whereas if \(mp_m\ge2\log m+\omega(1)\), then \(\Pr(M_m)\to1\). If \(m^2p_m\to0\), both \(\Pr(M_m)\) and \(\Pr(A_m)\) tend to one. Here \(\omega(1)\) denotes any positive sequence tending to infinity, and all inequalities hold eventually.

**Nearly complete games.** If \(p_m=1-c/m^2\) for fixed \(c>0\), then
\[
\boxed{\Pr(M_m)\to1,\qquad \Pr(A_m)\to e^{-c}.}
\]
Thus modal independence fails with overwhelming probability between two success regions but returns at a sharp logarithmic upper threshold; it is not a monotone function of action availability.

## Assumptions and scope

The independent cell law is a specified model, not a universal claim about arbitrary game distributions. Every nonempty complete action outcome is a singleton in \(\{u,v\}\); an unavailable joint action has empty outcome. A partial agent action is available exactly when it has some nonempty full completion. For coalition \(C\), \([C]\theta\) is true iff an available choice of \(C\) guarantees that every state in the union of outcomes of its completions satisfies \(\theta\). Propositional variables range over every valuation on the resulting three-state frame. The formulas at the root depend on their outcome truth sets at \(u,v\), so all four subsets of \(\{u,v\}\) are tested. Statements as \(m\to\infty\) concern probabilities over independent random game tables, with no independence assumed between the four line counts at finite \(m\).

## Proof

**1. Exact logical reduction.** An available row action guarantees a proper nonempty subset of \(\{u,v\}\) iff the row is pure of its unique color. The same holds for columns. An available full-profile action guarantees every nonempty subset that contains its one outcome. A failure of the displayed axiom is possible precisely when a row can guarantee \(u\) while a column guarantees \(v\), or vice versa: in either case the required intersection is empty and no available full-profile action can guarantee it. Any pair of nonempty intersecting guaranteed subsets has a common outcome \(x\in\{u,v\}\): one of the two guaranteeing actions can be extended to a nonempty full profile with outcome in the smaller set; since there are only two outcomes, the intersection must contain that outcome. A clearer case analysis is: the only proper nonempty subsets are \(\{u\}\) and \(\{v\}\); two such sets intersect unless they are opposite singletons. A premise involving the full set, or an empty-coalition action, cannot cause a failure. This proves the characterization. It also proves \(A_m\subseteq M_m\): intersect any two separately available actions in an available full profile, and use its outcome as a witness for the intersection of their guaranteed truth sets.

**2. Action-level enumeration.** Nonempty support is independent precisely when it is \(I\times J\) for its occupied row and column sets. A fixed nonempty rectangle with \(r\) rows and \(s\) columns has probability \(p_m^{rs}(1-p_m)^{m^2-rs}\), and there are \({m\choose r}{m\choose s}\) such choices. Different nonempty support rectangles are disjoint events; the empty support has probability \((1-p_m)^{m^2}\). Summation gives the exact formula.

**3. Sparse critical window.** If \(m^2p_m\to c\), the total occupied-cell count converges to \(\operatorname{Poisson}(c)\), and its two independently colored subcounts converge jointly to independent \(\operatorname{Poisson}(c/2)\) counts. With probability tending to one, no pair of occupied cells shares a row or a column: conditional on a tight occupied count, the collision probability is \(O(1/m)\). On this event, structural independence holds iff there is at most one occupied cell, whereas the modal scheme holds iff all occupied cells have the same color. The two probability formulas follow. Their positive gap equals \(2e^{-c}(e^{c/2}-1-c/2)\).

**4. General pure-line bounds and the two transition scales.** A prescribed row is nonempty and pure \(u\) with probability
\[
q_m=(1-p_m/2)^m-(1-p_m)^m.
\]
The same expression applies to the other three row/column-color kinds. Each individual count has \(\operatorname{Binomial}(m,q_m)\) distribution, because distinct rows (respectively columns) use disjoint cells. Set \(\mu_m=mq_m\). By the union bound and the characterization,
\[
\boxed{1-4\mu_m\ \le\ \Pr(M_m)\ \le\ 4e^{-\mu_m}.}
\]
For the upper bound, validity implies that at least one of the four pure-line kinds is absent; an individual kind is absent with probability \((1-q_m)^m\le e^{-\mu_m}\). For the lower bound, a failure requires at least one pure line. If \(m^2p_m\to0\), the mean-value bound \(q_m\le mp_m/2\) yields \(\mu_m\to0\). If \(m^2p_m\to\infty\) and \(mp_m\le2\log m-\omega(1)\), then \(\mu_m\to\infty\): when \(mp_m\le1\), use \(q_m\ge(mp_m/2)(1-p_m)^{m-1}\); otherwise use \(q_m\sim e^{-mp_m/2}(1-e^{-mp_m/2})\) uniformly on the indicated range, since \(mp_m^2\to0\). Finally, \(\mu_m\le m e^{-mp_m/2}\to0\) above the upper window. These bounds prove both off-critical zero-one laws.

**5. The upper four-Poisson law.** Suppose \(mp_m=2\log m+t+o(1)\). The four line counts have means converging to \(\lambda=e^{-t/2}\). To verify their joint law, fix nonnegative integers prescribing a factorial moment of any four kinds. Selected pure rows of opposite colors must be distinct, as must selected pure columns; the total number of choices is \((m)_{a+b}(m)_{c+d}\). Let \(h=a+b+c+d\) be the number of chosen lines. Each chosen line forbids entries of the opposite color. Away from the \(O(1)\) row-column intersections these constraints are independent, while the intersections alter the probability by a factor \(1+o(1)\), since \(p_m\to0\). Conditional on avoiding opposite colors, each chosen line contains its required color with probability \(1-o(1)\), since its conditional expected number of target-color entries is asymptotic to \(\log m\). Consequently, the joint factorial moment equals
\[
(m)_{a+b}(m)_{c+d}(1-p_m/2)^{mh}(1+o(1))
 \longrightarrow\lambda^h.
\]
These are exactly the joint factorial moments of four independent \(\operatorname{Poisson}(\lambda)\) variables; their joint law follows by the multivariate factorial-moment theorem. Thus the two disjoint pairs \((R_u,C_v)\) and \((R_v,C_u)\) asymptotically involve independent Poisson variables. The probability that one pair has at least one zero is \(2e^{-\lambda}-e^{-2\lambda}\); multiply for the two pairs to obtain the claimed limit.

**6. Nearly complete support.** For \(p_m=1-c/m^2\), the number of missing cells tends to \(\operatorname{Poisson}(c)\). With high probability no row or column is entirely missing; under this event structural independence holds iff no cell is missing, giving \(\Pr(A_m)\to e^{-c}\). Also \(\mu_m\le m(1-p_m/2)^m\to0\), so \(\Pr(M_m)\to1\) by the pure-line bound.

## Verification

The standalone `checker.py` exhaustively enumerates all \(3^{m^2}\) ternary outcome tables for \(m=1,2,3\). For each, it evaluates every disjoint-coalition instance over all sixteen ordered pairs of outcome truth sets, compares the resulting direct modal verdict with the pure-line characterization, and verifies that structural independence implies modal validity. It independently checks the finite action-independence probability formula at \(p=2/5\) using exact fractions. The resulting modal/action counts are \((3,3)\), \((61,41)\), and \((11115,1179)\), respectively; the program terminates with `COALITION_IA_FINITE_CHECKS_OK`. These tests are finite cross-checks, not proofs of the asymptotic limit statements. The latter rely on the preceding elementary probability estimates and the factorial-moment proof.

## Relationship to prior work

Wang and Dou (2026) define the general concurrent-game semantics and the independence axiom, and investigate the lattice of coalition logics and structural extensions. Their Theorem statements, game constructions, and further-problems section address algebraic coatoms, splitting, and compact meets; they do not assert the two-parameter random-action probability laws here. Li and Ju (2024; subsequent journal publications) establish the minimal logic and completeness of systems imposing independence, seriality, or determinism, rather than the distribution of validity for a fixed randomly generated game. The present paper's probabilistic model, exact pure-line criterion, two critical scales, and the fourfold Poisson limit form one connected result, not claims of a new general completeness theorem.

Potential overlap with classical Poisson limits for local defects in random bipartite graphs is acknowledged: the factorial-moment technique is standard. The new statement here concerns the specific **logical-versus-structural independence distinction** and the resulting pair of separated critical windows in this coalition semantics. No claim is made that the binomial/Poisson tools themselves are novel.

## Limitations

Only two agents and two possible terminal outcomes are analyzed. Cells are independent, nonempty outcomes are deterministic singletons, and the colors are equally likely. The exact modal characterization can change with three or more outcomes, nondeterministic profile outcomes, or constraints on valuations. The joint Poisson theorem is an asymptotic statement for the displayed scaling, not an assertion of finite-size independence. The priority comparison is based on the accessible full motivating article, published research summaries and targeted searches; unindexed or inaccessible specialized probability papers may contain overlapping results. Independent mathematical validation and external historical-priority audit have not been performed.

## References

1. S. Wang and Y. Dou, *The Lattice of Coalition Logics between MCL and CL: Coatoms and Compact Meets*, arXiv:2610.24466v1, publicly submitted 2026-10-17, Sections 2, 4, 6, 7. https://arxiv.org/abs/2610.24466.
2. Y. Li and F. Ju, *A Minimal Coalition Logic*, arXiv:2403.14704v1, 2024. https://arxiv.org/abs/2403.14704.
3. Y. Li and F. Ju, *Completeness of Coalition Logics with Seriality, Independence of Agents, or Determinism*, arXiv:2409.14635v1, 2024. https://arxiv.org/abs/2409.14635.
4. Z. Chen, F. Ju and T. Ågotnes, *Representation Theorems for Actual and Alpha Powers over General Concurrent Game Frames without Assuming Independence of Agents*, arXiv:2607.10567v1, 2026 (abstract-level comparison only). https://arxiv.org/abs/2607.10567.
