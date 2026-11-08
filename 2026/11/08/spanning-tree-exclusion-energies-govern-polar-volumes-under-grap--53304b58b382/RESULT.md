# Spanning-tree exclusion energies govern polar volumes under graph subdivision

## Finding
Fix any finite connected simple graph \(H=(V,E)\), with \(v=|V|\ge2\), \(e=|E|\) and cycle rank \(g=e-v+1\). Replace every edge by a path of \(m\ge1\) edges; denote the subdivision by \(H^{(m)}\). Let
\[
P_m=\operatorname{conv}\{\pm(\mathbf e_i-\mathbf e_j):ij\in E(H^{(m)})\}
\]
be the symmetric edge polytope in the Euclidean hyperplane \(\{x:\sum_i x_i=0\}\), and take the polar in that hyperplane:
\[
K_m=P_m^\circ=\{x:\sum_i x_i=0,\ |x_i-x_j|\le1\ \text{for every edge }ij\}.
\]
Its dimension is \(N_m-1\), where \(N_m=v+(m-1)e\). Define its rooted-coordinate volume by \(W_m=\sqrt{N_m}\operatorname{vol}_{N_m-1}^{\rm Euclidean}(K_m)\). Rooted-coordinate volume is independent of the root and differs from intrinsic Euclidean volume by exactly \(\sqrt{N_m}\).

Write \(\tau(H)\) for the number of spanning trees. For an edge \(f\in E(H)\), let \(r_f=\Pr[f\notin T]\), where \(T\) is a uniformly random spanning tree of \(H\). Then, for **every fixed** connected simple \(H\),
\[
\boxed{\displaystyle
W_m=\frac{2^{me}}{\sqrt{\tau(H^{(m)})}}\left(\frac{3}{2\pi}\right)^{g/2}\left(1-\frac{3}{20m}\sum_{f\in E(H)}r_f^2+O_H(m^{-2})\right),\quad m\to\infty,}
\]
where \(\tau(H^{(m)})=m^g\tau(H)\). For a tree this is an exact identity for all \(m\): \(W_m=2^{me}\). For any graph with a cycle, \(\sum_f r_f^2>0\), so the first relative correction is strictly negative. The factor \(\sum_f r_f^2\) is intrinsic to the original graph and is the squared Euclidean norm of its uniform-spanning-tree edge-exclusion probability vector.

For a triangle, the formula reads
\[
W_m=\frac{2^{3m}}{\sqrt{2\pi m}}\left(1-\frac{1}{20m}+O(m^{-2})\right).
\]
For \(H=K_{2,3}\), it reads
\[
W_m=\frac{2^{6m}\sqrt3}{4\pi m}\left(1-\frac{1}{10m}+O(m^{-2})\right).
\]

## Assumptions and scope
The graph is fixed as \(m\to\infty\); no joint uniformity in graph order is asserted. Edges have unit length; all inserted subdivision paths have the same integer length \(m\). Loops, multiple edges and a disconnected base are excluded. The polar is defined using the induced Euclidean structure on the **zero-sum** hyperplane. These choices determine the normalization, and the asymptotic statement concerns continuous intrinsic volume, not lattice-point enumerators. All probabilities and spanning-tree counts refer to the **original** graph \(H\).

## Proof
**Step 1: Cycle coordinates and the exact cube-density identity.** Orient \(H\) arbitrarily, choose a spanning tree and write a fundamental signed cycle matrix \(B\in\mathbb Z^{g\times e}\), with a unit column on each chosen chord and with rows forming a basis of the integral cycle lattice. For \(g=0\), use the empty matrix. Write \(b_f\) for its column indexed by edge \(f\), and \(Q=BB^\top\) when \(g\ge1\). Orient each subdivided path consistently and form \(B_m\) by repeating every column \(b_f\) exactly \(m\) times. The linear map from vertex potentials (anchored at any root) to edge differences is an integer lattice isomorphism onto \(\ker B_m\cap\mathbb Z^{me}\): a potential difference integrates pathwise consistently exactly when all cycle sums vanish. A fundamental-cycle matrix contains a \(g\times g\) chord-segment identity submatrix, so integrating the corresponding variables against these constraints has Jacobian one. Consequently, for independent \(U_j\sim\operatorname{Unif}[-1,1]\), the anchored volume of the polytope of consistent edge differences is
\[
W_m=2^{me} f_m(0),\qquad f_m=\text{density of }B_mU\ \text{on }\mathbb R^g.
\]
Here the convention is \(f_m(0)=1\) for \(g=0\). The Jacobian from anchored potential coordinates to zero-sum intrinsic Euclidean measure is \(1/\sqrt{N_m}\), establishing precisely the prefactor in the definition of \(W_m\).

