# Support-conditioned coadjoint rank strata of unicyclic graphical Lie algebras

## Finding

Let \(G=(V,E)\) be a finite connected simple unicyclic graph, with \(n=|V|=|E|\). Its graphical two-step nilpotent Lie algebra has basis \(x_v\) for \(v\in V\) and central basis \(z_e\) for \(e\in E\), with \([x_u,x_v]=z_{\{u,v\}}\) for each oriented edge \(u<v\), and zero bracket on nonedges. For a linear functional on its center, the alternating coadjoint commutator form on the vertex quotient is exactly the weighted matrix below. Fix any finite field \(\mathbb F_q\), including fields of characteristic two. For every assignment \(y:E\to\mathbb F_q\), let \(B_G(y)\) be the alternating weighted adjacency matrix: after ordering the vertices, the entry at \(u<v\) is \(y_{\{u,v\}}\) if \(uv\in E\), and zero otherwise, with the opposite entry its additive inverse. Put \(S(y)=\{e:y_e\ne0\}\), and let \(\nu(S)\) be the matching number of the spanning support graph \((V,S)\).

Define a support invariant \(\varepsilon(S)\in\{0,1\}\): repeatedly delete a degree-one support vertex **together with its unique neighbor**, deleting all incident edges, until no degree-one vertex remains. Take the smallest labeled available leaf at each step for definiteness. The remaining graph has only isolated vertices or one cycle with isolated vertices. Set \(\varepsilon(S)=1\) precisely when this residual cycle exists and has even length; otherwise put \(\varepsilon(S)=0\). The criterion, and the final rank statement, do not depend on which leaf was chosen.

**Support-conditioned rank law.** For a fixed support \(S\), if \(\varepsilon(S)=0\), all \((q-1)^{|S|}\) nonzero weight assignments have
\[\operatorname{rank}B_G(y)=2\nu(S).\]
If \(\varepsilon(S)=1\), exactly \((q-1)^{|S|-1}\) assignments have rank \(2\nu(S)-2\), and the remaining \((q-1)^{|S|}-(q-1)^{|S|-1}\) assignments have rank \(2\nu(S)\). The exceptional count is valid for \(q=2\): all weights are then forced, and every such even-cycle residual contributes one rank drop.

In particular, the **entire weighted alternating-rank enumerator** is the explicit support polynomial
\[
\boxed{\ R_G(q,z)=\sum_{S\subseteq E}(q-1)^{|S|}z^{\nu(S)}+\sum_{\substack{S\subseteq E\\\varepsilon(S)=1}}(q-1)^{|S|-1}\bigl(z^{\nu(S)-1}-z^{\nu(S)}\bigr).\ }
\]
If the unique cycle of \(G\) has odd length, the correction sum vanishes identically. For every odd prime power \(q\), the associated graphical class-two group has exactly
\[
\boxed{\ \operatorname{ch}(G,i;q)=q^{n-2i}[z^i]R_G(q,z)\ }
\]
irreducible complex characters of degree \(q^i\), for each integer \(0\le i\le\lfloor n/2\rfloor\).

For example, let \(G\) be a four-cycle with a single pendant edge attached at one cycle vertex. With \(t=q-1\),
\[
R_G(q,z)=1+(5t+6t^2+2t^3)z+(4t^2+8t^3+5t^4+t^5)z^2.
\]
At \(q=3\), the rank counts are \((1,50,192)\) and the character multiplicities in degrees \(1,3,9\) are \((243,1350,576)\).

## Assumptions and scope

The graph has exactly one simple cycle and may have arbitrarily many attached tree branches. The rank theorem applies to every finite field of any characteristic; the asserted graphical-group character formula uses the standard odd-characteristic class-two rank/character correspondence. The matching number refers to the **support graph**, including isolated vertices, not the matching count of the original graph. Support \(S=\varnothing\) has \(\nu=0\), \(\varepsilon=0\). If \(\varepsilon=1\), then \(S\) contains at least the even cycle and \(\nu(S)\ge2\), so the exponent \(|S|-1\) and corrected nonnegative ranks are well-defined.

