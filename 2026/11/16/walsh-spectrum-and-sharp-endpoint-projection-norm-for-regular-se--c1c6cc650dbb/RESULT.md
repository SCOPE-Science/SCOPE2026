# Walsh spectrum and sharp endpoint projection norm for regular seven-vertex tournaments

## Finding
Let \(G=\mathbb F_2^{21}\), with coordinates indexed by the edges \(\{i,j\}\) of \(K_7\), for \(0\le i<j\le6\). An orientation is represented by \(x\in G\), where \(x_{ij}=1\) means \(i\to j\), and \(x_{ij}=0\) means \(j\to i\). Let \(R\subseteq G\) be the \(2640\) regular orientations, namely those with outdegree three at every vertex. Define unnormalized convolution by
\[
(C_R f)(x)=\sum_{r\in R} f(x+r),\qquad
W(\xi)=\sum_{r\in R}(-1)^{\sum_{i<j}\xi_{ij}r_{ij}}.
\]
**Theorem.** Exactly \(553984\) of the \(2^{21}=2097152\) Walsh multipliers \(W(\xi)\) are nonzero. Their possible absolute values and multiplicities, divided by \(64\), are the following complete quotient spectrum:

| \(|W|\) | Quotient frequency count |
|---:|---:|
| 0 | 24112 |
| 16 | 3780 |
| 32 | 420 |
| 48 | 1365 |
| 80 | 630 |
| 96 | 1260 |
| 112 | 360 |
| 176 | 630 |
| 240 | 105 |
| 528 | 105 |
| 2640 | 1 |

Thus the exact nullity is \(1543168\); the smallest nonzero multiplier magnitude is \(16\), the largest is \(2640\), and the recoverable-spectrum \(\ell^2\) condition number is \(165\). Moreover, among **every** linear projection onto \(\operatorname{ran}C_R\) in either \(\ell^1(G)\) or \(\ell^\infty(G)\), the smallest possible operator norm is exactly
\[
\boxed{\Lambda_1(\operatorname{ran}C_R)=\Lambda_\infty(\operatorname{ran}C_R)=\frac{11155}{256}.}
\]
It is attained by the canonical translation-invariant Fourier projection. With counting-convolution normalization as above, \(\lVert C_R^\dagger\rVert_{2\to2}=1/16\).

## Assumptions and scope
The group is the full ambient **binary** edge-orientation cube, not the permutation group, the group of tournament relabelings, or a continuous compact group. A Walsh frequency is an arbitrary binary edge labelling, not necessarily an orientation satisfying any degree condition. All Fourier transforms are **unnormalized**; the inverse transform divides by the size of the group. Norms on functions over \(G\) use the usual counting-measure \(\ell^p\) norms. The results concern the regular seven-vertex tournament set, not a universal formula for all odd tournament orders.

## Proof
**1. Exact affine quotient.** Let \(y=(x_{ij})_{1\le i<j\le6}\in\mathbb F_2^{15}\). At vertex \(j\ge1\), the outdegree modulo two is \(j+\sum_{i\ne j}x_{\min(i,j),\max(i,j)}\) (there are \(j\) reference orientations arriving from a lower vertex). Hence any regular orientation satisfies
\[
x_{0j}\equiv 3-j+\sum_{\substack{1\le i<k\le6\\j\in\{i,k\}}}y_{ik}\pmod2.
\]
These six equations are independent because their left sides involve distinct star edges. Conversely every \(y\in\mathbb F_2^{15}\) determines exactly one orientation with the requisite vertex-outdegree parities for vertices \(1,\dots,6\); the vertex-zero parity then follows by summing incidence parity equations. Let \(F(y)\) equal one exactly when the reconstructed orientation has all seven **integer** outdegrees equal to three. Thus \(\sum_y F(y)=2640\), and the regular orientations occupy a subset of an affine 15-dimensional subspace.

Writing \(\eta_{ij}=\xi_{ij}+\xi_{0i}+\xi_{0j}\pmod2\) for each inner edge, and \(b_j=3-j\pmod2\), substitution gives the **exact all-frequency formula**
\[
W(\xi)=(-1)^{\sum_{j=1}^{6} b_j\xi_{0j}}\,V(\eta),\qquad
V(\eta)=\sum_{y\in\mathbb F_2^{15}}F(y)(-1)^{\eta\cdot y}.
\]
The map \(\xi\mapsto\eta\) is surjective and every quotient frequency has precisely \(2^6=64\) lifts. Consequently all absolute full-group Walsh multiplicities are 64 times the quotient multiplicities.

**2. Exhaustive exact computation.** The accompanying standalone `check_regular7.py` loops through all \(32768\) inner-edge words, reconstructs each of the six star edges by the displayed parity equations, tests all seven exact outdegrees, and performs a 15-stage integer Walsh–Hadamard transform of the resulting Boolean array. Its complete list of coefficients is `walsh_quotient.csv`; the absolute histogram is exactly the table above. The separately implemented `check_regular7_independent.cpp` instead enumerates **all \(2097152\)** ambient orientations, independently recognizes all \(2640\) regular ones, and obtains every quotient coefficient from direct character sums over those 2640 words. It checks every one of the 32768 certificate coefficients. This exhausts the finite domain; it does not extrapolate from samples. In addition, Parseval gives the independent integer checksum
\[
\sum_{\eta}V(\eta)^2=2^{15}\cdot2640=86507520.
\]
The first nonzero magnitude in the exhaustive histogram is 16, and its largest magnitude, 2640, is attained at the trivial frequency.

