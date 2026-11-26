# Perron-optimal variation gauges and branching rigidity for heat flow on finite trees

## Finding

On an arbitrary finite tree, the best possible prefactor-one exponential control of edge total variation under **linear graph heat diffusion** is a Perron eigenvalue of a symmetric conductance-weighted line-graph matrix. A positive choice of variation weights makes heat diffusion contractive at every nonnegative time **if and only if the tree is a path or the three-leaf star**, regardless of the positive heat conductances. For paths, the optimal variation decay rate is exactly the first nonzero weighted Laplacian eigenvalue; for the claw, no strictly positive prefactor-one exponential rate is possible.

Specifically, with notation in the next section, the precise instantaneous logarithmic norm and the optimal exponent over all positive variation weights are
\[
\mu(c,w)=\max_{e\in E} c_e\left(\frac{(Aw)_e}{w_e}-2\right),
\qquad
s_*(c)=\lambda_{\max}\!\left(C^{1/2}(A-2I)C^{1/2}\right).
\]
The sharp all-time inequality for a fixed variation gauge is
\[
J_w(e^{-tL_c}f)\le e^{\mu(c,w)t}J_w(f)
\quad\text{for every real }f\text{ and }t\ge0.
\]
Every individual column candidate defining \(\mu(c,w)\) has an explicit tree-cut indicator witnessing its exact derivative at time zero.

## Assumptions and scope

Let \(T=(V,E)\) be a finite connected simple undirected tree with \(|V|\ge2\), and let \(m=|E|=|V|-1\). Give its edges any orientation, and let \(B\in\mathbb R^{m\times |V|}\) be the incidence matrix, with a row containing one \(+1\) and one \(-1\) at each edge. Fix arbitrary strictly positive heat conductances \(c_e\) and arbitrary strictly positive *independent* variation weights \(w_e\); set \(C=\operatorname{diag}(c_e)\). Define the positive semidefinite combinatorial conductivity Laplacian \(L_c=B^{\mathsf T}CB\), the heat flow \(H_t=e^{-tL_c}\), and the translation-invariant seminorm
\[
J_w(f)=\sum_{e\in E}w_e|(Bf)_e|.
\]
The line graph has one vertex for each original edge, with two adjacent when the original edges share an endpoint. Its (ordinary unweighted) symmetric adjacency matrix is \(A\). Write \(\|H_t\|_{J_w}\) for the induced operator norm on vertex functions modulo constants; this is well-defined because \(H_t\) fixes constants.

The *prefactor-one exponential exponent* of a given gauge means the infimum over \(r\in\mathbb R\) such that \(J_w(H_tf)\le e^{rt}J_w(f)\) for all \(f\) and every \(t\ge0\). It is not the logarithm of the norm at a single specified positive time. The independent conductivity and variation weights must not be conflated.

## Proof

**1. Exact edge generator.** Because \(T\) is a tree, \(B\) has full row rank, so every edge-gradient vector \(g\in\mathbb R^m\) equals \(Bf\) for some vertex signal \(f\). Differentiating \(g(t)=BH_tf\) gives
\[
\dot g(t)=Qg(t),\qquad Q=-BB^{\mathsf T}C.
\]
Every row of \(B\) has squared length \(2\). Distinct incidence rows have inner product \(0\) for disjoint edges and \(\pm1\) for edges meeting at a vertex. Thus
\[
Q_{ee}=-2c_e,\qquad |Q_{ef}|=A_{ef}c_f\quad(e\ne f).
\]
For a weighted \(\ell^1\) norm with strictly positive weights \(w_e\), the induced matrix logarithmic norm of \(Q\) is the maximum weighted column sum with the actual diagonal:
\[
\mu_{1,w}(Q)=\max_f\left(Q_{ff}+\frac1{w_f}\sum_{e\ne f}w_e|Q_{ef}|\right)
=\max_f c_f\left(\frac{(Aw)_f}{w_f}-2\right)=\mu(c,w).
\]
Indeed, expanding \(e^{hQ}=I+hQ+O(h^2)\) columnwise yields \(\lim_{h\downarrow0}(\|e^{hQ}\|_{1,w}-1)/h=\mu_{1,w}(Q)\). Submultiplicativity or Gronwall then gives \(\|e^{tQ}\|_{1,w}\le e^{\mu(c,w)t}\), hence the displayed inequality for every \(f\) and \(t\ge0\). Conversely, its first-order limit forbids any smaller prefactor-one exponent.

