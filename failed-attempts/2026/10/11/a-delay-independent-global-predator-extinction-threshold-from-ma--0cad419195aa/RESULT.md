# A delay-independent global predator-extinction threshold from maturation survival

## Finding

Consider the delayed predator–prey system
\[
\begin{aligned}
\dot P_1(t)&=\frac{rP_1(t)}{1+k f P_3(t-\tau_1)}-d_1P_1(t)-c_1P_1(t)^2
-\frac{b_2P_1(t)P_3(t)}{(1+b_1P_1(t))(1+kb_3P_3(t))},\\
\dot P_2(t)&=\frac{\eta b_2P_1(t)P_3(t)}{(1+b_1P_1(t))(1+kb_3P_3(t))}
-(d_2+c_2)P_2(t),\\
\dot P_3(t)&=c_2P_2(t-\tau_2)-d_3P_3(t)-c_3P_3(t)^2.
\end{aligned}
\]
Assume all model parameters are positive, \(\tau_1,\tau_2\ge0\), the initial histories are positive, and \(r>d_1\). Put
\[
M=\frac{r-d_1}{c_1},\qquad
\mathcal R_{\mathrm{mat}}
=\frac{\eta b_2c_2}{d_3(d_2+c_2)}
\frac{r-d_1}{c_1+b_1(r-d_1)}.
\]
If \(\mathcal R_{\mathrm{mat}}<1\), then every positive solution obeys
\[
P_1(t)\longrightarrow M,\qquad P_2(t)\longrightarrow0,\qquad P_3(t)\longrightarrow0.
\]
Consequently the predator-free equilibrium \((M,0,0)\) is globally attracting among positive histories for arbitrary values of both delays. In particular, the strict positive cone contains no equilibrium, periodic orbit, or compact invariant recurrent set under this condition.

The threshold is exactly the strict local predator-free stability condition stated by Kong and Shao for the undelayed system, after division by \((d_2+c_2)d_3\). Thus the same invasion threshold is globally decisive even after both fear and maturation delays are introduced.

## Assumptions and scope

The result concerns the deterministic delay system printed as equation (1.3) in Kong and Shao. Positivity of parameters and histories is assumed as in that source. The conclusion is proved for \(r>d_1\) and the strict inequality \(\mathcal R_{\mathrm{mat}}<1\). The equality case \(\mathcal R_{\mathrm{mat}}=1\) is not claimed.

The factorization
\[
1+b_1P_1+kb_3P_3+kb_1b_3P_1P_3=(1+b_1P_1)(1+kb_3P_3)
\]
is used throughout. No small-delay, local-linearization, or small-amplitude hypothesis is imposed.

## Proof

First,
\[
\dot P_1\le P_1\bigl((r-d_1)-c_1P_1\bigr),
\]
because the fear factor can only reduce the birth term and predation is nonnegative. Therefore
\[
\limsup_{t\to\infty}P_1(t)\le M.
\]

Set
\[
a=\frac{c_2}{d_2+c_2}
\]
and define
\[
L(t)=aP_2(t)+P_3(t)+c_2\int_{t-\tau_2}^t P_2(s)\,ds.
\]
Direct differentiation along a positive solution gives the exact cancellation
\[
\dot L
=a\eta b_2\frac{P_1P_3}{(1+b_1P_1)(1+kb_3P_3)}-d_3P_3-c_3P_3^2.
\]
Indeed, the coefficient of the current immature-predator term is
\[
-a(d_2+c_2)+c_2=0,
\]
and the delayed maturation term from \(\dot P_3\) is cancelled by the lower endpoint of the integral.

Let
\[
h(x)=\frac{x}{1+b_1x}.
\]
Then \(h\) is increasing on the nonnegative half-line, and
\[
\frac{P_1P_3}{(1+b_1P_1)(1+kb_3P_3)}\le h(P_1)P_3.
\]
Since \(\mathcal R_{\mathrm{mat}}<1\), continuity of \(h\) allows a number \(\varepsilon>0\) such that
\[
\delta=d_3-a\eta b_2h(M+\varepsilon)>0.
\]
The logistic upper comparison makes \(P_1(t)\le M+\varepsilon\) for all sufficiently large \(t\). Hence, eventually,
\[
\dot L(t)\le-\delta P_3(t)-c_3P_3(t)^2.
\]
Thus \(L\) is eventually decreasing and bounded below, and
\[
\int_T^\infty P_3(t)\,dt<\infty
\]
for some finite \(T\). The same inequality bounds \(P_2\) and \(P_3\) after \(T\); boundedness before \(T\) follows from existence on the finite interval. Therefore \(\dot P_3\) is bounded. The function \(P_3\) is uniformly continuous and integrable, so the standard Barbalat argument yields
\[
P_3(t)\to0.
\]

