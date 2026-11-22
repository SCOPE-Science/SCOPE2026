# Boundary-cycle resonance and the sharp Robin quadrature penalty window

## Finding

A one-point positive boundary quadrature for a conforming piecewise-affine finite-element trace can leave an entire boundary mode invisible to a Robin penalty. On any polygonal boundary cycle with an even number of edges, the mode survives exactly when the products of the node fractions and their complements agree. In particular, midpoint quadrature has one invisible alternating boundary mode per even cycle and none per odd cycle. The Robin penalty tends to the discrete Dirichlet solution for **every** load if and only if no such cycle resonates.

A single bilinear element on the unit square provides a sharp quantitative realization. With one bottom-edge quadrature node displaced by \(\varepsilon\) from the midpoint, while the other edge nodes are midpoints, and penalty \(\lambda>0\), the discrete solution \(u_{\lambda,\varepsilon}\) for the exact volume load \(f=(1-2x)(1-2y)\) satisfies, along every sequence \(\lambda\to\infty\), \(\varepsilon\to0\) with \(\lambda\varepsilon^2\to\tau\in[0,\infty)\),

\[
 u_{\lambda,\varepsilon}\longrightarrow \frac{(1-2x)(1-2y)}{24+9\tau}.
\]

For \(\lambda\varepsilon^2\to\infty\), the limit is zero. At exact midpoints, the discrete solution is \((1-2x)(1-2y)/24\) for every positive penalty, whereas exact integration of the same boundary term gives \((1-2x)(1-2y)/[12(2+\lambda)]\), tending to zero. Thus the perturbation scale \(|\varepsilon|\asymp\lambda^{-1/2}\) is sharp. These conclusions concern a fixed mesh, not any refinement-limit rate.

## Assumptions and scope

Let \(\Omega\subset\mathbb R^2\) be a connected bounded polygonal Lipschitz domain with finitely many closed boundary components, each represented by a cyclic chain of edges with independently represented nodal boundary values. Let \(V_h\subset H^1(\Omega)\) be a standard conforming scalar nodal piecewise-linear triangular space, or a nodal space with the same affine traces and independent boundary vertex degrees of freedom. Assume a symmetric conductivity form \(K(u,v)=\int_\Omega a\nabla u\cdot\nabla v\,dx\), with \(0<a_0\le a\le a_1\), that has exactly the constant functions as its kernel on \(V_h\). Let \(F\in V_h^*\) be any fixed linear load. All volume integrals are exact.

On boundary component \(c\), label its \(N_c\ge3\) consecutive vertices \(P_{c,j}\) and edges \(P_{c,j}P_{c,j+1}\), indices modulo \(N_c\). Put one point \(z_{c,j}=(1-t_{c,j})P_{c,j}+t_{c,j}P_{c,j+1}\) on each edge, with \(0<t_{c,j}<1\) and weight \(w_{c,j}>0\). Set \(B_t(u,v)=\sum_{c,j}w_{c,j}u(z_{c,j})v(z_{c,j})\). For every \(\lambda>0\), \(u_{\lambda,t}\in V_h\) solves \(K(u_{\lambda,t},v)+\lambda B_t(u_{\lambda,t},v)=F(v)\) for all \(v\in V_h\). Set \(V_{h,0}=\{v\in V_h:v(P_{c,j})=0\ \forall c,j\}\); let \(u_D\in V_{h,0}\) solve \(K(u_D,v)=F(v)\) for all \(v\in V_{h,0}\), with the convention \(u_D=0\) if \(V_{h,0}=\{0\}\).

## Proof

**Cycle classification.** As every edge trace is affine, \(B_t(u,u)=0\) is equivalent to the \(N_c\) equations \((1-t_{c,j})u_{c,j}+t_{c,j}u_{c,j+1}=0\) on each component. Since all fractions lie strictly inside \((0,1)\), these give \(u_{c,j+1}=-[(1-t_{c,j})/t_{c,j}]u_{c,j}\). A nonzero cyclic trace exists exactly if

