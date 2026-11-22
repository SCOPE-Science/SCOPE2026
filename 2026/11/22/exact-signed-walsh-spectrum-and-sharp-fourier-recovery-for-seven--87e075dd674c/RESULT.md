# Exact signed Walsh spectrum and sharp Fourier recovery for seven-vertex squared-cycle ice

## Finding

Let \(G=C_7^2\), the simple labelled graph with vertex set \(\mathbb Z/7\mathbb Z\) and fourteen edges joining \(i\) to \(i+1\) and to \(i+2\). Fix the reference orientation of each unordered edge from its smaller integer label to its larger label. Let \(\mathcal I\subseteq\mathbb F_2^{14}\) be the binary edge-reversal vectors of the Eulerian orientations of \(G\), namely the orientations with exactly two outgoing and two incoming edges at every vertex. There are exactly \(60\) such vectors. Define unnormalized counting convolution \(Tf=\mathbf1_{\mathcal I}*f\) on functions on \(\mathbb F_2^{14}\), and define its Walsh multipliers by
\[
W(u)=\sum_{x\in\mathcal I}(-1)^{u\cdot x}\qquad(u\in\mathbb F_2^{14}).
\]
The *complete signed multiplier spectrum* is as follows:

| Multiplier \(W(u)\) | Multiplicity |
|---:|---:|
| \(-60\) | 32 |
| \(-24\) | 224 |
| \(-20\) | 224 |
| \(-16\) | 224 |
| \(-12\) | 224 |
| \(-8\) | 672 |
| \(-4\) | 1,568 |
| \(0\) | 10,048 |
| \(4\) | 1,568 |
| \(8\) | 672 |
| \(12\) | 224 |
| \(16\) | 224 |
| \(20\) | 224 |
| \(24\) | 224 |
| \(60\) | 32 |

In particular,
\[
\operatorname{rank}T=6336,\qquad \operatorname{nullity}T=10048,\qquad
\min_{W(u)\ne0}|W(u)|=4,\qquad
\kappa_2(T\vert_{\operatorname{ran}T})=15.
\]
The inverse of \(T\) restricted to its nonzero Walsh range has sharp Hilbert-space operator norm \(1/4\). Every multiplier is divisible by four. Global orientation reversal forces all \(8192\) odd-weight frequency vectors to vanish, and an additional \(1856\) even-weight frequencies vanish. The zero frequency has multiplier \(60\), while all fourteen one-edge frequencies vanish by reversal symmetry. The *only* zero frequencies of Hamming weight two are the fourteen pairs \(\{A_i,B_{i+2}\}\) and \(\{A_i,B_{i+4}\}\), where \(A_i=\{i,i+1\}\), \(B_j=\{j,j+2\}\), and all vertex subscripts are taken modulo seven.

Let \(R=\operatorname{ran}T\). Among **all** real or complex linear projections \(Q\) onto \(R\), without requiring translation invariance, the sharp endpoint norms are
\[
\boxed{\inf_{Q^2=Q,\ \operatorname{ran}Q=R}\|Q\|_{\ell^1\to\ell^1}
=\inf_{Q^2=Q,\ \operatorname{ran}Q=R}\|Q\|_{\ell^\infty\to\ell^\infty}
=\frac{281}{64}.}
\]

## Assumptions and scope

The edge set has fourteen distinct unordered edges, ordered lexicographically in the standalone verifier. Each coordinate of the vector \(x\) is one exactly when the corresponding edge direction is reversed from the ascending-label reference. Every Eulerian orientation is counted once, with no automorphism quotient or probability normalization. The ambient group has exactly \(2^{14}=16384\) elements. The theorem treats this particular seven-vertex graph, not all squared cycles, all circulants, or an infinite-volume ice model. All displayed norms use counting-measure \(\ell^p\) conventions, which give the same endpoint convolution norm here.

## Proof

