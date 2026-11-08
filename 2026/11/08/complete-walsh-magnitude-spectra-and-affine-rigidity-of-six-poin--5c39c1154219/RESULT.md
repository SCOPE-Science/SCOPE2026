# Complete Walsh-magnitude spectra and affine rigidity of six-point binary sets

## Finding
Let \(E\) be any six-element subset of \(\mathbb F_2^d\), where \(d\ge3\). The number of nonzero coefficients of the Walsh transform of \(1_E\) determines the entire affine-equivalence type of \(E\). In fact, all magnitudes and their multiplicities are classified as follows. Put \(r=\dim\operatorname{aff}(E)\). For each magnitude \(a\in\{0,2,4,6\}\), let \(M_a=|\{u\in\mathbb F_2^d:|W_E(u)|=a\}|\). The entries in the central table are \((M_0,M_2,M_4,M_6)/2^{d-r}\).

| Affine type | \(r\) | Normalized multiplicities \((0,2,4,6)\) | \(s(E)/2^d\) |
|---|---:|---|---:|
| Three-flat with two points removed | 3 | \((4,3,0,1)\) | \(1/2\) |
| Four-circuit with two independent additional points | 4 | \((6,7,2,1)\) | \(5/8\) |
| Six-point affine circuit | 4 | \((0,15,0,1)\) | \(1\) |
| Six-point affine simplex | 5 | \((10,15,6,1)\) | \(11/16\) |

These four types are each one affine-equivalence class and are all attained for \(d\ge5\). Only the first occurs when \(d=3\), and only the first three when \(d=4\). Thus the support of the Walsh transform is the entire dual group exactly for an affine six-circuit in a four-dimensional affine span.

## Assumptions and scope
Everything is over the field \(\mathbb F_2\). The unnormalized Walsh transform is
\[
W_E(u)=\sum_{x\in E}(-1)^{u\cdot x}, \qquad u\in\mathbb F_2^d,
\]
and \(s(E)=|\{u:W_E(u)\ne0\}|\). The rank \(r\) is the dimension of the smallest affine subspace containing \(E\); \(3\le r\le5\). An affine circuit is a minimal nonempty, even-cardinality subset whose vector sum is zero (the unique nontrivial affine dependence when \(r=4\)). Affine equivalence means an invertible affine map of the ambient binary vector space. Coefficients are integer-valued; no sign or phase constraint beyond the indicator \(1_E\) is hidden. The claim is for every integer \(d\ge3\), not only the checked small dimensions.

## Proof
**Step 1: Reduction to affine rank and four combinatorial types.** Translation changes Walsh phases but not magnitudes. After translating one point to zero, the differences span a space of dimension \(r\). A character on the ambient space restricts to a character on that \(r\)-dimensional difference space, and every local character has exactly \(2^{d-r}\) extensions. Therefore every local magnitude multiplicity is multiplied by \(2^{d-r}\).

There are six augmented affine columns and the affine-relation space has dimension \(5-r\). If \(r=5\), there are no relations; all such sets are affinely equivalent to \(\{0,e_1,e_2,e_3,e_4,e_5\}\). If \(r=4\), there is exactly one nonzero affine relation. Since it has even support and distinct points preclude two-point relations, its support has size four or six. By choosing independent affine coordinates, every configuration of either kind is equivalent to one normal form. Representatives are \(\{0,e_1,e_2,e_1+e_2,e_3,e_4\}\) and \(\{0,e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}\), respectively. If \(r=3\), the set is an affine three-flat with precisely two points removed; the affine group acts transitively on unordered pairs of distinct points. These are exactly four types, and all listed representatives have six distinct points.

**Step 2: Pair-sum energies.** Work in the local group \(V=\mathbb F_2^r\) after translating \(E\). For each nonzero \(t\in V\), let \(q(t)\) be the number of unordered distinct pairs \(\{x,y\}\subset E\) with \(x+y=t\). The convolution \(h=1_E*1_E\) satisfies \(h(0)=6\) and \(h(t)=2q(t)\) for nonzero \(t\). Hence the exact identity
\[
\sum_{u\in V}|W_E(u)|^4
=2^r\sum_{t\in V}h(t)^2
=2^r\left(36+4\sum_{t\ne0}q(t)^2\right).
\]
For a three-flat minus \(\{a,b\}\), exactly one nonzero difference, \(a+b\), has \(q=3\), and the other six have \(q=2\). Thus the parenthesized energy is \(168\). For a four-circuit, its three internal pair-sums occur twice; the other nine pair-sums each occur once, giving energy \(120\). For a six-circuit, no four-point relation is possible, so all fifteen unordered pair-sums are distinct; the energy is \(96\). The same absence of four-point relations holds for an affine five-simplex, also giving \(96\). These distributions account for all \(\binom62=15\) pairs in each case.

