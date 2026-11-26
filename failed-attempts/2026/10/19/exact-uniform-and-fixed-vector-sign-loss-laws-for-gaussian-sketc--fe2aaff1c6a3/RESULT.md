# Exact uniform and fixed-vector sign-loss laws for Gaussian-sketched positive-definite operators

## Finding
Let \(A\in\mathbb R^{2\times2}\) be symmetric positive definite with distinct eigenvalues \(0<\mu<L\), and condition number \(\kappa=L/\mu>1\). Let \(S\in\mathbb R^{k\times2}\), \(k\ge2\), have independent \(N(0,1)\) entries. Let \(I_z(a,b)=B(a,b)^{-1}\int_0^z t^{a-1}(1-t)^{b-1}\,dt\) be the regularized incomplete beta function, and let \(\Phi\) denote the standard normal distribution function. Put
\[
z_\kappa=\left(\frac{\kappa-1}{\kappa+1}\right)^2.
\]
The exact probability that the sketched positive-real bilinear form has a negative value somewhere is
\[
\boxed{P_\mathrm{all}(k,\kappa)=\Pr\{\exists v\ne0:(Sv)^\mathsf{T}SAv<0\}=I_{z_\kappa}\left(\frac{k-1}{2},\frac12\right).}
\]
By contrast, for a vector selected before observing \(S\), its largest possible sign-loss probability is
\[
\boxed{P_\mathrm{fixed}(k,\kappa)=\sup_{v\ne0}\Pr\{(Sv)^\mathsf{T}SAv<0\}=\frac12I_{z_\kappa}\left(\frac{k}{2},\frac12\right).}
\]
The fixed-vector formula is valid for every integer \(k\ge1\), including a single sketch row; the all-vector formula is asserted for \(k\ge2\). The two probabilities satisfy the exact one-row identity
\[
P_\mathrm{all}(k,\kappa)=2P_\mathrm{fixed}(k-1,\kappa),\qquad k\ge2.
\]
If \(\kappa\to\infty\) while \(k/\kappa\to\tau\in[0,\infty]\), then
\[
P_\mathrm{all}\longrightarrow2\Phi(-2\sqrt\tau),\qquad
P_\mathrm{fixed}\longrightarrow\Phi(-2\sqrt\tau),
\]
with both limits interpreted as zero when \(\tau=\infty\). Consequently the Gaussian sketch has vanishing risk of losing positive realness **uniformly over the starting vector** precisely when \(k/\kappa\to\infty\).

## Assumptions and scope
All claims concern exact real arithmetic and iid real Gaussian sketches of size \(k\times2\), including when \(k>2\). The sketch is independent of the deterministic matrix \(A\). In \(P_\mathrm{all}\), the adverse vector is permitted to depend on the realized \(S\). In \(P_\mathrm{fixed}\), the vector must be chosen before sampling \(S\). The sign of \((Sv)^\mathsf{T}SAv\) is unchanged by a global scaling of \(S\), so common \(1/\sqrt k\) sketch normalization gives the same probability. Exact equality to zero has probability zero for \(k\ge2\) and \(\kappa>1\). For \(\kappa=1\), neither type of negative sign loss occurs; the theorem uses \(\kappa>1\) to avoid degenerate angular notation.

For the one-dimensional trial space spanned by \(v\), the sketched Galerkin scalar is
\[
\lambda_\mathrm{G}(v)=\frac{(Sv)^\mathsf{T}SAv}{\|Sv\|_2^2},
\]
and the sketched harmonic scalar is
\[
\lambda_\mathrm{H}(v)=\frac{\|SAv\|_2^2}{(SAv)^\mathsf{T}Sv},
\]
whenever denominators are nonzero. Their signs are governed by the same bilinear form. The theorem quantifies positivity of all such one-dimensional projected scalars, not signs of eigenvalues of a complete two-dimensional generalized projected operator.

