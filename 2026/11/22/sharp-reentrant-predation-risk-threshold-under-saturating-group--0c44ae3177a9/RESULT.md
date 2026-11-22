# Sharp reentrant predation-risk threshold under saturating group attraction

## Finding

For any exponent \(p>0\), basal group-encounter fraction \(0<a<1\), and capture-success attenuation \(b\geq0\), consider the dimensionless *per-individual predation hazard*
\[
R(x)=\frac{e^{-bx}(a+x^p)}{x(1+x^p)},\qquad x>0.
\]
The factor \((a+x^p)/(1+x^p)\) represents a bounded, increasing group-encounter rate; \(1/x\) is numerical dilution when one individual is taken per successful attack; and \(e^{-bx}\) is the probability of successful capture, conditional on attack. Positive constant multipliers do not affect the results.

Set
\[
a_c(p)=\left(\frac{p-1}{p+1}\right)^2\quad(p>1),\qquad
B=(p-1)-(p+1)a,
\]
and, when \(p>1\) and \(0<a<a_c(p)\), set
\[
z_\pm=\frac{B\pm\sqrt{B^2-4a}}2,\qquad
H(x)=\frac{-x^{2p}+Bx^p-a}{x(x^p+a)(1+x^p)},
\]
\[
b_c(p,a)=\max_{z_-^{1/p}<x<z_+^{1/p}}H(x).
\]
This maximum exists, is positive, is attained at *exactly one* point, and is specified by a strictly unimodal one-variable function. The complete classification on \(x>0\) is:

1. If \(p\leq1\) or \(a\geq a_c(p)\) (for \(p>1\)), then \(R\) is strictly decreasing for every \(b\geq0\).
2. If \(p>1\), \(0<a<a_c(p)\), and \(0\leq b<b_c(p,a)\), then \(R\) has exactly two critical points, a strict local minimum followed by a strict local maximum, and derivative signs \(-,+,-\). In particular, *increasing group size increases individual predation risk on exactly one bounded interval*, despite improving conditional attack survival and dilution.
3. If \(b=b_c(p,a)\), then \(R\) is strictly decreasing with precisely one stationary point (a horizontal inflection). If \(b>b_c(p,a)\), then \(R'(x)<0\) everywhere.

Both transitions are sharp, including equality. At \(p=2\), a reentrant interval is possible exactly for \(a<1/9\). Moreover, with \(t=(p-1)/(p+1)\), the attenuation boundary satisfies
\[
b_c(p,a)\sim\frac{p\,[a_c(p)-a]}{t^{1+1/p}(1+t)^2}
\quad\text{as }a\uparrow a_c(p),
\]
and
\[
b_c(p,a)\sim C_p a^{-1/p}\quad\text{as }a\downarrow0,
\quad C_p=\max_{u>0}\frac{(p-1)u^p-1}{u(1+u^p)}.
\]
The maximizer in the definition of \(C_p\) is unique: its \(p\)-th power is
\[
w_p=\frac{p^2-p+2+\sqrt{(p^2-p+2)^2+4(p-1)}}{2(p-1)}.
\]

## Assumptions and scope

The variable \(x>0\) is continuously rescaled group size (for example \(x=N/K\) for integer group size \(N\) and known scale \(K>0\)). The model assumes a single randomly selected victim per successful attack, a saturated Hill response of *group encounter rate* with baseline \(a\), and a separate exponential falloff in conditional capture success. Encounters are sufficiently rare that their rate times success and dilution yields individual hazard. The exponent \(p\) may be any real positive number. No hypothesis of ecological equilibrium, behavior optimization, or statistical fitting is made. Statements about derivative sign and exact critical-point counts apply to the continuous variable \(x\); integer samples need not contain every critical interval.

## Proof

**1. A quadratic controls every derivative sign.** Differentiation and cancellation give
\[
\frac{R'(x)}{R(x)}=H(x)-b,
\quad H(x)=\frac{G(x^p)}{x(x^p+a)(1+x^p)},
\quad G(z)=-z^2+Bz-a.
\]
All denominators are strictly positive on the stated domain. If \(p\leq1\), then \(B<0\), so \(G(z)<0\) for every \(z>0\). For \(p>1\), a positive value of \(G\) exists if and only if its maximum lies at a positive \(z\) and is positive: \(B>0\) and \(B^2>4a\). Writing \(u=\sqrt a\), the joint inequalities reduce to
\[
(p+1)u^2+2u-(p-1)<0,
\]
which, for \(u>0\), is equivalent to \(u<(p-1)/(p+1)\), or \(a<a_c(p)\). Otherwise \(H\leq0\), with equality at no more than one positive argument. Since \(b\geq0\), this gives strict functional decrease in the first regime even at its equality boundary.

**2. Exactly one positive hump.** In the remaining regime, \(G\) is positive exactly between its two distinct positive roots \(z_-<z_+\), and is negative outside. Put \(y=\log x\) and \(z=e^{py}\). On the open positive interval, factor \(G(z)=(z-z_-)(z_+-z)\) and write
\[
\log H(e^y)=\log(z-z_-)+\log(z_+-z)-y-\log(z+a)-\log(z+1).
\]
A *strict* second derivative computation yields
\[
\frac{d^2}{dy^2}\log H(e^y)
=-p^2z\left[
\frac{z_-}{(z-z_-)^2}+
\frac{z_+}{(z_+-z)^2}+
\frac{a}{(z+a)^2}+
\frac{1}{(z+1)^2}\right]<0.
\]
The logarithm tends to negative infinity at each endpoint, because \(H\) tends to zero there. Thus it has exactly one interior maximizer and increases strictly before, decreases strictly after that point. This proves the existence and uniqueness defining \(b_c\), without numerical root assumptions.

**3. Complete phase diagram.** The equation \(R'=0\) is \(H=b\). On the positive hump, any horizontal level \(0<b<b_c\) cuts \(H\) exactly twice. Outside that hump \(H<0\). For \(b=0\), the two endpoints of the positive hump are the only stationary points. In either case the derivative signs are \(-,+,-\), giving the stated strict minimum and maximum. For \(b=b_c\), the unique contact with the positive hump is tangent and the derivative is strictly negative elsewhere; strict log-concavity shows a genuine quadratic zero of \(H-b_c\), so the corresponding critical point of \(R\) is a stationary inflection. For \(b>b_c\) there are no critical points. The first regime may have an isolated zero derivative at \(b=0,a=a_c\), but remains strictly decreasing.

**4. Two boundary asymptotics.** As \(a\uparrow a_c(p)\), both roots of \(G\) converge to \(t=(p-1)/(p+1)\). Write \(\delta=a_c(p)-a\). The maximum of \(G\) is \(p\delta+O(\delta^2)\): this follows by evaluating its vertex \(B/2\) and differentiating \(B^2/4-a\) at the critical \(a\). Uniformly between the coalescing roots, the positive denominator in \(H\) converges to \(t^{1+1/p}(1+t)^2\). This gives the first asymptotic equivalence.

For the second, put \(x=a^{1/p}u\), with \(p>1\) fixed. Uniformly for \(u\) in compact subsets of \((0,\infty)\),
\[
a^{1/p}H(a^{1/p}u)\longrightarrow
F_p(u)=\frac{(p-1)u^p-1}{u(1+u^p)}.
\]
A positive value requires \(u>(p-1)^{-1/p}+o(1)\). Also, whenever \(H>0\), the exact inequality \(a^{1/p}H(a^{1/p}u)\leq(p-1)/u\) rules out escaping maximizers at infinity. Consequently the maxima converge to \(\max F_p\). Differentiating \(F_p\), and substituting \(w=u^p\), shows its stationary equation is
\[
(p-1)w^2-(p^2-p+2)w-1=0.
\]
It has one positive root, displayed above, and produces the unique positive maximum \(C_p\).

## Verification

Run \(\texttt{python3 CHECK.py}\) with Python 3.9 or newer. It uses only standard-library facilities, checks the logarithmic-derivative identity with exact rational arithmetic on a grid, tests the discriminant inequalities, exercises the strictly negative log-curvature formula, checks the two continuous extrema for \(p=2,a=1/25,b=2/5\), and compares two asymptotic laws at shrinking parameters. The reproducibility checker reports 15,159 passed diagnostic assertions in its packaged version; exact identities and limiting assertions are proved above independently of finite tests.

For the illustrative parameters \(p=2,a=1/25,b=2/5\), the computed attenuation boundary is \(b_c\approx0.830314348690\), while the two stationary group-size coordinates are approximately \(0.249262946051\) and \(0.627099131723\). The hazard increases between those coordinates, even though both dilution and the conditional capture-success term decrease with group size. This numerical example is illustrative, not a replacement for the proof.

## Relationship to prior work

Turner and Pitcher (1986) formalized combined attack avoidance and numerical dilution. Wrona and Dixon (1991) empirically separated predator encounter and dilution effects; the accessible abstract documents their net risk reduction for the studied system. Ale and Brown (2007) analyzed coupled attraction, dilution, and endogenously chosen vigilance under a power-law encounter factor, rather than the bounded Hill law with exogenous exponential attack-success attenuation used here. Cresswell and Quinn (2011), first public on 18 January 2011, analyzed actual group-size relationships for attack frequency, capture success, and dilution. Their openly available full paper describes possible saturation of attack rate, and observed a quadratic (eventually decreasing) attack rate, but does not state or derive the sharp two-threshold Hill-family classification or its boundary asymptotics.

The present result does **not** claim originality for attack abatement, the general possibility that aggregation attracts predators, exponential decline in successful attacks, or elementary derivative calculus in isolation. Its claim is the global, all-parameter critical-point classification and its two sharp asymptotic transitions for this motivated three-factor family. A full-text historical search of every older attack-abatement paper was not achieved; in particular, Wrona and Dixon (1991) and Turner and Pitcher (1986) were available as publisher abstracts rather than full articles, leaving residual priority risk.

## Limitations

This is a deterministic instantaneous individual-hazard model. Positive group-level encounter rate saturates, not predator intake as a function of prey density. The result applies to group sizes represented by a positive continuous variable and does not say that any specific integer group-size sample will display a reversal. It makes no claim that actual predator success decreases exponentially, that prey are equally targetable, or that multiple kills per encounter can be neglected in a given species. No field data, parameter estimates, optimal behavioral strategy, population dynamics, or independent historical audit are supplied. If a source uses more general response functions, the one-window bound need not hold.

## References

- Turner, G. F., and T. J. Pitcher (1986). Attack abatement: A model for group protection by combined avoidance and dilution. *American Naturalist* 128, 228–240. DOI: 10.1086/284556. https://doi.org/10.1086/284556
- Wrona, F. J., and R. W. Jamieson Dixon (1991). Group size and predation risk: A field analysis of encounter and dilution effects. *American Naturalist* 137, 186–201. DOI: 10.1086/285153. https://doi.org/10.1086/285153
- Ale, S. B., and J. S. Brown (2007). The contingencies of group size and vigilance. *Evolutionary Ecology Research* 9, 1263–1276. https://www.academia.edu/76930012/The_contingencies_of_group_size_and_vigilance
- Cresswell, W., and J. L. Quinn (2011). Predicting the optimal prey group size from predator hunting behaviour. *Journal of Animal Ecology* 80, 310–319. First public 18 January 2011. DOI: 10.1111/j.1365-2656.2010.01775.x. https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2656.2010.01775.x
