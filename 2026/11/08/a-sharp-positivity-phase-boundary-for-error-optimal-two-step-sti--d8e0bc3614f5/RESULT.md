# A sharp positivity phase boundary for error-optimal two-step stiff multistep methods

## Finding
For the unique error-constant-optimal A-stable, second-order, two-step \(L(\kappa)\)-stable family in Jensen, Ketcheson and Lóczi [1], the entire backward-Euler-started numerical solution of the scalar decay equation \(y'=-\lambda y\) is nonnegative **if and only if** the nondimensional step \(r=h\lambda\) satisfies
\[
0\le r\le R(\kappa),\qquad
R(\kappa)=\begin{cases}
\dfrac{1+\kappa}{2(1-\kappa)},&0\le\kappa\le\tfrac12,\\
\dfrac1\kappa-\kappa,&\tfrac12\le\kappa<1.
\end{cases}
\]
Consequently the largest safe scalar step among the entire optimal family is \(R(1/2)=3/2\), uniquely attained at damping \(\kappa=1/2\), three times the BDF2 threshold \(R(0)=1/2\). The error-constant modulus of this member is \(1/9\) rather than BDF2's \(1/3\), using the formula proved in [1]. At \(\kappa=1/2\), \(r=3/2\), a special nilpotent recurrence has \(y_0=1\), \(y_1=2/5\), and \(y_n=0\) for every \(n\ge2\).

## Assumptions and scope
Fix \(0\le\kappa<1\), \(\lambda>0\) and \(h\ge0\), and define \(r=h\lambda\). Analyze the scalar initial-value problem \(y'=-\lambda y\), \(y(0)=1\). The numerical history is initialized by one backward-Euler step \(y_0=1\), \(y_1=(1+r)^{-1}\). For \(d=3+2\kappa-\kappa^2>0\), use the two-step method [1, Corollary 4.2] with
\[
(\beta_0,\beta_1,\beta_2)=\frac{1}{d}(2\kappa^2,4\kappa,2),\quad
(\alpha_0,\alpha_1,\alpha_2)=\frac{1}{d}((1+\kappa)(1-3\kappa),-4(1-\kappa^2),d).
\]
Its defining recurrence is \(\sum_{j=0}^2\alpha_jy_{n+j}=h\sum_{j=0}^2\beta_j f(y_{n+j})\) for \(f(y)=-\lambda y\). Positivity means \(y_n\ge0\) for *every* integer \(n\ge0\); transient or finitely tested positivity is insufficient. The classification includes both endpoints and permits zero numerical values.

## Proof
**1. Exact recurrence and two root certificates.** Direct substitution gives, for every \(n\ge0\),
\[
(d+2r)y_{n+2}=4(1-\kappa^2-\kappa r)y_{n+1}+((1+\kappa)(3\kappa-1)-2\kappa^2r)y_n.
\]
Write \(y_{n+2}=a y_{n+1}+b y_n\), with \(a,b\) equal to the two displayed numerator coefficients divided by \(d+2r\). Put \(z=(1+r)^{-1}\). The roots \(u_+\ge u_-\) of \(P(u)=u^2-au-b\), when real, have discriminant
\[
\Delta=a^2+4b=\frac{4(1+\kappa)^3(1+\kappa-2(1-\kappa)r)}{(d+2r)^2}.
\]
Two further exact identities are
\[
P(z)=\frac{r^2((1+\kappa)^2+2\kappa^2r)}{(1+r)^2(d+2r)}>0\quad(r>0),
\]
\[
z-\frac a2=\frac{(1+\kappa)^2+2\kappa^2r+2\kappa r(r+1)}{(1+r)(d+2r)}>0.
\]
Hence, whenever \(r>0\) and the roots are real, \(z>u_+\). Define the repeated-root threshold \(r_c=(1+\kappa)/(2(1-\kappa))\), and for \(\kappa>0\) the zero-sum threshold \(r_a=(1-\kappa^2)/\kappa\). The exact identity \(r_c-r_a=\frac{(2-\kappa)(1+\kappa)(2\kappa-1)}{2\kappa(1-\kappa)}\) shows \(r_c\le r_a\) when \(\kappa\le1/2\) and \(r_a\le r_c\) when \(\kappa\ge1/2\).

**2. Sufficiency below both thresholds.** If \(0<r\le\min(r_c,r_a)\), the discriminant is nonnegative and \(a\ge0\). Thus \(u_+\ge |u_-|\). At distinct roots the coefficients in \(y_n=C_+u_+^n+C_-u_-^n\) satisfy \(C_-=(u_+-z)/(u_+-u_-)<0\), \(C_+=1-C_->1\). If \(u_-\ge0\) or \(n\) is even, then \(y_n\ge(C_++C_-)u_+^n=u_+^n\ge0\); if \(u_-<0\) and \(n\) is odd, both terms are positive. At a positive repeated root \(u_+=u_-=q\), the limit formula \(y_n=q^n[1+n(z/q-1)]\) is nonnegative because \(z>q\). At the single double-zero case \((\kappa,r)=(1/2,3/2)\), \(a=b=0\) and \(y_{n\ge2}=0\). When \(r=0\), consistency gives \(y_n=1\) for all \(n\). Therefore every step in the stated interval is nonnegative.

**3. Necessity for \(0\le\kappa<1/2\).** If \(r_c<r<r_a\) (with \(r_a=+\infty\) for \(\kappa=0\)), then \(\Delta<0\). In that case every nonzero real solution of the recurrence has the form \(y_n=\rho^n\operatorname{Re}(C e^{in\theta})\), where \(\rho>0\), \(0<\theta<\pi\), and \(C\ne0\). The normalized terms have bounded partial sums because \(e^{i\theta}\ne1\). Were they all nonnegative, their bounded, increasing partial sums would imply the normalized terms converge to zero. But two consecutive normalized terms tending to zero would force the fixed nonzero cosine/sine coefficients to vanish, a contradiction. Thus some iterate is negative. For \(r\ge r_a\) with \(0<\kappa<1/2\), one has \(a\le0\) and \(b<0\), forcing \(y_2=az+b<0\). This proves necessity for the lower half of the damping range.

**4. Necessity for \(1/2\le\kappa<1\).** At \(\kappa=1/2\) and \(r>r_a=r_c=3/2\), both \(a,b<0\), so \(y_2<0\). For \(\kappa>1/2\), define \(r_b=(1+\kappa)(3\kappa-1)/(2\kappa^2)\). Direct subtraction yields \(r_b-r_a=(1+\kappa)^2(2\kappa-1)/(2\kappa^2)>0\). If \(r_a<r<r_b\), then \(a<0\) and \(b>0\), so the roots \(p>0\) and \(-q<0\) satisfy \(q>p\). Since \(z>p\), the coefficient of \((-q)^n\) is \((p-z)/(p+q)<0\). Therefore all sufficiently large even-index iterates are negative. At \(r\ge r_b\), \(a<0\) and \(b\le0\), whence \(y_2<0\). All forbidden steps therefore lose positivity.

**5. Unique optimization.** On \([0,1/2]\), \(r_c=(1+\kappa)/(2(1-\kappa))\) is strictly increasing; on \([1/2,1)\), \(r_a=1/\kappa-\kappa\) is strictly decreasing. They agree at \(\kappa=1/2\), yielding the unique global maximum \(3/2\). At that point \(a=b=0\) gives the claimed exact finite termination for this scalar mode.

## Verification
The standalone `bdfl2_phase_verifier.py` uses exact `fractions.Fraction` arithmetic. Its 11,548 rational checks include: characteristic discriminant and starter identities on a parameter grid, nonnegative iterates up to degree 74 within the asserted region, explicit negative iterates for sampled steps beyond the frontier, and the exact nilpotent endpoint. Run `python3 bdfl2_phase_verifier.py` from this package. The finite checks are corroboration; the case-split proof establishes the universal quantifiers. Rounding and finite precision are not addressed.

## Relationship to prior work
Jensen, Ketcheson and Lóczi [1, Section 4.1, Corollary 4.2] construct and optimize the A-stable, \(L(\kappa)\)-stable two-step family, including its error constant and damping; those optimization claims are **prior work**, not claimed here. Their inspected Section 4.1 does not provide the complete backward-Euler-started positivity region in the \((\kappa,r)\) plane. Classical BDF2 [2] and the published analysis [3] already contain the \(\kappa=0\) positivity cutoff \(r=1/2\); the new point is the complete positive-damping phase and its nonmonotone optimizer at \(\kappa=1/2\). Source [3] concerns BDF2's delayed sign reversal, not the whole error-optimal family. The root analysis here specifically incorporates the start value and all iterates, so an A-stability assertion alone does not imply it.

## Limitations
This is a scalar decay and backward-Euler-start theorem. It does **not** establish order-preserving matrix propagators, positivity on coupled ODE systems, strong stability preservation for arbitrary positive histories, positivity under variable timesteps, or robust finite-precision behavior. No independent audit has been performed. Related positive-recursion criteria may exist in older literature; equivalence to all such criteria has not been ruled out.

## References
[1] T. Jensen, D. I. Ketcheson and L. Lóczi, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1, first public 2026-10-15, Section 4.1 and Corollary 4.2, https://arxiv.org/abs/2610.22685.

[2] E. Hairer and G. Wanner, *Solving Ordinary Differential Equations II*, 1996, standard BDF/A-stability background (as cited in [1]).

[3] *Exact delayed sign loss just beyond BDF2's positivity boundary*, published published-finding corpus record `2026/10/4/SCOPE-exact-delayed-sign-loss-just-beyond-bdf2-s-positivity-boundary--cf66315c5a14`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-delayed-sign-loss-just-beyond-bdf2-s-positivity-boundary--cf66315c5a14 (record summary consulted for its BDF2-only statement).
