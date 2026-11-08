# Exact dedicated-input controllability of Dutch windmill Laplacians below the zero-forcing threshold

## Finding
For every integer \(m\ge2\) and every integer \(\ell\ge3\), form the unweighted Dutch windmill \(D_{\ell}^{(m)}\) by identifying a single hub in \(m\) copies of the cycle \(C_{\ell}\). For the fixed combinatorial Laplacian \(L\), the minimal number of independent coordinate controls is
\[
\kappa(D_{\ell}^{(m)})=m.
\]
An optimal placement selects exactly one neighbor of the hub in each cycle, with either choice permitted independently for each cycle. Every minimum-cardinality controllable placement must choose exactly one nonhub vertex in each cycle, so **none is a zero-forcing set**. In contrast, the previously known classical zero-forcing number of this graph family is
\[
Z(D_{\ell}^{(m)})=m+1.
\]
The newly established assertion here concerns the fixed-Laplacian *dedicated-control optimum and all of its placements' zero-forcing failure*. The formula for \(Z\) itself is prior literature.

## Assumptions and scope
The graph is finite, simple, undirected, unweighted, with \(m\ge2\), \(\ell\ge3\) and vertex set
\[
V=\{v_0\}\cup\{v_{r,k}:1\le r\le m,\ 1\le k\le\ell-1\}.
\]
For each petal \(r\), its edges are \(v_0v_{r,1}\), \(v_{r,k}v_{r,k+1}\) for \(1\le k\le\ell-2\), and \(v_{r,\ell-1}v_0\). Put \(L=\operatorname{diag}(\deg)-A\). A set \(S\subseteq V\) provides one *independent* input at each chosen coordinate, so \(B_S\) consists of distinct standard-basis columns. The system is
\[
\dot z=-Lz+B_Su.
\]
No arbitrary edge weights, single broadcast input, structural-robust guarantee, or arbitrary distinct petal lengths are claimed. By the Popov–Belevitch–Hautus criterion for real symmetric \(L\), controllability is equivalent to the absence of a nonzero Laplacian eigenvector vanishing at all coordinates of \(S\).

## Proof
Write \(D\) for the \((\ell-1)\)-by-\((\ell-1)\) tridiagonal matrix with diagonal \(2\) and nearest-neighbor off-diagonal \(-1\), and let \(b=e_1+e_{\ell-1}\). The Laplacian has block form
\[
L=\begin{pmatrix}2m&-b^{\mathsf T}&\cdots&-b^{\mathsf T}\\-b&D&&0\\\vdots&&\ddots&\\-b&0&&D\end{pmatrix}.
\]
The Dirichlet eigenpairs of \(D\) are
\[
\mu_j=2-2\cos(j\pi/\ell),\qquad \phi_j(k)=\sin(jk\pi/\ell),\qquad 1\le j,k\le\ell-1.
\]
Here \(b^{\mathsf T}\phi_j=[1+(-1)^{j+1}]\sin(j\pi/\ell)\), which vanishes for even \(j\) and is nonzero for odd \(j\).

**Lower bound and placement necessity.** For \(j=2\), the vector supported on any one petal with interior coordinates \(\phi_2\) and zero elsewhere (including at the hub) is an eigenvector of \(L\) with eigenvalue \(\mu_2\), because \(b^{\mathsf T}\phi_2=0\). These \(m\) eigenvectors are independent and have pairwise disjoint nonhub supports. Thus a controllable coordinate set must meet each petal, giving \(|S|\ge m\). If \(|S|=m\), it contains exactly one nonhub vertex per petal and excludes the hub.

**Upper bound.** Set \(S=\{v_{r,1}:1\le r\le m\}\). Suppose \(Lf=\lambda f\) and \(f|_S=0\), writing \(h=f(v_0)\) and \(y_r=(f(v_{r,1}),\ldots,f(v_{r,\ell-1}))\). Then
\[
(D-\lambda I)y_r=bh,\qquad (2m-\lambda)h=\sum_{r=1}^m b^{\mathsf T}y_r.
\]
If \(h=0\), each petal vector is a \(D\)-eigenvector with its first coordinate zero, so the tridiagonal three-term recurrence forces \(y_r=0\). Hence any possible nonzero \(f\) has \(h\ne0\).

If \(\lambda=\mu_j\) for odd \(j\), taking inner product of the petal equation with \(\phi_j\) gives \(0=h\,b^{\mathsf T}\phi_j\ne0\), impossible. For even \(j\), let \(\theta=j\pi/\ell\), so \(\ell\theta\) is a multiple of \(2\pi\). The symmetric particular solution of the petal equation is \(y_r(k)=h\cos(k\theta)\); any other solution differs by a scalar multiple of \(\phi_j\), whose \(b\)-sum is zero. Therefore every petal satisfies
\[
b^{\mathsf T}y_r=2h\cos\theta=(2-\lambda)h.
\]
The hub equation then gives \((2m-\lambda)h=m(2-\lambda)h\), equivalently \((m-1)\lambda h=0\), which is impossible because \(m\ge2\), \(\lambda=\mu_j>0\), and \(h\ne0\).

Finally, if \(\lambda\notin\operatorname{spec}(D)\), all \(y_r=h(D-\lambda I)^{-1}b\) coincide. Reflection of the path interchanges the two ends and fixes \(b,D\), so every \(y_r\) is reflection-symmetric. Its first coordinate vanishes by the choice of \(S\), and therefore its last coordinate also vanishes. The hub equation implies \(\lambda=2m\). But deletion of the hub leaves \(m\) copies of \(D\), whose largest eigenvalue is \(2+2\cos(\pi/\ell)<4\). Cauchy interlacing shows that the second-largest eigenvalue of \(L\) is strictly below \(4\). The graph contains the star on its hub and \(2m\) neighbors, so adding nonnegative edge-Laplacians to the star gives \(\lambda_{\max}(L)\ge2m+1\). Because \(2m\ge4\) and \(2m<2m+1\), the number \(2m\) lies strictly between the largest and second-largest eigenvalues of \(L\), and cannot be an eigenvalue. Contradiction.

