# Exact signed Fourier spectrum and sharp endpoint recovery for the order-three Aztec diamond

## Finding

Let \(G\) be the cell-adjacency graph of the order-three Aztec diamond: its vertices are the 24 unit-square cells with centers \((i+1/2,j+1/2)\) satisfying \(|i+1/2|+|j+1/2|\leq3\); its edges join cells sharing a side. Thus \(|E(G)|=36\). Let \(\mathcal M\) denote the 64 perfect matchings (domino tilings). Define counting convolution on \(\mathbb F_2^{E(G)}\) by the measure \(\mu=\sum_{M\in\mathcal M}\delta_{\mathbf1_M}\). For each edge set \(S\), the unnormalized Walsh multiplier is

\[
\Lambda(S)=\sum_{M\in\mathcal M}(-1)^{|M\cap S|}.
\]

**Theorem.** The signed eigenvalues of this convolution have the following exact multiplicities on the entire \(2^{36}\)-element character group:

| Eigenvalue | Multiplicity | Eigenvalue | Multiplicity |
|---:|---:|---:|---:|
| \(0\) | 40,105,934,848 | | |
| \(\pm8\) | 10,636,754,944 each | \(\pm16\) | 2,713,714,688 each |
| \(\pm24\) | 570,425,344 each | \(\pm32\) | 276,824,064 each |
| \(\pm40\) | 67,108,864 each | \(\pm48\) | 37,748,736 each |
| \(\pm64\) | 4,194,304 each | | |

Consequently the convolution range \(W\) has Fourier rank \(28{,}613{,}541{,}888\) and nullity \(40{,}105{,}934{,}848\). The smallest nonzero absolute multiplier is \(8\), the largest is \(64\), and the sharp unnormalized Hilbert-space condition number on \(W\) is \(8\).

For **all** real or complex linear projections \(Q\) onto \(W\), including those not commuting with translations, the sharp norms are

\[
\min_{Q^2=Q,\operatorname{ran}Q=W}\|Q\|_{\ell^1\to\ell^1}
=\min_{Q^2=Q,\operatorname{ran}Q=W}\|Q\|_{\ell^\infty\to\ell^\infty}
=\boxed{\frac{82305}{4096}}.
\]

Exactly eight individual edge positions yield a vanishing Walsh multiplier when their sign alone is negated; they are the eight edges of the four outermost two-choice corner pairs.

## Assumptions and scope

All sums and multiplicities are for **independent signs on all 36 possible domino positions**. The group, matching indicator and unnormalized Fourier convention above are fixed; convolution acts on functions on \(\mathbb F_2^{36}\). The matrix dimensions and the statement are finite and exact, with no asymptotic or arbitrary-order claim. The eight corner positions are understood through the coordinate realization above, not through a choice of spanning tree.

## Proof

**1. Exact perfect matching ensemble.** Order the 24 cell centers lexicographically. Join each cell to existing east and north neighbors to list the 36 edges. Recursively pick the least currently unmatched vertex and pair it with each currently unmatched neighbor. Every perfect matching is generated exactly once. The recursion gives 64 distinct matchings of size 12, agreeing with the classical Aztec-diamond enumeration.

**2. Complete reduction of edge signings.** A vertex switch multiplies the signs of all edges incident to that vertex by \(-1\). Each perfect matching uses exactly one incident edge at every vertex; hence the switch multiplies *every* term in its signed sum by the same sign, independent of the matching. For a connected graph, switchings form a \(2^{23}\)-element group on edge signs. Choose the deterministic lexicographic spanning tree and switch so that its 23 edge signs are positive. The remaining 13 chord signs are independent, giving exactly \(2^{13}=8192\) gauge classes. Each gauge class contains \(2^{23}\) signings. Half of these have the opposite multiplier sign (switch one vertex), and all have equal multiplier magnitude.

**3. Independent signed determinant identity.** Two-color the 24 cells by coordinate parity. Form the 12-by-12 bipartite adjacency matrix, assigning fixed sign \((-1)^i\) to a vertical edge in column \(i\) and \(+1\) to every horizontal edge, then multiply by the chosen independent chord signs. Each bounded square face has negative edge-sign product. For any alternating cycle of length \(2k\), the ratio of permutation signs in its two matching contributions is \((-1)^{k-1}\); by the face-sign rule and the even number of vertices strictly inside such a matching cycle, the product of fixed edge signs has the same ratio. Thus all determinant terms have the same signed matching coefficient. At all-positive chord signs the determinant is \(64\), so the determinant is exactly \(\Lambda\) for every chord signing, not just equal in absolute value.

