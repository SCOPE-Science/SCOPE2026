# Complete dihedral rational homology character of ordinary cycle Mycielski independence complexes

## Finding
Let \(n\ge4\), let \(C_n\) be the undirected cycle, and let \(\mu(C_n)\) be its ordinary Mycielski graph (one original and one clone per vertex, and one apex). The natural dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\), \(s(i)=-i\) simultaneously on both vertex layers, fixing the apex. Put \(X_n=\operatorname{Ind}(\mu(C_n))\).

Define \(p_0=1\), \(p_1=0\), and \(p_m=p_{m-1}-p_{m-2}\) for \(m\ge2\), and let \(c_d\) be the six-periodic integer sequence \((2,1,-1,-2,-1,1)\), with \(c_d\) indexed by \(d\bmod6\). Define
\[
q(n)=\begin{cases}\lfloor n/3\rfloor,&n\equiv0,1\pmod3,\\\lfloor n/3\rfloor+1,&n\equiv2\pmod3.\end{cases}
\]
Then all reduced rational homology of \(X_n\) vanishes except in degree \(q(n)\), where its dimension is two if \(3\mid n\) and one otherwise. Its complete rational \(D_n\)-character is
\[
\boxed{\operatorname{tr}(r^k\mid\widetilde H_{q(n)}(X_n;\mathbb Q))=(-1)^{q(n)}c_{\gcd(n,k)}}
\qquad(0\le k<n),
\]
and
\[
\boxed{\operatorname{tr}(r^ks\mid\widetilde H_{q(n)}(X_n;\mathbb Q))=(-1)^{q(n)}\begin{cases}
p_{(n-1)/2},&n\text{ odd},\\
p_{n/2+1},&n\text{ even and }k\text{ even},\\
p_{n/2-2},&n\text{ even and }k\text{ odd}.
\end{cases}}
\]
Here the reflection notation \(r^ks\) acts by \(i\mapsto k-i\). In particular, the geometric orbit space satisfies
\[
\boxed{\dim_{\mathbb Q}\widetilde H_i(|X_n|/D_n;\mathbb Q)=\begin{cases}
1,&i=q(n)\text{ and }n\equiv1,11\pmod{12},\\
0,&\text{otherwise}.
\end{cases}}
\]
The statement is rational: neither integral orbit-space torsion nor integral representation-lattice structure is asserted.

