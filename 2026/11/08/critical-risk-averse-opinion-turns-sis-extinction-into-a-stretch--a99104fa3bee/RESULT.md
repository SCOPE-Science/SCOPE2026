# Critical risk-averse opinion turns SIS extinction into a stretched exponential

## Finding

In the single-population coupled opinion–SIS model specified below, simultaneous criticality of ordinary SIS transmission and baseline opinion formation has an asymmetric consequence. For **every** strictly infected and strictly risk-averse initial state, infection goes extinct at a stretched-exponential rate with an exact positive prefactor. The opinion variable approaches neutrality at inverse-square-root speed, with a signed logarithmic correction in its reciprocal square.

Write \(c=1/3-k_x>0\), \(d=2/15-k_x\), and \(A=2c/\tau_x\). There exist constants \(K\in\mathbb R\) and \(P_\infty\in(0,\infty)\), depending on the initial state and parameters, such that

\[
\frac{1}{x(t)^2}=At-\frac{d}{c}\log t+K+o(1),
\qquad
p(t)\exp\!\left(\beta\sqrt{\frac{2\tau_x}{c}}\sqrt t\right)\longrightarrow P_\infty.
\]

In particular, \(\sqrt t(-x(t))\to A^{-1/2}\). At the **same two critical parameter values**, exactly neutral initial opinion \(x(0)=0\) is invariant and yields ordinary SIS clearance \(p(t)=p(0)/(1+\beta p(0)t)\), a \(1/t\) law rather than stretched-exponential decay. The logarithmic correction to reciprocal opinion square is negative for \(k_x<2/15\), zero for \(k_x=2/15\), and positive for \(2/15<k_x<1/3\).

## Assumptions and scope

The deterministic, single-population NOD–SIS system of Ordorica Arango et al. is

\[
\dot p=\bar\beta(1+x)(1-p)p-\delta p,\qquad
\tau_x\dot x=-x+\tanh\big((k_p p+k_x x^2+u_0)x\big).
\]

Here \(p\in[0,1]\) is infected prevalence and \(x\in[-1,1]\) is the signed behavioral opinion (negative means risk-averse). Fix

\[
0<\beta<1,\quad \bar\beta=\delta=\beta,\quad u_0=1,\quad
0<k_p<1,\quad 0\le k_x<1/3,\quad \tau_x>0,
\]

and all initial conditions \(0<p(0)<1\), \(-1<x(0)<0\). Parameters remain fixed as time tends to infinity. This is the *double critical boundary*: the basic SIS threshold is exactly one and the linearized opinion relaxation coefficient is exactly zero. The source paper's principal equilibrium theorem assumes \(u_0<1\); the model itself permits the present boundary \(u_0=1\).

All limits are in the physical time \(t\) of the displayed equations; the time constant \(\tau_x\) has **not** been normalized away. No global stability claim is made for positive initial opinion.

## Proof

**1. Invariant sector and comparison.** Put \(y=-x\), so \(0<y(0)<1\) and

\[
\dot p=-\beta p\{y+(1-y)p\},\qquad
\tau_x\dot y=F(y,p):=\tanh\big((1+k_p p+k_x y^2)y\big)-y.
\]

The boundaries \(p=0\) and \(y=0\) are invariant; at \(p=1\) the vector field points inward and at \(y=1\) it points inward. Smooth uniqueness consequently gives \(0<p(t)<1\), \(0<y(t)<1\) at finite times. Since \(y+(1-y)p\ge p\),

\[
\dot p\le-\beta p^2,
\qquad
0<p(t)\le\frac{p(0)}{1+\beta p(0)t}\longrightarrow0.
\]

For \(0<z<1\), \(\operatorname{arctanh}(z)>z+z^3/3\), so \(k_x<1/3\) implies

\[
F(z,0)=\tanh(z+k_xz^3)-z<0.
\]

Let \(z(t)\) solve \(\tau_x\dot z=F(z,0)\) with \(z(0)=y(0)\). It decreases to zero, and the Taylor expansion

\[
F(z,0)=-cz^3+dz^5+O(z^7),\qquad c=1/3-k_x,
\quad d=2/15-k_x
\]

shows, by differentiating \(z^{-2}\), that \(z(t)\sim(At)^{-1/2}\) with \(A=2c/\tau_x\). Since \(F(y,p)\ge F(y,0)\), scalar comparison yields \(y(t)\ge z(t)\) for all \(t\). Hence

\[
0<p(t)\le p(0)\exp\!\left(-\beta\int_0^t z(s)\,ds\right)
=\exp\!\left(-\frac{2\beta}{\sqrt A}\sqrt t+o(\sqrt t)\right),
\]

where multiplicative constants have been incorporated into the logarithmic error. In particular, for some \(a>0\) and \(M<\infty\) one has \(p(t)\le M e^{-a\sqrt t}\), \(\int_0^\infty p(t)\,dt<\infty\), and \(p(t)/y(t)^2\le p(t)/z(t)^2=O(te^{-a\sqrt t})\).

**2. Opinion extinction.** For any \(\epsilon\in(0,1)\), the continuous function \(F(y,0)\) is strictly negative on \([\epsilon,1]\). As \(p(t)\to0\), the same is true uniformly of \(F(y,p(t))\) for sufficiently large time. Therefore \(y\) eventually enters \((0,\epsilon)\) and cannot subsequently leave it. As \(\epsilon\) is arbitrary, \(y(t)\to0\).

