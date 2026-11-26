# Unicyclic graphical-group character degrees via an attachment-sensitive Pfaffian correction

## Finding

Let \(G=(V,E)\) be any finite connected simple graph with exactly one cycle \(C\), let \(n=|V|\), and let \(q\) be any prime power. For an ordering of \(V\), write \(M_G(w)\) for the alternating matrix with entries \(w_{ij}\) and \(-w_{ij}\) in positions indexed by edges \(\{i,j\}\), with all \(w_{ij}\in\mathbb F_q\) arbitrary. Define the rank enumerator
\[
A_G(q,z)=\sum_{w\in\mathbb F_q^E}z^{\operatorname{rank}M_G(w)/2}.
\]
Write \(\nu(H)\) for the maximum matching size of a graph \(H\). For each edge support \(S\subseteq E\), set \(H_S=(V,S)\). If the unique cycle has odd length, define \(\mathcal R(G)=\varnothing\). Otherwise, \(S\in\mathcal R(G)\) if and only if (i) \(S\) contains every edge of \(C\), and (ii) for each component \(T\) of \(H_S-V(C)\) that is joined to a cycle vertex by an edge of \(S\), the unique vertex \(u\in T\) incident to that bridge is covered by **every** maximum matching of \(T\): equivalently \(\nu(T-u)=\nu(T)-1\). Components not joined to the cycle impose no condition.

**Theorem.** Uniformly for all such \(G\) and all finite fields,
\[
\boxed{A_G(q,z)=\sum_{S\subseteq E}(q-1)^{|S|}z^{\nu(H_S)}
+\sum_{S\in\mathcal R(G)}(q-1)^{|S|-1}\bigl(z^{\nu(H_S)-1}-z^{\nu(H_S)}\bigr).}
\]
For every odd prime power \(q\), the number of ordinary irreducible complex characters of the class-two graphical group \(\mathbf G_G(\mathbb F_q)\) of degree \(q^r\) is exactly
\[
\boxed{\mathrm{ch}(G,r;q)=q^{n-2r}[z^r]A_G(q,z)}.
\]
Thus every character degree and multiplicity of every unicyclic graphical group is determined by the matching-support formula and a single type of cycle correction. The rank formula remains valid in characteristic two, though the stated character formula is limited to odd characteristic.

## Assumptions and scope

A graph is unicyclic when it is connected, simple, and has one (necessarily chordless) cycle, of length at least three. A *support* consists of exactly those edges whose matrix weights are nonzero. The graph \(H_S\) can be disconnected. The components \(T\) in the definition of \(\mathcal R(G)\) are trees induced by the off-cycle vertices and the selected off-cycle edges; only components with a selected bridge to \(C\) are tested. Since \(G\) is unicyclic, a component cannot have two distinct selected bridges to the cycle. A one-vertex component joined by a bridge is not eligible: it has \(\nu(T)=\nu(T-u)=0\).

The variable \(z\) marks half of an alternating-matrix rank, not the rank itself. The coefficient formula permits \(q=2\), where every nonzero edge weight equals one. No claim is made about groups in characteristic two or about graphs containing more than one cycle.

## Proof

**1. Forest ranks.** If \(F\) is a forest and all weights on its edges are nonzero, then \(\operatorname{rank}M_F=2\nu(F)\). Induct on the number of edges: for a leaf \(v\) with neighbor \(u\), the nonzero \(2\times2\) alternating block at \(u,v\) is invertible. Simultaneous row-column elimination removes those two vertices and increases rank by two, without altering the matrix indexed by the other vertices. The matching recursion \(\nu(F)=1+\nu(F-u-v)\) follows by exchanging an arbitrary maximum matching to use the leaf edge. Isolated vertices contribute zero.

