# Sharp persistence transition and critical tail in a symmetric cubic neuronal Lorenz map

## Finding
For a natural symmetric full-branch parameter curve in the cubic voltage map of Bartłomiejczyk, Llovera Trujillo and Signerska-Rynkowska, consecutive same-side visits change from exponential persistence to a critical inverse-time tail, then to positive-probability permanent trapping. The critical tail has a sharp leading coefficient and logarithmic second term.

Let \(4<\mu<8\), \(c=\sqrt{1/4-1/\mu}\), \(\beta=2c\), \(\alpha=-c\), and set \(a=d=1/2\). The interval \(I=[1/2-c,1/2+c]\) is invariant under
\[
G(x)=x+\mu x(x-1/2)(1-x)-\alpha-\beta\mathbf1_{\{x\ge1/2\}}.
\]
Choose the initial point uniformly on \(I\). Let \(\tau=\inf\{n\ge1:(x_n-1/2)(x_0-1/2)\le0\}\), with \(\tau=\infty\) if the set is empty. The initial midpoint and the countable collection of points hitting it have measure zero; either threshold convention gives the same probabilities.

The following is a complete trichotomy on this curve:

1. If \(4<\mu<6\), then with \(\Lambda_\mu=4-\mu/2>1\),
\[
\Pr(\tau>n)=\Theta_\mu(\Lambda_\mu^{-n}).
\]
In particular, \(\tau\) is finite almost surely and has finite mean.
2. At \(\mu=6\),
\[
\Pr(\tau>n)=\frac{2}{3n}+\frac{22\log n}{27n^2}+O(n^{-2}).
\]
Every point other than the two endpoints and an immaterial countable preimage set eventually changes side, but \(\mathbb E\tau=\infty\).
3. If \(6<\mu<8\), let
\[
u_*=\frac{-c+\sqrt{c^2+4/\mu}}2\in(0,c).
\]
Then
\[
\Pr(\tau=\infty)=\frac{c-u_*}{c}>0.
\]
Exactly the two intervals of centered coordinates \((u_*,c]\) and \([-c,-u_*)\), up to their zero-measure boundaries, never change sign. Their points converge monotonically to the corresponding endpoint fixed points. All other points eventually change sign.

## Assumptions and scope
All statements concern the frozen, one-dimensional voltage subsystem; the recovery variable is held fixed at \(\alpha\). The original parameters have \(\mu>0\), \(a\in(0,1)\), \(\beta>0\) and \(d\) between the cubic extrema, which hold here. The full two-dimensional slow-fast neuron map is not analyzed. The probability law is **uniform Lebesgue sampling on the invariant interval**, not sampling from an invariant probability measure.

## Proof
Write \(u=x-1/2\), so the centered map is
\[
T_\mu(u)=\left(1+\frac\mu4\right)u-\mu u^3-c\operatorname{sgn}(u),\qquad -c\le u\le c,
\]
with the positive sign used at \(u=0\). Since \(\mu(1/4-c^2)=1\), the positive branch \(B(u)=(1+\mu/4)u-\mu u^3-c\) obeys \(B(0)=-c\), \(B(c)=c\). Its derivative is \(1+\mu/4-3\mu u^2\), bounded below by \(4-\mu/2>0\) for \(0\le u\le c\). Its image is \([-c,c]\), and odd symmetry gives the corresponding negative branch. The endpoints \(\pm c\) are fixed with common multiplier \(\Lambda_\mu=4-\mu/2\).

A positive fixed point of \(B\) satisfies
\[
\mu u\left(\frac14-u^2\right)=c,
\]
which factors as \((u-c)(u^2+cu-1/\mu)=0\). The only other positive root is
\[
u_*=\frac{-c+\sqrt{c^2+4/\mu}}2.
\]
For \(4<\mu<6\) it lies strictly above \(c\), and \(B(u)<u\) throughout \((0,c)\). At \(\mu=6\) the two roots coalesce at \(c\), with \(B(u)<u\) for \(0<u<c\). Hence all initial \(0<u<c\) eventually leave the positive side: otherwise decreasing iterates would converge to a positive fixed point, or to zero despite \(B(0^+)=-c\), both impossible. The negative side is symmetric. For \(6<\mu<8\), \(0<u_*<c\), \(B(u)-u<0\) below \(u_*\) and \(>0\) above it, so the positive nonswitching set is precisely \([u_*,c]\), converging to \(c\); mirror symmetry gives the negative set. Uniform length yields its stated probability.

