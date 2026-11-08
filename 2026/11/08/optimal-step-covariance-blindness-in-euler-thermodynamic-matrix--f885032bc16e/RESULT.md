# Optimal-step covariance blindness in Euler thermodynamic matrix inversion

## Finding

**Theorem (complete inverse fibers, optimal-step collapse, and recovery).** Fix a step size \(h>0\) and a dimension \(d\ge1\). For a real symmetric positive-definite matrix \(A\) satisfying \(0<h\lambda_{\max}(A)<2\), define the Euler--Maruyama chain
\[
X_{k+1}=(I-hA)X_k+\sqrt{2h}\,\xi_k,\qquad \xi_k\overset{\mathrm{iid}}\sim N(0,I_d).
\]
Let \(\mathcal C_h(A)\) be its stationary covariance. Then:

1. Its exact covariance-to-precision map is
   \[
   \mathcal C_h(A)^{-1}=A-\tfrac h2 A^2.
   \]
   The range of \(\mathcal C_h\) on stable symmetric positive-definite drifts is exactly the set of matrices \(C\succeq 2hI_d\). For such \(C\), put \(M=I_d-2hC^{-1}\). **Every** preimage is
   \[
   A=h^{-1}(I_d-K),\qquad K=K^{\mathsf T},\qquad K^2=M.
   \]
   On an eigenspace \(E_c\) of \(C\) with eigenvalue \(c>2h\) and multiplicity \(m_c\), the choices are precisely
   \[
   K|_{E_c}=\sqrt{1-2h/c}\,(2P_c-I_{E_c}),
   \]
   for any orthogonal projector \(P_c\) on \(E_c\); on \(E_{2h}\), necessarily \(K=0\). Thus the fiber is a product over \(c>2h\) of the disjoint unions \(\bigsqcup_{r=0}^{m_c}\mathrm{Gr}(r,m_c)\). In particular, the covariance uniquely identifies the drift **if and only if** \(C=2hI_d\); otherwise there are at least two drifts, and a repeated eigenvalue \(c>2h\) gives a continuous family.

2. If \(A\) is nonscalar, \(\mathcal C_h(A)=cI_d\) for some \(c>0\) **if and only if** \(A\) has exactly two distinct eigenvalues \(0<a<b\) and \(h=2/(a+b)\). This \(h\) is exactly the unique minimizer of \(\rho(I-hA)\) over \(0<h<2/b\). At this step,
   \[
   \mathcal C_h(A)=\frac{a+b}{ab}\,I_d.
   \]
   More strongly, for deterministic \(X_0=0\) all one-time distributions, including finite-time ones, are isotropic and depend on \(a,b\) but **not** on the eigenspaces or their multiplicities:
   \[
   X_k\sim N\!\left(0,\frac{a+b}{ab}\left[1-\left(\frac{b-a}{b+a}\right)^{2k}\right]I_d\right),\qquad k\ge0.
   \]
   Hence even complete collections of one-time marginal laws at the optimal Euler step cannot recover the two eigenspaces.

3. If stationary covariances of the same unknown \(A\) are available at two **distinct known** stable step sizes \(h_1\ne h_2\), then \(A\) is uniquely recovered without choosing branches:
   \[
   A=\frac{h_2\mathcal C_{h_1}(A)^{-1}-h_1\mathcal C_{h_2}(A)^{-1}}{h_2-h_1}.
   \]
   This identity assumes exact population covariances, not finite-sample estimates.

## Assumptions and scope

All matrices are real \(d\times d\). The symmetric positive-definite drift \(A\) and a fixed positive Euler step \(h\) are assumed known to obey the stability condition \(0<h\lambda_{\max}(A)<2\) when the forward covariance is defined. The noise vectors are independent standard Gaussian, and the noise coefficient is exactly \(\sqrt{2h}\,I_d\). The inverse-fiber classification allows arbitrary symmetric positive-definite drifts with the same step, not just diagonal drifts. The optimal-step statement is restricted to nonscalar matrices; for a scalar matrix the covariance is isotropic for every stable step. The finite-time claim starts at deterministic zero and concerns marginal distributions, not the joint path law. The two-step identity requires that both step sizes separately satisfy stability.

## Proof

