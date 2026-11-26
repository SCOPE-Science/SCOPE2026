# Exact checkerboard phase selection and classical-energy obstruction for Strang splitting

## Finding
For the semidiscrete Allen–Cahn gradient flow on any finite connected regular bipartite graph, two symmetric orientations of reaction–diffusion Strang splitting have explicitly different, step-size-dependent, nonconstant attracting equilibria on the invariant checkerboard subspace. On that subspace, the exact stable squared amplitudes are
\[
Y_{\mathrm{DRD}}=\frac{\sinh((1-\delta)h)}{\sinh h},\qquad
Y_{\mathrm{RDR}}=\frac{\sinh((1-\delta)h)}{\sinh((1-\delta)h)+\sinh(\delta h)}.
\]
For every \(h>0\) and \(0<\delta<1\), the diffusion–reaction–diffusion (DRD) equilibrium underestimates the physical squared amplitude \(1-\delta\). The reaction–diffusion–reaction (RDR) equilibrium overestimates it for \(\delta<1/2\), matches it at every step size for \(\delta=1/2\), and underestimates it for \(\delta>1/2\). Consequently, a single DRD step begun at the exact nonconstant physical equilibrium strictly *increases the original Allen–Cahn energy* for every positive step; RDR does so for every positive step unless \(\delta=1/2\). This does not contradict known dissipation of a *modified* discrete energy.

## Assumptions and scope
Let \(G=(V,E)\) be an arbitrary finite connected, undirected, unweighted \(r\)-regular bipartite graph with \(N=|V|\), \(r\ge1\), combinatorial Laplacian \(L=rI-A\), and checkerboard sign vector \(s\in\{-1,1\}^{N}\) equal to \(+1\) on one vertex class and \(-1\) on the other. Fix \(\eta>0\), \(\delta=2\eta r\in(0,1)\), \(\alpha=1-\delta\), and any \(h>0\). Consider the ODE and its classical energy
\[
\dot u=-\eta Lu+u-u^{\circ3},\qquad
E(u)=\frac{\eta}{2}u^{T}Lu+\frac14\sum_{i\in V}(u_i^2-1)^2.
\]
Define diffusion and reaction flow maps for all positive times by
\[
D_tu=e^{-\eta tL}u,\qquad
(R_tu)_i=\frac{e^tu_i}{\sqrt{1+(e^{2t}-1)u_i^2}}.
\]
Two methods are \(S_{\mathrm{DRD}}=D_{h/2}\circ R_h\circ D_{h/2}\) and \(S_{\mathrm{RDR}}=R_{h/2}\circ D_h\circ R_{h/2}\). All statements about convergence and uniqueness of nonzero numerical equilibria refer **only to the invariant one-dimensional checkerboard subspace** \(\{xs:x\in\mathbb R\}\); no uniqueness or attraction in the full \(N\)-dimensional state space is asserted.

## Proof
**Invariant reduction.** Bipartite regularity gives \(Ls=2rs\), hence \(D_t(xs)=e^{-\delta t}xs\). Odd pointwise reaction maps \(xs\) to \(g_t(x)s\). Thus both exact subflows preserve the checkerboard subspace. The original ODE reduces there to \(\dot x=\alpha x-x^3\), with three equilibria \(0\) and \(\pm\sqrt\alpha\); both nonzero equilibria are attracting *within this subspace*.

**Exact numerical dynamics.** For \(y=x^2\), a reaction subflow of duration \(t\) acts as \(F_t(y)=e^{2t}y/[1+(e^{2t}-1)y]\), whereas diffusion multiplies \(y\) by \(e^{-2\delta t}\). Direct composition yields for either orientation
\[
y^+=\frac{e^{2\alpha h}y}{1+\beta_j y},\quad
\beta_{\mathrm{DRD}}=(e^{2h}-1)e^{-\delta h},\quad
\beta_{\mathrm{RDR}}=(e^h-1)(1+e^{(1-2\delta)h}).
\]
The positive squared fixed point is uniquely \(Y_j=(e^{2\alpha h}-1)/\beta_j\). Elementary identities \(e^{2z}-1=2e^z\sinh z\) and \(\sinh a+\sinh b=2\sinh((a+b)/2)\cosh((a-b)/2)\) give exactly the two displayed hyperbolic-sine formulas. The zero fixed point has squared-map derivative \(e^{2\alpha h}>1\). For every \(y_0>0\), taking reciprocals yields an affine contraction and its exact iterates:
\[
\frac1{y_n}=\frac1{Y_j}+e^{-2\alpha hn}\left(\frac1{y_0}-\frac1{Y_j}\right).
\]
The sign of the amplitude is preserved by each subflow, so every nonzero initial amplitude converges to the corresponding signed numerical equilibrium, and the origin is unstable on the checkerboard line.

