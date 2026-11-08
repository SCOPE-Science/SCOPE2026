# Exact formula algebra and sharp depth two on two-layer \(\mathsf{S4}\)–\(\mathsf{S5}\) products

## Finding
Fix integers \(k\ge0\) and \(m\ge1\). The formula-equivalence algebra on the product of a reflexive two-point chain and an \(m\)-world universal equivalence frame, under **all** valuations of \(k\) propositional letters, has exactly
\[
 2^{T_{k,m}},\qquad
 T_{k,m}=\sum_{s=1}^{\min(m,4^k)}s\binom{4^k}{s}
\]
elements. Every equivalence class has a representative of modal depth at most two. The least uniform depth is \(0\) if \(k=0\); \(1\) if \(k\ge1\) and \(m=1\); and \(2\) if \(k\ge1\) and \(m\ge2\). The count strictly increases with \(m\) until \(m=4^k\), then is constant, with \(T_{k,m}=4^k2^{4^k-1}\).

For one variable, the numbers of distinct formulas are \(16\), \(2^{16}\), \(2^{28}\), and \(2^{32}\) for respectively \(m=1,2,3\), and every \(m\ge4\).

## Assumptions and scope
The frame is \(F_m=(\{0,1\}\times\{1,\ldots,m\},R_a,R_b)\), where
\[
 (i,j)R_a(i',j')\iff i\le i'\text{ and }j=j',\qquad
 (i,j)R_b(i',j')\iff i=i'\text{ and }1\le j'\le m.
\]
Both relations are reflexive; \(R_a\) is an \(\mathsf{S4}\)-relation and \(R_b\) an \(\mathsf{S5}\)-relation. The language is classical Boolean propositional logic with arbitrary nesting of \(\Diamond_a\) and \(\Diamond_b\), with \(\Box_a\) and \(\Box_b\) as their Boolean duals. Valuations at the \(2m\) worlds are independent and unrestricted. Modal depth is the maximum number of nested modal connectives. Equivalence means equality of truth at every pointed valuation on this *one fixed frame*, not provable equivalence in \(\mathsf{S4}\times\mathsf{S5}\) over all products.

Write \(Q=2^k\) for the number of propositional truth colors, and encode the lower and upper colors of column \(j\) by \(c_j=(a_j,b_j)\in[Q]^2\). Its support is \(S=\{c_j:1\le j\le m\}\), a nonempty set of at most \(m\) pair-colors. Let \(U=\{b:(a,b)\in S\}\) and \(\Delta U=\{(b,b):b\in U\}\). An observed type at \((0,j)\) is \((c_j,S)\), whereas at \((1,j)\) it is \(((b_j,b_j),\Delta U)\). The upper observed type is thus also realizable at a lower world with a diagonal support.

## Proof
**1. The upper color is expressible at each world.** For each propositional letter \(p_i\), define
\[
 u_i=(p_i\wedge\Box_a p_i)\vee(\neg p_i\wedge\Diamond_a p_i).
\]
At a lower point, if \(p_i\) holds there, then \(u_i\) reduces to \(\Box_a p_i\), which is true exactly when it holds upstairs in the same column; if it does not hold downstairs, then \(u_i\) reduces to \(\Diamond_a p_i\), again detecting the upstairs value. At an upper point \(\Diamond_a\) and \(\Box_a\) both act as identity, so \(u_i=p_i\). Thus \(u_i\) always expresses the upper-coordinate value. For any ordered pair of truth colors \(c=(a,b)\in[Q]^2\), let \(E_c\) assert that the local values of all \(p_i\) form color \(a\) and all \(u_i\) form color \(b\), using the corresponding literals. It has modal depth at most one and holds precisely at points of local pair-color \(c\). At an upper point only diagonal pair-colors occur.

**2. Support tests are depth two.** The formula \(\Diamond_bE_c\) holds at a lower point precisely when some column carries pair-color \(c\); at an upper point it holds precisely when \(c\) belongs to \(\Delta U\). Therefore, for every nonempty \(S\subseteq[Q]^2\) with \(|S|\le m\), and \(c\in S\), the formula
\[
 \chi_{c,S}=E_c\wedge
 \bigwedge_{d\in S}\Diamond_bE_d\wedge
 \bigwedge_{d\notin S}\neg\Diamond_bE_d
\]
has depth at most two and defines exactly the pointed valuations of observed type \((c,S)\). Empty conjunctions have the conventional value \(\top\). For \(k=0\), this construction remains meaningful with the single empty truth color.

