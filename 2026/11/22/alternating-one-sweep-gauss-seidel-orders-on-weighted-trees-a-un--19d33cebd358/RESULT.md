# Alternating one-sweep Gauss–Seidel orders on weighted trees: a universal fourth-order penalty

## Finding

For every fixed finite connected tree with at least three vertices and strictly positive edge weights, the **unique optimal classes of one-sweep exact coordinate-descent permutations for sufficiently weak coupling** are precisely the two source–sink (bipartite) edge orientations. Each class includes all linear extensions of its orientation; different orders within a class attain the same exact expected objective risk for *every* coupling that keeps the Hessian positive definite.

The first asymptotic penalty of any other order is exactly twice the total weighted contribution from pairs of incident edges whose other endpoints are visited on opposite sides of their common vertex. It occurs at fourth order in the coupling, with a sixth-order remainder. On a path of \(n\) vertices there are exactly \(2E_n\) optimal orders in this regime, where \(E_n\) is the Euler zigzag number (for \(n=3,4,5,6\): \(4,10,32,122\)).

## Assumptions and scope

Let \(T=(V,E)\) be a finite simple connected tree, \(n=|V|\ge3\), with \(w_e>0\) for every \(e\in E\). Set \(W_{uv}=w_{\{u,v\}}\) on edges and zero otherwise. For \(\varepsilon>0\) with \(H_\varepsilon=I-\varepsilon W\) positive definite, consider \(f_\varepsilon(x)=\frac12x^{\mathsf T}H_\varepsilon x\). Start with any mean-zero random vector \(x^{(0)}\) with covariance \(I\). Fix a permutation \(\pi\) of \(V\) and minimize \(f_\varepsilon\) exactly along each coordinate once in that order. Define the **doubled risk**

\[
R_\pi(\varepsilon)=2\mathbb E f_\varepsilon(x^{(n)})=\mathbb E[(x^{(n)})^{\mathsf T}H_\varepsilon x^{(n)}].
\]

No Gaussian assumption is needed. For each vertex \(v\), let \(E_v^-\) be incident edges whose other endpoint precedes \(v\) in \(\pi\), and \(E_v^+\) those whose other endpoint follows it. Put

\[
M_\pi=\sum_{v\in V}\sum_{e\in E_v^-}\sum_{g\in E_v^+} w_e^2w_g^2.
\]

Let \(S_2=\sum_{e\in E}w_e^2\) and

\[
S_4=\sum_{e\in E}w_e^4+2\sum_{\{e,g\}:e\ne g,\ e\cap g\ne\varnothing}w_e^2w_g^2,
\]

where the latter sum is over **unordered** distinct incident edge pairs.

**Theorem.** For either bipartite source–sink ordering \(\rho\), and for every \(\varepsilon\) where \(H_\varepsilon\) is positive definite,

\[
R_\rho(\varepsilon)=\varepsilon^2S_2-\varepsilon^4S_4.
\]

For *every* permutation \(\pi\), as \(\varepsilon\downarrow0\),

\[
R_\pi(\varepsilon)-R_\rho(\varepsilon)
=2\varepsilon^4 M_\pi+O_{T,w,\pi}(\varepsilon^6).
\]

Moreover, \(M_\pi=0\) exactly when \(\pi\) is a linear extension of one of the two source–sink orientations. Since there are finitely many permutations and each non-source–sink order has \(M_\pi>0\), there is an \(\varepsilon_0(T,w)>0\) such that for all \(0<\varepsilon<\varepsilon_0\), with \(H_\varepsilon\) positive definite, **the complete set** of minimizers consists of the two source–sink linear-extension families.

## Proof

**1. Sweep and risk identity.** Relabel coordinates into their update order. Write \(L\) for the strict lower triangular part of \(\varepsilon W\). Thus \(H_\varepsilon=I-L-L^{\mathsf T}\), and the completed exact coordinate sweep has iteration matrix

\[
P=(I-L)^{-1}L^{\mathsf T}.
\]

The finite triangular inverse exists for all \(\varepsilon\). The identity

\[
H_\varepsilon=(I-L)^{\mathsf T}(I-L)-L^{\mathsf T}L
\]

and \((I-L)P=L^{\mathsf T}\) give, using the identity covariance,

\[
R_\pi=\operatorname{tr}(P^{\mathsf T}H_\varepsilon P)
=\lVert L\rVert_F^2-\lVert LP\rVert_F^2.
\]

This identity is exact and has no asymptotic approximation.

**2. Fourth-order coefficient.** Write \(L=\varepsilon N\), where \(N\) is a fixed strictly lower triangular oriented adjacency matrix. Nilpotence yields the finite expansion

\[
LP=\varepsilon^2NN^{\mathsf T}+\varepsilon^3N^2N^{\mathsf T}
+\varepsilon^4N^3N^{\mathsf T}+\cdots.
\]

A tree is bipartite, and multiplication by \(N\) reverses the vertex parity. Consequently \(NN^{\mathsf T}\) has nonzero entries only between vertices of the same color, while \(N^2N^{\mathsf T}\) has nonzero entries only between vertices of opposite colors. Their Frobenius inner product vanishes, ruling out the fifth-order term. Therefore