Thus every eigenvector zero on \(S\) vanishes identically. PBH proves controllability with exactly \(m\) inputs. Independently reflecting any cycle exchanges its two hub neighbors without changing \(L\), proving all \(2^m\) left/right neighbor placements controllable.

**Zero-forcing comparison.** A zero-forcing initial set with no vertex in some petal can never enter that petal: only the hub connects it to the others and the two uncolored neighbors of the hub in that petal prevent a first force. Therefore any zero-forcing set must meet all \(m\) petals. A set of only \(m\) seeds would consequently contain precisely one nonhub vertex per petal and no hub. Every seed has two uncolored neighbors, so the process cannot start. Conversely, the hub together with one adjacent neighbor in each petal forces successively along each cycle. Consequently \(Z=m+1\), also a previously published result, and every optimal \(m\)-coordinate control set is stalled.

## Verification
The standalone `verify.py` builds integer Laplacians and uses exact modular Krylov rank elimination for the proposed hub-neighbor placements on \(36\) parameter pairs (\(2\le m\le5\), \(3\le\ell\le11\)), with two independent primes. Every one of its \(72\) modular full-rank checks succeeds, which suffices for the sampled rational controllability assertions. It also checks forcing and performs \(776\) exhaustive low-cardinality forcing trials on seven small graphs. Running `python verify.py` prints `VERIFY_OK`.

These finite tests are **not** the proof of the universal quantifiers. The proof above uses a Dirichlet eigenspace lower bound, explicit Fredholm obstruction, reflection symmetry, and exact interlacing, valid for all integer parameters in scope.

## Relationship to prior work
Burgarth, D'Alessandro, Hogben, Severini and Young (arXiv:1111.1475, first posted 2011-11-07), §4, establish sufficient zero-forcing controllability criteria and explicitly note that converses can fail. Their result does not identify the dedicated-input minimum on Dutch windmill graphs.

Monshizadeh, Zhang and Camlibel (arXiv:1403.4868), §IV, characterize controllability for **all matrices** in a qualitative graph class via zero forcing. This stronger robustness quantifier differs from the present fixed, unit-weight Laplacian and hence does not imply equality of its minimal dedicated-input count with the zero-forcing number.

Eroh, Kang and Yi (arXiv:1207.6127, §3.2, Theorem 3.19, citing Chilakamarri–Dean–Kang–Yi) report the previously known \(Z=m+1\) for bouquets of arbitrary cycle lengths. No novelty is asserted for that formula. Their paper discusses zero forcing, metric dimension and **line graphs** of bouquets, not the fixed-Laplacian minimal coordinate-control placement of the bouquet itself.

Mousavi, Haeri and Mesbahi (arXiv:1802.03599) give modal controllability results on cographs. The Dutch windmill contains an induced four-vertex path when \(\ell\ge5\), so the full two-parameter family is not covered by that graph class. For \(\ell=3,4\), this source provides related general coverage, and those small-girth special cases are not the asserted novelty.

Li, Zhang and Wang (DOI:10.3934/math.2026685, June 2026) derive characteristic-polynomial factorizations for the exact Dutch windmill graph family. This is especially close at the **graph and spectrum** level and may yield the eigenvalue-multiplicity lower bound. However, a characteristic polynomial does not decide observability of a specified set of vertices, and the inspected paper focuses on spectra and graph energies rather than a PBH-optimal neighbor placement. The present control-location result adds that separate property.

## Limitations
Only fixed, unweighted, undirected combinatorial Laplacians and one independent input per controlled vertex are covered. Neither strong structural controllability under arbitrary edge weights nor an arbitrary collection of unequal cycle lengths is addressed. The zero-forcing formula itself is established prior knowledge. Available searches and inspected primary literature have not ruled out all differently named, unindexed, or later independently obtained control-location formulas. No independent mathematical audit has yet been conducted.

## References
1. D. Burgarth, D. D'Alessandro, L. Hogben, S. Severini, M. Young, *Zero forcing, linear and quantum controllability for systems evolving on networks*, arXiv:1111.1475 (first public 2011-11-07). https://arxiv.org/abs/1111.1475
2. N. Monshizadeh, S. Zhang, M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868 (2014). https://arxiv.org/abs/1403.4868
3. L. Eroh, C. X. Kang, E. Yi, *Metric Dimension and Zero Forcing Number of Two Families of Line Graphs*, arXiv:1207.6127, Theorem 3.19 (first posted 2012-07-25). https://arxiv.org/abs/1207.6127
4. K. B. Chilakamarri, N. Dean, C. X. Kang, E. Yi, *Iteration index of a zero forcing set in a graph*, Bulletin of the Institute of Combinatorics and its Applications 64 (2012), pp. 57–72, cited for the established bouquet zero-forcing count by [3].
5. S. S. Mousavi, M. Haeri, M. Mesbahi, *Laplacian Dynamics on Cographs: Controllability Analysis through Joins and Unions*, arXiv:1802.03599 (2018). https://arxiv.org/abs/1802.03599
6. W. Li, Y. Zhang, Y. Wang, *On the characteristic polynomials of Dutch windmill graphs and their applications*, AIMS Mathematics 11 (2026), 16697–16711. https://doi.org/10.3934/math.2026685
