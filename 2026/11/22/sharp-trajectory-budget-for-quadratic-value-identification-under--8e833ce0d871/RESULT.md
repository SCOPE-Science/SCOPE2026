# Sharp trajectory budget for quadratic-value identification under spectral collisions

## Finding

Let \(F\in\mathbb R^{n\times n}\) be diagonalizable over the real numbers, and consider a single unknown symmetric matrix \(P\). For each of \(r\ge1\) independently chosen initial states \(x_0^{(k)}\), observe the noiseless quadratic values \((x_t^{(k)})^\top P x_t^{(k)}\) along \(x_t^{(k)}=F^t x_0^{(k)}\) at times \(0\le t<H\). These values may, for example, be regression targets in quadratic terminal-value fitting.

Write the eigenvalues of \(F\), with algebraic multiplicity, as \(\lambda_1,\ldots,\lambda_n\). For each distinct product \(\mu\) among \(\lambda_i\lambda_j\), \(1\le i\le j\le n\), define its *symmetric-product multiplicity*
\[
m_\mu=\#\{(i,j):1\le i\le j\le n,\ \lambda_i\lambda_j=\mu\}.
\]
Let \(s\) be the number of distinct products and suppose \(H\ge s\). Then the exact maximum possible rank of the linear quadratic-regression design, over all choices of the \(r\) initial states, is
\[
\boxed{\max_{x_0^{(0)},\ldots,x_0^{(r-1)}}\operatorname{rank}\mathcal M
=\sum_\mu\min\{r,m_\mu\}.}
\]
Consequently the **minimum number of independently initialized trajectories** permitting unique reconstruction of an unrestricted symmetric \(P\) is exactly
\[
\boxed{r_\star=\max_\mu m_\mu.}
\]
The maximum is attained by an explicit deterministic choice of initial states and by almost every choice drawn from any absolutely continuous distribution. If \(r<r_\star\), even restricting \(P\) to positive-definite matrices does not restore identifiability.

A sharp illustrative family is \(\lambda_i=c a^{i-1}\) for \(0<a,c<1\): here \(s=2n-1\), a single trajectory has maximum quadratic-regression rank \(2n-1\), and exactly \(\lceil n/2\rceil\) trajectories suffice and are necessary. For \(n\ge3\), one trajectory never identifies all \(n(n+1)/2\) coefficients, no matter how long it is observed, although the eigenvalues are distinct and a modal-nonzero initial state is cyclic for ordinary linear state dynamics.

## Assumptions and scope

All vector spaces and matrices are real, all calculations exact, and the target \(P\in\mathbb S^n\) is otherwise unrestricted. The same known, fixed, real-diagonalizable transition matrix \(F\) governs each trajectory, which can be initialized independently. A trajectory produces one scalar quadratic value per sampling instant; measurements use common integer times \(0,\ldots,H-1\), with \(H\ge s\). Eigenvalues may be zero, negative or repeated. This theorem is about the rank of direct quadratic-value measurements, **not** the observability of an unknown state from a known quadratic sensor or the identification of an unknown dynamics matrix.

The regression operator is \(\mathcal M: \mathbb S^n\to\mathbb R^{rH}\), with \((\mathcal M(P))_{k,t}=(F^t x_0^{(k)})^\top P(F^t x_0^{(k)})\). Its rank is independent of the choice of vectorization of symmetric matrices.

## Proof

**1. Diagonal modal reduction.** Choose a real nonsingular \(V\) such that \(F=V\operatorname{diag}(\lambda_1,\ldots,\lambda_n)V^{-1}\). Set \(z^{(k)}=V^{-1}x_0^{(k)}\) and \(Q=V^\top PV\). Congruence is an invertible bijection of symmetric matrices. Define independent coordinates \(q_{ii}=Q_{ii}\) and \(q_{ij}=2Q_{ij}\) for \(i<j\). The measured scalar at time \(t\) becomes
\[
\sum_{1\le i\le j\le n}q_{ij}\,z_i^{(k)}z_j^{(k)}(\lambda_i\lambda_j)^t.
\]
Thus the design column associated with \((i,j)\) is the tensor product of the temporal vector \((1,\mu,\ldots,\mu^{H-1})\), \(\mu=\lambda_i\lambda_j\), and the \(r\)-vector \((z_i^{(k)}z_j^{(k)})_{k=0}^{r-1}\).

