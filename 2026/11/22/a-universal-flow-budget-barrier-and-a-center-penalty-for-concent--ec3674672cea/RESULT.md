# A universal flow-budget barrier and a center penalty for concentrated reproduction

## Finding

Let \(D,v,L>0\). A nonnegative spatial growth measure \(\mu\) on \((0,L)\) models the local linear reproductive potential under diffusion \(D\) and constant downstream drift \(v\). Let \(B=\mu((0,L))\). For the backward operator and boundary conditions specified below, its principal eigenvalue \(\lambda(\mu)\) satisfies:

1. If \(0\le B<v\), then \(\lambda(\mu)\le -(v-B)/L<0\), for **every** spatial arrangement of the growth budget.
2. If \(B=v\), then \(\lambda(\mu)\le0\), and equality is possible **only** for a single point mass \(\mu=v\delta_a\), with \(0<a<L\). Every distributed positive growth measure of that same total budget has strictly negative principal eigenvalue.
3. For a single hotspot \(\mu=\beta\delta_a\), the sign of the principal eigenvalue is exactly the sign of \(\beta-v\). Thus the critical total growth budget is \(\beta_c=v\), independent of diffusivity, interval length and hotspot position. For \(\beta>v\), the eigenvalue is symmetric about \(a=L/2\) and decreases strictly from either end toward the center. The center is the unique least favorable *interior* hotspot location above threshold.
4. A fixed budget above threshold need not guarantee growth for an arbitrary distribution. For \(D=1/100\), \(v=L=1\), the distributed growth \(\mu=2\,dx\) has \(\lambda\le-23\), whereas \(\mu=2\delta_{1/2}\) has \(\lambda>0\).

The conjunction is a sharp, shape-uniform barrier to the spectral establishment of rare lineages, with strict equality and an exact location-dependent supercritical complement.

## Assumptions and scope

All parameters \(D,v,L\) are strictly positive. A growth measure is a finite nonnegative Borel measure on the open interval \((0,L)\); this includes continuous nonnegative profiles \(b(x)\,dx\) and interior point masses. A point mass is an idealized narrow growth patch, not a conventional smooth reaction coefficient. The original biological growth profile is not assumed to equal such a measure.

Define the backward spectral equation formally as

\[
D\phi''+v\phi'+\mu\phi=\lambda\phi,\qquad
\phi'(0)=0,\quad D\phi'(L)+v\phi(L)=0.
\]

For atomic \(\mu=\beta\delta_a\), interpret this distributionally: \(\phi\) is continuous at \(a\), and \(D(\phi'(a+)-\phi'(a-))=-\beta\phi(a)\). For general measures the rigorous meaning is the self-adjoint closed form below. The eigenvalue \(\lambda\) is its largest (algebraically simple, positive-eigenfunction) eigenvalue, which determines the linear spectral growth sign. No nonlinear population dynamics, spatially varying diffusion, density feedback, or stochastic branching construction for atomic growth is asserted.

## Proof

**Gauge and spectral form.** Set \(h=v/(2D)>0\) and \(\phi(x)=e^{-hx}u(x)\). The differential expression becomes \(D u''-D h^2u+\mu u\), with equal positive Robin coefficients

\[
u'(0)=hu(0),\qquad u'(L)=-hu(L).
\]

On \(H^1(0,L)\), define

\[
E[u]=D\int_0^L|u'|^2dx+Dh\bigl(|u(0)|^2+|u(L)|^2\bigr)+Dh^2\int_0^L|u|^2dx.
\]

Because point evaluation is bounded on \(H^1(0,L)\), the finite-measure form is well defined, bounded above and has compact resolvent. Its top eigenvalue is

\[
\lambda(\mu)=\sup_{u\ne0}\frac{\int_{(0,L)}|u|^2d\mu-E[u]}{\int_0^L|u|^2dx}.
\]

**Exact trace identity and universal budget.** For every \(a\in[0,L]\) and every complex \(u\in H^1(0,L)\), integrating cross terms gives

\[
E[u]-v|u(a)|^2=
D\int_0^a|u'-hu|^2dx+D\int_a^L|u'+hu|^2dx\ge0.
\]

As \(a\) may be chosen at a maximizer of \(|u|\), this proves \(E[u]\ge v\|u\|_\infty^2\). For \(\mu\ge0\) with total mass \(B\), \(\int|u|^2d\mu\le B\|u\|_\infty^2\). If \(B<v\), then

\[
\frac{\int|u|^2d\mu-E[u]}{\int|u|^2dx}
\le-(v-B)\frac{\|u\|_\infty^2}{\|u\|_2^2}
\le-\frac{v-B}{L}.
\]

For \(B=v\), the quotient is nonpositive. If its largest eigenvalue is zero, its positive top eigenfunction realizes equality in both inequalities. Equality in the trace identity implies \(u'=hu\) to the left of a maximizing point \(a\), and \(u'=-hu\) to the right. Hence \(|u|\) has a *unique* maximizer \(a\), and equality in the measure bound forces \(\mu\) to be supported at that one point. The mass requirement then gives \(\mu=v\delta_a\). This uses the attained principal eigenvalue, not just pointwise inequalities on arbitrary tests.

**Sharpness at one growth hotspot.** For any \(a\in(0,L)\), the function

\[
\phi_a(x)=\begin{cases}1,&0\le x\le a,\\
\exp[-v(x-a)/D],&a\le x\le L
\end{cases}
\]

