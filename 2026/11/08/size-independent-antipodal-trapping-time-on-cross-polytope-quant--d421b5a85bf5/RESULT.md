# Size-independent antipodal trapping time on cross-polytope quantum networks

## Finding
For every integer \(n\ge2\), let \(G_n=K_{2n}\setminus M_n\), with \(M_n\) a perfect matching, and let \(a,b\) be the two endpoints of one deleted edge. Consider the loss-only, one-excitation continuous-time quantum dynamics
\[
\dot\psi(t)=\left(-iJ A(G_n)-\frac{\kappa}{2}|a\rangle\langle a|\right)\psi(t),\qquad \psi(0)=|b\rangle,
\]
with \(J>0\), \(\kappa>0\), and \(\hbar=1\). The absorption probability is exactly one, although \(a\) and \(b\) are nonadjacent. Writing \(m=2n-2\), the mean absorption time is
\[
\boxed{\mathbb E[T_{n}]=\frac{3}{\kappa}+\frac{\kappa}{4J^2}\left(1-\frac2m+\frac4{m^2}\right).}
\]
Consequently \(\lim_{n\to\infty}\mathbb E[T_n]=3/\kappa+\kappa/(4J^2)\): the mean absorption time remains bounded as the network size grows. Its unique optimal positive absorption rate and corresponding minimum time are
\[
\kappa_*(n)=\frac{2\sqrt3 J}{\sqrt{1-2/m+4/m^2}},\qquad
\min_{\kappa>0}\mathbb E[T_n]=\frac{\sqrt{3(1-2/m+4/m^2)}}{J}.
\]
For comparison, if the excitation instead starts at any vertex \(c\) adjacent to \(a\), its eventual absorption probability is exactly \(1/m\). This latter capture-efficiency statement is a consequence of existing graph-subspace methods and is stated for physical comparison, not as a separately novel theorem.

## Assumptions and scope
The graph is the \(1\)-skeleton of the \(n\)-dimensional cross-polytope. Each of its \(2n\) vertices has exactly one nonneighbor distinct from itself. Edge hopping is homogeneous, real and nonzero. There is only one local irreversible absorber; no other decay, site disorder, dephasing, resetting, interactions or other trap is present. The jump-loss convention is \(\kappa\langle a|\rho|a\rangle\) for the instantaneous absorption density. All statements concern finite \(n\) before the stated size limit.

## Proof
Let \(C=V(G_n)\setminus\{a,b\}\), so \(|C|=m=2n-2\), and set \(|s\rangle=m^{-1/2}\sum_{v\in C}|v\rangle\). The orthogonal subspace \(\mathcal B=\operatorname{span}\{|a\rangle,|b\rangle,|s\rangle\}\) is invariant under the adjacency Hamiltonian. In the displayed ordered orthonormal basis, its Hamiltonian is
\[
H_{\mathcal B}=J\begin{pmatrix}0&0&\sqrt m\\0&0&\sqrt m\\\sqrt m&\sqrt m&m-2\end{pmatrix}.
\]
The complement of \(\mathcal B\) lies in the orthogonal complement of \(|a\rangle\), and is invariant under both \(H\) and the loss dynamics. Therefore it is dark. The initial state \(|b\rangle\) lies entirely in \(\mathcal B\); a vertex \(|c\rangle\) in \(C\) has squared projection \(\|P_{\mathcal B}|c\rangle\|^2=1/m\).

The three eigenvalues of \(H_{\mathcal B}\) are \(0,-2J,(2n-2)J\), which are distinct for every \(n\ge2\). None of their eigenvectors has zero \(a\)-component: a vector \((0,y,z)\) with \(H_{\mathcal B}(0,y,z)^T\) having zero first component must have \(z=0\), after which its third component forces \(y=0\). Thus the loss generator \(B=-iH_{\mathcal B}-(\kappa/2)|a\rangle\langle a|\) has all eigenvalues strictly in the left half-plane. Indeed for an eigenvector \(v\), \(2\operatorname{Re}\lambda\|v\|^2=-\kappa |v_a|^2<0\). It follows that \(\|e^{Bt}|b\rangle\|\to0\), so absorption occurs with probability one.

