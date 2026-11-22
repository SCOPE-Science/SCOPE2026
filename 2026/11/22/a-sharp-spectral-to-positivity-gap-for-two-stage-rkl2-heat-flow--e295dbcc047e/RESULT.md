# A sharp spectral-to-positivity gap for two-stage RKL2 heat flow on triangular graphs

## Finding

For every finite connected simple undirected unweighted \(d\)-regular graph \(G\), with adjacency matrix \(A\), Laplacian \(L=dI-A\), minimum number of common neighbors along an edge
\[
 t=\min_{ij\in E(G)}(A^2)_{ij},
\]
and largest Laplacian eigenvalue \(\Lambda>0\), the completed two-stage second-order Runge–Kutta–Legendre (RKL2) heat update is
\[
 T(h)=I-hL+\tfrac12h^2L^2.
\]
For every real \(h\ge0\), it is entrywise nonnegative **if and only if**
\[
 \boxed{0\le h\le h_{\rm pos}=\frac{2}{2d-t}.}
\]
It is an \(\ell^2\)-contraction **if and only if** \(0\le h\le h_{\rm stab}=2/\Lambda\). Consequently every linearly stable timestep preserves nonnegative states exactly when \(\Lambda\ge 2d-t\); otherwise the entire interval \((h_{\rm pos},h_{\rm stab}]\) is stable but not positive.

In the triangular graph \(J(n,2)\), whose vertices are unordered pairs of an \(n\)-element set and whose edges join intersecting pairs, for **every integer** \(n\ge4\) these sharp bounds are
\[
 \boxed{h_{\rm pos}=\frac{2}{3(n-2)},\qquad h_{\rm stab}=\frac{1}{n-1}.}
\]
They agree at \(n=4\) and differ strictly for every \(n\ge5\). Their ratio has the exact asymptotic limit
\[
 \boxed{\frac{h_{\rm stab}}{h_{\rm pos}}=\frac{3(n-2)}{2(n-1)}\longrightarrow\frac32.}
\]
At \(n=5\), the stable step \(h=7/30\) produces the **exact negative transition** \(T(h)_{\{1,2\},\{1,3\}}=-7/600\). Every update still preserves total mass and contracts \(\ell^2\) throughout the stable interval.

For any \(\tau>0\), compose the heat update with the exact Allen–Cahn reaction half-flow on each coordinate:
\[
 \Phi_{\tau/2}(u)=\frac{u}{\sqrt{e^{-\tau}+(1-e^{-\tau})u^2}},\qquad
 S_\tau=\Phi_{\tau/2}\circ T(\tau)\circ\Phi_{\tau/2}.
\]
Then \(S_\tau\) maps the entire cube \([-1,1]^{|V|}\) into itself **if and only if** \(\tau\le h_{\rm pos}\). Thus the same triangular-graph gap is an exact maximum-principle failure window for the network Allen–Cahn splitting, not merely a linear sign defect.

## Assumptions and scope

The graph is finite, connected, simple, undirected, unweighted and regular of integer degree \(d\ge1\); all step sizes are nonnegative and diffusion has unit edge rate. The triangular-graph specialization requires integer \(n\ge4\). Positivity is entrywise nonnegativity of the completed update matrix, and stability is nonexpansiveness in the Euclidean norm. The reaction map acts componentwise; the cube assertion is for every initial vector in the cube at a single complete step, and hence at all iterates whenever the condition is satisfied. The method has exactly two RKL2 stages; no claim is made for three or more stages or varying graph generators.

## Proof

**1. Identification of the method.** The two-stage RKL2 polynomial in the motivating RKL construction, with \(P_2(z)=(3z^2-1)/2\), is
\[
 \frac23 I+\frac13P_2(I+hQ)=I+hQ+\frac{h^2}{2}Q^2,
 \qquad Q=-L.
\]
This identifies the completed operator without relying on positivity of its internal stages.

**2. Exhaustive entry classification.** Because \(A\) is symmetric and \(d\)-regular, \((A^2)_{ii}=d\). Directly expanding \(T=I+h(A-dI)+\tfrac12h^2(A^2-2dA+d^2I)\) gives
\[
 T_{ii}=1-dh+\frac{d(d+1)}2h^2>0,
\]
\[
 T_{ij}=h\left[1-\frac{2d-(A^2)_{ij}}2h\right]\quad(ij\in E),
 \qquad T_{ij}=\frac{h^2}{2}(A^2)_{ij}\ge0\quad(ij\notin E,\ i\ne j).
\]
The diagonal quadratic is strictly positive because its discriminant is \(-d(d+2)<0\). On edges the smallest common-neighbor count \(t\) gives the first and only sign violation, at \(2/(2d-t)\). Since every edge has at most \(d-1\) common neighbors, \(2d-t>0\). This proves the exact, global-in-\(h\) positivity cutoff. Since \(L\mathbf1=0\), all rows sum to one even past that cutoff.