**3. Endpoint range projection.** Let \(S=\{\eta:V(\eta)\ne0\}\) with \(|S|=8656\), and define its unnormalized Walsh transform
\[
H(z)=\sum_{\eta\in S}(-1)^{\eta\cdot z},\qquad z\in\mathbb F_2^{15}.
\]
The second complete integer certificate, `projection_kernel.csv`, evaluates \(H\) at all 32768 arguments. Its **absolute-value histogram** is

| \(|H|\) | Number of quotient elements |
|---:|---:|
| 0 | 5760 |
| 16 | 3360 |
| 32 | 6720 |
| 48 | 11760 |
| 64 | 1344 |
| 80 | 2730 |
| 208 | 560 |
| 240 | 420 |
| 496 | 112 |
| 8656 | 2 |

The exact absolute sum is \(\sum_z |H(z)|=1427840\), whence the convolution kernel of the canonical range projection has \(\ell^1\)-norm \(1427840/32768=11155/256\). Indeed the original full-group spectral support is the preimage of \(S\) under \(\xi\mapsto\eta\). The inverse Walsh transform of its indicator vanishes outside the underlying 15-dimensional linear orientation-difference subspace; on that subspace it equals \(2^{-15}H(z)\) after the natural parametrization. Hence its full-group \(\ell^1\) kernel norm equals the displayed quotient quantity.

Finally, let \(P\) be **any** bounded linear projection onto \(\operatorname{ran}C_R\). Averaging \(\tau_gP\tau_g^{-1}\) over every group translation \(\tau_g\) leaves a projection onto the same invariant range and cannot increase either endpoint norm. The average commutes with all translations, so is a Fourier multiplier. There is only one translation-invariant projection onto the specified Fourier range: its multiplier is one on the nonzero spectrum of \(C_R\) and zero elsewhere. Thus the displayed kernel norm is a universal lower bound, attained by that projection. The \(\ell^1\) and \(\ell^\infty\) norms of convolution by a real kernel both equal its absolute kernel sum, finishing the proof.

## Verification
Run `python3 check_regular7.py` from the directory containing the two CSV files to regenerate the complete 32768-point spectrum and projection kernel and compare **every** certificate entry. Alternatively use `python3 check_regular7.py --write` to reproduce them. An independent exact check uses `c++ -std=c++17 -O2 check_regular7_independent.cpp -o check7 && ./check7`, run from that same directory. The C++ checker enumerates every full ambient orientation and performs direct signed sums rather than using the parity-reconstruction enumeration and transform algorithm. Both programs print explicit pass markers upon success. The certificates and checkers are embedded in full, with their exact byte hashes in the enclosing manifest. The finite exhaustion is a proof of the order-seven numerical constants, while the quotient and projection-optimality arguments explain why they are the correct invariants for all ambient characters and unrestricted endpoint projections.

## Relationship to prior work
Kühn, Osthus and Treglown, *Hamilton decompositions of regular tournaments* (arXiv:0908.3411, first publicly submitted 2009-08-24), study Hamilton-cycle packing; they give the familiar regular tournament definition, but do not determine the signed edge-orientation Walsh spectrum or its endpoint range projection. Isaev, *Asymptotic behavior of the number of Eulerian orientations of graphs* (arXiv:1110.2598, first publicly submitted 2011-10-12), studies unsigned counts and graph asymptotics, explicitly treating regular tournaments as Eulerian orientations of complete graphs. A publicly accessible 2026 study titled *Integral tight Fourier sampling and tree-complement designs for regular tournaments* determines first-degree edge-coordinate covariance and maximal independent Walsh sampling; those statements do **not** give the complete frequency-space Fourier support of the regular-tournament indicator or the endpoint projection norm computed here. Yu and Zhu, *Counting degree-constrained orientations* (arXiv:2504.12693), give a general signed-subset duality for unsigned degree-constrained orientation counts; its identified claims do not include this order-seven Fourier support histogram or projection norm. The affine-quotient reduction, Walsh transform, and translation-averaging principle are standard tools and are not claimed as inventions.

## Limitations
The evaluated spectrum and norm are specific to seven vertices; there is no claim of a closed formula for all odd orders. The complete finite coefficients are supplied as exhaustive code-generated certificates, not a compact representation-theoretic closed form. General signed enumerators might provide alternative ways to derive individual coefficients, so historical priority for the **exact evaluated** support spectrum and projection constant is subject to bounded-literature-search uncertainty. Independent mathematical audit has not been performed.

## References
- D. Kühn, D. Osthus and A. Treglown, *Hamilton decompositions of regular tournaments*, arXiv:0908.3411, first submitted 2009-08-24. https://arxiv.org/abs/0908.3411
- M. Isaev, *Asymptotic behavior of the number of Eulerian orientations of graphs*, arXiv:1110.2598, first submitted 2011-10-12. https://arxiv.org/abs/1110.2598
- *Integral tight Fourier sampling and tree-complement designs for regular tournaments*, publicly available 2026-11-02: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-tight-fourier-sampling-and-tree-complement-designs-for--eaf6965e2c4a
- J. Yu and J.-X. Zhu, *Counting degree-constrained orientations*, arXiv:2504.12693, first submitted 2025-04-17. https://arxiv.org/abs/2504.12693
