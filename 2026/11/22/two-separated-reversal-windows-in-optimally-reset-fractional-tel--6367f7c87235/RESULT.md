# Two separated reversal windows in optimally reset fractional-telegrapher searches

## Finding

Fix an anomalous exponent \(0<\mu<1\), fractional transport coefficient \(K>0\), clock scale \(\tau>0\), and target distance \(L>0\). Compare the two homogeneous fractional-telegrapher search models FTE-I and FTE-II of Górska et al. under independent complete Poisson resetting to the starting point. Their mean first-passage times, quoted from equations (31) and (40) of [1], are
\[
T_I(r,L)=\frac{\exp\!\left[L\sqrt{r^\mu(1+(\tau r)^\mu)/K}\right]-1}{r},\quad
T_{II}(r,L)=\frac{\exp\!\left[L\sqrt{r^\mu(1+\tau r)/K}\right]-1}{r}.
\]
Here the second expression is the renewal-consistent reading of the printed equation (40), as also enforced by its stationarity equation (41) and the ordinary-telegraph limit.

Define the dimensionless quantities \(x=r\tau\), \(a=L/\sqrt{K\tau^\mu}\), the shape functions
\[
h_I(x)=x^{\mu/2}\sqrt{1+x^\mu},\qquad h_{II}(x)=x^{\mu/2}\sqrt{1+x},
\]
and dimensionless MFPTs \(F_j(x,a)=[e^{a h_j(x)}-1]/x\), so \(T_j=\tau F_j\). Write \(x_j(a)\) for an optimally chosen dimensionless resetting rate, and \(m_j(a)=F_j(x_j(a),a)\).

**Theorem (separated optimal reversals).** For every \(a>0\), each \(F_j(\cdot,a)\) has exactly one global minimizer. Let \(z(\eta)>0\), for \(0<\eta<1\), be the unique positive solution of \(\eta z=1-e^{-z}\). Define
\[
b_{II}=\frac{z((2\mu+1)/4)}{\sqrt2},\qquad b_I=\frac{z(3\mu/4)}{\sqrt2}.
\]
There is a unique \(\chi\in(0,1)\) solving
\[
\mu \chi^{\mu-1}=1+(1-\mu)\chi^\mu,
\]
and define
\[
\eta_\chi=\frac\mu2+\frac\mu2\frac{\chi^\mu}{1+\chi^\mu},\qquad
b_\chi=\frac{z(\eta_\chi)}{\chi^{\mu/2}\sqrt{1+\chi^\mu}}.
\]
These constants obey \(0<b_{II}<b_I<b_\chi\). The **optimized MFPT preference** satisfies
\[
m_I(a)<m_{II}(a)\ \ (0<a\le b_{II}),\qquad
m_I(a)>m_{II}(a)\ \ (a\ge b_I),
\]
with at least one equality for \(a\in(b_{II},b_I)\) and no equality outside this open interval. The **optimal reset-rate preference** instead satisfies
\[
x_I(a)>x_{II}(a)\ \ (0<a\le b_I),\qquad
x_I(a)<x_{II}(a)\ \ (a\ge b_\chi),
\]
with at least one equality for \(a\in(b_I,b_\chi)\) and none outside. Thus all cost-reversal points lie strictly *before* all rate-reversal points in dimensionless target distance. These statements do not assert uniqueness of either crossover within its bracket.

For completeness, write \(\eta_0=\mu/2\), \(z_0=z(\eta_0)\). The short- and long-target asymptotics are
\[
\begin{aligned}
 x_I(a)&\sim [z(\mu)/a]^{1/\mu},
 &m_I(a)&\sim C_\mu a^{1/\mu},\\
 x_{II}(a)&\sim [z((1+\mu)/2)/a]^{2/(1+\mu)},
 &m_{II}(a)&\sim C_{(1+\mu)/2}a^{2/(1+\mu)}\quad(a\downarrow0),
\end{aligned}
\]
where \(C_\eta=(e^{z(\eta)}-1)/z(\eta)^{1/\eta}\). As \(a\to\infty\), both optimal rates are asymptotic to \(x_0(a)=[z_0/a]^{2/\mu}\), while the *difference* of optimized MFPTs has the sharp positive law
\[
m_I(a)-m_{II}(a)\sim\frac12 e^{z_0}z_0\,x_0(a)^{\mu-1}.
\]

## Assumptions and scope