## Proof

**Leaf splitting.** Suppose the present-edge support has a leaf \(v\) adjacent to \(u\), and write \(a=B_G(y)_{uv}\ne0\). The corresponding alternating plane on \(u,v\) has matrix \(\begin{pmatrix}0&a\\-a&0\end{pmatrix}\). By subtracting suitable multiples of the leaf basis vector from every other basis vector, we eliminate all entries involving \(u\) and vertices other than \(v\) while leaving unchanged the submatrix on vertices other than \(u,v\). Thus the whole matrix is congruent to this invertible plane plus the weighted alternating matrix of the induced remaining support graph. Each leaf-pair deletion therefore reduces the rank by exactly two, over all fields including characteristic two. Separately, an exchange argument for matchings shows \(\nu(S)=1+\nu(S-\{u,v\})\): some maximum matching uses \(uv\), since any edge incident with \(u\) can be replaced by \(uv\). Thus a leaf-pair deletion reduces matching number by exactly one.

**Residual core.** Iterate until no leaf survives. A subgraph of a unicyclic graph has at most one cycle; after leaf-pair pruning its only nonisolated component is therefore either empty or the entire original cycle, necessarily with all its edges present. Let \(k\) be the number of deleted leaf pairs, let \(H\) denote the residual graph, and use \(B_H\) for its residual alternating matrix. The preceding argument yields
\[
\operatorname{rank}B_G(y)=2k+\operatorname{rank}B_H(y),\qquad \nu(S)=k+\nu(H).
\]
If \(H\) is edgeless, both residual quantities vanish. If \(H\) is a cycle of odd length \(2\ell+1\), deleting one vertex leaves a weighted path on \(2\ell\) vertices whose alternating matrix has a nonzero determinant equal to the square of an alternating edge product. The cycle matrix has even rank at most \(2\ell\), so its rank is exactly \(2\ell\), which equals twice its matching number.

If \(H\) is a cycle of even length \(2\ell\), its Pfaffian is, up to sign,
\[
\operatorname{Pf}(B_H)=\prod_{j=1}^{\ell}a_{2j-1}-\prod_{j=1}^{\ell}a_{2j},
\]
where the \(a_j\) are the cyclic edge weights, and the relative sign can be absorbed in the orientation convention. Both products are nonzero. When they differ, the matrix has full rank \(2\ell\). When they coincide, the determinant vanishes. The matrix obtained by deleting two adjacent cycle vertices is an even-order weighted path with nonzero determinant; hence the rank in the singular case is exactly \(2\ell-2\), not smaller. Matching number remains \(\ell\), so the only possible departure from twice the matching number is a drop of precisely two.

**Count of exceptional weights.** Fix \(S\) with an even cycle surviving pruning. The leaf-pair eliminations only remove alternating planes; in particular, the residual cycle entries are precisely the original weights of its edges, without new cross terms. Once every nonzero support weight other than one selected residual-cycle edge has been fixed, the cancellation equation uniquely determines that final weight, and it is nonzero. Thus precisely \((q-1)^{|S|-1}\) assignments produce the drop, among \((q-1)^{|S|}\) choices. The criterion for a surviving cycle is invariant under pruning order because the rank drop from \(2\nu(S)\) has just been proved intrinsically; alternatively it follows by the parity of the forest branches attached to each cycle vertex. This proves the support-wise law and, upon summing support classes, the polynomial identity.

**Character multiplicities.** For odd \(q\), the usual class-two graph group has order \(q^{n+|E|}\), abelianization of order \(q^n\), and commutator matrix \(B_G(y)\) with one central functional coordinate per edge. The class-two orbit/character formula gives \(q^{n-2i}\) characters of degree \(q^i\) for each central functional whose matrix has rank \(2i\). Summation yields the displayed multiplicity law. As a consistency check, \(\sum_i\operatorname{ch}(G,i;q)q^{2i}=q^nR_G(q,1)=q^{n+|E|}\), the group order.

