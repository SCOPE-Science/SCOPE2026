# A sharp simultaneous last-isolation law for bipartite edge clocks

## Finding

Give every edge of the complete bipartite graph with labeled parts of sizes \(a,b\ge2\) an independent rate-one exponential clock, and reveal an edge at its clock time. Write \(T_A\) and \(T_B\) for the last times at which an initially isolated vertex in the respective parts obtains its first edge. The event \(T_A=T_B\) means one edge simultaneously eliminates the last isolated vertex on each side.

For every \(a,b\ge2\), its probability has the exact finite form
\[
\Pr(T_A=T_B)=ab\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}
\frac{(-1)^{i+j}\binom{a-1}{i}\binom{b-1}{j}}
{a+b-1+i(b-1)+j(a-1)-ij}.
\]

Let \(a=a_n,b=b_n\) be positive integers with \(a+b=2n\) and
\[
\frac{(a-b)\log n}{n}\longrightarrow\kappa\in\mathbb R.
\]
Then the *rare synchronized completion law* is
\[
\boxed{\lim_{n\to\infty}n\Pr(T_A=T_B)
=\frac{1}{4\cosh^2(\kappa/2)}.}
\]
Moreover, conditional on \(T_A=T_B\), if \(Z_n=nT_A-\log n\) and \(\lambda_\kappa=2\cosh(\kappa/2)\), then
\[
\lambda_\kappa e^{-Z_n}\xrightarrow{d}\operatorname{Gamma}(2,1),
\]
with the shape-two, rate-one gamma convention. This differs from the ordinary Gumbel completion-time law.

For comparison, the entire joint completion-time limit holds:
\[
(nT_A-\log n,\ nT_B-\log n)
\xrightarrow{d}(G_1+\kappa/2,G_2-\kappa/2),
\]
where \(G_1,G_2\) are independent standard Gumbel variables. In particular,
\[
\Pr(T_A>T_B)\longrightarrow \frac{1}{1+e^{-\kappa}},
\qquad \Pr(T_B>T_A)\longrightarrow\frac{1}{1+e^{\kappa}}.
\]
Thus the competition window is a part-size imbalance of order \(n/\log n\), and synchronized finishes persist at the smaller, explicit scale \(1/n\).

## Assumptions and scope

All clocks are independent \(\operatorname{Exp}(1)\) variables \(E_{ij}\) on the \(ab\) distinct potential edges; the process adds each edge once, and is therefore not the repeated-draw coupon collector. Define the first appearance times \(R_i=\min_{1\le j\le b}E_{ij}\) and \(C_j=\min_{1\le i\le a}E_{ij}\); then \(T_A=\max_iR_i\) and \(T_B=\max_jC_j\). The finite exact formula needs only \(a,b\ge2\). The limiting assertions require \(a+b=2n\to\infty\) and a finite real imbalance limit \(\kappa\); they do not claim uniformity over diverging imbalance parameters.

