# A sharp constant-dose trichotomy and a finite eradication window under drug-induced cell plasticity

## Finding

A two-phenotype model of drug-sensitive and reversibly drug-tolerant tumor cells has a complete, sharp phase diagram for the constant concentration minimizing its long-run net growth rate. Depending only on explicit inequalities between intrinsic growth, maximal drug killing, and switching parameters, the growth rate is strictly decreasing at every finite concentration, strictly increasing at every concentration, or decreases and then increases with **exactly one** interior optimum. At the transition from finite to unbounded optimal concentration, the optimizer diverges as the reciprocal of a model-parameter gap while the achievable improvement below tolerant-cell growth vanishes quadratically. An exact rational parameter set has a bounded interval of drug concentrations producing net decay, despite net growth at zero concentration and at arbitrarily large concentration.

In particular, write \(d=r-t\) and \(L=\nu k/(m+k)+\mu_0k/m\), under the assumptions below. The exhaustive alternatives are:

1. If \(d\ge k\), then \(\sigma\) is strictly decreasing on \([0,\infty)\), \(\sigma(c)>t\) for all finite \(c\), and \(\sigma(c)\to t\) as \(c\to\infty\). The infimum is not attained at a finite concentration.
2. If \(0\le d<k\), there is one \(c_*>0\) at which \(\sigma\) attains its unique strict global minimum; \(\sigma\) strictly decreases before and strictly increases afterward, and \(\sigma(c_*)<t\).
3. If \(d<0\), let \(g=t-r=-d\). If \(g\ge L\), the unique minimizer is \(c=0\), and \(\sigma\) is strictly increasing on \((0,\infty)\). If \(g<L\), there is exactly one \(c_*>0\) with the same decrease–increase behavior as in case 2.

When the interior optimum exists, it is determined by the **unique admissible** root \(y=1+c_*>1\) of
\[
 k+t-r=\frac{2k}{y}+\frac{k(\mu_0-m)}{m y^2}+\frac{\nu k}{m y^2+k},
\qquad
 \sigma(c_*)=t-\frac{\nu k}{m y^2+k}.
\]
For any imposed finite dose cap \(C>0\), the constant-dose optimum is \(C\) in case 1, zero in the increasing case 3, and \(\min\{C,c_*\}\) otherwise.

Let \(k,m,\mu_0,\nu,t\) remain fixed and let \(r=t+k-\delta\) for \(\delta\downarrow0\). Then
\[
 c_*(\delta)=\frac{2k}{\delta}+\frac{\mu_0-m+\nu}{2m}-1+O(\delta),
 \qquad
 t-\sigma(c_*(\delta))=\frac{\nu\delta^2}{4mk}+O(\delta^3).
\]
This is a singular transition: the optimal concentration becomes arbitrarily large while the growth benefit below \(t\) becomes quadratically small.

An exact extinction-window example is \(r=19/33\), \(t=1/11\), \(k=2\), \(m=\mu_0=\nu=1\). Its unique global minimum is at \(c_*=2\), with \(\sigma(c_*)=-1/11\), whereas \(\sigma(0)>0\) and \(\lim_{c\to\infty}\sigma(c)=1/11>0\). In fact, \(\sigma(c)<0\) **exactly when**
\[
\frac{202-\sqrt{33445}}{33}<c<\frac{202+\sqrt{33445}}{33}.
\]

## Assumptions and scope

Let \(r,t\in\mathbb R\), and \(k,m,\mu_0,\nu>0\). Dose \(c\) ranges over all \(c\ge0\), unless an explicit cap is imposed. Drug-sensitive cells have net birth-minus-death rate \(s(c)=r-kc/(1+c)\) and transition to tolerance at rate \(\mu(c)=\mu_0+mc\); tolerant cells have drug-independent net birth rate \(t\) and revert to sensitivity at rate \(\nu\). The linear population vector \(z=(z_S,z_T)^\top\) satisfies
\[
\dot z=M(c)z,\qquad
M(c)=\begin{pmatrix}s(c)-\mu(c)&\nu\\\mu(c)&t-\nu\end{pmatrix}.
\]
\(\sigma(c)\) is the eigenvalue of \(M(c)\) with maximal real part; irreducibility implies that it is real and simple. It is the asymptotic logarithmic growth rate for each strictly positive initial population under a **constant** dose. Comparisons do not assert optimality among arbitrary time-dependent doses beyond the previously established bounded-dose treatment theorem in the initiating source.

