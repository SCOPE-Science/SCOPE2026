# All-temperature strict boundary bias in disordered single-wall Ising chains

## Finding
For independent symmetric, strictly log-concave bond-energy increments, the disorder-averaged *single-wall Gibbs* probability decreases **strictly at every step from either boundary toward the center**, at every finite positive inverse temperature. Precisely, if \(N\ge3\) and the independent identically distributed increments \(Z_1,\ldots,Z_{N-1}\) have an everywhere-positive, even, strictly log-concave density, put \(S_0=0\), \(S_j=\sum_{k=1}^j Z_k\), \(p_j=e^{S_j}/\sum_{k=0}^{N-1}e^{S_k}\), and \(q_j=\mathbb E p_j\). Then
\[
q_j=q_{N-1-j},\qquad q_j>q_{j+1}\quad\text{for }0\le j<(N-2)/2.
\]
For even \(N\), the two central weights coincide; for odd \(N\), the unique central weight is minimal. For \(N=2\) the two weights both equal \(1/2\). The high-temperature uniform limit is an equality only at zero coupling to the disorder; no positive-temperature parameter tuning reverses the spatial order.

## Assumptions and scope
The probability density \(f\) of the increments is strictly positive and even on \(\mathbb R\), with strictly concave \(\log f\); increments are independent and identically distributed. A centered Gaussian with positive variance is included. Neither a Gaussian tail nor a moment hypothesis is needed. The Ising application considers a ferromagnetic chain with antiparallel pinned spins and restricts the classical thermal ensemble to its configurations having exactly one domain wall. If the wall location is indexed from \(0\) to \(N-1\), and independent local longitudinal fields \(\zeta_k\) are centered Gaussian, the known energy-difference law gives \(E_j-E_{j-1}=2\zeta_j\). The Gibbs position weights therefore equal the displayed random-walk softmax with \(Z_j=-2\beta\zeta_j\). The claim concerns annealing over field disorder *after* normalizing the Gibbs law in each field realization. It is not the full finite-temperature Ising measure with multiple domain walls and is not a quantum dynamical statement.

