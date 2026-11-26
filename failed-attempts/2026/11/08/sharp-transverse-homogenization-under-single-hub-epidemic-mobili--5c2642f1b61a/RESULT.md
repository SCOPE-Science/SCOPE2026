# Sharp transverse homogenization under single-hub epidemic mobility

## Finding
In the disease-free linearization of the equal-population SIR-network metapopulation model with one exceptional hub and identical nonhub infection rates, suppose mobility is symmetric and every nonhub sends the same fraction \(q\) to the hub. The centered vector of nonhub infectious perturbations evolves **exactly autonomously**, irrespective of the hub's infection rate. Its sharp Euclidean decay exponent is
\[
\delta(B)=\gamma-\beta_0\bigl\|B|_{\mathbf{1}^\perp}\bigr\|_2^2.
\]
Across all admissible symmetric nonhub mobility blocks \(B\), the complete attainable interval is
\[
\boxed{\gamma-\beta_0(1-q)^2\ \le\ \delta(B)\ \le\ \gamma.}
\]
Both bounds and every intermediate exponent are attained by explicitly specified connected mobility networks that have **exactly the same reproduction number**, even when the common infection process is linearly supercritical. In particular, variation of the background network can change the persistence time of between-community heterogeneity without changing the invasion threshold.

## Assumptions and scope
Fix an integer \(m\ge2\), giving \(m\) equal-sized ordinary communities and one equal-sized hub. Let \(\gamma>\beta_0>0\), hub infection rate \(\beta_h=\zeta\beta_0>\gamma\), and \(0<q\le1/m\). Let \(B\in\mathbb R^{m\times m}\) be symmetric, entrywise nonnegative, with \(B\mathbf{1}=(1-q)\mathbf{1}\). The symmetric row-stochastic mobility matrix is
\[
\Phi=\begin{pmatrix}B&q\mathbf{1}\\q\mathbf{1}^{\mathsf T}&1-mq\end{pmatrix}.
\]
Every such network is connected through the hub because \(q>0\). Its disease-free infected linearization, in units of physical time, is
\[
\dot i=Li,\quad L=\beta_0\Phi\,\operatorname{diag}(1,\ldots,1,\zeta)\Phi-\gamma I_{m+1}.
\]
Let \(P=I_m-\mathbf{1}\mathbf{1}^{\mathsf T}/m\) and let \(u=P(i_1,\ldots,i_m)^{\mathsf T}\). This is a **linearized** result; it does not assert nonlinear trajectory synchronization or a bound on final outbreak size. Write \(B|_{\mathbf{1}^\perp}\) for the self-adjoint restriction of \(B\) to the zero-sum subspace.

## Proof
1. Symmetry and the constant-row-sum condition imply \(PB=BP\) and \(P\mathbf{1}=0\). The upper-left block of \(\Phi\operatorname{diag}(1,\ldots,1,\zeta)\Phi\) is \(B^2+\zeta q^2\mathbf{1}\mathbf{1}^{\mathsf T}\). Its upper-right block is a multiple of \(\mathbf{1}\). Therefore, applying \(P\) to the first \(m\) components of \(\dot i=Li\) cancels every hub-dependent term, yielding the exact closed equation
\[
\boxed{\dot u=(\beta_0 B^2-\gamma I_m)u.}
\]
This identity holds for every initial infected perturbation, whether or not the ordinary-community initial values agree.

2. Since \(B\) is real symmetric, it admits an orthonormal eigenbasis. Nonnegativity and row sum \(1-q\) imply that every eigenvalue \(\mu\) obeys \(|\mu|\le1-q\) (e.g., the maximum row-sum norm). On the invariant zero-sum subspace the eigenvalues of the autonomous generator are \(\beta_0\mu^2-\gamma<0\). Its semigroup has norm exactly \(\exp[-\delta(B)t]\). Consequently for all \(t\ge0\),
\[
\|u(t)\|_2\le e^{-\delta(B)t}\|u(0)\|_2,
\]
and no larger exponent works for all zero-sum initial vectors: choose an eigenvector where \(|\mu|\) is maximal. This establishes the formula and universal bounds.

3. Let \(J=\mathbf{1}\mathbf{1}^{\mathsf T}/m\). For any \(\alpha\in[0,1]\), define
\[
B_\alpha=(1-q)\bigl[\alpha I_m+(1-\alpha)J\bigr].
\]
The block is nonnegative, symmetric and has row sum \(1-q\); the full mobility graph remains connected via its hub. On \(\mathbf{1}^\perp\), it is exactly the scalar \(\alpha(1-q)\). Hence
\[
\delta(B_\alpha)=\gamma-\beta_0\alpha^2(1-q)^2.
\]
As \(\alpha\) ranges from zero to one, this realizes every value of the claimed closed interval. At \(\alpha=0\) every contrast decays at exactly the recovery rate \(\gamma\); at \(\alpha=1\) every contrast decays at the universal slow bound.

