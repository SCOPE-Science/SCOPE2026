# Gumbel budget crossover and a Gaussian exhaustion-clock edge in Brownian resetting

## Finding

There is a **two-scale termination law** for Brownian target search with a finite budget of resetting attempts. If the reset rate grows so that the dimensionless distance is \(\log n+c\), exhaustion remains neither certain nor negligible: its probability converges to the Gumbel-profile value \(e^{-e^{-c}}\). On the larger termination-time scale, the stopped search clock has a truncated exponential limit with an atom at exhaustion. Within that atom, a narrower Gaussian clock layer survives, and gives an explicit finite-deadline transition profile.

Fix \(a,D>0\) and \(c\in\mathbb R\). For integers \(n\) sufficiently large that \(\log n+c>0\), put
\[
 r_n=\frac{D}{a^2}(\log n+c)^2,\qquad
 \lambda=e^{-c}.
\]
Let \(T_n\) be the time until the first target hit or the \(n\)-th reset alarm, whichever occurs first, and \(F_n\) the event of terminating by that final alarm without a hit. Then
\[
 \Pr(F_n)\longrightarrow e^{-\lambda}=e^{-e^{-c}}.
\]
Moreover, if \(Z_\lambda\) is an exponential variable with rate \(\lambda\), then the following **joint** convergence holds:
\[
 \left(\frac{r_nT_n}{n},\mathbf 1_{F_n}\right)
 \Rightarrow
 \left(\min\{Z_\lambda,1\},\mathbf 1_{\{Z_\lambda>1\}}\right).
\]
Consequently, the limiting time distribution has density \(\lambda e^{-\lambda t}\) on \(0<t<1\) and an atom of size \(e^{-\lambda}\) at \(t=1\). Conditional on success, the limiting time density is \(\lambda e^{-\lambda t}/(1-e^{-\lambda})\) on \(0<t<1\).

**Gaussian exhaustion layer.** Conditionally on \(F_n\),
\[
 \frac{r_nT_n-n}{\sqrt n}\Rightarrow N(0,1).
\]
For every fixed \(y\in\mathbb R\), writing \(\Phi\) for the standard normal distribution function, this gives the finite-deadline edge:
\[
 \Pr\left(T_n\le\frac{n+y\sqrt n}{r_n}\right)
 \longrightarrow 1-e^{-\lambda}+e^{-\lambda}\Phi(y).
\]
The conditional exhaustion mean is exactly
\[
 \mathbb E[r_nT_n\mid F_n]
 =n-\frac{\lambda(\log n+c)}{2(1-\lambda/n)},
\]
and, in particular, has a logarithmic offset that is negligible on the Gaussian \(\sqrt n\)-scale. This exact conditional-mean identity is a specialization of the established finite-budget moment formulas, not a separate novelty claim.

## Assumptions and scope

Consider independent attempts indexed by \(j\ge1\). On each attempt let \(H_j\) be the hitting time of zero by \(X_t=a+\sqrt{2D}W_t\), starting anew at \(a>0\). Let \(E_j\) be an independent exponential alarm of rate \(r_n\); all pairs \((H_j,E_j)\) are mutually independent. The process succeeds at the first attempt satisfying \(H_j<E_j\). If no such success has occurred among attempts \(1,\ldots,n\), it is stopped by alarm \(n\), without starting another search. Exact ties have probability zero. A reset alarm is instantaneous and has no additional return-time cost. The rate \(r_n\) depends on \(n\) as prescribed above, whereas \(a,D,c\) remain fixed.

Let \(J_n=\min\{j\ge1:H_j<E_j\}\) and \(K_n=\min\{J_n,n\}\); then \(F_n=\{J_n>n\}\) and
\[
 T_n=\sum_{j=1}^{K_n}\min\{H_j,E_j\}.
\]

## Proof

**1. Exact one-attempt identities.** The classical Brownian first-hitting Laplace transform is \(\mathbb E[e^{-qH_j}]=e^{-a\sqrt{q/D}}\). Set \(z=a\sqrt{r_n/D}\), \(p=e^{-z}\) and \(Y_j=r_n\min(H_j,E_j)\). Thus
\[
 \Pr(H_j<E_j)=\mathbb E[e^{-r_nH_j}]=p,
 \qquad \Pr(E_j<H_j)=1-p.
\]
For any real \(s>-1\), condition on the alarm duration and integrate the Brownian survival probability:
\[
 f_z(s):=\mathbb E[e^{-sY_j};\ E_j<H_j]
 =\int_0^\infty e^{-(1+s)t}\Pr(r_nH_j>t)\,dt
 =\frac{1-e^{-z\sqrt{1+s}}}{1+s}.
\]
This is an identity of *unnormalized* transforms, with \(f_z(0)=1-p\). Differentiate at zero to find
\[
 \begin{aligned}
 m_z&:=\mathbb E[Y_j\mid E_j<H_j]
 =1-\frac{zp}{2(1-p)},\\
 v_z&:=\operatorname{Var}(Y_j\mid E_j<H_j)
 =2-\frac{p(z^2+5z)}{4(1-p)}-m_z^2.
 \end{aligned}
\]
Furthermore \(\mathbb E[Y_j]=1-p\), by integrating the survival probability up to the independent alarm, and \(\mathbb E[Y_j^2]\le2\), since \(Y_j\le r_nE_j\).

**2. The budget crossover and joint macroscopic clock.** The geometric success index satisfies \(\Pr(J_n>k)=(1-p)^k\). Under the theorem's scaling, \(p=\lambda/n\) *exactly*. Therefore \(J_n/n\Rightarrow Z_\lambda\), \(\Pr(F_n)=(1-\lambda/n)^n\to e^{-\lambda}\), and \(K_n/n\Rightarrow\min\{Z_\lambda,1\}\). The last probability is also the canonical Gumbel distribution function evaluated at \(c\).

