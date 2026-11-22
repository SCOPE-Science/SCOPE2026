# Complete marked-query shattering polynomial for three-colourings of double stars

## Finding

Let \(D_{a,b}\), for integers \(a,b\ge1\), be the tree with two adjacent hubs, \(a\) pendant leaves at the first hub and \(b\) at the second. Let the hypotheses be all proper colourings with the three *named* colours \(\{1,2,3\}\), represented on the query domain \(V(D_{a,b})\times\{1,2,3\}\) by binary vertex--colour equalities. Write \(s_j(a,b)\) for the number of *query sets*, not merely vertex projections, of size \(j\) that are VC-shattered, and define \(\Phi_{a,b}(z)=\sum_j s_j(a,b)z^j\).

Put
\[
X_t(z)=(1+z)^t,\qquad Y_t(z)=(1+2z)^t,\qquad
L_t(z)=1+3Y_t(z)-3X_t(z),\qquad D_t(z)=1+Y_t(z)-2X_t(z).
\]
**Theorem.** For all integers \(a,b\ge1\), the *complete* marked-query shattering polynomial is
\[
\begin{aligned}
\Phi_{a,b}(z)={}&L_a(z)L_b(z)-3D_a(z)D_b(z)\\
&+z\Bigl[6X_a(z)\bigl(X_b(z)+Y_b(z)-1\bigr)-9X_b(z)+6\\
&\qquad\ +6X_b(z)\bigl(X_a(z)+Y_a(z)-1\bigr)-9X_a(z)+6\Bigr]\\
&+6z^2\bigl(X_a(z)+X_b(z)-1\bigr).
\end{aligned}
\]
It has degree \(a+b+1\), and its highest coefficient is
\[
\boxed{s_{a+b+1}(a,b)=6\bigl(2^a+2^b+2+\mathbf 1_{a=1}+\mathbf 1_{b=1}\bigr).}
\]
For fixed \(a+b\), this *one coefficient* determines the unordered pair \(\{a,b\}\) and therefore the isomorphism type of the double star. For example, \(D_{1,3}\) and \(D_{2,2}\) both have six vertices and VC dimension five, but their top marked-query coefficients are respectively \(78\) and \(60\). The VC-dimension statement is included for orientation, **not** claimed as a new scalar result.

## Assumptions and scope

All vertices of the tree are distinguished and all three colours are named; proper means the ends of every edge receive different colours. No surjectivity onto the three colours is imposed. A query \((v,c)\) asks whether the colouring assigns colour \(c\) to vertex \(v\). A query support is shattered if every assignment of binary answers to it extends to a proper colouring. The polynomial counts individual query supports in \(V\times\{1,2,3\}\). In particular, a set of selected vertices can contribute between zero and many query supports depending on the colour targets; this is **not** the face polynomial counting selected vertex sets admitting at least one suitable target assignment. The empty query set is shattered. The integer parameters satisfy \(a,b\ge1\) without any bound on their size.

## Proof

**1. Three-colour feasibility lemma.** A shattered query set contains at most one query per vertex: two different colour equalities at one vertex could not both be answered positively. Let \(U\subseteq\{1,2,3\}\) be the set of *distinct colour targets* among the queried left leaves, and \(V\) the analogous set for the right leaves. If queried, let the left and right hub targets be \(p\) and \(q\), respectively. Write \(x\) and \(y\) for the actual hub colours.

For each specified binary pattern on the queried hubs, a complete answer pattern on all queried vertices is realizable **if and only if** there exist \(x,y\in\{1,2,3\}\) with \(x\ne y\), \(x\notin U\), \(y\notin V\), and with the required equality/inequality answers for the marked hubs. The forward implication follows by selecting the trace with *every queried leaf positive*. Conversely, choose such hub colours for the given hub pattern, independently of the arbitrary leaf answers. Each positive leaf can receive its target colour, which differs from its hub. A negative leaf can receive one of the three colours different from both its target and its hub; such a colour always exists. Distinct leaves have no mutual edges. This proves the lemma for every pattern and every size of the leaf sets.