**2. Universal upper bound.** Group columns by their common spectral product \(\mu\). Every group has column rank at most \(\min\{r,m_\mu\}\), since every column in that group has the same nonzero temporal factor. Summing group ranks proves the asserted upper bound for *all* choices of initial states. The temporal factor is nonzero also for \(\mu=0\), since its time-zero entry is one.

**3. One explicit family simultaneously attains every group bound.** Let
\[
b_i=2^{2^{i-1}}>0,\qquad z_i^{(k)}=b_i^k,
\qquad 1\le i\le n,\quad 0\le k<r.
\]
For unordered pairs \((i,j)\), the products \(\gamma_{ij}=b_i b_j\) are pairwise distinct: their base-two exponents \(2^{i-1}+2^{j-1}\) uniquely encode the unordered pair, including diagonal pairs by carrying. Therefore, inside each product class \(\mu\), the coefficient matrix is an ordinary Vandermonde matrix with rows \(k=0,\ldots,r-1\) and distinct nodes \(\gamma_{ij}\). Its rank is exactly \(\min\{r,m_\mu\}\).

Since \(H\ge s\), the temporal Vandermonde matrix with nodes equal to the \(s\) distinct real products \(\mu\) has full column rank. Applying a left inverse to its temporal index separates different product classes without mixing their \(r\) coefficient vectors. Hence the full design has rank equal to the **sum** of their separate Vandermonde ranks. This attains the upper bound. The initial conditions are the real vectors \(x_0^{(k)}=Vz^{(k)}\), so the construction obeys the rank-one form imposed by actual trajectories.

**4. Genericity and necessity.** Each possible maximal minor of the design is a polynomial in the \(rn\) real modal initial-state coordinates. The explicit construction proves at least one minor of the maximum rank is a nonzero polynomial. Its zero set has Lebesgue measure zero, and the complement is Zariski open and dense. Thus generic initializations achieve the maximal rank. Full identification is equivalent to rank \(d=n(n+1)/2=\sum_\mu m_\mu\); by the formula this holds exactly when \(r\ge \max_\mu m_\mu\). If rank is smaller, choose a nonzero symmetric \(\Delta\in\ker\mathcal M\). For sufficiently small \(\epsilon>0\), both \(I+\epsilon\Delta\) and \(I-\epsilon\Delta\) are positive definite and yield identical measured values. Thus even positivity cannot resolve the ambiguity.

**5. Geometric stable spectra.** For \(\lambda_i=c a^{i-1}\), distinct products are \(c^2a^h\) at exponents \(h=0,\ldots,2n-2\), hence \(s=2n-1\). The number of unordered pairs with \(i+j=h+2\) has maximum \(\lceil n/2\rceil\), at the central exponent(s), by direct enumeration of integer pairs within \(1\le i\le j\le n\). The conclusions follow from the general formula. For \(n\ge3\), \(2n-1<n(n+1)/2\). Because all eigenvalues are distinct and every entry of \(z^{(0)}\) equals one, the ordinary Krylov matrix \((z^{(0)},\Lambda z^{(0)},\ldots,\Lambda^{n-1}z^{(0)})\) is nonsingular, illustrating the distinction from ordinary linear cyclicity.

## Verification

`CHECKER.py` checks the derived design rank by modular Gaussian elimination for 63 exact-rational-spectrum families (geometric, all-equal, all-zero, signed, and partially repeated spectra) and 643 choices of trajectory count. Each predicted rank comes from the exact multiplicity formula; every tested constructed design achieves it. The script uses a prime modulus and therefore is a supplementary finite check, not a proof over the reals. The analytic proof above handles all dimensions, real eigenvalues, and allowed initial conditions; no completeness assertion depends on finite enumeration.