4. The two-dimensional subspace where all \(m\) ordinary-community entries coincide is invariant under \(L\). In coordinates (ordinary common value, hub value), the next-generation matrix is
\[
Q=\frac{\beta_0}{\gamma}\,A\operatorname{diag}(1,\zeta)A,
\qquad A=\begin{pmatrix}1-q&q\\mq&1-mq\end{pmatrix}.
\]
This quotient depends only on \(m,q,\zeta,\beta_0/\gamma\), not on \(B\). Because \(q>0\) and \(\zeta>0\), the full nonnegative next-generation matrix is strictly positive (the hub term contributes a positive amount to each ordinary-ordinary entry, and direct hub transmission is positive). Its positive Perron eigenvector therefore lies in this invariant two-dimensional subspace, so the full reproduction number equals \(\rho(Q)\). Thus every \(B_\alpha\) above has the same invasion threshold, even though its sharp transverse relaxation exponent varies. In a parameter regime where \(\rho(Q)>1\), the principal infection mode grows but zero-sum ordinary-community differences still decay exponentially.

**A supercritical comparison.** For \(m=3\), \(q=1/4\), \(\gamma=1\), \(\beta_0=2/3\), and \(\zeta=5\), every admissible background has the same \(\mathcal R_0=(2/3)(3+5)/4=4/3>1\). Yet the all-to-all low-risk block \(B_0=(3/4)J\) has transverse decay exponent \(\delta=1\), whereas the diagonal block \(B_1=(3/4)I_3\) has \(\delta=5/8\). The full networks remain connected through the hub in both cases.

## Verification
The standalone Python/SymPy file `verify.py` checks the exact projection, block invariance, mobility admissibility and worst/best/intermediate rate identities for \(342\) rational parameter families, including \(m=2,\ldots,7\). Run `python verify.py` from the extracted package directory; the expected success line begins `VERIFY_OK`. The proof of the all-size bound is spectral and analytic, not inferred from finite testing.

## Relationship to prior work
Das and Stolerman (2023 preprint, 2024 journal) introduce precisely this SIR-network single-high-risk-hub geometry, prove invasion thresholds for star and other restricted structures, and state the broader symmetric-flux threshold as a conjecture. Their explicit star spectrum has a single repeated transverse decay mode; the present finding treats **every** symmetric stochastic ordinary-community mobility block and sharply classifies the entire attainable range of nonuniform-mode decay rates. The quotient/Perron mechanism behind topology-independent invasion thresholds is established spectral methodology and **is not asserted here as a new general principle**. Bonaccorsi et al. (2014 preprint, 2015 journal) establish spectral-radius preservation under equitable partitions in an SIS network model; this is a close conceptual predecessor, but their cited results do not state the exact nonhub transverse semigroup or the sharp rate interval for the heterogeneous-mobility SIR model. O'Clery et al. (2013) study equitable-partition synchronization in graph consensus dynamics, a related but different generator.

## Limitations
The result is restricted to the disease-free **linearization**, equal populations, symmetric mobility, identical nonhub rates, and uniform mobility flux to the hub. It provides neither nonlinear synchronization nor epidemic final-size ordering. The exact quotient invariant is a standard linear-algebraic idea; possible unindexed applications of this framework to the same SIR mobility model remain a publication-priority risk. No independent external audit has been performed.

## References
- H. K. Das and L. M. Stolerman, *Epidemic thresholds and disease dynamics in metapopulations: the role of network geometry and human mobility*, arXiv:2308.01998v1 (3 August 2023), https://arxiv.org/abs/2308.01998; journal DOI 10.1137/23M1579522 (2024).
- S. Bonaccorsi, S. Ottaviano, D. Mugnolo and F. De Pellegrini, *Epidemic Outbreaks in Networks with Equitable or Almost-Equitable Partitions*, arXiv:1412.6157 (2014), https://arxiv.org/abs/1412.6157; DOI 10.1137/140995829 (2015).
- N. O'Clery, Y. Yuan, G.-B. Stan and M. Barahona, *Observability and coarse graining of consensus dynamics through the external equitable partition*, Phys. Rev. E 88, 042805 (2013), https://doi.org/10.1103/PhysRevE.88.042805.
