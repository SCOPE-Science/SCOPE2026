# A wildfire-hazard reversal in the optimal fire deadline for maturing canopy seed banks

## Finding

Consider a simplified serotinous canopy seed bank with a maturation delay and exponential loss of stored viable seeds. An elective fire at age \(T\) is preempted if an independent wildfire occurs first. The objective is the expected viable seed release at the first fire divided by the expected time until that fire. This *release-rate proxy* has a unique finite maximizing deadline whenever both maturation delay and seed loss are positive. The optimizer becomes **later**, not earlier, as the wildfire hazard rises, and becomes earlier as seed loss increases. If either positive seed decay is removed or the maturation delay is removed, the finite interior optimum disappears. The exact optimizer and strict comparative statics are below.

Let \(m>0\) be maturation age, \(\delta>0\) be the rate of decay of viable stored seeds, \(\mu>0\) the constant wildfire hazard, and \(r>0\) the constant seed-production rate after maturation. Define \(b=\mu+\delta\). The unique maximizing finite deadline \(T_*\) is the root in \((m,\infty)\) of

\[
 b e^{\mu T}-\mu e^{b(T-m)}-\delta=0.
\]

It obeys the strict, explicit bracket

\[
 \frac{bm}{\delta}<T_*<\frac{bm}{\delta}+\frac1\delta\log\left(1+\frac\delta\mu\right).
\]

It increases strictly with \(\mu\) and \(m\) and decreases strictly with \(\delta\). In particular,

\[
 \lim_{\mu\to\infty}\frac{\delta T_*}{\mu m}=1,
 \qquad \lim_{\delta\downarrow0}\delta T_*=\mu m
\]

with the other positive parameters held fixed. No population-survival or ecosystem-wide optimization assertion is made.

## Assumptions and scope

A single idealized stand is born at age zero; until age \(m\), it produces no seeds, and afterward produces \(r\) seeds per unit time. A seed of age \(a\) remains viable with probability \(e^{-\delta a}\). No mortality of parent plants, density effect, competition, changing fire severity, spatial spread, recruitment failure, spontaneous seed release, or fire-induced loss of viable stored seeds is included. The viable canopy seed stock just before a fire at age \(t\) is thus

\[
 B(t)=\begin{cases}
 0,&0\le t\le m,\\
 \dfrac r\delta\bigl(1-e^{-\delta(t-m)}\bigr),&t>m.
 \end{cases}
\]

An independent unplanned fire occurs at \(F\sim\mathrm{Exp}(\mu)\). The prescribed deadline is \(T\in(0,\infty)\); the actual fire time is \(S_T=\min(F,T)\). All stock at that first fire is counted as released. Define the well-specified yield-rate proxy

\[
 J(T)=\frac{\mathbb E[B(S_T)]}{\mathbb E[S_T]}.
\]

For positive \(\mu\), an extended \(T=\infty\) policy (no elective fire) has \(S_\infty=F\) and is admissible. This ratio is an objective for **one cohort**, not the probability of successful regeneration. If externally reset and independent cycles exist, it is also a renewal-reward rate; the theorem does not assume or prove that fire produces a viable subsequent cohort.

## Proof

**1. Exact expected reward and duration.** For \(T>m\), integration by parts (equivalently, the layer-cake identity) gives

\[
 \mathbb E[B(S_T)]
 =\int_m^T e^{-\mu t}B'(t)\,dt
 =\frac{r e^{-\mu m}}{\mu+\delta}
 \bigl(1-e^{-(\mu+\delta)(T-m)}\bigr).
\]

Also \(\mathbb E[S_T]=(1-e^{-\mu T})/\mu\). Consequently,

\[
 J(T)=\frac{r\mu e^{-\mu m}}b
 \frac{1-e^{-b(T-m)}}{1-e^{-\mu T}}
 \quad (T>m),
\]

and \(J(T)=0\) for \(T\le m\). At infinity the ratio tends to \(J_\infty=r\mu e^{-\mu m}/b>0\).

