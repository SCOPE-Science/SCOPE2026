# Finite-color detection and integral cross-effect splitting for categorical-product independence complexes

## Finding

For any **nonempty finite simple graph** \(G\), let \(G\times K_n\) be the categorical graph product: its vertex set is \(V(G)\times\{1,\ldots,n\}\) and its edges join \((u,i)\) and \((v,j)\) exactly when \(uv\in E(G)\) and \(i\ne j\). Put \(X_n=\operatorname{Ind}(G\times K_n)\).

For \(s\ge1\), let \(p_i:X_{s+1}\to X_{s+1}\), for \(2\le i\le s+1\), merge color \(i\) into the distinguished color 1, leaving all other colors unchanged. For \(d\ge0\), define the finitely generated abelian group
\[
A_{d,s}(G)=\bigcap_{i=2}^{s+1}\ker\bigl((p_i)_*:\widetilde H_d(X_{s+1};\mathbb Z)\to\widetilde H_d(X_{s+1};\mathbb Z)\bigr).
\]
Then for **every** integer \(d\ge0\) and \(n\ge1\),
\[
\boxed{\widetilde H_d(X_n;\mathbb Z)\cong\bigoplus_{s=1}^{\min(d,n-1)}A_{d,s}(G)^{\oplus\binom{n-1}{s}}.}
\]
The summands correspond to named subsets of nonbase colors. Inclusions \(X_m\hookrightarrow X_n\) for \(m\le n\) respect these summands and induce split injections over \(\mathbb Z\). Consequently \(\widetilde H_d(X_{d+1};\mathbb Z)\), **together with its named color-merger endomorphisms**, determines the groups in degree \(d\) at **every** palette size, including all integral torsion. The presence or absence of torsion requires only the abstract group at this stage: degree-\(d\) torsion is absent at every palette size if and only if it is absent at \(d+1\) colors. The rational degree-\(d\) Betti numbers satisfy
\[
\widetilde\beta_d(X_n)=\sum_{s=1}^{d}\operatorname{rank}_{\mathbb Z} A_{d,s}(G)\binom{n-1}{s},
\]
with nonnegative integer coefficients; this identity holds at *all* positive integers \(n\), not merely eventually. Empty sums are zero.

## Assumptions and scope

The graph is finite, undirected, nonempty, simple and loop-free; isolated vertices are allowed. The graph \(K_1\) has one vertex and no edges. All homology is reduced simplicial homology with integer coefficients. Maps induced by color mergers are simplicial maps of independence complexes, **not** in general graph homomorphisms of categorical products. A palette inclusion fixes the distinguished color 1. The result is degreewise; it does not claim a finite test of torsion across every homological degree at once, nor an equivariant splitting under all color permutations.

## Proof

**1. Color mergers are simplicial.** For any set map \(f:[n]\to[m]\), send \((v,i)\mapsto(v,f(i))\). If an image pair were adjacent in \(G\times K_m\), then its underlying vertices would form a \(G\)-edge and its two image colors would differ; the source colors would therefore also differ, making the original pair adjacent. Contraposition proves that the image of every independent set remains independent (repeated vertices are simply identified). Thus all color identifications induce well-defined chain maps.

**2. Orthogonal integral chain projections.** On \(C_*(X_n;\mathbb Z)\), let \(p_i\) merge \(i\) with 1 for \(2\le i\le n\). These normalized simplicial chain maps commute and satisfy \(p_i^2=p_i\), including orientation signs and zero images from repeated vertices. For each \(S\subseteq\{2,\ldots,n\}\), set
\[
E_S=\prod_{i\in S}(1-p_i)\prod_{j\in\{2,\ldots,n\}\setminus S}p_j.
\]
They commute with the boundary, are pairwise orthogonal idempotents, and sum to the identity. Hence the entire integral chain complex splits as the direct sum of its subcomplexes \(E_S C_*\). The image \(E_S C_*\) is contained in the subcomplex using only colors \(\{1\}\cup S\); the evident inclusion of that subcomplex, followed by color-merging all outside colors, identifies its \(E_S\)-summand with \(\prod_{i\in S}(1-p_i) C_*(X_{s+1})\), where \(s=|S|\). On homology this is precisely \(\bigcap_{i\in S}\ker(p_i)_*\): commuting idempotents \(1-(p_i)_*\) have product whose image equals their kernel intersection. Therefore each named \(s\)-subset contributes one copy of \(A_{d,s}(G)\).