**Step 3: Recover all magnitudes and multiplicities.** All Walsh values are sums of six signs, so their absolute values belong to \(\{0,2,4,6\}\). The value \(6\) in absolute magnitude occurs for precisely the trivial local character: since \(E\) affinely spans \(V\), any character taking a constant sign on all its points must annihilate every difference, and is therefore trivial. Write \(m_a\) for the local multiplicities. The total character count, Plancherel identity, and Step 2 give
\[
\begin{aligned}
m_0+m_2+m_4+m_6&=2^r,\\
m_6&=1,\\
4m_2+16m_4+36&=6\cdot2^r,\\
16m_2+256m_4+1296&=2^r Q,
\end{aligned}
\]
where \(Q\) is respectively \(168,120,96,96\). Solving this exact integer linear system yields the four multiplicity rows stated above. Multiplying by \(2^{d-r}\) gives the ambient answer. Their nonzero-support fractions \(1/2,5/8,1,11/16\) are mutually distinct, proving the affine rigidity consequence. This argument requires no enumeration in unbounded dimension.

## Verification
The self-contained Python 3 checker `CHECK.py` computes all six-subsets of \(\mathbb F_2^3\) and \(\mathbb F_2^4\), determines their affine-relation type from exact binary rank and four-subset XOR tests, and checks every coefficient with integer Walsh sums. It also evaluates all four canonical types in dimension five. It checks the \(28\) three-dimensional subsets and the \(8008\) four-dimensional subsets, including the predicted dimension-four class counts \(840,6720,448\). Its final output is `CHECK_OK exact_subsets_3d=28 exact_subsets_4d=8008 canonical_5d=4`. Run `python3 CHECK.py`; it requires no third-party packages. The proof above, rather than finite enumeration, establishes the theorem for all \(d\).

## Relationship to prior work
Kadowaki, *Fuglede's conjecture holds in* \(\mathbb F_2^7\) (arXiv:2610.24022v1, first posted 2026-10-16), proves spectrality and tiling results and an eight-point Fourier zero-avoidance theorem. Ferguson and Iosevich, *Fuglede's conjecture holds in* \(\mathbb F_p^d\) *for* \(p=2,d=8\) *and* \(p=11,d=3\) (arXiv:2610.30712v1, first posted 2026-10-22), prove in particular that certain indicator Fourier supports contain two-dimensional subspaces. Neither stated result supplies the six-point magnitude multiplicities and affine reconstruction law here. Jauberty and Méaux, *On the Cardinality of the Walsh Support of a Boolean Function* (IACR ePrint 2025/1651), characterize attainable Walsh-support cardinalities for Boolean functions without prescribing Hamming weight or identifying all six-point affine classes. Their full text was not available for complete comparison, leaving a priority risk. The standard character orthogonality, fourth-moment identity, and elementary binary matroid circuit facts are classical ingredients and are not claimed as original.

## Limitations
The statement concerns binary indicators of sets of **exactly six** elements and their unnormalized Walsh transform; it does not classify arbitrarily weighted six-sparse functions, other support sizes, or stability under perturbations. The Fourier support size distinguishes affine **types**, not individual supports within an affine orbit. The accessible literature comparison does not establish historical priority against every earlier Boolean-function table or equivalent coding-theory formulation. No independent mathematical validation has been performed.

## References
1. A. Kadowaki, *Fuglede's conjecture holds in* \(\mathbb F_2^7\), arXiv:2610.24022v1 (2026-10-16), https://arxiv.org/abs/2610.24022.
2. S. J. Ferguson and J. Iosevich, *Fuglede's conjecture holds in* \(\mathbb F_p^d\) *for* \(p=2,d=8\) *and* \(p=11,d=3\), arXiv:2610.30712v1 (2026-10-22), https://arxiv.org/abs/2610.30712.
3. M. Jauberty and P. Méaux, *On the Cardinality of the Walsh Support of a Boolean Function*, IACR Cryptology ePrint Archive 2025/1651 (2025), https://eprint.iacr.org/2025/1651.
