# Exact endpoint-leader rank transfer through uniformly attached weighted paths

## Finding

Let \(H\) be a connected finite undirected weighted graph with \(n\ge2\) vertices, with all conductances strictly positive. Attach one identical weighted path of length \(\ell\ge1\) to each base vertex; the original base vertex is the depth-zero endpoint (root) of its path. The \(\ell\) fiber-edge weights \(t_1,\dots,t_\ell>0\) need not be equal to one another but are identical across all fibers. Denote the expanded rooted-product graph by \(G\).

For a set \(S\) of independently actuated nodes, assume that every actuator occupies the root (depth \(0\)) or the far tip (depth \(\ell\)) of a fiber. Write \(J\) for the set of base indices of fibers that contain an actuator. Then

\[
\boxed{\operatorname{rank}\mathcal C(-L_G,B_S)=(\ell+1)\operatorname{rank}\mathcal C(-L_H,B_J).}
\]

Here \(\mathcal C(A,B)=[B,AB,\ldots,A^{N-1}B]\) is the ordinary Kalman controllability matrix for an \(N\)-state system, and \(B_S\) consists of the coordinate vectors indexed by \(S\). Multiple actuators in one fiber are allowed; roots and tips may be mixed arbitrarily between fibers. In particular the expanded system is fully controllable exactly when the base is, and the minimum number of endpoint-localized independently actuated vertices equals the minimum leader number of the base.

For example, if the base is a weighted path and the control is placed at the far tip of the fiber rooted at one end of that base path, the entire enlarged graph is controllable by this single remote actuator, for every positive base-edge weight and every positive fiber-edge weight.

The endpoint assumption is essential: for the unit-weight base \(K_2\), with two unit-weight pendant edges in each fiber, one actuator at depth \(1\) in one fiber gives reachable dimension \(5\) on the six-vertex graph, whereas actuation at that fiber's root or tip gives dimension \(6\).

## Assumptions and scope

The matrix \(L_H\) is the combinatorial weighted Laplacian, so an undirected edge \(i\sim j\) of conductance \(w_{ij}>0\) contributes \(w_{ij}(e_i-e_j)(e_i-e_j)^\top\). All base edge weights can differ. All pendant paths have the same \(\ell\) ordered weights \(t_1,\ldots,t_\ell>0\), and their roots are connected to one another only along the edges of \(H\). In fiber-block order, with \(q=\ell+1\),

\[
L_G=L_H\otimes e_0e_0^\top+I_n\otimes Q,
\]

where \(Q\) is the weighted \(q\)-vertex path Laplacian with edge weights \(t_j\), and \(e_0\) is its root coordinate vector. Both matrices are real symmetric. Each input column of \(B_S\) controls a distinct vertex; no constraint links input signals. The assertion concerns exact rank in real arithmetic, not numerical condition numbers or the energy required to steer the system.

## Proof

**1. Fiber eigenvalue branches do not collide.** Let \(\theta\ge0\) run over distinct eigenvalues of \(L_H\), and put \(Q_\theta=Q+\theta e_0e_0^\top\). This is a real symmetric irreducible Jacobi (tridiagonal) matrix because each \(t_j\) is strictly positive. Its \(q\) eigenvalues are simple; call them \(\lambda_0(\theta)<\cdots<\lambda_\ell(\theta)\). No eigenvector of \(Q_\theta\) can have a zero root coordinate, as the first row and the recurrence down the path would force every coordinate to vanish. The same backwards recurrence proves its tip coordinate is nonzero.

Let \(\alpha_0<\cdots<\alpha_\ell\) be the eigenvalues of \(Q=Q_0\). Let \(\delta_0<\cdots<\delta_{\ell-1}\) be those of the principal submatrix obtained by deleting the root row and column. Irreducibility gives strict Cauchy interlacing,

\[
\alpha_0<\delta_0<\alpha_1<\cdots<\delta_{\ell-1}<\alpha_\ell.
\]

Rank-one positive semidefinite monotonicity and strict interlacing for \(Q_\theta\) yield, for every finite \(\theta\ge0\),

\[
\alpha_j\le\lambda_j(\theta)<\delta_j\quad(0\le j<\ell),
\qquad \lambda_\ell(\theta)\ge\alpha_\ell.
\]

Thus distinct branch indices \(j\) occupy disjoint spectral intervals. Within one branch, the Hellmann–Feynman identity gives

\[
\lambda_j'(\theta)=|u_{j,0}(\theta)|^2>0,
\]

where \(u_j(\theta)\) is a normalized eigenvector of \(Q_\theta\). Consequently \(\lambda_j(\theta)\) is different for different \(\theta\), including if eigenvalues of \(L_H\) themselves have multiplicity greater than one. Thus the expanded spectral eigenspaces are exactly the subspaces in Step 2, with no hidden collisions.

**2. Exact eigenspace decomposition.** Write \(E_\theta=\ker(L_H-\theta I_n)\). Tensor multiplication shows that for every \(x\in E_\theta\),

\[
L_G(x\otimes u_j(\theta))=\lambda_j(\theta)(x\otimes u_j(\theta)).
\]

These account for \(nq\) independent eigenvectors, and Step 1 proves that the complete eigenspace at \(\lambda_j(\theta)\) is precisely \(E_\theta\otimes\operatorname{span}\{u_j(\theta)\}\).

