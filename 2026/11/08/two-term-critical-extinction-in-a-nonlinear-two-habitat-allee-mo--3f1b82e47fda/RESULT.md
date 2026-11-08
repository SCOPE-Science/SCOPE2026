# Two-term critical extinction in a nonlinear two-habitat Allee model

## Finding
For the continuous-time two-patch model defined below, an exactly balanced recruitment–dispersal threshold has a globally attracting boundary equilibrium with a sharp, initial-condition-independent two-term extinction profile. Define
\[
B=\frac{s\delta}{s+\delta},\qquad c=\frac{\delta}{s+\delta},\qquad v_0=\frac{s}{s+\delta},\qquad m_c=\frac1{h+B}.
\]
Impose \(e=B\). For every strictly positive initial condition and every \(m\ge m_c\),
\[
(u(t),v(t))\longrightarrow(0,v_0).
\]
At the double threshold \(m=m_c\), the exact two-term asymptotics in the normalized time of the model are
\[
\boxed{u(t)=\frac{m_c}{\sqrt{2t}}+
\left(\frac{m_c}{2}+\frac{\delta^2m_c^2}{2s(s+\delta)}\right)\frac1t+o(t^{-1})},
\]
\[
\boxed{v(t)=v_0+c\frac{m_c}{\sqrt{2t}}+
 c\left(\frac{m_c}{2}+\frac{\delta^2m_c^2}{2s(s+\delta)}\right)\frac1t+o(t^{-1})}.
\]
For \(m>m_c\), write \(\kappa=h+B-1/m>0\). The faster alternative has exact amplitudes
\[
\lim_{t\to\infty}t u(t)=\frac1\kappa,\qquad
\lim_{t\to\infty}t(v(t)-v_0)=\frac{c}{\kappa}.
\]
The mechanism is an exact globally valid, strictly decreasing weighted population product at and above the threshold, together with a cubic cancellation which makes the critical first-patch extinction scale \(t^{-1/2}\) instead of \(t^{-1}\). The leading cubic normal-form information is present in the initiating source; the new statement is the global equality-case conclusion, the exact weighted product and the universal *second* asymptotic coefficient.

## Assumptions and scope
Let \(s,\delta,h>0\), and suppose \(0<B=s\delta/(s+\delta)<1\). Fix the mortality parameter \(e=B\), allow any \(m>0\), and solve the autonomous ODE
\[
\dot u=u\left(\frac{u}{m+u}-e-hu\right)+\delta u(v-u),
\qquad
\dot v=sv(1-v)+\delta v(u-v).
\]
Both initial conditions are arbitrary finite real numbers \(u(0)>0\), \(v(0)>0\). This is exactly the normalized continuous-time ODE (2.1) in Xia, Chen, Srivastava and Parshad [1], not its related discrete-time or spatial PDE variants. All asymptotic coefficients refer to this dimensionless time; they must be rescaled before interpreting dimensional extinction times. The result concerns the two positive habitat density coordinates, not total extinction of both habitats: the second habitat tends to \(v_0>0\).

## Proof
**1. Positivity, boundedness and the surviving habitat.** The coordinate axes are invariant, so strictly positive initial data remain strictly positive by uniqueness. For \(W=u+v\), cancellation of terms gives
\[
\dot W=\frac{u^2}{m+u}-eu+sv-hu^2-sv^2-\delta(u-v)^2
\le u+sv-hu^2-sv^2.
\]
Consequently \(\dot W\le C W-c_*W^2/2\), with \(C=\max\{1,s\}\) and \(c_*=\min\{h,s\}>0\). The positive solution is global and bounded. Moreover,
\[
\dot v\ge v\{s-(s+\delta)v\}.
\]
Comparison with the positive logistic solution yields \(\liminf_{t\to\infty}v(t)\ge v_0>0\).

**2. An exact global logarithmic population law.** Put \(c=\delta/(s+\delta)\) as above. Direct cancellation in the two per-capita equations gives, at \(e=B\),
\[
\frac{d}{dt}\log\bigl(u(t)v(t)^c\bigr)
=\frac{u}{m+u}-(h+B)u
=u\left(\frac1{m+u}-\frac1{m_c}\right).
\]
For \(m\ge m_c\) this is strictly negative whenever \(u>0\). Thus \(P(t)=u(t)v(t)^c\) decreases to a limit \(L\ge0\). If \(L>0\), boundedness of \(v\) forces \(u(t)\) eventually to be bounded below by a positive constant, making the displayed logarithmic derivative bounded above by a strictly negative constant: a contradiction. Hence \(P(t)\to0\). The logistic comparison bounds \(v\) away from zero eventually, so \(u(t)\to0\). The equation \(\dot v=v\{s+\delta u-(s+\delta)v\}\), sandwiched for large time between logistic equations with growth parameters arbitrarily close to \(s\), then yields \(v(t)\to v_0\). This proves global attraction without a small-initial-density assumption or an appeal to finite simulations.

