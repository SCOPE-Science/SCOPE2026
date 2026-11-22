# Complete ternary Fourier spectrum of the proper colourings of \(K_{2,n}\)

## Finding
Let \(n\ge1\), let \(G_n=(\mathbb Z/3\mathbb Z)^{n+2}\), and let \(P_n\subset G_n\) consist of all proper three-colourings of \(K_{2,n}\), whose first two vertices are the two-vertex part. Write \(f_n=\mathbf1_{P_n}\) and use the unnormalized additive Fourier transform
\[
W_n(\alpha,\gamma,\beta_1,\ldots,\beta_n)
=\sum_{x\in P_n}\exp\left(\frac{2\pi i}{3}(\alpha x_0+\gamma x_1+\sum_{j=1}^n\beta_jx_{j+1})\right).
\]
Set \(S=\sum_j\beta_j\pmod3\), let \(z=|\{j:\beta_j=0\}|\), and put \(m=n-z\). Then **every** Fourier coefficient is given by
\[
\boxed{W_n(b)=
\begin{cases}
0,&\alpha+\gamma+S\not\equiv0\pmod3,\\
3\big((-1)^m2^z-1+3\mathbf1_{\alpha=\gamma=S}\big),&\alpha+\gamma+S\equiv0\pmod3.
\end{cases}}
\]
Its complete signed eigenvalue multiplicity list, with coincident values combined, is: for each \(0\le z\le n\),
\[
\begin{aligned}
A_z&=3\big((-1)^{n-z}2^z-1\big),&\quad \operatorname{mult}(A_z)&\mathrel{+}=2\binom nz2^{n-z},\\
B_z&=3\big((-1)^{n-z}2^z+2\big),&\quad \operatorname{mult}(B_z)&\mathrel{+}=\binom nz2^{n-z},
\end{aligned}
\]
with an additional \(2\cdot3^{n+1}\) zero coefficients outside the balanced hyperplane. A \(\mathrel{+}=\) means to add this multiplicity when two displayed levels coincide, including zero.

For odd \(n\), all balanced coefficients are nonzero; for even \(n\), precisely \((n+4)2^{n-1}\) further balanced coefficients vanish. Thus
\[
\boxed{\operatorname{rank}(f_n*)=
\begin{cases}
3^{n+1},& n\text{ odd},\\
3^{n+1}-(n+4)2^{n-1},& n\text{ even}.
\end{cases}}
\]
The exact smallest positive Fourier magnitude is \(3\) for odd \(n\) and \(9\) for even \(n\). Consequently the unnormalized convolution operator \(C_n:h\mapsto f_n*h\) on counting-measure \(\ell^2(G_n)\) has
\[
\boxed{\|C_n^\dagger\|_{2\to2}=
\begin{cases}1/3,&n\text{ odd},\\1/9,&n\text{ even},\end{cases}}
\qquad
\boxed{\kappa_2^+(C_n)=
\begin{cases}2^n+2,&n\text{ odd},\\(2^n+2)/3,&n\text{ even}.\end{cases}}
\]
Here \(\dagger\) denotes the Moore–Penrose pseudoinverse and \(\kappa_2^+\) the ratio of greatest to least positive singular values. For odd \(n\), the range is exactly the subspace of functions invariant under simultaneous addition of one constant colour to every coordinate. For even \(n\), the range is strictly smaller.

## Assumptions and scope
Colours are the elements \(0,1,2\) of the additive cyclic group; proper means different colours on every edge. The two vertices in the first bipartition are **not adjacent**. Each of the other \(n\) vertices is adjacent to both. The dimension is \(n+2\), and the ambient group order is \(3^{n+2}\). The characters use the unnormalized transform stated above; changing the sign in the exponential conjugates all coefficients and does not affect the results. All formulae hold for every integer \(n\ge1\) without asymptotic hypotheses. No claim is made for four or more colours or for different graphs.

## Proof
Write the two first vertex colours as \(a,b\in\mathbb Z/3\mathbb Z\). For any leaf frequency \(\beta\), its colour contribution is \(\sum_{t\ne a,b}\exp(2\pi i\beta t/3)\). If \(a=b\), this is \(2\) for \(\beta=0\), and \(-\exp(2\pi i\beta a/3)\) otherwise, because a nontrivial character sums to zero over three colours. If \(a\ne b\), there is exactly one allowed leaf colour, namely \(-a-b\pmod3\), and its contribution is \(\exp(-2\pi i\beta(a+b)/3)\) for **every** \(\beta\), including zero.

Put \(T=\alpha+\gamma+S\pmod3\). The sum over the equal-pole case \(a=b\) is therefore \(3\mathbf1_{T=0}(-1)^m2^z\). The sum over unequal poles is
\[
\sum_{a\ne b}\exp\left(\frac{2\pi i}{3}\left[(\alpha-S)a+(\gamma-S)b\right]\right)
=9\mathbf1_{\alpha=\gamma=S}-3\mathbf1_{T=0}.
\]
The last identity is obtained by summing over all nine ordered pairs and subtracting the diagonal; its diagonal frequency is \(\alpha+\gamma-2S\equiv T\pmod3\). Since \(\alpha=\gamma=S\) automatically implies \(T=0\), combining the two cases proves the boxed all-frequency formula.

