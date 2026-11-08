# A single cross-approving voter creates a quadratic stochastic-representation threshold

## Finding

Consider an approval-based temporal election with exactly two repeatedly available candidates \(A,B\), \(a\ge1\) voters approving only \(A\), \(b\ge1\) approving only \(B\), and \(c\ge0\) approving both. Put \(n=a+b+c\). In a horizon of \(L\ge1\) rounds, a stationary independent lottery selects \(A\) with fixed probability \(p\in[0,1]\) on each round. Let \(T\) count its selections.

Define the exact integer bounds
\[
\ell_L=\left\lfloor\frac{La}{n}\right\rfloor,
\qquad u_L=L-\left\lfloor\frac{Lb}{n}\right\rfloor.
\]
Then each of temporal proportional justified representation (PJR), extended justified representation (EJR), and extended justified representation+ (EJR+) holds **if and only if** \(\ell_L\le T\le u_L\). Their common exact success probability is
\[
F_L(p)=\sum_{j=\ell_L}^{u_L}\binom Lj p^j(1-p)^{L-j}.
\]
If \(1\le\ell_L\le u_L\le L-1\), there is a **unique** best stationary independent lottery, and its probability is given without numerical optimization by
\[
\log\frac{p_L}{1-p_L}=
\frac{\log\binom{L-1}{\ell_L-1}-\log\binom{L-1}{u_L}}{u_L-\ell_L+1}.
\]
If \(\ell_L=0\) and \(u_L<L\), the maximum is attained at \(p=0\); if \(\ell_L>0\) and \(u_L=L\), at \(p=1\); and if \(\ell_L=0,u_L=L\), every \(p\) succeeds surely.

For fixed positive \(a,b\), no overlap (\(c=0\)) leads to \(\max_p F_L(p)=\Theta(L^{-1/2})\). On horizons divisible by \(n\), this is exactly
\[
\max_p F_L(p)=\binom L{La/n}\left(\frac an\right)^{La/n}
\left(\frac bn\right)^{Lb/n}
\sim\frac{1}{\sqrt{2\pi L(a/n)(b/n)}}.
\]
With any fixed overlap \(c>0\), put \(\alpha=a/n\) and \(\beta=1-b/n\), so \(0<\alpha<\beta<1\). For each fixed \(p\in(\alpha,\beta)\), success tends to one exponentially, with the exact failure rate
\[
\lim_{L\to\infty}-\frac1L\log(1-F_L(p))
=\min\{D(\alpha\Vert p),D(\beta\Vert p)\},
\]
where \(D(x\Vert p)=x\log(x/p)+(1-x)\log((1-x)/(1-p))\). The asymptotically optimal rate and the limit of the exact optimizing probabilities occur at the unique \(p_*\in(\alpha,\beta)\) satisfying \(D(\alpha\Vert p_*)=D(\beta\Vert p_*)\), namely
\[
\log\frac{p_*}{1-p_*}=
\frac{h(\beta)-h(\alpha)}{\beta-\alpha},\qquad
h(x)=x\log x+(1-x)\log(1-x).
\]

In particular, take \(a=b=m\ge1\), \(c=1\), so \(n=2m+1\). For every \(L\ge3\), the exact optimum is the fair coin \(p_L=1/2\). Along any odd \(n\to\infty\) and \(L=L_n\to\infty\), if \(L_n/n^2\to\tau\in[0,\infty)\), then
\[
\boxed{\lim_{n\to\infty}\max_p F_{L_n}(p)=2\Phi(\sqrt\tau)-1,}
\]
where \(\Phi\) is the standard normal cumulative distribution function. If \(L_n/n^2\to\infty\), the limit equals one. Thus even **one** voter approving both options creates a sharp quadratic-horizon transition between negligible and overwhelming probability of ex-post proportional representation.

## Assumptions and scope

