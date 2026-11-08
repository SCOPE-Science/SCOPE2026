# Integral homotopy and deck symmetry of wheel Mycielskians

## Finding

Let \(W_n=K_1\vee C_n\) be the wheel with an \(n\)-vertex rim, \(n\ge5\). The join in this graph expression means that the hub is adjacent to every rim vertex; it is **not** a topological wedge. For \(\ell\ge0\), let \(\mu_\ell(W_n)\) be the generalized Mycielskian defined below, and let \(I(G)=\operatorname{Ind}(G)\).

Define integers \(e_m,a_m\) for \(m\ge3\) by
\[
(e_m,a_m)=\begin{cases}(2,t-1)&m=3t,\\(1,t-1)&m=3t+1,\\(1,t)&m=3t+2.\end{cases}
\]
Set \(e=e_n\), \(a=a_n\), and
\[
(z,d)=\begin{cases}(e_{2n},a_{2n})&n\text{ odd},\\(e_n^2,2a_n+1)&n\text{ even}.\end{cases}
\]
All the dimensions below are at least one except for the explicitly stated zero-parameter case. Let \(c_{k,r}=\binom{k}{r}z^r\) for \(0\le r\le k\). In each display, repeated sphere dimensions are combined by summing multiplicities.

**Complete classification.** For \(k\ge0\),
\[
I(\mu_{3k+2}(W_n))\simeq\bigvee_{r=0}^{k+1}\bigvee^{\binom{k+1}{r}z^r}S^{2k+1+r(d-1)},
\]
\[
I(\mu_{3k+1}(W_n))\simeq\bigvee_{r=0}^{k}\left(\bigvee^{c_{k,r}}S^{2k+1+r(d-1)}\ \vee\ \bigvee^{ec_{k,r}}S^{a+2k+1+r(d-1)}\right).
\]
For \(k\ge1\),
\[
I(\mu_{3k}(W_n))\simeq\bigvee_{r=0}^{k}\left(\bigvee^{2c_{k,r}}S^{2k+r(d-1)}\ \vee\ \bigvee^{ec_{k,r}}S^{a+2k+r(d-1)}\right).
\]
At \(\ell=0\),
\[
I(\mu_0(W_n))\simeq\left(\bigvee^e S^a\right)\sqcup\{p\}\sqcup\{q\}.
\]
All equivalences are of ordinary geometric homotopy types over the integers, hence determine integral homology with no torsion.

**Structural refinement.** For every nonempty finite loopless simple graph \(H\), writing \(B(H)=H\times K_2\) for its Kronecker double cover and \(H^+=K_1\vee H\) for its cone graph, there is a homotopy equivalence
\[
I(B(H^+))\simeq I(B(H))\vee S^1.
\]
In particular \(I(B(W_n))\simeq S^1\vee\bigvee^z S^d\), where \(d\ge2\). Its first integral homology is canonically infinite cyclic up to choice of orientation. The involution exchanging the two sheets of \(B(W_n)\) acts by multiplication by \(-1\) on this group, whereas every rim dihedral automorphism, lifted without exchanging sheets, acts by \(+1\).

## Assumptions and scope

All graphs are finite, simple, loopless, undirected. The wheel \(W_n\) has vertices \(\{0,\ldots,n-1,h\}\), edges \(\{i,i+1\}\) with indices modulo \(n\), and all edges \(\{h,i\}\). In the categorical (Kronecker) product \(B(G)=G\times K_2\), the vertices are \((v,s)\) with \(s\in\{0,1\}\), and \((u,0)\) is adjacent to \((v,1)\) exactly when \(uv\) is an edge of \(G\).

The graph \(\mu_\ell(G)\) has \(\ell+1\) vertex layers \(V(G)\times\{0,1,\ldots,\ell\}\) and one apex \(w\); its edges include crossed copies of each \(G\)-edge between consecutive layers, all original \(G\)-edges within the final layer, and an apex edge from \(w\) to every vertex in the first layer. There are no other edges. At \(\ell=0\) this is the cone graph. This is the indexing in Carnero Bravo's Theorem 5 [1].

