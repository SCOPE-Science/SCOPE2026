# Prime cyclic color quotients of triangle-coloring Hom complexes: integral homology and cup-length

## Finding

For every odd prime \(p\ge5\), let \(X_p=\operatorname{Hom}(K_3,K_p)\), where the graphs are finite, simple, and loopless. Let \(C_p\) act by a single \(p\)-cycle on the **target color labels**, fixing the three ordered source positions, and let \(Y_p=|X_p|/C_p\) be the ordinary geometric orbit space. Put \(d=p-3\), an even positive integer. Then the action is free, \(\pi_1(Y_p)\cong C_p\), and all integral homology groups are

\[
H_i(Y_p;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/p,&1\le i<d\text{ and }i\text{ odd},\\
\mathbb Z^{(2^p-p-2)/p},&i=d,\\
0,&\text{otherwise}.
\end{cases}
\]

The quotient's mod-\(p\) cohomology through degrees strictly below \(d\), including its products whose total degree is below \(d\), is the corresponding truncation of
\[H^*(BC_p;\mathbb F_p)=\Lambda_{\mathbb F_p}(v)\otimes\mathbb F_p[u],\qquad |v|=1,\ |u|=2.\]
In particular, its **exact positive-degree mod-\(p\) cup-length** is
\[\operatorname{cl}_{\mathbb F_p}(Y_p)=\frac{p-3}{2}.\]
For \(p\ge7\), the mod-\(p\) Bockstein of the canonical degree-one class satisfies \(\beta(v)=u\), in the asserted degree range. Thus the torsion occurs in an unbounded number of different degrees and the cup-length grows without bound as the prime increases. No higher homotopy equivalence or homeomorphism classification of \(Y_p\) is asserted.

## Assumptions and scope

A cell of \(X_p\) is an ordered triple \((A_1,A_2,A_3)\) of nonempty, pairwise disjoint subsets of the color set \(\mathbb Z/p\). Its closure is \(\Delta(A_1)\times\Delta(A_2)\times\Delta(A_3)\), of dimension \(|A_1|+|A_2|+|A_3|-3\). Faces shrink one or more blocks without making a block empty. A generator \(g\) of \(C_p\) sends \((A_1,A_2,A_3)\) to \((A_1+1,A_2+1,A_3+1)\); the source positions remain ordered. We use singular integral homology, ordinary cohomology with coefficients \(\mathbb F_p\), and the usual cup product. Cup-length means the largest number of positive-degree cohomology classes with a nonzero cup product. The result concerns prime target sizes and these target-label rotations only: it does not classify composites, block-position permutations, or full target-label symmetry.

## Proof

**1. Connectivity and dimension of the covering space.** Babson and Kozlov's complete-graph Hom theorem [2, Proposition 4.5] gives \(\operatorname{Hom}(K_m,K_n)\simeq\bigvee^{f(m,n)}S^{n-m}\), with \(f(3,n)=2^n-3\) [2, Proposition 4.6]. Applying it to \(m=3,n=p\) gives
\[X_p\simeq\bigvee^{2^p-3}S^{p-3}.\]
Consequently \(X_p\) is \((d-1)\)-connected, with reduced integral homology only in degree \(d\); for \(p\ge5\), \(d\ge2\), so \(X_p\) is simply connected. Its actual cellular dimension is at most \(d\), because there are only \(p\) colors and every cell contains three nonempty blocks.

**2. The target rotation is free on points.** Any nonidentity \(g^a\) of \(C_p\) is a transitive \(p\)-cycle on the color set because \(p\) is prime. If it fixed a point of the polyhedral complex, it would preserve the unique relative interior cell containing that point. Hence each \(A_i\) would have to be a nonempty \(g^a\)-invariant subset of the \(p\)-element color set. Transitivity forces every \(A_i\) to be the whole color set, contradicting pairwise disjointness. Thus no nonidentity element fixes any point. The quotient projection is a regular \(p\)-sheeted covering, \(X_p\) is its universal cover, and \(\pi_1(Y_p)=C_p\).

**3. Integral homology strictly below top degree.** Since the action is free, the Borel construction \(EC_p\times_{C_p}X_p\) is homotopy equivalent to \(Y_p\). The Cartan–Leray homology spectral sequence is
\[E^2_{s,t}=H_s(C_p;H_t(X_p;\mathbb Z))\Longrightarrow H_{s+t}(Y_p;\mathbb Z).\]
Only the rows \(t=0\) and \(t=d\) can be nonzero. For total degree \(0<i<d\), only the \(t=0\) row contributes, and no differential can enter or leave the entries under consideration. Therefore \(H_i(Y_p;\mathbb Z)=H_i(C_p;\mathbb Z)\), the integral homology of the cyclic group: \(\mathbb Z/p\) for positive odd \(i\), and zero for positive even \(i\). Connectedness gives \(H_0=\mathbb Z\).

**4. Top degree and its integral freeness.** The free action on product cells gives a finite quotient CW structure of dimension \(d\). Since \(C_{d+1}(Y_p;\mathbb Z)=0\), the top homology \(H_d(Y_p;\mathbb Z)\) is a subgroup of a finitely generated free abelian group and is itself free. The Euler characteristic of the covering space is
\[\chi(X_p)=1+(-1)^d(2^p-3)=2^p-2,\]
using that \(d\) is even. A finite free \(p\)-sheeted CW covering satisfies \(\chi(Y_p)=\chi(X_p)/p=(2^p-2)/p\). Because all positive homology in degrees below \(d\) is torsion, the Euler characteristic of \(Y_p\) is \(1+\operatorname{rank}H_d(Y_p;\mathbb Z)\). Hence the asserted top rank is \((2^p-p-2)/p\); this is integral by Fermat's congruence \(2^p\equiv2\pmod p\). No homology exists in degrees above the cellular dimension.

**5. Multiplicative mod-\(p\) cohomology.** For the same Borel fibration, the mod-\(p\) cohomology spectral sequence begins with
\[E_2^{s,t}=H^s(C_p;H^t(X_p;\mathbb F_p))\Longrightarrow H^{s+t}(Y_p;\mathbb F_p).\]
Again the only nonzero fiber-cohomology rows are \(t=0\) and \(t=d\). Every entry in total degree strictly below \(d\) is consequently in the base row, and the classifying map \(Y_p\to BC_p\) is an isomorphism on mod-\(p\) cohomology in those degrees. Naturality and multiplicativity identify every product whose total degree is below \(d\). For odd prime \(p\), \(H^*(BC_p;\mathbb F_p)=\Lambda(v)\otimes\mathbb F_p[u]\), with \(|v|=1\), \(|u|=2\) and the canonical mod-\(p\) Bockstein \(\beta(v)=u\). The latter identity is imported to \(Y_p\) when its degree two lies strictly below \(d\), namely \(p\ge7\).

**6. Exact cup-length.** The nonzero class \(v\,u^{(d-2)/2}\) has total degree \(d-1\) and is a product of precisely \(d/2\) positive-degree classes. Therefore \(\operatorname{cl}_{\mathbb F_p}(Y_p)\ge d/2\). Conversely \(H^1(Y_p;\mathbb F_p)\) is one-dimensional, generated by \(v\), whose square is zero because \(p\) is odd and the cup product is graded-commutative. Every nonzero product may therefore contain at most one degree-one factor; all other positive-degree factors have degree at least two. A product of \(d/2+1\) factors would have degree at least \(1+2(d/2)=d+1\), exceeding the dimension of \(Y_p\) and hence vanishing. This proves exact cup-length \(d/2=(p-3)/2\). For \(p=5\), the argument uses only the nonzero degree-one class, which is within the guaranteed range.

## Verification

The standalone verifier `verify.py` enumerates every ordered nonempty disjoint three-block cell by coloring each target label as unused or assigned to one of the three source positions. For primes \(p=5,7\), it independently checks that every cell orbit has size \(p\), constructs the actual signed quotient cellular boundaries with orientation-transfer signs, verifies every integral consecutive boundary composition is zero, computes exact sparse ranks over \(\mathbb F_p\) and \(\mathbb F_{1000003}\), and checks the resulting Betti numbers against the theorem. In the \(p=5\) case it also performs integer Smith normal form, finding the single nonunit invariant factor five. Its recorded output is in `verification_output.txt`. Run with Python 3 and the declared dependency in `requirements.txt`. These finite computations corroborate the cellular model and selected special cases; the all-prime conclusion is the mathematical argument above, not an extrapolation.

The quotient orbit-cell counts by dimension for \(p=5\) are \((12,36,30)\), with integral boundary Smith nonunit five; for \(p=7\) they are \((30,180,450,540,258)\), with mod-seven Betti numbers \((1,1,1,1,18)\) and mod-\(1000003\) Betti numbers \((1,0,0,0,17)\), in agreement with the universal formulas and universal coefficient theorem.

## Relationship to prior work

Babson and Kozlov [1, Theorem 6.2(d)] describe the same ordered-disjoint-nonempty-block poset, prove its underlying sphere-wedge concentration, and study a quotient by permutations of **block positions**. Their [2, Propositions 4.5–4.6] give the modern Hom-complex formulation and the precise unquotiented sphere count \(2^p-3\). Those results are expressly prior inputs; their inspected statements do not compute the **target-color** prime-cycle quotient's integral homology, low-degree cohomology ring, or exact cup-length. Existing full target-color character computations [3,4] determine rational group actions and some full or alternating label quotients. Rational characters do not recover the present lower-degree integral cyclic torsion or Bockstein products, and their results concern different subgroups. Prior cyclic chessboard Bockstein results [5] address a different matching-complex family. The novelty claim is restricted to the stated *target-color prime-order quotient's integral and multiplicative classification*. No claim of an original connectivity theorem, non-equivariant Betti formula, or general group-cohomology machinery is made.

## Limitations

No integral top-homology \(\mathbb Z[C_p]\)-module, attaching-map classification, homotopy type beyond fundamental group, or mod-\(p\) cohomology ring in degrees at least \(d\) is determined. The classifying map cohomology-isomorphism statement is asserted only below the covering connectivity cutoff \(d\). The result holds for odd primes at least five; composite color counts are not covered because their nonidentity rotations need not act transitively or freely. While primary statements and close indexed records were compared, hidden equivalent treatments under deleted-product or orbit-space terminology remain a bibliographic priority risk. This is a theorem-level application of classical Hom-complex connectivity and cyclic-group spectral sequences; these tools and the rational character results are not presented as novel. The computation files are finite corroboration, not a proof for unbounded \(p\).

## References

[1] E. Babson and D. N. Kozlov, *Diagrams of classifying spaces and k-fold Boolean algebras*, arXiv:math/9704227, first public preprint 1997-04-29, https://arxiv.org/pdf/math/9704227, especially Definition 6.1 and Theorem 6.2.

[2] E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056, first public preprint 2003-10-05, https://arxiv.org/abs/math/0310056, especially Definition 1.2 and Propositions 4.5–4.6.

[3] *Color-permutation characters of complete-graph Hom complexes*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-color-permutation-characters-of-complete-graph-hom-complexes--50c1a3944425, especially the target-\(S_n\) rational character and its explicit integral-limit statements.

[4] *Full two-sided symmetry character of complete-graph Hom complexes*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-full-two-sided-symmetry-character-of-complete-graph-hom-complexe--ce942485ca98, especially its exact color-\(S_n\)/\(A_n\) rational quotient calculations and integral-limit statements.

[5] *A nontrivial mod-five Bockstein cup-product in the cyclic chessboard quotient*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-nontrivial-mod-five-bockstein-cup-product-in-the-cyclic-chessb--19b7184f8768.
