# Global diagonal synchronization beyond coexistence-equilibrium instability in symmetric Ricker competition

## Finding
For real \(h>0\) and \(0<c<1\) satisfying
\[
(1-c)e^{h-1}<2,
\]
every strictly positive orbit of the two-species Ricker competition map
\[
(x,y)\longmapsto \big(xe^{h-x-cy},\;ye^{h-cx-y}\big)
\]
synchronizes exponentially in logarithmic abundance ratio: for each initial pair \(x_0,y_0>0\) there exist constants \(C>0\), \(0<q<1\) and \(N\in\mathbb N\) such that
\[
\left|\log\frac{x_n}{y_n}\right|\le Cq^{n-N}\qquad(n\ge N).
\]
In particular \(x_n/y_n\to1\) and \(|x_n-y_n|\to0\), regardless of whether the diagonal scalar dynamics converge to an equilibrium. The parameter region includes \(h=3\), \(c=9/10\), where the diagonal coexistence equilibrium is longitudinally unstable, with eigenvalue \(-2\). The displayed condition is sufficient, not claimed necessary or sharp.

## Assumptions and scope
Both states are strictly positive at time zero. The natural logarithm and exponentiation are real. Set \(k=1-c\in(0,1)\). The map preserves strict positivity. All bounds and quantifiers concern the entire positive quadrant and fixed permitted \(h,c\), without any small-initial-imbalance hypothesis. The asymptotic contraction factor may depend on the initial log-ratio. No assertion is made about convergence of the common synchronized population coordinate.

## Proof
**Uniform upper mass bound.** Define \(T_n=x_n+y_n\). The elementary maximum \(\max_{t\ge0}te^{-t}=e^{-1}\) and \(c>0\) give, for every \(n\ge1\),
\[
0<T_n\le L:=2e^{h-1}.
\]
Also each crowding load is at most \(T_n\), since \(c<1\), hence
\[
T_{n+1}\ge T_n e^{h-T_n}.
\]

**Eventually positive lower mass bound.** While \(T_n<h/2\), this lower inequality multiplies \(T_n\) by at least \(e^{h/2}>1\); therefore, starting at time 1, the orbit reaches \(T_n\ge h/2\) in finitely many iterates. Put
\[
m:=\min\{h/2,\;(h/2)e^{h-L}\}>0.
\]
If \(T_n\ge h/2\), the upper bound \(T_n\le L\) gives \(T_{n+1}\ge(h/2)e^{h-L}\ge m\). If \(m\le T_n<h/2\), then \(T_{n+1}\ge e^{h/2}T_n\ge m\). By induction, for some finite \(N\ge1\),
\[
m\le T_n\le L\quad(n\ge N).
\]
(The value \(m\) is positive but can be very small. This does not affect the conclusion.)

**Logarithmic-ratio contraction.** Let \(u_n=\log(x_n/y_n)\). Subtracting the logarithms of the two update equations gives the exact identity
\[
u_{n+1}=u_n-k(x_n-y_n)
=u_n-kT_n\tanh(u_n/2).
\]
Set \(p(u)=\tanh(u/2)/u\) for \(u\ne0\), with \(p(0)=1/2\). The function is continuous, even, strictly positive, bounded above by \(1/2\), and nonincreasing with \(|u|\). Consequently
\[
u_{n+1}=[1-kT_np(u_n)]u_n.
\]
For \(n\ge1\), positivity and the parameter hypothesis imply
\[
0<kT_np(u_n)\le kL/2=(1-c)e^{h-1}<2.
\]
Thus \(|u_{n+1}|<|u_n|\) unless \(u_n=0\), in which case all later log-ratios vanish. If \(u_1\ne0\), write \(U=|u_1|\); then \(|u_n|\le U\) for all \(n\ge1\), so \(p(u_n)\ge p(U)>0\). After the index \(N\) from the mass bound, the multiplier parameter belongs to the compact subinterval
\[
a:=km p(U)\le kT_np(u_n)\le b:=kL/2<2.
\]
We also have \(a>0\) and \(a\le b\). The explicit constant
\[
q=\max\{|1-a|,|1-b|\}<1
\]
bounds every subsequent multiplier, proving \(|u_n|\le |u_N|q^{n-N}\). Finally
\[
|x_n-y_n|=T_n|\tanh(u_n/2)|\le (L/2)|u_n|,
\]
and \(x_n/y_n=e^{u_n}\to1\). The conclusion also holds immediately for \(u_1=0\).

**Instability witness.** The diagonal equilibrium is \((h/(1+c),h/(1+c))\). Direct differentiation yields the longitudinal eigenvalue \(1-h\) and transverse eigenvalue \(1-h(1-c)/(1+c)\). At \((h,c)=(3,9/10)\), the sufficient condition is \(e^2/10<2\) but \(1-h=-2\), proving that global synchronization is not the same statement as fixed-point attraction.

## Verification
A standalone standard-library checker, `checks/check.py`, evaluates five positive parameter/initial-condition cases for 1000 iterates, checks the upper mass bound and strict log-ratio monotonicity after the first bounded iterate, and checks the longitudinal instability witness. The computation corroborates, but does not replace, the proof of all-parameter and all-positive-seed behavior.

## Relationship to prior work
Goldar et al. (2026) study the coupled Ricker map's boundedness, permanence, local fixed-point stability, flip and Neimark–Sacker bifurcations, and numerical complex dynamics. Kulakov, Neverova and Frisman (2022) numerically and analytically investigate phase multistability and synchronization indices of two-species Ricker competition, emphasizing coexistence of in-phase and out-of-phase modes in other regimes. Wu and Wong (2015) study global attraction to a fixed point, which cannot imply the current global synchronization result where that fixed point is longitudinally unstable. The theorem here provides an all-positive-seed, explicit sufficient condition for attraction toward the *diagonal set*, without assuming fixed-point attraction. Published results about local Floquet spectra and individual periodic orbits do not themselves supply an all-positive-seed basin theorem.

## Limitations
The sufficient inequality may be conservative. Neither optimality of the parameter region nor the existence of chaos on the diagonal is established. The theorem does not imply convergence to a particular orbit or a uniform rate valid independently of the positive initial condition. Historical priority outside the inspected articles, especially older work on coupled Ricker synchronization, merits independent scrutiny.

## References
1. S. Goldar, S. S. Hassan, R. Pati, A. A. Mohsen and M. Izadi, *Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth*, Discrete Dynamics in Nature and Society (2026), doi:10.1155/ddns/7255117. First publicly available 2026-09-16.
2. M. Kulakov, G. Neverova and E. Frisman, *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, Mathematics **10** (2022), 1076, doi:10.3390/math10071076.
3. C. Wu and P. J. Y. Wong, *Global asymptotical stability of the coexistence fixed point of a Ricker-type competitive model*, DCDS-B **20** (2015), 3255–3266, doi:10.3934/dcdsb.2015.20.3255.