## Proof
**Step 1: uniform positivity is a definite Jordan-product condition.** Define \(W=S^\mathsf{T}S\) and \(J=(WA+AW)/2\). For all real \(v\),
\[
(Sv)^\mathsf{T}SAv=v^\mathsf{T}Jv.
\]
Orthogonal invariance of the Gaussian sketch permits \(A=\operatorname{diag}(\mu,L)\) without loss. Write \(S=[X\;Y]\) with independent \(X,Y\sim N(0,I_k)\). Then
\[
J=\begin{pmatrix}
\mu\|X\|_2^2&\frac{\mu+L}{2}X^\mathsf{T}Y\\
\frac{\mu+L}{2}X^\mathsf{T}Y&L\|Y\|_2^2
\end{pmatrix}.
\]
Both diagonal entries are strictly positive almost surely. Hence \(J\) is positive definite precisely when
\[
R^2:=\frac{(X^\mathsf{T}Y)^2}{\|X\|_2^2\|Y\|_2^2}<\frac{4\mu L}{(\mu+L)^2}=1-z_\kappa.
\]
If the reversed strict inequality holds, \(J\) has a negative eigenvalue and its eigenvector witnesses negative sign loss. The boundary has probability zero.

**Step 2: angular probability.** Conditional on \(X\ne0\), decompose \(Y\) parallel and perpendicular to \(X\). Rotational invariance gives independent \(U^2\sim\chi_1^2\) and \(V\sim\chi^2_{k-1}\), with
\[
R^2\;\overset{d}{=}\;\frac{U^2}{U^2+V}\sim\operatorname{Beta}\left(\frac12,\frac{k-1}{2}\right).
\]
The survival probability above \(1-z_\kappa\) is \(I_{z_\kappa}((k-1)/2,1/2)\), yielding \(P_\mathrm{all}\).

**Step 3: fixed vectors.** For fixed \(v\ne0\), define
\[
c(v)=\frac{v^\mathsf{T}Av}{\|v\|_2\|Av\|_2}>0.
\]
The pair \((Sv,SAv)\), after length normalization, consists of correlated Gaussian columns with correlation \(c(v)\). By conditioning on the first column, negative inner product occurs with probability
\[
\mathbb E\Phi\left(-\frac{c(v)}{\sqrt{1-c(v)^2}}\sqrt{\chi_k^2}\right)
=\frac12 I_{1-c(v)^2}\left(\frac k2,\frac12\right).
\]
At \(c(v)=1\) this formula is understood as zero. This fixed-pair sign-flip identity is a standard Gaussian projection fact, including the form of Kabán and Durrant [4]; it is not claimed as independently novel. In an eigenbasis of \(A\), let \(t\) be the squared proportion of \(v\) in the \(L\)-eigenspace. Then
\[
c(v)^2=\frac{(1+(\kappa-1)t)^2}{1+(\kappa^2-1)t},\quad 0\le t\le1.
\]
Differentiating yields the unique interior minimum at \(t=1/(\kappa+1)\), with \(c_\mathrm{min}=2\sqrt\kappa/(\kappa+1)\). Since sign-flip probability decreases strictly with \(c\), substitution gives \(P_\mathrm{fixed}\). The maximizing vectors, up to nonzero scale and eigenvector signs, have squared weights \(\kappa/(\kappa+1)\) for \(\mu\) and \(1/(\kappa+1)\) for \(L\). The one-row identity follows by comparing beta parameters; no asymptotic argument is involved.

