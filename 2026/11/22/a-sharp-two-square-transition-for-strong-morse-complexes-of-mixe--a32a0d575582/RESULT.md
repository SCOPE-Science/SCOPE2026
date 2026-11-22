# A sharp two-square transition for strong Morse complexes of mixed polygon bouquets

## Finding
For integers \(p,q\ge 1\), let \(G_{p,q}\) be the connected one-dimensional simplicial graph formed by identifying one common vertex of \(p\) *unfilled triangles* and \(q\) *unfilled squares*, all remaining vertices disjoint. Let \(\mathcal{SM}(G_{p,q})\) denote the **full strong discrete-Morse matching complex** of Knudson and Owens–White: the simplicial downward closure of the vertex–edge incidence matchings produced by injective vertex filtrations, not the ordinary Morse complex or the pure strong complex.

**Theorem (complete mixed triangle–square classification).** For every such \(p,q\),
\[
|\mathcal{SM}(G_{p,q})|\simeq
\begin{cases}
\displaystyle\bigvee^{3^p+4} S^{p+1},&q=1,\\
\displaystyle\bigvee^{3^p}S^{p+2q-1},&q\ge2.
\end{cases}
\]
For \(q\ge2\) there is, more strongly, a sequence of elementary simplicial collapses onto \(D_4^{*p}*C_6^{*q}\), where \(D_4\) denotes a four-point discrete complex and \(C_6\) a six-vertex circle. All reduced integral homology groups are therefore free; they are concentrated in the single degree and have the rank displayed above. The entire face enumerator, including its constant term for the empty face, is
\[
\begin{aligned}
F_{p,q}(z)={}&(1+4z)^p(1+6z+6z^2)^q\\
&+2pz(1+2z)^{p-1}(1+4z+3z^2)^q\\
&+2qz(1+3z)(1+2z)^p(1+4z+3z^2)^{q-1}.
\end{aligned}
\]
In particular, these complexes are pure of dimension \(p+2q-1\), but the number of top-dimensional sphere summands drops by exactly four upon passing from one to at least two square petals, with a concomitant two-dimensional increase in sphere dimension when adding a second square.

## Assumptions and scope
The graph is regarded strictly as a one-dimensional simplicial complex, even at triangular cycles: no graph cycle is filled with a two-simplex. Write its shared vertex as \(o\), its triangle-petal vertices as \(a_i,b_i\) (edges \(oa_i,a_ib_i,b_io\)) for \(1\le i\le p\), and its square-petal vertices as \(u_j,v_j,w_j\) (edges \(ou_j,u_jv_j,v_jw_j,w_jo\)) for \(1\le j\le q\). No vertices besides \(o\) are identified across petals.

An oriented incidence \([x\to y]\) is the Hasse pair consisting of vertex \(x\) and edge \(\{x,y\}\). If a total ordering of graph vertices is fixed, then \([x\to y]\) appears in the associated strong gradient **if and only if** \(y\) is the unique neighbor of \(x\) preceding \(x\) in that ordering. Indeed, the descending link in a one-dimensional simplicial graph is discrete and is a nonempty cone exactly when it consists of one vertex. Every subset of any such strong gradient belongs to the full complex.

