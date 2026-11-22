# Simultaneous mean, variance, and relative-risk optimality of unequal tumbling in two-particle ring encounters

## Finding

Fix a ring of circumference \(L>0\), a common particle speed \(v>0\), and a strictly positive total individual direction-reversal rate \(g>0\). Two labeled, independently moving run-and-tumble particles flip their velocity signs at rates \(a,b\ge0\), with \(a+b=g\). Initial positions are independent uniform on the ring and initial velocity signs are independent fair signs. Let \(T\) be their **first physical encounter time** (the process is stopped at first contact, before any jamming or contact response). Define

\[
\kappa=\frac{2ab}{g},\qquad r=\frac{gL}{v},\qquad h=\frac{\kappa L}{v}=\frac{2abL}{gv}\in[0,r/2].
\]

Then all three first-contact performance statistics are exact:

\[
\boxed{\mathbb ET=\frac Lv\left(\frac12+\frac h{12}+\frac1{2r}\right)},
\]

\[
\boxed{\operatorname{Var}(T)=\left(\frac Lv\right)^2\frac{7h^2+60h+60+180h/r+360/r+540/r^2}{720}},
\]

\[
\boxed{\frac{\operatorname{Var}(T)}{(\mathbb ET)^2}=
\frac{7r^2h^2+60r^2h+60r^2+180rh+360r+540}{5(rh+6r+6)^2}}.
\]

For every fixed \(r>0\), **all three displayed quantities increase strictly with \(h\) throughout \([0,r/2]\)**. Hence they share exactly the same set of global minimizers at fixed reversal budget: \((a,b)=(g,0)\) or \((0,g)\). Their unique global maximizer is the balanced pair \(a=b=g/2\). Thus transferring all available reversals to one particle simultaneously minimizes the mean, absolute variance, and squared coefficient of variation of first contact. If both individual rates are required to be strictly positive, the same endpoint values are sharp unattained infima; the equal-rate maximum remains attained. This comparison does **not** assert stochastic ordering of the entire contact-time distributions.

## Assumptions and scope

Positions lie in \(\mathbb R/L\mathbb Z\). Before first contact, \(\dot X_1=v\sigma_1\) and \(\dot X_2=v\sigma_2\), with \(\sigma_i\in\{-1,+1\}\). Sign \(\sigma_1\) flips at the times of a rate-\(a\) Poisson process and \(\sigma_2\) independently at rate \(b\). At least one rate is positive; exactly zero is permitted for the other. There is no translational diffusion, drift, excluded-volume force prior to contact, or finite tumbling duration. The initial oriented gap \(x=(X_2-X_1)\bmod L\) is uniform on \((0,L)\), independent of the four equiprobable velocity-sign pairs. First contact occurs when the gap reaches either \(0\) or \(L\) from the open interval.

The four states are \(A=(+,-)\) (gap velocity \(-2v\)), \(B=(-,+)\) (gap velocity \(+2v\)), \(C=(+,+)\) and \(D=(-,-)\) (both with zero gap velocity). Only the **incoming absorbing conditions** \(f_A(0)=0\) and \(f_B(L)=0\) are imposed on conditional first moments, with analogous conditions for second moments. The outgoing values need not vanish. From either moving state, a no-flip interval of duration \(L/(2v)\) guarantees absorption. From a stalled state, one flip during a prescribed bounded interval followed by such a no-flip interval guarantees absorption. Therefore a uniform positive probability of collision in a bounded time gives an exponential tail for \(T\) for every \(g>0\), including the one-frozen-particle endpoints. All polynomial moments exist.

## Proof

**Conditional mean equations.** Write \(f_i(x)=\mathbb E[T\mid x,i]\). The backward generator equations are

\[
\begin{aligned}
-2vf'_A+a(f_D-f_A)+b(f_C-f_A)&=-1,\\
 2vf'_B+a(f_C-f_B)+b(f_D-f_B)&=-1,\\
 a(f_B-f_C)+b(f_A-f_C)&=-1,\\
 a(f_A-f_D)+b(f_B-f_D)&=-1.
\end{aligned}
\]

The last two equations give
\[
 f_C=\frac{1+af_B+bf_A}{g},\qquad
 f_D=\frac{1+af_A+bf_B}{g}.
\]
Eliminating these stalls and applying the two incoming endpoint conditions uniquely yields
\[
 f_A(x)=\frac{x}{v}+\frac{\kappa x(L-x)}{2v^2},\qquad
 f_B(x)=\frac{L-x}{v}+\frac{\kappa x(L-x)}{2v^2}.
\]
The orientation-averaged conditional mean equals \((f_A+f_B)/2+1/(2g)\). Integrating over the uniform gap gives the stated formula for \(\mathbb ET\).

**Conditional second moment equations.** Put \(G_i(x)=\mathbb E[T^2\mid x,i]\). The same generator acts on these with source \(-2f_i\). The two stalled equations give
\[
G_C=\frac{2f_C+aG_B+bG_A}{g},\qquad
G_D=\frac{2f_D+aG_A+bG_B}{g}.
\]
Writing \(S=G_A+G_B\) and \(\Delta=G_A-G_B\), elimination reduces the two differential equations to
\[
\Delta'(x)=\frac{2(f_A+f_B)+2/g}{v},\qquad
S'(x)=\frac{[1+(a-b)^2/g^2](f_A-f_B)-\kappa\Delta}{v}.
\]
The absorbing conditions are \(S(0)=-\Delta(0)\) and \(S(L)=\Delta(L)\). Direct polynomial integration determines
\[
\Delta(0)=-\frac{L\bigl(L^2g\kappa+6Lgv+6v^2\bigr)}{6gv^3}.
\]
These displayed differential equations and this initial value determine the full polynomial solutions; no boundary data are tacitly imposed on outgoing phases. Since
\[
\frac14(G_A+G_B+G_C+G_D)
=\frac12S+\frac{f_A+f_B}{2g}+\frac1{g^2},
\]
uniform-gap integration gives the exact raw second moment
\[
\mathbb ET^2=\left(\frac Lv\right)^2
\frac{h^2+10h+20+20h/r+60/r+60/r^2}{60}.
\]
Subtracting the square of the first moment yields the variance formula. Dividing by the mean squared yields the displayed squared coefficient of variation. Each equality is an identity of rational polynomials on the whole stated domain, including the boundaries \(a=0\) or \(b=0\) by continuity (and the direct generator equations remain valid there).