## Assumptions and scope
All graphs are finite, simple, undirected, and loopless. The vertex set of \(\mu(G)\), for a nonempty graph \(G=(V,E)\), is \(V\sqcup V'\sqcup\{w\}\). Its edges are \(E\) among originals, \(uv'\) whenever \(uv\in E\), and \(wv'\) for every clone; it has no edges among clones. The group \(\operatorname{Aut}(G)\) acts on originals and clones via the same permutation and fixes \(w\). \(\operatorname{Ind}(G)\) includes the empty face, and the reduced Lefschetz number uses that face as a chain generator in degree \(-1\). The absolute geometric quotient is the ordinary topological orbit space, not a simplicial orbit complex obtained by naively merging vertices.

## Proof
**1. Signed fixed-face formula.** If \(h\) is an automorphism of a finite graph \(F\), the reduced simplicial Lefschetz number of its independence complex is
\[
\widetilde L_{\operatorname{Ind}(F)}(h)=-\sum_{S}(-1)^{o_h(S)},
\]
where \(S\) ranges over all \(h\)-invariant independent vertex sets, including the empty set, and \(o_h(S)\) is the number of cycles of the permutation \(h\) on \(S\). Indeed, the oriented simplex indexed by \(S\) contributes its permutation sign \((-1)^{|S|-o_h(S)}\), times the alternating chain sign \((-1)^{|S|-1}\). These multiply to \(-(-1)^{o_h(S)}\). The equality between alternating chain and homology traces holds for any finite chain complex over \(\mathbb Q\).

**2. A general Mycielski Lefschetz identity.** For every nonempty finite simple graph \(G\) and automorphism \(h\) of \(G\),
\[
\boxed{\widetilde L_{\operatorname{Ind}(\mu(G))}(h)=-\widetilde L_{\operatorname{Ind}(G)}(h).}
\]
To prove it, select the \(h\)-orbits of original vertices appearing in an invariant independent set of \(\mu(G)\). Such orbits form an independent union \(S\) in \(G\). If the apex is absent, every clone orbit is optional unless it is adjacent to some vertex of \(S\). In particular, *the clone orbit corresponding to any chosen original orbit* is optional, because \(S\) is independent. If \(S\) is empty, every clone orbit is optional; at least one exists because \(G\) is nonempty. Since distinct clone orbits have no edges between them, the signed sum over optional clone orbits is multiplied by \((1-1)^a=0\) with \(a\ge1\). Thus all apex-free contributions cancel, for every independent original orbit union \(S\). If the apex is present, it excludes every clone; the signed contribution is \(-(-1)^{o_h(S)}\). Therefore the signed independent-set orbit sum for \(\mu(G)\) is the negative of that for \(G\). Applying Step 1 gives the displayed Lefschetz identity. This is a character-level statement, not a claim of equivariant homotopy equivalence.

**3. Rotations of the original cycle.** For \(r^k\), let \(d=\gcd(n,k)\). Each vertex orbit of the rotation is a residue class modulo \(d\). If \(d=1\), the sole orbit contains an edge and is forbidden in an independent union, leaving one eligible union (empty). If \(d=2\), the two eligible vertex orbits are adjacent, so the signed orbit-enumeration is the independence polynomial of \(K_2\) at \(-1\), equal to \(-1\). If \(d\ge3\), eligibility and adjacency among vertex orbits are exactly those of the cycle \(C_d\). Its independence polynomial at \(-1\) is \(2\cos(\pi d/3)\): this follows from the standard deletion recurrence for a path and the edge-closing recurrence for a cycle (or from the order-six recurrence with initial values). These three cases are unified by \(c_d\). Step 2 and Step 1 therefore yield \(\widetilde L_{X_n}(r^k)=c_d\).

**4. Reflections of the original cycle.** For \(n=2m+1\), a reflection has one fixed vertex and \(m\) two-vertex orbits. The last orbit consists of two adjacent vertices, so it is ineligible; the remaining eligible orbits form the path \(P_m\). For \(n=2m\), a vertex-axis reflection (\(k\) even) has two fixed vertices and \(m-1\) eligible paired orbits, with path adjacency \(P_{m+1}\). An edge-axis reflection (\(k\) odd) has two ineligible edge-orbits and the remaining eligible orbits form \(P_{m-2}\). The independence polynomial of \(P_j\) at \(-1\) equals \(p_j\), since deleting its terminal vertex gives \(p_j=p_{j-1}-p_{j-2}\), with \(p_0=1,p_1=0\). By Step 2, the three path values are exactly \(\widetilde L_{X_n}(r^ks)\).

**5. From Lefschetz numbers to the unique homology character.** The ordinary Mycielski suspension theorem states \(\operatorname{Ind}(\mu(G))\simeq\Sigma\operatorname{Ind}(G)\). The classical cycle classification gives \(\operatorname{Ind}(C_{3a})\simeq S^{a-1}\vee S^{a-1}\), \(\operatorname{Ind}(C_{3a+1})\simeq S^{a-1}\), and \(\operatorname{Ind}(C_{3a+2})\simeq S^a\). These are ordinary, not assumed equivariant, equivalences. Thus the only reduced homology of \(X_n\) is concentrated in degree \(q(n)\), with rank one or two as specified. Its trace is \((-1)^{q(n)}\widetilde L_{X_n}\), proving both character formulas.

**6. Exact quotient criterion.** The path sequence \(p_j\) has period six with values \((1,0,-1,-1,0,1)\). When \(3\mid n\), the rank-two rational character has zero reflection traces and its rotations form a two-dimensional nontrivial dihedral representation; hence it has no invariant vector. Otherwise the module is one-dimensional. For even \(n\) not divisible by three, the generator \(r\) acts by \(-1\), precluding invariants. For odd \(n\) not divisible by three, the generator \(r\) acts by \(+1\), while the reflection acts by \(+1\) exactly for \(n\equiv1,11\pmod{12}\). This proves the full-invariant criterion. For a finite group acting simplicially, barycentric subdivision and averaging rational cellular chains identify \(\widetilde H_i(|X|/D_n;\mathbb Q)\) with \(\widetilde H_i(X;\mathbb Q)^{D_n}\). No integral transfer is used.

## Verification
The standalone exact-integer program `check.py` constructs the Mycielski graph directly. One check evaluates reduced Lefschetz traces using eligible vertex orbits and exact recursive independence-polynomial evaluation, and compares them to the formulas. Another independently enumerates all independent faces in small cases, tests setwise invariance, and applies the oriented-simplex permutation signs. Results: 166 orbit-graph trace checks and 66 independent signed-face trace checks passed. The same program verifies the dimension, character averaging, and resulting quotient-invariant criterion for every \(3\le n\le75\) (the \(n=3\) case is a consistency check, not part of the asserted novel parameter range). All these checks are finite corroboration; Steps 1–6 are the all-parameter proof.

## Relationship to prior work
Goyal–Shukla–Singh (first public 2019) proved the ordinary Mycielski suspension equivalence for every graph. Carnero Bravo (first public January 19, 2026) gave generalized-Mycielski homotopy formulas and the cycle sphere ranks. Both give ordinary homotopy types, not the dihedral action on homology. Published complete-symmetry calculations for Mycielskians of complete graphs and crowns cover, in particular, the special cycle orders \(n=3\) and \(n=6\), but neither gives this all-cycle character formula or the modulo-twelve quotient criterion. Published dihedral calculations for other cycle-associated independence, matching, and neighborhood complexes involve different simplicial complexes and do not determine the present character. The present claim is the explicit full dihedral representation and quotient determination, proved by signed-orbit cancellation; the already known nonequivariant wedge decomposition is not claimed as new. The 2019 suspension construction may itself admit a natural equivariant refinement yielding the general Lefschetz identity, but it does not give the dihedral character values or quotient criterion without further calculation.

## Limitations
Only the canonical lifted \(D_n\)-action, ordinary one-step Mycielskian, rational representation character, and rational orbit-space homology are classified. The theorem does not determine the full automorphism group when it is larger, integral representation lattices, integral quotient torsion, generalized levels \(\mu_\ell\) for \(\ell>1\), or equivariant homotopy type. Literature searches and inspection of relevant accessible works reduce but cannot eliminate priority risk from unindexed results.

## References
1. S. Goyal, S. Shukla, A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (first posted 2019-05-16), especially Theorem 4.1. https://arxiv.org/html/1905.06926v1
2. A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432 (first posted 2026-01-19), especially Theorem 5 and Corollary 9. https://arxiv.org/html/2601.13432
3. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, J. Combin. Theory Ser. A 119 (2012), 1031–1047; classical cycle homotopy classification (also recalled in reference 2).
4. *The symmetric-group homology modules of generalized Mycielskians of complete graphs*, published research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-symmetric-group-homology-modules-of-generalized-mycielskians--a69c919d2b95
5. *Integral symmetry modules of generalized Mycielskian crown independence complexes*, published research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-symmetry-modules-of-generalized-mycielskian-crown-indep--f15d4ab4d8e9