The immature-predator equation satisfies, for some finite bound \(B\) on \(P_1\),
\[
\dot P_2\le \eta b_2B P_3-(d_2+c_2)P_2.
\]
Variation of constants and \(P_3(t)\to0\) imply \(P_2(t)\to0\).

Finally, because also \(P_3(t-\tau_1)\to0\), the prey equation can be written
\[
\frac{\dot P_1}{P_1}=(r-d_1)-c_1P_1+q(t),
\qquad q(t)\to0.
\]
For every sufficiently small \(\epsilon>0\), scalar logistic comparison eventually gives
\[
\frac{r-d_1-\epsilon}{c_1}
\le \liminf_{t\to\infty}P_1(t)
\le \limsup_{t\to\infty}P_1(t)
\le \frac{r-d_1}{c_1}.
\]
Letting \(\epsilon\downarrow0\) proves \(P_1(t)\to M\).

## Verification

The derivative of \(L\), the algebraic equivalence of the threshold with the source's local stability condition, and the exact numerical example below were checked symbolically in the accompanying verifier.

For the source's numerical coefficients
\[
r=3,\ d_1=\frac1{10},\ c_1=\frac1{10},\ b_1=\frac12,\ b_2=\frac35,\ d_2=\frac1{10},\ d_3=\frac1{10},
\]
together with \(c_2=\frac45\), the new threshold is
\[
\eta<\frac{93}{928}\approx0.1002155172.
\]
The source's cruder sufficient extinction condition \(\eta b_2/b_1<d_3\) gives only
\[
\eta<\frac1{12}\approx0.0833333333.
\]
Thus, for these coefficients, the maturation-aware threshold certifies a strictly larger extinction region.

## Relationship to prior work

Kong and Shao introduce the delayed Crowley–Martin model with predator stage structure, prove positivity and boundedness, and discuss extinction. Their Section 2 gives the sufficient condition \(\eta b_2/b_1<d_3\) for predator extinction. Their Theorem 3.1 gives the undelayed local predator-free stability condition
\[
(d_2+c_2)d_3-
\frac{\eta c_2b_2(r-d_1)}{c_1+b_1(r-d_1)}>0.
\]
The present result shows that this latter condition is not merely local: in its strict form it forces global predator extinction for the full two-delay system.

Related literature proves global stability for other delayed predator–prey models, including systems with fear but without this immature/mature predator chain and systems with stage structure for prey. Those results do not imply the stated threshold for the Kong–Shao Crowley–Martin system. A related stage-structured literature contains global predator-extinction results for different functional responses and state structures; this is recorded as a residual comparison risk rather than treated as evidence of uniqueness.

## Limitations

The boundary case \(\mathcal R_{\mathrm{mat}}=1\) is unresolved here. No convergence rate is asserted. The theorem does not describe the superthreshold regime \(\mathcal R_{\mathrm{mat}}>1\), where coexistence equilibria, oscillations, and more complicated delayed dynamics may occur. The literature comparison cannot exclude an equivalent theorem in every inaccessible or differently parameterized stage-structured predator model.

## References

1. W. Kong and Y. Shao, “The effects of fear and delay on a predator-prey model with Crowley-Martin functional response and stage structure for predator,” *AIMS Mathematics* 8(12) (2023), 29260–29289. DOI: 10.3934/math.20231498.
2. Y. Shao, “Global stability of a delayed predator–prey system with fear and Holling-type II functional response in deterministic and stochastic environments,” *Mathematics and Computers in Simulation* 200 (2022), 65–77. DOI: 10.1016/j.matcom.2022.04.013.
3. K. Chakraborty, S. Haldar, and T. K. Kar, “Global stability and bifurcation analysis of a delay induced prey-predator system with stage structure,” *Nonlinear Dynamics* 73 (2013), 1307–1325. DOI: 10.1007/s11071-013-0864-1.
4. L. Wang and G. Feng, “Global dynamics of a predator-prey model with stage structure and Holling type-II functional response,” DOI: 10.1007/s12190-014-0762-9.