**2. Reduction of attached trees.** Fix a support containing the whole cycle, and let \(T\) be an off-cycle tree component joined to a cycle vertex \(v\) through \(u\in T\). Set \(D=M_T\), a possibly degenerate alternating form. If \(u\) is covered by every maximum matching of \(T\), then \(\nu(T-u)=\nu(T)-1\), so \(\operatorname{rank}D-\operatorname{rank}D_{T-u}=2\) by Step 1. Therefore each vector in \(\ker D\) has zero \(u\)-coordinate. (For any alternating matrix, the opposite case, equality of the two ranks, is equivalent to the existence of a radical vector with nonzero \(u\)-coordinate, as is immediate from block elimination.) The bridge functional annihilates the radical of \(D\); completing alternating squares splits the \(D\)-block off, without modifying the cycle-cycle block, because the bridge meets only \(v\) and an alternating form gives zero diagonal Schur correction. Repeating over all attached components gives the direct sum of the original cycle form, the forest forms, and zero isolated coordinates.

If instead some attached \(T\) has \(\nu(T-u)=\nu(T)\), then a vector in \(\ker D\) has nonzero \(u\)-coordinate. The bridge pairs that radical vector with \(v\); an invertible alternating plane can be eliminated containing \(v\), thereby breaking the only cycle. Subsequent leaf eliminations take place in a forest and involve only nonzero edge weights. The rank is consequently independent of the actual nonzero values on the entire support in this case. Its value is \(2\nu(H_S)\): over independent edge indeterminates, a maximum-matching principal Pfaffian contains a distinct noncancelling matching monomial, whereas no larger Pfaffian can be nonzero, proving generic rank \(2\nu(H_S)\). The constant rank agrees with that generic value.

This case division can equivalently be implemented solely by pendant-pair elimination: cycle survival occurs exactly when each attached-root vertex is matched in every maximum matching of its off-cycle tree. This equivalence is field-independent.

**3. Cycle residue.** If all attached roots meet the essentiality test, deleting the forest blocks leaves precisely the weighted cycle. Moreover \(\nu(H_S)=\nu(H_S-V(C))+\nu(C)\): a bridge used in a matching cannot improve the total because its off-cycle endpoint is essential in its tree. An odd weighted cycle has rank \(|C|-1=2\nu(C)\). For an even cycle of length \(2s\), orient its edges cyclically and label the corresponding nonzero cyclic matrix entries \(w_0,\ldots,w_{2s-1}\). Its Pfaffian (up to a nonzero global sign) is
\[
\prod_{j=0}^{s-1} w_{2j}-\prod_{j=0}^{s-1} w_{2j+1}.
\]
Therefore its rank is \(2s\) except when these products agree, in which case its rank is \(2s-2\); the latter follows also because deleting one cycle vertex gives a full-rank odd path of rank \(2s-2\). Thus the only possible exceptional support is in \(\mathcal R(G)\), and on it half-rank drops by exactly one.

**4. Field count.** Each support \(S\) has exactly \((q-1)^{|S|}\) nonzero assignments. For \(S\in\mathcal R(G)\), the equality of alternating products is one equation with a uniquely determined value for one cycle weight once the other \(|S|-1\) nonzero weights are chosen. Thus exactly \((q-1)^{|S|-1}\) assignments on that support have the lower half-rank. All other assignments have half-rank \(\nu(H_S)\), giving the boxed identity. The argument includes \(q=2\).

**5. Graphical-group characters.** In odd characteristic, the graphical group has a two-step Lie-model with \(n\) vertex coordinates and \(|E|\) central edge coordinates. For a linear functional on the center with edge weights \(w\), its commutator form on the vertex quotient is \(M_G(w)\). The finite Kirillov correspondence gives an irreducible of degree \(q^{\operatorname{rank}M_G(w)/2}\) per coadjoint orbit. There are \(q^n\) functionals extending a prescribed central functional and each orbit has \(q^{\operatorname{rank}M_G(w)}\) elements, giving \(q^{n-\operatorname{rank}M_G(w)}\) characters. Summing over all weights of fixed rank proves the second box. In particular the degree-square sum is \(\sum_r q^{2r}\mathrm{ch}(G,r;q)=q^{n+|E|}\), as required by the group order.