\[
R_\pi(\varepsilon)=\varepsilon^2 S_2-\varepsilon^4\lVert NN^{\mathsf T}\rVert_F^2+O_{T,w,\pi}(\varepsilon^6).
\]

**3. Exact wedge count.** The diagonal of \(NN^{\mathsf T}\) consists of sums of squared edge weights from neighbors visited earlier. Its squared Frobenius norm contributes each \(w_e^4\), plus twice \(w_e^2w_g^2\) for each pair of incident edges whose common vertex is visited later than both opposite endpoints. Distinct rows of \(NN^{\mathsf T}\) have at most one common predecessor on a tree (two such predecessors would form a cycle of length four). Their off-diagonal squared contributions add twice \(w_e^2w_g^2\) when the common vertex is visited earlier than both opposite endpoints. Every incident pair contributes in either of those cases except when its common vertex is strictly between the other endpoints in the update order. Thus

\[
\lVert NN^{\mathsf T}\rVert_F^2=S_4-2M_\pi,
\]

which establishes the fourth-order penalty and its coefficient.

**4. Exactly two zero-penalty orientations.** Because all weights are strictly positive, \(M_\pi=0\) if and only if, at every vertex of degree at least two, all its neighbors are either earlier or later. This means every vertex is a pure source or a pure sink of the oriented tree; leaves satisfy this automatically. A connected tree has a unique bipartition up to reversal, so the orientation must direct every edge from one part to the other, or the reverse. Conversely, every linear extension of either orientation has \(M_\pi=0\).

For either such orientation there can be no directed path of length two, hence \(N^2=0\). Therefore \(LP=\varepsilon^2NN^{\mathsf T}\) *exactly*, yielding the stated quartic formula at every admissible \(\varepsilon\). The two opposite orientations have the same \(S_4\). Each other order has strictly positive penalty coefficient. Finiteness of the permutation set gives a common positive \(\varepsilon_0(T,w)\), proving the complete small-coupling minimizer classification.

**5. Path-order count.** On a path, the source–sink property says that the position of each internal vertex is alternately larger and smaller than the positions of its two neighbors. The inverse visit-time permutation is thus alternating or reverse-alternating. Each class has \(E_n\) permutations, and the classes are disjoint for \(n\ge3\). This gives \(2E_n\).

## Verification

The standalone, standard-library-only `verification/verify.py` evaluates sweep matrices using exact rational arithmetic. Its embedded output records complete enumeration of 1590 permutations across weighted paths, stars and a branched tree of three through six vertices. It checks source–sink equality, strict separation for those finite examples at a specified coupling, and fourth-order coefficient consistency at smaller coupling. These finite checks support but do not prove the arbitrary-tree statement; the proof above supplies the infinite family argument.

Run: `python verification/verify.py` from the extracted package root.

## Relationship to prior work

Xiao, Xiao and Sun (arXiv:1910.04366, first public version 2019-10-10) analyze cyclic and symmetrized coordinate orders, primarily through worst-case convergence bounds and a dense equicorrelated counterexample. Gurbuzbalaban and coauthors (arXiv:1803.08200) study order/randomization rates for a permutation-invariant diagonal-dominance family. Neither inspected analysis provides the all-weighted-tree, *isotropic single-sweep objective*, sharp fourth-order mixed-wedge loss or complete source–sink optimizer classes proved here. Standard red–black Gauss–Seidel parallel scheduling was already known; the new statement is a risk optimality result, not the existence or parallelizability of coloring.

## Limitations

Only exact single-coordinate updates, one sweep, isotropic initial covariance, positive weights and sufficiently weak coupling are covered. The small-coupling threshold depends on the tree and weights and is not quantified explicitly. The quartic optimal-class risk remains an exact identity whenever the Hessian is positive definite, but no global ordering optimality is claimed outside the weak-coupling regime. The result concerns expected quadratic energy, not worst-case energy contraction, spectral radius, total wall-clock cost, non-tree graphs or multiple sweeps. Bibliographic priority is based on the sources inspected and can require independent verification.

## References

- P. Xiao, Z. Xiao and R. Sun, *Understanding Limitation of Two Symmetrized Orders by Worst-case Complexity*, arXiv:1910.04366, first version 2019-10-10, https://arxiv.org/abs/1910.04366 .
- M. Gurbuzbalaban, A. Ozdaglar, N. D. Vanli and S. J. Wright, *Randomness and Permutations in Coordinate Descent Methods*, arXiv:1803.08200 (2018), https://arxiv.org/abs/1803.08200 .
- C.-P. Lee and S. J. Wright, *Random Permutations Fix a Worst Case for Cyclic Coordinate Descent*, arXiv:1607.08320 (2016), https://arxiv.org/abs/1607.08320 .
- Cornell CS 5220 notes, *Stationary Iterations* (2020), section “Red-Black Gauss-Seidel”, https://www.cs.cornell.edu/courses/cs5220/2020fa/lec/2020-10-27-stationary.html .