**3. Sharp reciprocal-square law.** The smooth Taylor expansion, uniform for small positive \(p,y\), is

\[
F(y,p)=k_p p y-cy^3+dy^5+O(py^3+y^7),
\]

where the cross term \(O(py^3)\) also covers higher powers of \(p\) in bounded neighborhoods. Set \(w=y^{-2}\). Differentiating gives

\[
\dot w=A-\frac{2d}{\tau_x w}
-\frac{2k_p}{\tau_x}p w+O(p+w^{-2}).
\]

The comparison in Step 1 yields \(w(t)\le z(t)^{-2}=O(t)\); hence \(p w\to0\). Because \(w\to\infty\), the displayed identity gives \(\dot w\to A\), and therefore \(w(t)/t\to A\). Consequently \(w^{-1}=O(1/t)\) for large \(t\), and all terms besides the displayed \(1/w\) term are integrable in time. It follows first that \(w(t)=At+O(\log t)\). Substitution then improves the equation to

\[
\dot w=A-\frac{d}{ct}+O\!\left(\frac{\log t}{t^2}\right)+O\!\left(t e^{-a\sqrt t}\right).
\]

The two remainders are absolutely integrable on \([1,\infty)\); thus \(w(t)-At+(d/c)\log t\) converges to a finite real constant \(K\), proving the first formula.

**4. Infection prefactor.** From Step 3,

\[
y(t)=\frac1{\sqrt{At}}+O\!\left(\frac{\log t}{t^{3/2}}\right).
\]

The error is integrable on \([1,\infty)\), as is \((1-y)p\). Since

\[
\frac{d}{dt}\log p=-\beta y-\beta(1-y)p,
\]

integration gives \(\log p(t)=-(2\beta/\sqrt A)\sqrt t+\log P_\infty+o(1)\) with finite \(\log P_\infty\), so \(P_\infty>0\). Finally \(2\beta/\sqrt A=\beta\sqrt{2\tau_x/c}\). If \(x(0)=0\) instead, uniqueness forces \(x(t)=0\) identically and the first equation reduces exactly to \(\dot p=-\beta p^2\).

This completes the proof for every initial condition in the stated strict risk-averse interior sector.

## Verification

The standalone Python 3 program `verify.py` uses SymPy to check the cubic and fifth-order coefficients, the signed logarithmic coefficient, and the normalized example. Its SciPy initial-value integration checks finite-time trend consistency but is **not** used to certify the infinite-time limit. The program was executed from the actual packaged directory and printed `VERIFY_OK`.

For \(\beta=\delta=1/2\), \(k_p=1/2\), \(k_x=1/6\), \(u_0=1\), and \(\tau_x=1\), the exact formulas reduce to

\[
\frac1{x(t)^2}=\frac t3+\frac15\log t+K+o(1),
\qquad p(t)e^{\sqrt{3t}}\longrightarrow P_\infty>0.
\]

With initial state \((p(0),x(0))=(0.4,-0.6)\), direct integration gives an estimated value of \(K\) of approximately \(-0.08535\) at \(t=25600\) and \(-0.08538\) at \(t=40000\). These are diagnostics and do not define \(K\) or prove its existence.

## Relationship to prior work

The originating 2024 preprint establishes equilibria and bifurcations in the NOD–SIS system, primarily under \(u_0<1\), including the usual SIS transcritical threshold and the possibility of risk-averse extinction. It does not state the double-critical \(u_0=1\), \(\bar\beta=\delta\) large-time laws above. The NOD background paper analyzes saturating opinion dynamics and pitchfork-type transitions but not their coupling to infection or the resulting stretched exponential. The related actSIS network model uses a different feedback mechanism and addresses equilibria/secondary bifurcations rather than this two-component double-critical asymptotic.

The structural fact that an equation of the form \(\dot y=-cy^3+\cdots\) can produce a \(t^{-1/2}\) decay is standard and not claimed as novel. The new result is its exact global coupling to the NOD–SIS epidemic at two simultaneous thresholds, the positive stretched-exponential prefactor valid throughout the risk-averse sector, and the model-specific sign-changing logarithmic correction.

## Limitations

This is a deterministic homogeneous-population result, restricted to weak peer pressure, exact simultaneous thresholds, and negative or exactly neutral initial opinion. It does not address finite-population stochastic extinction times, heterogeneous network SIS, positive-opinion dynamics, or the strong-peer-pressure boundary \(k_x=1/3\). The cited source literature and indexed comparisons do not rule out all unindexed equivalent priority claims. Symbolic expansion and numerical checks are subordinate to the complete asymptotic proof above; independent external validation remains outstanding.

## References

1. M. Ordorica Arango, A. Bizyaeva, S. A. Levin, and N. E. Leonard, *Opinion-driven risk perception and reaction in SIS epidemics*, arXiv:2410.12993, first public version 2024-10-16, https://arxiv.org/abs/2410.12993 (the accessible current preprint version was inspected in full).
2. A. Bizyaeva, A. Franci, and N. E. Leonard, *Nonlinear Opinion Dynamics with Tunable Sensitivity*, arXiv:2009.04332, https://arxiv.org/abs/2009.04332 (full open-access text inspected).
3. A. Bizyaeva, M. Ordorica Arango, Y. Zhou, S. Levin, and N. E. Leonard, *Active risk aversion in SIS epidemics on networks*, arXiv:2311.02204, https://arxiv.org/abs/2311.02204 (abstract-level comparison only; full text unavailable during the comparison).
