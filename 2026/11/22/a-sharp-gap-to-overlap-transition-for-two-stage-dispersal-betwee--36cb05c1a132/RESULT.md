# A sharp gap-to-overlap transition for two-stage dispersal between temporary habitats

## Finding
Consider a source habitat active over \([0,L]\) and a destination habitat active over \([d,d+L]\), where \(L>0\) is fixed and the destination start \(d\in\mathbb R\) may be chosen freely. One propagule departs at a uniformly distributed time \(U\in[0,L]\), crosses two independent exponential transport stages of common rate \(\lambda>0\), and establishes if and only if arrival occurs while the destination is active. Let \(P_{\lambda,L}(d)=\Pr\{d\le U+E_1+E_2\le d+L\}\), where \(E_1,E_2\) are independent \(\mathrm{Exp}(\lambda)\).

There is exactly one global maximizing destination start \(d_*(L)>0\). Write \(x=\lambda L\), \(z_*(x)=\lambda d_*(L)\), and let \(x_c=1.256431208626169\ldots\) be the unique positive solution of \(e^{x_c}=1+2x_c\). Then:

1. **Separated windows:** if \(0<x<x_c\), the optimal destination begins strictly *after* the source closes, and
   \[z_*(x)=x\coth(x/2)-1>x.\]
2. **Just touching:** if \(x=x_c\), then \(z_*(x)=x\).
3. **Overlapping windows:** if \(x>x_c\), then \(0<z_*(x)<x\), characterized as the unique root in \((0,x)\) of
   \[1-(1+z+x)e^{-(z+x)}=2\bigl[1-(1+z)e^{-z}\bigr].\]

The function \(z_*(x)\) is continuous and strictly increasing in \(x>0\), and for every finite positive \(x\) obeys the sharp limits
\[1<z_*(x)<m=1.678346990016660\ldots,\qquad e^m=2(1+m).\]
In particular, shortening the habitats' active windows eventually makes a *strict dry-period gap* optimal, rather than synchrony or overlap. If \(P_x^{\rm sync}=P_{1,x}(0)\) denotes the probability with simultaneous openings, then
\[\frac{\max_d P_{1,x}(d)}{P_x^{\rm sync}}\sim\frac{6}{e x}\quad(x\downarrow0),\]
so the relative advantage of phase staggering is unbounded as both active windows shrink. For comparison, with only **one** exponential transport stage of rate \(\lambda\), the unique optimum always overlaps:
\[\lambda d_*^{(1)}(L)=\log(2-e^{-x})<x.\]
Thus two sequential transport stages are the smallest Erlang-stage count in this family capable of producing a positive optimal gap.

## Assumptions and scope
All statements quantify over every \(\lambda,L>0\) and all real \(d\), with normalized equal active-window lengths \(L\). The departure time is independent uniform conditional on a source-active emission; successful transit means neither death nor time-dependent travel rerouting. Both exponential stages have the **same rate** and are independent of departure time. Establishment is immediate on arrival and requires a wet destination at that instant. The outcome is **single-propagule arrival-window success probability**, not regional persistence, growth rate, or species richness. The source need not remain active after propagule departure. Negative \(d\) are allowed in the global optimization and are ruled out by the proof.

