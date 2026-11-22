# Integral full-automorphism homology of pentagonal Dutch windmill matching complexes

## Finding
For every integer \(n\ge2\), form \(D_n\) from \(n\) pentagons by identifying exactly one vertex of each pentagon to a common center \(c\). Write \(X_n=\mathcal M(D_n)\) for the ordinary matching complex, and let \(W_n\) be the set of the \(2n\) graph edges incident with \(c\) (the **spokes**). The full graph automorphism group is
\[
G_n=\operatorname{Aut}(D_n)\cong (C_2)^n\rtimes S_n=C_2\wr S_n.
\]
Write \(\theta:G_n\to\{\pm1\}\) for the sign of the permutation induced on the \(n\) pentagonal blades. Then the only nonzero reduced integral homology group of \(X_n\) is in degree \(n\), and there is an **integral \(\mathbb Z[G_n]\)-module isomorphism**
\[
\boxed{\widetilde H_n(X_n;\mathbb Z)\cong
\theta\otimes_{\mathbb Z}\ker\!\left(\varepsilon:\mathbb Z[W_n]\longrightarrow\mathbb Z\right),
\quad \varepsilon\!\left(\sum_{w\in W_n}a_w w\right)=\sum_{w\in W_n}a_w.}
\]
Here \(\theta\) denotes the rank-one sign lattice, and all other reduced integral homology groups vanish. In particular, \(\widetilde H_n(X_n;\mathbb Z)\) is free of rank \(2n-1\).

For \(g\in G_n\), let \(\pi_g\in S_n\) be its permutation of blades and let \(f_0(g)\) be the number of blades fixed by \(\pi_g\) on which \(g\) does **not** reverse the four-vertex path away from the center. The complete rational homology character is
\[
\boxed{\chi_n(g)=\operatorname{sgn}(\pi_g)\bigl(2f_0(g)-1\bigr).}
\]
For the independent reflection subgroup \(N_n=(C_2)^n\), its invariant rational homology has dimension \(n-1\), whereas the invariant subspace under the **full** group has dimension \(1\) for \(n=2\) and \(0\) for every \(n\ge3\). The restriction to blade permutations is \(\operatorname{sgn}_n\otimes(\mathbf1\oplus 2\mathrm{Std}_n)\); this restricted character was known previously and is not claimed as new.

## Assumptions and scope
The vertices of the \(i\)-th pentagon, \(1\le i\le n\), are \(c,v_{i,1},v_{i,2},v_{i,3},v_{i,4}\), cyclically in that order. Its five graph edges are \(cv_{i,1}\), \(v_{i,1}v_{i,2}\), \(v_{i,2}v_{i,3}\), \(v_{i,3}v_{i,4}\), \(v_{i,4}c\). Distinct pentagons share only \(c\). The matching complex has graph edges as simplicial vertices and pairwise vertex-disjoint graph edges as simplices. Its homology is *reduced* simplicial homology, with the natural integral oriented-chain action.

For \(n\ge2\), the center is the unique graph vertex of valence \(2n\); all other vertices have valence \(2\). Deleting the center leaves \(n\) separate four-vertex paths. Automorphisms therefore permute these paths freely and may reverse each one independently. This proves the displayed full-automorphism-group identification; the action on \(W_n\) is the natural faithful action on two spokes per blade.