## Verification

The accompanying `verify.py` uses independently implemented finite-field Gaussian elimination to compute alternating ranks, then compares complete edge-weight enumerations against the support-and-matching formula. It checks even and odd cycles, an attached leaf, a two-edge tail, two leaves at one cycle vertex, and several further attached-tree examples. Over prime fields, the program also verifies that each predicted coefficient sum equals \(q^{|E|}\). Run it with `python3 verify.py`.

For the first nontrivial even-cycle survival example, attach a two-edge path to a vertex of a four-cycle. Then \(n=|E|=6\); at \(q=3\) the half-rank counts are \((1,56,384,288)\) for ranks \(0,1,2,3\). Thus the graphical group's character-degree multiplicities are \((729,4536,3456,288)\) for degrees \(1,3,9,27\). The degree-square sum is \(3^{12}\). By comparison, a single attached leaf prevents the resonance **on full support** (although supports omitting its bridge still inherit the bare-cycle correction), whereas the full support of a two-edge tail permits it.

## Relationship to prior work

The original 2011 skew-characteristic-polynomial work of Hou and Lei provides the orientation/Pfaffian setting, and Gong and Xu (2012) treat arbitrary weighted skew matrices over the reals at the characteristic-polynomial level. Li and Yu (2014), especially Sections 2, 4, and 5, classify skew ranks of **unweighted oriented** unicyclic graphs using matching and pendant reduction. Their results are important antecedents for the essential-root condition, but do not give the finite-field counts of independently varying edge weights across all zero patterns.

Rossmann (2022), Section 1.6, explicitly asks for character-degree enumeration of graphical groups. The previously available tree and bare-cycle formulas in published-finding corpus determine useful boundary families but do not calculate the effect of attaching arbitrary rooted trees to the unique cycle. The present theorem gives a closed graph-theoretic distribution for every such attachment, with a precise and countable finite-field resonance correction. Earlier implicit coverage, especially through the general weighted characteristic-polynomial identity, is a remaining priority risk.

## Limitations

This theorem assumes a simple connected graph with exactly one cycle. It supplies an explicit but potentially exponential edge-subset sum, rather than a uniformly polynomial-time evaluation algorithm. The rank result is valid in any characteristic; the ordinary-character correspondence is stated only for odd characteristic. Its self-review does not constitute independent verification, and the complete 2012 Gong–Xu text was not available for full comparison. The finite enumerations do not replace the general proof.

## References

1. Y. Hou and T. Lei, “Characteristic Polynomials of Skew-Adjacency Matrices of Oriented Graphs,” *Electronic Journal of Combinatorics* 18 (2011), P156, DOI: 10.37236/643 (public 2011-08-05).
2. S.-C. Gong and G.-H. Xu, “The characteristic polynomial and the matchings polynomial of a weighted oriented graph,” *Linear Algebra and its Applications* 436 (2012), 3597–3607, DOI: 10.1016/j.laa.2011.12.033.
3. X. Li and G. Yu, “The skew-rank of oriented graphs,” arXiv:1404.7230v1 (public 2014-04-29), especially Lemmas 2.2–2.5 and Theorems 4.2, 4.5.
4. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” *Bulletin of the London Mathematical Society* 54 (2022), 1923–1943, DOI: 10.1112/blms.12665, especially Question 1.10.
5. Published published-finding corpus findings: “Tree graphical groups have matching-support character polynomials” (2026-10-04, id `2026/10/4/SCOPE-tree-graphical-groups-have-matching-support-character-polynomial--fb80c871ed65`) and “Cycle graphical groups have an explicit character-degree enumerator” (2026-10-04, id `2026/10/4/SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e`).