**3. The extra one-color vanishing lemma.** A simplex of dimension \(d\) has only \(d+1\) vertices. If \(|S|>d+1\), it omits one color of \(S\), so \((1-p_i)\) annihilates it and \(E_S C_d=0\). If \(|S|=d+1\), any \(d\)-simplex that survives \(E_S\) must use each color of \(S\) exactly once and no vertex of color 1. Since the distinct colors make every pair of its vertices eligible for a categorical-product edge, its underlying vertices form an independent set in \(G\). Choose the underlying vertex \(v\) of one of its vertices and append \((v,1)\). This produces an independent \((d+1)\)-simplex \(\tau\), because \(G\) has no loops and all its chosen underlying vertices were mutually nonadjacent. Every face of \(\tau\) other than the original \(d\)-simplex omits a color in \(S\), hence is killed by \(E_S\); therefore \(\partial E_S[\tau]=\pm E_S[\sigma]\). The images of those \(d\)-simplices span \(E_S C_d\), so \(E_S C_d\subseteq\partial(E_S C_{d+1})\). Hence \(H_d(E_S C_*)=0\) also when \(|S|=d+1\). Thus only \(|S|\le d\) can contribute to degree \(d\) homology.

**4. Consequences.** Counting the \(\binom{n-1}{s}\) named subsets proves the displayed integral decomposition. Appending new colors identifies the preexisting summands and sends them identically into the enlarged split sum; the reverse map merging every additional color into 1 is an explicit retraction. Since the named summands with \(s\le d\) can all be read from the stage with \(d+1\) colors and its mergers, they determine all larger stages. Direct-sum decompositions preserve and detect torsion, and rational ranks give the polynomial formula. For \(d=0\), all named summands vanish, recovering connectivity of these complexes. This completes the proof for all finite simple \(G\) and every \(d,n\) in the stated ranges.

## Verification

The self-contained script `check/verify.py` enumerates independence faces for an edge, a triangle, a three-vertex path and a pentagon, at palettes of two through four colors. It verifies that merger maps preserve faces and commute with signed simplicial boundaries, checks every tested chain's orthogonal-idempotent decomposition, constructs the cone fillings in the top cross-effect case, and computes low-degree homology over \(\mathbb F_2\) as a separate check of nonnegative binomial coefficient formulas. The recorded successful output appears in `check/verify_output.txt`. These are finite computational stress tests, not the infinite proof; the proof is Steps 1–4.

## Relationship to prior work

Church–Ellenberg–Farb proved the abstract classification of FI-sharp modules (Theorem 4.1.5 in their paper), which already supplies a general subset-indexed module decomposition. That **general algebraic theorem is not new here**. The graph-specific content is the functorial color-identification model and, crucially, the explicit integral cone filling eliminating the highest possible color cross-effect in degree \(d\), giving the \(d+1\)-color test and torsion propagation for this family.

Antolín Camarena and Carnero Bravo gave stagewise homotopy calculations of \(\operatorname{Ind}(C_m\times K_n)\), solved multiple infinite subfamilies, and explicitly posed an integral torsion-freeness question for cycle products. Those known stagewise formulas and the general FI-sharp classification do not state the degreewise all-graph finite-color torsion test with the above graph-theoretic cone proof. The theorem does not itself settle torsion-freeness simultaneously in all degrees for all cycles.

## Limitations

The splitting is an isomorphism of integral homology groups compatible with palette inclusions, not a claimed homotopy wedge splitting or a full \(S_n\)-equivariant representation decomposition. The theorem does not evaluate \(A_{d,s}(G)\) for arbitrary \(G\); it reduces such calculations to bounded-color problems in each specified degree. Finite verification covers only the listed graph instances and low homological degrees. The originality comparison is against the cited primary work and available indexed records; unidentified equivalent literature remains possible.

## References

1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public July 23, 2023), published in *Homology, Homotopy and Applications* 26 (2024), 349–373. https://arxiv.org/html/2307.12401v2
2. T. Church, J. Ellenberg and B. Farb, *FI-modules and stability for representations of symmetric groups*, arXiv:1204.4533, Theorem 4.1.5 on FI-sharp modules. https://arxiv.org/pdf/1204.4533
3. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019). https://arxiv.org/abs/1905.06926
