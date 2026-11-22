# Exact Walsh spectrum and optimal range projection for Heawood perfect matchings

## Finding
Let \(H\) be the Heawood graph, the bipartite point-line incidence graph of the Fano plane. On the Boolean group \(G=\mathbb F_2^{E(H)}\), with \(|E(H)|=21\), let \(\mu\) be the indicator of the edge-incidence vectors of the perfect matchings of \(H\). Its (unnormalized) XOR convolution operator \(Tg=\mu*g\) has the following **complete signed Walsh spectrum**, with multiplicities:

| Walsh multiplier | Multiplicity |
|---:|---:|
| \(-24\) | 4,096 |
| \(-8\) | 356,352 |
| \(0\) | 1,376,256 |
| \(8\) | 356,352 |
| \(24\) | 4,096 |

Consequently \(\operatorname{rank}T=720896\), \(\operatorname{nullity}T=1376256\), and the ratio of largest to least nonzero singular value is exactly \(3\). If \(W=\operatorname{ran}T\), the sharp endpoint constants for **all** real or complex linear projections onto \(W\), not merely translation-invariant ones, are
\[
\min_{Q^2=Q,\ \operatorname{ran}Q=W}\|Q\|_{\ell^1(G)\to\ell^1(G)}
=\min_{Q^2=Q,\ \operatorname{ran}Q=W}\|Q\|_{\ell^\infty(G)\to\ell^\infty(G)}
=\frac{93}{16}.
\]
The Moore–Penrose inverse of \(T\) has \(\ell^2\)-operator norm \(1/8\) with counting-measure normalization. These are exact finite-dimensional assertions, not asymptotic claims.

## Assumptions and scope
Number the seven line vertices and seven point vertices by \(0,\ldots,6\). The line \(L_i=\{i,i+1,i+3\}\pmod 7\) is adjacent to its three points. An edge is the ordered pair \((i,j)\) with \(j\in L_i\), sorted lexicographically in the certificate. A perfect matching is a set of seven disjoint incidence edges covering all fourteen vertices, equivalently a permutation \(\sigma\) of \(\{0,\ldots,6\}\) satisfying \(\sigma(i)\in L_i\) for every \(i\).

For \(\xi\in G\), write \(\chi_\xi(x)=(-1)^{\langle\xi,x\rangle}\), and \(\Lambda(\xi)=\sum_M\chi_\xi(\mathbf1_M)\), summing over all perfect matchings. The operator is unnormalized convolution, while inverse Fourier transforms have factor \(2^{-21}\). Rank and nullity refer to the full \(2^{21}\)-dimensional real or complex function space. The endpoint norms use ordinary counting-measure \(\ell^1\) and \(\ell^\infty\) norms.

## Proof
**Step 1: a signed permanent-determinant coincidence.** Let \(A\) be the seven-by-seven unsigned incidence matrix \(A_{ij}=\mathbf1_{j\in L_i}\). Any two different lines intersect in exactly one point. Hence \(AA^{\mathsf T}=2I+J\) and \(|\det A|=24\). Complete recursive matching enumeration gives \(\operatorname{perm}A=24\); the explicit algorithm checks all admissible bijections independently. Equality of the absolute determinant and the unsigned permanent forces every contributing permutation to have the same parity. For our prescribed order that parity is even. Thus for *every* assignment of signs to incidence edges, the signed matching enumerator equals the ordinary determinant of the signed incidence matrix. This is an equality of all twenty-four signed monomials, not an equality merely at the all-positive point.

**Step 2: reduce all Walsh characters to 256 signings.** Choose the lexicographically first spanning tree by the standard union-find greedy rule on the fourteen vertices. It has thirteen edges; the eight cotree edges in order are
\[
(2,3),(3,4),(4,4),(4,5),(5,5),(5,6),(6,2),(6,6).
\]
Multiplying all three edge signs at a single point or line vertex by \(-1\) multiplies the weight of every perfect matching by exactly \(-1\). Since the underlying graph is connected, vertex sign switchings can make all thirteen tree-edge signs positive. Each normalized character is therefore determined by the signs on the eight cotree edges. There are exactly \(2^{13}\) original character signings for each normalized choice, half changing the common matching sign and half not. The zero/nonzero status is invariant under these switchings.

**Step 3: exhaustive exact reduced determinant census.** For each of the \(2^8=256\) cotree sign vectors \(t\), make a signed incidence matrix \(A_t\) by placing \(-1\) on exactly the negatively marked cotree incidences and \(+1\) on all other incidences. The 256 exact integer determinants have the complete table

| \(\det A_t\) | Number of \(t\) |
|---:|---:|
| \(-8\) | 45 |
| \(0\) | 168 |
| \(8\) | 42 |
| \(24\) | 1 |

