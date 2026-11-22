# Sharp four-vertex positivity frontier for a symmetrically filtered heat step

## Finding

Let \(L_G\) be the unweighted Laplacian of a finite undirected graph and consider the first-order two-sided resolvent filtered Euler update for heat flow \(u'=-L_Gu\), with physical and splitting operators both equal to \(L_G\):
\[
T_1(h)=I-hL_G(I+\tfrac h2L_G)^{-2},\qquad h\ge0.
\]
For every graph and every \(h\ge0\), \(T_1(h)\) is symmetric, preserves the all-ones vector, and has every eigenvalue in \([1/2,1]\). Nonetheless, entrywise positivity can fail.

**Sharp minimal witness and interval.** Every undirected simple unweighted graph on at most three vertices has entrywise nonnegative \(T_1(h)\) for every \(h\ge0\). For the four-vertex path \(P_4\), numbered consecutively \(1,2,3,4\), the step is entrywise nonnegative exactly when \(0\le h\le h_*\), where \(h_*\) is the unique positive root of
\[
h^3-6h^2-10h-4=0,\qquad h_*=7.42030108523868\ldots.
\]
For \(h>h_*\), the only negative entries are \((1,2),(2,1),(3,4),(4,3)\). Thus four vertices are the minimal possible graph order of a positivity failure for this method, even though the matrix remains strictly positive definite, conservative and norm-contracting at every step.

**Graph-theoretic mechanism and higher filters.** On any fixed connected undirected weighted graph with Laplacian \(L\), integer filter order \(p\ge1\), and positive splitting multiple \(c\), put
\[
J_{p,c}(h)=(I+\tfrac{hc}{2}L)^{-1},\quad R_{p,c}(h)=I-(I-J_{p,c}(h))^p,\quad T_{p,c}(h)=I-hL R_{p,c}(h)^2.
\]
Then, in matrix norm,
\[
T_{p,c}(h)=I-\frac{4p^2}{c^2h}L^++O(h^{-2})\quad(h\to\infty),
\]
where \(L^+\) denotes the Moore–Penrose pseudoinverse. Consequently, any positive off-diagonal entry \((L^+)_{ij}>0\) forces \((T_{p,c}(h))_{ij}<0\) for all sufficiently large \(h\). In particular, on every unweighted path \(P_n\) with \(n\ge4\), the endpoint-adjacent entry is eventually negative for every fixed finite \(p\) and every fixed \(c>0\), because
\[
(L_{P_n}^+)_{12}=\frac{(n-1)(2n-7)}{6n}>0.
\]
This remains true for uniformly energy-contractive, nonnegative-spectrum choices \(c\ge4C_p\), where \(C_p=\max_{x\ge0}x[1-(x/(1+x))^p]^2\): for those choices every eigenvalue of \(T_{p,c}(h)\) belongs to \([1/2,1]\) at every \(h\ge0\).

## Assumptions and scope

Graphs are finite, undirected, connected when using the pseudoinverse asymptotic, and have positive symmetric conductances; \(P_n\) and the minimality statement concern unit conductances and simple graphs. The physical model is the linear heat equation on the graph, with generator \(-L\), so the exact solution \(e^{-hL}\) is entrywise nonnegative and preserves total mass. The scheme is the completed filtered forward-Euler branch of Wu and Shu, specialized to a constant linear diffusion operator, not an arbitrary IMEX method. The sharp four-node claim fixes the natural matching choice \(c=p=1\). The generalized large-step statement fixes \(p,c,G\) before sending \(h\) to infinity. It concerns only completed steps, not positivity of intermediate filtered states or floating-point rounding.

## Proof

**1. Exact filter and spectral stability.** The first-order filter in the source is \(J=(I+hS/2)^{-1}\), and its residual is \(-J\mathcal A Ju\). With \(S=\mathcal A=L\), the completed update is the stated \(T_1\). For each eigenvalue \(\lambda\ge0\) of \(L\), the amplification is
\[
f(h\lambda)=1-\frac{h\lambda}{(1+h\lambda/2)^2}
=\frac{1+(h\lambda/2)^2}{(1+h\lambda/2)^2}.
\]
Writing \(x=h\lambda/2\), the inequality \(0\le2x/(1+x)^2\le1/2\) proves \(1/2\le f\le1\). Since \(L\mathbf1=0\), \(T_1\mathbf1=\mathbf1\). Symmetry, strict positive definiteness, and \(\ell^2\) contraction follow from spectral calculus.

**2. No graph of order at most three can fail.** The only connected simple graphs up to three vertices are a singleton, \(K_2\), \(P_3\), and \(K_3\). Disconnected graphs give direct sums of these smaller updates. Direct rational inversion on \(K_2\) gives the single off-diagonal value \(h/(1+h)^2>0\) for \(h>0\); on \(K_3\), each off-diagonal equals \(h/(1+3h/2)^2>0\). On \(P_3\), the two adjacent off-diagonals are \(4h/(3h+2)^2>0\), and the endpoint-to-endpoint entry is
\[
\frac{16h^2(h+1)}{(h+2)^2(3h+2)^2}>0.
\]
All diagonals are positive by Step 1. At \(h=0\), the updates are the identity.

**3. Four-vertex rational certificate.** For the path \(P_4\), define the positive denominator
\[
D(h)=2(h+1)^2(h^2+4h+2)^2.
\]
Exact matrix inversion gives the four classes of off-diagonal entries (the other positions follow by symmetry and path reflection):
\[
\begin{aligned}
(T_1)_{12}=(T_1)_{34}&=-\frac{h(h+2)(h^3-6h^2-10h-4)}{D(h)},\\
(T_1)_{13}=(T_1)_{24}&=\frac{h^2(3h^3+12h^2+18h+8)}{D(h)},\\
(T_1)_{14}&=\frac{h^3(5h^2+12h+6)}{D(h)},\\
(T_1)_{23}&=\frac{h(h+2)(h^3+2h^2+6h+4)}{D(h)}.
\end{aligned}
\]
The last three classes are positive for every \(h>0\). The polynomial \(g(h)=h^3-6h^2-10h-4\) has exactly one positive root by Descartes' rule of signs; its value is negative at zero and tends to infinity. Therefore the first class is nonnegative exactly for \(0\le h\le h_*\). All diagonal entries are positive by Step 1, proving the exact interval and the claimed uniqueness of the negative positions.

**4. General-order large-step mechanism.** On the positive spectral subspace of connected \(L\), let \(x=hc\lambda/2\). For each fixed \(p\), the binomial expansion at infinity yields
\[
r_p(x)=1-\bigl(x/(1+x)\bigr)^p=\frac{p}{x}+O(x^{-2})
=\frac{2p}{hc\lambda}+O(h^{-2}).
\]
Thus \(h\lambda r_p(x)^2=4p^2/(c^2h\lambda)+O(h^{-2})\). On the constant subspace both \(L\) and the subtractive term vanish. Finite-dimensional spectral calculus proves the stated matrix expansion with \(L^+\). A strictly positive off-diagonal entry of \(L^+\) makes the corresponding entry of \(T_{p,c}\) strictly negative for all sufficiently large finite steps.

**5. Path pseudoinverse sign.** For a connected graph, effective resistances obey \(R_{ij}=(L^+)_{ii}+(L^+)_{jj}-2(L^+)_{ij}\). With \(H=I-\mathbf1\mathbf1^\mathsf T/n\), double centering gives \(L^+=-HRH/2\). On the unit path the unique-flow formula yields \(R_{ij}=|i-j|\). Therefore
\[
(L^+)_{12}=\frac1{2n}\sum_k(|1-k|+|2-k|)-\frac12-\frac1{2n^2}\sum_{i,j}|i-j|.
\]
The sums are \(n(n-1)/2\), \(1+(n-2)(n-1)/2\), and \(n(n^2-1)/3\), respectively, giving \((n-1)(2n-7)/(6n)\). It is strictly positive exactly when the integer \(n\ge4\).

Finally, the scalar spectral multiplier of \(T_{p,c}\) is \(1-(2/c)x r_p(x)^2\). If \(c\ge4C_p\), it lies in \([1/2,1]\) for every \(x\ge0\). Hence the large-step entrywise negativity persists despite a strictly nonnegative spectrum and unconditional \(\ell^2\) contraction. This proves all parts.

## Verification

The standalone `artifacts/verify.py` is executed using Python 3 and SymPy with `python artifacts/verify.py`; it prints `VERIFY_OK` on success. It recomputes the path and triangle matrix updates independently from exact resolvent inversions; checks the displayed rational identities and their \(h=7,8\) signs; verifies conservation for rational steps and the path pseudoinverse formula through nine vertices; and checks the arbitrary filter-order asymptotic scalar constant symbolically for orders one through eight. These are finite diagnostics supporting the proof, not a substitute for the all-order analytic argument. A rational witness is
\[
(T_1(8))_{12}=-\frac{440}{194481}<0.
\]

## Relationship to prior work

Wu and Shu introduce the two-sided symmetric filter and prove unconditional \(L^2\) stability under operator comparison, including the first-order scheme analyzed here. Their spectral bound is used with attribution; they do not provide the presented componentwise graph positivity classification. Fontan and Altafini previously explain why Laplacian pseudoinverses can have positive off-diagonal entries, and earlier graph inverse work likewise supplies the underlying sign phenomenon: that generic fact is not claimed as new. A published exact classification of weighted-path positivity for the fourth-order two-stage Gauss method uses a different rational scalar multiplier \((z^2-6z+12)/(z^2+6z+12)\) and does not imply the present filtered-Euler cubic boundary. A published criterion for all-step positivity on complete multipartite graphs covers a different graph class; the four-node path is not complete multipartite. The new assertion is the exact first-order filtered-Euler path threshold, its minimal witness dimension, and its explicit connection to finite-order filter stiff limits.

## Limitations

The exact finite-step cutoff is proved only for the unweighted four-vertex path and the matched first-order filter. For larger paths and general finite filter orders, only eventual positivity failure (not a complete finite-step sign classification) is proved. The implication using \(L^+\) is a sufficient obstruction, not a claimed necessary-and-sufficient criterion for arbitrary graphs. Spectral contractivity is not a guarantee of accuracy for stiff steps, and the result does not address nonlinear coefficients, positivity limiters, higher-order SSP compositions, or floating-point perturbations. Historical priority is subject to unindexed or inaccessible equivalent work; no independent specialist validation is claimed.

## References

1. Y. Wu and C.-W. Shu, *Unconditionally \(L^2\)-stable explicit–implicit–null filtered Runge–Kutta methods for general nonlinear degenerate parabolic equations*, arXiv:2611.02282v1, publicly listed November 3, 2026, https://arxiv.org/abs/2611.02282.
2. A. Fontan and C. Altafini, *On the properties of Laplacian pseudoinverses*, arXiv:2109.14587v1, 2021, https://arxiv.org/abs/2109.14587.
3. *Unconditional fourth-order Gauss positivity on weighted paths: a four-vertex cutoff*, publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unconditional-fourth-order-gauss-positivity-on-weighted-paths-a--73910250a06c.
4. *A scalar criterion for unconditionally positive rational graph-heat steps on complete multipartite networks*, publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-scalar-criterion-for-unconditionally-positive-rational-graph-h--335027f86795.
