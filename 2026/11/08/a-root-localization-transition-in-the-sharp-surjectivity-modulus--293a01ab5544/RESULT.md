# A root-localization transition in the sharp surjectivity modulus of a tree shift

## Finding
Let \(\mathcal T\) be the rooted tree in which the root has exactly one child and every other vertex has exactly four children. On \(H=\ell^2(V(\mathcal T);\mathbb C)\), let \(Se_v=e_{\mathrm{par}(v)}\) for nonroot vertices, and \(Se_{\mathrm{root}}=0\). For \(\lambda\in\mathbb C\), let
\[
\gamma(\lambda)=\inf_{\|f\|=1}\|(S^*-\overline\lambda I)f\|.
\]
Putting \(r=|\lambda|\), the **exact global formula** is
\[
\boxed{\gamma(\lambda)=\begin{cases}
\sqrt{\frac12+r^2+\frac12\sqrt{1-\frac43r^2}},&0\le r<\frac67,\\
|2-r|,&r\ge\frac67.
\end{cases}}
\]
For \(0\le r<2\), the operator \(S-\lambda I\) is onto, and its sharp bounded-right-inverse norm is \(\gamma(\lambda)^{-1}\); equivalently the supremal radius of a ball contained in \((S-\lambda I)\) of the open unit ball is \(\gamma(\lambda)\). At \(r=2\) it is not onto; at \(r>2\) it is invertible and its inverse norm is \((r-2)^{-1}\). The root-localized minimizing singular vector exists precisely when \(0\le r<6/7\); at \(6/7\) the defect eigenvalue merges into the bulk continuum. The modulus is nonmonotone inside the universal disk: it increases from \(\gamma(0)=1\) to the unique maximum \(2/\sqrt3\) at \(r=\sqrt{2/3}\), then decreases to zero at \(r=2\).

## Assumptions and scope
The tree is countably infinite, leafless and bounded-degree. Its root has degree one toward descendants, while every vertex at depth at least one has four children. The shift is the **unweighted backward sum shift**, not the normalized Markov shift. The Hilbert norm is the standard counting-measure \(\ell^2\) norm. For any bounded onto map between Hilbert spaces, the least possible norm of a bounded linear right inverse equals the reciprocal of the minimum modulus of its adjoint; the assertion is about right inverses, not a unique inverse inside the disk.

## Proof
Write \(H_j\) for the coordinate Hilbert space of depth \(j\), and \(W=S^*\). The normalized child-lifting maps \(U_j:H_j\to H_{j+1}\) are isometries, with \(W|_{H_0}=U_0\) and \(W|_{H_j}=2U_j\) for \(j\ge1\). Decompose \(H_0\) and the wandering complements \(E_j=H_j\ominus U_{j-1}H_{j-1}\), \(j\ge1\), and propagate them by successive \(U_k\). The propagated chains are mutually orthogonal and span \(H\). Since \(E_1=0\), the resulting direct sum consists of exactly one unilateral weighted forward shift \(W_\mathrm{root}\) with weights \((1,2,2,\ldots)\), and countably many copies of the constant-weight forward shift \(2U\). In particular \(\sigma(S)\) is the closed disk of radius \(2\).

Conjugating by a diagonal phase unitary reduces the shifted minimum modulus to the case \(\lambda=r\ge0\). For the constant-weight component, the minimum modulus of \(2U-rI\) is \(|2-r|\): the triangle inequality gives the lower bound, and truncated approximate boundary eigenvectors give equality.