## Proof
Write \(Y_k=e^{Z_k}\). Define exponential random-walk sums
\[
A_0=0,\qquad A_n=\sum_{h=1}^n\prod_{k=1}^hY_k\quad(n\ge1),\qquad B_n=1+A_n.
\]
Their laws obey \(A_{n+1}\stackrel d=Y(1+A_n')\), with \(Y=e^Z\) and \(A_n'\) an independent copy of \(A_n\). Let \(L_n=\log A_n\) for \(n\ge1\), and let \(g(x)=\log(1+e^x)\). Thus \(L_1\stackrel d=Z\) and \(L_{n+1}\stackrel d=Z+g(L_n')\).

We first prove a strict monotone-likelihood-ratio ordering: for every \(n\ge1\), the density of \(L_{n+1}\) divided by the density of \(L_n\) is strictly increasing. For any shift \(u>0\), strict log-concavity implies \(f(x-u)/f(x)\) is strictly increasing in \(x\). Since \(g(Z')>0\) almost surely, \(L_2=Z+g(Z')\) has density \(\int f(x-u)\,d\mu(u)\), and the density ratio relative to \(L_1=Z\) is strictly increasing. If \(L_{n+1}\) is larger than \(L_n\) in likelihood-ratio order, then their increasing images under \(g\) retain this order. Moreover convolution with an independent \(Z\) retains it, because the kernel \(K(x,u)=f(x-u)\) is strictly totally positive of order two: for \(x_1<x_2\) and \(u_1<u_2\),
\[
f(x_1-u_1)f(x_2-u_2)>f(x_1-u_2)f(x_2-u_1).
\]
Indeed this is the decreasing-secant-slope property of strictly concave \(\log f\). Integrating the positive two-by-two determinant against the ordered input-density determinant proves the new output-density determinant is positive. Induction establishes strict likelihood-ratio order for every successive pair, and hence for any \(L_a,L_b\) with \(b>a\ge1\). Increasing \(g\) again shows \(B_b=1+A_b\) strictly larger in likelihood-ratio order than \(B_a\). For \(a=0\), \(B_0=1\) and \(B_b>1\) almost surely, treated separately.

Fix adjacent wall sites \(i,i+1\). Write \(W_j=e^{S_j}\) and isolate \(Y=W_{i+1}/W_i=e^{Z_{i+1}}\). Define the independent left and right branch ratios
\[
U=\sum_{j=0}^{i}\frac{W_j}{W_i},\qquad V=\sum_{j=i+1}^{N-1}\frac{W_j}{W_{i+1}}.
\]
Symmetry of the increment distribution, and reversal of the corresponding product lists, give \(U\stackrel d=B_i\) and \(V\stackrel d=B_{N-i-2}\). The variables \(U,V,Y\) are mutually independent. Because the total partition sum is \(W_i(U+YV)\),
\[
q_i-q_{i+1}=\mathbb E\frac{1-Y}{U+YV}.
\]
The equality in law \(Y\stackrel d=1/Y\) then gives the **exact antisymmetric representation**
\[
q_i-q_{i+1}=\frac12\mathbb E\left[
\frac{(Y-1)^2(V-U)}{(U+YV)(YU+V)}\right].
\]
If \(i=(N-2)/2\), the independent variables \(U,V\) have the same distribution, and antisymmetry forces equality. If \(i<(N-2)/2\), the branch length \(N-i-2\) exceeds \(i\). For \(i=0\), \(U=1<V\) almost surely, making the expectation strictly positive. Otherwise the proven strict likelihood-ratio order says the density ratio \(d\mathcal L(V)/d\mathcal L(U)\) strictly increases. Pairing points \((u,v)\) and \((v,u)\) with \(u<v\), their joint density difference has the sign of \(f_U(u)f_V(v)-f_U(v)f_V(u)>0\); the antisymmetric kernel has the same positive sign. Since \(\Pr(Y\ne1)=1\), the expectation is strictly positive. Finally, reversing \(S_0,\ldots,S_{N-1}\) and subtracting the terminal value turns the steps into reversed negated increments, which have the same joint law. Hence \(q_i=q_{N-1-i}\), finishing the proof for all \(N\).

## Verification
The proof is analytical and applies simultaneously to all finite lengths and temperatures; numerical integration cannot replace it. The included `check_profile.py` applies deterministic Gaussian Gauss–Hermite product quadrature to \(N=3,4,5,6\) at three positive increment scales, verifying normalization, reflection symmetry and all strict adjacent comparisons in 36 consistency assertions. Run `python check_profile.py` with Python, NumPy installed. The exact antisymmetrized identity is established algebraically in the proof; no numerical or experimental certificate is required for the infinite quantifiers.

## Relationship to prior work
Chowdhury, Hopkins, Chancellor and Kendon (arXiv:2610.40504v1, first publicly released October 29, 2026), §II.B–C, equations (5)–(8), derive the random-walk-energy Gibbs law and show U-shaped disorder averages numerically, while discussing the zero-temperature arcsine limit. Chancellor et al. (arXiv:2006.07685; npj Quantum Information 8, 73, 2022) established the physical entropic-bias phenomenon and its high-temperature quadratic expansion. Accordingly **the U shape itself is not claimed to be new**. The asserted extension is the rigorous *strict nearest-neighbor ordering, without restriction on positive temperature or size, for an entire class of symmetric strictly log-concave disorder distributions*. It does not follow from either a quadratic small-inverse-temperature expansion or the zero-temperature arcsine limit. The likelihood-ratio convolution principle used in the proof is standard (Shanthikumar and Yao, 1986), not asserted as new.

## Limitations
The statement is restricted to exactly one classical wall and iid symmetric strictly log-concave fields. Neither correlated fields nor heavy-tailed non-log-concave field laws are covered. The disorder strength must be nonzero; at zero noise or exactly zero inverse temperature the annealed law is uniform. This result establishes strict order, not a closed formula for the gaps or the amount of bias, and does not address quantum interference, dynamical freeze-out, or excited multi-wall sectors. Priority risk remains from implicit older proofs of the same all-temperature inequality in the 2022 paper's supplementary material, which was not fully accessible at review, and from the general total-positivity literature.

## References
1. S. Chowdhury, A. Hopkins, N. Chancellor and V. Kendon, *Using domain walls to benchmark fast quantum anneals*, arXiv:2610.40504v1 (October 29, 2026), https://arxiv.org/abs/2610.40504.
2. N. Chancellor et al., *Error measurements for a quantum annealer using the one-dimensional Ising model with twisted boundaries*, npj Quantum Information **8**, 73 (2022), https://doi.org/10.1038/s41534-022-00580-w; preprint arXiv:2006.07685.
3. J. G. Shanthikumar and D. D. Yao, *The preservation of likelihood ratio ordering under convolution*, Stochastic Processes and their Applications **23**, 259–267 (1986), https://doi.org/10.1016/0304-4149(86)90039-6.
