# Sharp orientation extremizers for zero-product probabilities in radical-square-zero quiver algebras

## Finding

For a finite loopless quiver \(Q=(V,E)\), with \(n=|V|\) vertices and \(m=|E|\) arrows (parallel arrows allowed), let \(A_Q=\mathbb F_qQ/J^2\) over a finite field of cardinality \(q\), where \(J\) is the arrow ideal. Define the **zero-product probability**
\[
 z(Q;q)=\Pr_{X,Y\,\mathrm{uniform}\,\mathrm{independent}\,\mathrm{in}\,A_Q}(XY=0).
\]
For \(F\subseteq E\), write \(i(F)\) for the number of vertices with no selected incident arrow, \(s(F)\) for the number of vertices incident to selected arrows only as a source or only as a target, and \(b(F)\) for the number incident to selected arrows as both source and target. A previously obtained all-quiver annihilator-spectrum identity can be specialized to the following **oriented-subgraph expansion**, which we use as a counting lemma, **not as the new contribution**:
\[
 \boxed{z(Q;q)=q^{-2n-m}\sum_{F\subseteq E}(q-1)^{|F|}(2q-1)^{i(F)}q^{s(F)}.}\tag{1}
\]
The exponent at the \(b(F)\) mixed vertices is zero; they contribute a multiplicative factor of one.

For every finite **bipartite loopless undirected multigraph** \(G\), the maximum of \(z(Q;q)\) over all orientations \(Q\) of the edges of \(G\) is
\[
 \boxed{q^{-2n-m}\sum_{F\subseteq E(G)}(q-1)^{|F|}(2q-1)^{n-|V(F)|}q^{|V(F)|}.}\tag{2}
\]
Equality holds **precisely** for the source–sink orientations: at every vertex, all incident arrows point outward or all point inward. On each connected component containing an edge, these are the two orientations induced by the bipartition; isolated vertices do not affect the statement. This is an exact characterization for all prime powers \(q\ge2\).

For the undirected path on \(n\ge3\) vertices, \(z(Q;q)\) is **minimized exactly** by its two consistently directed orientations and **maximized exactly** by its two alternating (source–sink) orientations. For \(n=1,2\), all orientations tie. Define integers \(L_n(q)\) and \(U_n(q)\) for \(n\ge0\) by
\[
 \begin{aligned}
 L_0&=U_0=1,\\
 L_1&=U_1=2q-1,\\
 L_{n+2}&=(3q-2)L_{n+1}+(q-1)^3L_n,\\
 U_{n+2}&=(q^2+q-1)U_{n+1}-q(q-1)^2U_n.
 \end{aligned}\tag{3}
\]
Then the exact extremal probabilities on the \(n\)-vertex path are
\[
 \boxed{z_{\min}(n,q)=q^{1-3n}L_n(q),\qquad z_{\max}(n,q)=q^{1-3n}U_n(q).}\tag{4}
\]
In particular, at \(q=2\), the two unnormalized sequences \(L_n,U_n\) for \(n=1,\ldots,6\) are respectively \((3,13,55,233,987,4181)\) and \((3,13,59,269,1227,5597)\). Their counts of zero-product ordered pairs are \(q^{n-1}L_n\) and \(q^{n-1}U_n\).

The orientation gap is **exponentially strict** at fixed \(q\). Let
\[
 \begin{aligned}
 \lambda_{L,\pm}&=\frac{3q-2\pm q\sqrt{4q-3}}2,\\
 \lambda_{U,\pm}&=\frac{q^2+q-1\pm\sqrt{(q^2+q-1)^2-4q(q-1)^2}}2,\\
 A_L&=\frac{2q-1-\lambda_{L,-}}{\lambda_{L,+}-\lambda_{L,-}},\qquad
 A_U=\frac{2q-1-\lambda_{U,-}}{\lambda_{U,+}-\lambda_{U,-}}.
 \end{aligned}\tag{5}
\]
Then \(A_L,A_U>0\), \(\lambda_{U,+}>\lambda_{L,+}>0\), and
\[
 \boxed{z_{\min}(n,q)\sim qA_L\left(\frac{\lambda_{L,+}}{q^3}\right)^n,
 \quad z_{\max}(n,q)\sim qA_U\left(\frac{\lambda_{U,+}}{q^3}\right)^n.}\tag{6}
\]
Thus \(z_{\max}(n,q)/z_{\min}(n,q)\sim (A_U/A_L)(\lambda_{U,+}/\lambda_{L,+})^n\).