## Proof

**1. Perron geometry and direct derivative.** The characteristic equation, derived by expanding the determinant, is
\[
 (\sigma-s+\mu)(\sigma-t+\nu)-\mu\nu=0.
\]
The positive Perron right eigenvector gives \(\sigma\) as a strictly positive weighted average of \(s\) and \(t\); therefore \(\min\{s,t\}<\sigma<\max\{s,t\}\) whenever \(s\ne t\), and \(\sigma=t\) if \(s=t\). Implicit differentiation, with \(s'(c)=-k/(1+c)^2\) and \(\mu'=m\), gives
\[
\sigma'(c)=\frac{s'(c)(\sigma-t+\nu)-m(\sigma-t)}{2\sigma-s+\mu-t+\nu}.
\]
The denominator is the positive eigenvalue gap; \(\sigma-t+\nu>0\) follows from the positive eigenvector equation. Whenever \(s\ge t\), this is strictly negative. If \(r-t\ge k\), \(s(c)>t\) at every finite \(c\). The characteristic relation shows that \(\sigma(c)\to t\) as \(\mu(c)\to\infty\); this proves case 1.

**2. Strictly monotone crossing in the below-tolerant-rate regime.** Wherever \(s(c)<t\), set \(w=t-s>0\), \(u=t-\sigma\in(0,\nu)\), and \(q=u/(\nu-u)>0\). Expanding the characteristic equation at \(\sigma=t-u\) and substituting \(u=\nu q/(1+q)\) yields the exact identity
\[
 w(c)=\frac{\nu q(c)}{1+q(c)}+\mu(c)q(c).
\]
The right side is strictly increasing in \(q\), so \(q(c)\) is uniquely defined and differentiable. Since \(w'=k/(1+c)^2\),
\[
 q'(c)=\frac{k/(1+c)^2-mq(c)}{\nu/(1+q(c))^2+\mu(c)}.
\]
Put \(q_{\rm crit}(c)=k/[m(1+c)^2]\) and \(F=q-q_{\rm crit}\). At any zero, \(q'=0\), whence \(F'=-q_{\rm crit}'>0\). Thus every zero is a strictly negative-to-positive crossing; continuity excludes two distinct zeros (otherwise some positive-to-negative crossing would intervene). Moreover, because \(w(c)\to k+t-r>0\), the equation implies \(q(c)\sim(k+t-r)/(mc)\) while \(q_{\rm crit}(c)\sim k/(mc^2)\); hence \(F>0\) eventually. Since \(\sigma=t-\nu q/(1+q)\), the derivative signs of \(\sigma\) and \(q\) are opposite.

When \(0\le r-t<k\), \(s(c)\) crosses \(t\) at \(c_0=(r-t)/(k-r+t)\), including \(c_0=0\) when \(r=t\). Immediately after crossing, \(q=0<q_{\rm crit}\), hence \(q'>0\) and \(\sigma'<0\); the single later crossing proves case 2. When \(r<t\), the below-tolerant-rate region begins at zero. Comparing \(q(0)\) to \(q_{\rm crit}(0)=k/m\), using the strictly increasing right side of the identity, shows \(q(0)\ge k/m\) exactly when \(t-r\ge\nu k/(m+k)+\mu_0k/m=L\). This gives both alternatives in case 3. At equality, \(q'(0)=0\) but \(F>0\) immediately afterward, so the unique global minimum remains at zero.

**3. Interior optimum and singular boundary.** At the unique stationary point, \(q=k/[m(1+c)^2]\). Substitution into the exact identity above and writing \(y=1+c\) proves the two boxed stationary formulas. Their uniqueness is guaranteed by the strict crossing established above; extraneous algebraic roots outside \(y>1\) are immaterial. With \(\delta=k+t-r\), the stationary equation has expansion \(\delta=2k/y+k(\mu_0-m+\nu)/(my^2)+O(y^{-4})\) as \(y\to\infty\). Inverting it gives \(y=2k/\delta+(\mu_0-m+\nu)/(2m)+O(\delta)\). Substitution into \(t-\sigma(c_*)=\nu k/(my^2+k)\) proves the claimed quadratic benefit.

**4. Exact biological-window witness.** For the stated rational parameters, the stationary identity is solved by \(y=3\). The strict uniqueness theorem therefore yields \(c_*=2\), and the stationary value is \(-1/11\). A direct determinant computation gives
\[
\det M(c)=-\frac{33c^2-404c+223}{363(1+c)},\qquad
\operatorname{tr}M(c)=-\frac{(c+4)(3c+1)}{3(c+1)}<0.
\]
Because the trace is negative, the Perron eigenvalue is negative exactly where the determinant is positive. Solving its quadratic numerator yields the two asserted positive zeroes, and proves the bounded interval with strictly negative growth. Outside it the determinant is negative and there is a positive eigenvalue. At zero dose \(\det M(0)=-223/363<0\), and the high-dose limit is \(t=1/11\).

## Verification

The accompanying executable `verify_calculations.py` checks the exact rational witness using rational arithmetic, the high-dose asymptotic constants through direct numerical tests at decreasing positive parameter gaps, the stationary identities, and derivative-sign/trichotomy consistency over parameter grids. The proof above, not finite computation, establishes the global quantifiers and asymptotic statements. Execute `python3 verify_calculations.py` in the same directory. No external Python packages are required.

## Relationship to prior work

Gunnarsson, Magnússon and Foo (arXiv:2412.16391v1, Sections 2.1, 4 and Supplement S1.2) introduce the two-phenotype linear-plasticity framework, display its equilibrium Perron growth formula and prove that among sufficiently regular bounded-dose treatment schedules an asymptotically optimal constant dose can be chosen for linear induction. Those claims, the model equations, and the qualitative preference for intermediate constant dosing are **prior work**, not discoveries here. The narrower contribution here is an explicit **global phase diagram with strict uniqueness across all positive parameter ratios**, a singular finite-to-unbounded optimum law, and a rational full extinction-window classification. The paper's biological baseline assumes additional inequalities not required here.

Corigliano and collaborators (2025) analyze intermediate dosing and treatment holidays in a different plasticity model with saturating induction and treatment-stage transitions. Fischer and Blüthgen (2023/2024) analyze genetic and epigenetic treatment resistance at a broad optimal-control level; an accessible abstract does not resolve whether special equivalent results occur in their full work. These comparisons do not prove absolute priority. The strict trichotomy is based on the exact structural differences and is restricted to the model specified above.

## Limitations

The unbounded concentration model extrapolates linear tolerance induction far beyond realistic clinical dose limits. The findings concern deterministic linearized asymptotic tumor growth, not stochastic relapse, drug toxicity, nonlinear tumor growth, finite-horizon control, or clinical patient outcomes. The extinction-window example is a mathematical construction, not a dose recommendation. A closely related earlier optimal-control article was not fully inspectable; independent historical-priority assessment remains appropriate. No independent validation has been performed.

## References

1. E. B. Gunnarsson, B. V. Magnússon, J. Foo, *Optimal dosing of anti-cancer treatment under drug-induced plasticity*, arXiv:2412.16391v1 (public 20 December 2024), https://arxiv.org/html/2412.16391v1; npj Systems Biology and Applications 11, 98 (2025), DOI 10.1038/s41540-025-00571-5.
2. A. Corigliano et al., *Optimal Treatment for Drug-Induced Cancer Persisters Involves Release Periods and Intermediate Drug Doses*, PRX Life (2025), DOI 10.1103/mh5v-lcyw.
3. M. M. Fischer and N. Blüthgen, *On minimising tumoural growth under treatment resistance*, Journal of Theoretical Biology 579, 111716 (2024), DOI 10.1016/j.jtbi.2023.111716.