For the duration noise, set \(\xi_j=Y_j-(1-p)\). Then \(\xi_j\) are independent and centered with \(\mathbb E[\xi_j^2]\le2\). Because \(\{K_n\ge j\}\) depends only on the outcomes of the first \(j-1\) attempts, the stopped-martingale orthogonality identity gives
\[
 \mathbb E\left[\left(\sum_{j=1}^{K_n}\xi_j\right)^2\right]
 =\sum_{j=1}^n\mathbb E[\xi_j^2\mathbf1_{\{K_n\ge j\}}]
 \le 2n.
\]
Consequently,
\[
 \frac{r_nT_n}{n}-\frac{K_n}{n}
 =\frac{1}{n}\sum_{j=1}^{K_n}\xi_j
 -p\frac{K_n}{n}\xrightarrow{L^2}0.
\]
The joint limit follows by continuous mapping from \(J_n/n\) to the pair \((\min(J_n/n,1),\mathbf1_{\{J_n/n>1\}})\). The mapping is discontinuous only at \(1\), an event of zero limiting exponential probability. The asserted macroscopic density and atom are the law of this pair's first coordinate.

**3. Conditional central limit theorem at exhaustion.** On \(F_n\), each of the first \(n\) attempts has \(E_j<H_j\). By independence the conditional \(Y_j\) are themselves independent and identically distributed, each with transform \(f_z(s)/(1-p)\). At \(z=\log n+c\), the above formulas give
\[
 m_z=1-O\left(\frac{\log n}{n}\right),
 \qquad v_z=1+O\left(\frac{(\log n)^2}{n}\right).
\]
The conditional third absolute moments are uniformly bounded: \(Y_j\le r_nE_j\) and therefore
\(\mathbb E[Y_j^3\mid E_j<H_j]\le6/(1-p)\). In particular, \(v_z\to1\) and the triangular-array Lyapunov central limit theorem applies to \(\sum_{j=1}^n(Y_j-m_z)\), conditioned on \(F_n\). Its mean displacement is exactly \(nm_z-n=-\lambda(\log n+c)/(2(1-\lambda/n))=o(\sqrt n)\). Thus \((r_nT_n-n)/\sqrt n\mid F_n\Rightarrow N(0,1)\).

**4. Narrow deadline limit.** For fixed \(y\), all successful paths contribute asymptotically to the event \(r_nT_n\le n+y\sqrt n\): from the joint macroscopic convergence, a successful path ending at scaled time at least \(1-\varepsilon\) has limiting probability no more than \(\Pr(1-\varepsilon\le Z_\lambda\le1)\), which vanishes as \(\varepsilon\downarrow0\). Meanwhile the failing paths have mass approaching \(e^{-\lambda}\) and their conditioned clock has the standard Gaussian limit in Step 3. Addition yields \(1-e^{-\lambda}+e^{-\lambda}\Phi(y)\). This proves all statements.

## Verification

The standalone Python 3 script `check.py` verifies the one-attempt unnormalized Laplace transform against independent quadrature of the Brownian survival integral; differentiation formulas for conditional moments; finite-budget Gumbel probabilities; triangular-array variance convergence; centered Gaussian moment-generating-function behavior; and exact stopped means. It uses only the standard library. Execute `python3 check.py` in the extracted package directory. The script reports `PASS: 76 exact-identity, integration, moment and asymptotic diagnostics`. These finite diagnostics support but do not replace the analytic proof above. In particular, no finite computation alone proves an infinite asymptotic or a claim of publication priority.

## Relationship to prior work

Bressloff (2023/2024) formulated the finite-reset-count Brownian search and derived its **exact finite-budget** splitting probabilities and conditional mean first-passage times. Those results and the finite-budget survival factor \((1-p)^n\) are not new here. Linn and Lawley (2023) proved frequent-resetting exponential first-passage limits for **unrestricted** searching. Sunil et al. (2023) gave a joint time/reset-count transform that already contains exact finite-count renewal information. The present theorem addresses the different *joint regime* where the count bound and reset rate diverge together: its sharp Gumbel crossover, atom-resolved joint stopped-clock law, conditional Gaussian exhaustion layer and narrow-deadline profile. None of the three examined primary-source treatments was found to state this assembled two-scale limit theorem. It may nevertheless be derivable as a corollary of more general renewal-limit work not located in the accessible searches; uniqueness or publication priority is not claimed.

## Limitations

This is a theorem for independent one-dimensional Brownian searches with absorption at a point, instantaneous returns to the same fixed initial position, a constant Poisson reset rate within each experiment, and the stated joint scaling. There are no claims for non-Poisson resets, target motion, dependent attempts, additional return delays, optimal search policy, or finite-sample inference. No quantitative uniform-in-\(c\) error bound is asserted. Existing exact finite-budget identities and unrestricted-reset exponential limits remain credited prior work. Independent scientific assessment has not been performed.

## References

1. P. C. Bressloff, “Truncated stochastically switching processes,” arXiv:2310.20502, first submitted 2023-10-31; *Physical Review E* 109, 024103 (2024). https://arxiv.org/abs/2310.20502
2. S. Linn and S. D. Lawley, “First passage times under frequent stochastic resetting,” arXiv:2302.05409, first submitted 2023-02-10; *Physical Review E* 108, 024114 (2023). https://arxiv.org/abs/2302.05409
3. J. C. Sunil, R. A. Blythe, M. R. Evans and S. N. Majumdar, “The cost of stochastic resetting,” arXiv:2304.09348, first submitted 2023-04-19; *Journal of Physics A: Mathematical and Theoretical* 56, 395001 (2023). https://arxiv.org/abs/2304.09348