**1. Two exhaustive descriptions of the orientation ensemble.** The direct construction tests every one of the \(16384\) binary edge orientations, counting its outgoing edges at each vertex, and retains precisely the vectors with seven outdegrees equal to two. Independently, use the forward jump variables \(a_i,b_i\in\{0,1\}\) for orientations of \(\{i,i+1\}\) and \(\{i,i+2\}\): the Eulerian balance equations are exactly
\[
a_i+b_i=a_{i-1}+b_{i-2}\qquad(i\in\mathbb Z/7\mathbb Z).
\]
Testing all \(2^{14}\) assignments of these variables, translating their directed edges to the lexicographic edge basis, yields exactly the same \(60\) words. Hence both enumerations are exhaustive without an implicit graph-isomorphism or sampling assumption.

**2. Exact integer Fourier certificate by independent constructions.** Applying the standard unnormalized Walsh–Hadamard butterfly to the \(16384\)-entry orientation indicator computes \(W(u)\) for *every* frequency. A second construction uses no orientation enumeration: for \(u\in\mathbb F_2^{14}\), with edges \(e=(a,b)\) ordered so that \(a<b\), the exact coefficient identity is
\[
W(u)=[t_0^2t_1^2\cdots t_6^2]
\prod_{e=(a,b)\in E(G)}(t_a+(-1)^{u_e}t_b).
\]
Indeed each factor selects the edge's source vertex; degree two at each vertex is equivalent to the Eulerian rule, while the coefficient sign records the selected reversal bit. The seven polynomial degrees can be truncated above two without changing the desired coefficient because every exponent only increases.

Every Eulerian reversal vector differs from a fixed reference orientation by a binary cycle-space word, so the Fourier magnitudes are constant on cut-space cosets. A spanning tree has six edges and the cycle space has dimension eight; the verifier therefore independently evaluates the coefficient identity for **all** \(2^8=256\) representatives with tree-edge signs fixed positive, comparing each value against a direct signed sum of the sixty words and the full Walsh transform. The verifier also tests invariance of the zero set under each of the seven generating vertex cuts. The complete transform's exact signed multiplicities are the fifteen rows in the table. As separate integer checks, the multiplicities sum to \(16384\), and Parseval's identity gives \(\sum_uW(u)^2=16384\cdot60\). These finite exhaustive identities prove the exact spectrum; they are not probabilistic evidence.

**3. First nontrivial cancellation.** Reversing every arrow preserves the Eulerian property and complements all fourteen bits, so \(W(u)=(-1)^{|u|}W(u)\), proving the odd-weight zeros. The frequency at zero is \(60\). Exhausting all fourteen one-edge and ninety-one two-edge frequencies in the exact transform confirms all fourteen one-edge zeros and gives exactly the fourteen displayed two-edge pairs. The claimed supports were independently generated using the two jump-edge families and compared with the entire computed set, not merely counted. Rank, Hilbert inverse bound, and condition number now follow from Walsh diagonalization and the exact nonzero spectrum.

**4. Globally optimal endpoint projection.** The orthogonal Fourier projection onto \(R\) is convolution by
\[
K(x)=2^{-14}\sum_{u:W(u)\ne0}(-1)^{u\cdot x}.
\]
A second exact integer Walsh transform of the support indicator computes the \(16384\) integers \(16384K(x)\). Their complete histogram is: numerator \(0\), multiplicity \(16128\); \(\pm448\), multiplicity \(14\) each; \(\pm320\), multiplicity \(42\) each; \(\pm192\), multiplicity \(28\) each; \(\pm64\), multiplicity \(42\) each; and the four remaining exceptional entries \(1856,1856,6336,6336\). Thus the kernel has exactly \(256\) nonzero positions, and
\[
\sum_{x\in\mathbb F_2^{14}}|16384K(x)|=71936,
\qquad\|K\|_{\ell^1}=\frac{71936}{16384}=\frac{281}{64}.
\]
The endpoint norm of convolution by \(K\) equals \(\|K\|_{\ell^1}\) on either \(\ell^1\) or \(\ell^\infty\). If \(Q\) is any real or complex projection onto \(R\), average \(U_gQU_g^{-1}\) over all group translations \(U_g\). Each conjugate preserves \(R\), and the average is again a projection onto \(R\), with no larger endpoint norm. It commutes with all translations, hence is diagonal in the Walsh basis. A translation-invariant projection onto exactly \(R\) must have eigenvalues one on its Fourier support and zero off that support, so the average is precisely convolution by \(K\). This establishes global optimality rather than merely optimality among convolution projections.

