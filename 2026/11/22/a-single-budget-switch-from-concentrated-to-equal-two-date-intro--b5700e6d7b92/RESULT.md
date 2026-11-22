# A single budget switch from concentrated to equal two-date introductions under a two-founder quorum

## Finding

Let \(0<\ell<h\le1\) be two calibrated per-founder probabilities of surviving to a common census under unfavorable and favorable conditions. Let \(B>0\) be the total mean number of founders released at two prescribed dates. Suppose the two dates have a fair, exchangeable binary environment with discordance probability strictly greater than zero. Under conditionally independent founder survival and independent Poisson release counts, success is defined as at least two founders alive at the common census, pooled across release dates.

Write \(\alpha=(h+\ell)/2\), \(\beta=(h-\ell)/2\). There is a unique \(B_*\in(1/\alpha,1/\ell)\) solving

\[
\beta B_*\coth(\beta B_*/2)=1+\alpha B_*.
\]

The complete set of global maximizers for the expected number \(x\) released at the first date, with \(B-x\) at the second date, is

\[
\mathop{\mathrm{argmax}}_{0\le x\le B}P_B(x)=
\begin{cases}
\{0,B\},&0<B<B_*,\\
\{0,B/2,B\},&B=B_*,\\
\{B/2\},&B>B_*.
\end{cases}
\]

This is an abrupt optimizer transition, with no strictly unequal interior maximum. Its threshold depends on \(h,\ell\), but **not** on the strength of the environmental correlation as long as discordant conditions have positive probability. In the degenerate case of perfectly coincident environmental conditions, or \(h=\ell\), every allocation ties. Requiring at least **one**, rather than at least two, surviving founder instead makes equal splitting uniquely optimal whenever environmental discordance and survival contrast are positive.

## Assumptions and scope

A finite, common census occurs after both release dates. The environmental pair \((E_1,E_2)\) is exchangeable and takes values \(G,L\) with marginal probabilities \(1/2\). Parameterize its joint probabilities by \(\rho\in[-1,1)\):

\[
\Pr(G,G)=\Pr(L,L)=\frac{1+\rho}{4},\qquad
\Pr(G,L)=\Pr(L,G)=\frac{1-\rho}{4}.
\]

Thus \(\rho<1\) is precisely nonzero chance of discordance. A stationary symmetric two-state continuous-time Markov environment observed at a positive lag gives the example \(\rho=e^{-2\kappa\tau}\in(0,1)\), for switching rate \(\kappa>0\) and lag \(\tau>0\). The general result does not require the Markov assumption.

A designer selects \(x\in[0,B]\). Release counts at the first and second dates are independent Poisson random variables with means \(x\) and \(B-x\). Given the environmental pair, each released individual independently survives to the common census with probability \(h\) in state \(G\) or \(\ell\) in state \(L\). These probabilities already include any effects of the different elapsed times to the census; equal state-calibrated survival at both dates is an explicit modeling restriction. No reproduction or migration takes place before the census. Success means that the *pooled total* of surviving individuals is at least two; there is no separate per-date or per-habitat viability test. The budget \(B\) constrains *expected releases*, not the realized total and not the integer count of available animals.

The result is a one-census probability theorem about a two-founder survival proxy. It does not identify long-term stochastic establishment, mate availability, or ecological safety.

## Proof

**Conditional thinning and reduction.** Conditional on \((E_1,E_2)\), Poisson thinning and independence imply that the pooled surviving count is Poisson with mean \(x p(E_1)+(B-x)p(E_2)\), where \(p(G)=h\) and \(p(L)=\ell\). Define

\[
F(z)=\Pr\{\operatorname{Pois}(z)\ge2\}=1-(1+z)e^{-z},\quad
m=\alpha B,\quad t=\beta(2x-B),\quad T=\beta B.
\]

The possible values of \(t\) cover \([-T,T]\). Conditioning on all four environmental outcomes gives exactly

\[
P_B(x)=\frac{1+\rho}{4}\bigl[F(hB)+F(\ell B)\bigr]
+\frac{1-\rho}{4}\bigl[F(m+t)+F(m-t)\bigr].\tag{1}
\]

The first bracket is independent of \(x\), and the coefficient of the second is strictly positive. Therefore maximizing \(P_B\) is equivalent to maximizing the even function \(G_m(t)=F(m+t)+F(m-t)\) on \([-T,T]\), irrespective of \(\rho\).