**Strict three-objective optimization.** At fixed \(r>0\), the derivative of the dimensionless mean with respect to \(h\) is \(1/12\). The derivative of the dimensionless variance is \((14h+60+180/r)/720>0\). Direct differentiation of the squared coefficient of variation gives
\[
\frac{\partial}{\partial h}
\frac{\operatorname{Var}(T)}{(\mathbb ET)^2}
=\frac{24r^2(rh+10r-4h+30)}{5(rh+6r+6)^3}>0.
\]
Indeed \(0\le h\le r/2\) implies \(10r-4h\ge8r\). The product \(ab\) is zero only at the two extreme allocations and is uniquely maximized at \(a=b=g/2\). Since \(h\) is proportional to \(ab\), all three objectives have exactly the claimed simultaneous minimizers and maximizer.

## Verification

The accompanying standalone `verification.py` (Python 3 and SymPy) reconstructs the moment polynomials, tests the generator and the mixed absorbing boundary conditions symbolically, and checks the risk derivative algebra. It also compares the exact formulas against 240,000 independently generated event-driven paths across four allocated-rate choices, including a zero-rate endpoint and an equal-rate case. Its deterministic run reports 10 symbolic identities, 8 symbolic generator equations, and 2 algebraic risk identities, plus the simulation comparisons, all passing. Reproduce by running `python verification.py` with `sympy` installed. The simulation is finite supporting evidence, not a proof of the quantified optimization.

## Relationship to prior work

Hahn, Guillin and Michel (arXiv:2306.00831, first public 2023-06-01), *Jamming pair of general run-and-tumble particles*, give the finite-ring pair dynamics, generator approach and steady-state universality classes. Those are antecedents; their stationary jamming laws do not give an optimized first-contact variance or relative risk under a fixed **sum of distinct individual flipping rates**. Cheliotis, Kontoyiannis, Loulakis and Toumpis (arXiv:1808.03830), Section 4.2, give a potential and first return mean for a pair with a **common** flip rate as part of a message-transfer calculation; the equal-rate mean is not novel here. Le Doussal, Majumdar and Schehr (arXiv:1902.06176) analyze first contact for equal-rate particles on the **infinite line**.

The closest published pair-encounter findings are *First-collision transform and rare-reversal moment singularity for a run-and-tumble pair on a ring* (2026), which computes an initially closing **equal-rate** transform and rare-flip moments, and *A sharp speed-ratio threshold for beneficial tumbling in two-particle ring encounters* (2026), which varies the rate of **both particles together** while their **speeds differ**. Neither establishes the three-observable ordering at varying individual reversal rates and fixed total budget. *Heterogeneous tumbling sharpens the exponential binding length of a jammed two-swimmer pair* (2026) does vary two individual rates at fixed sum, but optimizes a **stationary exponential separation exponent** in a different, linearly attracting model on the infinite line. Exact moment equations and parameter comparisons here are necessary; matching only the four-state generator would not imply the optimization statement. These are comparisons with checked materials, not a claim of an exhaustive literature census or independent publication-priority certification.

## Limitations

The claim requires a common positive speed, a circular domain, independent Poisson velocity reversals and uniform independent starting positions and headings. It applies to **first** encounter only; no post-contact reaction, hard-core jamming dynamics or finite-length tumble is included. Both-rate-positive restrictions remove attainment of the optimal endpoint but not the sharp infimum. It gives no stochastic ordering of full first-contact laws, no finite number-of-particles generalization, and no result for a fixed total physical energy cost when reversal costs differ. Wider or unindexed work using general Markov-modulated fluid first-passage methods may already imply related formulas or an equivalent allocation comparison; such publication-priority uncertainty is not excluded.

## References

1. L. Hahn, A. Guillin and M. Michel, *Jamming pair of general run-and-tumble particles: Exact results and universality classes*, arXiv:2306.00831, first public 2023-06-01; revised version, *Exact results, symmetries and steady-state universality classes* (2025). https://arxiv.org/abs/2306.00831
2. D. Cheliotis, I. Kontoyiannis, M. Loulakis and S. Toumpis, *A Simple Network of Nodes Moving on the Circle*, arXiv:1808.03830, Section 4.2, Lemma 4.5. https://arxiv.org/abs/1808.03830
3. P. Le Doussal, S. N. Majumdar and G. Schehr, *Non-crossing run-and-tumble particles on a line*, arXiv:1902.06176. https://arxiv.org/abs/1902.06176
4. *First-collision transform and rare-reversal moment singularity for a run-and-tumble pair on a ring*, public mathematical research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-first-collision-transform-and-rare-reversal-moment-singularity-f--f5ea568543a0
5. *A sharp speed-ratio threshold for beneficial tumbling in two-particle ring encounters*, public mathematical research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-speed-ratio-threshold-for-beneficial-tumbling-in-two-par--04a25262f2b9
6. *Heterogeneous tumbling sharpens the exponential binding length of a jammed two-swimmer pair*, public mathematical research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-heterogeneous-tumbling-sharpens-the-exponential-binding-length-o--4b3e35d48fc9
