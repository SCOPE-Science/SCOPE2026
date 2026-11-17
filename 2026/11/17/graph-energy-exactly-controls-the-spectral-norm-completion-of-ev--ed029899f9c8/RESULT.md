# Graph energy exactly controls the spectral-norm completion of every edge-transitive graph

## Finding
For every finite undirected simple edge-transitive graph \(G\) with at least one edge, let \(A=A(G)\) denote its real adjacency matrix, \(m=|E(G)|\), and \(\mathcal E(G)=\operatorname{tr}|A|\) its graph energy. The minimum spectral norm of a Hermitian completion whose entries on every edge are fixed to one, with every non-edge and diagonal entry free, is
\[
\boxed{\delta(G)=\frac{2m}{\mathcal E(G)}.}
\]
A minimizer has an especially rigid form: set \(P_-=\mathbf1_{(-\infty,0)}(A)\) and
\[
\boxed{B_*=\delta(G)(I-2P_-),\qquad B_*^{2}=\delta(G)^2I.}
\]
Thus the graph energy provides an exactly computable best-completion invariant on the full symmetry class, with an optimal scalar orthogonal involution even when the zero-filled adjacency matrix is not optimal.

For the cycle graph \(C_n\), \(n\ge3\), put \(S_n=\sum_{k=0}^{n-1}|\cos(2\pi k/n)|\). Then
\[
\delta(C_n)=\frac n{S_n}=\frac\pi2+\begin{cases}
\frac{\pi^3}{6n^2}+O(n^{-4}), & n\equiv0\pmod4,\\
-\frac{\pi^3}{12n^2}+O(n^{-4}), & n\equiv2\pmod4,\\
-\frac{\pi^3}{48n^2}+O(n^{-4}), & n\text{ odd}.
\end{cases}
\]
Each asymptotic is along the indicated sequence of integers. In particular, the first correction changes sign with the cycle's congruence class.

## Assumptions and scope
The graph is finite, simple, undirected, and has \(m\ge1\) edges. Edge-transitivity means that for any two unordered edges some graph automorphism carries one onto the other; vertex-transitivity, connectivity and absence of isolated vertices are not required. Hermitian completion means \(B=B^*\in M_{|V(G)|}(\mathbb C)\), \(B_{ij}=1\) whenever \(\{i,j\}\in E(G)\). Since \(B\) is Hermitian, both ordered edge entries equal one. Diagonal entries may be arbitrary real numbers and non-edge entries arbitrary conjugate-symmetric complex numbers. No positivity constraint is imposed. The norm is the Hilbert-space operator/spectral norm, and graph energy is the sum of absolute adjacency eigenvalues (with algebraic multiplicities). The precise cycle expansion is for simple cycles \(n\ge3\).

