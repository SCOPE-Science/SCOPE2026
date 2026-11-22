# Exact end-to-end absorption time and optimal loss on the open SSH chain

## Finding

For each integer \(n\ge1\), let \(H\) be the real symmetric single-particle Hamiltonian on the open path with \(2n\) vertices, zero diagonal and successive positive hoppings \(v,w,v,w,\ldots,v\). Thus the \(v\)-bonds are intracell bonds \((2j-1,2j)\); the \(w\)-bonds are intercell bonds \((2j,2j+1)\). Put an irreversible sink of rate \(\kappa>0\) at vertex 1 and initialize the particle at vertex \(2n\). The no-jump generator is \(B=-iH-(\kappa/2)|1\rangle\langle1|\). Its survival probability is \(S(t)=\|e^{Bt}|2n\rangle\|^2\).

Then absorption is certain, and for every \(v,w,\kappa>0\) and integer \(n\ge1\),

\[
T_n(\kappa):=\int_0^\infty S(t)\,dt
=\frac{2n}{\kappa}+\kappa\left(\frac{n-1}{2w^2}+\frac{w^{2n-2}}{4v^{2n}}\right).
\]

Writing \(C_n=(n-1)/(2w^2)+w^{2n-2}/(4v^{2n})\), the unique optimum over positive loss rates is

\[
\kappa_* = \sqrt{\frac{2n}{C_n}},\qquad
T_{n,\min}=2\sqrt{2n C_n}.
\]

For fixed hoppings and \(n\to\infty\),

\[
T_{n,\min}\sim\begin{cases}2n/w,&w\le v,\\
\sqrt{2n}\,(w/v)^{n-1}/v,&w>v.
\end{cases}
\]

## Assumptions and scope

Time is measured in units with \(\hbar=1\); only the single-excitation no-jump dynamics is considered. This is continuous *irreversible absorption*, not periodically repeated projective measurement, a many-body filled band, or an environment that reinjects particles. The formula includes \(n=1\) (there are no intercell bonds, and the term containing \(w\) is zero). It does not assert a finite result for zero hopping or zero loss. The large-size statements hold with positive \(v,w\) held fixed.

## Proof

**1. Completeness of absorption and the Lyapunov representation.** Every eigenvector of an irreducible Jacobi matrix has a nonzero first coordinate: if the first coordinate vanished, the eigenvalue recurrence would force all coordinates to vanish. Since \(H\) is real symmetric, an eigenmode of \(B\) with zero decay would be an eigenvector of \(H\) vanishing at vertex 1, which is impossible. Every eigenvalue of \(B\) therefore has strictly negative real part. The Hermitian positive matrix

\[
X(\kappa)=\int_0^\infty e^{B^\dagger t}e^{Bt}\,dt
\]

is the unique solution of \(B^\dagger X+XB=-I\), and \(T_n(\kappa)=X_{2n,2n}\).

**2. Exact dependence on \(\kappa\).** Conjugate by alternating site phases to make the coherent part a real skew-symmetric irreducible tridiagonal matrix \(A\). Write \(P=e_1e_1^T\), \(L(Z)=[Z,A]\), \(D(Z)=PZ+ZP\). In this real representation \(X\) is real symmetric and satisfies

\[
L(X)-\frac{\kappa}{2}D(X)=-I.
\]

Split symmetric matrices into \(E\) (entries only for same-parity vertex indices) and \(O\) (entries only for opposite-parity indices), writing \(X=X_E+X_O\). Since \(L\) exchanges the two spaces and \(D\) preserves them, the equations are

\[
L(X_O)-\frac{\kappa}{2}D(X_E)=-I,\qquad
L(X_E)-\frac{\kappa}{2}D(X_O)=0.
\]

Because \(A\) is irreducible skew tridiagonal with simple eigenvalues, its real symmetric commutant is \(\operatorname{span}\{I,A^2,\ldots,A^{2n-2}\}\), contained in \(E\). The vectors \(e_1,A^2e_1,\ldots,A^{2n-2}e_1\) form a basis of the odd-indexed coordinate subspace: each introduces a new nonzero component two positions farther along the path. Taking inner products of the first equation with each commuting power of \(A\) therefore fixes every entry of \(\kappa D(X_E)\), independently of \(\kappa\). It follows that \(L(X_O)\) is independent of \(\kappa\). The kernel of \(L\) within \(O\) is zero, so \(X_O\) is independent of \(\kappa\).

The second equation now fixes \(L(X_E)/\kappa\) independently of \(\kappa\), whereas the first fixes \(\kappa D(X_E)\). The linear map \(Z\mapsto(L(Z),D(Z))\) on \(E\) is injective: a matrix in its kernel must commute with \(A\) and have zero first row, and since \(e_1\) is cyclic for \(A\), that matrix is zero. Since these constraints have solutions at distinct positive rates, linearity yields fixed real symmetric \(U,V\in E\) with

\[
X_E(\kappa)=\kappa^{-1}U+\kappa V.
\]

Hence each diagonal entry, in particular the desired mean lifetime, has the *exact* form \(a/\kappa+b\kappa\), with constants independent of the loss strength.