## Verification

Run `python3 -S verify_ice7.py` from the directory containing the standalone verifier. It uses only the Python 3 standard library. It exhausts the two distinct orientation descriptions, computes the full \(16384\)-point integer Walsh transform, compares direct signed sums with independent coefficient extraction on all \(256\) tree-gauge representatives, tests the generating cut invariances, checks Parseval, identifies the precise fourteen two-edge vanishing motifs, computes and checks the complete projection kernel histogram, and asserts the exact value \(281/64\). The expected success line is `ICE7_EXACT_PASS`. The proof's all-frequencies claim is supported by complete bounded enumeration; no infinite-family claim is made.

## Relationship to prior work

Felsner (2004) develops general fixed-outdegree orientation lattice structure, but its published abstract and scope do not determine the signed Walsh spectrum on this particular circulant. Golin and Leung (2004) study combinatorial recurrences for graph parameters of circulants and Eulerian orientations; the inspected accessible conference paper provides general counting methods, not a tabulation of individually signed fourteen-edge Fourier coefficients. The cited extended report was not recovered. Isaev (2011) studies asymptotic Eulerian orientation counts under substantial algebraic-connectivity hypotheses rather than this finite signed operator.

A publicly available 2026 result, *Two-winding enumeration of Eulerian orientations on odd cycle squares*, gives the **unweighted count of sixty** here and a complete **two-variable** polynomial for the numbers of forward short and long edges. That count and winding polynomial are prior knowledge, not claimed as new. Their specialization to two uniform weights does not determine the response to all \(2^{14}\) independent edge-sign assignments, the fourteen individual weight-two cancellation motifs, or the Fourier-range projection norm. A separate published result on the octahedral graph \(C_6^2\) determines only degree-one sampling covariances, not this graph's complete convolution spectrum; a published full-spectrum computation for the nine-vertex \(3\times3\) square-ice torus concerns a different graph and cannot imply these precise values without new calculation. These nearby methods are acknowledged as mathematical precedent.

## Limitations

The fifteen-level spectrum, rank, cancellation classification and optimal norm are claimed **only** for the labelled seven-vertex squared cycle with the specified edge coordinates. The proof is an exact complete finite computation and an abstract projection-averaging argument, not a closed formula for all odd cycle squares. The related 2007 work by Zhang and Shen on Eulerian orientations of a class of circulants was accessible only bibliographically; it could contain equivalent scalar enumerations, though no full fourteen-sign spectrum was verified there. The unlocated longer Golin–Leung report and unindexed tables remain historical-priority risks. Independent external mathematical review has not been performed.

## References

1. S. Felsner, *Lattice Structures from Planar Graphs*, Electronic Journal of Combinatorics **11** (2004), R15, published 2004-02-14. DOI: https://doi.org/10.37236/1768
2. M. J. Golin and Y.-C. Leung, *Unhooking Circulant Graphs: A Combinatorial Method for Counting Spanning Trees and Other Parameters*, WG 2004, LNCS **3353**, 296–307 (2004). Open full text: https://cse.hkust.edu.hk/~golin/pubs/golin_WG_04_new.pdf
3. M. Isaev, *Asymptotic behavior of the number of Eulerian orientations of graphs*, arXiv:1110.2598, first submitted 2011-10-12. https://arxiv.org/abs/1110.2598
4. *Two-winding enumeration of Eulerian orientations on odd cycle squares* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-winding-enumeration-of-eulerian-orientations-on-odd-cycle-sq--3a8bfe6cd8c8
5. *The first anisotropic degree-one Walsh frame in quartic graph ice* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-the-first-anisotropic-degree-one-walsh-frame-in-quartic-graph-ic--d9cbbafa7ebf
6. *Complete Walsh spectrum and optimal range projections for the smallest simple periodic square-ice torus* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-walsh-spectrum-and-optimal-range-projections-for-the-sm--fdbca339c304
7. Y. Zhang and X. Shen, *Counting the Eulerian orientations of one class of circulant graphs* (2007), bibliographic record only: https://www.researchgate.net/publication/266247805_Counting_the_Eulerian_orientations_of_one_class_of_circulant_graphs