**Exact covariance and range.** Write \(B=I_d-hA\). Stability gives \(B=B^{\mathsf T}\) and \(\rho(B)<1\). Its stationary covariance exists uniquely as
\[
C=2h\sum_{j=0}^{\infty}B^{2j}=2h(I_d-B^2)^{-1},
\]
so \(C^{-1}=(I_d-B^2)/(2h)=A-\frac h2 A^2\). Since \(0\preceq B^2\prec I_d\), \(C\succeq2hI_d\). Conversely, for any symmetric \(C\succeq2hI_d\), the matrix \(M=I_d-2hC^{-1}\) is symmetric with spectrum in \([0,1)\). Choose any symmetric square root \(K\) of \(M\) (e.g. its nonnegative root) and set \(A=(I_d-K)/h\). Every eigenvalue of \(K\) lies strictly between \(-1\) and \(1\), hence \(A\succ0\) and \(h\lambda_{\max}(A)<2\). The previous formula yields stationary covariance \(C\). This proves the full range.

**Complete fiber.** If a drift \(A\) produces \(C\), its symmetric matrix \(K=I_d-hA\) obeys \(K^2=M\). Conversely every symmetric root produces a valid drift as just established. The relation \(KM=MK\) follows from \(M=K^2\), so each \(M\)-eigenspace is \(K\)-invariant. On the eigenspace for \(\mu=0\), symmetry and \(K^2=0\) force \(K=0\) (as \(\|Kv\|^2=\langle v,K^2v\rangle\)). On an eigenspace with \(\mu>0\), \(K/\sqrt\mu\) is a symmetric involution; its spectral projections are orthogonal and give \(K=\sqrt\mu(2P-I)\). Conversely every such projection defines a root. The eigenvalues of \(M\) are \(1-2h/c\), establishing the asserted product of projector manifolds. Each positive \(\mu\) allows at least the choices \(P=0\) and \(P=I\), so uniqueness is equivalent to \(M=0\), equivalently \(C=2hI_d\). For multiplicity at least two, rank-one projections form infinitely many choices.

**Isotropic collapse and optimization.** If \(A\) has distinct eigenvalues \(a<b\) only, then at \(h_*=2/(a+b)\), \(B=I-h_*A\) has eigenvalues \(q=(b-a)/(a+b)\) and \(-q\), so \(B^2=q^2I_d\), and
\[
\mathcal C_{h_*}(A)=\frac{2h_*}{1-q^2}I_d=\frac{a+b}{ab}I_d.
\]
Starting from \(X_0=0\), iterating the covariance recursion yields
\(\operatorname{Cov}(X_k)=2h_*\sum_{j=0}^{k-1}B^{2j}=\frac{2h_*}{1-q^2}(1-q^{2k})I_d\). Every \(X_k\) is Gaussian with zero mean, giving the complete marginal law. Moreover, the spectral radius \(\rho(I-hA)=\max\{|1-ha|,|1-hb|\}\) is uniquely minimized on \((0,2/b)\) where these two endpoint absolute values agree, namely \(h=h_*\).

For necessity, suppose nonscalar \(A\) has isotropic \(C=cI_d\). Since \(C^{-1}=A-\frac h2A^2\), every eigenvalue \(\lambda\) of \(A\) solves the same scalar quadratic \(\lambda-\frac h2\lambda^2=1/c\). There are at most two roots; nonscalarity forces exactly two distinct positive roots \(a<b\). Subtracting their equations gives \((a-b)(1-h(a+b)/2)=0\), hence \(h=2/(a+b)\), which was shown optimal. No analogous isotropy is possible for three distinct eigenvalues.

**Two-step identification.** For each stable step \(h_j\), put \(C_j=\mathcal C_{h_j}(A)\). The previously proved identity gives \(C_j^{-1}=A-\frac{h_j}{2}A^2\). Multiplying the first by \(h_2\), the second by \(h_1\), and subtracting cancels the quadratic term. Division by \(h_2-h_1\) yields the exact formula, which is valid without simultaneous-diagonalization assumptions beyond those already imposed on \(A\).

## Verification