**3. An exact fast-variable reduction.** Define \(z=v-v_0-cu\), \(a=1/m-1/m_c\). Simple algebra, without truncation, gives
\[
\dot u=a u^2-\frac{u^3}{m(m+u)}+\delta uz,
\]
\[
\dot z=-\bigl((s+\delta)v+c\delta u\bigr)z-ca u^2+
\frac{cu^3}{m(m+u)}.
\]
As \(t\to\infty\), \(z(t)\to0\), \((s+\delta)v+c\delta u\to s>0\), and \(\dot u/u\to0\) by the first transformed equation. Every calculation below is along an arbitrary positive global solution.

**4. The doubly critical case.** Set \(m=m_c\), so \(a=0\). The quotient \(r=z/u^3\) satisfies the *exact* nonautonomous linear equation
\[
\dot r=-\left((s+\delta)v+c\delta u+3\frac{\dot u}{u}\right)r+
\frac{c}{m_c(m_c+u)}.
\]
The bracket tends to \(s>0\), and the forcing tends to \(c/m_c^2\); the elementary variation-of-constants formula therefore implies
\[
\frac{z(t)}{u(t)^3}\longrightarrow\frac{c}{s m_c^2}.
\]
Substituting this limit in the exact \(u\)-equation and expanding the rational denominator gives
\[
\dot u=-\alpha u^3+\beta u^4+o(u^4),\qquad
\alpha=\frac1{m_c^2},\quad
\beta=\frac1{m_c^3}+\frac{\delta c}{s m_c^2}.
\]
With \(Q=u^{-2}\), we have \(\dot Q=2\alpha-2\beta u+o(u)\). First \(Q(t)/t\to2\alpha\), hence \(u(t)\sim A t^{-1/2}\), where \(A=1/\sqrt{2\alpha}=m_c/\sqrt2\). Integration then gives
\[
Q(t)=2\alpha t-4\beta A\sqrt t+o(\sqrt t).
\]
Inverting this scalar expansion yields
\[
u(t)=A t^{-1/2}+\frac{\beta}{2\alpha^2}t^{-1}+o(t^{-1}),
\quad
\frac{\beta}{2\alpha^2}=\frac{m_c}{2}+
\frac{\delta^2 m_c^2}{2s(s+\delta)}.
\]
Finally \(z=O(u^3)=O(t^{-3/2})=o(t^{-1})\), and \(v=v_0+cu+z\). This proves both displayed two-term formulas. Notice that the second coefficient is independent of the initial state; such initial-state information can first enter lower-order terms.