**2. One and only one interior maximizer.** The sign of \(J'(T)\) for \(T>m\) is the sign of

\[
 Q(T)=b e^{\mu T}-\mu e^{b(T-m)}-\delta.
\]

We have \(Q(m)=b(e^{\mu m}-1)>0\), and

\[
 Q'(T)=\mu b\bigl(e^{\mu T}-e^{b(T-m)}\bigr).
\]

The derivative is positive until \(T_0=bm/\delta\) and strictly negative thereafter. Moreover \(Q(T_0)=\delta(e^{\mu T_0}-1)>0\), while \(Q(T)\to-\infty\) as \(T\to\infty\). Therefore \(Q\) has exactly one zero \(T_*>T_0\), and \(J\) rises strictly on \((m,T_*)\), then falls strictly on \((T_*,\infty)\). It follows that \(T_*\) is the unique global maximizer over all positive finite and infinite deadlines. Rearrangement of \(Q(T_*)=0\) gives

\[
 e^{\delta T_*-bm}=\frac b\mu-\frac\delta\mu e^{-\mu T_*}.
\]

Because \(T_*>T_0\), the left side is strictly greater than one; the right side is strictly smaller than \(b/\mu\), proving the bracket.

**3. Hazard, decay, and maturity comparative statics.** Write

\[
 L(k,z)=\frac{k}{e^{kz}-1},\qquad
 g(T;\mu,\delta,m)=L(\mu+\delta,T-m)-L(\mu,T).
\]

The critical point satisfies \(g(T_*)=0\). Let \(\ell=L(b,T_*-m)=L(\mu,T_*)>0\). Direct differentiation shows

\[
 \partial_Tg\big|_{T_*}=-\delta\ell<0.
\]

For \(u>0\), define

\[
 H(u)=\frac{e^u-1-u e^u}{(e^u-1)^2}.
\]

It is negative and strictly increasing: its derivative has the sign of \((u-2)e^u+u+2\), whose value and first derivative vanish at zero and whose second derivative is \(u e^u>0\). Since \(T_*>bm/\delta\), we have \(b(T_*-m)>\mu T_*\). Hence

\[
 \partial_\mu g\big|_{T_*}=H(b(T_*-m))-H(\mu T_*)>0,
 \quad \partial_\delta g\big|_{T_*}=H(b(T_*-m))<0.
\]

Also \(\partial_m g\big|_{T_*}=\ell(b+\ell)>0\). Implicit differentiation with \(\partial_Tg<0\) proves

\[
 \frac{\partial T_*}{\partial\mu}>0,\qquad
 \frac{\partial T_*}{\partial\delta}<0,\qquad
 \frac{\partial T_*}{\partial m}>0.
\]

This is global for every \(\mu,\delta,m>0\), not a local numerical trend.

**4. Degenerate boundaries and limits.** If \(m=0\) with \(\delta>0\), the same \(Q\) has \(Q(0)=0\) and \(Q'(T)<0\) for all \(T>0\), so \(J\) strictly decreases: the supremum is approached only as \(T\downarrow0\). If \(\delta=0\) and \(m>0\), use the continuous-limit stock \(B(t)=r(t-m)_+\). For \(\mu>0\),

\[
 J(T)=r e^{-\mu m}
 \frac{1-e^{-\mu(T-m)}}{1-e^{-\mu T}}
 \quad (T>m),
\]

which strictly increases in \(T\), with supremum only at \(T=\infty\). If \(\delta=m=0\), then \(B(t)=rt\), and \(J(T)=r\) for every positive finite deadline. The analogous limits when \(\mu=0\) are obtained by taking \(F=\infty\): for \(m,\delta>0\),

\[
 J(T)=\frac{r}{\delta T}(1-e^{-\delta(T-m)})
\]

has exactly one maximizing \(T>m\), solving \(e^{\delta(T-m)}=1+\delta T\). When \(\mu\downarrow0\), the positive-hazard optimizer converges to that root (divide \(Q\) by \(\mu\) and pass to the limit on compact intervals). In the remaining degenerate cases at zero hazard, \(m=0,\delta>0\) makes the rate strictly decreasing, \(m>0,\delta=0\) makes it strictly increasing, and \(m=\delta=0\) makes it constant.

Finally the explicit bracket implies \(T_*=\mu m/\delta+m+O(1/\mu)\) as \(\mu\to\infty\), and \(\delta T_*\to\mu m\) as \(\delta\downarrow0\) for fixed \(\mu,m>0\). The improvement over doing no planned burn tends to zero at high wildfire hazard: using \(T_*>bm/\delta\), the relative gain is positive but bounded above by

\[
 \frac{\delta}{b}\frac{e^{-\mu T_*}}{1-e^{-\mu T_*}}.
\]

This resolves the apparently paradoxical divergence of the elective deadline: waiting longer has vanishing incremental benefit when spontaneous fires are already overwhelmingly likely before maturity.

## Verification

A standalone Python 3 program `check.py` numerically reproduces the optimum by bisection on a scaled critical-point equation, checks its global ordering on a deterministic parameter grid, checks the signs of its parameter responses, independently approximates the expected reward integral, and verifies the zero-decay and zero-maturity boundary monotonicities. Its recorded replay on the embedded file yielded **91,091 passing deterministic assertions**. Numerical finite sampling is corroboration, not proof of the statements quantified over all positive real parameters. The exact derivative and sign arguments above supply the global proof.

With \(m=1\), \(\delta=1\), \(\mu=1/4\), and \(r=1\), the optimum is \(T_*=2.251203073190526\ldots\), with \(J(T_*)=0.286160317878394\ldots\), versus \(J(\infty)=0.155760156614281\ldots\). The rate proxy is about \(83.72\%\) larger under the optimal finite deadline. These parameter values are illustrative and not field estimates.

## Relationship to prior work

Enright, Marsula, Lamont and Wissel (1998) model how reproductive maturation, seed viability, and variable fire intervals influence serotinous plant population growth. Lamont and Enright (2000) discuss canopy storage and the loss of viability in aging cones. McCarthy, Possingham and Gill (2001) analyze stochastic unplanned fires and prescribed fire management via finite-state stochastic dynamic programming, optimizing persistence and management outcomes that depend on both plant density and time since fire. These motivate the ingredients, but **their reported results are not the present continuous-time single-cohort release-rate theorem**, and their objectives differ from \(J\). No priority claim is made for the renewal-reward ratio or for elementary exponential integration in isolation. The mathematical statement assessed here combines the exact global finite-deadline phase, strict hazard/decay/maturation comparative statics, and singular zero-decay boundary in this explicitly normalized seed-stock model. A general age-replacement theorem may cover parts of the analysis; no exhaustive historical priority claim is made.

## Limitations

This is not a fire-management recommendation, a prescription for endangered populations, or a prediction of population persistence. It optimizes the expected viable seed release **per expected time**, rather than expected regeneration probability, survival, economic value, biodiversity, or suppression cost. The same stock size is used at either wildfire or prescribed fire, and the model neglects standing-plant senescence, fuel changes, age-dependent ignition, spatial spread, recruitment stochasticity, loss during burning, seasonal seed production, maximum plant lifespan, and the possibility that a fire before maturity causes local extinction. A long optimal elective deadline in the high-wildfire-hazard limit does not imply that delaying fires is safe. The simplest exponential assumptions and a single-age maturity threshold may fail under empirical conditions. Historical originality is provisional against broader replacement-policy and renewal-reward literature.

## References

1. McCarthy, M. A., Possingham, H. P., and Gill, A. M. (2001). *Using stochastic dynamic programming to determine optimal fire management for Banksia ornata*. Journal of Applied Ecology 38, 585–592. First published 21 December 2001. https://doi.org/10.1046/j.1365-2664.2001.00617.x
2. Enright, N. J., Marsula, R., Lamont, B. B., and Wissel, C. (1998). *The ecological significance of canopy seed storage in fire-prone environments: a model for non-sprouting shrubs*. Journal of Ecology 86, 946–959. https://doi.org/10.1046/j.1365-2745.1998.00312.x
3. Lamont, B. B., and Enright, N. J. (2000). *Adaptive advantages of aerial seed banks*. Plant Species Biology 15, 157–166. https://doi.org/10.1046/j.1442-1984.2000.00036.x
