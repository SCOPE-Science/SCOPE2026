# Exact graph-cut error and balanced-projector hardness in nonlinear split parareal

## Finding

**Theorem (exact split-projection error and its combinatorial optimization).** Let \(G=(V,E)\) be any finite simple undirected graph with an even number \(n=|V|\ge 2\) of vertices. Write \(u\in\mathbb R^n\), \(z\in\mathbb R\), and
\[
\varphi_G(u)=\sum_{\{i,j\}\in E}u_i u_j.
\]
For \(h>0\) and an integer \(p\ge1\), set \(\delta=h^{p+1}\), and use the exact fine propagator and the order-\(p\) coarse propagator
\[
\mathcal F_h(u,z)=(u,z+h\varphi_G(u)),\qquad
\mathcal G_h(u,z)=((1+\delta)u,z+h\varphi_G(u)).
\]
Start both projection-based parareal variants from \((\mathbf1,z_0)\), using the standard coarse-grid initialization, on at least two coarse intervals. For each subset \(S\subset V\) of size \(n/2\), let \(P_S\) be the orthogonal coordinate projector retaining the components \(u_i\) with \(i\in S\) and deleting all other components, including \(z\). Compare the split map
\[
\mathcal S_{P_S}(x)=\mathcal F_h(P_Sx)+\mathcal G_h((I-P_S)x)
\]
with the modified map
\[
\mathcal H_{P_S}(x)=\mathcal G_h(x)+\mathcal F_h(P_Sx)-\mathcal G_h(P_Sx).
\]
Define the graph cut size \(b_G(S)=|\{\{i,j\}\in E: |\{i,j\}\cap S|=1\}|\). Let \(e_{2,\mathcal S}^{1}\) and \(e_{2,\mathcal H}^{1}\) be the vectors *computed minus the fine reference* at the second coarse time point after one parareal iteration for the respective maps. Then, exactly for every \(h>0\),
\[
\boxed{e_{2,\mathcal S}^{1}=(-\delta^2\mathbf1_{S^c},\ h(2\delta+\delta^2)b_G(S)),\qquad
 e_{2,\mathcal H}^{1}=(-\delta^2\mathbf1_{S^c},0).}
\]
Consequently,
\[
\boxed{\|e_{2,\mathcal S}^{1}\|_2^2-\|e_{2,\mathcal H}^{1}\|_2^2
=h^2(2\delta+\delta^2)^2b_G(S)^2,\qquad
\|e_{2,\mathcal H}^{1}\|_2^2=\frac n2\delta^4.}
\]
The rank-\(n/2\) coordinate projection minimizing the first split-method error is therefore *exactly* a minimum graph bisection. Its rational squared-error decision problem is NP-complete, even for unweighted graphs and fixed \(h=1\). On forests, the optimum is computable by cardinality-indexed tree dynamic programming in polynomial time. A zero added split-method error is possible precisely when a union of connected components contains \(n/2\) vertices. If \(G\) is connected, then for each fixed bisection \(S\),
\[
\frac{\|e_{2,\mathcal S}^{1}\|_2}{\|e_{2,\mathcal H}^{1}\|_2}
\sim \frac{2b_G(S)}{\sqrt{n/2}}h^{-p}\qquad(h\downarrow0).
\]

## Assumptions and scope

The underlying ODE is the globally defined polynomial initial-value problem
\[
\dot u=0,\qquad \dot z=\varphi_G(u).
\]
The propagators are maps on all of \(\mathbb R^{n+1}\), and the coarse map has local defect \(\mathcal G_h-\mathcal F_h=(h^{p+1}u,0)\), so it is of order \(p\) uniformly on bounded sets. It is a deliberately simple, equilibrium-preserving coarse approximation, not asserted to be a particular Runge--Kutta method. Both schemes use the same fine and coarse maps. The old iterates are initialized by \(U_0^0=(\mathbf1,z_0)\) and \(U_j^0=\mathcal G_h(U_{j-1}^0)\). Only coordinate projectors of prescribed rank are optimized; no claim is made about all orthogonal projectors or about projectors selected from Krylov histories.

## Proof

**1. Fine flow and projection residuals.** Since \(u\) is constant along the ODE, integration of \(z\) gives \(\mathcal F_h\) exactly. Fix \(S\), write \(Q_S=I-P_S\), and define
\[
C_S(u)=\sum_{\substack{\{i,j\}\in E\\|\{i,j\}\cap S|=1}}u_i u_j.
\]
Every edge lies within \(S\), within \(S^c\), or crosses the cut, hence
\[
\varphi_G(u)-\varphi_G(P_Su)-\varphi_G(Q_Su)=C_S(u).
\]
Direct substitution in the two projected maps yields
\[
\mathcal F_h(u,z)-\mathcal S_{P_S}(u,z)
=(-\delta Q_Su,\ hC_S(u)),
\]
\[
\mathcal F_h(u,z)-\mathcal H_{P_S}(u,z)
=(-\delta Q_Su,0),
\]
where \(Q_Su\) denotes the vector retaining coordinates in \(S^c\); the scalar \(z\) belongs to the complementary projected block but does not affect \(\varphi_G\).