**4. Exhaustive integer spectral certificate.** In the attached `verify.py`, each of the 8192 normalized chord signings is evaluated twice: by explicit summation of the 64 matching monomials and by an independently constructed integer Kasteleyn determinant computed with exact fraction-free elimination. All 8192 results agree. The *normalized* signed counts, prior to vertex-switch sign symmetrization, are:

| Multiplier | Count | Multiplier | Count |
|---:|---:|---:|---:|
| \(-48\) | 3 | \(8\) | 1,486 |
| \(-40\) | 8 | \(16\) | 427 |
| \(-32\) | 28 | \(24\) | 86 |
| \(-24\) | 50 | \(32\) | 38 |
| \(-16\) | 220 | \(40\) | 8 |
| \(-8\) | 1,050 | \(48\) | 6 |
| \(0\) | 4,781 | \(64\) | 1 |

The entries sum to 8192 and their squared-multiplier sum is \(8192\cdot64\), the exact Parseval check. Symmetrizing each nonzero multiplier across the \(2^{23}\) vertex-switch signings gives the claimed *full* signed spectrum. In particular, 3411 reduced classes survive, giving rank \(3411\cdot2^{23}\). The smallest nonzero magnitude is 8, which is attained.

**5. Exact sharp endpoint projection.** Let \(h\) be the indicator of the 3411 nonvanishing normalized frequencies. Compute its unnormalized 13-dimensional Walsh transform \(H\). Exact integer inversion gives

\[
\sum_{a\in\mathbb F_2^{13}}|H(a)|=164610,\qquad
H(0)=3411.
\]

The Fourier multiplier of the canonical translation-invariant projection onto \(W\) is the indicator of the nonzero spectrum. Its kernel is the inverse Walsh transform of this indicator, supported on the annihilator of the vertex-switch cut space; its endpoint norm is therefore \(164610/8192=82305/4096\). Any other projection onto \(W\) can be averaged over all translations without increasing either endpoint norm. The average remains a projection onto \(W\), while a translation-invariant projection onto this Fourier-defined range is unique. Hence the displayed constant is the global minimum, over all real or complex projections.

## Verification

Run `python3 verify.py` using only the standard Python library. The program constructs the exact graph from cell coordinates; enumerates all 64 perfect matchings; proves completeness by the least-unmatched-vertex recursion; constructs a spanning tree; evaluates every normalized Fourier signing by both matching sums and integer Kasteleyn determinants; checks the complete signed spectrum, rank and smallest gap; evaluates the inverse Walsh projection kernel in exact integers; checks Fourier inversion and Parseval; and checks all 36 one-edge frequencies. Its final line is `PASS`. These are exhaustive integer certificates for the finite claimed domain, not extrapolations from small samples.

## Relationship to prior work

Elkies–Kuperberg–Larsen–Propp's original Aztec-diamond theorem gives the tiling count and generating functions for orientation and rank, but not the 36-edge independent-sign Walsh spectrum. Classical Kasteleyn determinant theory supplies the signed perfect-matching method used here; the determinant identity alone does not provide the 8192-class magnitude distribution or the evaluated range-projection norm. Chhita–Young analyze particular one-periodic, height-weighted and two-periodic edge families, not the complete independently signed space. Barkley–Liu's channel analysis provides a two-adic divisor for Aztec-diamond matching counts. A later exact-divisibility result for independent Aztec edge signings establishes the all-order greatest common divisor \(2^n\) but explicitly does not give the full spectrum, the zero-frequency count or the endpoint projection norm. In particular, that divisibility result does not imply the rank or the exact norm found here.

## Limitations

The theorem concerns only order three. The finite exact certificate does not classify all orders or establish any asymptotic in diamond size. The endpoint norm refers to projections onto the Fourier-recoverable space, not to the inverse convolution operator. General signed determinant formulas encode the raw problem algorithmically; a previously published, unindexed evaluation of the same order-three distribution remains a historical-priority risk. The verification and review are not independent external mathematical validation.

## References

1. N. Elkies, G. Kuperberg, M. Larsen, and J. Propp, *Alternating Sign Matrices and Domino Tilings* (first public arXiv posting 1991-06-01), https://arxiv.org/abs/math/9201305.
2. S. Chhita and B. Young, *Coupling Functions for Domino Tilings of Aztec Diamonds* (2013), https://arxiv.org/abs/1302.0615.
3. G. T. Barkley and R. I. Liu, *Channels, Billiards, and Perfect Matching 2-Divisibility* (first posted 2019-11-19), https://arxiv.org/abs/1911.08102.
4. *Sharp Walsh Divisibility for Aztec-Diamond Domino Tilings* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-walsh-divisibility-for-aztec-diamond-domino-tilings--c4f40564fd16.