\[
(-1)^{N_c}\prod_{j=1}^{N_c}\frac{1-t_{c,j}}{t_{c,j}}=1.
\]

The positive product forces \(N_c\) to be even; for even \(N_c\) the remaining requirement is \(\prod_j(1-t_{c,j})=\prod_jt_{c,j}\). A resonant cycle has exactly one dimensional boundary kernel, because its first vertex determines all others; a nonresonant cycle has none. Boundary nodal values can be independently prescribed, so the total kernel consists of \(V_{h,0}\) plus one boundary trace lift for each resonant cycle. At midpoints every product equality holds automatically, giving exactly the stated parity classification.

**Penalty limit.** For every \(\lambda>0\), \(K+\lambda B_t\) is positive definite: the nullspace of \(K\) consists of constants, and a nonzero constant has strictly positive sampled boundary energy. Consequently \(u_{\lambda,t}\) exists uniquely. For \(\lambda\ge1\), coercivity of \(K+B_t\) gives a uniform finite-dimensional bound on the solution. Testing with the solution yields \(\lambda B_t(u_{\lambda,t},u_{\lambda,t})\le C\), hence any convergent subsequence has its limit in \(W_t=\ker B_t\). Testing against arbitrary \(v\in W_t\) shows that every limit solves \(K(u_W,v)=F(v)\) on \(W_t\). This has a unique solution because no nonzero constant is in \(W_t\); thus \(u_{\lambda,t}\to u_W\). If no cycle resonates, \(W_t=V_{h,0}\), so the limit equals \(u_D\) for all loads. If some cycle resonates, select a nonzero additional trace lift \(z\in W_t\) orthogonal to \(V_{h,0}\) under \(K\). Choose a load with \(F(z)\ne0\) and \(F|_{V_{h,0}}=0\); then \(u_D=0\) while \(u_W\ne0\). This proves the claimed necessary and sufficient condition for all-load Dirichlet convergence. Exact positive boundary integration vanishes only for zero affine boundary traces and therefore always has \(W=V_{h,0}\).

**Square example and exact singular window.** On \(\Omega=[0,1]^2\), take the single \(Q_1\) element with basis \(\phi=((1-x)(1-y),x(1-y),(1-x)y,xy)^T\) and \(v=(1,-1,-1,1)^T\). The represented function is \(\phi^Tv=(1-2x)(1-2y)\). Exact volume stiffness and load obey \(Kv=(2/3)v\), \(F=(\int_\Omega f\phi_i)_i=v/36\), so \(v^TKv=8/3\) and \(v^TF=1/9\).

The four unit-weight edge evaluations, in bottom–right–top–left order, are rows of

\[
C_\varepsilon=\begin{pmatrix}
\tfrac12-\varepsilon&\tfrac12+\varepsilon&0&0\\
0&\tfrac12&0&\tfrac12\\
0&0&\tfrac12&\tfrac12\\
\tfrac12&0&\tfrac12&0
\end{pmatrix},\qquad \det C_\varepsilon=\varepsilon/4.
\]

Thus \(B_\varepsilon=C_\varepsilon^TC_\varepsilon\) has null vector \(v\) precisely at \(\varepsilon=0\). The solution of \((K+\lambda B_\varepsilon)U=F\) at that point is exactly \(U=v/24\) for every \(\lambda>0\). In contrast, the exactly integrated boundary mass satisfies \(B_{\mathrm{exact}}v=v/3\); the exact-boundary-assembly solution is \(U=v/[12(2+\lambda)]\).