For sharpness, delete a selected edge \(f\), and take the indicator of either resulting component. Its edge gradient is \(\pm\mathbf e_f\); the weighted absolute derivative at time zero is exactly \(w_fc_f((Aw)_f/w_f-2)\). Choosing a maximizing edge realizes \(\mu(c,w)\). Thus there is strict small-time amplification whenever \(\mu(c,w)>0\).

**2. Optimal positive gauge.** Define the irreducible Metzler matrix \(M=C(A-2I)\) if \(m\ge2\), with an evident scalar interpretation when \(m=1\). The preceding formula is \(\mu(c,w)=\max_f (Mw)_f/w_f\). Adding a sufficiently large scalar multiple of the identity makes \(M\) nonnegative; the Perron–Frobenius/Collatz–Wielandt theorem gives
\[
\inf_{w>0}\mu(c,w)=s(M),
\]
where \(s(M)\) is the largest real-part eigenvalue. A strictly positive Perron eigenvector attains the infimum (and is unique up to scale for \(m\ge2\)). The matrix \(M\) is similar to the real symmetric matrix \(C^{1/2}(A-2I)C^{1/2}\). Therefore
\[
s(M)=\lambda_{\max}\left(C^{1/2}(A-2I)C^{1/2}\right)=s_*(c).
\]
Congruence by invertible \(C^{1/2}\) preserves inertia, so \(\operatorname{sign}(s_*(c))=\operatorname{sign}(\rho(A)-2)\), where \(\rho(A)\) is the spectral radius of the nonnegative line-graph adjacency matrix. In particular, the sign is independent of all positive conductances.

**3. Classifying trees.** If \(T\) is a path, its line graph is the path on \(m\) vertices. It has \(\rho(A)=2\cos(\pi/(m+1))<2\), including the one-edge case. If \(T=K_{1,3}\), its line graph is \(K_3\), with \(\rho(A)=2\). In every other nonpath tree, either some vertex has degree at least \(4\), or a degree-\(3\) vertex lies in a tree with more than four vertices. In the first case the line graph contains an induced \(K_4\), whose adjacency spectral radius is \(3\). In the second it contains a triangle with a pendant fourth vertex: the Rayleigh quotient at a vector equal to \(1\) on the triangle and to \(\varepsilon\) at that pendant vertex is \((6+2\varepsilon)/(3+\varepsilon^2)>2\) for \(0<\varepsilon<1\). Extending the vector by zero gives \(\rho(A)>2\). Hence \(s_*(c)\) is negative, zero, or positive exactly in the three stated classes.

For the claw, \(Aw\le2w\) holds with \(w>0\) only for equal coordinates: summing the three inequalities gives equality and forces each equality, and \(Aw=2w\) implies equal weights. For a path, the contraction region is explicitly the positive discrete-concave weight profiles \(2w_j\ge w_{j-1}+w_{j+1}\) with zero boundary conventions, independently of conductances.