**3. Endpoint observation ranks equal base observation ranks.** A state \(x\otimes u_j(\theta)\) has value \(x_i u_{j,d}(\theta)\) at the depth-\(d\) node of the fiber rooted at base vertex \(i\). For \(d\in\{0,\ell\}\), the factor \(u_{j,d}(\theta)\) is nonzero by Step 1. Therefore, restricting vectors in this eigenspace to the independently actuated coordinates \(S\) has exactly the same rank as the restriction \(E_\theta\to\mathbb R^J\), even if root and tip of a single fiber are both selected.

**4. Controllability ranks.** For a real symmetric generator \(A\) with distinct eigenvalues indexed by \(\nu\) and eigenspaces \(E_\nu\), the spectral decomposition and Vandermonde interpolation give the exact identity

\[
\operatorname{rank}\mathcal C(A,B)=\sum_{\nu}\operatorname{rank}(B^\top|_{E_\nu}).
\]

This follows because the powers of \(A\) separate different eigenvalues while the reachable direction inside each eigenspace is exactly the orthogonal complement of \(\ker(B^\top|_{E_\nu})\). The signs of eigenvalues do not change these ranks. Applying this identity to \(-L_G\), followed by Steps 2–3, gives

\[
\begin{aligned}
\operatorname{rank}\mathcal C(-L_G,B_S)
 &=\sum_{\theta\in\operatorname{spec}(L_H)}\sum_{j=0}^{\ell}\operatorname{rank}(B_J^\top|_{E_\theta})\\
 &=(\ell+1)\operatorname{rank}\mathcal C(-L_H,B_J).
\end{aligned}
\]

A one-to-one choice of endpoint leader in each fiber indexed by a base leader set attains the same full-controllability status; conversely any endpoint leader set projects to a base leader set with cardinality no larger than its own. This proves the minimum-leader equality.

**5. Endpoint restriction is genuine.** With \(H=K_2\), \(\ell=2\) and all edge weights one, the base has eigenvalue \(\theta=0\) with eigenvector \((1,1)\), while \(Q\) has eigenvalue \(1\) with eigenvector \((1,0,-1)\). Their tensor product is invisible from either fiber's depth-one node. Hence one middle-node input cannot control all six states. Direct exact-rational Kalman elimination gives rank \(5\). An endpoint input gives rank \(3\times2=6\) by the proved theorem.

## Verification

The independent-of-proof arithmetic script `verify.py` uses Python's standard-library exact `fractions.Fraction` Gaussian elimination to build controllability matrices directly. It checks 925 cases/conditions across weighted base paths, cycles, and cliques with two to five base vertices, path fibers of lengths one through three, root-only/tip-only/mixed endpoint inputs, two inputs in one fiber, and the specific interior-node counterexample. Execute `python3 verify.py` in the directory containing this document and the script; the expected diagnostic is `VERIFY_OK 925`. These finitely many tests support reproducibility; the proof in the preceding section establishes the universal real-weight statement.

## Relationship to prior work

Parlangeli and Notarstefano, *On the reachability and observability of path and cycle graphs* (first arXiv release 2011-09-16, arXiv:1109.3556v1), analyze control locations for base paths and cycles, rather than rank transfer through uniformly attached weighted paths. Yazicioglu, Abbas, and Egerstedt, *A Tight Lower Bound on the Controllability of Networks with Multiple Leaders* (arXiv:1205.3058), give distance-based lower bounds for multi-input systems, not an exact multiplication formula for rooted products. Hsu, *Laplacian Controllability of Interconnected Graphs* (arXiv:1808.03022v1), Theorem 3.4, already establishes a root-input **single-input full-controllability equivalence** for composite graphs and provides the spectral tensor construction. The present claim is specifically the general **reachable-rank** formula for arbitrary many leaders, including mixed root/tip sensors, repeated base eigenspaces and arbitrary strictly positive weighted paths; no novelty is asserted for Hsu's earlier root-single-input equivalence. Shan and Liu, *Exploring Graphs with Distinct M-Eigenvalues* (arXiv:2412.18759v1), use a related rooted-product framework with a different all-ones-input notion of M-controllability.

## Limitations

The fiber must be identical in every cell and must be a positive-weight path. Actuators are restricted to its two endpoints: the explicit six-state counterexample shows the same formula need not hold at an interior vertex. Individual edge weights in the base may vary but all fibers share a fixed weight profile. Nothing is claimed about nonlinear control, heterogeneous fiber profiles, conditioning, minimum control energy, or dependent input channels. A full literature-universality claim is not made; general spectral tensor arguments may yield equivalent implications in related work, and the unavailable complete text of Liu and Ji's 2017 path/cycle network-controllability paper leaves a publication-priority risk.

## References

- G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, 2011-09-16. https://arxiv.org/pdf/1109.3556
- Y. Yazicioglu, W. Abbas, and M. Egerstedt, *A Tight Lower Bound on the Controllability of Networks with Multiple Leaders*, arXiv:1205.3058. https://arxiv.org/abs/1205.3058
- S.-P. Hsu, *Laplacian Controllability of Interconnected Graphs*, arXiv:1808.03022v1, Theorems 3.3–3.4, 2018. https://arxiv.org/pdf/1808.03022
- S. Shan and Y. Liu, *Exploring Graphs with Distinct M-Eigenvalues: Product Operation, Wronskian Vertices, and Controllability*, arXiv:2412.18759v1, 2024. https://arxiv.org/pdf/2412.18759
- [Access limitation] Y. Liu and Z. Ji, *Controllability of multiagent systems based on path and cycle graphs*, 2017; full article not available for material comparison in this review.
