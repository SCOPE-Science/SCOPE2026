# Complete stay-operator design and a phase-independent convergence rate for a reducible qubit open quantum walk

## Finding
Fix two qubit Kraus operators \(L,R\in M_2(\mathbb C)\) with \(C=I-L^*L-R^*R\succeq0\). Suppose they have **exactly one common invariant ray** \(\mathbb Cv\), with \(\|v\|=1\), and the available stay probability on this ray is strictly positive: \(\beta=\langle v,Cv\rangle>0\). Write \(Lv=\ell v\), \(Rv=rv\). Relative to an orthonormal basis \((v,w)\), write
\[
L=\begin{pmatrix}\ell&u_L\\0&d_L\end{pmatrix},\quad R=\begin{pmatrix}r&u_R\\0&d_R\end{pmatrix},\quad C=\begin{pmatrix}\beta&c\\\overline c&t\end{pmatrix}.
\]
Put \(h=(t-|c|^2/\beta)^{1/2}\). **All** operators \(B\) satisfying both \(B^*B=C\) and \(Bv\in\mathbb Cv\) are, with arbitrary phases \(\theta,\varphi\in[0,2\pi)\),
\[
B_{\theta,\varphi}=\begin{pmatrix}\sqrt\beta e^{i\theta}&c\,e^{i\theta}/\sqrt\beta\\0&h e^{i\varphi}\end{pmatrix}.
\]
Every such \(B\) defines a lazy homogeneous nearest-neighbor open quantum walk on \(\mathbb Z\) whose auxiliary quantum channel \(\mathcal A(\rho)=L\rho L^*+B\rho B^*+R\rho R^*\) has the **unique** invariant density \(P_v=|v\rangle\langle v|\). Moreover, the same scalar
\[
\eta=1-|u_L|^2-|u_R|^2-|c|^2/\beta\in[0,1)
\]
is independent of both completion phases and satisfies, for every density matrix \(\rho\) and every integer \(n\ge0\),
\[
\langle w,\mathcal A^n(\rho)w\rangle=\eta^n\langle w,\rho w\rangle,\qquad \|\mathcal A^n(\rho)-P_v\|_1\le 2\eta^{n/2}\sqrt{\langle w,\rho w\rangle}.
\]
By the published ergodic lazy-walk recurrence criterion, **all** these completions are site recurrent (in the divergent expected-return-occupation sense) **if and only if** \(|\ell|=|r|\); if the magnitudes differ, they are site transient. Thus, for fixed \(L,R\) with a unique common eigenray, the entire family of ray-preserving stay completions is classified and explicitly constructible without solving nonlinear stationary-state equations.

## Assumptions and scope
Here \(C\succeq0\) is necessary for any completely positive trace-preserving stay completion. Having exactly one common invariant ray means \(v\) is an eigenvector of each of \(L,R\), but **no distinct complex one-dimensional subspace** is invariant under both. The strict condition \(\beta>0\) guarantees a genuine nonzero stay Kraus operator on \(v\) and permits a uniform two-phase parametrization. No normality, commutation, faithfulness of the invariant state, or invertibility of \(C\) is assumed. In the degenerate case \(h=0\), \(\varphi\) is a redundant phase; all operators are still covered. The recurrence convention is \(\sum_{n\ge0}\mathbb P_{0,\rho}(X_n=0)=\infty\) for every initial internal density \(\rho\), rather than a separate, unverified first-return-probability claim.

## Proof
Since \(C\succeq0\) and \(\beta>0\), the Schur complement gives \(t-|c|^2/\beta\ge0\). If \(Bv=bv\), its first column in the chosen basis is \((b,0)^T\). The equation \(B^*B=C\) forces \(|b|^2=\beta\), \(\overline b B_{12}=c\), and \(|B_{22}|^2=t-|c|^2/\beta\). Conversely these three equations suffice for \(B^*B=C\). They yield exactly the displayed family and prove Kraus completeness \(L^*L+B^*B+R^*R=I\).

