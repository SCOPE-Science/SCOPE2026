# The bull graph is the smallest network with a reversal of localized consensus relaxation

## Finding
For a connected simple unweighted undirected graph \(G\), start linear consensus \(\dot z=-L_G z\) from a unit impulse at a vertex. Although every such initial condition has the same squared distance from consensus, the ordering of their residual squared disagreements need not be fixed in time. **Five vertices are necessary and sufficient for a strict reversal.** On every graph of at most four vertices, vertices of smaller degree have strictly larger residual disagreement at all positive times than vertices of larger degree, and equal-degree vertices have identical residual disagreement. On the five-vertex bull graph, one degree-three vertex and one degree-two vertex exchange their residual-disagreement ranking **exactly once**, at an explicitly specified positive time.

More precisely, let the bull graph have vertices \(a,b,c,d,e\), triangle edges \(ab,bc,ca\), and pendant edges \(ad,ce\). Set
\[
 E_v(t)=\left\|e^{-tL_G}e_v-\frac{\mathbf 1}{|V(G)|}\right\|_2^2,
 \qquad t\ge0.
\]
There is a unique \(t_*\in(0,\infty)\), numerically \(t_*=1.5728107003557037216776143509897\ldots\), with
\[
 E_a(t)<E_b(t)\quad (0<t<t_*),\qquad
 E_a(t_*)=E_b(t_*),\qquad
 E_a(t)>E_b(t)\quad(t>t_*).
\]
The crossing is simple. This is a **time-dependent ordering reversal** between equally distant initial conditions, not an assertion that their initial errors differ.

## Assumptions and scope
Throughout, \(G\) is connected, undirected, loop-free, unweighted, and simple; \(L_G=\operatorname{diag}(\deg v)-A_G\) is its combinatorial Laplacian. Each experiment uses exactly the same initial magnitude, supported at one vertex: \(z(0)=e_v\). Only the deterministic linear consensus equation is asserted. Since \(G\) is connected, its equilibrium projection is \(\mathbf 1/|V(G)|\). The square-norm measure, not a maximum or pairwise norm, is used. Define the heat time \(s=2t\) and \(q=e^{-s}\in(0,1)\).

## Proof
**1. Spectral reduction.** Because \(L_G\) is real symmetric and \(L_G\mathbf1=0\),
\[
 E_v(t)=e_v^{\mathsf T}e^{-2tL_G}e_v-\frac1n.
\]
Consequently, for any two vertices \(v,w\), their error difference is the difference between the diagonal entries of the ordinary graph heat kernel at time \(s=2t\). For distinct Laplacian eigenvalues \(\lambda\), write \(P_\lambda\) for the orthogonal spectral projection. Then the difference equals \(\sum_{\lambda>0}[(P_\lambda)_{vv}-(P_\lambda)_{ww}]e^{-\lambda s}\). This formula follows directly by diagonalizing the symmetric matrix; no assumptions about an eigenbasis inside a repeated eigenspace are needed.

**2. Every connected graph through four vertices.** There is one connected graph on one vertex, one on two vertices, two on three vertices, and six on four vertices. The connected isomorphism types are \(K_1,K_2,P_3,K_3,K_{1,3},P_4\), the paw (triangle with one leaf), \(C_4\), the diamond (\(K_4\) with an edge deleted), and \(K_4\). In each, automorphisms act transitively on each degree class, so equal-degree vertices have equal \(E_v\). The complete list of differences \(H_{\ell,h}(s)\), defined as heat diagonal at degree \(\ell\) minus that at degree \(h>\ell\), is:

| Graph | Lower/higher degrees | Exact \(H_{\ell,h}(s)\) |
|---|---|---|
| \(P_3\) | \(1,2\) | \((q-q^3)/2\) |
| \(K_{1,3}\) | \(1,3\) | \(2(q-q^4)/3\) |
| \(P_4\) | \(1,2\) | \(\frac{\sqrt2}{4}(q^{2-\sqrt2}-q^{2+\sqrt2})\) |
| Paw | \(1,2\) | \((q-q^3)/2\) |
| Paw | \(1,3\) | \(2(q-q^4)/3\) |
| Paw | \(2,3\) | \((q+3q^3-4q^4)/6\) |
| Diamond | \(2,3\) | \((q^2-q^4)/2\) |

All entries are strictly positive for \(0<q<1\). For the paw \((2,3)\) entry, \(q+3q^3-4q^4=q(1-q)(1+q+4q^2)>0\). The remaining connected graph types are regular, giving equality everywhere. This proves that no graph with at most four vertices admits a reversal. The table is obtained by the projector formula \(P_\lambda=\prod_{\mu\ne\lambda}(L_G-\mu I)/(\lambda-\mu)\); the accompanying checker reproduces every table entry exactly, and the list of ten unlabeled connected types is established by elementary enumeration of adjacency subsets.

