# The conjugacy-class number of unicyclic height-two incidence-algebra unit groups

## Finding

**Theorem.** Let \(P\) be any finite height-two poset whose undirected comparability (equivalently, Hasse) graph \(G\) is connected and unicyclic. Write \(v=|P|\) and let \(\ell\ge4\) be the length of its unique cycle (necessarily even). Let \(k=\mathbb F_q\) be a field of any prime-power cardinality \(q\ge2\), let \(A=I(P,k)\) be the ordinary incidence algebra, and let \(U=A^\times\) be its unit group. The number of ordinary conjugacy classes of \(U\) is exactly
\[
\boxed{k(U)=q^v+(q-2)q^{v-\ell+1}.}
\]
In particular, this class number depends only on \(q\), the number of vertices, and the unique cycle length: the size and attachment pattern of every tree hanging from that cycle have no further effect. The group has order \(|U|=q^v(q-1)^v\). For fixed \(q>2\), the pair \((|U|,k(U))\) determines both \(v\) and \(\ell\) within this family; at \(q=2\), the unit group is abelian and \(k(U)=2^v\) cannot detect \(\ell\).

## Assumptions and scope

A height-two poset is a poset in which every strict comparability joins a minimal element to a maximal one; no chains of three distinct elements occur. Its comparability graph is therefore a simple bipartite graph. Unicyclic means connected with precisely one undirected simple cycle, so \(|E(G)|=|V(G)|=v\). All conjugations are internal to the full unit group, not only the subgroup of diagonal units. The incidence algebra has basis elements \(e_{xx}\) for vertices and \(e_{xy}\) for comparable distinct vertices \(x<y\), with multiplication \(e_{xy}e_{zw}=\delta_{yz}e_{xw}\). The Jacobson radical \(J\) is the span of the edge elements and satisfies \(J^2=0\). This excludes higher-height posets and graph-associated class-two nilpotent groups, which are different objects.

## Proof

Set \(Q=q-1\), and identify the diagonal torus with \(T=(k^\times)^V\). Every unit is uniquely \(t+a\) with \(t\in T\), \(a\in J\), and the multiplication is
\[
(t+a)(s+b)=ts+(tb+as).
\]
For an oriented comparability edge \(e=(x,y)\), \(x<y\), the radical coordinate of \(tb\) is \(t_xb_e\) and that of \(as\) is \(a_es_y\). In particular, diagonal coordinates are invariant under conjugation. Conjugating \(t+a\) by a radical unit \(1+b\) changes \(a_e\) by \((t_y-t_x)b_e\). Hence if \(t_x\ne t_y\), the entire coordinate \(a_e\) can be removed; if \(t_x=t_y\), that coordinate survives radical conjugation. Put \(E_t=\{xy\in E(G):t_x=t_y\}\). The remaining diagonal conjugations act on \(k^{E_t}\) by \(a_{xy}\mapsto (s_x/s_y)a_{xy}\).

For any fixed support \(S\subseteq E_t\) of nonzero edge coordinates, the number of orbits of these edge weights is \(Q^{\beta(S)}\), where \(\beta(S)=|S|-v+c(V,S)\) is the cycle rank of the spanning subgraph \((V,S)\). Indeed, the vertex-scaling homomorphism \(T\to(k^\times)^S\) has kernel consisting of scalars constant on each connected component of \((V,S)\); its image has size \(Q^{v-c(V,S)}\), leaving precisely \(Q^{|S|-v+c(V,S)}\) weight orbits. Therefore the number of conjugacy classes with fixed diagonal \(t\) is
\[
K(t)=\sum_{S\subseteq E_t}Q^{\beta(S)}.
\]
This orbit identity applies to every height-two poset. In the unicyclic case, \(\beta(S)=1\) exactly when \(S\) contains all \(\ell\) cycle edges; otherwise it is zero. Let \(\chi(t)=1\) if all cycle vertices have one and the same diagonal value, and \(\chi(t)=0\) otherwise. We obtain
\[
K(t)=2^{|E_t|}+(Q-1)\chi(t)2^{|E_t|-\ell}.
\]
The exponent in the second term is only used when \(\chi(t)=1\), when \(|E_t|\ge\ell\).