**2. Feasible centre profiles.** If neither hub is queried, the lemma reduces to the existence of distinct \(x\notin U\) and \(y\notin V\). This holds exactly when each target set has size at most two, excluding the case \(|U|=|V|=2\) and \(U=V\). Indeed, the allowed hub-colour sets are nonempty, and a pair of nonempty sets has no distinct representatives precisely when both are the same singleton.

If just the left hub is queried, the set of feasible left hub colours is
\[
A(U,V)=\{x\in\{1,2,3\}\setminus U:\exists y\in\{1,2,3\}\setminus V,\ y\ne x\}.
\]
Its target \(p\) can be shattered in both binary states precisely when \(p\in A(U,V)\) and \(|A(U,V)|\ge2\). This gives the following exhaustive cases for the number of possible hub target colours: \(3\) when \(U=\varnothing\) and \(|V|\le1\); \(2\) when \(U=\varnothing\) and \(|V|=2\); \(2\) when \(|U|=1\) and \(|V|\le1\); \(2\) when \(U=\{u\}\) and \(V=\{1,2,3\}\setminus\{u\}\); and zero otherwise. The case with only the right hub is symmetric.

When both hubs are queried, all four hub-answer pairs must be feasible. This occurs in exactly three disjoint situations: (i) \(U=V=\varnothing\) and \(p\ne q\), giving six ordered hub targets; (ii) \(U=\{u\}\), \(V=\varnothing\), \(p\ne u\), \(q=u\), giving two hub targets per fixed \(u\); (iii) \(U=\varnothing\), \(V=\{v\}\), \(p=v\), \(q\ne v\), again two per fixed \(v\). To see exhaustiveness, if both leaf sets are nonempty and feasible then the allowed centre-colour sets each have at most two members, hence admit at most three *distinct* ordered pairs \((x,y)\), too few for four binary hub patterns. If either side admits only one centre colour, its own hub bit cannot vary. The remaining cases with one side unrestricted and the other side allowing two colours give the stated target restrictions by direct inspection of the three named colours.

**3. Enumerating queried leaves.** For a fixed set of \(i\ge1\) leaf positions, there are \(3(2^i-1)\) assignments of their target colours using at most two distinct names. Including the choice of positions and the empty set gives \(L_t(z)=1+3Y_t(z)-3X_t(z)\) for a leaf bank of size \(t\). For one *fixed pair* of colour names, the target assignments using both names are enumerated by \(D_t(z)=Y_t(z)-2X_t(z)+1\). Thus the no-hub contribution is \(L_aL_b-3D_aD_b\), subtracting the three equal two-colour-palette pairs.

Write \(H_t(z)=X_t(z)-1\) for the generating polynomial of nonempty queried subsets with a prescribed single colour target, and \(B_t(z)=1+3H_t(z)=3X_t(z)-2\) for target assignments using at most one distinct colour. When only the left hub is queried, the centre-profile cases in step 2 contribute, in order,
\[
3B_b+6D_b+6H_aB_b+6H_aD_b
=(6X_a-3)(3X_b-2)+6X_aD_b.
\]
Simplifying this gives \(6X_a(X_b+Y_b-1)-9X_b+6\). The right-hub-only contribution is its \(a,b\)-interchange. If both hubs are queried, the centre-profile cases give \(6+6H_a+6H_b=6(X_a+X_b-1)\). Multiplying by \(z\) per queried hub and adding all cases proves the displayed polynomial for *every* \(a,b\ge1\).

**4. Top rank and exact coefficient.** Every vertex can have at most one query in a shattered support, and a support querying *all* vertices cannot be shattered: then both hubs are queried and each of the two leaf banks is nonempty, a case excluded in step 2. Conversely, query all leaves for colour one and the left hub for colour two. Both hub answers can be realized with the opposite hub assigned the remaining appropriate colour; independent choices at leaves then realize all binary patterns. Thus the degree is \(a+b+1\). To compute the coefficient, omit exactly one vertex. Omitting the left or right hub gives respectively \(6(2^a+1)\) and \(6(2^b+1)\) admissible target assignments, as follows from the highest terms of the single-hub expressions. Omitting a left leaf leaves both hubs queried, which is possible only if \(a=1\), contributing six assignments; symmetrically for a right leaf if \(b=1\). Summing gives the stated top coefficient.