For all parameters let \(r_0=0\), and recursively let \(r_n\in(0,c)\) be the unique inverse positive-branch image of \(r_{n-1}\): \(B(r_n)=r_{n-1}\). Monotonicity implies the positive-side points staying positive for the first \(n\) steps are precisely \((r_n,c]\). Their negative counterparts have the same length, so
\[
\Pr(\tau>n)=\frac{c-r_n}{c}.
\]
For \(4<\mu<6\), put \(v_n=c-r_n\). The inverse branch fixes \(c\) with derivative \(1/\Lambda_\mu<1\). Its Taylor expansion gives \(v_{n+1}=\Lambda_\mu^{-1}v_n+O(v_n^2)\), and standard elementary product estimates yield \(v_n=\Theta_\mu(\Lambda_\mu^{-n})\).

At \(\mu=6\), \(c=1/(2\sqrt3)\) and the right branch has the exact expansion
\[
B(c-v)=c-v-3\sqrt3\,v^2+6v^3.
\]
Set \(a_0=3\sqrt3\). The exact inverse recursion becomes
\[
v_{n-1}=v_n+a_0v_n^2-6v_n^3,\qquad v_0=c.
\]
It follows that \(v_n\searrow0\) and \(v_n\sim1/(a_0n)\). For the second-order term set \(y_n=1/v_n\). Expanding the **exact** reciprocal relation gives
\[
y_n-y_{n-1}=a_0-\frac{a_0^2+6}{y_n}+O(y_n^{-2})
=a_0-\frac{33}{y_n}+O(y_n^{-2}).
\]
First \(y_n=a_0n+O(\log n)\). Summing the corrected relation therefore yields
\[
y_n=a_0n-\frac{33}{a_0}\log n+O(1).
\]
Inversion and division by \(c\) give
\[
\frac{v_n}{c}=\frac{2}{3n}+\frac{22\log n}{27n^2}+O(n^{-2}).
\]
The harmonic first term makes \(\mathbb E\tau=\sum_{n\ge0}\Pr(\tau>n)\) infinite, while \(\Pr(\tau=\infty)=\lim_n \Pr(\tau>n)=0\). This proves all cases.

## Verification
The standalone \(\texttt{check.py}\) verifies the exact endpoint and fixed-point identities for eight admissible parameters, branch monotonicity on a rational grid and inverse-branch critical tails through ten thousand iterations. It reports \(n\Pr(\tau>n)\) approaching \(2/3\). These are finite consistency checks, **not proofs** of the infinite asymptotics; the proof above handles every real parameter in the stated open interval.

## Relationship to prior work
Bartłomiejczyk, Llovera Trujillo and Signerska-Rynkowska (2024) introduced and analyzed the cubic voltage subsystem, especially its expanding Lorenz regimes, rotation intervals, invariant probability measures and spike itineraries. Their study expressly notes the interest of nonexpanding cases and slow passage near near-diagonal fixed points. The present fixed-endpoint symmetric curve and the trichotomy for the first sign change, including its exact critical constants, are not stated in its inspected text. Standard parabolic intermittency explains the qualitative inverse-time mechanism, and the neutral Lorenz **flow** studied by Bruin and Canales Farías (2023) is a different dynamical object. Neither is claimed as a new general method. This is a model-specific quantified transition, not a claim that inverse-time tails are novel in general.

## Limitations
The symmetric full-branch constraint is a codimension-three parameter slice, chosen naturally by the midpoint reflection and fixed-endpoint equations; extending the transition to unconstrained parameters is open. The first-sign-change statistic is not the full distribution of consecutive spikes in a stationary state. No mixing-rate or invariant-density claim is made. Independently unindexed versions of the same exact calculations remain a publication-priority risk.

## References
1. P. Bartłomiejczyk, F. Llovera Trujillo and J. Signerska-Rynkowska, *Analysis of dynamics of a map-based neuron model via Lorenz maps*, Chaos **34**, 043110 (first publicly released 2024-04-01), DOI: 10.1063/5.0188464. Full text studied, especially Sections III–V and VIII.
2. H. Bruin and H. H. Canales Farías, *Mixing Rates of the Geometrical Neutral Lorenz Model*, Journal of Statistical Physics **190**, 198 (2023), DOI: 10.1007/s10955-023-03212-5 (a related neutral Lorenz flow, not the present map).
3. F. Llovera Trujillo, *Discrete neuron models from the point of view of dynamical system theory*, doctoral dissertation, Gdańsk, 2025 (open institutional compilation of the 2024 primary article).