## Proof
**1. A sphere subcomplex.** Let \(A_n\subset X_n\) comprise matchings with no spoke. For blade \(i\), label its three non-spoke edges \(u_i=v_{i,1}v_{i,2}\), \(v_i=v_{i,2}v_{i,3}\), and \(z_i=v_{i,3}v_{i,4}\). A matching can contain \(u_i,z_i\) together but cannot contain either alongside \(v_i\). Hence its local non-spoke matching complex \(T_i\) is one interval \(u_i z_i\) and one isolated vertex \(v_i\); it has the homotopy type of \(S^0\). The full non-spoke subcomplex is the join
\[
A_n=T_1*\cdots*T_n\simeq S^{n-1}.
\]
A generator of \(\widetilde H_0(T_i;\mathbb Z)\) is the cycle \([v_i]-[u_i]\). Reversing a blade exchanges \(u_i\) and \(z_i\) while fixing \(v_i\); as \([u_i]=[z_i]\) in \(H_0(T_i;\mathbb Z)\), the reversal acts trivially on the local reduced \(H_0\). Interchanging two join factors of reduced degree zero reverses the orientation of the join generator. Thus the entire \(G_n\)-action on \(\widetilde H_{n-1}(A_n;\mathbb Z)\cong\mathbb Z\) is precisely \(\theta(g)=\operatorname{sgn}(\pi_g)\).

**2. Spoke links and their inclusions.** No matching contains two spokes because they all meet \(c\). For a fixed spoke \(w=cv_{i,1}\), its matching link within the non-spoke complex is
\[
L_w=T_1*\cdots*T_{i-1}*U_i*T_{i+1}*\cdots*T_n,
\]
where \(U_i\) is the discrete two-vertex complex on \(v_i,z_i\). For \(w=cv_{i,4}\), use instead the discrete two-vertex complex on \(u_i,v_i\). In both cases \(U_i\simeq S^0\), hence \(L_w\simeq S^{n-1}\). The inclusion \(U_i\hookrightarrow T_i\) meets both connected components exactly once, and induces an isomorphism on reduced integral \(H_0\). In fact, it is a homotopy equivalence: each of the two components of \(T_i\) is contractible. Joining with the other factors shows that every inclusion \(j_w:L_w\hookrightarrow A_n\) induces an isomorphism \(\widetilde H_{n-1}(L_w;\mathbb Z)\xrightarrow{\sim}\widetilde H_{n-1}(A_n;\mathbb Z)\).

**3. Integral equivariant exact sequence.** Every matching either belongs to \(A_n\) or has a unique spoke, and therefore
\[
X_n=A_n\ \cup\ \bigcup_{w\in W_n}(w*L_w),
\]
where different spoke cones meet only inside \(A_n\). Consequently the relative chain complex \(C_*(X_n,A_n;\mathbb Z)\) splits as the direct sum of the reduced complexes of the spoke links, shifted upward by one degree. Thus
\[
H_k(X_n,A_n;\mathbb Z)\cong
\bigoplus_{w\in W_n}\widetilde H_{k-1}(L_w;\mathbb Z),
\]
and the only nonzero relative group is \(H_n(X_n,A_n;\mathbb Z)\cong\mathbb Z^{W_n}\). Its connecting homomorphism to \(\widetilde H_{n-1}(A_n;\mathbb Z)\cong\mathbb Z\) has component \((j_w)_*\) on the \(w\)-th direct summand. By step 2, every component is an isomorphism.

Use \((j_w)_*\) to identify each relative summand with the *same* orientation lattice \(\widetilde H_{n-1}(A_n;\mathbb Z)\). These identifications commute with every graph automorphism, since \(g\circ j_w=j_{gw}\circ g\). The relative action is therefore \(\theta\otimes\mathbb Z[W_n]\), and its connecting map is \(\theta\otimes\varepsilon\). The reduced long exact sequence of the pair becomes
\[
0\longrightarrow\widetilde H_n(X_n;\mathbb Z)
\longrightarrow\theta\otimes\mathbb Z[W_n]
\xrightarrow{\ \theta\otimes\varepsilon\ }
\theta\longrightarrow\widetilde H_{n-1}(X_n;\mathbb Z)
\longrightarrow0.
\]
Since \(\varepsilon\) is surjective, this proves the claimed **integral** kernel representation, the free rank \(2n-1\), and vanishing of all other reduced homology groups. Notice that the integral kernel is not claimed to split equivariantly as the complement of a trivial lattice summand.