This is a mathematically exhaustive finite check, not a sampling inference: `verify.py` constructs the full list of all 256 signings from the displayed incidence rule, evaluates each determinant by exact fraction-free elimination, separately evaluates its signed permanent by a row-state recursion, and separately checks the enumeration of all matchings. The three calculations agree at every signing. The table and the switching multiplicities give the full signed spectrum and rank above. In particular every nonzero multiplier has absolute value \(8\) or \(24\).

**Step 4: exact optimal projection norm.** Let \(\mathcal C\subseteq G\) be the eight-dimensional binary cycle space, orthogonal to the thirteen-dimensional cut space. The Fourier symbol of the orthogonal projection onto \(W\) is \(\mathbf1_{\Lambda\ne0}\). It is constant on cut-space cosets by Step 2; therefore its inverse Fourier kernel \(q\) is supported on \(\mathcal C\). Express the elements of \(\mathcal C\) in the fundamental-cycle basis, indexed by the eight cotree edges. For each \(x\in\mathbb F_2^8\), the integer \(256q(x)\) is the eight-variable Walsh transform of the indicator of the 88 nonzero normalized determinants. The complete integer kernel histogram is

| \(256q(x)\) | Multiplicity in \(\mathcal C\) |
|---:|---:|
| \(-8\) | 77 |
| \(0\) | 108 |
| \(8\) | 42 |
| \(16\) | 28 |
| \(88\) | 1 |

All \(2^8\) coefficients are checked independently by the direct character sum and by an in-place Walsh–Hadamard transform. The convolution norm equals the \(\ell^1\) norm of this kernel,
\[
\|q\|_1=\frac{77\cdot8+42\cdot8+28\cdot16+88}{256}=\frac{93}{16}.
\]
Finally let \(R\) be *any* linear projection onto \(W\). Averaging the conjugates of \(R\) by every translation of \(G\) yields a translation-commuting projection onto the same \(W\), with endpoint norm no greater than that of \(R\). Character diagonalization makes the translation-commuting projection onto \(W\) unique, namely convolution by \(q\). Thus no arbitrary projection can improve either endpoint norm, and convolution by \(q\) attains the displayed minimum.

## Verification
Run `python3 verify.py` in a directory containing the standalone file. It uses only the Python standard library. Its separate exact checks are (i) the Fano incidence axioms; (ii) all 24 matchings by permutation enumeration and recursive enumeration; (iii) the 13-edge spanning tree and eight fundamental cycles; (iv) signed permanents by dynamic programming and determinants by Bareiss elimination for **all 256 normalized signings**; (v) complete signed spectral and Parseval tables; (vi) both direct and fast inverse transforms on the full reduced group; (vii) exact full-space multiplicity and endpoint-norm arithmetic. The certificate enumerates all required finite configurations; the general translation-averaging proof is supplied above and is not inferred from numerical output.

## Relationship to prior work
The incidence geometry, perfect-matching count \(24\), Hamiltonian complements, and two-factor structure of the Heawood graph are established background. Abreu–Labbate–Sheehan (arXiv:1002.1891v1, posted 2010-02-09) examine the two-factor-isomorphic cubic graphs, and Brouwer's graph reference explicitly gives the 24 perfect matchings. Araujo–Balogh–Wang (arXiv:2011.01892v1) treat **unsigned** sparse permanent/determinant bounds and note the Fano incidence determinant \(24\). These inputs do not state the full *signed* permanent histogram across all incidence-edge signings, the Boolean-convolution rank, or the exact unrestricted endpoint projection norm. General Fourier inversion and translation averaging are standard, and their use here is not asserted to be novel. The separately known Fourier spectrum of the 28 six-cycles in this same graph concerns a different incidence codebook and does not imply the present 24-matching spectrum merely from the shared graph.

## Limitations
This is a complete finite result for the specified Fano-incidence graph, not a theorem for all projective planes or all cubic bipartite graphs. The signed histogram and exact norm depend on exhaustive but fully reproduced 256-case integer calculations; no purely symbolic uniform derivation of the histogram is asserted. Unindexed older signed-incidence determinant tables may contain equivalent evaluations. The mathematical argument has received self-review only; no independent audit has been performed. The full text of a potentially relevant 2004 two-factor paper was not available in the comparison, although its subject is structural two-factor classification rather than signed Fourier inversion.

## References
- M. Abreu, D. Labbate, J. Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs*, arXiv:1002.1891v1, 2010-02-09. https://arxiv.org/abs/1002.1891
- A. E. Brouwer, *Heawood graph*, specialist distance-regular-graph reference, https://aeb.win.tue.nl/graphs/Heawood.html
- I. Araujo, J. Balogh, Y. Wang, *Maximum determinant and permanent of sparse 0-1 matrices*, arXiv:2011.01892v1, 2020-11-03. https://arxiv.org/abs/2011.01892
- M. Abreu et al., *Graphs and digraphs with all 2-factors isomorphic*, J. Combin. Theory Ser. B 92 (2004), 395–404, DOI:10.1016/j.jctb.2004.09.004 (abstract inspected; full text not verified).