## Assumptions and scope

All fields are finite, with \(q\) any prime power at least two. Quivers have finitely many vertices and arrows, no loops, and may have parallel arrows. A quiver orientation of a fixed undirected multigraph assigns one direction to each edge without altering endpoints or multiplicities. The algebra \(\mathbb F_qQ/J^2\) has \(n+m\) vector-space dimensions, a unit given by the sum of the vertex idempotents, and a square-zero ideal spanned by the arrows. Zero-product probability concerns **ordered** pairs and **one-sided multiplication \(XY=0\)**, not the simultaneous condition \(XY=YX=0\) or the commutator condition \(XY=YX\). Statement (2) needs bipartiteness to realize its upper bound by an orientation; formula (1) does not. The path extremal assertions apply to simple paths.

## Proof

**1. Multiplication and exact expansion.** Adopt the path convention \(e_u\alpha=\alpha=\alpha e_v\) for an arrow \(\alpha:u\to v\). Write
\[
 X=\sum_{v\in V}a_ve_v+\sum_{\alpha\in E}r_\alpha\alpha,
 \qquad Y=\sum_{v\in V}b_ve_v+\sum_{\alpha\in E}s_\alpha\alpha.
\]
Since products of two arrow basis elements vanish in \(A_Q\), the condition \(XY=0\) is equivalent to
\[
 a_vb_v=0\ (v\in V),\qquad
 a_{u}s_\alpha+r_\alpha b_{v}=0\ (\alpha:u\to v).
\]
There are exactly \(2q-1\) diagonal pairs \((a_v,b_v)\) with product zero. With fixed diagonal pairs, the arrow equation has \(q^2\) solutions in \((r_\alpha,s_\alpha)\) if \(a_u=b_v=0\), and \(q\) solutions otherwise. Factor its count as
\[
 q\bigl[1+(q-1)\mathbf 1_{a_u=0,\,b_v=0}\bigr].
\]
Multiplication over the \(m\) independent arrow equations, followed by expansion of the product into subsets \(F\subseteq E\), requires \(a_v=0\) wherever \(F\) has an outgoing arrow and \(b_v=0\) wherever \(F\) has an incoming arrow. At a vertex with neither restriction there are \(2q-1\) allowed pairs; with exactly one restriction there are \(q\); with both restrictions there is one. The number of zero-product pairs is therefore \(q^m\sum_F(q-1)^{|F|}(2q-1)^{i(F)}q^{s(F)}\). Division by \(|A_Q|^2=q^{2(n+m)}\) proves (1).

**2. Bipartite-graph maximizers.** In each summand of (1), every vertex touched by \(F\) contributes at most \(q\); equality occurs at that vertex precisely when it has selected incidence of only one direction. Termwise comparison gives the upper bound (2) for **every** orientation of \(G\). If \(G\) is bipartite, directing all edges from one side to the other makes every vertex a pure source or pure sink and attains every bound simultaneously. Conversely, if a vertex has at least one incoming and one outgoing arrow in the full orientation, choose \(F\) consisting of one arrow of each kind. That term has a factor of one instead of \(q\), so the total is strictly below (2) because \(q>1\) and all terms are positive. Hence equality forces all vertices to be pure sources or sinks. For each connected bipartite component with edges, the two bipartition directions are the only choices.

**3. Path minimizers.** On a simple path, a selected edge subset \(F\) is a union of disjoint runs. Vertices internal to a run see two selected edges. Their factor is one if the two arrows form a directed passage through the vertex, and is \(q\) if the arrows both enter or both leave the vertex (a turn). The isolated and run-endpoint factors depend only on \(F\), not its orientation. Therefore, each term is smallest for a consistently oriented path (no turns), and largest for an alternating path (a turn at every internal vertex). If an orientation has any turn, the term choosing the two incident edges is strictly larger than under a consistent orientation, proving uniqueness of the two minima for \(n\ge3\). If it has any nonturn, the same two-edge term is strictly smaller than under an alternating orientation, proving uniqueness of the two maxima.

