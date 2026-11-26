# Universal two-sector equilibration under dynamical bond percolation

## Finding
Let \(G=(V,E)\) be any connected undirected simple graph, \(n=|V|\ge2\). At successive intervals of length \(\tau>0\), independently retain each edge \(e\) with probability \(p_e\in(0,1)\), choose the Laplacian \(L_B\) of the retained edge set \(B\), and act on density operators by \(\rho\mapsto U_B\rho U_B^*\), with \(U_B=\exp(-i\tau L_B)\). Average over the independent fresh configurations. For every \(\tau\notin\pi\mathbb Z\), the resulting channel \(\Phi_\tau\) has an exact, graph-independent long-time limit:

\[
\lim_{k\to\infty}\Phi_\tau^k(\rho)
 =wP+\frac{1-w}{n-1}(I-P),\qquad
 P=|s\rangle\langle s|,\quad
 |s\rangle=\frac1{\sqrt n}\sum_{v\in V}|v\rangle,\quad
 w=\operatorname{tr}(P\rho).
\]

The convergence is in every finite-dimensional matrix norm, including trace norm. The only fixed operators form \(\operatorname{span}\{P,I-P\}\), and the only peripheral eigenvalue is \(1\). For all initial states, every limiting position probability is exactly \(1/n\). Yet the limiting off-diagonal density entries are \((nw-1)/(n(n-1))\), and the limiting purity is \(w^2+(1-w)^2/(n-1)\). A position-localized input has \(w=1/n\) and tends to \(I/n\), whereas the coherent uniform input \(P\) remains pure. The exclusion \(\tau\notin\pi\mathbb Z\) is sharp uniformly over connected graphs: for the graph of one edge and \(\tau\in\pi\mathbb Z\), every possible one-step unitary is identity, so arbitrary coherences remain.

## Assumptions and scope
All graphs are finite, connected, undirected and simple, including the two-vertex graph. The Hilbert space is \(\mathbb C^V\) with vertex basis. Put \(f_e=|u\rangle-|v\rangle\) for \(e=\{u,v\}\), and \(E_e=f_ef_e^*\); then \(L_B=\sum_{e\in B}E_e\), and \(E_e\) has eigenvalues \(0\) and \(2\). At each discrete interval, all edge indicators are sampled independently of one another and of previous intervals, with probabilities strictly inside \((0,1)\). The time evolution is unitary for each realization; the theorem concerns its ensemble-averaged channel \(\Phi_\tau(X)=\sum_{B\subseteq E}q_B U_B XU_B^*\), where \(q_B>0\) for every \(B\). It does not assert that individual quantum trajectories converge. The Laplacian convention, including its changing diagonal, is essential: adjacency-only or fixed-diagonal noise is a different model.

## Proof
**1. All peripheral eigenoperators must commute with every configuration.** Let \(\Phi_\tau(X)=zX\) and \(|z|=1\), with \(X\ne0\). Unitary conjugation preserves Hilbert–Schmidt norm. Direct expansion yields
\[
\sum_{B\subseteq E}q_B\|U_B XU_B^*-zX\|_2^2
=2\|X\|_2^2-2\operatorname{Re}\langle zX,\Phi_\tau(X)\rangle_2=0.
\]
Every summand is nonnegative and \(q_B>0\), hence every \(U_BXU_B^*=zX\). The empty-edge configuration has \(U_\varnothing=I\), so \(z=1\). Therefore the only possible unit-modulus eigenvalue is \(1\); moreover \(X\) is fixed if and only if it commutes with every \(U_B\).

**2. Singleton configurations force a connected-edge commutant.** For a one-edge configuration \(\{e\}\), the rank-one orthogonal projector \(Q_e=E_e/2\) gives
\[
U_{\{e\}}=I+(e^{-2i\tau}-1)Q_e.
\]
If \(\tau\notin\pi\mathbb Z\), the scalar coefficient is nonzero, so commuting with \(U_{\{e\}}\) is equivalent to commuting with \(Q_e\) or \(E_e\). If \(XQ_e=Q_eX\), then \(Xf_e=a_ef_e\) and \(f_e^*X=a_ef_e^*\), with the same scalar \(a_e\). Whenever two distinct graph edges share a vertex, \(f_e^*f_h\ne0\) (up to arbitrary orientation), and
\[
a_e(f_e^*f_h)=f_e^*Xf_h=a_h(f_e^*f_h),\]
so \(a_e=a_h\). The line graph of every connected graph with at least one edge is connected. Thus all \(a_e\) share one scalar \(a\). The edge-difference vectors span the codimension-one subspace \(s^\perp\); therefore \(X\) acts as \(aI\) on \(s^\perp\). Since each edge projector commutes with \(X\), and the intersection of their kernels is precisely \(\operatorname{span}\{s\}\), the vector \(s\) is also an eigenvector of \(X\), say with eigenvalue \(b\). Consequently
\[X=bP+a(I-P).\]
Conversely every such \(X\) commutes with all \(L_B\), since \(L_Bs=0\). So the fixed-operator space is precisely \(\operatorname{span}\{P,I-P\}\).

