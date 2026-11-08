# A one-peak law and late-time reversal for infectivity in a two-strain mutation–SIR epidemic

## Finding

In a closed, well-mixed susceptible–infected–recovered (SIR) epidemic with two transmissibility types and symmetric interconversion of the infected types, the infected-population mean transmissibility has **at most one stationary turning point on positive times**. If one exists it is a strict maximum: the mean first increases, then strictly decreases. It cannot have a local minimum or multiple maxima. The conclusion holds for all strictly positive epidemiological parameters and all interior initial states, not merely near a disease-free equilibrium. The mean converges to an explicit mutation–selection balance at the residual susceptible fraction. An exact rational parameter/initial-state choice forces a genuine interior maximum.

## Assumptions and scope

Let \(0\le\lambda_L<\lambda_H\le1\), \(k>0\), \(\mu>0\), and \(\nu>0\). Let \(s(0)>0\), \(I_L(0)>0\), \(I_H(0)>0\), \(r(0)\ge0\), with their sum equal to one. The deterministic, mass-action, closed SIR equations are

\[
\begin{aligned}
\dot s&=-ks(\lambda_LI_L+\lambda_HI_H),\\
\dot I_L&=(k\lambda_Ls-\mu)I_L+\nu(I_H-I_L),\\
\dot I_H&=(k\lambda_Hs-\mu)I_H+\nu(I_L-I_H),\\
\dot r&=\mu(I_L+I_H).
\end{aligned}
\]

The two infected types interconvert at rate \(\nu\) in each direction; new infections inherit the transmitting type. This is a finite two-type, *reflecting* mutation model, not an assertion about an unbounded continuous trait-diffusion PDE. Define \(i=I_L+I_H\), \(x=I_H/i\), and \(\bar\lambda=\lambda_L+(\lambda_H-\lambda_L)x\). All are well-defined at every finite time since both infected classes remain strictly positive.

Define \(a(t)=k(\lambda_H-\lambda_L)s(t)\), and for \(a>0\) define
\[
y(a)=\frac{a-2\nu+\sqrt{a^2+4\nu^2}}{2a}\in(1/2,1).
\]
The theorem says \(x\) either strictly decreases for every positive time, strictly increases for every positive time, or strictly increases up to one finite time and then strictly decreases. At a possible stationary initial instant the subsequent motion is strictly decreasing. In all cases \(x(t)\to y(a_\infty)\), with \(a_\infty=k(\lambda_H-\lambda_L)s_\infty>0\) and \(s_\infty=\lim_{t\to\infty}s(t)\).

## Proof

**Invariance and an exact scalar equation.** The nonnegative unit simplex is invariant; mutation makes both initially positive infected classes remain positive, while \(s(t)=s(0)\exp(-k\int_0^t(\lambda_LI_L+\lambda_HI_H)\,du)>0\) for finite \(t\). Summing the infected equations gives \(\dot i=(ks\bar\lambda-\mu)i\). Hence exact differentiation of \(x=I_H/i\) yields
\[
\dot x=F_{a(t)}(x),\qquad F_a(x)=ax(1-x)+\nu(1-2x).
\tag{1}
\]
The polynomial \(F_a\) is strictly decreasing on \([1/2,1]\), is positive at \(1/2\), and negative at \(1\). Its other real root is negative, so its unique zero inside \((0,1)\) is \(y(a)\), with \(F_a(x)>0\) below the root and \(F_a(x)<0\) above it. Implicit differentiation at the positive root gives
\[
y'(a)=\frac{y(a)(1-y(a))}{2\nu+a(2y(a)-1)}>0.
\]
Since \(I_H(t)>0\), \(\lambda_H>0\), and \(s(t)>0\), we have \(\dot a(t)<0\) at every finite time and consequently \(d[y(a(t))]/dt<0\).

**At most one change of direction.** Set \(z(t)=x(t)-y(a(t))\). Whenever \(z(t)=0\), equation (1) gives \(\dot x(t)=0\), while \(\dot z(t)=-\frac{d}{dt}y(a(t))>0\). Therefore every zero of \(z\) crosses strictly from negative to positive. There can be at most one such zero: after any crossing a second positive-to-negative crossing would be necessary to return to the negative side, contradicting the strictly positive derivative at every zero. Equation (1) gives strictly positive \(\dot x\) when \(z<0\) and strictly negative \(\dot x\) when \(z>0\). This proves the asserted full direction classification and strict maximality of any positive-time turning point. In particular \(\dot{\bar\lambda}=(\lambda_H-\lambda_L)\dot x\) has the same sign.