**4. Recurrences.** For a directed path, group each diagonal pair \((a_v,b_v)\) into the three states \(0:(0,0)\), \(A:(a\ne0,b=0)\), and \(B:(a=0,b\ne0)\), of multiplicities \(1,q-1,q-1\). Upon factoring the universal \(q^{n-1}\) for arrow solutions, the transfer matrix is
\[
 T=\begin{pmatrix}
 q&q(q-1)&q-1\\
 1&q-1&q-1\\
 q&q(q-1)&q-1
 \end{pmatrix}.
\]
Thus \(L_n=(1,q-1,q-1)T^{n-1}(1,1,1)^{\mathsf T}\) for \(n\ge1\). The characteristic polynomial is
\[
 t\bigl(t^2-(3q-2)t-(q-1)^3\bigr).
\]
Direct evaluation gives \(L_1=2q-1\), \(L_2=q^3+3q^2-4q+1\), and \(L_3=(3q-2)L_2+(q-1)^3L_1\). Cayley–Hamilton supplies the second-order recurrence thereafter; the stated extension \(L_0=1\) also matches \(L_2\).

For an alternating path use binary indicators \(\epsilon_i\in\{0,1\}\) of selected edges in the expansion, with boundary indicators \(\epsilon_0=\epsilon_n=0\). Every vertex touched by a selected edge contributes \(q\); untouched vertices contribute \(2q-1\). The two-state transfer matrix is
\[
 M=\begin{pmatrix}2q-1&q(q-1)\\q&q(q-1)\end{pmatrix},
 \qquad U_n=(M^n)_{0,0}.
\]
The characteristic polynomial of \(M\) is \(t^2-(q^2+q-1)t+q(q-1)^2\), proving the second recurrence in (3). Equation (4) follows from the normalization in (1).

**5. Sharp spectral laws and strict gap.** The characteristic roots yield (5). For \(q\ge2\), \(\lambda_{L,+}>0>\lambda_{L,-}\) with \(|\lambda_{L,-}|<\lambda_{L,+}\); for \(U\) both roots are positive, distinct, and the plus root is larger. The initial conditions in (3) therefore yield \(L_n=A_L\lambda_{L,+}^n+(1-A_L)\lambda_{L,-}^n\) and the analogous formula for \(U_n\). Since \(\lambda_{L,-}<0\) and \(\lambda_{L,+}>2q-1\), the coefficient \(A_L\) is positive. The polynomial for \(U\) evaluated at \(2q-1\) equals \(-q^2(q-1)<0\), so \(2q-1\) lies strictly between the two positive roots and \(A_U>0\).

To compare Perron roots, the polynomial \(P_L(t)=t^2-(3q-2)t-(q-1)^3\) satisfies \(P_L(2q-1)=-(q-1)(2q-1)-(q-1)^3<0\); hence \(\lambda_{L,+}>2q-1\). For \(P_U(t)=t^2-(q^2+q-1)t+q(q-1)^2\), substitution of \(P_L(\lambda_{L,+})=0\) gives
\[
 P_U(\lambda_{L,+})=(q-1)^2(2q-1-\lambda_{L,+})<0.
\]
Thus \(\lambda_{L,+}\) lies strictly between the two roots of \(P_U\) and \(\lambda_{U,+}>\lambda_{L,+}\). Dominance of the plus roots gives (6) and the exponential ratio.

## Verification

Execute `python verify.py` using Python 3 and no external dependencies. The verifier directly enumerates the vector-space elements and multiplies all ordered pairs for path quivers over prime fields \(q=2\) with \(n\le5\) and \(q=3\) with \(n\le3\), for **every path orientation**. It checks the independent oriented-subgraph expansion for small cyclic and parallel-arrow examples. It enumerates all path orientations through \(n=6\) at \(q=2\) and through \(n=5\) at \(q=3\), verifies the extremizer uniqueness and both recurrences, and tests a star's source–sink maximizers. Numeric checks of the two spectral roots at \(q=2,3,5\) are sanity tests only, not proofs. The successful exit message is `VERIFY_OK`.

