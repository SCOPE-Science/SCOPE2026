# Sharp endemic bistability frontier in an SIS epidemic with prevalence-dependent logit incentives

## Finding

Consider a population in which cooperation suppresses SIS transmission and behavioral adjustment uses finite-rationality logit choice. Suppose the payoff advantage of **defection** is the positive, prevalence-amplified quantity \(A+B I\), independent of the opponent's action, with \(A,B>0\). This is a valid two-action payoff specialization of the SIS–logit dynamics in [1]. Put \(c=\sigma A>0\), \(d=\sigma B>0\), \(k=\gamma/\beta\in(0,1)\), and define
\[
\ell(z)=\frac{e^z}{1+e^z},\qquad g(I)=(1-I)\ell(c+dI),\qquad g_0=\ell(c).
\]
The disease-free equilibrium is a hyperbolic sink for \(k>g_0\), a hyperbolic saddle for \(k<g_0\), and nonhyperbolic at equality; local asymptotic stability at equality is not asserted.

**Complete endemic-equilibrium classification.** If \(d\leq1+e^c\), then there is one endemic equilibrium for \(0<k<g_0\), and none for \(k\geq g_0\). If \(d>1+e^c\), define the principal positive Lambert function \(W_0\) by \(W_0(s)e^{W_0(s)}=s\), and let
\[
 I_m=1-\frac{1+W_0(e^{c+d-1})}{d},\qquad
 g_m=\frac{W_0(e^{c+d-1})}{d}>g_0.
\]
In this case, there is one endemic equilibrium for \(0<k\leq g_0\), exactly **two distinct endemic equilibria** for \(g_0<k<g_m\), exactly one nonhyperbolic double endemic equilibrium for \(k=g_m\), and no endemic equilibrium for \(k>g_m\). Every endemic equilibrium on the decreasing branch \(I>I_m\) is a hyperbolic sink; every equilibrium on the increasing branch \(0<I<I_m\) is a hyperbolic saddle.

In particular, the following condition is **necessary and sufficient** for simultaneous local asymptotic stability of the disease-free state and a positive endemic state separated by an endemic saddle:
\[
\boxed{d>1+e^c,\qquad \ell(c)<k<\frac{W_0(e^{c+d-1})}{d}.}
\]
This gives a sharp backward-endemic bistability wedge, despite a locally subcritical infection reproduction factor at disease freedom. The theorem does not equate local bistability with a claim about every global trajectory.

A rational-parameter witness is \(\sigma=A=\beta=1\), \(B=20\), \(\gamma=4/5\). It has a stable disease-free equilibrium \((x,I)=(1/(1+e),0)\), a lower endemic saddle at \(I\approx0.026390022712\), and an upper endemic sink at \(I\approx0.193911638779\). These three equilibria are exhaustive. In this witness the sufficient finite-rationality endemic-existence threshold of [1, Lemma 3] is \(\sigma^{\mathrm{TH}}=\log4>1=\sigma\), and that lemma's uniqueness condition (16) is violated because the relevant payoff-difference terms are \(-\beta B\) and \(-\gamma B\); thus the source's sufficient theorem does not imply this coexistence.

## Assumptions and scope

The physical state is \((x,I)\in[0,1]^2\), where \(x\) is the fraction cooperating and \(I\) is the infected fraction. Parameters satisfy \(\sigma,A,B,\beta,\gamma>0\) and \(0<\gamma<\beta\). The coupled differential equations are
\[
\dot x=\frac{1}{1+e^{\sigma(A+BI)}}-x,\qquad
\dot I=\beta(1-x)I(1-I)-\gamma I.
\]
They arise from the source's prevalence-interpolated payoff matrices by taking the cooperating row identically zero and the defecting row equal to \((A,A)\) in the disease-free payoff matrix and \((A+B,A+B)\) in the infected-environment payoff matrix. In particular the source assumption that defection strictly dominates cooperation at zero prevalence is respected. This deliberately models an *anti-protective* (not a protective) payoff response to increasing prevalence.