The theorem compares two prescribed first-passage mean formulas of [1] on the whole domain \(0<\mu<1\), \(a>0\), \(x>0\), with identical positive \(K,\tau,L\) and independent complete resets. No spatial heterogeneity, partial resets, finite reset duration, or change of fractional exponent between models is allowed. For \(\mu=1\), the two means coincide identically and there is no strict reversal. The physical rate and target distance are recovered by \(r=x/\tau\) and \(L=a\sqrt{K\tau^\mu}\).

## Proof

**1. Unique global minimizers.** For each model put \(\eta_j(x)=xh'_j(x)/h_j(x)\). Elementary differentiation gives
\[
\eta_I(x)=\frac\mu2+\frac\mu2\frac{x^\mu}{1+x^\mu},\qquad
\eta_{II}(x)=\frac\mu2+\frac12\frac{x}{1+x}.
\]
Each is strictly increasing, takes values in \((\mu/2,1)\), and has limiting values \(\mu\) and \((1+\mu)/2\), respectively. The function \(\Phi(z)=z/(1-e^{-z})\) is strictly increasing on positive \(z\), from \(1\) to infinity: \(\Phi'(z)>0\) follows from \(e^z>1+z\). The sign of \(\partial_x F_j(x,a)\) equals the sign of \(\eta_j(x)\Phi(ah_j(x))-1\). This expression is strictly increasing from \(\mu/2-1<0\) to infinity. Moreover \(F_j\to\infty\) both as \(x\downarrow0\) (since \(\mu/2<1\)) and as \(x\to\infty\). Therefore a unique stationary point exists and is the unique global minimum. Its continuity and strict decrease in \(a\) follow from the strict monotonic root equation.

**2. Exact cost window.** For fixed \(x\ne1\), the sign of \(F_I(x,a)-F_{II}(x,a)\) is the sign of \(x^\mu-x\). Thus model II is better for \(0<x<1\), and model I is better for \(x>1\). At \(x=1\), the optimizer condition is \(\eta_j(1)\Phi(a\sqrt2)=1\). The two elasticities there are \(3\mu/4\) and \((2\mu+1)/4\), the latter strictly larger. The positive root \(z(\eta)\) exists uniquely and decreases strictly with \(\eta\), so \(0<b_{II}<b_I\). For \(a\le b_{II}\), the II minimizer lies at or to the right of one, and testing its position in the I objective gives \(m_I<m_{II}\); equality of the two objectives exactly at \(x=1\) does not spoil strictness because the I minimizer lies strictly to the right at \(a=b_{II}\). Likewise, for \(a\ge b_I\), testing the I minimizer in the II objective gives \(m_{II}<m_I\), including strictness at \(a=b_I\). Continuity of both optimized costs gives at least one internal crossing.

**3. Exactly separated reset-rate window.** A direct subtraction shows that \(\eta_I(x)-\eta_{II}(x)\) has the sign of
\[
g(x)=\mu x^{\mu-1}-1-(1-\mu)x^\mu.
\]
The function \(g\) decreases strictly from infinity to a negative value at \(x=1\), yielding a unique \(\chi\in(0,1)\). At \(x\ge1\), both \(h_I<h_{II}\) and \(\eta_I<\eta_{II}\), hence the II derivative-sign expression exceeds that of I; when \(x_I\ge1\), necessarily \(x_{II}<x_I\). This covers \(a\le b_I\). At \(0<x\le\chi\), both inequalities reverse: \(h_I>h_{II}\), \(\eta_I\ge\eta_{II}\), so for \(x_I\le\chi\), necessarily \(x_I<x_{II}\). By the optimality equation, \(x_I=\chi\) exactly when \(a=b_\chi\). Since \(x_I(b_I)=1\) and \(x_I\) decreases strictly, \(b_\chi>b_I\). For \(a\ge b_\chi\), the reverse ordering is strict. Continuity proves at least one rate crossing in \((b_I,b_\chi)\). The two brackets are disjoint.

**4. Asymptotic boundaries.** For \(x\to\infty\), the shapes obey \(h_I\sim x^\mu\), \(h_{II}\sim x^{(1+\mu)/2}\) and their elasticities approach the corresponding exponents. The stationary equation \(\eta_j(x)\Phi(ah_j(x))=1\) yields \(ah_j(x_j)\to z(\eta_\infty)\) as \(a\downarrow0\). Substitution gives the stated small-target rates and costs. In particular \(m_I/m_{II}\to0\).

For \(a\to\infty\), set \(x_0=(z_0/a)^{2/\mu}\) and \(x=x_0u\). Both scaled objectives converge uniformly on compact positive \(u\)-sets to \(f(u)=[e^{z_0u^{\mu/2}}-1]/u\), with its unique nondegenerate minimum at \(u=1\) and divergence at both ends. Moreover \(F_j\) dominates the common base objective since \(h_j(x)\ge x^{\mu/2}\), ensuring minimizing \(u\)'s remain in a compact neighborhood of one. Taylor expansion on that neighborhood gives
\[
\begin{aligned}
 x_0F_I(x_0u,a)&=f(u)+\tfrac12 z_0u^{3\mu/2-1}e^{z_0u^{\mu/2}}x_0^\mu+O(x_0^{2\mu}),\\
 x_0F_{II}(x_0u,a)&=f(u)+\tfrac12 z_0u^{\mu/2}e^{z_0u^{\mu/2}}x_0+O(x_0^2).
\end{aligned}
\]
Nondegeneracy of the minimum and the standard first-order optimal-value perturbation argument imply \(x_0m_I= f(1)+\tfrac12 z_0e^{z_0}x_0^\mu+o(x_0^\mu)\) and \(x_0m_{II}=f(1)+O(x_0)\). As \(0<\mu<1\), the II correction is negligible compared with the I correction. Division by \(x_0\) gives the claimed positive difference and \(x_I/x_0,x_{II}/x_0\to1\).

## Verification

Run `python check.py` from this package after installing `scipy` from `requirements.txt`. It evaluates the two independent stationary equations with bracketed root finding, checks the strict analytic brackets for five exponents, resolves sample cost- and rate-reversal locations, and tests the two asymptotic regimes. The 225 deterministic assertions passed for the package source. These tests check numerical consistency, not the infinite-domain quantifiers, which are proved above.

For \(\mu=1/2\), the analytical brackets and representative numerical crossover locations are \(b_{II}\approx1.12686252094\), cost crossing \(a\approx1.44141310360\), \(b_I\approx1.72002612735\), rate crossing \(a\approx3.05842781641\), and \(b_\chi\approx3.82609216005\). The numbers are examples, not uniqueness certificates.

## Relationship to prior work

Górska, Sevilla, Chacón-Acosta, and Sandev [1] derived both first-passage MFPTs, exhibited existence of rate optima and studied their dependence on the anomalous exponent, separately for each model. Thus the MFPT formulas, existence of some optimizer, fixed-rate equality at \(r\tau=1\), and original first-order stationarity equations are not claimed here. The new statement compares **globally optimized** costs and **uniquely optimal** rate choices *between* the two different temporal fractionalizations, proving strict, nonoverlapping analytical windows for their two different order reversals and sharp extreme-target laws. Sandev, Singh, Méndez, and Kocarev [2] study **heterogeneous spatial** telegrapher operators under resetting; their two variants are distinguished by spatial operators rather than the temporal kernels \(1+x^\mu\) versus \(1+x\) compared here. Their general renewal stationary conditions do not state the two-window optimized order theorem.

## Limitations

The results concern the homogeneous two-model mean-first-passage formulas, not the full first-passage distributions or a direct coupling of sample paths. Neither the cost crossover nor the optimizer-rate crossover is shown unique inside its corresponding strict interval; a claim of one crossing would require further analysis. The numerical example and asymptotic checks are not proofs of global uniqueness. Other possible equivalent results outside the examined literature and searchable research records remain a publication-priority risk. The original FTE-II printed equation (40) has an ambiguous parenthesis; the renewal-consistent interpretation used here follows its stated first-order equation (41) and the equal-model limit at \(\mu=1\).

## References

[1] K. Górska, F. J. Sevilla, G. Chacón-Acosta, and T. Sandev, *Fractional Telegrapher's Equation under Resetting: Non-Equilibrium Stationary States and First-Passage Times*, Entropy 26 (2024), 665, DOI: 10.3390/e26080665. First publicly released 2024-08-05. https://www.mdpi.com/1099-4300/26/8/665

[2] T. Sandev, R. K. Singh, V. Méndez, and L. Kocarev, *First-passage times for generalized heterogeneous telegrapher's processes*, Physical Review E 111 (2025), 044105, DOI: 10.1103/PhysRevE.111.044105. https://journals.aps.org/pre/pdf/10.1103/PhysRevE.111.044105