The symbol \(\bigvee^m S^d\) denotes a one-point wedge of \(m\) spheres. When \(m=0\), the pointed wedge is a point. The symbol \(\sqcup\) denotes disjoint topological union, not a wedge.

## Proof

**Step 1: a universal cone-cover splitting.** Let \(H\) have nonempty vertex set \(V\), with hubs \(h_0,h_1\) in \(B(K_1\vee H)\), and let \(Z=I(B(H))\) on the rim copies \(V_0,V_1\). Every subset of \(V_s\) is independent, hence the full simplices \(P_s=\Delta(V_s)\) lie in \(Z\). Since no vertex is adjacent to its own opposite-sheet copy, \(\{(v,0),(v,1)\}\) is an independent edge for each \(v\in V\), connecting \(P_0\) and \(P_1\) within \(Z\). Thus \(Z\) is path connected.

Every independent face involving \(h_s\) but not the other hub lies in the simplex \(h_s*P_s\), since the hub is adjacent to every rim vertex of the opposite sheet. A face containing both hubs contains no rim vertices, and the two hubs span precisely one extra edge. Consequently,
\[
I(B(K_1\vee H))=Z\cup(h_0*P_0)\cup(h_1*P_1)\cup\{h_0,h_1\}.
\]
The two cones intersect the preceding union along their full simplex bases \(P_s\). Since each base is contractible, collapsing both cones relative to their bases gives a homotopy equivalence from the union without the final hub edge to \(Z\). Reattaching that edge between two points of the path-connected complex \(Z\) increases its homotopy type by one \(S^1\): formally, the attaching maps from \(S^0\) land in the same path component, so the homotopy pushout is \(Z\vee S^1\). This proves the universal splitting without any unstated connectivity requirement on \(H\).

**Step 2: specialize the rim.** For \(H=C_n\), the cover \(B(C_n)\) is \(C_{2n}\) if \(n\) is odd and the disjoint union of two copies of \(C_n\) if \(n\) is even. The classical cycle formula [2,3] is \(I(C_m)\simeq\bigvee^{e_m}S^{a_m}\). Graph disjoint unions become joins of independence complexes. Since \(S^p*S^q\simeq S^{p+q+1}\) and the join distributes over nontrivial pointed sphere wedges up to homotopy, we obtain \(I(B(C_n))\simeq\bigvee^z S^d\). Here \(d\ge2\) for \(n\ge5\). Step 1 then implies \(D:=I(B(W_n))\simeq S^1\vee\bigvee^z S^d\).

The hub is adjacent to all rim vertices in \(W_n\), so \(I(W_n)=I(C_n)\sqcup\{h\}\simeq\left(\bigvee^e S^a\right)\sqcup\{h\}\), with \(a\ge1\). Relative to a basepoint in the circle wedge, the standard suspension/join identities give
\[
D^{*j}\simeq\bigvee_{r=0}^{j}\bigvee^{\binom jr z^r} S^{2j-1+r(d-1)}\qquad (j\ge1),
\]
\[
I(W_n)*D^{*j}\simeq\bigvee_{r=0}^{j}\left(\bigvee^{\binom jr z^r}S^{2j+r(d-1)}\vee\bigvee^{e\binom jr z^r}S^{a+2j+r(d-1)}\right).
\]
To justify the disconnected join formula, regard \(I(W_n)\) as a based homotopy equivalent of \(S^0\vee\bigvee^e S^a\), then use \(X*Y\simeq\Sigma(X\wedge Y)\) for based models with the usual reduced join; the isolated component contributes the suspension of \(D^{*j}\). These are homotopy statements about spaces, not merely formal Betti-number identities.