**4. Character and invariants.** Over \(\mathbb Q\), the augmentation kernel has character \(\#\operatorname{Fix}_{W_n}(g)-1\). A spoke is fixed by \(g\) exactly when its blade is fixed and not reversed, giving \(\#\operatorname{Fix}_{W_n}(g)=2f_0(g)\). Tensoring by \(\theta\) yields the displayed complete character formula.

For \(N_n\), the invariant coefficient vectors in \(\mathbb Q[W_n]\) have equal coordinates on the two spokes of each blade. Their augmentation-zero condition leaves dimension \(n-1\). The twist \(\theta\) is trivial on \(N_n\), so the same conclusion holds for homology. To find full \(G_n\)-invariants, use Frobenius reciprocity: \(\mathbb Q[W_n]\) is induced from the stabilizer of one spoke, and the multiplicity of \(\theta\) in it is one exactly when \(\theta\) is trivial on that stabilizer. The stabilizer contains \(S_{n-1}\) acting on the other blades. Thus the multiplicity is one for \(n=2\) and zero for \(n\ge3\). Since \(\theta\) is nontrivial on \(G_n\), it is not present in the trivial quotient \(\mathbb Q\), so the same multiplicity holds in the augmentation kernel. This proves the full invariant-space formula.

## Verification
The standalone program `artifacts/verify.py` constructs the graphs and every matching face directly. For \(n=2,3,4\), it tests all \(2^n n!\) automorphisms by computing **signed augmented simplicial Lefschetz traces**, independently of the relative-chain proof. Across these three sizes there are \(8+48+384=440\) exact group-element checks. It also reduces all mod-two boundary matrices for those sizes, finding only the expected Betti numbers \(3,5,7\) in degrees \(2,3,4\). Twenty additional signed-Lefschetz tests for \(n=5\) include blade cycles and nontrivial internal reversals. The recorded output finishes with `VERIFY_OK`. These finite tests do not substitute for the proof for all \(n\ge2\) or verify the integral module by themselves; the all-parameter integral conclusion follows from the long exact sequence and the explicit orientation identifications above.

## Relationship to prior work
Donovan and Scoville, *Star clusters in the matching, Morse, and generalized Morse complex* (first publicly available July 27, 2022), give the **nonequivariant** Dutch-windmill matching-complex homotopy classification. Their Theorem 30 gives \(X_n\simeq\bigvee^{2n-1}S^n\) for the five-cycle blades but does not calculate automorphism-group homology actions.

The earlier online result *Blade-permutation homology of Dutch windmill matching complexes* determines the **restricted rational \(S_n\)-character** for a family of cycle lengths, including five. It explicitly leaves within-blade automorphisms and the integral lattice unclassified. The present theorem restricts to the known character \(\operatorname{sgn}_n\otimes(\mathbf1\oplus2\mathrm{Std}_n)\), but additionally identifies the **full wreath-product action over \(\mathbb Z\)**. Internal blade reversals act nontrivially on the homology and cannot be recovered merely from the restricted \(S_n\)-character. Bate, Everitt, Ford and Ramos study symmetric-group representations of the matching complexes of complete hypergraphs, a distinct graph family and symmetry action, not the present windmill group.

## Limitations
The result treats pentagonal blades, \(n\ge2\), and the ordinary matching complex. The full integral module is described as a kernel, not decomposed into integral indecomposables. No equivariant homotopy equivalence is claimed. The lack of an indexed equivalent theorem is not a mathematical proof of uniqueness; unindexed or unpublished formulations remain a residual originality risk. The independent audit has not been performed.

## References
1. Connor Donovan and Nicholas A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1 (July 27, 2022), Theorem 30; revised journal presentation in *New York Journal of Mathematics* 29 (2023), 1393–1412. https://arxiv.org/abs/2207.13780
2. *Blade-permutation homology of Dutch windmill matching complexes*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-blade-permutation-homology-of-dutch-windmill-matching-complexes--4a7f2d144faf
3. Michael Bate, Brent Everitt, Sam Ford and Eric Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750v1 (December 21, 2023), https://arxiv.org/abs/2312.13750