All three Kraus operators are now upper triangular. Trace preservation on \(v\) gives \(|\ell|^2+|r|^2+\beta=1\); hence \(\mathcal A(P_v)=P_v\). Let \(q=\langle w,\rho w\rangle\). For each upper-triangular \(K\), the bottom-right entry of \(K\rho K^*\) is \(|K_{22}|^2q\). Thus \(q'=\eta q\) with \(\eta=|d_L|^2+|d_R|^2+h^2\). The bottom-right entry of Kraus completeness is \(1=|u_L|^2+|d_L|^2+|u_R|^2+|d_R|^2+|c|^2/\beta+h^2\), establishing the claimed formula for \(\eta\). If \(u_L=u_R=0\), the orthogonal ray \(\mathbb Cw\) would also be invariant under both \(L,R\), contrary to the unique-common-ray hypothesis. Hence \(0\le\eta<1\). Iteration proves the exact population identity.

For a qubit density \(\sigma\), its trace distance from the pure state \(P_v\) satisfies \(\|\sigma-P_v\|_1\le2\sqrt{1-\langle v,\sigma v\rangle}=2\sqrt{\langle w,\sigma w\rangle}\) (the pure-state fidelity/trace-distance inequality). This proves the exponential bound and uniqueness of the stationary density, even though the stationary density is rank one and the auxiliary map is reducible. The lazy-walk recurrence theorem of Loebens (2026), Theorem 3.8 (also Theorem 5.2 for qubit coins), applies because \(\mathcal A\) has a unique invariant density; its drift is \(\mathrm{Tr}(R P_vR^*)-\mathrm{Tr}(L P_vL^*)=|r|^2-|\ell|^2\). The theorem gives recurrence exactly when this drift vanishes, and transience otherwise.

## Verification
An exact-rational example uses
\[
L=\begin{pmatrix}1/4&1/4\\0&1/4\end{pmatrix},\quad R=\begin{pmatrix}1/4&0\\0&0\end{pmatrix},\quad v=(1,0)^T.
\]
These two matrices have only the first coordinate ray in common. In the above construction, \(\beta=7/8\), \(c=-1/16\), and \(h^2=195/224\). For every phase choice, \(\eta=209/224\). Both jump amplitudes on the invariant ray are \(1/4\), so all constructed walks are recurrent. The standalone script `verify.py` checks Kraus completeness and \(\eta=209/224\) symbolically, the stationary-ray population recurrence at exact small times, and 12 non-real completion phase pairs numerically. These finite checks corroborate, but do not replace, the symbolic proof for all admissible \(L,R\).

## Relationship to prior work
Newton Loebens, *Recurrence Criteria for Reducible Homogeneous Open Quantum Walks on the Line and on the Grid* (arXiv:2501.01249, earliest public submission 2025-01-02; later Quantum Information Processing 25, 157, 2026), establishes the drift-based recurrence criterion for lazy walks with a unique invariant density. Its Example 6.3 and the following discussion explicitly raise the problem of deciding whether a stay operator \(B\) can be selected for fixed jump operators \(L,R\), and say explicit constructions can be difficult. Here the new component is the **complete constructive description** of every completion preserving a unique common eigenray, together with a phase-independent exact contraction coefficient; the general drift theorem is imported, not re-proved or claimed original. The 2020 work of Jacq and Lardizabal addresses non-lazy walks and related recurrence/absorption properties, not this fixed-\(L,R\) lazy completion construction. Generic Kraus and polar-factor identities alone do not supply the combined recurrence classification and exact population-decay law without the special enclosure analysis.

## Limitations
This theorem treats two-dimensional internal coins with exactly one common jump-operator eigenray and positive \(\beta\), and only the subfamily of stay operators that preserve that ray. It does **not** classify all recurrent completions where \(B\) mixes the eigenray, nor arbitrary higher-dimensional jump operators or the boundary \(\beta=0\). The trace-norm bound concerns the auxiliary internal state, not a mixing bound for the position distribution; recurrent walks have unbounded spatial support. The published recurrence theorem is invoked for mean site occupation, not for probability-one eventual return. The simple polar-completion mechanism could be implicit in further quantum-channel literature; a bounded literature/database search does not establish global priority.

## References
1. N. Loebens, *Recurrence Criteria for Reducible Homogeneous Open Quantum Walks on the Line and on the Grid*, arXiv:2501.01249 (initial submission 2025-01-02), https://arxiv.org/html/2501.01249v4 ; Quantum Information Processing 25, 157 (2026), https://doi.org/10.1007/s11128-026-05180-7 .
2. T. S. Jacq and C. F. Lardizabal, *Homogeneous open quantum walks on the line: criteria for site recurrence and absorption*, arXiv:2010.03085 (2020), https://arxiv.org/abs/2010.03085 .
3. S. Attal, F. Petruccione, C. Sabot, and I. Sinayskiy, *Open quantum random walks*, Journal of Statistical Physics 147, 832–852 (2012), as referenced in Loebens, Section 1.