**Step 4: simultaneous condition-number and sketch-size asymptotics.** By Step 2 and \(k\to\infty\),
\[
kR^2\Rightarrow\chi_1^2,
\qquad \frac{4\kappa k}{(\kappa+1)^2}\longrightarrow4\tau
\]
whenever \(k/\kappa\to\tau\in(0,\infty)\). Therefore the failure probability tends to \(\Pr\{\chi_1^2>4\tau\}=2\Phi(-2\sqrt\tau)\). For \(\tau=0\), this remains valid when \(k\to\infty\); for bounded \(k\), the beta tail tends to one directly. For \(k/\kappa\to\infty\), the beta mean \(\mathbb ER^2=1/k\) and Markov's inequality give
\[
P_\mathrm{all}(k,\kappa)\le\frac{(\kappa+1)^2}{4\kappa k}\longrightarrow0.
\]
The fixed-vector limits follow from the exact one-row identity (using a one-row shift); for bounded \(k\) and \(\kappa\to\infty\) the fixed probability tends to \(1/2\). Finally, if the uniform risk vanished without \(k/\kappa\to\infty\), some subsequence would have \(k/\kappa\) bounded; extracting a subsequential finite ratio and applying the positive Gaussian-tail limit gives a contradiction. This proves the stated if-and-only-if criterion.

## Verification
A standalone numerical and analytical test program, `CHECKER.py`, evaluates the incomplete-beta formulas and their exact one-row relation over multiple \((k,\kappa)\) pairs, constructs definite/indefinite explicit Gram examples across the threshold, verifies the sharp fixed-vector angle through an independent grid calculation, performs reproducible Gaussian Monte Carlo tests, and checks the critical normal-law profile. Running `python CHECKER.py` with NumPy and SciPy prints `ALL TESTS PASSED`. These finite checks support the derivation but are not the reason the all-parameter theorem holds; the preceding proof supplies that argument.

## Relationship to prior work
Güttel, Liu, and Nyman [1] motivate the role of positive-realness and sketched harmonic projections in matrix-function Krylov computations. Güttel and Schweitzer [2] prove convergence under sketched-subspace embedding conditions, rather than these exact unconditional two-dimensional Gaussian sign-loss probabilities. Palitta, Schweitzer, and Simoncini [3] analyze sketched Krylov Ritz behavior, including eigenvalue outliers, but do not present this all-starting-vector Gaussian law. Kabán and Durrant [4, Lemma 2.2] already derive the **fixed-pair** Gaussian sign-flip probability, which is explicitly acknowledged and used; the new comparison is the sharp **adaptive all-vector** probability, its exact one-row bridge to the worst fixed-vector risk, and the condition-number/sketch-size limit. Standard beta and chi-square facts underpin the calculation.

## Limitations
The ambient operator dimension is exactly two, the operator is real symmetric positive definite, and the sketch has independent Gaussian entries. No theorem for sparse sketches, nonnormal operators, floating-point computations, higher-dimensional eigenspaces, or algorithmic convergence is asserted. The quantifier distinction matters: uniform failure permits a vector to be selected after the sketch is realized; this does not imply the same failure probability for a fixed Krylov start. A complete two-dimensional Ritz projection of an invertible sketch may retain positive eigenvalues even when the associated all-vector bilinear form is indefinite. Although accessible published sources were inspected, a complete version of the motivating 2026 manuscript could not be inspected; a potential appendix with stronger coverage remains a residual bibliographic risk. Mathematical correctness and novelty have not been independently audited.

## References
[1] S. Güttel, J. Liu, and L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354 (first posted 11 July 2026), https://arxiv.org/abs/2607.10354.

[2] S. Güttel and M. Schweitzer, *Randomized Sketching for Krylov Approximations of Large-Scale Matrix Functions*, SIAM Journal on Matrix Analysis and Applications 44 (2023), 1073–1095, https://doi.org/10.1137/22M1518062.

[3] D. Palitta, M. Schweitzer, and V. Simoncini, *Sketched and Truncated Polynomial Krylov Methods: Evaluation of Matrix Functions*, Numerical Linear Algebra with Applications 32 (2025), e2596, https://doi.org/10.1002/nla.2596 (first online 11 November 2024).

[4] A. Kabán and R. J. Durrant, *Structure from Randomness in Halfspace Learning with the Zero-One Loss*, Journal of Artificial Intelligence Research (2020), Lemma 2.2, https://pure-oai.bham.ac.uk/ws/files/105807329/Structure_from_Randomness.pdf.