The two candidate options remain available every round; approvals do not vary by round. The integers \(a,b\) are positive, \(c\) is nonnegative, and \(L\) is any positive integer. Random choices are **independent across rounds with a single, fixed parameter** \(p\); correlated, history-adaptive or quota-enforcing schedules are outside the optimization problem. The proportionality notions are the ordinary (not strong-prefixed) temporal PJR/EJR/EJR+ definitions of Phillips et al. (2025) and Teh (2026): a group agreeing in \(t\) rounds receives a quota of \(\lfloor t|S|/n\rfloor\) satisfying rounds, collectively or through one group member as appropriate. EJR+ uses the \((\sigma,\tau)\)-cohesion and single-round disjunction of the cited definitions.

## Proof

**1. Exact reduction to two integer quotas.** Let \(S\) be any voter group unanimous on a candidate in some round. As approvals are static, it is unanimous throughout. If \(S\) contains a voter approving both candidates, that voter is personally satisfied on all \(L\) rounds, and \(S\) is collectively satisfied on all rounds. Therefore no PJR or EJR demand can fail. In the EJR+ formulation the same voter satisfies every possible demand \(\lfloor\tau\sigma/n\rfloor\le L\).

If \(S\) contains no such voter, it can have unanimous agreement only when it is contained entirely in the \(a\) exclusively-\(A\) voters or entirely in the \(b\) exclusively-\(B\) voters. For the first case both collective and individual satisfaction are \(T\), and the strongest quota is \(\lfloor La/n\rfloor\). For the second it is \(L-T\), with quota \(\lfloor Lb/n\rfloor\). Thus PJR and EJR are equivalent to the stated interval. EJR+ also follows when these quotas hold: for a single-type cohesive group \(S\), every \((\sigma,\tau)\)-demand has \(\sigma\le |S|\), \(\tau\le L\), hence cannot exceed its satisfied full-horizon quota. Conversely if one quota fails, use the entire corresponding pure group, \(\sigma=|S|\), \(\tau=L\), and a round choosing the opposite candidate: neither EJR+ disjunct holds. This directly establishes EJR+ equivalence as well.

**2. Exact probability and optimizer.** Independence gives \(T\sim\operatorname{Binomial}(L,p)\), yielding the finite sum. For \(1\le\ell_L\le u_L\le L-1\), differentiate and telescope consecutive binomial terms:
\[
F_L'(p)=L\left[\binom{L-1}{\ell_L-1}p^{\ell_L-1}(1-p)^{L-\ell_L}
-\binom{L-1}{u_L}p^{u_L}(1-p)^{L-1-u_L}\right].
\]
Dividing the two positive terms shows that the derivative changes from positive to negative precisely once, when \((p/(1-p))^{u_L-\ell_L+1}=\binom{L-1}{\ell_L-1}/\binom{L-1}{u_L}\). This proves uniqueness and the log-odds formula. When an endpoint quota vanishes, the claimed endpoint solutions follow from monotonicity of a binomial lower or upper tail; if both vanish, the event is certain.

**3. No overlap versus positive overlap.** For \(c=0\), since \(a+b=n\), the allowed interval contains either one or two adjacent integers, both at distance \(O(1)\) from \(L a/n\). At each such interior integer the maximized binomial point mass is \(O(L^{-1/2})\) by Stirling's formula; setting \(p=a/n\) attains a matching \(\Omega(L^{-1/2})\). When \(n\mid L\), the interval is a singleton and its maximum is at \(p=a/n\); Stirling gives the displayed equivalent.

For \(c>0\), the two endpoints normalized by \(L\) approach \(\alpha<\beta\). For \(p\) strictly between them, standard one-sided binomial large-deviation bounds, with matching single boundary-mass lower bounds, give rates \(D(\alpha\Vert p)\) and \(D(\beta\Vert p)\) for the disjoint failure tails. The smaller rate controls their sum. On \((\alpha,\beta)\), the first divergence increases strictly with \(p\), the second decreases strictly; their unique intersection maximizes the minimum. Subtracting the two divergences gives \(h(\alpha)-h(\beta)+(\beta-\alpha)\log(p/(1-p))\), proving the displayed formula. Finally, Stirling applied to the finite log-odds optimizer from step 2 yields the same limit \(p_L\to p_*\). Because it is optimal for every finite \(L\), it attains the optimal exponential rate.

