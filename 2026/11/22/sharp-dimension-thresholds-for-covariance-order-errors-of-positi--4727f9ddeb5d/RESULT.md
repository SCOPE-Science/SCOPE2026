# Sharp dimension thresholds for covariance-order errors of positive integrating-factor Runge–Kutta quadratures

## Finding

**Theorem (first omitted covariance moment controls the exact Loewner-sign phase).** Let \(T>0\), \(m\ge1\), and let \(\mathcal Q\) be a finite quadrature on \([0,T]\) with distinct nodes and strictly positive weights, integrating polynomials of degree at most \(2m-1\) exactly, but not the monomial of degree \(2m\). Put
\[
\varepsilon_{2m}=\mathcal Q(t^{2m})-\frac{T^{2m+1}}{2m+1}\ne0.
\]
For each dimension \(n\ge1\), take the nilpotent shift \(A e_j=e_{j+1}\) for \(j<n\), \(Ae_n=0\), and \(b=e_1\). Let \(X_T\) be the solution at time \(T\) of
\[
\dot X=AX+XA^{\mathsf T}+bb^{\mathsf T},\qquad X(0)=0,
\]
and \(X_{\mathcal Q}\) the covariance obtained by replacing its exact variation-of-constants integral by \(\mathcal Q\). Both covariances are positive semidefinite, and \(X_T\) is positive definite. The **signed numerical covariance error** \(E=X_{\mathcal Q}-X_T\) satisfies, for every positive \(T\):

- If \(n\le m\), the numerical covariance is exact: \(E=0\).
- If \(n=m+1\), the signed error has rank one, with the exact identity \(E=\varepsilon_{2m}(m!)^{-2}e_{m+1}e_{m+1}^{\mathsf T}\).
- If \(n\ge m+2\), the error is indefinite (has both positive and negative eigenvalues), with the explicit two-by-two principal minor
\[
\det E_{\{m,m+2\},\{m,m+2\}}=-\left(\frac{\varepsilon_{2m}}{(m-1)!(m+1)!}\right)^2<0.
\]

If \(r\) distinct quadrature nodes have positive weights, \(\operatorname{rank}(X_{\mathcal Q})=\min(n,r)\).

**Sharp application to two recent positive integrators.** For the IF-SSPRK2 and IF-SSPRK3 differential Lyapunov schemes of Zhang, Lan, and Jing (2026), let \(N\ge1\) equal steps of length \(h=T/N\), with constant forcing \(bb^{\mathsf T}\). The transformed equations reduce their completed covariance updates exactly to the composite trapezoidal and composite Simpson rules. Thus:

| Scheme | Exact dimension | One-sided, nonzero error | Indefinite error | Rank after \(N\) steps |
| --- | --- | --- | --- | --- |
| IF-SSPRK2 | \(n=1\) | \(n=2:\ E=(Th^2/6)e_2e_2^{\mathsf T}\) | every \(n\ge3\) | \(\min(n,N+1)\) |
| IF-SSPRK3 | \(1\le n\le2\) | \(n=3:\ E=(Th^4/480)e_3e_3^{\mathsf T}\) | every \(n\ge4\) | \(\min(n,2N+1)\) |

The respective indefinite-case principal minors are exactly \(-T^2h^4/144\) and \(-T^2h^8/518400\). These statements hold **for every** positive stepsize and completed step count, not merely in an asymptotic refinement regime.

## Assumptions and scope

All matrices are real and of arbitrary finite dimension. The source is the constant rank-one positive semidefinite matrix \(bb^{\mathsf T}\), the initial covariance is zero, and the drift in the exact phase diagram is the controllable nilpotent chain specified above. The continuous and numerical objects are finite-horizon covariances, not stationary solutions. Numerical quadrature weights are strictly positive; in the general theorem, the nodes can be arbitrary distinct points of \([0,T]\), subject to the exactness assumptions. No numerical floating-point rounding is involved.

## Proof

**1. Reduction to a polynomial covariance moment matrix.** By nilpotency,
\[
v(t)=e^{tA}b=\left(1,t,\frac{t^2}{2!},\ldots,\frac{t^{n-1}}{(n-1)!}\right)^{\mathsf T}.
\]
Variation of constants gives \(X_T=\int_0^T v(t)v(t)^{\mathsf T}\,dt\). If \(c\ne0\), the polynomial \(c^{\mathsf T}v(t)\) is nonzero, and its square has strictly positive integral. Hence \(X_T\succ0\). Positive quadrature gives \(X_{\mathcal Q}\succeq0\). With indices starting at zero, the signed-error entries are
\[
E_{ij}=\frac{\mathcal Q(t^{i+j})-T^{i+j+1}/(i+j+1)}{i!j!},\qquad 0\le i,j<n.
\]

**2. Exact sign classification.** All moments through degree \(2m-1\) have zero error. If \(n\le m\), every entry has \(i+j\le2m-2\), hence \(E=0\). If \(n=m+1\), the only entry with degree \(2m\) is the bottom-right entry \((i,j)=(m,m)\), giving the claimed rank-one identity. For \(n\ge m+2\), the principal minor with zero-based indices \(i=m-1\) and \(j=m+1\) has \(E_{ii}=0\), whereas \(E_{ij}=\varepsilon_{2m}/((m-1)!(m+1)!)\ne0\). Its determinant is the stated strictly negative number. A real symmetric matrix with a negative principal two-by-two determinant has both positive and negative eigenvalues; therefore neither one-sided Loewner comparison is possible.