**No unequal interior maximum.** Since \(F'(z)=ze^{-z}\), for \(t>0\),

\[
G_m'(t)=2e^{-m}\bigl(t\cosh t-m\sinh t\bigr)
=2e^{-m}\sinh t\left(\frac{t}{\tanh t}-m\right).\tag{2}
\]

The function \(R(t)=t/\tanh t\) increases strictly from \(1\) to infinity on \((0,\infty)\). Indeed \(R'(t)>0\) is equivalent to \(\sinh t\cosh t>t\), true by differentiation and strict positivity for \(t>0\). If \(m\le1\), derivative (2) is strictly positive. If \(m>1\), it is negative until the single positive root \(R(t)=m\) and strictly positive thereafter. Thus on \([0,T]\) the function either increases or decreases and then increases, and its global maximum can occur only at \(t=0\) or \(t=T\). In case of equality of these endpoint values there are no other maximizers because the intervening values are strictly smaller. Symmetry gives candidates \(x=0,B/2,B\).

**Exactly one global switch.** The exact endpoint difference is

\[
G_m(T)-G_m(0)=2e^{-m}(\cosh T-1)
\left[T\coth(T/2)-(1+m)\right].\tag{3}
\]

Set \(H(B)=\beta B\coth(\beta B/2)-1-\alpha B\). For \(u=\beta B/2>0\),

\[
H'(B)=\beta\left[\coth u-u\operatorname{csch}^{2}u\right]-\alpha.
\]

The bracket lies strictly between \(0\) and \(1\): positivity follows from \(\sinh u\cosh u>u\), and the upper bound follows from \((1-e^{-2u})/2<u\). Consequently \(H'(B)<\beta-\alpha=-\ell<0\). Moreover \(H(B)\to1\) as \(B\downarrow0\), whereas \(H(B)=-\ell B-1+o(1)\) as \(B\to\infty\). Therefore there is exactly one positive root, and (3) proves the asserted optimizer sets.

For the location bounds, the strict inequalities \(T\coth(T/2)>2\) and \(T\coth(T/2)<T+2\) imply \(H(1/\alpha)>0\) and \(H(1/\ell)<0\); strict monotonicity then gives \(1/\alpha<B_*<1/\ell\). At \(B=B_*\), equation (2) ensures strict inequality for every interior candidate besides the center and the two ends, completing the exact three-way tie statement.

**The one-founder contrast and degeneracies.** For a threshold of one, replace \(F\) with \(F_1(z)=1-e^{-z}\). In discordant environments, the allocation-sensitive term becomes \(F_1(m+t)+F_1(m-t)=2-2e^{-m}\cosh t\), strictly decreasing in \(|t|\). Thus \(x=B/2\) is unique if \(\rho<1\) and \(h>\ell\). If \(\rho=1\), the discordant term in (1) vanishes; if \(h=\ell\), then \(t=0\) for every allocation. All allocations then tie. These are the only degeneracies under the stated positive budget.

## Verification

The accompanying `verify.py` implements separate direct calculations using the four environmental states and the reduced formula, compares the predicted global optimizers against finite allocation grids across multiple parameters, checks the derivative factorization and monotonicity numerically, tests the one-founder contrast, and computes a high-precision critical budget. Execute `python3 verify.py` using only the Python standard library. It passes 44,948 finite assertions in the reference run. Finite checks do **not** establish the all-real theorem, which follows from the proof above.

For \(\ell=1/4\), \(h=3/4\), \(\rho=1/2\), the critical budget is

\[
B_*=2.09064648697929298018\ldots .
\]

At \(B=2\), the predicted concentrated and equal-split success probabilities are approximately \(0.266189305029988\) and \(0.265702258186770\), respectively. At \(B=4\), the corresponding probabilities are approximately \(0.532546422092830\) and \(0.547908354142163\). The sign change is verified with 60-digit decimal arithmetic.

## Relationship to prior work

Grevstad (1999) studies the competing influences of environmental stochasticity and Allee effects on release strategies, including the possibility of intermediate optimal release size. The present claim is specifically the *exact continuous two-date Poisson budget allocation*, with a *pooled threshold of two survivors*, an explicit unique \(\coth\)-root, and correlation-independent optimizer classification; these are not asserted to follow from Grevstad's available abstract. Its full article was not accessible for a conclusive priority determination.

Haccou and Iwasa (1996, section on invasion success, equations 36–43) analytically compare sequential and simultaneous invasions for success of *at least one independently establishing lineage*. Their Hölder argument does not imply the two-survivor pooled-quorum reversal: replacing the success event by \(\Pr\{N\ge2\}\) changes the curvature, and the preferred allocation actually reverses with \(B\). Shea and Possingham (2000) use stochastic dynamic programming to choose release types across distinct sites and states, with a different sigmoid success function. Schreiber and Lloyd-Smith (2009, Appendix E) establish a spatial-releases advantage via Muirhead inequalities for at least one successful lineage. Drolet and Locke (published online in 2015) use a two-stage stochastic population simulation to compare introduction number and size under Allee effects. These sources give strong motivation, but none of the materially inspected passages states or dominates the exact pooled two-date all-budget theorem. General rearrangement arguments and older unretrieved results remain potential historical-priority risks; no literature search proves novelty.

## Limitations

Only two release dates are allowed, with equal marginal environmental-state probabilities and equal conditional survival mapping at the two dates. Release totals are Poisson and controlled in expectation; survivors are conditionally independent. There is neither reproduction before the census nor a mechanistic Allee population process after it. Success is a two-survivor **proxy**, not long-term establishment. Positive environmental discordance is required; with perfectly correlated identical states, release timing is immaterial. The solution is not a recommendation for releasing nonnative species or modifying biological-control practice. No independent external validation or comprehensive historical-priority certification has been performed.

## References

1. F. S. Grevstad (1999), *Factors Influencing the Chance of Population Establishment: Implications for Release Strategies in Biocontrol*, *Ecological Applications* **9**, 1439–1447. First published November 1, 1999. https://doi.org/10.1890/1051-0761(1999)009[1439:FITCOP]2.0.CO;2
2. P. Haccou and Y. Iwasa (1996), *Establishment Probability in Fluctuating Environments: A Branching Process Model*, *Theoretical Population Biology* **50**, 254–280. https://doi.org/10.1006/tpbi.1996.0031
3. K. Shea and H. P. Possingham (2000), *Optimal release strategies for biological control agents: an application of stochastic dynamic programming to population management*, *Journal of Applied Ecology* **37**, 77–86. https://doi.org/10.1046/j.1365-2664.2000.00467.x
4. S. J. Schreiber and J. O. Lloyd-Smith (2009), *Invasion Dynamics in Spatially Heterogeneous Environments*, *The American Naturalist* **174**, 490–505. https://doi.org/10.1086/605405
5. D. Drolet and A. Locke (2016; online December 8, 2015), *Relative importance of propagule size and propagule number for establishment of non-indigenous species: a stochastic simulation study*, *Aquatic Invasions* **11**, 101–110. https://doi.org/10.3391/ai.2016.11.1.11
