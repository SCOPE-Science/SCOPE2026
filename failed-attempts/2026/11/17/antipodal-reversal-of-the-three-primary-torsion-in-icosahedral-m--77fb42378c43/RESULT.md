# Antipodal reversal of the three-primary torsion in icosahedral matching homology

## Finding
Let \(I\) be the regular icosahedral graph, \(K=\mathcal M(I)\) its ordinary matching complex, and \(\tau\) the vertex-antipodal graph automorphism. The three-primary torsion group in \(\widetilde H_3(K;\mathbb Z)\) is nonzero and cyclic, and the antipodal action on it is multiplication by \(-1\). Moreover, the ordinary orbit space has the complete three-local reduced homology
\[
\widetilde H_j(|K|/\langle\tau\rangle;\mathbb Z_{(3)})\cong
\begin{cases}\mathbb Z_{(3)}^{40},&j=3,\\0,&j\ne3.\end{cases}
\]
Here \(\mathbb Z_{(3)}\) denotes integers localized at the prime three. The previously established nonequivariant integral homotopy decomposition \(K\simeq(\bigvee^{64}S^3)\vee M(\mathbb Z/3,3)\) is prior work, not part of the new claim. The new information is the sign of the antipodal action on torsion and the elimination of all three-torsion in the ordinary antipodal quotient.

## Assumptions and scope
Vertices are \(0,\ldots,11\), with the thirty undirected edges given explicitly by the `EDGES` constant in `verify_icosa_antipodal.py`. These edges describe the icosahedral graph: all twelve vertices have degree five, all twenty triangular facets form the standard icosahedral triangulation, and each vertex has a **unique** opposite vertex at graph distance three. Define \(\tau(v)\) to be that opposite vertex. The verifier reconstructs the resulting graph involution and its action on the thirty edge-vertices of the matching complex. A simplex of \(K\) is a collection of pairwise endpoint-disjoint graph edges. Its cellular orientation is the increasing order of the indexed edges. No coefficient fields of characteristic two are used for the eigenspace splitting.

## Proof
**Complete chain complex.** Enumerating all matchings gives, in dimensions zero through five, the complete face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(30,315,1400,2535,1482,125).
\]
The signed simplicial differential removes one indexed edge at a time with its alternating sign. Applying \(\tau\) to an oriented simplex gives the sorted image simplex multiplied by the parity of the induced edge permutation. The verifier reconstructs the involution and checks that it preserves every simplex and the oriented differential.

**Exact antipodal eigenspace calculation.** Over any field of characteristic other than two, the chain complex decomposes into the \(+1\) and \(-1\) eigenspace subcomplexes. For a two-element simplex orbit, use the eigenvector consisting of an oriented simplex plus or minus its signed antipodal image; for a fixed simplex, retain it only in the matching orientation eigenspace. The code constructs these bases and performs deterministic sparse Gaussian elimination directly on all resulting signed boundary matrices.

For the \(+1\) subcomplex, the chain dimensions in simplex cardinalities zero through six (including the augmented empty face) are
\[
(1,15,150,700,1290,741,55).
\]
For the \(-1\) subcomplex they are
\[
(0,15,165,700,1245,741,70).
\]
The augmented-boundary ranks in those cardinalities, with an initial zero, are respectively
\[
(0,1,14,136,564,686,55),
\]
\[
(0,0,15,150,550,670,70)
\]
over \(\mathbb F_3\), and the same except for the \(-1\) rank from cardinality five to four, which increases from \(670\) to \(671\), over \(\mathbb F_5\). Thus the reduced eigenspace Betti vectors, indexed by degrees zero through four, are
\[
\begin{array}{c|cc}
&+1&-1\\\hline
\mathbb F_3&(0,0,0,40,0)&(0,0,0,25,1)\\
\mathbb F_5&(0,0,0,40,0)&(0,0,0,24,0).
\end{array}
\]
The boundary from degree five is injective in both eigenspaces, so degree five homology is zero. As a separate matrix construction, the verifier forms the **full** unorbitsplit augmented boundary matrices and obtains ranks \((0,1,29,286,1114,1356,125)\) over \(\mathbb F_3\) and \((0,1,29,286,1114,1357,125)\) over \(\mathbb F_5\); each equals the sum of the two independent eigenspace ranks.

