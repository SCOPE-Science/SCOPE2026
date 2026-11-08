# Sharp stochastic-order reversal for SI sentinel placement on a star

## Finding

On a star with one hub and \(m\ge1\) leaves, suppose infection follows a continuous-time susceptible–infected (SI) process with leaf-to-hub transmission rate \(\alpha>0\) and hub-to-each-leaf rate \(\beta>0\). Choose one initial infected vertex uniformly from the \(m+1\) vertices. Continuously monitor exactly \(k\) vertices, where \(1\le k\le m\), and let \(T\) be the first time a monitored vertex is infected; detection at time zero is permitted.

There are exactly two classes of \(k\)-vertex monitoring layouts up to leaf symmetry: \(H\), monitoring the hub and \(k-1\) leaves, and \(L\), monitoring \(k\) leaves but not the hub. Write \(T_H,T_L\) for their detection times. For every \(t>0\),

\[
\Pr(T_L>t)-\Pr(T_H>t)=
\frac{(m-k+1)\alpha-k\beta}{m+1}
\int_0^t e^{-\alpha u}e^{-k\beta(t-u)}\,du.
\]

The integral is strictly positive. Thus the complete, sharp optimality classification is

\[
\begin{cases}
T_H<_{\rm st}T_L,& k\beta<(m-k+1)\alpha,\\
T_H\overset{d}=T_L,&k\beta=(m-k+1)\alpha,\\
T_L<_{\rm st}T_H,&k\beta>(m-k+1)\alpha.
\end{cases}
\]

Here \(X<_{\rm st}Y\) means \(\Pr(X>t)<\Pr(Y>t)\) for every \(t>0\); both layouts also have the same time-zero detection probability \(k/(m+1)\). Consequently, the displayed choice minimizes **every** nondecreasing integrable penalty of detection delay, not merely its expected value. At equality, every such penalty ties because the **entire laws coincide**.

Equivalently, as the integer monitoring budget increases, the optimum changes from including the hub to omitting it at the critical value

\[
k_{\rm c}=\frac{(m+1)\alpha}{\alpha+\beta}.
\]

Choose \(H\) for \(k<k_{\rm c}\), choose \(L\) for \(k>k_{\rm c}\), and either at integer equality. In particular, with symmetric rates \(\alpha=\beta\), the hub is excluded when more than half of the vertices are monitored; if exactly half are monitored, the two first-detection laws are identical.

## Assumptions and scope

The graph is the undirected star \(K_{1,m}\), but each undirected edge carries two oriented, independently timed transmission mechanisms. An infected leaf attempts transmission to the susceptible hub after an exponential waiting time with rate \(\alpha\). An infected hub attempts transmission to each susceptible leaf at independent rate \(\beta\). Infections are permanent, with no recovery or reinfection. Only one vertex is infected initially, uniformly over all vertices and independently of transmission clocks. A monitored initial seed triggers detection immediately; otherwise detection is at first infection of the monitored set. All monitors are perfect and continuously active. Rates are constant and positive. Results concern finite \(m,k\), all \(t\ge0\), and no asymptotic population limit.

## Proof

**Step 1 (all possible placements).** Leaves are exchangeable. A set of exactly \(k\) monitored vertices either includes the hub, leaving \(m-k+1\) unmonitored leaves, or excludes the hub, leaving \(m-k\) unmonitored leaves and one unmonitored hub. These exhaust all layouts up to symmetry.

**Step 2 (conditional detection laws).** Let \(E_\alpha\sim\operatorname{Exp}(\alpha)\) and \(E_r\sim\operatorname{Exp}(r)\), independently, where \(r=k\beta\). Under \(H\), the initially infected vertex is monitored with probability \(k/(m+1)\); otherwise it is an unmonitored leaf and infects the monitored hub after \(E_\alpha\). Therefore

\[
T_H\sim \frac{k}{m+1}\delta_0+
\frac{m-k+1}{m+1}\operatorname{Exp}(\alpha).
\]

Under \(L\), the seed is monitored with probability \(k/(m+1)\). With probability \(1/(m+1)\), it is the hub, and detection occurs when the first of \(k\) monitored leaves is infected, after an \(\operatorname{Exp}(r)\) time. With probability \((m-k)/(m+1)\), it is an unmonitored leaf. Its transmission to the hub takes an independent \(E_\alpha\); subsequently the first monitored leaf is infected after \(E_r\). Infection of other unmonitored leaves cannot speed up infection of a monitored leaf on a star. Hence

\[
T_L\sim \frac{k}{m+1}\delta_0+
\frac{1}{m+1}\operatorname{Exp}(r)+
\frac{m-k}{m+1}\mathcal L(E_\alpha+E_r).
\]

The mixture notation here means a random choice among the displayed components, not their sum; \(\mathcal L\) denotes the law of the indicated sum.

**Step 3 (strict signed survival difference).** For independent exponential variables,

\[
\Pr(E_\alpha+E_r>t)
=e^{-\alpha t}+
\alpha\int_0^t e^{-\alpha u}e^{-r(t-u)}\,du.
\]