For the exceptional root chain, set \(J_r=(W_\mathrm{root}-rI)^*(W_\mathrm{root}-rI)\). In the canonical basis \((e_j)_{j\ge0}\), its Jacobi diagonal is \(1+r^2,4+r^2,4+r^2,\ldots\), while its successive off-diagonal entries are \(-r,-2r,-2r,\ldots\). The constant tail has spectral interval \([(2-r)^2,(2+r)^2]\). Below the lower edge, a square-summable eigenvector must have the form \(x_j=Ct^{j-1}\) for \(j\ge1\), where \(0<t<1\), with \(x_0=2C/t\). The tail dispersion and root boundary equations read
\[
\mu=4+r^2-2r(t+t^{-1}),\qquad
\mu=1+r^2-\frac{rt}{2}.
\]
They are equivalent to \(3rt^2-6t+4r=0\). Its smaller positive solution is
\[
t=\frac{1-\sqrt{1-4r^2/3}}r,
\]
which lies in \((0,1)\) exactly when \(0<r<6/7\). It generates the unique eigenvalue below the tail band,
\[
\mu_\mathrm{loc}(r)=\frac12+r^2+\frac12\sqrt{1-\frac43r^2}.
\]
At \(r=0\), \(e_0\) is an eigenvector with eigenvalue \(1\), the limiting formula. When \(r\ge6/7\), no square-summable eigenvector exists below the tail edge. The elementary one-dimensional Jacobi recurrence gives no other spectrum below the tail edge (any spectral point strictly below that edge would be an eigenvalue of this finite-rank boundary modification). Therefore the minimum squared modulus for the root chain is \(\mu_\mathrm{loc}(r)\) below \(6/7\), and \((2-r)^2\) from \(6/7\) onward. Since the root-chain lower edge is at most that of every constant-weight component, this gives the displayed formula for \(\gamma\).

For \(r<2\), the formula is positive, hence \(W-\overline\lambda I\) is bounded below, so \(S-\lambda I\) has closed range. Its kernel is infinite-dimensional: the many constant-weight backward-shift summands each have a nonzero eigenvector for \(r<2\). Equivalently, one can directly solve for each target by the convergent backward-shift right inverse; this establishes surjectivity (or use the absence of kernel of \(W-\overline\lambda I\), since a bounded-below adjoint gives a dense and closed range). Hilbert-space orthogonal decomposition then gives the optimal bounded-right-inverse norm \(1/\gamma\). At \(r=2\) the lower modulus vanishes and the range cannot be all of \(H\). For \(r>2\), the spectral-radius formula gives invertibility and \(\|(S-\lambda I)^{-1}\|=1/\gamma\). Finally differentiating the isolated-eigenvalue branch gives its sole positive critical point \(r=\sqrt{2/3}\), with value \(\gamma=2/\sqrt3\); the bulk branch is strictly decreasing on \([6/7,2]\).

## Verification
Direct finite-section checks used rectangular truncations of the root forward shift (including the last outgoing edge), avoiding the spurious zero singular value of square nilpotent truncations. For radii \(0,0.1,0.3,0.6,0.8\), numerical minimum singular values agreed with the isolated-eigenvalue formula to the displayed precision; above \(6/7\) finite sections approach the predicted bulk edge from above. These checks are illustrations, not the proof. All exact constants follow from the Jacobi recurrence and the derivatives above; no external computation is needed for the infinite-dimensional conclusion.

## Relationship to prior work
Buckley and Seco (2026) establish universality of shifts on leafless bounded-degree trees and identify branching growth thresholds for spectral radius and universality, but do not give the optimal right-inverse norm, the root-induced localized singular state, or the sharp transition \(6/7\). Budzyński, Dymek, Planeta and Ptak (2017) establish general Wold-type decompositions for balanced weighted shifts on directed trees; this structural antecedent is explicitly used. D'Aniello and Maiuriello (2022) give general spectral facts for unilateral weighted shifts. Earlier two-periodic bilateral recurrence stability results concern translation-periodic bulk operators without a finite root defect; those formulae do not produce this localized root eigenvalue or its transition. The novelty assessed is **not** the elementary general Jacobi method, but the exact root-sensitive phase transition and nonmonotone sharp universality margin for this natural rooted-tree shift.

## Limitations
This is one explicit tree, not a classification of all irregular rooted trees. The formula concerns a Hilbert \(\ell^2\) backward sum shift with exactly one exceptional branching level; no \(\ell^p\), arbitrary branching, or nonlinear stability claim follows. Generic half-line Jacobi bound-state theory may contain an equivalent defect calculation under another normalization; priority is not independently established. The verification is analytical and same-model only, with no independent audit.

## References
- J. Buckley and D. Seco, *Rota universality of shifts on trees*, arXiv:2610.40089v1, submitted 29 October 2026, https://arxiv.org/abs/2610.40089.
- P. Budzyński, P. Dymek, A. Planeta and M. Ptak, *Weighted shifts on directed trees. Their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765 (2017), https://arxiv.org/abs/1702.00765.
- E. D'Aniello and M. Maiuriello, *On the spectrum of weighted shifts*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas (2022), https://doi.org/10.1007/s13398-022-01328-z.