**5. Reconstruction from one coefficient.** Fix \(s=a+b\) and take \(1\le a\le b=s-a\). After removing the known additive term two and factor six, the top coefficient is \(T_s(a)=2^a+2^{s-a}+\mathbf1_{a=1}+\mathbf1_{s-a=1}\). If \(s\ge3\), for every \(1\le a<\lfloor s/2\rfloor\),
\[
T_s(a)-T_s(a+1)=2^{s-a-1}-2^a+\mathbf1_{a=1}>0.
\]
The inequality holds because \(s\ge 2a+2\). For \(s=2\) the only unordered pair is \(\{1,1\}\). Hence knowing \(s\) and the top coefficient uniquely determines the unordered arm-size pair.

## Verification

The standalone `verify.py` uses only the Python standard library. It directly enumerates every proper colouring of eleven double-star parameter pairs, every possible query support on those vertices (four choices per vertex: no query or one of three named colour tests), and the full binary trace of each support. It separately checks the centre-feasibility condition against these traces, computes all predicted polynomial coefficients from binomial expansions, and compares every coefficient. The largest checked trees have eight vertices. Across the eleven parameter pairs, exactly \(256256\) possible query-support profiles were tested, and all comparisons passed. Further exact integer polynomial and highest-coefficient arithmetic checks passed for all \(121\) pairs with \(1\le a,b\le11\). Run `python3 verify.py` from the directory containing the file. The finite verification is a cross-check; the unlimited two-parameter theorem follows from proof steps 1--5.

## Relationship to prior work

Blanca, Chen, Štefankovič and Vigoda (2017) treat proper graph colourings as hard-constraint graph-homomorphism samples but recover an *unknown graph*, whereas here the graph is fixed and the hypotheses are its individual proper colourings under vertex--colour Boolean questions. Guingona, Kolesnikov, Nierwinski and Soucy (2021) establish sharp VC/Littlestone ranks for zero sets of nontrivial linear combinations of independent functions, not an exact colouring-query polynomial. Walker (2022) gives general tree-dimension and Sauer--Shelah shattering theory, with no double-star colouring enumerator.

Existing work on proper three-colouring shattering of paths, small trees and complete bipartite graphs concerns other graph classes or a vertex *projection* rather than the complete query-pair counts. In particular, an earlier double-star result counts which **vertex subsets** admit *some* shattering colour targets and describes their projected complex. The present theorem does not reclaim that vertex-projected classification, its VC dimension or its topology: it counts **all individual marked target assignments**, a finer invariant that is not determined by the existence of one target assignment per vertex set. For instance, with two queried leaves and one queried hub, some choices of hub target are shattered while others are not. The complete-bipartite result is also not an implication: a complete bipartite graph has strictly more edges, hence a different proper-colouring family; its polynomial cannot be substituted into this theorem. Search by synonyms and related published statements did not locate an identical marked-query formula, but this is not an absolute priority proof.

## Limitations

Only three named colours, nonempty leaf banks, proper vertex colourings and binary equality questions are covered. The displayed polynomial does not count ordinary proper colourings, whole-colour prediction queries, or the vertex-projected support complex. No adaptive dimension or homotopy equivalence for the full marked-query complex is asserted. Finite experiments alone cannot establish the unbounded formula; the case analysis is the proof. An independently conducted mathematical audit has not been performed. Unindexed equivalent literature could affect historical priority.

## References

1. A. Blanca, Z. Chen, D. Štefankovič and E. Vigoda, *Structure Learning of H-colorings*, first public version 17 August 2017, arXiv:1708.05118, https://arxiv.org/abs/1708.05118.
2. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, first public version 10 September 2021, arXiv:2109.04805, https://arxiv.org/abs/2109.04805.
3. R. Walker, *Tree Dimension and the Sauer--Shelah Dichotomy*, first public version 23 March 2022, arXiv:2203.12211, https://arxiv.org/abs/2203.12211.
4. *The first branching obstruction to three-colouring shattering on trees*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-first-branching-obstruction-to-three-colouring-shattering-on--6dd09fced05e.
5. *Exact shattering polynomial and palette transition for complete-bipartite proper colourings*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-shattering-polynomial-and-palette-transition-for-complete--69c08503d33f.