For each choice of the \(n\) leaf frequencies there are precisely three pole-frequency pairs with \(T=0\). Exactly one has \(\alpha=\gamma=S\); the remaining two do not. The number of leaf-frequency vectors with \(z\) zeros is \(\binom nz2^{n-z}\). This proves both full multiplicity formulae, including the other \(2\cdot3^{n+1}\) frequencies with \(T\ne0\).

To classify the additional zeros, first take the two unexceptional pole choices. The equation \((-1)^{n-z}2^z=1\) requires \(z=0\) and even \(n\), giving \(2^{n+1}\) zero frequencies. For the exceptional pole choice the equation \((-1)^{n-z}2^z=-2\) requires \(z=1\) and even \(n\), giving \(n2^{n-1}\) zeros. These two cases are disjoint, and neither occurs at odd \(n\). Subtraction from \(3^{n+1}\) gives the rank.

For odd \(n\), the exceptional value \(B_0=3\) gives the smallest possible nonzero magnitude, since every coefficient is a multiple of three. For even \(n\), the values \(B_0=9\) and \(A_1=-9\) occur; \(A_0=B_1=0\), and all other \(A_z,B_z\) have absolute value at least nine by inspecting the parity of \(z\) and the integer \(2^z\). This proves the exact gaps. At frequency zero, \(W_n(0)=|P_n|=3(2^n+2)\), which is the largest absolute eigenvalue by the triangle inequality. Fourier diagonalization of convolution proves the pseudoinverse and condition-number formulae. The range claim follows because the balanced Fourier characters are exactly those invariant under the diagonal colour-translation subgroup.

## Verification
Run `python3 verify.py` using Python 3 with no third-party packages. The script independently enumerates proper colourings and evaluates their character sums using exact integer counts of the three cubic-root phases. It compares all \(9{,}828\) frequency positions for \(1\le n\le6\) with the displayed multiplicity histograms; within the balanced hyperplane it directly verifies every multiplier. It additionally performs reproducible signed checks at lengths seven and eight, verifies predicted spectral multiplicities through length eighteen, and checks the rank and gap formulae. Its expected completion marker is `TERNARY_BICLIQUE_FOURIER_EXACT_PASS exhaustive_frequencies=9828 random_tests=320`. The computation is finite corroboration; the all-length proof is the preceding character-orthogonality argument.

## Relationship to prior work
Babson and Beck's 2012 paper on group-valued graph colourings uses Fourier methods to expand **unweighted graph-homomorphism counts**. The present result instead obtains every **vertex-coordinate additive Fourier coefficient** on a specified bipartite family, including its complete signed multiplicity histogram and exact spectral stability. Their abstract does not state such a classification; however the complete paper could not be compared and remains an explicit priority risk.

The previously available complete-bipartite result *Exact Fourier sampling spectra and a thin-side conditioning transition for bipartite colourings* (public research record `2026/11/1/SCOPE-exact-fourier-sampling-spectra-and-a-thin-side-conditioning-tran--2b34d08d2568`) was inspected in full in its `RESULT.md`. That theorem concerns the **degree-one restricted Gram matrix** of proper colourings for arbitrary palette size; its strict positivity does not determine the Fourier zeros or multiplicities at higher degrees. These distinct operators are not equivalent, and its finite-sampling condition number does not imply the present convolution pseudoinverse norm. Standard colouring enumerations recover \(|P_n|=3(2^n+2)\) but not the complete signed Fourier spectrum. A related ternary-cycle character classification concerns a different family of graphs and does not imply the biclique formula.

## Limitations
The historical comparison is bounded. The full 2012 Babson–Beck paper was unavailable for close reading, despite attempted open-access retrieval; it remains possible that an equivalent vertex-weighted formula or a stronger graph-colouring character theorem appears there or elsewhere. The result covers only ordinary three-colourings of \(K_{2,n}\), not all complete bipartite graphs or all palettes. The finite checker does not certify an infinite proof, and independent validation has not been performed. All spectral values use unnormalized counting-measure convolution; dividing by the support size would change the stated inverse norms.

## References
1. E. Babson and M. Beck, *Counting Group Valued Graph Colorings*, arXiv:1204.1283, first publicly posted 2012-04-05. https://arxiv.org/abs/1204.1283 .
2. *Exact Fourier sampling spectra and a thin-side conditioning transition for bipartite colourings*, public result and complete `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-fourier-sampling-spectra-and-a-thin-side-conditioning-tran--2b34d08d2568 .
3. M. Celaya, K. Choo, G. MacGillivray and K. Seyffarth, *Reconfiguring k-colourings of Complete Bipartite Graphs*, Kyungpook Mathematical Journal 56 (2016), 647–655, https://doi.org/10.5666/KMJ.2016.56.3.647 . The subject is colouring reconfiguration, not character-weighted enumeration.
