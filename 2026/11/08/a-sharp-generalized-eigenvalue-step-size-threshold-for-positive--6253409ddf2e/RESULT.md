# A sharp generalized-eigenvalue step-size threshold for positive-spectrum gradient tracking

## Finding

Let \(n\ge2\), let \(W\in\mathbb R^{n\times n}\) be a real symmetric doubly stochastic matrix with strictly positive eigenvalues and simple eigenvalue \(1\), and assume \(W\) is entrywise nonnegative. Let \(H=\operatorname{diag}(h_1,\ldots,h_n)\), with \(h_i>0\). For common constant step \(\alpha>0\), apply the distributed gradient-tracking update
\[
 x_{k+1}=W(x_k-\alpha y_k),\qquad
 y_{k+1}=Wy_k+H(x_{k+1}-x_k)
\]
to scalar local quadratic objectives \(f_i(u)=\tfrac12 h_i(u-b_i)^2\), initialized with \((y_0)_i=h_i((x_0)_i-b_i)\).

Write \(x_\star=\sum_i h_i b_i/\sum_i h_i\) and
\[
 \alpha_\star=\frac12\lambda_{\min}\!\left(H^{-1/2}(W^{-1}+2I+W)H^{-1/2}\right).
\]
Then **every** admissibly initialized trajectory converges geometrically to \(x_\star\mathbf1\) in its primal coordinates if and only if
\[
 \boxed{\ 0<\alpha<\alpha_\star\ }.
\]
At \(\alpha=\alpha_\star\) the error dynamics has an accessible multiplier \(-1\). Above it, the dynamics has a real accessible multiplier strictly below \(-1\), so some valid initial primal positions do not converge. No nonreal multiplier can cross the unit circle at positive stepsizes under these assumptions.

In particular, the sharp threshold is computable from one symmetric generalized eigenvalue problem for networks of arbitrary finite size, without requiring common local curvatures or a complete mixing graph.

## Assumptions and scope

All arithmetic is exact. The matrix \(W\) is fixed, symmetric, nonnegative, doubly stochastic and positive definite; the eigenvalue \(1\) is simple (e.g. a connected lazy undirected consensus network). Thus \(0<W\preceq I\). The local quadratics are scalar and strongly convex, their centers are arbitrary real numbers, and all nodes use the same positive step. The algorithm and gradient initialization are exactly as written; no stochastic gradient noise, delays, local step variation, or changing network weights are included. The theorem concerns universal convergence over all admissible primal initializations. Some specially chosen initializations may converge outside the stated range.

## Proof

**1. Centering and the invariant.** Put \(z_k=x_k-x_\star\mathbf1\). The algorithm is the linear recurrence
\[
 \begin{pmatrix}z_{k+1}\\y_{k+1}\end{pmatrix}
 =T_\alpha\begin{pmatrix}z_k\\y_k\end{pmatrix},\qquad
 T_\alpha=\begin{pmatrix}W&-\alpha W\\H(W-I)&W-\alpha HW\end{pmatrix}.
\]
Since \(\mathbf1^{\mathsf T}W=\mathbf1^{\mathsf T}\), the linear functional \(\mathbf1^{\mathsf T}(y-Hz)\) is preserved. Initially it is zero because \(\sum_i h_i(x_\star-b_i)=0\). Thus all initialized error states belong to the invariant codimension-one subspace
\[
 \mathcal S=\{(z,y):\mathbf1^{\mathsf T}y=\mathbf1^{\mathsf T}Hz\}.
\]