**3. Every formula is invariant on observed types.** We show by structural induction that the truth value of any formula depends only on \((c,S)\). At type \((c,S)\), \(R_b\)-successors have types \((d,S)\) as \(d\) ranges over \(S\). For a possibly diagonal type this is still the correct list: both lower and upper realizations have the same type set of \(R_b\)-successors. For \(c=(a,b)\), the \(R_a\)-successor types are the current type and \(((b,b),\Delta U)\). At an upper realization the latter equals the current type, so the same *set* of types again results. Thus both diamond operations, and hence all Boolean connectives and their dual boxes, preserve invariance. Every Boolean union of type-defining \(\chi_{c,S}\) is a formula of depth at most two. Conversely, no formula can distinguish two pointed valuations of equal observed type.

**4. Every indexed type is realized.** Given any \(S\) with \(1\le |S|\le m\) and any \(c\in S\), place one column of each pair-color in \(S\), repeat arbitrary colors until there are \(m\) columns, and designate a lower column carrying \(c\). This realizes the indexed type. There are exactly \(s\binom{Q^2}{s}\) indexed types of support size \(s\). By steps 2 and 3, the full algebra is the Boolean algebra of all subsets of this finite set of types, proving the claimed count and normal form.

**5. Depth and stabilization are sharp.** For \(k=0\), the two Boolean constants are the only classes. For \(k\ge1,m=1\), depth-one formulas \(u_i\) distinguish lower pointed valuations having the same current atomic values but different upper values, so depth zero is insufficient. When \(k\ge1,m\ge2\), consider two models whose first column has color pair \((0,0)\); the second columns have pairs \((1,0)\) and \((1,1)\), respectively; any remaining columns repeat \((0,0)\). At the first lower world, propositional values and the sets of colors visible separately through either single modality are identical, so every depth-one formula agrees. But \(\Box_a\Diamond_b p_1\) is false in the first model and true in the second, so depth two is necessary (choose one propositional letter to distinguish colors \(0\) and \(1\)). Finally, the term \(m\binom{Q^2}{m}\) is positive for every \(1\le m\le Q^2\), and no support has more than \(Q^2\) distinct colors. The threshold \(m=Q^2\) is therefore exact.

## Verification
The attached standalone `checker.py` evaluates formulas directly on the original \(2m\)-world frames, independently computes observed type descriptors from valuations, and compares the semantics of each pair selector \(E_c\) and support test \(\Diamond_bE_c\). It exhausts all valuations in the eight cases \((k,m)=(0,1),(0,4),(1,1),(1,2),(1,3),(1,4),(2,1),(2,2)\), checks \(26{,}922\) pair/support comparisons, confirms the predicted numbers of observed types, and checks invariance of additional nested formulas. It separately tests the depth-one indistinguishability example against every Boolean truth function on one atomic letter, and checks that the depth-two separator differs. Run `python3 checker.py`. All infinitely many parameters are established by the five proof steps, not by this finite check.

## Relationship to prior work
Meadors (2024, first public version) studies local tabularity and products involving \(\mathsf{S4}[n]\times\mathsf{S5}\), establishing qualitative syntactic/semantic criteria for extensions; it does not state a count for the particular fixed chain-by-cluster frame. Shapirovsky and Sliusarev (2024), in their sections on products and local tabularity above \(\mathsf{S4}\times\mathsf{S5}\), also analyze broad product-logics rather than the exact finite-variable quotient on this fixed frame. Shapirovsky (2025) studies general finite modal-depth criteria and bounds, not the present sharp depth-two/one/zero classification. These are conceptually related but do not directly imply the pair-support census. The theorem here is a fixed-frame classification, **not** a theorem of local tabularity for the full product logic.

## Limitations
The frame has exactly two ordered layers and a finite universal cluster, with arbitrary valuations. The classification is not asserted for longer chains, arbitrary partial orders, semiproducts, nonclassical propositional bases, or the full logic of all products. The literature search did not establish historical uniqueness against every unindexed source; an equivalent canonical-type argument could have appeared in earlier product-logic work. Finite computation is supplementary to the proof, and no independent audit has been performed.

## References
1. Chase Meadors, *Local tabularity in MS4 with Casari's axiom*, arXiv:2412.01026, first public 2024-12-02, sections 1, 2 and 5, https://arxiv.org/html/2412.01026v3.
2. Ilya B. Shapirovsky and Vladislav Sliusarev, *Locally tabular products of modal logics*, arXiv:2404.01670, first public 2024-04-02, sections 2 and 6, https://arxiv.org/abs/2404.01670.
3. Ilya B. Shapirovsky, *Generalizations of The Finite Height Criterion for Local Tabularity*, arXiv:2509.17612, first public 2025-09-22, sections 2 and 6, https://arxiv.org/abs/2509.17612.