To reproduce: place `CHECKER.py` beside this document and execute `python3 CHECKER.py` with a standard Python 3 interpreter. No external packages are required.

## Relationship to prior work

Baltussen et al. (2026), Section 2.2 and their equation (6), fit symmetric terminal-cost matrices by least squares on closed-loop quadratic samples and require full quadratic-regression rank; they explicitly permit extra trajectories, initial conditions, or excitation when rank is insufficient. They do not give the spectrum-dependent exact rank or minimum count proved here.

Zhou (2016) proves that **unrestricted linear** output matrices for a fixed state transition need a number of rows equal to the largest geometric eigenvalue multiplicity. Applying that general theory to the symmetric-square lifted system suggests the *lower bound* given by product multiplicities. But a lifted output matrix generated by actual initial states has a restrictive rank-one quadratic structure; the unrestricted-sensor sufficiency theorem does not furnish the structured sufficiency or explicit simultaneous Vandermonde construction established here. Zhou explicitly raises structured sensor restrictions as a separate problem.

Van Waarde et al. (2020) develop collective persistency of excitation from multiple input-driven trajectories for general linear systems, rather than the spectral classification of unforced quadratic-value measurements. Gosea and Gugercin (2022) study frequency-domain interpolation of input/output linear systems with quadratic output; Berkane et al. (2023) study state estimation when quadratic output matrices are known. These are different inverse problems. Tu and Recht (2018) study LQR policy evaluation with stochastic excitation and statistical sample complexity, rather than deterministic fixed-dynamics exact rank.

## Limitations

The number \(r_\star\) is sharp given at least \(s\) observation times **per trajectory**; this is not a sharp joint time-versus-trajectories budget when \(H<s\). The exponentially separated explicit modal start may be numerically ill-conditioned and physically infeasible under state bounds; generic starts establish existence but no condition-number bound. There is no claim for nondiagonalizable transitions, complex eigenvalue pairs represented only over the complex numbers, unequal observation times, noisy regression, stochastic exploration, or feedback changing within a trajectory. Rank deficiency of the regression design alone does not imply that a value matrix constrained by a known Riccati or Lyapunov equation is unidentifiable by other means. No independent mathematical audit has been performed.

## References

1. T. M. J. T. Baltussen, N. P. Lawrence, A. Katriniok, A. Mesbah, W. P. M. H. Heemels, *Policy Iteration over Terminal Cost Functions: From LQR to MPC* (2026), arXiv:2611.03401v1, https://arxiv.org/abs/2611.03401 . First publicly posted 2026-11-02 (UTC).
2. T. Zhou, *Minimal Inputs/Outputs for a Networked System* (2016), arXiv:1610.00063, https://arxiv.org/abs/1610.00063 .
3. H. J. van Waarde, C. De Persis, M. K. Camlibel, P. Tesi, *Willems' Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets* (2020), arXiv:2002.01023, https://arxiv.org/abs/2002.01023 .
4. I. V. Gosea, S. Gugercin, *Data-Driven Modeling of Linear Dynamical Systems with Quadratic Output in the AAA Framework* (2022), Journal of Scientific Computing 91, 16, https://doi.org/10.1007/s10915-022-01771-5 .
5. S. Berkane, D. Theodosis, T. Hamel, D. V. Dimarogonas, *State Estimation for Linear Systems with Quadratic Outputs* (2023), arXiv:2312.10684, https://arxiv.org/abs/2312.10684 .
6. S. Tu, B. Recht, *The Gap Between Model-Based and Model-Free Methods on the Linear Quadratic Regulator: An Asymptotic Viewpoint* (2018), arXiv:1812.03565, https://arxiv.org/abs/1812.03565 .