Also \(e^{-rt}-e^{-\alpha t}=(\alpha-r)\int_0^t e^{-\alpha u}e^{-r(t-u)}\,du\), including \(r=\alpha\) by continuity. Substitution into the two mixtures, followed by cancellation of their identical atoms at zero, gives

\[
(m+1)\bigl[\Pr(T_L>t)-\Pr(T_H>t)\bigr]
=\bigl[(m-k+1)\alpha-r\bigr]
\int_0^t e^{-\alpha u}e^{-r(t-u)}\,du.
\]

For every positive \(t\), the integral is strictly positive. This proves all strict stochastic-order comparisons and equality of full laws, including the repeated-rate case \(r=\alpha\). Since all layouts belong to \(H\) or \(L\), each comparison is globally optimal among exactly \(k\) monitored vertices.

**Step 4 (budget boundary and moments).** The threshold inequality \(k\beta>(m-k+1)\alpha\) is equivalent to \(k> (m+1)\alpha/(\alpha+\beta)\). Independently, integrating the survival functions yields

\[
\mathbb E[T_H]=\frac{m-k+1}{(m+1)\alpha},\qquad
\mathbb E[T_L]=\frac{1}{m+1}
\left(\frac{m-k}{\alpha}+\frac{m-k+1}{k\beta}\right).
\]

At \(m=5\), \(\alpha=\beta=1\), the means for \(k=2,3,4\) are, respectively, \((2/3,5/6)\), \((1/2,1/2)\), and \((1/3,1/4)\), in \((H,L)\) order. Thus including the highest-degree vertex is optimal for two monitors, completely tied for three, and strictly suboptimal for four.

## Verification

Run `python3 verify_star.py` using Python 3. The verifier independently constructs the full susceptible–infected continuous-time Markov chain of every star with \(1\le m\le7\) under each layout. It computes exact rational Laplace transforms of first detection from each possible seed by recursive state equations, then compares them against the separately derived mixture transforms for multiple rational transmission and transform parameters, including the exact-tie rate. It also checks the survival-difference formula at positive times. The recorded execution passed **6,048** assertions. The finite grid is a diagnostic cross-check: the universally quantified result follows from Steps 1–4, not the finite tests.

For each \(s>0\), a useful independent algebraic identity is

\[
\mathbb E[e^{-sT_L}]-\mathbb E[e^{-sT_H}]
=\frac{s\,[k\beta-(m-k+1)\alpha]}
{(m+1)(s+\alpha)(s+k\beta)}.
\]

## Relationship to prior work

Leskovec, Krause, Guestrin, Faloutsos, VanBriesen and Glance (2007) formalize outbreak detection on networks and prove submodularity of broad expected sensor-reward functions; their general-purpose approximation results do not supply a star-specific directed-SI stochastic-order classification or equality-in-law threshold. Ciccolini, Donker, Grundmann, Bonten and Woolhouse (first online January 27, 2014) analyze directed interhospital SI spread and optimize surveillance performance on actual patient-movement networks by heuristic methods; their main article does not state the present exact all-budget star law. Colman, Holme, Sayama and Gershenson (2019) study degree-based versus spatially distributed sentinel placement by simulation in SIR networks; their outcomes and process differ from first-detection time in this SI model. The novelty claim is only the precise all-parameter stochastic-order phase diagram and exact full-distribution tie for this defined model. General sensor optimization, SI mechanics, and exponential waiting-time identities are not claimed as new.

## Limitations

The uniform seed and exponential transmission clocks are essential to the stated exact tie and global stochastic ordering. For instance, replace transmission times by deterministic oriented delays of 1 from leaf to hub and \(1/2\) from hub to leaf. At \(m=5,k=3\), \(H\) has survival probability \(1/2\) until time 1 and zero afterward, while \(L\) has survival probability \(1/2\) before time \(1/2\), \(1/3\) between \(1/2\) and \(3/2\), and zero afterward. The survival curves therefore cross, so there is no universal stochastic-order comparison for arbitrary delays. A nonuniform initial-seed law, imperfect tests, recovery, adaptive monitoring, or general topology may also break the phase diagram. No claim is made about minimizing the number infected before detection, clinical effectiveness, or empirical optimal surveillance arrangements. Historical completeness remains subject to external checking.

## References

1. Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., VanBriesen, J., and Glance, N. (2007). *Cost-effective outbreak detection in networks*. KDD 2007. DOI: 10.1145/1281192.1281239. Full technical report: https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf
2. Ciccolini, M., Donker, T., Grundmann, H., Bonten, M. J. M., and Woolhouse, M. E. J. (2014). *Efficient surveillance for healthcare-associated infections spreading between hospitals*. PNAS 111, 2271–2276. First online January 27, 2014. DOI: 10.1073/pnas.1308062111. Full text: https://www.pnas.org/content/pnas/111/6/2271.full.pdf
3. Colman, E., Holme, P., Sayama, H., and Gershenson, C. (2019). *Efficient sentinel surveillance strategies for preventing epidemics on networks*. PLoS Computational Biology 15, e1007517. DOI: 10.1371/journal.pcbi.1007517. Full text: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007517