The companion standalone Python program `verify.py` uses only the standard library and exact rational arithmetic. Executing `python verify.py` checks 690 rational identities, including thirty distinct rational projectors producing the same isotropic covariance, the complete finite-time covariance recursion for fifteen steps each, and independent two-step reconstructions from two stable steps. It also confirms the exact fixed-point Lyapunov equation and the unique-fiber example. These finite tests do **not** prove the statements for arbitrary dimensions or real matrices; the spectral argument above does so.

An illustrative exact case is \(a=1\), \(b=3\), \(h=1/2\). For every rank-one orthogonal projector \(P\) on \(\mathbb R^2\), the drift \(A=3I_2-2P\) is positive definite with eigenvalues \(1,3\), but every such drift produces \(\mathcal C_h(A)=\frac43I_2\) and identical one-time laws from zero. A population covariance at a second stable step, for example \(h_1=1/5\), resolves the ambiguity via the formula above.

## Relationship to prior work

Kirsten et al. (2026, arXiv:2608.09743) derive the exact Euler covariance recursion and show that its **first-order truncation** is equivalent to a deterministic inverse-residual optimization method. Their Theorem 3 recommends \(h=1/(a+b)\) for the spectral radius of that **first-order covariance iteration** (whose error propagator is \(I-2hA\)); this must not be conflated with \(h_*=2/(a+b)\), the minimizer of the **exact Euler transition** \(I-hA\) and its exact covariance mixing rate. At their first-order optimal step, the isotropic collapse established here does not occur for nonscalar \(A\). That recursion is the starting point here, not claimed as new. The present result classifies **all** stable positive-definite drifts sharing an **exact discrete stationary covariance**, links its worst identifiability collapse to the optimal contraction step, proves the finite-time snapshot loss, and gives exact multi-step-size recovery. These consequences are not furnished by a first-order approximation alone.

Aifer et al. (2023/2024, arXiv:2308.05660) establish thermodynamic inversion through the **continuous-time** Ornstein--Uhlenbeck covariance, which is \(A^{-1}\) under the normalization here. Continuous time has no Euler branch ambiguity. Singh, Ghosh, and Adhikari (2018, arXiv:1706.04961) infer OU dynamics from **time-ordered sample paths**, which contain lag information absent from isolated one-time marginals. Van Seeventer and Salehkaleybar (2026, arXiv:2603.08311) study sign identifiability for **continuous-time, generally nonsymmetric** causal drifts with unknown diffusion and known graph; their observational equivalence is different from the present fixed-isotropic-diffusion Euler problem. The scalar fact that stationary AR(1) variance forgets the sign of an autoregressive coefficient is classical; it is not claimed as new. The contribution is the exact matrix-fiber structure and its numerical optimal-step implication.

## Limitations

No claim is made for nonsymmetric drifts, correlated or unknown noise, continuous-time OU observations, nonlinear potentials, or finite-sample statistical uncertainty. The finite-time indistinguishability concerns **individual marginal laws** from zero, not time-correlated path data; lag-one covariance distinguishes the signs. A second-step population covariance solves identifiability algebraically but finite-time simulations, noise, and numerical conditioning may affect empirical reconstruction. Some older system-identification and discrete Lyapunov literature could overlap the stated fiber geometry; the cited comparisons do not independently establish historical priority.

## References

1. G. Kirsten, M. Selby, J. Petangoda, O. Hallqvist Elias, J. Meech, and P. Stanley-Marbell, *Theoretical Analysis of Thermodynamic Matrix Inversion: First-order Equivalence to Preconditioned Gradient Descent and Implications for Analog Computing*, arXiv:2608.09743, first posted August 10, 2026. https://arxiv.org/abs/2608.09743
2. M. Aifer et al., *Thermodynamic Linear Algebra*, arXiv:2308.05660, 2023; npj Unconventional Computing 1, 13 (2024). https://arxiv.org/abs/2308.05660
3. R. Singh, D. Ghosh, and R. Adhikari, *Fast Bayesian inference of the multivariate Ornstein-Uhlenbeck process*, Physical Review E 98, 012136 (2018). https://doi.org/10.1103/PhysRevE.98.012136
4. G. van Seeventer and S. Salehkaleybar, *Sign Identifiability of Causal Effects in Stationary Stochastic Dynamical Systems*, arXiv:2603.08311 (2026). https://arxiv.org/abs/2603.08311
