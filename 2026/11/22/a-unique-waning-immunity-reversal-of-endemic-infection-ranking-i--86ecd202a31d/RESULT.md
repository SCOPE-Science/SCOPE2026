# A unique waning-immunity reversal of endemic infection ranking in two cross-contact groups

## Finding

Two populations that transmit infection **only to one another** can reverse their ranking of endemic infected fractions when a *single shared rate of immunity loss* changes. Each population's infected fraction nevertheless increases strictly with that rate. The reversal occurs at most once, and its presence, direction, and location have exact necessary-and-sufficient algebraic conditions.

For positive \(a,b,g,h\) satisfying \(ab>gh\), put
\[
A=ah-bg,\qquad B=ab(h-g)+gh(a-b).
\]
Then, as the common rate \(\delta>0\) varies,
\[
\operatorname{sgn}(y_1^*(\delta)-y_2^*(\delta))=\operatorname{sgn}(A\delta+B).
\]
A strict change in the ranking at a positive rate occurs **if and only if** \(AB<0\), at the unique rate \(\delta_*=-B/A\). If \(A=B=0\), the infected fractions coincide for every positive rate. Otherwise, if \(AB\ge0\) or one of \(A,B\) is zero, there is no strict reversal on the positive half-line.

## Assumptions and scope

Let \(x_i(t),y_i(t),z_i(t)\) be the susceptible, infected and recovered fractions of group \(i\in\{1,2\}\), so \(x_i+y_i+z_i=1\). The total group fractions are normalized separately, with no demography or physical migration. Rates \(a,b,g,h,\delta\) are finite and strictly positive, and the sole infection contacts are across groups:
\[
\begin{aligned}
\dot y_1&=a y_2(1-y_1-z_1)-g y_1,&\dot z_1&=g y_1-\delta z_1,\\
\dot y_2&=b y_1(1-y_2-z_2)-h y_2,&\dot z_2&=h y_2-\delta z_2.
\end{aligned}
\]
This is the two-node irreducible, zero-diagonal specialization of the heterogeneous deterministic network SIRS model in Gatti--Como [1]. Positive endemic equilibrium means all six compartment fractions are strictly positive. The reproduction number is \(\mathcal R_0=\sqrt{ab/(gh)}\). Here \(\delta\) is varied with all other rates fixed; the statement concerns **equilibrium prevalence**, not incidence, time-dependent peak ordering, observed burden, or finite stochastic outbreaks.

## Proof

At any positive steady state, \(z_1=g y_1/\delta\), \(z_2=h y_2/\delta\). Set \(\alpha=1+g/\delta\), \(\eta=1+h/\delta\) and \(U=1/y_1\), \(V=1/y_2\). Dividing the two infection-balance equations by the positive products \(a y_1 y_2\) and \(b y_1 y_2\), respectively, gives the *linear* system
\[
U-\frac ga V=\alpha,\qquad V-\frac hb U=\eta.
\]
Its determinant is \(1-gh/(ab)\). When \(ab\le gh\), any proposed positive \(U,V\) contradicts these equations: at equality they are inconsistent since the right-hand sides are positive, and below equality the unique algebraic solution has both reciprocals negative. When \(ab>gh\), there is exactly one positive reciprocal solution,
\[
U=\frac{ab\alpha+bg\eta}{ab-gh},\qquad
V=\frac{ab\eta+ah\alpha}{ab-gh}.
\]
Taking reciprocals proves the claimed formulas
\[
y_1^*(\delta)=\frac{\delta(ab-gh)}{b[\delta(a+g)+g(a+h)]},\qquad
y_2^*(\delta)=\frac{\delta(ab-gh)}{a[\delta(b+h)+h(b+g)]}.
\]
The corresponding susceptible fractions are \(x_1=g y_1/(a y_2)>0\) and \(x_2=h y_2/(b y_1)>0\) by equilibrium balance, and recovered fractions are \(z_i=\gamma_i y_i/\delta>0\); the equations \(x_i=1-y_i-z_i\) then ensure all fractions lie in \((0,1)\). Thus the positive algebraic solution is physically admissible and unique. Its local asymptotic stability follows from Theorem 3 of [1], whose hypotheses (irreducible nonnegative contact matrix, positive rates, reproduction number above one) hold here. This is *not* a claim of global attraction.