**4. The path spectral-gap identity.** Orient path edges consistently in increasing vertex order. Then \(BB^{\mathsf T}\) has diagonal entries \(2\) and adjacent off-diagonal entries \(-1\). Thus \(Q=(A-2I)C\) itself, with positive off-diagonal entries; its top eigenvalue is \(-\lambda_2(L_c)\), because its eigenvalues are the negatives of the \(m\) positive eigenvalues of \(L_c\). Since \(Q\) is irreducible Metzler, the corresponding right edge eigenvector \(g>0\). Integrating \(g=Bf\) produces a Fiedler eigenvector \(f\) up to an additive constant, with all consecutive edge differences of one sign. The unique optimal positive variation weight vector, up to scale, is \(w=Cg\), since \(Q^{\mathsf T}Cg=CQg=-\lambda_2(L_c)Cg\). Therefore on a path the optimal prefactor-one decay exponent is precisely \(-\lambda_2(L_c)\). The proof also covers the one-edge path directly.

## Verification

The self-contained Python checker `verify.py` uses the actual incidence matrices to compute the edge generator independently of the line-graph formula; tests its small-time weighted-column derivatives against matrix exponentials; checks the all-time exponential envelope numerically; computes the optimal Perron gauge by symmetric eigenvalue calculation; and tests the path/claw/other sign trichotomy. It also tests the generator column identities with exact rational arithmetic and independently compares the optimal path exponent with the second vertex-Laplacian eigenvalue.

An execution on Python with NumPy and SciPy returned: `PASS: 1890 weighted-tree Perron/log-norm cases (424 path, 50 claw, 1416 other); 4400 rational column-derivative checks; 23 weighted-path spectral-gap cross-checks.` These finite checks test the implementation and examples; the unrestricted conclusions follow from the preceding proof, not enumeration.

## Relationship to prior work

The Li–Yau graph-gradient work of Bauer, Horn, Lin, Lippner, Mangoubi and Yau (first public 2013-06-11; arXiv:1306.2561v1) gives pointwise positive-solution gradient estimates with curvature assumptions, not the exact signed-signal weighted-\(\ell^1\) edge seminorm of an arbitrary finite tree. Lin, Liu and Yang (first public 2015-09-26; arXiv:1509.07981v1) likewise obtain positive-solution gradient/Harnack inequalities using a quadratic local gradient form, not a universal total-variation contraction classification. Kolmogorov, Pock and Rolínek (first public 2015-02-26; arXiv:1502.07770v1) study static tree-TV minimization and algorithms, rather than the ordinary linear heat semigroup or its optimal positive gauge.

The proof uses standard matrix logarithmic norms, the Collatz–Wielandt principle, and elementary tree/line-graph spectra; those ingredients are not claimed as new. What is claimed is their specific sharp combination for independently weighted tree heat conductances and edge variation, including the absolute tree classification and exact path spectral-gap optimization. A general spectral or matrix-measure theorem would recover individual steps only after the nontrivial edge-gradient reduction and line-graph classification, and should not be mistaken for a preexisting statement of these tree consequences.

## Limitations

The result is for **finite simple trees**, **strictly positive** heat conductances, real-valued signals, the standard counting-measure heat equation, and weighted absolute edge gradients. It does not cover cyclic graphs (whose gradient vectors satisfy circulation constraints), directed heat flows, nonlinear total-variation flows, vertex-mass-normalized diffusion, or the exact norm at a fixed positive time. The Perron exponent is the best *uniform prefactor-one* exponential exponent, not necessarily the large-time asymptotic decay rate of each signal. No claim of independent validation or exhaustive literature coverage is made.

## References

1. F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi, S.-T. Yau, *Li-Yau inequality on graphs*, arXiv:1306.2561v1, first posted 2013-06-11. https://arxiv.org/abs/1306.2561
2. V. Kolmogorov, T. Pock, M. Rolínek, *Total variation on a tree*, arXiv:1502.07770v1, first posted 2015-02-26. https://arxiv.org/abs/1502.07770
3. Y. Lin, S. Liu, Y. Yang, *A gradient estimate for positive functions on graphs*, arXiv:1509.07981v1, first posted 2015-09-26. https://arxiv.org/abs/1509.07981
4. R. A. Horn, C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2012, for standard matrix/spectral theory.