## Verification

The standalone file `check_unicyclic.py` independently computes each weighted alternating-matrix rank by modular row reduction, evaluates the support formula by a separate exhaustive matching and leaf-pruning routine, and compares full rank histograms. It exhaustively tested thirteen unicyclic graph shapes across fifty-two finite-field configurations involving \(q\in\{2,3,4,5\}\), directly evaluating 126,870 weighted matrices, plus 1,200 reproducible further weighted assignments. The \(\mathbb F_4\) implementation uses \(\mathbb F_2[t]/(t^2+t+1)\). The output in `verification_output.txt` reports both test sets passing. These finite checks corroborate; the proof above establishes the universal assertions.

For the four-cycle with one leaf over \(\mathbb F_3\), \(1+50+192=243\) equals the number of edge-weight assignments and \(243+1350\cdot9+576\cdot81=59049=3^{10}\) checks the character degree-squared identity.

## Relationship to prior work

Li and Yu (2014) established structural skew-rank formulas for fixed orientations of unicyclic graphs; their pendant-reduction and matching ideas are acknowledged. Their oriented adjacency matrices have prescribed unit-magnitude edge entries; the present claim concerns **every support and every nonzero finite-field weight assignment**, including exact frequencies of Pfaffian cancellation. Rossmann (2021/2022) formulated the character-degree enumeration problem for graphical groups and translated it to alternating-matrix rank counts, without a complete unicyclic support-conditioned answer. O'Brien and Voll provided the class-two character/rank bridge used here.

Earlier recorded results provide character-degree polynomials for pure cycles and for trees, and a general one-vertex amalgamation recurrence for rank-polynomial computations. These results are not claimed new. In fact, their combination can in principle compute rank polynomials of unicyclic graphs recursively. The assertion assessed here is the **sharper support-wise classification** identifying exactly which support patterns have weight-sensitive rank, and the universal closed correction term \((q-1)^{|S|-1}\) for each such pattern. The full-rank and character polynomial identities are consequences of that support-conditioned classification, not asserted to be the first possible algorithmic computations for this graph family.

## Limitations

The theorem requires a connected simple graph with exactly one cycle. For graphs with several cycles, Pfaffian cancellations can interact and the single correction term need not suffice. The theorem counts labeled assignments and irreducible characters by degree, not character values or orbits under graph automorphisms. Independently verified historical priority remains outstanding; in particular, general graph-gluing recurrences may contain equivalent unicyclic specializations not presented in this form. No assertion of independent audit is made.

## References

1. X. Li and G. Yu, “The skew-rank of oriented graphs,” arXiv:1404.7230v1, first public version April 29, 2014, https://arxiv.org/abs/1404.7230.
2. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564v1, July 12, 2021, https://arxiv.org/abs/2107.05564; *Bulletin of the London Mathematical Society* 54 (2022), DOI 10.1112/blms.12665.
3. E. A. O'Brien and C. Voll, “Enumerating classes and characters of p-groups,” arXiv:1203.3050, https://arxiv.org/abs/1203.3050; *Transactions of the American Mathematical Society* 367 (2015), 7775–7796.
4. “Cycle graphical groups have an explicit character-degree enumerator,” accessible scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e.
5. “Tree graphical groups have matching-support character polynomials,” accessible scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-tree-graphical-groups-have-matching-support-character-polynomial--fb80c871ed65.
6. “Coning recurrence for character degrees of graphical groups,” accessible scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-coning-recurrence-for-character-degrees-of-graphical-groups--732adc755a75.
7. D. DeCoste, L. DeMeyer, and M. Mainkar, “Graphs and metric 2-step nilpotent Lie algebras,” arXiv:1512.07944v1, December 25, 2015, https://arxiv.org/abs/1512.07944.