**3. Determine the weak-loss coefficient.** The eigenvalues of \(H\) are simple, and weak rank-one loss gives an eigenmode with decay rate \(\kappa|\phi_j(1)|^2\) in its *probability*. Cross terms in the time integral remain bounded at vanishing \(\kappa\) because distinct eigenfrequencies are separated. Thus

\[
\lim_{\kappa\downarrow0}\kappa T_n(\kappa)
=\sum_{j=1}^{2n}\frac{|\phi_j(2n)|^2}{|\phi_j(1)|^2}.
\]

The SSH bond sequence is reflection symmetric, so each simple eigenvector is even or odd under reflection; the ratio of squared endpoint components is one. Consequently \(a=2n\).

**4. Determine the strong-loss coefficient.** As \(\kappa\to\infty\), eliminating the rapidly decaying first site leaves, to leading order, the \((2n-1)\)-site Hamiltonian \(H'\) on vertices \(2,\ldots,2n\), with an effective no-jump loss amplitude \(-2v^2/\kappa\) at its first site. Every mode of \(H'\) has nonzero first amplitude, so the same nondegenerate mode perturbation gives

\[
\lim_{\kappa\to\infty}\frac{T_n(\kappa)}{\kappa}
=\frac1{4v^2}\sum_{j=1}^{2n-1}\frac{|\psi_j(2n)|^2}{|\psi_j(2)|^2}.
\]

For \(n=1\), the sole residual site gives the sum one. For \(n\ge2\), partition the residual chain into \(n\) even-indexed sites and \(n-1\) odd-indexed sites. The inter-sublattice coupling matrix \(C\) has entries \(C_{j,j}=w\) and \(C_{j+1,j}=v\), so \(C^TC\) is an irreducible \((n-1)\)-by-\((n-1)\) Jacobi matrix with constant diagonal \(v^2+w^2\) and off-diagonal \(vw\). Each of its eigenvectors has equal-magnitude first and last coordinates by reflection symmetry. The \(2n-2\) nonzero-energy modes of \(H'\) therefore have squared endpoint ratio \(v^2/w^2\). The remaining zero mode, supported on even-indexed sites, satisfies \(w a_j+v a_{j+1}=0\), giving squared endpoint ratio \((w/v)^{2n-2}\). The sum is exactly

\[
(2n-2)\frac{v^2}{w^2}+\left(\frac wv\right)^{2n-2}.
\]

Thus \(b=(n-1)/(2w^2)+w^{2n-2}/(4v^{2n})\). Combining this with the exact dependence from Step 2 proves the identity. Differentiating \(2n/\kappa+C_n\kappa\) proves uniqueness of the optimum, and comparison of the two terms in \(C_n\) proves the two asymptotic regimes.

## Verification

Run `python verify.py` with Python, NumPy and SciPy. It solves the full complex Lyapunov equation independently for 150 different finite parameter combinations (up to \(n=10\)) and checks the deleted-site spectral endpoint identity for 56 additional combinations (up to \(n=15\)). It has no dependency on previous experiments or unpublished tables. These calculations check finite cases; the proof above supplies the all-size statement.

## Relationship to prior work

The Su--Schrieffer--Heeger hopping geometry originated in Su, Schrieffer and Heeger (1979). Menczel et al. (2026, Sec. II H, Figs. 2 and 6) consider first-passage statistics for a **periodic two-cell SSH chain with a collective decay operator**. Their operator and boundary conditions differ from the open many-cell chain with one endpoint absorber; the inspected section does not give this lifetime identity. Wang and Zhang (2026) study the **single-site-loss SSH chain**, the closest physical model, and obtain Liouvillian spectral-gap asymptotics and exceptional-point statements. The accessible abstract does not state the endpoint-to-endpoint mean lifetime identity or exact loss-rate optimum; the complete paper could not be examined, and priority is therefore provisional. Liu et al. (2020) study **repeated projective** first detection, rather than continuous rank-one loss, so their general formula is not directly the same observable.

## Limitations

This is a finite open-chain single-particle absorption theorem, not a statement of experimental robustness, many-body relaxation, finite-temperature topological protection or a thermodynamic phase transition. The exponentially large time when \(w>v\) is an optimized endpoint-capture time, not solely a Liouvillian-gap estimate. Wider historical coverage may contain equivalent general path-network absorption formulas; priority requires independent assessment.

## References

- W. P. Su, J. R. Schrieffer and A. J. Heeger, "Solitons in Polyacetylene," *Phys. Rev. Lett.* **42** (1979), 1698. https://doi.org/10.1103/PhysRevLett.42.1698
- P. Menczel et al., "Full Counting Statistics and First-Passage Times in Quantum Markovian Processes," *PRX Quantum* **7** (2026), 010304. https://doi.org/10.1103/4hc1-l8w4
- Y. T. Wang and X. Z. Zhang, "From local weight selection to Zeno slowdown in an open Su-Schrieffer-Heeger chain with a single local loss," *Phys. Rev. A* **114** (2026), 012457. https://arxiv.org/abs/2607.10218
- Q. Liu, R. Yin, K. Ziegler and E. Barkai, "Quantum walks: the first detected transition time" (2020). https://arxiv.org/abs/2001.00231