**2. Exact two-time-point parareal identity.** Let \(\mathcal M\) denote either projected map. The one-iteration recurrence is
\[
U_{j+1}^{1}=\mathcal F_h(U_j^0)+\mathcal M(U_j^1)-\mathcal M(U_j^0).
\]
At \(j=0\), the old and new initial data coincide, so \(U_1^1=\mathcal F_h(U_0^0)\). Therefore, writing \(U_2^\star=\mathcal F_h(U_1^1)\),
\[
U_2^1-U_2^\star=(\mathcal F_h-\mathcal M)(U_1^0)
-(\mathcal F_h-\mathcal M)(U_1^1).
\]
The old first time point has \(u=(1+\delta)\mathbf1\), whereas the exact first time point has \(u=\mathbf1\). Thus \(Q_S((1+\delta)\mathbf1)-Q_S\mathbf1=\delta\mathbf1_{S^c}\) and, by homogeneity of the quadratic cut polynomial,
\[
C_S((1+\delta)\mathbf1)-C_S(\mathbf1)
=((1+\delta)^2-1)b_G(S).
\]
Substitution proves the two error vectors and their squared norms. These identities are finite algebraic identities, not small-step approximations.

**3. Sharp order separation.** Every nontrivial cut of a connected graph has \(b_G(S)\ge1\). For \(\delta=h^{p+1}\), the modified error norm equals \(h^{2p+2}\sqrt{n/2}\); the split norm has leading term \(2b_G(S)h^{p+2}\), giving the displayed ratio. For disconnected graphs, \(b_G(S)=0\) exactly when no edge crosses \(S\), which is equivalent to \(S\) being a union of connected components.

**4. Hardness and tractable boundary.** At fixed \(h=1\), hence \(\delta=1\), deciding whether a bisection gives squared split error at most \(n/2+9B^2\) is equivalent, by the exact formula, to deciding whether the graph has a bisection with at most \(B\) crossing edges. The latter is the classical NP-complete MINIMUM BISECTION decision problem. The numerical decision problem belongs to NP: a subset \(S\) is a polynomial-size certificate and its cut size and rational squared error are computed in polynomial time. This proves NP-completeness without relying on numerical approximations.

For a forest, root each tree. For each rooted subtree with root \(v\), store the minimum cut cost \(D_v(k,b)\) among labelings that put exactly \(k\) vertices into \(S\) and assign \(b\in\{0,1\}\) to \(v\). Initialize the one-vertex table by \(D_v(0,0)=D_v(1,1)=0\), with other states infinite. When merging a child \(w\) connected by an edge, combine states by
\[
D_{\rm merged}(k+\ell,b)=\min_{c\in\{0,1\}}
\bigl\{D_{\rm old}(k,b)+D_w(\ell,c)+\mathbf1_{b\ne c}\bigr\},
\]
where the minimum also ranges over all splits of the total vertex count. Merge root tables from different components without an edge penalty and read the state with \(n/2\) selected vertices. Tables have at most \(O(n)\) count states for each binary label and at most \(O(n)\) merges; even naive pairwise table combination requires at most \(O(n^3)\) arithmetic operations. This supplies a polynomial-time exact optimizer on forests.

## Verification

Run `python3 CHECK.py` with Python 3 and no external packages. The checker independently constructs both projected maps, performs the first parareal iteration with `fractions.Fraction`, and compares the resulting vectors to the closed formulas. It also compares the forest dynamic program against all bisections on small forests and tests a graph with multiple possible projectors. The included checker returned `VERIFY_OK: 430 exact split/modified recurrences and forest cut tests; 6 balanced-projection comparisons`.

The finite checks support the algebra and the dynamic-programming implementation. They do not establish NP-completeness or the infinite family of formulas; those conclusions follow from the proof and the classical minimum-bisection result.

## Relationship to prior work

Tan, Xu, Zhang, and Su define the two nonlinear projection-based parareal maps and analyze the differences between their residuals, including a mixed nonlinear term and differing asymptotic error orders. Their general results motivate the question but do not provide this graph-dependent exact two-time-point formula or the computational complexity of balancing coordinate projectors. The source explicitly treats projector-space construction as outside its analysis. Gander and Petcu analyze a Krylov-enhanced method for linear problems, whereas the present example involves a quadratic polynomial vector field. The NP-hardness of graph bisection itself is classical: the new assertion here is the exact reduction from a natural numerical-method error minimization problem. This distinction matters; the theorem does not claim that minimum bisection or the general parareal recurrence is new.

## Limitations

The coarse map is a designed order-\(p\) approximation that preserves zero and is not a claim about an off-the-shelf time integrator. The split-method hardness is proved for rank-constrained **coordinate** projections, not arbitrary orthogonal projectors or the particular history-generated projectors of a Krylov-enhanced implementation. Only the second coarse time point after the first parareal iteration is optimized. Polynomial-time tree optimization does not imply a polynomial-time procedure for arbitrary graphs. The analysis is exact arithmetic; it does not estimate wall-clock performance, communication costs, or roundoff. The result is not a counterexample to convergence of the modified method or to the general error bounds of the motivating paper.

## References

1. C. Tan, Y. Xu, Y. Zhang, and Y. Su, *Projection-Based Parareal for Nonlinear Initial-Value Problems*, arXiv:2610.21680v1, October 15, 2026. https://arxiv.org/html/2610.21680
2. M. J. Gander and M. Petcu, *Analysis of a Krylov Subspace Enhanced Parareal Algorithm for Linear Problems*, ESAIM Proceedings and Surveys 25 (2008), 114–129, doi:10.1051/proc:082508. https://doi.org/10.1051/proc:082508
3. C. G. Fernandes, T. J. Schmidt, and A. Taraz, *On Minimum Bisection and Related Cut Problems in Trees and Tree-Like Graphs*, arXiv:1708.06411 (2017). https://arxiv.org/abs/1708.06411
4. B. Jin, Q. Lin, and Z. Zhou, *Optimizing Coarse Propagators in Parareal Algorithms*, SIAM Journal on Scientific Computing 47 (2025), A735–A761, doi:10.1137/23M1619733. https://doi.org/10.1137/23M1619733