**Step 2: A uniform local expansion.** For \(g>0\), Fourier inversion gives, for all sufficiently large integers \(m\),
\[
f_m(0)=\frac{1}{(2\pi)^g}\int_{\mathbb R^g}\prod_{f\in E(H)}\left(\frac{\sin(b_f\cdot t)}{b_f\cdot t}\right)^m\,dt,
\]
with \(\operatorname{sinc}(0)=1\). Write \(a_f=Q^{-1/2}b_f\) and substitute \(t=\sqrt{3/m}\,Q^{-1/2}z\). Because \(\sum_f a_fa_f^\top=I_g\), the Taylor identity
\[
\log(\operatorname{sinc}u)=-u^2/6-u^4/180+O(u^6)
\]
gives, on the growing central region \(\|z\|\le m^{1/12}\),
\[
\prod_f\operatorname{sinc}\!\left(\sqrt{3/m}\,a_f\cdot z\right)^m=e^{-\|z\|^2/2}\left[1-\frac1{20m}\sum_f(a_f\cdot z)^4+O_H\!\left(m^{-2}(1+\|z\|^8)\right)\right].
\]
The error integrates against the Gaussian to \(O_H(m^{-2})\). On the complement, select the \(g\) independent chord columns. Their sinc factors give an integrable product tail for \(m\ge2\); on any region bounded away from the origin, at least one factor has absolute value bounded strictly below one. Splitting the integral into \(\|t\|\le\varepsilon\), \(\varepsilon<\|t\|\le R\) and \(\|t\|>R\) bounds the noncentral contribution by \(O_H(e^{-c m^{1/6}})\) after the change of variables (the far tail is also exponentially small using the independent-column factors). Thus this termwise integrated expansion is justified, not merely a formal moment computation.

For a standard \(g\)-dimensional Gaussian \(Z\), \(\mathbb E(a_f\cdot Z)^4=3\|a_f\|^4\). Integrating yields
\[
f_m(0)=\left(\frac3{2\pi m}\right)^{g/2}\frac1{\sqrt{\det Q}}\left[1-\frac3{20m}\sum_f(b_f^\top Q^{-1}b_f)^2+O_H(m^{-2})\right].
\]

**Step 3: Identify the graph invariants.** Cauchy–Binet gives \(\det Q=\sum_{|S|=g}(\det B_S)^2\). Fundamental cycle matrices are totally unimodular on full-rank minors: \(\det B_S=\pm1\) precisely when the complementary \(e-g=v-1\) edges form a spanning tree, and it vanishes otherwise. Hence \(\det Q=\tau(H)\). Independently, subdividing an edge in a spanning tree allows all its \(m\) segments; each original edge absent from the contracted tree contributes exactly one of its \(m\) segments as the unique deleted segment. There are exactly \(g\) absent original edges, giving \(\tau(H^{(m)})=m^g\tau(H)\).

The matrix \(\Pi=B^\top(BB^\top)^{-1}B\) is the orthogonal projector onto the cycle space of \(H\). Its \(f\)-diagonal is \(1-\Pr(f\in T)\): the complementary orthogonal projector onto gradients has diagonal \(\mathsf R_{\rm eff}^H(f)\), which equals the edge-inclusion probability by the matrix-tree/transfer-current identity. Therefore \(b_f^\top Q^{-1}b_f=r_f\). Substituting these identities into Step 2 and the exact identity of Step 1 gives the theorem. If \(g=0\), no constraints remain and \(W_m=2^{me}\) exactly. If \(g>0\), at least one cycle edge has \(r_f>0\), making the coefficient strictly negative.

## Verification
The standalone `artifacts/verify.py` depends only on Python 3 and SymPy. It constructs fundamental cycle matrices from exact incidence matrices, checks \(\det(BB^\top)=\tau(H)\), verifies all leverage/exclusion identities, and checks \(\tau(H^{(m)})=m^g\tau(H)\) for four subdivision factors on seven structurally different graphs (28 graph profiles). It also computes 21 exact central box-spline volume profiles independently of the Fourier expansion; these include a series-parallel theta realization of \(K_{2,3}\) and cycle subdivisions, and checks agreement with the predicted second-order asymptotics. The exact output marker is `GRAPH_POLAR_SUBDIVISION_CHECKS_PASSED`. Finite checks are corroboration; the proof above establishes the infinite-family statement.

## Relationship to prior work
D’Alì, Delucchi and Michałek study graph symmetric edge polytopes and their polars, including lattice-point and face data, in *Many Faces of Symmetric Edge Polytopes* (first public arXiv version October 11, 2019). Higashitani, Jochemko and Michałek address arithmetic and Ehrhart properties of symmetric edge polytopes. Xu’s *Multivariate Splines and Polytopes* supplies a general multivariate spline approach to cube sections. The spanning-tree transfer-current formula and multivariate Fourier/Edgeworth methods are classical. The present assertion concerns a different conjunction: the **two-term continuous polar-volume expansion for arbitrary uniform graph subdivisions** and its explicit first correction expressed as the squared \(\ell_2\) norm of spanning-tree **exclusion** probabilities. The listed prior results provide tools or related invariants but no verified statement of that combined formula. Novelty is provisional pending independent literature review.

## Limitations
The error constant depends on the fixed graph. Nonuniform edge subdivision, weighted edges, joint limits with growing graph complexity, and higher-order coefficients are not claimed. The box-spline representation and the local central-limit method are known general tools; the claimed contribution is their graph-specific invariant identification and sharp first correction, not invention of these tools. Full historical priority is unverified, and a more general preexisting box-spline expansion could imply this special case without sharing its wording. No independent mathematical audit has been performed.

## References
- A. D’Alì, E. Delucchi, and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193v1 (posted 2019-10-11); Electronic Journal of Combinatorics (2022), DOI:10.37236/10387. Primary literature, full preprint inspected.
- A. Higashitani, K. Jochemko, and M. Michałek, *Arithmetic Aspects of Symmetric Edge Polytopes*, arXiv:1807.07678 (2018). Background arithmetic and facet theory.
- Z. Xu, *Multivariate Splines and Polytopes*, arXiv:0806.1127 (2008). General box-spline/cube-section machinery.
- Standard matrix-tree theorem, transfer-current/effective-resistance identity, and Fourier inversion for compactly supported box splines.