**3. Exact contraction window.** For each \(\lambda\in[0,\Lambda]\), the scalar multiplier is \(r(h\lambda)=1-h\lambda+(h\lambda)^2/2\). On the nonnegative real axis, \(0<r(z)\le1\) precisely for \(0\le z\le2\); when \(z>2\), \(r(z)>1\). Orthogonal diagonalization of the symmetric Laplacian proves the exact bound \(h_{\rm stab}=2/\Lambda\), hence the sharp graph criterion and the interval of stable-but-negative updates.

**4. Triangular-graph spectrum.** In \(J(n,2)\), each pair meets \(2(n-2)\) other pairs, so \(d=2(n-2)\). For adjacent \(\{1,2\}\) and \(\{1,3\}\), their common neighbors comprise the \(n-3\) pairs \(\{1,k\}\) with \(k\ge4\), together with \(\{2,3\}\); hence \(t=n-2\). Let \(B\) be the \(n\)-by-\(\binom n2\) unsigned vertex-edge incidence matrix of \(K_n\). Then \(B^\top B=2I+A\) and \(BB^\top=(n-2)I+J\). Thus \(A\) has eigenvalues \(2(n-2)\), \(n-4\), and \(-2\) (for \(n=4\), all three sectors are present). Therefore \(L\) has largest eigenvalue \(d+2=2(n-1)\). Substituting into Steps 2–3 proves both cutoffs and the ratio. At \(n=5,h=7/30\), an edge entry is \((7/30)(1-9(7/30)/2)=-7/600\), while \(7/30<1/4\), proving the concrete stable violation.

**5. Exact cube equivalence for nonlinear splitting.** The reaction flow \(\Phi_a\), for \(a\ge0\), maps \([-1,1]\) into itself and fixes \(\pm1\); furthermore \(|\Phi_a(z)|>1\) whenever \(|z|>1\), by comparing its positive denominator with \(|z|\). If \(T\) is nonnegative and row-stochastic, it maps the cube into itself and the composition preserves it. Conversely suppose one entry of \(T\) is negative. For that row choose an initial sign vector with signs matching the row entries (arbitrary signs at zero entries). The first half-flow fixes every sign, and the heat update at that row equals its absolute row sum, strictly greater than one because the signed row still sums to one. The last reaction half-flow retains a value greater than one. Hence cube invariance fails. This proves the claimed *if and only if* without relying on experiments.

## Verification

The standalone standard-library script `verify.py` forms graph adjacency matrices and exact-rational quadratic updates, and tests the general sign formula on complete graphs, hypercubes, odd cycles and triangular graphs. It reconstructs the specified ten-vertex counterexample, as well as row sums and boundary positivity with exact fractions. Run `python3 verify.py` from the extracted package. The script verifies finite instances only; Steps 1–5 prove the all-graph and all-\(n\) statements.

## Relationship to prior work

Tan, Aslam and Bertozzi (2026, arXiv:2611.16238, Sections 3.1 and 4.1) define the RKL2 scheme and prove a one-dimensional Allen–Cahn maximum principle, noting that multidimensional numerical monotonicity is not automatic. Their earlier work (arXiv:2507.17062) studies one-dimensional monotone stability; its abstract was accessible here but the full text was not. The published exact degree-two Taylor positivity result on *complete multipartite* graphs establishes a special family of graph updates but does not cover the triangular graphs \(J(n,2)\) for \(n\ge5\), nor the exact spectral/positivity ratio limit in that family. Another published study optimizes products of two **real forward-Euler** steps on regular graphs; its full proof does not imply this RKL2 polynomial, because \(1+z+z^2/2\) has nonreal roots and cannot be such a product. These sources are credited for the method and relevant narrower comparison results, not represented as the present theorem. No claim of exhaustive historical priority is made.

## Limitations

The calculation is for the *completed* linear step, not its internal stages; cube preservation concerns the stated network Allen–Cahn Strang composition, not arbitrary nonlinear flows. It is not a claim that every stable timestep on every one-dimensional spatial mesh violates positivity, nor a guarantee of improved efficiency or higher-order accuracy. The precise positive cutoffs for other graph families can differ. Publication priority remains conditional on unlocated equivalent specialist work and one inaccessible related full text. Independent validation has not been performed.

## References

1. Z. Tan, T. D. Aslam and A. L. Bertozzi, *Fully Explicit Stabilized Runge–Kutta Methods for Allen–Cahn and Cahn–Hilliard Dynamics*, arXiv:2611.16238v1, first posted 2026-11-12. https://arxiv.org/html/2611.16238v1 .
2. Z. Tan, T. D. Aslam and A. L. Bertozzi, *Explicit Monotone Stable Super-Time-Stepping Methods for Finite Time Singularities*, arXiv:2507.17062v1, first posted 2025-07-22, *SIAM J. Appl. Math.* 86 (2026), 457–481. https://arxiv.org/abs/2507.17062 .
3. *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs*, published mathematical record (2026-11-02). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-positivity-radii-and-an-order-three-reversal-for-taylor-ru--0aa3ec090e79 .
4. *A triangle-count law for positive two-stage Euler supersteps on regular graphs*, published mathematical record (2026-11-08). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-triangle-count-law-for-positive-two-stage-euler-supersteps-on--395a6d422888 .