## Relationship to prior work

The nullity degree of finite rings and its annihilator-counting interpretation were studied by Khasraw (2018 public preprint) and Dolžan (2022). Shumyatsky and Vannacci (2023 public preprint) proved structural consequences of **lower bounds** on product-zero probability; their results do not enumerate quiver orientations. Zaid, Sarmin, and Khasraw (2023) studied particular two-by-two matrix subsets over residue rings, not the radical-square-zero path algebra family or its orientation extremizers. Dolžan (2025 public preprint) established multiplication-probability results for simple and local rings; the present connected path algebras are nonlocal for \(n\ge2\). Vaso (2021) studied higher cluster tilting subcategories of the same broad family of radical-square-zero quiver algebras, with distinct hypotheses and invariants.

An earlier exact right-annihilator-dimension formula already covers **the all-quiver zero-product count** after evaluating its generating polynomial. Formula (1) is therefore presented solely as an explicit lemma for the optimization argument. Neither the existence of a generic annihilator count nor the transfer-matrix technique is claimed as new. The new assertions are the complete source–sink maximizing classification on bipartite multigraphs, the unique minimum and maximum path orientations for every length, and their strictly separated exponential rates. A prior cycle-specific transfer-matrix result covers coherent and alternating small cycle comparisons, not the full path extremal classification.

An exact commuting-tuple probability for radical-square-zero quiver algebras is a different invariant: it is unchanged by reversing arbitrary arrows, while the present one-sided zero-product probability already distinguishes the directed and alternating three-vertex paths over \(\mathbb F_2\), with probabilities \(55/256\) and \(59/256\). The generic combinatorial mechanism of a subgraph expansion is not asserted to be new in isolation. The mathematical assertions assessed as new are the sharp source–sink extremal characterization for bipartite graphs and both strict path extremizers with their exponential separation; the expansion is a supporting lemma, not an originality claim. No claim of comprehensive publication priority is made.

## Limitations

The expansion relies on the radical-square-zero relation and loopless arrows; it is not stated for full path algebras with nonzero products of arrows, for loops, or for arbitrary bound-quiver relations. The bipartite theorem identifies maxima but not minima on every graph; the minimum is determined here only for paths. The asymptotics hold for fixed finite-field cardinality while the number of path vertices grows. Direct exhaustive computation was performed only in small prime fields; the arbitrary-prime-power results rest on the counting and matrix arguments. The literature comparisons are limited to inspected accessible papers and records; a stronger undetected theorem about oriented graph partition functions or finite-algebra annihilator statistics remains a publication-priority risk. Independent mathematical validation has not been performed.

## References

1. S. M. S. Khasraw, *What is the probability that two elements of a finite ring have product zero?*, arXiv:1810.13312v1, publicly posted 2018-10-31. https://arxiv.org/abs/1810.13312
2. D. Dolžan, *The probability of zero multiplication in finite rings*, Bulletin of the Australian Mathematical Society 106 (2022), 83–88, publicly online 2022-01-24, DOI 10.1017/S0004972721001246. https://doi.org/10.1017/S0004972721001246
3. L. Vaso, *\(n\)-cluster tilting subcategories for radical square zero algebras*, arXiv:2105.05830v1, publicly posted 2021-05-12. https://arxiv.org/abs/2105.05830
4. P. Shumyatsky and M. Vannacci, *Commuting and product-zero probability in finite rings*, arXiv:2307.12633v1, publicly posted 2023-07-24. https://arxiv.org/abs/2307.12633
5. N. Zaid, N. H. Sarmin, and S. M. S. Khasraw, *The zero product probability of ring of matrices based on Euler's phi-function*, KZYJC 38 (2023), 2319–2326. https://people.utm.my/nizasarmin/wp-content/uploads/sites/980/2024/01/KZYJC_Nurhidayah.pdf
6. D. Dolžan, *The multiplication probability of a finite ring*, arXiv:2504.12886v1, publicly posted 2025-04-17. https://arxiv.org/abs/2504.12886