**Residual-susceptibility limit.** Since \(r'=\mu i\ge0\) and \(r\le1\), \(\int_0^\infty i(t)\,dt\le1/\mu\). Therefore
\[
s(t)\ge s(0)\exp(-k\lambda_H/\mu)>0,
\]
so \(s(t)\downarrow s_\infty>0\) and \(a(t)\downarrow a_\infty>0\). The infected prevalence has a bounded derivative, so the integrable function \(i(t)\) tends to zero (or alternatively apply uniform continuity). The scalar inequalities \(F_{a_\infty}(x)\le \dot x\le F_{a_\infty+\varepsilon}(x)\) for sufficiently large time, followed by scalar comparison with autonomous equations, force
\[
\liminf_{t\to\infty}x(t)\ge y(a_\infty),\qquad
\limsup_{t\to\infty}x(t)\le y(a_\infty+\varepsilon).
\]
Letting \(\varepsilon\downarrow0\) proves \(x(t)\to y(a_\infty)\).

**A provably reversed trajectory.** Take
\[
(\lambda_L,\lambda_H,k,\mu,\nu)=(0,1,10,1,1/10),\quad
(s(0),I_L(0),I_H(0),r(0))=(9/10,3/100,7/100,0).
\]
Then \(x(0)=7/10\) and equation (1) gives \(\dot x(0)=37/20>0\). At \(x=1/2\), equation (1) gives \(\dot x=a/4>0\); hence \(x(t)>1/2\) always. Divide the identity \(d(\log s)/dt=-10ix\) by \(\dot r=i\) to obtain \(d(\log s)/dr=-10x\le-5\), so
\[
s(t)\le(9/10)e^{-5r(t)}.
\]
At infinity, \(i_\infty=0\) implies \(r_\infty+s_\infty=1\). The strictly concave function \(f(u)=1-u-(9/10)e^{-5u}\) is positive at \(u=0\), and also at \(u=99/100\), because \(e^{99/20}>90\). By concavity it is positive throughout \([0,99/100]\). But the preceding upper bound on \(s_\infty\) yields \(f(r_\infty)\le0\). Thus \(r_\infty>99/100\) and \(s_\infty<1/100\), so \(a_\infty=10s_\infty<1/10\). Finally,
\[
F_{a_\infty}(7/10)=\frac{21}{100}a_\infty-\frac1{25}<\frac{21}{1000}-\frac1{25}<0.
\]
Consequently \(y(a_\infty)<7/10=x(0)\). The trajectory initially rises but its limit lies below its initial value. Thus by the one-crossing theorem, it has exactly one strict positive-time maximum. This is a proof of existence rather than inference from numerical integration.

## Verification

The standalone `check.py` verifies the quotient identity and mass balance symbolically, exact-rational inequalities for the constructive example, and numerically integrates the example at tight tolerances. On execution, it found one sampled derivative-sign change near \(t\approx0.456\), with \(x_{\mathrm{peak}}\approx0.95145\) and \(x_\infty\approx0.50151\). The at-most-one statement, strictness, and existence are analytically proved above; the numerical trajectory is illustrative, not an exhaustive proof.

## Relationship to prior work

Lamata-Otín, Arenas, Gómez-Gardeñes and Soriano-Paños (first posted 19 March 2026, arXiv:2603.18801) study a more general evolving-infectivity SIR model, give a replicator–mutator reduction and a first-moment balance, and analyze epidemic peaks and control effects. Their continuum and discrete approximations emphasize early-time growth of mean infectivity under negligible trait-boundary flux; they do not establish this two-type, bounded-mutation, full-time at-most-one-extremum classification or a forced late-time reversal. The related Lamata-Otín et al. arXiv:2506.03279 studies susceptible–infectious–mutation–susceptible dynamics with immune memory and genotype networks, not this closed two-trait SIR theorem. The scalar moving-nullcline argument is elementary; we do not claim its general comparison principle is new. The contribution is the resulting sharp ecological-epidemiological structure and reversal example under explicitly defined mutation boundaries.

## Limitations

The theorem requires two types, symmetric strictly positive mutation, shared removal rate, closed SIR demography and strictly positive initial infected populations. Additional types or nonsymmetric time-varying mutation may admit more extrema. The limit of type frequencies is a deterministic mathematical statement even though total prevalence vanishes; an epidemic in a finite stochastic population would reach extinction and could not meaningfully identify an infinitesimal terminal frequency. The finding does not establish global laws for the epidemic prevalence peak, optimal interventions or continuous-trait diffusion.

## References

1. S. Lamata-Otín, A. Arenas, J. Gómez-Gardeñes and D. Soriano-Paños, *Interplay between evolutionary and epidemic time scales challenges the outcome of control policies*, arXiv:2603.18801v1 (19 March 2026), https://arxiv.org/abs/2603.18801 ; *Physical Review Letters* 137, 137401 (22 September 2026), https://doi.org/10.1103/56yd-sfks .
2. S. Lamata-Otín, O. C. Rotita-Ion, A. Arenas, D. Soriano-Paños and J. Gómez-Gardeñes, *Genotype networks drive oscillating endemicity and epidemic trajectories in viral evolution*, arXiv:2506.03279v1 (3 June 2025), https://arxiv.org/abs/2506.03279 .