**5. The supercritical Allee-strength case.** When \(m>m_c\), let \(\kappa=1/m_c-1/m>0\), so \(a=-\kappa\). The quotient \(r_2=z/u^2\) satisfies
\[
\dot r_2=-\left((s+\delta)v+c\delta u+2\frac{\dot u}{u}\right)r_2
+c\kappa+\frac{cu}{m(m+u)}.
\]
Variation of constants yields \(r_2(t)\to c\kappa/s\), and therefore \(\dot u=-\kappa u^2+o(u^2)\). Integrating \((u^{-1})'=\kappa+o(1)\) proves \(tu(t)\to1/\kappa\). Since \(v-v_0=cu+O(u^2)\), the companion limit for \(v\) follows. This completes the theorem.

## Verification
Run `python verify.py` from the extracted directory. It uses only the Python standard library, checks the weighted-log identity and both exact transformed differential equations with rational arithmetic over multiple parameter families, checks the critical coefficients algebraically, and supplies finite-time numerical illustrations. The observed run returned `VERIFY_OK: 1968 exact rational identities/coefficient checks; 6 numerical-limit sanity checks`. These computations do not prove the global or infinite-time statements, which follow from Steps 1–5.

For the exact parameter choice \(s=\delta=1\), \(h=e=1/2\), one has \(B=v_0=c=1/2\) and \(m_c=1\). The critical formulas reduce to
\[
u(t)=\frac1{\sqrt{2t}}+\frac{3}{4t}+o(t^{-1}),\qquad
v(t)=\frac12+\frac1{2\sqrt{2t}}+\frac{3}{8t}+o(t^{-1}).
\]
At \(m=2\), the faster laws give \(tu(t)\to2\) and \(t(v(t)-1/2)\to1\). At \(m=1/2\), the positive equilibrium is \((1/2,3/4)\); its global attraction was already proved in [1].

## Relationship to prior work
Xia et al. [1], equation (2.1), Theorems 2.2–2.7 and Figure 1, establish existence and local stability regimes for this identical continuous-time model and global attraction of the positive equilibrium for \(e=B\), \(m<m_c\). Their Theorem 2.3 and local center calculation (2.6)–(2.7) already contain a nonzero cubic term at \(e=B\), \(m=m_c\); thus the *qualitative possibility* of inverse-square-root local slowing is not claimed as independently new. The text does not state an all-positive-data global theorem at that equality, the exact weighted population product or the quartic/coupling correction and resulting universal second coefficient. Those additional implications require the separate global and asymptotic arguments given here.

Gao, Chen and Chen [2] study a *discrete-time* two-patch recurrence and its fold and flip bifurcations, not the continuous-time equality-case profile. Guiver, Packman and Townley [3] give general dispersal-growth criteria in a discrete-patch setting. Grumbach et al. [6] study Beverton–Holt and logistic two-patch models with linear exchange and the effects of connectivity on their asymptotic carrying populations, not Allee-suppressed nonlinear flow or its critical relaxation coefficients. Neither contains the present exact nonlinear per-capita product. Related published cubic-extinction results for modified Leslie–Gower and multiple-exposure epidemic systems [4,5] concern different vector fields and parameters; they motivate comparison of the normal-form *method* but neither state nor algebraically imply the two coefficients for [1].

## Limitations
The identity and asymptotics require the exact equality \(e=B\); arbitrary perturbations of this equality are not classified. The result is for the nonlinear-dispersal ODE, not its PDE or discrete-time analogues. Both initial densities must be strictly positive; \(u(0)=0\) is an invariant exceptional boundary and does not follow the displayed slow law. The nonvanishing second habitat \(v_0\) makes the result *patch-one extinction*, not extinction of the full metapopulation. The first inverse-square-root exponent is consistent with the published cubic normal form; the novel scope lies in the global conclusion, exact identity and higher asymptotic coefficient. Unindexed equivalent mathematics remains possible.

## References
[1] Y. Xia, L. Chen, V. Srivastava and R. D. Parshad, *Stability and bifurcation analysis of a two-patch model with Allee effect and dispersal*, arXiv:2310.10558v1 (first public 2023-10-16), Mathematical Biosciences and Engineering 20 (2023), 19781–19807, DOI:10.3934/mbe.2023876. Full open text: https://arxiv.org/html/2310.10558v1.

[2] M. Gao, L. Chen and F. Chen, *Dynamical analysis of a discrete two-patch model with the Allee effect and nonlinear dispersal*, Mathematical Biosciences and Engineering 21 (2024), 5499–5520, DOI:10.3934/mbe.2024242, https://www.aimspress.com/article/doi/10.3934/mbe.2024242.

[3] C. Guiver, D. Packman and S. Townley, *A necessary condition for dispersal driven growth of populations with discrete patch dynamics*, Journal of Theoretical Biology 424 (2017), 11–25, DOI:10.1016/j.jtbi.2017.03.030.

[4] *Universal cubic slowing at a doubly tangent predator-only threshold*, publicly available scientific finding (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-cubic-slowing-at-a-doubly-tangent-predator-only-thresh--574227374316.

[5] *Global attraction and two-term critical relaxation at the multiple-exposure disease-free degeneracy*, publicly available scientific finding (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-global-attraction-and-two-term-critical-relaxation-at-the-multip--45a437e4957f.

[6] C. Grumbach, F. N. Reurik, J. Segura, D. Franco and F. M. Hilker, *The effect of dispersal on asymptotic total population size in discrete- and continuous-time two-patch models*, Journal of Mathematical Biology 87 (2023), article 60, DOI:10.1007/s00285-023-01984-8, full open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10514157/.