For the integrated unnormalized state \(X=\int_0^\infty e^{Bt}|b\rangle\langle b|e^{B^\dagger t}\,dt\), integration of its derivative gives the unique Lyapunov equation
\[
BX+XB^\dagger=-|b\rangle\langle b|.
\]
An explicit Hermitian solution in the \((a,b,s)\) basis is
\[
X=\begin{pmatrix}
1/\kappa&ip&iq\\
-ip&1/\kappa+\kappa(m^2-3m+4)/(4J^2m^2)&z+ir\\
-iq&z-ir&1/\kappa+\kappa/(4J^2m)
\end{pmatrix},
\]
where
\[
p=\frac{m-2}{2Jm},\quad q=-\frac1{2J\sqrt m},\quad r=\frac1{2J\sqrt m},\quad
z=-\frac{\kappa(m-2)}{4J^2m^{3/2}}.
\]
Direct multiplication verifies the equation exactly; the included checker repeats this symbolically. Since survival is \(S(t)=\|e^{Bt}|b\rangle\|^2\) and eventual absorption is certain, the layer-cake identity gives \(\mathbb E[T_n]=\int_0^\infty S(t)\,dt=\operatorname{tr}X\). Summing the displayed diagonal entries gives the boxed formula. Elementary differentiation in \(\kappa\), with \(1-2/m+4/m^2>0\), gives the unique minimizer and minimum. The projection argument gives capture probability \(1/m\) from each adjacent vertex, independently of the absorber's positive strength.

## Verification
Run `python check_exact.py` with Python, SymPy, NumPy and SciPy. The checker verifies the exact symbolic Lyapunov identity, reconstructs every graph adjacency independently for \(2\le n\le12\), verifies the invariant three-dimensional subspace, and compares the predicted mean absorption time against independent numerical Lyapunov solves for three distinct pairs of coupling and loss parameters at each size. All tests passed. The finite tests are supplementary; the proof uses exact algebra for arbitrary \(n\ge2\).

## Relationship to prior work
Rebentrost et al. (2008, arXiv:0807.0929) motivated quantum energy transport with traps and environmental effects, but their studied systems are photosynthetic complexes and disordered trees rather than this loss-only cross-polytope. Razzoli, Paris and Bordone (2020, arXiv:2011.13794) established the general trapping-subspace viewpoint and analyzed various network families including strongly regular graphs; that viewpoint covers the capture-efficiency projection and is not claimed to be new here. Their reported graph study considers trapping efficiencies, not the explicit mean time and optimal absorption rate displayed above. Alterman, Berman and Strauch (2023, arXiv:2309.00164) provide mean transfer times on the fully connected graph, with no deleted matching; their exact formulas cannot be substituted into the present graph's Hamiltonian. The new object-specific result is the exact unconditional mean absorption time from the deleted-edge partner, including its size limit and optimal absorber strength.

## Limitations
The time formula assumes coherent homogeneous hopping and a single rank-one absorber. It does not describe dephasing, distributed loss, thermal dynamics, arbitrary initial superpositions, or graph perturbations. It establishes an explicit finite-network identity and not a general all-graph bound. Historical priority has not been independently certified; the accessible literature and research-index comparisons do not establish another identical formula.

## References
1. P. Rebentrost, M. Mohseni, I. Kassal, S. Lloyd and A. Aspuru-Guzik, *Environment-Assisted Quantum Transport*, arXiv:0807.0929, first submitted 2008-07-07. https://arxiv.org/abs/0807.0929
2. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, arXiv:2011.13794, first submitted 2020-11-27. https://arxiv.org/abs/2011.13794
3. S. Alterman, J. Berman and F. W. Strauch, *Optimal Conditions for Environment-Assisted Quantum Transport on the Fully Connected Network*, arXiv:2309.00164, first submitted 2023-08-31. https://arxiv.org/abs/2309.00164