The square is forward invariant: the behavioral field points inward at \(x=0\) and \(x=1\); the infection field vanishes at \(I=0\) and is strictly negative at \(I=1\). Since the logit response is strictly inside \((0,1)\), stationary states can lie on the physical boundary only at \(I=0\). Only finite, positive rationality is considered; stochastic outbreaks, network heterogeneity, and arbitrary action-dependent payoffs are not covered.

## Proof

**1. Reduction to one function.** Write \(h(I)=1/(1+e^{c+dI})\). At an equilibrium with \(I>0\), the first equation requires \(x=h(I)\), and the second requires \(\beta[1-h(I)](1-I)=\gamma\). As \(1-h(I)=\ell(c+dI)\), endemic equilibria correspond bijectively to roots of \(g(I)=k\) with \(0<I<1\). There is exactly one disease-free equilibrium \((h(0),0)\).

**2. Shape and critical level.** Direct differentiation gives
\[
\frac{g'(I)}{g(I)}=-\frac1{1-I}+\frac{d}{1+e^{c+dI}},
\qquad
\frac{d}{dI}\left[\frac{g'(I)}{g(I)}\right]
=-\frac1{(1-I)^2}-\frac{d^2e^{c+dI}}{(1+e^{c+dI})^2}<0.
\]
Hence the logarithmic derivative decreases strictly from \(-1+d/(1+e^c)\) to \(-\infty\) as \(I\uparrow1\). When \(d\leq1+e^c\), \(g\) decreases strictly on \((0,1)\), from \(g_0\) to zero. When \(d>1+e^c\), it has exactly one strict interior maximum \(I_m\), rising from \(g_0\) and then decreasing to zero. Thus root-count classification follows immediately from the intermediate-value theorem and strict monotonicity on either side.

At the maximum, \(1+e^{c+dI_m}=d(1-I_m)\). Set \(z=d(1-I_m)-1=e^{c+dI_m}>0\). Replacing \(I_m\) gives \(ze^z=e^{c+d-1}\), hence \(z=W_0(e^{c+d-1})\). Moreover
\[
g(I_m)=\frac{1+z}{d}\cdot\frac{z}{1+z}=\frac zd,
\]
proving the announced formulas. The maximum is nondegenerate because the logarithmic derivative is strictly decreasing there: \(g''(I_m)<0\). Consequently the equality \(k=g_m\) is a genuine simple fold as \(k\) varies, with one double positive root.

**3. Exact local stability.** At an endemic equilibrium \((x,I)=(h(I),I)\), the Jacobian is
\[
J=\begin{pmatrix}
 -1&-d\,x(1-x)\\
 -\beta I(1-I)&-\beta I(1-x)
\end{pmatrix},
\quad\operatorname{tr}J=-1-\beta I(1-x)<0,\quad
\det J=-\beta I g'(I).
\]
The last identity follows by expanding the determinant and using \(g'(I)=(1-x)[-1+d x(1-I)]\). Thus a strictly decreasing-branch root has positive determinant and negative trace, so both eigenvalues have negative real part; an increasing-branch root has negative determinant, so is a hyperbolic saddle. At \(I_m\) the determinant vanishes, with the other eigenvalue negative. At disease freedom, the Jacobian is triangular with eigenvalues \(-1\) and \(\beta(g_0-k)\). This proves the stability statements and the necessary-and-sufficient coexistence wedge.

**4. Completely certified finite witness.** Take \(c=1\), \(d=20\), \(k=4/5\). Since \(e<4\), \(g(0)=e/(1+e)<4/5\). At \(I=1/10\),
\[
g(1/10)=\frac9{10}\frac{e^3}{1+e^3}>\frac45,
\]
where the strict inequality is equivalent to \(e^3>8\), true since \(e>2\). Finally \(g(1)=0<4/5\). By the strict-unimodality proof, exactly one root lies on each side of the unique peak: no other positive roots are possible. Its smaller root is a saddle, its larger root a sink, and the unique disease-free state is also a sink. The numerical values stated above locate rather than establish these roots. \(\square\)

## Verification

The dependency-free `verify.py` tests the Lambert maximum identity, counts the two endemic roots by bisection in 175 additional strict-wedge parameter triples, checks the exact Jacobian determinant identity and both stability signs, and reproduces the reported numerical witness. Execute `python3 verify.py` using standard Python 3. The certified rational witness rests on the elementary inequalities \(2<e<4\), not numerical root finding. Finite tests do not prove the continuum theorem: the analytic monotonicity and Jacobian arguments above do that.

## Relationship to prior work

Maitra, Paarporn and Eksin [1, equations (1)–(5), Lemma 3 and its condition (16), and local stability theorems] introduce the exact SIS–logit game and prove equilibrium facts subject to additional hypotheses. Their sufficient monotonicity condition (16) is violated by the prevalence-amplified payoff difference treated here, and their paper does not supply a necessary-and-sufficient two-endemic fold frontier for this subfamily. The contribution here is **not** the game, logit response, disease-free linearization, or a general observation that behavioral epidemics can be bistable; it is the exact parameter-space classification, fold level and strict three-equilibrium construction for this specific admissible payoff family.

A separate result [2] supplies a sharp universal sufficient exclusion of periodic cycles for the same SIS–logit model; nothing about the absence of cycles is presented here as new. Other SIS/game formulations [3, 6] and feedback-evolving population games [4] use different response rules or payoff/environment dynamics and do not directly yield this explicit Lambert-frontier statement. The related 2026 general feedback-game analysis [5] was accessible only through its abstract, so potential broader implications from that work have not been excluded by a full-text comparison.

## Limitations

The source's strongest simplifying assumption here is that the defection advantage increases with prevalence, while the benefits of distancing are not modeled as increasing with infections. For protective payoff feedback \(B<0\), the asserted bistability wedge does not apply. The theorem addresses only equilibrium counts, local stability and a local fold, not global basin geometry or stochastic persistence. It does not cover action-dependent payoff differences, arbitrarily many population groups, delayed feedback or measured disease/behavior data. Historical-priority comparison was limited by inaccessible text of [5] and by possible unindexed equivalent formulations; no independent validation has occurred.

## References

[1] U. Maitra, K. Paarporn and C. Eksin, *SIS Epidemic Containment under Game-theoretic Rational Learning*, arXiv:2610.03173v1, first publicly submitted 2026-10-02. https://arxiv.org/abs/2610.03173 ; full PDF https://arxiv.org/pdf/2610.03173.

[2] *A sharp universal logit-slope barrier for epidemic oscillations, with periodic SIS witnesses* (2026-10-18). https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-sharp-universal-logit-slope-barrier-for-epidemic-oscillations--20f9724cad5f/RESULT.md.

[3] K. Paarporn and C. Eksin, *SIS epidemics coupled with evolutionary social distancing dynamics* (replicator behavioral response), 2023, https://arxiv.org/search/?query=SIS+epidemics+coupled+with+evolutionary+social+distancing+dynamics&searchtype=all .

[4] S. Park et al., *Epidemic Population Games And Perturbed Best Response Dynamics*, arXiv:2401.15475, 2024. https://arxiv.org/abs/2401.15475.

[5] R. Gavin, K. Paarporn and M. Cao, *Learning to Avoid Tragedies: Boundedly Rational Agents in Feedback-Evolving Games*, IEEE Transactions on Automatic Control, first online 2026-04-29, doi:10.1109/TAC.2026.3685548. https://doi.org/10.1109/TAC.2026.3685548.

[6] M. Ordorica Arango, A. Bizyaeva, S. A. Levin and N. E. Leonard, *Opinion-driven risk perception and reaction in SIS epidemics*, arXiv:2410.12993, first submitted 2024-10-16. https://arxiv.org/abs/2410.12993. Their bistability is in an opinion-mediated, rather than logit-payoff, epidemic system.