satisfies both endpoint conditions and the derivative jump with \(\beta=v\). It is strictly positive, hence has principal eigenvalue zero. If \(\beta>v\), evaluating the variational quotient at its corresponding transformed \(u_a=e^{hx}\phi_a\) gives a strictly positive value. If \(0\le\beta<v\), the already proved uniform negative bound applies. Thus the point-source threshold is exactly \(v\), independently of \(a,D,L\).

**Strict supercritical center penalty.** Fix \(\beta>v\), so the principal eigenvalue \(\lambda>0\), and put \(q=\sqrt{h^2+\lambda/D}>h\). On a source-free left or right subinterval, normalized positive solutions of \(u''=q^2u\) are respectively \(w_q(x)\) and \(w_q(L-x)\), with

\[
w_q(t)=\cosh(qt)+\frac hq\sinh(qt),\qquad
g_q(t)=\frac{w_q'(t)}{w_q(t)}=\frac{q\tanh(qt)+h}{1+(h/q)\tanh(qt)}.
\]

The point-source jump is equivalent to the single scalar equation

\[
\frac{\beta}{D}=g_q(a)+g_q(L-a).
\]

For \(q>h>0\), \(g_q(0)=h\), \(0<g_q(t)<q\), and

\[
g_q'(t)=q^2-g_q(t)^2>0,\qquad g_q''(t)=-2g_q(t)g_q'(t)<0.
\]

For every \(t>0\), \(g_q(t)\) is strictly increasing in \(q\): differentiating the Riccati equation gives \((\partial_qg)'=2q-2g\partial_qg\) with zero initial value, and a positive forcing integral. Hence for each \(a\in(0,L)\) the right-hand side of the jump equation increases strictly with \(q\), starting at \(v/D\) when \(q=h\) and diverging as \(q\to\infty\). When \(0<a<L/2\), strict concavity gives \(g_q'(a)>g_q'(L-a)\), so the right-hand side increases strictly with \(a\) for fixed \(q\). Its unique root \(q\), and therefore \(\lambda=D(q^2-h^2)\), must decrease strictly as \(a\) moves toward \(L/2\). Reflection symmetry gives the unique center minimum.

**Same-budget counterexample.** For \(D=1/100\), \(v=L=1\) and constant density \(b(x)=2\), the form satisfies \(E[u]\ge Dh^2\|u\|_2^2=25\|u\|_2^2\), giving \(\lambda(2\,dx)\le2-25=-23\). With the same budget at one interior point, \(\lambda(2\delta_{1/2})>0\) by the point-source result. Thus an above-barrier budget alone is not sufficient for every spatial arrangement.

## Verification

The standalone `check.py` uses exact rational arithmetic to verify the completion-of-squares identity on piecewise-linear tests. It also checks the critical atom eigenfunction and interface jump, solves the positive-eigenvalue jump equation by bisection for illustrative parameter sets, confirms strict center ordering and reflection symmetry, and verifies the distributed-versus-concentrated sign witness. Execute `python3 check.py` using only the Python standard library.

The inequalities for *every* nonnegative measure and the strict continuum of hotspot positions follow from the analytic proof, not from numerical enumeration. Neither computational experiments nor the checker substitute for the compact-operator and Riccati arguments.

## Relationship to prior work

Alexandre, Loverdo and Bitbol (2026) derive the same transport boundary pair and a self-adjoint gauge for a nonlinear fixation model. Their supplement examines the spectral threshold for a self-consistent resident profile and gives exact washout conditions for a step-function division profile. The present statement instead treats all *independently prescribed finite nonnegative growth measures*, including Dirac resources, under a fixed integrated budget. It does not assert their resident profiles can realize arbitrary measures.

Caubet, Deheuvels and Privat (2017) study optimal resource location for a different population operator: drift follows the **gradient of the resource field**, the admissible growth weight is bounded and sign-indefinite, and the design variable is a region of finite width. Their bang-bang rearrangement and Robin optimization results do not imply the present shape-independent \(B=v\) threshold, its atomic equality case, or supercritical center penalty for the constant-advection boundary pair. General advection-persistence research by Ryabov and Blasius (2008) supplies background but not the same statement. Standard one-dimensional point interactions and Robin eigenvalue theory underlie the method and are not claimed as new in general.

## Limitations

The claim is a linear spectral theorem for the stated constant-coefficient one-dimensional operator. An idealized point growth measure is a singular limit; a physical nutrient distribution is bounded, may alter advection or diffusion, and may be constrained by the resident bacteria and nutrient balances. The statement does not give a stochastic branching-process construction for atomic growth, actual mutant fixation probabilities, nonlinear persistence, or finite-width patch-error estimates. The exact trace identity may be recognizable in older Sturm–Liouville, sharp Sobolev or point-potential literature not found in the literature comparison; originality therefore remains literature-bounded, with independent audit outstanding.

## References

- A. Alexandre, C. Loverdo, A.-F. Bitbol, *Hydrodynamic flow in the gut hinders the fixation of beneficial mutants but accelerates their invasion*, arXiv:2611.00134v1 (first public 2026-10-29), https://arxiv.org/abs/2611.00134; especially supplement equations S33–S39 and S160–S169.
- F. Caubet, T. Deheuvels, Y. Privat, *Optimal location of resources for biased movement of species: the 1D case*, SIAM Journal on Applied Mathematics **77** (2017), 1876–1903; arXiv:1704.08016, https://arxiv.org/abs/1704.08016, Theorems 1.8–1.12.
- A. B. Ryabov, B. Blasius, *Population Growth and Persistence in a Heterogeneous Environment: the Role of Diffusion and Advection*, Mathematical Modelling of Natural Phenomena **3** (2008), https://doi.org/10.1051/mmnp:2008064.