**4. One bridge voter and the critical window.** For \(a=b=m\), \(c=1\), the interval is symmetric about \(L/2\). For \(L\ge3\), its lower endpoint is positive, so step 2 gives the unique optimum \(p=1/2\). Since \(m/n=1/2-1/(2n)\), the interval boundaries differ from \(L/2\) by \(L/(2n)+O(1)\). Under the fair coin, \((T-L/2)/(\sqrt L/2)\) converges to a standard normal, while the normalized half-width is \(\sqrt L/n+O(L^{-1/2})\). If \(L/n^2\to\tau\in(0,\infty)\), continuity of the normal distribution yields \(2\Phi(\sqrt\tau)-1\). If \(L/n^2\to0\) while \(L\to\infty\), the binomial maximal atom is \(O(L^{-1/2})\); at most \(O(1+L/n)\) atoms are accepted, so their total probability vanishes. If \(L/n^2\to\infty\), Chebyshev's inequality gives vanishing failure probability. These three regimes complete the proof.

## Verification

Run `python3 CHECK.py` using only the Python standard library. The checker directly reconstructs temporal PJR, EJR and EJR+ on all binary outcomes in its finite test domain rather than assuming their equivalence. It compares exact-rational binomial probabilities against direct enumeration, tests stationary optimizer stationarity, and evaluates the critical-window limit numerically without Monte Carlo. In the checked environment it passed 6,858 direct axiom checks and 900 additional exact-probability/optimizer checks (7,758 total), together with four critical-window examples. The proof above, not those finite checks, establishes the statements for unbounded parameters.

## Relationship to prior work

Phillips, Elkind, Teh and Wąs (2025), *Strengthening Proportionality in Temporal Voting*, introduce stronger temporal representation axioms including EJR+. Teh (2026), *The Price of Proportional Representation in Temporal Voting*, specifies the relevant axioms, proves EJR+ coincides with EJR on static approvals (Lemma 4.2), and studies deterministic welfare costs and fixed-candidate optimization. Borodin and Lueger (2026), *Online Temporal Voting: Strategyproofness, Proportionality and Asymptotic Analysis*, study online rules and approximate proportionality. The present claim instead fixes the independent stationary sampling restriction and derives an exact ex-post success probability, its unique optimum, a KL-rate transition, and a quadratic Gaussian boundary when one voter crosses the two approval blocs. Existing general binomial-tail probability results provide techniques, not a claim about these electoral axioms or this crossover. Dependent quota-enforcing schemes can achieve deterministic ex-post representation on these elections and are not ruled out by the probabilistic limits here.

## Limitations

The analysis is confined to two always-available candidates, fixed approvals, and independent identically distributed choices. It does not prove analogous thresholds for three or more candidates, changing approvals, correlated randomization, arbitrary strategic agents, or temporal axioms beyond PJR/EJR/EJR+. The \(\Theta(L^{-1/2})\) asymptotic holds at fixed positive bloc sizes, and the Gaussian formula assumes both odd electorate size and horizon diverge in the specified joint limit. The literature comparison is not an assertion of publication priority: unindexed treatments of randomized temporal fairness may exist. The result is a scientific self-review, not an independent validation.

## References

1. B. Phillips, E. Elkind, N. Teh, T. Wąs, *Strengthening Proportionality in Temporal Voting*, first public arXiv version 2025-05-28, https://arxiv.org/abs/2505.22513.
2. N. Teh, *The Price of Proportional Representation in Temporal Voting*, first public arXiv version 2026-05-11, https://arxiv.org/abs/2605.11157; IJCAI 2026 full text https://ijcai.org/proceedings/2026/394.
3. A. Borodin and T. Lueger, *Online Temporal Voting: Strategyproofness, Proportionality and Asymptotic Analysis*, first public arXiv version 2026-03-27, https://arxiv.org/abs/2603.26504.
4. N. Chandak, S. Goel, D. Peters, *Proportional Aggregation of Preferences for Sequential Decision Making*, AAAI 2024, https://arxiv.org/abs/2306.14858.