**2. Symmetric quadratic eigenvalue pencil.** For an eigenvalue \(\zeta\) of \(T_\alpha\) and a nonzero eigenvector \((z,y)\), invertibility of \(W\) implies \(z\ne0\) and
\[
 y=-\frac1\alpha W^{-1}(\zeta I-W)z,\qquad
 Q_\alpha(\zeta)z=0,
\]
where
\[
 Q_\alpha(\zeta)
 =\zeta^2W^{-1}+\zeta(\alpha H-2I)+W-\alpha H
 =(\zeta I-W)W^{-1}(\zeta I-W)+\alpha(\zeta-1)H.
\]
The converse is immediate. The point \(\zeta=1\) is always a root, because \(Q_\alpha(1)=(I-W)W^{-1}(I-W)\) has kernel \(\operatorname{span}\{\mathbf1\}\). It is a **simple** root when \(\alpha>0\): on a unit consensus vector \(v\), \(v^{\mathsf T}Q'_\alpha(1)v=\alpha v^{\mathsf T}Hv>0\); the remaining eigenvalues of \(Q_\alpha(1)\) are positive. Its eigenvector has \(y=0\) and \(z\propto\mathbf1\), hence does not lie in \(\mathcal S\). Every other eigenvector does lie in \(\mathcal S\), by invariance of the conserved functional.

**3. No nonreal unit-circle crossing.** Suppose \(|\zeta|=1\), \(\zeta=e^{it}\), and \(\sin t\ne0\). For a nonzero complex nullvector \(z\) set \(u=z^*W^{-1}z>0\), \(v_0=z^*z>0\), \(w=z^*Wz\), and \(h=z^*Hz>0\). The imaginary part of \(z^*Q_\alpha(\zeta)z=0\) gives
\[
 2u\cos t+\alpha h-2v_0=0.
\]
Substituting into the real part yields \(w-u-\alpha h=0\), impossible because \(0<W\preceq I\) implies \(w\le u\), and \(\alpha h>0\). Thus the only possible unit-circle root besides the permanent simple \(1\) is \(-1\).

**4. Starting stability.** At \(\alpha=0\), the two diagonal blocks of \(T_0\) equal \(W\). All eigenvalues different from \(1\) are strictly inside the unit disk. The double eigenvalue \(1\) is semisimple because \(W\mathbf1=\mathbf1\) and \(H(W-I)\mathbf1=0\). For small \(\alpha>0\), one copy stays exactly at \(1\), while the other is \(1-\alpha\bar h+O(\alpha^2)\), where \(\bar h=n^{-1}\sum_i h_i>0\). To verify the derivative directly, block-decompose \(Q_\alpha(\zeta)\) in the consensus/disagreement eigenbasis of \(W\), set \(\delta=\zeta-1\), and take the Schur complement of the positive disagreement block. The resulting scalar equation near \((\delta,\alpha)=(0,0)\) is
\[
 \delta\bigl[\delta+\alpha\bar h+O(\alpha^2|\delta|)\bigr]=0.
\]
Hence all nonpermanent eigenvalues lie strictly inside the disk for sufficiently small positive steps.

**5. The exact frontier.** Define \(C=W^{-1}+2I+W\). Then
\[
 Q_\alpha(-1)=C-2\alpha H.
\]
This matrix is positive definite exactly when \(0<\alpha<\alpha_\star\), singular at \(\alpha_\star\), and has a negative direction for every \(\alpha>\alpha_\star\). By continuity of polynomial eigenvalues, starting stability and Step 3, no nonpermanent eigenvalue can leave the open unit disk before \(\alpha_\star\). At the threshold, \(-1\) is a root. Above the threshold, the smallest eigenvalue of the real symmetric \(Q_\alpha(-1)\) is negative, whereas \(Q_\alpha(-R)\) is positive definite for all sufficiently large \(R>1\), since its leading coefficient is \(W^{-1}>0\). Continuity of the smallest eigenvalue gives a singular \(Q_\alpha(\zeta)\) for some real \(\zeta<-1\).

**6. Sharpness for legitimate initializations.** An eigenvalue \(\zeta\ne1\) cannot be invisible for every initialization \((z_0,y_0)=(z_0,Hz_0+g_\star)\), with fixed \(\mathbf1^{\mathsf T}g_\star=0\). Indeed, if a nonzero left eigenvector \((u^{\mathsf T},v^{\mathsf T})\) had \(u^{\mathsf T}+v^{\mathsf T}H=0\), its first left-eigenvector equation would reduce to \((1-\zeta)v^{\mathsf T}H=0\), a contradiction. Some choice of \(z_0\) therefore has nonzero projection on the left eigenvector. A state multiplier \(-1\), or one of modulus greater than one, rules out convergence of the error state to zero for that choice. If \(z_k\to0\), however, the tracker satisfies \(y_{k+1}=Wy_k+H(z_{k+1}-z_k)\), with a vanishing input, contracting disagreement dynamics and consensus component \(\mathbf1^{\mathsf T}y_k=\mathbf1^{\mathsf T}Hz_k\to0\); hence \(y_k\to0\). Therefore the nonconvergent state implies nonconvergent primal iterates, proving both directions of the theorem.

**Exact two-agent certificate.** Take
\[
 W=\begin{pmatrix}3/4&1/4\\1/4&3/4\end{pmatrix},\quad
 H=\operatorname{diag}(7/6,5/6).
\]
Then \(\alpha_\star=9/5\), \(\det(C-18H/5)=0\), and at this threshold
\[
 \det(\zeta I-T_{9/5})
 =(\zeta-1)(\zeta+1)(40\zeta^2-12\zeta-19)/40.
\]
The remaining two roots are \((3\pm\sqrt{199})/20\), both in the open unit disk. This illustrates that the first loss of stability is a real flip rather than a complex-pair crossing.

## Verification

The accompanying `verify.py` uses exact symbolic rational algebra to establish the displayed two-agent characteristic factorization and the threshold pencil's singularity. It also checks a further 168 independently generated connected positive-spectrum consensus networks of sizes \(2\) through \(8\), each with heterogeneous diagonal curvatures, at subcritical, critical, and supercritical steps. Running `python verify.py` with NumPy and SymPy produces the expected PASS messages. Those finite diagnostics corroborate but do not replace the all-network proof.

## Relationship to prior work

Wang, Ballotta, Carli, Iannelli, Cao and Schenato (2026) study precisely this common-step quadratic gradient-tracking recurrence, derive practical bounds from spectral radius and curvature dispersion, and identify exact rate optimization in the complete-graph and homogeneous-curvature regimes. Their general certificate is sufficient rather than an exact heterogeneous fixed-network stability frontier. The present theorem instead assumes positive spectrum and computes the exact fixed-network upper stable step from a symmetric generalized eigenvalue problem; it does not give a decentralized tuning formula or the optimal contraction rate. A published homogeneous sign-aware graph tuning result addresses optimal rates when all curvatures agree, rather than the noncommuting \(W,H\) stability ceiling here. Earlier control-oriented quadratic gradient-tracking work uses invariant-subspace and stabilizing-gain methods, but available abstracts do not settle this specific exact eigenvalue identity.

## Limitations

Positive definiteness of \(W\) is essential to the inverse-based proof and to the exclusion of complex unit-circle crossings; networks with negative eigenvalues need not have this frontier. Singular positive-semidefinite \(W\), node-dependent stepsizes, dynamic mixing, nonlinear objectives, and perturbations are not treated. The theorem is an exact-arithmetic asymptotic stability result and does not bound transient amplification, optimize convergence speed, or certify a distributed online step selection. Literature searches and partial access do not prove unique historical priority; the 2019–2020 control-oriented quadratic gradient-tracking literature remains a possible source of an equivalent formulation.

## References

1. Y. Wang, L. Ballotta, R. Carli, A. Iannelli, X. Cao and L. Schenato, *Adaptive Stepsizes With Certified Convergence in Distributed Gradient Tracking With Quadratic Costs*, arXiv:2608.03548v1 (first public 2026-08-04), https://arxiv.org/abs/2608.03548.
2. M. Bin, I. Notarnicola, L. Marconi and G. Notarstefano, *A System Theoretical Perspective to Gradient-Tracking Algorithms for Distributed Quadratic Optimization*, arXiv:1911.06665, https://arxiv.org/abs/1911.06665.
3. G. Carnevale, M. Bin, I. Notarnicola, L. Marconi and G. Notarstefano, *Enhanced Gradient Tracking Algorithms for Distributed Quadratic Optimization via Sparse Gain Design*, IFAC-PapersOnLine 53(2) (2020), 2696–2701, https://doi.org/10.1016/j.ifacol.2020.12.405.
4. *Exact sign-aware graph-specific tuning for homogeneous distributed gradient tracking*, publicly indexed mathematical research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-sign-aware-graph-specific-tuning-for-homogeneous-distribut--4bef30512fd6.