**3. Exact five-vertex witness.** Use the vertex order \((a,b,c,d,e)\). Its Laplacian is
\[
 L=\begin{pmatrix}
 3&-1&-1&-1&0\\
 -1&2&-1&0&0\\
 -1&-1&3&0&-1\\
 -1&0&0&1&0\\
 0&0&-1&0&1
 \end{pmatrix}.
\]
Its eigenvalues are \(0\), \(\alpha=(5-\sqrt{13})/2\), \(\beta=(5-\sqrt5)/2\), \(\gamma=(5+\sqrt5)/2\), and \(\delta=(5+\sqrt{13})/2\), strictly increasing as written. Direct substitution into the projector formula gives
\[
 F(s):=E_a(s/2)-E_b(s/2)
 = A e^{-\alpha s}-B e^{-\beta s}-C e^{-\gamma s}+D e^{-\delta s},
\]
with
\[
 A=\frac{13-3\sqrt{13}}{52},\qquad
 B=\frac{5+\sqrt5}{20},\qquad
 C=\frac{5-\sqrt5}{20},\qquad
 D=\frac{13+3\sqrt{13}}{52}.
\]
All four coefficients are positive. We have \(F(0)=0\), \(F'(0)=-1\), since the degrees of \(a,b\) are three and two respectively; and \(\lim_{s\to\infty}e^{\alpha s}F(s)=A>0\).

**4. Exactly one positive crossing.** Put \(g(s)=e^{\alpha s}F(s)\). Its derivative satisfies
\[
 e^{(\delta-\alpha)s}g'(s)
 =B(\beta-\alpha)e^{(\delta-\beta)s}
  +C(\gamma-\alpha)e^{(\delta-\gamma)s}
  -D(\delta-\alpha).
\]
The right-hand side is strictly increasing for \(s\ge0\), tends to infinity, and is negative at \(s=0\), because \(g'(0)=F'(0)=-1\). Thus \(g\) first strictly decreases, then strictly increases. Since \(g(0)=0\) and \(g(s)\to A>0\), it has precisely one positive simple zero \(s_*\). Therefore \(t_*=s_*/2\) is the unique positive crossing, with the asserted strict signs. High-precision root evaluation is merely a numerical representation of this uniquely defined constant. This completes the proof.

## Verification
Run `python verify.py` with Python 3, SymPy, NetworkX and mpmath. The checker reconstructs ten connected isomorphism types through four vertices from the standard graph atlas, computes exact Laplacian spectral projectors, checks all nontrivial pair formulas, reconstructs the bull polynomial in radicals, and numerically brackets the unique positive crossing. The universal size and uniqueness statements follow from the foregoing proof, not finite numerical scanning.

## Relationship to prior work
Li, Li and Li [1] analyze the synchronization Mpemba effect and Laplacian-mode crossing mechanisms in dissipatively coupled quantum van der Pol oscillators. Their network mode decomposition motivates the present question but does not assert this sharp unweighted-graph size threshold for *unit localized inputs*. The present dynamics is ordinary linear consensus, not the original quantum model. Chung [2] studies graph heat kernels and localized diffusion more broadly, including degree-normalized kernels and PageRank; it does not state the bull-graph degree-order reversal with an exact minimum size. General spectral expansions explain why mode weights can change rankings; they do not by themselves supply the finite-size obstruction and unique witness crossover established here.

## Limitations
The bound of five is specific to connected simple **unweighted** graphs, the **combinatorial** Laplacian, vertex impulses of equal amplitude, and the squared Euclidean consensus error. No such threshold is claimed for weighted, directed, degree-normalized, nonlinear, noisy, or quantum dynamics. The result identifies a minimum witness, not a classification of all larger graphs or of all possible crossing counts. Historical novelty is judged against the primary sources inspected and remains subject to independent literature review.

## References
[1] Yan Li, Wenlin Li, and Xingli Li, “Synchronization Mpemba Effect,” arXiv:2611.04994v1, first posted 2026-11-03, https://arxiv.org/abs/2611.04994 .

[2] Fan Chung, “The heat kernel as the pagerank of a graph,” *Proceedings of the National Academy of Sciences* **104** (2007), 19735–19740, https://doi.org/10.1073/pnas.0708838104 .

[3] S. Chatterjee, M. Takada, and H. Hayakawa, “Multiple quantum Mpemba effect: exceptional points and oscillations,” *Physical Review A* **110** (2024), 022213, https://doi.org/10.1103/PhysRevA.110.022213 .