**Step 3: all Mycielskian orders.** By Theorem 5 of [1], for \(\ell=3k\), \(3k+1\), \(3k+2\), respectively,
\[
I(\mu_\ell(G))\simeq\begin{cases}I(G)*I(B(G))^{*k}\vee\Sigma I(B(G))^{*k},&\ell=3k,\\\Sigma\big(I(G)*I(B(G))^{*k}\big),&\ell=3k+1,\\I(B(G))^{*(k+1)},&\ell=3k+2.\end{cases}
\]
Substituting \(G=W_n\) and the two preceding join formulas yields the three claimed sphere families with their binomial multiplicities. For \(\ell=0\), the cone's independence complex is \(I(W_n)\sqcup\{w\}\), yielding the separately displayed three-component space. Every reduction preserves homotopy type, giving integral, not merely rational, conclusions.

**Step 4: sheet and rim symmetry.** In Step 1 the subcomplex before adding the final hub edge retracts to \(Z=I(B(C_n))\), which has trivial \(H_1(-;\mathbb Z)\), as \(d\ge2\). The relative long exact sequence of adjoining one edge identifies \(H_1(I(B(W_n));\mathbb Z)\) with the free relative class of that oriented edge. Sheet exchange interchanges its endpoints and reverses its orientation, hence acts by \(-1\). Each lifted dihedral permutation of rim vertices fixes both hub endpoints and preserves the oriented edge; it acts by \(+1\). This also proves that the first homology is \(\mathbb Z\), not a finite torsion group.

## Verification

The accompanying standalone `verify.py` constructs independent faces and reduced simplicial boundary maps, using exact arithmetic over \(\mathbb F_2\). It checks all \(75\) labeled graphs on one through four vertices for the universal splitting at the Betti-number level; separately checks the wheel-cover formulas for \(5\le n\le9\); and builds six small generalized Mycielskians (including \(\ell=0,1,2,3\)) directly from the defining edge rules. Each comparison independently enumerates faces and reduces finite-field matrices. The saved output ends with `ALL_VERIFY_OK wheel_covers=5 coned_graphs=75 mycielskians=6`.

These are **finite corroborations only**. The all-parameter homotopy theorem follows from the topological cone-cover argument, the classical cycle theorem, and [1, Theorem 5]. Exact finite-field calculations do not independently certify infinite families or integral attaching maps.

## Relationship to prior work

Carnero Bravo [1], originally made public 2026-01-19, proves the general three-periodic Mycielskian splitting in terms of \(I(G)\) and \(I(B(G))\). The paper explicitly computes its implications for paths, cycles, complete graphs, and selected products, not the wheel cone-cover evaluation used here. Thus that general theorem supplies Step 3, but its published family formulas do not include the explicit all-wheel classification or the deck-sign refinement. Goyal, Shukla and Singh [4] compute generalized Mycielskians of complete graphs, not wheels. Antolín Camarena and Carnero Bravo [3] determine \(I(C_n\times K_2)\), the rim input in Step 2, but do not analyze the two new cone hubs. None of these earlier statements alone asserts the universal splitting of Step 1.

## Limitations

The classification is for ordinary independence complexes of wheels with \(n\ge5\) and the precisely defined generalized Mycielskian construction. It does not classify iterated Mycielskians, arbitrary graph joins beyond the stated one-hub splitting, or the full deck action in homology of every generalized Mycielskian. The circle action statement concerns the Kronecker cover of the original wheel only. The result uses established theorems and is subject to residual priority risk from unindexed formulations of graph-cover splittings. No independent mathematical audit has been performed.

## References

[1] Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432, first posted 2026-01-19, especially Theorem 5 and the cycle computations. https://arxiv.org/abs/2601.13432

[2] D. N. Kozlov, *Complexes of directed trees*, J. Combin. Theory Ser. A 88 (1999), 112–122 (classical independence-complex homotopy calculation for cycles; as cited in [1,3]).

[3] Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, originally 2023-07-23, Lemma 9 and Theorem 10. https://arxiv.org/abs/2307.12401

[4] Shuchita Goyal, Samir Shukla, and Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, first posted 2019-05-16, published in Contributions to Discrete Mathematics 16(3), 2021. https://arxiv.org/abs/1905.06926