**Sharp orientation comparison.** Because \(z\mapsto\sinh z/z\) is strictly increasing for \(z>0\) (differentiate: \(z\cosh z-\sinh z>0\)), and \(0<\alpha<1\), one has \(Y_{\mathrm{DRD}}<\alpha\) for every \(h>0\). Likewise
\[
Y_{\mathrm{RDR}}\gtrless\alpha
\iff
\delta\sinh(\alpha h)\gtrless\alpha\sinh(\delta h)
\iff
\alpha\gtrless\delta,
\]
which proves the stated trichotomy. As \(h\downarrow0\), Taylor expansion gives
\[
Y_{\mathrm{DRD}}=\alpha-\frac{\alpha\delta(2-\delta)}6h^2+O(h^4),\quad
Y_{\mathrm{RDR}}=\alpha+\frac{\alpha\delta(1-2\delta)}6h^2+O(h^4).
\]
As \(h\to\infty\), \(Y_{\mathrm{DRD}}\to0\), while \(Y_{\mathrm{RDR}}\to1\) if \(\delta<1/2\), \(1/2\) if \(\delta=1/2\), and \(0\) if \(\delta>1/2\).

**Classical-energy obstruction.** On the checkerboard line, \(s^TLs=2rN\) and therefore
\[
E(xs)=\frac N4\big[(x^2-\alpha)^2+1-\alpha^2\big].
\]
Starting at the genuine physical steady state \(u_*=\sqrt\alpha\,s\), either Strang map produces squared amplitude \(y^+\). This equals \(\alpha\) if and only if \(Y_j=\alpha\), because the scalar map's sole positive fixed point is \(Y_j\). Consequently,
\[
E(S_j(u_*))-E(u_*)=\frac N4(y^+-\alpha)^2>0
\]
for every DRD step and for RDR unless \(\delta=1/2\); in that exceptional RDR case the exact checkerboard physical equilibrium remains fixed. The energy increase at the *true continuous equilibrium* disproves a universal one-step dissipation inequality for the **unmodified original energy** under the specified conditions.

## Verification
Run `python verify.py` with Python 3, NumPy and SciPy. The accompanying `verification_output.txt` records a completed run. The script independently assembles graph Laplacians, evaluates full matrix-exponential diffusion and nonlinear reaction, checks both symbolic Möbius maps, equilibrium orientation inequalities, the classical-energy identity and exact reciprocal iterates. Its finite tests use the single edge and even cycles of 4, 6 and 8 vertices; they do not replace the proof for arbitrary regular bipartite graphs, positive time steps, or all \(\delta\in(0,1)\).

## Relationship to prior work
Luo, Quan, Tan and Wu (2026, arXiv:2610.14867) analyze the **DRD** orientation with long-time Sobolev bounds, optimal-parameter error estimates, and modified-energy dissipation. Li, Quan and Xu (2021, arXiv:2108.05214) established stability and strict dissipation for a deliberately **modified** energy, not a claim of unconditional decrease of the original energy. The related matrix-valued work of Quan, Tang and Wang (2025, arXiv:2508.03992) also concerns modified-energy analysis. The exact checkerboard squared-amplitude laws, the RDR orientation threshold, and the original-energy obstruction are not identified in the inspected portions or claims of those papers. They are specialized finite-graph consequences, not strengthened global Sobolev estimates for continuous-domain solutions. An independently published equivalence may still exist.

## Limitations
The graph is connected, undirected, unweighted, regular and bipartite; the strict parameter regime is \(0<2\eta r<1\). Convergence and all fixed-point classifications concern only the invariant checkerboard line, not arbitrary full-space initial conditions or continuous PDE spatial discretizations with other operators. The original-energy counterexample does not invalidate dissipation of a modified energy and does not rule out classical-energy decay for some other states or under additional hypotheses. All claims are proved analytically; numerical tests are finite sanity checks. Independent verification of originality and correctness has not been performed.

## References
1. R. Luo, C. Quan, Z. Tan, Y. Wu, *Stability and Error Estimates with Optimal \(\varepsilon\)-Dependence for Strang Splitting of the Allen–Cahn Equation*, arXiv:2610.14867, first posted 2026-10-10. https://arxiv.org/abs/2610.14867
2. D. Li, C. Quan, J. Xu, *Stability and convergence of Strang splitting. Part I: Scalar Allen-Cahn equation*, arXiv:2108.05214, first posted 2021-08-11. https://arxiv.org/abs/2108.05214
3. C. Quan, T. Tang, D. Wang, *Unconditional energy dissipation of Strang splitting for the matrix-valued Allen-Cahn equation*, arXiv:2508.03992, first posted 2025-08-06. https://arxiv.org/abs/2508.03992