For \(u,v\ge0\), put \(X_A(u)=\#\{i:R_i>u\}\), \(X_B(v)=\#\{j:C_j>v\}\). For any nonnegative integers \(r,s\), with \(r\le a,s\le b\), the exact mixed falling-factorial moment identity is
\[
\mathbb E[(X_A(u))_{\underline r}(X_B(v))_{\underline s}]
=(a)_{\underline r}(b)_{\underline s}
\exp[-rbu-sav+rs\min(u,v)].
\]
Consequently, the exact joint distribution function is
\[
\Pr(T_A\le u,T_B\le v)
=\sum_{r=0}^a\sum_{s=0}^b(-1)^{r+s}\binom ar\binom bs
\exp[-rbu-sav+rs\min(u,v)].
\]
These formulas specify the joint finite law without any independence approximation.

## Proof

**Mixed moments and the joint limit.** Select \(r\) distinct rows and \(s\) distinct columns. For all those rows to have no incident edge by \(u\) and all those columns to have none by \(v\), the \(rb\) row-incident and \(sa\) column-incident clocks must survive their relevant deadlines. Their \(rs\) intersections must survive to \(\max(u,v)\). Multiplying exponential survivals gives \(\exp[-rbu-sav+rs\min(u,v)]\). Counting ordered selections proves the mixed factorial moments; inclusion-exclusion gives the exact joint distribution function.

At \(u=(\log a+x)/b\) and \(v=(\log b+y)/a\), with \(a,b\sim n\), the mixed factorial moments tend to \(e^{-rx-sy}\). The joint counts therefore converge to independent Poisson variables with means \(e^{-x}\) and \(e^{-y}\), by the multivariate factorial-moment criterion. In the critical window \((a-b)\log n/n\to\kappa\), replacing the separate centers by \((\log n)/n\) gives independent Poisson limits of means \(e^{\kappa/2-x}\) and \(e^{-\kappa/2-y}\) at the common scaled times. The joint event of zero isolated vertices has the asserted bivariate Gumbel limit. The difference of two independent standard Gumbels is standard logistic; continuity and the vanishing tie probability below yield both winner limits.

**Exact tie density.** Let \(F_{r,s}(t)\) denote the probability that an independent-edge clock process on a complete bipartite graph with parts of sizes \(r,s\) has no isolated vertices at time \(t\). On \(T_A=T_B=t\), there is almost surely one unique edge \(e\) whose arrival simultaneously completes its row and column. For a specified \(e\), its clock has density \(e^{-t}\), the other \(a+b-2\) incident clocks must exceed \(t\), and the independent remaining \((a-1)\)-by-\((b-1)\) submatrix must have no isolates at \(t\). Hence the subprobability density for a synchronized completion is
\[
 h_{a,b}(t)=ab\,e^{-(a+b-1)t}F_{a-1,b-1}(t),\qquad t>0.
\]
Inclusion-exclusion gives, for all positive integers \(r,s\),
\[
 F_{r,s}(t)=\sum_{i=0}^r\sum_{j=0}^s(-1)^{i+j}\binom ri\binom sj
 e^{-t(is+jr-ij)}.
\]
Integration of the nonnegative density \(h_{a,b}\) over \((0,\infty)\) and termwise integration of this finite sum yield the stated rational expression. This proof also covers the possibility that the final edge is incident to two previously isolated endpoints, rather than incorrectly assuming the two completion times are almost surely distinct.

**Rare-event scaling and the conditional law.** Put \(t_n(x)=(\log n+x)/n\), \(\lambda_\kappa=e^{\kappa/2}+e^{-\kappa/2}\), and \(Z_n=nT_A-\log n\) on the tie event. The joint Poisson limit already proved, applied to the remaining submatrix, gives for each fixed real \(x\)
\[
F_{a-1,b-1}(t_n(x))\longrightarrow
\exp[-\lambda_\kappa e^{-x}].
\]
The density formula and \(a+b=2n\) then give, pointwise in \(x\),
\[
 n\frac{d}{dx}\Pr(T_A=T_B,\ Z_n\le x)
=ab\,e^{-(2n-1)t_n(x)}F_{a-1,b-1}(t_n(x))
\longrightarrow e^{-2x-\lambda_\kappa e^{-x}}.
\]
Here the derivative is the density of the subprobability law on the tie event, and the formula holds for \(x> -\log n\).

To justify integration, let \(L=\max(a,b)\ge n\) and \(S=\min(a,b)\le n\). The requirement that every vertex on the larger side of the residual submatrix be nonisolated implies, for \(t\ge0\),
\[
F_{a-1,b-1}(t)
\le(1-e^{-(S-1)t})^{L-1}
\le\exp[-(L-1)e^{-(S-1)t}].
\]
At \(t=t_n(x)\), the exponent magnitude is at least \((1-1/n)e^{-x}\). After the substitution, the density is thus dominated for negative \(x\) by a constant times \(e^{2|x|}\exp[-e^{|x|}/2]\), and for positive \(x\) by a constant times \(e^{-3x/2}\); both bounds are integrable, independent of sufficiently large \(n\). Dominated convergence yields
\[
\lim_{n\to\infty}n\Pr(T_A=T_B)
=\int_{-\infty}^{\infty}e^{-2x-\lambda_\kappa e^{-x}}\,dx
=\frac1{\lambda_\kappa^2}.
\]
Dividing the limiting subprobability density by this mass gives the conditional density \(\lambda_\kappa^2e^{-2x-\lambda_\kappa e^{-x}}\). The change of variables \(y=\lambda_\kappa e^{-x}\) turns it into \(ye^{-y}\,dy\), the \(\operatorname{Gamma}(2,1)\) density. This proves all the claimed assertions.

## Verification

The standalone Python 3 program `verify.py` uses only the standard library. It computes the finite tie formula in exact rational arithmetic and independently enumerates every ordering of edges on all eight small rectangular matrices in its test set, including all \(9!\) orderings for the \(3\)-by-\(3\) case. Separately it enumerates every two-time edge-state assignment on the nine matrices with side sizes one through three at three pairs of rational survival probabilities, comparing with the exact two-time inclusion-exclusion formula. It also checks an independent special-family identity for \(a=2\). The program passed 51 exact assertions. These finite checks are separate from, and do not certify, the infinite proof above.

Run `python verify.py` in the directory containing this manuscript and `verify.py`.

## Relationship to prior work

Blasiak and Durrett [1, pp. 2, 8] investigate bipartite graph coverage and quote Saltykov's earlier first-order Poisson isolation result. Their repeated-draw model has exact row/column coverage independence at a fixed number of draws; it is not the distinct-edge exponential-clock model used here. Neither the first-order coverage threshold nor that independence statement supplies the exact synchronized-completion probability or its \(1/n\) coefficient.

Penrose [2, Theorems 2.1–2.3] proves broad isolated-vertex Poisson approximations for inhomogeneous random graphs. Such first-order total-count convergence alone cannot determine an event whose probability vanishes like \(1/n\), nor the conditional gamma law of its time. Berikkyzy and colleagues [4, Theorems 2–3 and Section 2] study **the same uniform edge-ordering process** and derive the distribution of the **total number** of edges whose two endpoints were unseen, equivalently the component count of a forest. Their recurrence tracks state transitions but their stated theorems do not distinguish whether the *final* coverage edge has two unseen endpoints; that finer terminal event, its rare-imbalance scaling, and its conditional time are not determined by the total component-count distribution. Saltykov [3] treats aggregate isolated vertices in a repeated-draw bipartite model; his original full text was unavailable for a complete comparison. The literature comparison concerns the precise new claim, not an assertion of universal priority.

## Limitations

The exact finite identity is stated for independent continuous exponential clocks on all distinct potential edges. The asymptotic coefficient and conditional law are established in the finite \(\kappa\) imbalance window; no uniform extension to diverging \(\kappa\) is asserted. The result concerns disappearance of isolated vertices, not the first time the graph becomes connected or obtains a matching. Other historical work on two-class coupon collection and bipartite graph processes might contain an equivalent rare-tie formula. No independent validation has been performed.

## References

[1] J. Blasiak and R. Durrett, *Random Oxford Graphs*, preprint dated June 7, 2004, https://sites.math.duke.edu/~rtd/RG/rndgr0604.pdf .

[2] M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, arXiv:1507.07132, first submitted July 25, 2015, https://arxiv.org/abs/1507.07132 .

[3] A. I. Saltykov, *The number of components in a random bipartite graph*, Diskretnaya Matematika 7(4) (1995), 86–94; translation in Discrete Mathematics and Applications 5(6), 515–523, https://www.mathnet.ru/eng/dm609 .

[4] Z. Berikkyzy, S. Butler, J. Cummings, K. Heysse, P. Horn, R. Luo, and B. Moran, *A forest building process on simple graphs*, arXiv:1608.00335, first submitted August 1, 2016, https://arxiv.org/abs/1608.00335 .