Because both denominators are strictly positive for every \(\delta>0\), subtracting the formulas shows
\[
\begin{aligned}
\operatorname{sgn}(y_1^*-y_2^*)&=\operatorname{sgn}\{a[\delta(b+h)+h(b+g)]-b[\delta(a+g)+g(a+h)]\}\\
&=\operatorname{sgn}\{(ah-bg)\delta+ab(h-g)+gh(a-b)\}.
\end{aligned}
\]
The affine expression has exactly one positive, sign-changing zero if and only if its slope and intercept have opposite strict signs. If both vanish, all positive rates give equality; if only one vanishes, there is no positive strict sign change. Finally, each infected fraction has the form \(C\delta/(D\delta+E)\) with \(C,D,E>0\), hence derivative \(CE/(D\delta+E)^2>0\).

When \(a=b\), the ranking numerator reduces to \(a(h-g)(\delta+a)\). When \(g=h\), it reduces to \(g(a-b)(\delta+g)\). Therefore heterogeneity in *both* the directional transmission and recovery parameters is necessary for strict reversal.

For the exact witness \((a,b,g,h)=(2,5,1,2)\), \(ab-gh=8\) and
\[
y_1^*(\delta)=\frac{8\delta}{15\delta+20},\qquad
 y_2^*(\delta)=\frac{4\delta}{7\delta+12};\qquad A=-1,\quad B=4.
\]
At \(\delta=1\), \((y_1^*,y_2^*)=(8/35,4/19)\), so group 1 is higher. At \(\delta=4\), both are \(2/5\). At \(\delta=10\), they are \((8/17,20/41)\), so group 2 is higher. The source's reproduction threshold stays \(\sqrt5\) throughout.

## Verification

`CHECK.py` uses symbolic polynomial identities to reconstruct the unique positive endemic fractions and the ranking numerator, checks the exact witness at three immunity-loss rates, and tests equilibrium balance and positivity over 36 additional rational parameter selections. Run with `python CHECK.py` using Python 3 and SymPy. The analytic argument above, not finite testing, proves the universal statements.

## Relationship to prior work

Gatti and Como [1] establish existence, uniqueness, local stability, and componentwise monotonicity of the endemic equilibrium under general irreducible interactions. Their explicit Example 1 assumes out-regular contact and homogeneous recovery and immunity-loss rates, resulting in equal endemic fractions. They do not give the two-cross-contact-group closed-form threshold or a classification of *relative group ranking* under a common changing rate. The local stability used above is expressly inherited from [1]; the general monotonicity is also known from [1].

Saha, Das, and Samanta [2] study a different two-patch SIRS model with physical movement, demographic inflows and locally generated infection; it does not have the cross-only contact structure used here. El Khalifi and Britton [3] analyze alternative *within-individual* immunity-waning laws in homogeneous SIRS models, not cross-group ranking. Earlier multigroup SIRS stability work [4] and heterogeneous virus spreading models [5] establish broad persistence/stability properties; their accessible abstracts or closely related expositions do not determine this exact ranking boundary.

The new content is the sharp all-positive-parameter sign classification, its structural heterogeneity obstructions and an admissible strict-reversal witness. A literature search is not a proof of historical priority; independent evaluation of broad multigroup SIRS literature remains appropriate.

## Limitations

This is a deterministic, cross-infection-only, two-group theorem with a uniform immunity-loss rate; adding within-group transmission, changing group sizes, demographics, nonexponential immunity or stochastic processes can change the ranking boundary. The result does not establish global convergence of trajectories, forecast real epidemic prevalence or identify optimal interventions. The striking comparison is *relative prevalence*, even though each group increases individually. No independent validation has been performed.

## References

[1] G. Gatti and G. Como, *On the dynamic behavior of the network SIRS epidemic model*, arXiv:2604.21065, first public version 2026-04-22. https://arxiv.org/abs/2604.21065

[2] S. Saha, M. Das and G. P. Samanta, *Analysis of an SIRS Model in Two-Patch Environment in Presence of Optimal Dispersal Strategy*, Axioms 13(2):94 (2024). https://doi.org/10.3390/axioms13020094

[3] M. El Khalifi and T. Britton, *Extending susceptible-infectious-recovered-susceptible epidemics to allow for gradual waning of immunity*, Journal of the Royal Society Interface (2023). https://doi.org/10.1098/rsif.2023.0042

[4] Y. Muroya, Y. Enatsu and T. Kuniya, *Global stability for a multi-group SIRS epidemic model with varying population sizes*, Nonlinear Analysis: Real World Applications 14:1693--1704 (2013). https://doi.org/10.1016/j.nonrwa.2012.11.005

[5] L. Yang, M. Draief and X. Yang, *Heterogeneous virus propagation in networks: a theoretical study*, Mathematical Methods in the Applied Sciences 40:1396--1413 (2017). https://doi.org/10.1002/mma.4061