## Proof
Scale time by \(\lambda\), write \(x=\lambda L\) and \(z=\lambda d\), and put \(V=\lambda U\sim\mathrm{Uniform}[0,x]\). The two-stage travel time \(Y=\lambda(E_1+E_2)\) has density \(g(t)=te^{-t}\) and cumulative distribution
\[F(t)=1-(1+t)e^{-t}\quad(t\ge0),\qquad F(t)=0\quad(t<0).\]
The arrival time \(V+Y\) has continuous density
\[f_x(t)=\frac{F(t)-F(t-x)}{x},\]
and the success probability \(P_x(z)=\Pr\{z\le V+Y\le z+x\}\) is differentiable with
\[P_x'(z)=f_x(z+x)-f_x(z).\tag{1}\]
For \(z<0\), the derivative is nonnegative, and it is strictly positive whenever \(-x<z<0\); any \(z\le-x\) gives zero success. Thus no nonpositive \(z\) can maximize.

For \(0\le z\le x\), equation (1) has the sign of
\[H_x(z)=F(z+x)-2F(z).\tag{2}\]
Here \(H_x(0)=F(x)>0\). With \(g(t)=te^{-t}\),
\[H'_x(z)=g(z+x)-2g(z),\qquad \frac{g(z+x)}{g(z)}=e^{-x}\left(1+\frac{x}{z}\right)\quad(z>0).\]
The ratio strictly decreases in \(z\), from infinity to \(e^{-x}<2\). Hence \(H_x\) initially increases and subsequently strictly decreases, and may cross zero at most once for \(z>0\). At the right endpoint,
\[H_x(x)=F(2x)-2F(x)=-(1-e^{-x})\bigl[1-(1+2x)e^{-x}\bigr].\tag{3}\]
The positive root \(x_c\) of \(e^x=1+2x\) is unique: \(e^x-1-2x\) is strictly convex, begins at zero with negative derivative, then tends to infinity. By (3), \(H_x(x)\) is positive below \(x_c\), zero at \(x_c\), and negative above it. Consequently, for \(x>x_c\), (2) has exactly one zero in \((0,x)\), with a change from positive to negative; for \(x\le x_c\), (2) is positive before \(x\) except for its endpoint at equality.

For \(z\ge x\), define
\[A_x(z)=(e^x-1)(1+z)-xe^x.\]
Direct substitution gives
\[P'_x(z)=\frac{e^{-z}}{x}(1-e^{-x})\bigl[x-A_x(z)\bigr].\tag{4}\]
Since \(A_x\) increases strictly with \(z\), (4) changes sign exactly once across its unrestricted extension, at
\[z_{\rm tail}=\frac{x(e^x+1)}{e^x-1}-1=x\coth(x/2)-1.\]
This lies above, at, or below \(x\) according as \(e^x<1+2x\), \(e^x=1+2x\), or \(e^x>1+2x\). Combining (2)–(4) proves the unique *global* optimizer and all three regimes: the probability rises up to the identified point and falls after it, and tends to zero as \(z\to\infty\).

On \((0,x_c)\), differentiation yields
\[\frac{d}{dx}\bigl(x\coth(x/2)-1\bigr)=\frac{\sinh x-x}{2\sinh^2(x/2)}>0.\]
On \((x_c,\infty)\), the optimizer is the unique descending zero of \(H_x(z)\), so \(\partial_zH_x(z_*)<0\), whereas \(\partial_xH_x(z_*)=g(z_*+x)>0\). Implicit differentiation gives \(z_*'(x)>0\). The two formulas agree at \(x_c\), proving continuity. As \(x\downarrow0\), the tail expression tends to 1. As \(x\to\infty\), the interior equation (2) tends to \(1-2F(z)=0\) on each bounded \(z\)-interval. The unique root approaches the median \(m>0\) of the two-stage travel distribution, characterized by \(F(m)=1/2\), equivalently \(e^m=2(1+m)\). Strict monotonicity yields \(1<z_*(x)<m\) for all finite \(x>0\), with both endpoint bounds sharp.

For the small-window comparison, put \(G(t)=t-2+(t+2)e^{-t}\) for \(t\ge0\), and \(G(t)=0\) otherwise. As \(G'=F\),
\[P_x(z)=\frac{G(z+x)-2G(z)+G(z-x)}{x}.\tag{5}\]
At synchrony, \(P_x(0)=G(x)/x=x^2/6+O(x^3)\). At the optimizer, \(z_*(x)\to1\); the arrival density over a shrinking interval converges locally to \(g(1)=1/e\), so \(P_x(z_*(x))=x/e+o(x)\). Their ratio is \(6/(ex)(1+o(1))\).

For the one-stage comparison, replace \(F\) by \(F_1(t)=1-e^{-t}\) for \(t\ge0\). The derivative of the arrival-window probability is positive for \(z<0\), has sign \((2-e^{-x})e^{-z}-1\) for \(0\le z\le x\), and is negative for \(z\ge x\). Its sole maximum is \(z=\log(2-e^{-x})\). The strict inequality \(\log(2-e^{-x})<x\) follows from \(2<e^x+e^{-x}\) for \(x>0\).

## Verification
The accompanying standard-library `checker.py` computes both one- and two-stage optima, checks the derivative equations and signs against thousands of independent parameter samples, compares global success probabilities at randomized competitor phases, verifies numerical monotonicity and the limiting approximations, and prints representative optimal phases. Its tests are **supplementary finite checks**, not substitutes for the analytic quantifiers above. In dimensionless units, the critical duration is approximately \(1.256431208626170\), while the limiting optimal phase is approximately \(1.678346990016661\).

## Relationship to prior work
Moisset de Espanés and Ramos-Jiliberto (2024) investigate ecological metacommunities with asynchronous site activity via stochastic migration and local equilibria. Their movement events require simultaneously active sites; the result here instead models a propagule already in transit and counts later arrival at an active destination. Hockaday and colleagues (2024) experimentally investigate managed temporary-wetland hydroperiods and community recovery, motivating attention to opening and drying calendars without furnishing a transport-delay optimality theorem. Karnatak and Wollrab (2020) study probabilistic spatial connectivity with dynamic links, rather than the present continuous arrival-time window optimization. Classical exponential/Erlang distribution identities and convolution calculus are used, not claimed as new. In the inspected primary publications and searches for competing interval/window theorems, no statement directly implies the three-regime global optimizer and the singular synchronization-loss asymptotic under these assumptions; this is a bounded, provisional originality assessment, not a claim of exhaustive historical priority.

## Limitations
The source and destination have equal fixed wet durations, and the destination is freely schedulable; no season-end calendar constraint is imposed. Travel comprises exactly two independent identical-rate exponential stages. The model does not account for travel mortality, germination delay, species interactions, repeat dispersal, seasonal forcing, density dependence, or feedback between species and habitat. Multiple propagules with independent identical departures would have establishment probability \(1-(1-P_x(z))^N\) for fixed positive integer \(N\), so the phase optimum carries over, but dependence or nonidentical propagation can change it. The result is a theoretical benchmark, not a field-calibrated wetland management plan. Historical-priority risk persists for unindexed time-window/queueing formulations.

## References
1. P. Moisset de Espanés and R. Ramos-Jiliberto, “Both local stability and dispersal contribute to metacommunity sensitivity to asynchronous habitat availability,” *Scientific Reports* 14 (2024), article 6273. First public article date: 2024-03-15. https://doi.org/10.1038/s41598-024-56632-y
2. A. C. Hockaday, A. S. León, K. Patterson, and S. C. Pennings, “Freshwater wetlands for flood control: How manipulating the hydroperiod affects plant and invertebrate communities,” *PLOS ONE* 19 (2024), e0306578. Published 2024-07-03. https://doi.org/10.1371/journal.pone.0306578
3. R. Karnatak and S. Wollrab, “A probabilistic approach to dispersal in spatially explicit meta-populations,” *Scientific Reports* 10 (2020), article 22234. Published 2020-12-17. https://doi.org/10.1038/s41598-020-79162-9