To prove the two-parameter limit, let \(C_0=C_{\varepsilon=0}\) and \(E=(C_\varepsilon-C_0)/\varepsilon\). The right kernel of \(C_0\) is \(\operatorname{span}\{v\}\), and its left unit null vector is \(\ell=(1,-1,1,-1)^T/2\). Hence \(\ell^TEv=-1\). The minimizing quadratic energy \(\frac12U^TKU+\frac\lambda2\|C_\varepsilon U\|_2^2-F^TU\) has bounded minimizers for \(\lambda\ge1\). If \(\lambda\varepsilon^2\to\tau<\infty\) while \(\lambda\to\infty\), its bounded minimizers approach \(cv\); the stiff constraints suppress \(\operatorname{ran}C_0\) and the optimal transverse correction removes exactly that component of \(\varepsilon cEv\). The remaining penalty is \(\tau c^2\|\operatorname{proj}_{\ker C_0^T}Ev\|_2^2=\tau c^2\). Thus the limiting scalar energy is \(\frac12(8/3+\tau)c^2-(1/9)c\), whose unique minimum is \(c=1/(24+9\tau)\). This argument also covers \(\tau=0\). If instead \(\lambda\varepsilon^2\to\infty\), the smallest singular value of \(C_\varepsilon\) obeys \(\sigma_{\min}(C_\varepsilon)\sim|\varepsilon|/2\), by its simple zero singular value and normalized left/right null vectors. Consequently \(\lambda B_\varepsilon\) becomes uniformly coercive, forcing \(U\to0\). These claims are additionally verified by symbolic inversion of the explicit four-by-four system in the accompanying checker.

## Verification

Run `python verify.py` with SymPy installed. It reconstructs the stiffness, load, sampled and exactly integrated boundary mass matrices by exact polynomial integration; checks the null vector, determinant, both exact formulas and the two-parameter limit; and checks cycle ranks for finitely many positive rational node fractions. The script prints `VERIFY_OK 64`. Finite checks of cycles and limits are corroboration, not proofs of their universal versions; the proof above supplies those steps.

## Relationship to prior work

Han and Wu, *The effect of numerical integration in the FEM for elliptic problems with mixed boundary conditions* (arXiv:2606.16675, first submitted 2026-06-15), establish conditions on volume and face quadrature precision for optimal mesh-refinement error rates and numerical counterexamples for insufficient precision. Their introduction, quadrature definitions, main estimates, examples and conclusion were inspected. Their analyzed regime is not the fixed-mesh Robin penalty limit, nor a classification by boundary-cycle parity or a two-parameter node-displacement boundary layer. Chiba and Saito, *Nitsche's method for a Robin boundary value problem in a smooth domain* (arXiv:1905.01605; journal DOI 10.1002/num.23038), analyze Robin/Dirichlet penalty error estimates but do not assert the stated one-point boundary-sampling resonance. Classical reduced-integration literature including Oden's 1984 report discusses spurious zero-energy mechanisms generally; the present contribution is a fully specified boundary-trace necessary-and-sufficient condition and a sharp \(\lambda\varepsilon^2\) crossover in a concrete element. These distinctions are implication comparisons, not a claim of exhaustive historical priority.

## Limitations

The topological classification assumes affine boundary traces, positive interior-edge quadrature weights, all boundary cycles sampled, independent boundary nodal degrees of freedom and exact volume integration. The square calculation uses a single \(Q_1\) element, one intentionally shifted edge node, a specific load and fixed geometry. It does not demonstrate failure of appropriately designed higher-order quadrature, does not contradict fixed-Robin-parameter mesh-refinement estimates, and does not provide a universal mesh-refinement error rate. Exact singular-value asymptotics rely on the exhibited matrix, not generic meshes. Historical originality is assessed against named accessible sources, without independent audit of every possible equivalent earlier result.

## References

1. J. Han and H. Wu, *The effect of numerical integration in the FEM for elliptic problems with mixed boundary conditions*, arXiv:2606.16675 (2026-06-15). https://arxiv.org/abs/2606.16675
2. Y. Chiba and N. Saito, *Nitsche's method for a Robin boundary value problem in a smooth domain*, arXiv:1905.01605 (2019), journal DOI:10.1002/num.23038. https://arxiv.org/abs/1905.01605
3. J. T. Oden, *Stability and Convergence of Underintegrated Finite Element Approximations*, NASA-CP-2297 proceedings (1984). https://ntrs.nasa.gov/api/citations/19840023618/downloads/19840023618.pdf