**3. Rank is controlled exactly by evaluation nodes.** The covariance quadrature is a positively weighted sum of outer products of \(v(t_j)\). Its rank equals the rank of the matrix whose columns are the vectors \(v(t_j)\), because every weight is positive. The first \(\min(n,r)\) rows form an ordinary Vandermonde evaluation matrix, rescaled by nonzero factorials; its columns or rows, as appropriate, have full possible rank at distinct nodes. Therefore \(\operatorname{rank}X_{\mathcal Q}=\min(n,r)\). This establishes the sharp nonsingularity thresholds, not just upper bounds on rank.

**4. Identification of the published completed integrators.** Set \(W(t)=e^{-tA}X(t)e^{-tA^{\mathsf T}}\) and \(F(t)=e^{-tA}bb^{\mathsf T}e^{-tA^{\mathsf T}}\). Then \(W'=F(t)\). For a state-independent forcing, the published two-stage SSP formula completes as \(W_{k+1}=W_k+h(F(t_k)+F(t_{k+1}))/2\); the three-stage formula completes as
\[
W_{k+1}=W_k+\frac h6\big(F(t_k)+4F(t_k+h/2)+F(t_{k+1})\big).
\]
After conjugation by \(e^{TA}\), their quadratures act on \(v(T-t)v(T-t)^{\mathsf T}\); symmetry under \(t\mapsto T-t\) gives the same composite rules acting on \(v(t)v(t)^{\mathsf T}\).

The trapezoidal rule has \(m=1\) and \(\varepsilon_2=Th^2/6\) (one-panel error \(h^3/6\)); Simpson's rule has \(m=2\) and \(\varepsilon_4=Th^4/120\) (one-panel error \(h^5/120\)). Substitution in the general formula gives all signed-error coefficients and minors above. Their distinct positive node counts are \(N+1\) and \(2N+1\), yielding the exact numerical rank formulas.

**5. Stable perturbations of the indefinite examples.** Replace the nilpotent drift by \(A_\delta=A-\delta I\), where \(\delta>0\). This matrix is Hurwitz. Its continuous covariance is positive definite since \(e^{tA_\delta}b=e^{-\delta t}v(t)\) and the polynomial cannot vanish on an interval. At any fixed \(T>0\) and positive integer \(N\), the numerical and exact matrix entries depend continuously on \(\delta\). The displayed negative principal minors therefore remain negative for all sufficiently small \(\delta>0\), establishing stable examples with indefinite numerical covariance *error*. The numerical covariance itself remains positive semidefinite. No uniform perturbation radius over all \(T,N\) is asserted.

## Verification

The standalone `verify.py` uses Python rational arithmetic and SymPy exact matrix rank. It tests the exact first omitted moment, all entries of the covariance errors at the low-dimensional boundaries, the strict negative principal minors, and the exact rank formulas over dimensions \(1\) through \(7\) and panel counts \(1\) through \(4\), for both published schemes at \(T=7/5\). All \(56\) dimension/panel checks pass. The proof above establishes the arbitrary-dimension statements; the finite tests alone do not.

## Relationship to prior work

Zhang, Lan, and Jing introduce the IF-SSPRK2/3 integrating-factor differential Lyapunov schemes, establish positivity of the numerical covariance, and prove a norm-error estimate for IF-SSPRK2. These results do not classify the **sign of the matrix error** in Loewner order, its first one-sided dimension, or the exact finite-horizon rank thresholds for the controllable nilpotent chain.

Existing published research records study, separately, a planar-rotation covariance aliasing boundary for the same two integrators, a stationary four-mode error-inertia theorem for positive exponential quadratures, and a universal Loewner upper-bound condition for second-order covariance trapezoids. A result for a rotating planar system does not imply this polynomial-chain phase diagram; a stationary negative/positive inertia result for distinct real decay modes does not determine the finite-time rank-one and indefinite crossover here. The general first-omitted-moment mechanism is closely related to classical moment-matrix and quadrature exactness theory, so independent confirmation of historical priority remains necessary.

## Limitations

The complete classification applies to a nilpotent controllable chain and a rank-one constant source, not to arbitrary drifts, nonlinear matrix forcing, or arbitrary initial covariance. For dimensions beyond the thresholds, the claim is that the **difference** between two positive semidefinite covariances is indefinite; it is **not** that the numerical covariance becomes indefinite. Stable perturbations are only guaranteed at each fixed physical horizon and panel count. The rank formulas assume strictly positive weights and exact arithmetic. The analysis is finite-horizon and does not address stationary covariance or roundoff sensitivity.

## References

1. W. Zhang, R. Lan, X. Jing, “Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation,” arXiv:2606.15703v1 (14 June 2026), https://arxiv.org/abs/2606.15703 .
2. L. N. Trefethen, “Exactness of Quadrature Formulas,” *SIAM Review* 64 (2022), 132–150, https://doi.org/10.1137/20M1389522 .
3. C. Berg and R. Szwarc, “A determinant characterization of moment sequences with finitely many mass-points,” arXiv:1405.7267, https://arxiv.org/abs/1405.7267 .