## Proof
**Trace-norm lower certificate.** Since \(A\) is the zero-diagonal symmetric adjacency matrix, for every feasible Hermitian \(B\),
\[
\operatorname{tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=2m.
\]
The spectral/trace-norm duality inequality gives
\[
2m=|\operatorname{tr}(AB)|\le\|A\|_1\|B\|_{\mathrm{op}}=\mathcal E(G)\|B\|_{\mathrm{op}}.
\]
Because \(m>0\), the energy is positive. Therefore all feasible completions satisfy \(\|B\|_{\mathrm{op}}\ge2m/\mathcal E(G)\).

**Spectral-sign construction and edge uniformity.** Let \(P_-\) be the spectral projection of the real symmetric matrix \(A\) onto its strictly negative eigenspaces. Then \(U=I-2P_-\) is real symmetric, \(U^2=I\), and \(\|U\|_{\mathrm{op}}=1\). Every automorphism of \(G\), represented by a permutation matrix \(Q\), satisfies \(QAQ^{\mathsf T}=A\), and hence \(QUQ^{\mathsf T}=U\), by spectral functional calculus. Edge-transitivity implies that the real number \(U_{ij}\) is constant, say \(c\), on all unordered edges.

In an eigenbasis of \(A\), the eigenvalues of \(U\) equal \(-1\) on negative adjacency eigenvalues and \(+1\) on zero and positive eigenvalues. Accordingly,
\[
\operatorname{tr}(AU)=\sum_{j}\lambda_j(A)\bigl(1-2\mathbf1_{\{\lambda_j(A)<0\}}\bigr)=\sum_j|\lambda_j(A)|=\mathcal E(G).
\]
On the other hand, \(\operatorname{tr}(AU)=2mc\). Thus \(c=\mathcal E(G)/(2m)>0\). The scaled matrix \(B_*=(2m/\mathcal E(G))U\) has every edge entry equal to one, so it is feasible. It has norm exactly \(2m/\mathcal E(G)\) and its square is that scalar squared times \(I\). This attains the lower bound and proves the theorem, including the zero-eigenvalue and disconnected cases.

**Cycle formula.** For \(C_n\), the adjacency spectrum consists of \(2\cos(2\pi k/n)\) for \(0\le k<n\), with repetitions. There are \(n\) edges and \(\mathcal E(C_n)=2S_n\), whence \(\delta(C_n)=n/S_n\).

**Sharp arithmetic second-order term.** The absolutely convergent Fourier expansion is
\[
|\cos x|=\frac2\pi+\frac4\pi\sum_{r=1}^{\infty}\frac{(-1)^{r+1}}{4r^2-1}\cos(2rx).
\]
Set \(L=n/\gcd(n,2)\). Averaging this series over \(x=2\pi k/n\) uses the orthogonality of roots of unity: a term survives exactly when \(n\mid2r\), that is \(L\mid r\). Thus
\[
\frac{S_n}{n}=\frac2\pi+\frac4\pi\sum_{q=1}^{\infty}\frac{(-1)^{Lq+1}}{4L^2q^2-1}.
\]
Uniformly as \(L\to\infty\), the tail is
\[
\frac1{4L^2}\sum_{q=1}^{\infty}\frac{(-1)^{Lq+1}}{q^2}+O(L^{-4}),
\]
where the remainder is bounded by a convergent multiple of \(L^{-4}\sum q^{-4}\). For even \(L\), the series is \(-\pi^2/6\); for odd \(L\), it is \(+\pi^2/12\). Expanding the reciprocal gives \(\delta(C_n)=\pi/2+\pi^3/(24L^2)+O(L^{-4})\) for even \(L\), and \(\pi/2-\pi^3/(48L^2)+O(L^{-4})\) for odd \(L\). Distinguishing \(4\mid n\), \(n\equiv2\pmod4\), and odd \(n\) gives exactly the three asserted corrections.

## Verification
The mathematical proof above is independent of numerical enumeration. A standalone Python standard-library script (`CHECK.py`) verifies the cycle spectral-sign edge entry and involutory eigenvalue identities for 198 cycle sizes, checks three asymptotic branches at eight larger sizes against the predicted fourth-order error, and checks the complete-graph and complete-bipartite specializations in 49 and 529 cases. It prints a PASS line when all finite checks succeed. These probes do not certify arbitrary finite graphs; the universal result rests on the analytical trace-duality and edge-transitivity argument.

For the complete graph \(K_r\), \(r\ge2\), the formula yields \(\delta(K_r)=r/2\). For the complete bipartite graph \(K_{a,b}\), \(a,b\ge1\), it gives \(\delta(K_{a,b})=\sqrt{ab}\). Both agree with known special examples and are checks on the theorem's normalization.

## Relationship to prior work
Bottazzi and Varela, *Characterizations of minimal Hermitian completions via moments and subdifferentials* (2026), develop general norm-minimality criteria and prove that the zero-filled adjacency matrix of a connected graph is itself a minimum-norm completion if and only if the graph is complete bipartite (Section 6.1, Proposition 6.4). Their explicit examples compute the complete-graph constant and some small-graph instances. The present result asks for the **minimum value and an optimal completion even when the adjacency matrix is not minimal**, and obtains a graph-energy formula and a universal spectral-sign construction on every edge-transitive graph; it also yields cycle congruence-class asymptotics. The claimed new result is this explicit general classification, not spectral-norm duality or the previously known complete-graph/bipartite cases.

Faber, Liesen and Tichý (2025) provide a generic spectral-norm best-approximation framework; Bottazzi and Varela (2026, earlier) treat approximation relative to a \(C^*\)-subalgebra. Their general results are compatible with, but do not explicitly supply in the inspected material, this graph-energy identity or congruence asymptotic. Earlier graph-energy literature studies adjacency trace norms and energy changes rather than optimal Hermitian completion. An unindexed equivalent theorem could still exist and constitutes a bibliographic risk; a lack of search hits cannot prove novelty.

## Limitations
The exact formula depends on edge-transitivity. It is not claimed for graphs with multiple non-equivalent edge orbits, for independently weighted prescribed edges, for positive-semidefinite completions, or for constrained diagonal/non-edge entries. The construction establishes existence of one minimizer, not uniqueness or a classification of all minimizers. The asymptotics apply to simple cycles, not arbitrary graph sequences. No independent mathematical audit has yet been performed.

## References
1. T. Bottazzi and A. Varela, *Characterizations of minimal Hermitian completions via moments and subdifferentials*, arXiv:2611.10323v1 (first posted 6 November 2026), https://arxiv.org/html/2611.10323v1 .
2. V. Faber, J. Liesen and P. Tichý, *Matrix best approximation in the spectral norm*, arXiv:2506.09687 (first posted 11 June 2025), https://arxiv.org/abs/2506.09687 .
3. T. Bottazzi and A. Varela, *Best approximants relative to a \(C^*\)-subalgebra, joint numerical range and subdifferentials*, arXiv:2604.16041 (first posted 17 April 2026), https://arxiv.org/abs/2604.16041 .
4. J. Day and W. So, *Singular value inequality and graph energy change*, Electronic Journal of Linear Algebra 16 (2007), https://doi.org/10.13001/1081-3810.1202 .