Evaluate the first sum over all \(t\in T\). It is the \(Q\)-color graph-coloring partition sum \(Z_G=\sum_t\prod_{xy\in E(G)}(1+\mathbf 1_{t_x=t_y})\). Summing over the color of a leaf multiplies the sum by \(2+(Q-1)=q\); deleting all attached trees leaves the unique cycle. Thus
\[
\sum_{t\in T}2^{|E_t|}=q^{v-\ell}\operatorname{tr}(M^\ell),
\qquad M=I_Q+\mathbf 1\mathbf 1^\mathsf T.
\]
The eigenvalues of \(M\) are \(q\) once and \(1\) with multiplicity \(Q-1\), so this equals \(q^{v-\ell}(q^\ell+q-2)\). For the correction, choose the common cycle color in \(Q\) ways and sum independently over each attached tree vertex, each contributing a factor \(q\):
\[
\sum_{t:\chi(t)=1}2^{|E_t|-\ell}=Qq^{v-\ell}.
\]
Consequently
\[
\begin{aligned}
k(U)&=q^{v-\ell}(q^\ell+q-2)+(Q-1)Qq^{v-\ell}\\
&=q^v+(q-2)q^{v-\ell+1},
\end{aligned}
\]
as claimed. Since every unit has \(v\) independent nonzero diagonal entries and \(v\) independent arbitrary edge entries, \(|U|=(q-1)^vq^v\). If \(q>2\), increasing the allowed even cycle length strictly decreases the positive correction \((q-2)q^{v-\ell+1}\), while \(|U|\) determines \(v\), proving the final assertion. If \(q=2\), the diagonal group is trivial and \(U=1+J\) is abelian because \(J^2=0\).

## Verification

The included standalone `verify.py` uses only the Python standard library and prints `VERIFY_OK` after two independent checks. First it enumerates actual conjugacy orbits using diagonal and radical conjugation generators over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (using the polynomial \(u^2+u+1\) for \(\mathbb F_4\)). Second it counts commuting pairs from the original incidence-algebra multiplication, without using the support-orbit formula, and applies the finite-group identity \(k(U)=|\{(g,h)\in U^2:gh=hg\}|/|U|\). The tests cover the four-cycle, six-cycle, and three distinct tree-attachment patterns with \(v\le6\), at field orders \(2,3,4,5\) where feasible: 11 direct orbit enumerations and 16 independent commuting-pair enumerations. Example results: for a bare four-cycle, \(k(U)=84\) at \(q=3\) and \(264\) at \(q=4\); for a bare six-cycle, the corresponding counts are \(732\) and \(4104\); for a four-cycle with two attached vertices, they are \(756\) and \(4224\). These experiments check finite cases only; the theorem for every \(v\), \(\ell\), and \(q\) follows from the proof.

## Relationship to prior work

General structural and functorial descriptions of incidence-algebra unit groups, including the diagonal-unit criterion, are established in the cited work of e Silva. Dugas, Herden, and Rebrovich investigate normal and maximal abelian subgroups of incidence-algebra unit groups. The present theorem concerns a different and more numerical invariant: the exact total number of conjugacy classes, for every finite connected unicyclic height-two poset. Rossmann's graphical groups also have graph-polynomial conjugacy enumerators, but those groups are class-two nilpotent graph groups, not the unit groups of the height-two incidence algebras here; the results are not interchangeable. The vertex-gauge action and elementary cycle transfer matrix are acknowledged mathematical ingredients, not independently claimed innovations. The exact unicyclic unit-group class-number formula and its cycle-length rigidity are the specific assessed contribution.

## Limitations

The theorem assumes a finite field and a height-two poset with connected, unicyclic comparability graph. It does not count conjugacy classes for higher-height incidence algebras or arbitrary multi-cycle graphs. Conjugacy classes are those of the full algebra unit group and not isomorphism classes of algebras or graph groups. The literature comparison is not an exhaustive proof of publication priority; a general torus-action or pattern-group orbit formula could encompass this statement. Complete publisher full-text access to the 2020 normal-subgroup paper was unavailable for this comparison, although relevant accessible introductory and theorem sections were inspected. No independent mathematical audit has been carried out.

## References

1. J. V. P. e Silva, *Topological incidence rings and the incidence functor*, arXiv:2310.13238 (initial public version 2023-10-20). The inspected open preprint includes its sections on incidence-ring units and solvability.
2. M. Dugas, D. Herden, J. Rebrovich, *Normal subgroups of the group of units of incidence algebras*, Linear Algebra and its Applications **586** (2020), 64–88, DOI:10.1016/j.laa.2019.10.017.
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bulletin of the London Mathematical Society **54** (2022), 1923–1943, DOI:10.1112/blms.12665.