**3. Convergence and the exact projection.** \(\Phi_\tau\) is a contraction in Hilbert–Schmidt norm by convexity of unitary conjugations. Hence its matrix representation has no nontrivial Jordan block at an eigenvalue of modulus one: otherwise its powers would have unbounded norm. By step 1, all remaining eigenvalues are strictly inside the unit disk, so \(\Phi_\tau^k\) converges to its spectral projection onto the fixed space. For every \(B\), both \(P\) and \(I-P\) commute with \(U_B\); in particular \(\operatorname{tr}(P\Phi_\tau(X))=\operatorname{tr}(PX)\) and \(\operatorname{tr}((I-P)\Phi_\tau(X))=\operatorname{tr}((I-P)X)\). These two conserved traces uniquely identify the limiting fixed operator as
\[
\operatorname{tr}(P\rho)P+\frac{\operatorname{tr}((I-P)\rho)}{n-1}(I-P).
\]
Every diagonal of \(P\) equals \(1/n\), proving uniform limiting position statistics. Each off-diagonal of \(P\) equals \(1/n\), yielding the displayed coherent residual. Orthogonality of \(P\) and \(I-P\) gives the purity formula.

**4. Sharp graph-uniform resonance.** On the graph of two vertices joined by one edge, the only nonempty-configuration Laplacian is \(E_e\), with nonzero eigenvalue \(2\). For \(\tau=m\pi\), \(\exp(-i\tau E_e)=I\), so the averaged channel is identity. A localized input stays localized instead of approaching \(I/2\). Thus no theorem valid for every connected graph can retain those excluded switching intervals.

## Verification
The included independent numerical **consistency checker** `verify_percolation.py` enumerates all bond configurations for connected paths, cycles, and the complete graph of up to four vertices. It compares 650 channel iterations with the closed-form limiting density for a nonuniform complex coherent initial state, and verifies the two-vertex resonance at \(\tau=\pi\). Numerical checks do not prove the infinite-time claim; the four analytic steps above do. The test uses \(\tau=0.7\), edge-retention \(p=0.39\), and SciPy/NumPy; every reported matrix norm discrepancy is less than \(5\times10^{-14}\).

## Relationship to prior work
Darázs and Kiss, *Time evolution of continuous-time quantum walks on dynamical percolation graphs* (first arXiv release 15 November 2012, arXiv:1211.3550), introduced the percolated-Laplacian model, rigorously obtained time rescaling in the fast-switching limit, and reported numerical flattening of finite-step position probabilities over long times. The present statement instead treats the **fixed, nonresonant switching interval**, proves the full density-operator limit uniformly over every connected finite graph and edge-dependent retention profile, and distinguishes flat position statistics from surviving global coherence.

Kollár et al., *Discrete time quantum walks on percolation graphs* (arXiv:1404.4509), developed the general random-unitary attractor formalism and conditional projector-plus-mixed-sector limits for **coined discrete-time quantum walks**. That formalism suggests the method but does not identify the complete fixed algebra for all connected continuous-time Laplacian percolation graphs nor the sharp graph-uniform resonant intervals. Benedetti, Rossi and Paris (arXiv:1812.06676) reviewed related classical random-telegraph tunnelling fluctuations; their Hamiltonian typically holds the diagonal degree term fixed, unlike the independently resampled subgraph Laplacian here. Bressanini, Benedetti and Paris (2022) analyzed intrinsic dephasing and site-dephasing Lindblad models, not this finite-interval random-unitary channel. These comparisons do not constitute an exhaustive literature-priority guarantee.

## Limitations
The result concerns an ensemble average over freshly resampled independent bond sets at every interval; it does not claim almost-sure wave-function equilibration, quantitative spectral-gap bounds, or treatment of correlated bond noise, directed/weighted edges, changing diagonal outside the Laplacian convention, disconnected graphs, or every exceptional interval for an individual fixed graph. At \(\tau=m\pi\), some graphs might nevertheless mix; only a graph-uniform counterexample is proved. The result is a self-review analytical review, not an independent verification. The general attractor framework may have unlocated applications implying parts of the theorem; originality remains subject to further primary-literature comparison.

## References
1. Z. Darázs and T. Kiss, *Time evolution of continuous-time quantum walks on dynamical percolation graphs*, arXiv:1211.3550 (first submitted 2012-11-15), https://arxiv.org/pdf/1211.3550 .
2. B. Kollár, J. Novotný, T. Kiss and I. Jex, *Discrete time quantum walks on percolation graphs*, arXiv:1404.4509 (first submitted 2014-04-17), https://arxiv.org/pdf/1404.4509 .
3. C. Benedetti, M. A. C. Rossi and M. G. A. Paris, *Continuous-time quantum walks on dynamical percolation graphs*, arXiv:1812.06676 (2018), https://arxiv.org/html/1812.06676v1 .
4. G. Bressanini, C. Benedetti and M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, Quantum Information Processing 21, 317 (2022), https://doi.org/10.1007/s11128-022-03647-x .