For triangle \(i\), put
\[
D_i=\{[a_i\to b_i],[b_i\to a_i],[a_i\to o],[b_i\to o]\},\quad E_i=\{[a_i\to o],[b_i\to o]\},
\]
with \(D_i\) and \(E_i\) considered discrete zero-dimensional complexes. For square \(j\), abbreviate its six non-hub oriented incidences by
\[
A_j=[u_j\to o],\ B_j=[v_j\to u_j],\ C_j=[w_j\to o],\ D_j=[v_j\to w_j],\ E'_j=[u_j\to v_j],\ F_j=[w_j\to v_j].
\]
Let \(L_j\) be the six-edge cycle with edges \(A_jB_j,A_jC_j,C_jD_j,D_jE'_j,E'_jF_j,F_jB_j\). Let \(H_j\subset L_j\) be the three-edge path \(A_jB_j,A_jC_j,C_jD_j\). Let \(T_{j,u}\) be the discrete triple \(\{B_j,C_j,E'_j\}\), and \(T_{j,w}\) the discrete triple \(\{F_j,A_j,D_j\}\).

## Proof
**1. Exact no-hub subcomplex.** Enumerating the relative vertex orders within a triangle shows that any filtration contributes at most one of its four atoms \(D_i\), and every one is realizable. Enumerating the 24 orders of \(o,u_j,v_j,w_j\) within a square shows that, when hub-rooted incidences are discarded, the maximal local faces are precisely the six edges of \(L_j\). The local orders in different petals can always be interleaved globally: put all local vertices required to precede \(o\) before \(o\), and all others after \(o\), preserving each local order. Consequently the subcomplex of faces **without any incidence rooted at \(o\)** is exactly
\[
X=\Bigl(*_{i=1}^{p}D_i\Bigr)*\Bigl(*_{j=1}^{q}L_j\Bigr)\cong D_4^{*p}*C_6^{*q}.
\]
Each four-point \(D_i\) is a wedge of three zero-spheres, and \(L_j\simeq S^1\). Join distributivity and the suspension identity yield
\[
|X|\simeq\bigvee^{3^p} S^{p+2q-1}.
\]
This is the **actual** join decomposition and not an assumption that strong Morse complexes preserve vertex wedges.

**2. Every face involving the hub.** There is at most one incidence rooted at \(o\), because it pairs the same Hasse vertex. If \([o\to a_i]\) or \([o\to b_i]\) occurs, its indicated leaf is the only neighbor of \(o\) preceding \(o\). No other non-hub incidence from the distinguished triangle can occur, all other triangles contribute one of their two inward incidences \(E_k\), and every square contributes a face in the path \(H_j\). Conversely all these local choices are jointly realizable by interleaving relative orders. Thus each of the two hub-incidence vertices of triangle \(i\) has link exactly
\[
B_i=\Bigl(*_{k\ne i}E_k\Bigr)*\Bigl(*_{j=1}^{q}H_j\Bigr).
\]
If instead \([o\to u_j]\) (respectively \([o\to w_j]\)) occurs, its distinguished square contributes a face from \(T_{j,u}\) (respectively \(T_{j,w}\)), every other square contributes a face from its \(H_k\), and every triangle contributes a face from its \(E_i\). The two corresponding links are exactly
\[
Q_{j,t}=T_{j,t}*\Bigl(*_{i=1}^{p}E_i\Bigr)*\Bigl(*_{k\ne j}H_k\Bigr),\qquad t\in\{u,w\}.
\]
Here each link is a subcomplex of \(X\), and the stars of distinct hub-incidence vertices meet **only inside** \(X\). These formulas classify every face of \(\mathcal{SM}(G_{p,q})\).

**3. At least two square petals: a genuine simplicial collapse.** Each \(H_j\) is a three-edge path, hence is nonempty and simplicially collapsible. A join with a nonempty collapsible factor is collapsible. For \(q\ge2\), every \(B_i\) contains such a factor, and every \(Q_{j,t}\) contains \(H_k\) for at least one \(k\ne j\); hence **all** hub-incidence links are collapsible. If a vertex \(h\) has collapsible link \(L\), then \(h*L\) collapses *relative to its base \(L\)* by lifting a collapse of \(L\) to the cone and finally removing \(h\) with its final incident edge. Applying this to the hub-incidence vertices one by one deletes every face outside \(X\), since no simplex contains two such vertices. Therefore
\[
\mathcal{SM}(G_{p,q})\searrow X,\qquad q\ge2.
\]
The join homotopy computation in Step 1 proves the second case of the theorem, integrally and at the level of simple homotopy.

**4. Exactly one square: two nontrivial cone attachments.** For \(q=1\), every triangle hub-incidence link \(B_i\) contains \(H_1\), so all \(2p\) triangle-rooted hub apices can again be removed by relative elementary collapses. The two square-rooted apices remain. Their common-type link is
\[
Q=T_3*E_1*\cdots*E_p\simeq
\bigvee^{2}S^{p},
\]
where \(T_3\) is a discrete three-point complex and each \(E_i\cong S^0\). The base \(X\simeq\bigvee^{3^p}S^{p+1}\) is \(p\)-connected for \(p\ge1\). Consequently the inclusion \(Q\hookrightarrow X\) is nullhomotopic: \(Q\) has the homotopy type of a wedge of \(p\)-spheres, while \(\pi_p(X)=0\). Each of the two square-apex cones therefore attaches along a nullhomotopic map, contributing the suspension \(\Sigma Q\simeq\bigvee^2S^{p+1}\). Their interiors are disjoint, so their contributions add without further identifications. Altogether
\[
|\mathcal{SM}(G_{p,1})|\simeq |X|\vee\Sigma Q\vee\Sigma Q
\simeq\bigvee^{3^p+4}S^{p+1}.
\]
This argument uses vanishing of the appropriate **homotopy** group, not merely vanishing of homology or a numerical Euler-characteristic inference.

**5. Exact face enumeration and purity.** Write \(F_Y(z)=\sum_{r\ge0}f_{r-1}(Y)z^r\), with the empty face counted once. Joins multiply their enumerators. The factors \(D_i,E_i,L_j,H_j,T_{j,t}\) respectively have enumerators \(1+4z,1+2z,1+6z+6z^2,1+4z+3z^2,1+3z\). Step 1 supplies the first term of the stated \(F_{p,q}\); the \(2p\) distinct triangle hub apices contribute the second term, and the \(2q\) distinct square hub apices contribute the third term. Since no face has two hub apices, there is no double counting. Every maximal no-hub simplex has \(p+2q\) vertices. Every hub-apex link has maximal faces with exactly \(p+2q-1\) vertices, proving purity of dimension \(p+2q-1\). \(\square\)

## Verification
The accompanying standalone Python 3 standard-library program `verify.py` enumerates **every** strict vertex order independently of the join-and-cone construction, builds every strong incidence matching using the unique-earlier-neighbor criterion, and takes its complete downward closure. Independently it constructs the proposed local \(D,E,L,H,T\) pieces and compares the **entire sets of simplices**, not only their face numbers. The checker also computes mod-two boundary ranks, compares the full face polynomial coefficient by coefficient, and, for the two-square profiles, explicitly verifies every relative elementary collapse to the actual no-hub join. Full enumeration passes for \((p,q)=(1,1),(2,1),(1,2)\), as well as four known one-type boundary profiles. The new mixed cases yield respectively \(105,493,1357\) total faces including the empty face, and reduced mod-two ranks \(7\) in degree 2, \(13\) in degree 3, and \(3\) in degree 4. For \((1,2)\), exactly 256 elementary collapse pairs delete all hub-apex faces.

Run `python3 verify.py` in a directory containing the script; no third-party packages are needed. The finite tests corroborate the proof, but the unrestricted theorem is established by the symbolic join/link and attachment arguments in Steps 1–4. Mod-two rank computations alone would not exclude integral torsion; the explicit integral homotopy equivalences do so.

## Relationship to prior work
Knudson and Owens–White introduced this full strong matching complex, determined several single-graph families, and proved a join theorem for **disjoint unions**. Their arXiv:2609.06844v1, Sections 3–4, 8 and 10, does not determine bouquets with a **shared** hub. Published follow-up calculations establish the all-triangle friendship-graph case \(q=0\), the all-square case \(p=0,q\ge2\), and finite mixed cases \((p,q)=(1,1),(2,1)\). Those are genuine prior coverage and are **not claimed as new** here. Their statements do not imply the uniform mixed family with arbitrary \(p\ge1\), \(q\ge2\), nor the general \(q=1\) formula for all \(p\). The present two-parameter theorem explains the sharp two-square transition by links becoming collapsible. The ordinary Morse-matching complex and ordinary edge matching complex are different constructions; their results do not imply this strong-filtering classification.

## Limitations
The cycles must be unfilled triangles and squares with precisely one common vertex and otherwise disjoint vertex sets. The theorem treats the full strong matching complex, not its pure subcomplex, the ordinary Morse complex, or filled clique complexes. It determines ordinary integral and, for \(q\ge2\), simple homotopy; it does not determine integral equivariant symmetry modules, canonical attaching maps relative to other topological constructions, or other polygon lengths. Previously published special cases are not new, and unindexed equivalent literature may exist. The complete finite checks cover selected small parameters; the all-parameter argument is mathematical rather than computational extrapolation. No independent mathematical audit has been performed.

## References
1. K. P. Knudson and A. Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first publicly posted 2026-09-06, especially Definitions 3.2 and 4.2 and Section 10, https://arxiv.org/abs/2609.06844 .
2. *Strong Morse complexes of friendship graphs: an exponential sphere-wedge formula*, publicly available mathematical research record, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-strong-morse-complexes-of-friendship-graphs-an-exponential-spher--c88f401c5072 .
3. *A six-cycle join core for strong Morse matching complexes of square bouquets*, publicly available mathematical research record, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-six-cycle-join-core-for-strong-morse-matching-complexes-of-squ--d0ea73d39bd5 .
4. *First mixed-dimensional strong-Morse homotopy in triangle–cycle bouquets*, publicly available mathematical research record, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-first-mixed-dimensional-strong-morse-homotopy-in-triangle-cycle--faf3b520e7e7 .
5. *Thirteen three-spheres and the full symmetry character of a mixed three-petal strong-Morse complex*, publicly available mathematical research record, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-thirteen-three-spheres-and-the-full-symmetry-character-of-a-mixe--9a657e6e0edb .