**Integral three-torsion sign.** Let \(T\) be the three-primary torsion subgroup in integral degree-three reduced homology. The mod-five degree-four vanishing proves that integral \(H_4\) has rank zero. The mod-three degree-five vanishing rules out integral three-primary torsion in \(H_4\) by the universal coefficient theorem. Therefore the natural Bockstein/universal-coefficient isomorphism
\[
\widetilde H_4(K;\mathbb F_3)\cong
\operatorname{Tor}(\widetilde H_3(K;\mathbb Z),\mathbb F_3)
\]
is equivariant for \(\tau\). Its one-dimensional source is entirely \(-1\)-eigen, proving that \(T\) has one cyclic factor and that \(\tau\) reduces to multiplication by \(-1\) modulo three on that factor. Because \(\tau\) is an involution, its action on a cyclic group of order a power of three must itself be either \(+1\) or \(-1\); the reduction forces \(-1\). The established integral homotopy result independently determines \(T\cong\mathbb Z/3\), though that precise exponent is not needed for the antipodal sign argument.

**Orbit-space homology.** For the action of the two-element group, barycentric subdivision yields an admissible simplicial action. Since two is invertible in \(\mathbb Z_{(3)}\), the chain invariants compute the ordinary orbit-space homology, and the invariant-chain functor is exact. The \(+1\)-eigenspace mod-three calculation has exactly forty degree-three classes and none elsewhere. The degree-four mod-three invariant homology vanishes, so there is no three-primary torsion in invariant integral degree three; the lower-degree mod-three vanishing excludes a hidden lower-degree extension. Hence invariant three-local integral homology is free of rank forty and concentrated in degree three. This proves the quotient formula, without an assertion of integral contractibility or any assertion about two-primary torsion.

## Verification
Run `python3 verify_icosa_antipodal.py` under Python 3, with no third-party dependencies. The program constructs all \(5887\) nonempty simplices, determines opposite vertices from graph distances, builds all signed boundary maps, computes two independent forms of each modular rank, and asserts the exact tables displayed above. The verified output is included as `icosa_antipodal_output.txt`, ending with `ICOSAHEDRAL_ANTIPODAL_TORSION_SIGN_PASS`. The provided executable source is the certificate; an output log alone is not treated as proof.

## Relationship to prior work
Shareshian and Wachs (arXiv:math/0409054; first public 2004-09-03) develop integral torsion calculations for the **complete-graph** matching complexes and chessboard complexes, not the antipodal action on this icosahedral subgraph complex. Engström (arXiv:math/0512420; first public 2005-12-17) studies independence complexes of claw-free graphs, which includes matching complexes via line graphs, but gives connectivity rather than the present torsion character. A published 2026 research record entitled *Three-torsion in the icosahedral matching complex: a planar counterexample* (public published-finding corpus record suffix `28565ad1ea1a`) determines the **integral homotopy type of this exact complex**, including its unique order-three torsion summand. Its complete available result does not determine the antipodal involution's action or the three-local homology of the quotient. Those are the claims proved here. An abstract homotopy type alone does not specify an automorphism action on homology, so the present sign statement is not a corollary of the prior nonequivariant decomposition.

## Limitations
The claim is restricted to the canonical antipodal involution and the prime-three localization of the quotient. It does not determine the complete full-automorphism integral module, the ordinary quotient's two-primary torsion, its fundamental group, or its homotopy type. The absolute uniqueness of the result in unindexed literature is not certified. The finite rank calculations are exact but rely on a reproducible computational enumeration; no separate independent mathematical audit has been carried out.

## References
1. J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first publicly available 2004-09-03), https://arxiv.org/abs/math/0409054 .
2. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420 (first publicly available 2005-12-17), https://arxiv.org/abs/math/0512420 .
3. *Three-torsion in the icosahedral matching complex: a planar counterexample*, public published-finding corpus research record (2026; stable suffix `28565ad1ea1a`), repository https://github.com/published-finding corpus/2026 .
