# Exact first zero-subsidy arrival law for three agents under independent house rankings

## Finding
For three agents and sequentially appearing houses with independent continuous random values, let \(T\) be the first number of houses at which an injection assigning each agent one house, leaving the other houses unassigned, can be envy-free **without subsidies**. For every integer \(m\ge3\),
\[
\Pr(T>m)=q_m:=\prod_{r=3}^{m}\frac{3r-2}{r^2},\qquad
\Pr(T=m)=q_{m-1}\frac{(m-1)(m-2)}{m^2},\quad q_2=1.
\]
In particular the probability of a zero-subsidy allocation at \(m=3,4,5,6\) is respectively \(2/9,37/72,269/360,719/810\). Furthermore,
\[
q_m=\frac{4\,3^{m-2}\Gamma(m+1/3)}{\Gamma(7/3)(m!)^2}
\sim\frac4{9\Gamma(7/3)}\frac{3^m}{m!\,m^{2/3}},
\qquad \mathbb ET=3+\sum_{m=3}^{\infty}q_m=4.693896792076972\ldots.
\]
Thus the first feasible zero-subsidy horizon has an explicit complete law and a superexponentially decaying tail.

## Assumptions and scope
There are exactly three labeled agents and an infinite stream of labeled houses. Utilities \(U_{i,h}\), independently over agents \(i\) and houses \(h\), follow one common atomless distribution, such as \(\operatorname{Uniform}(0,1)\). Only the relative ranking among the first \(m\) houses matters. Each agent must receive exactly one distinct house; remaining houses may be unassigned. Envy compares only the three agents' assigned houses. An allocation is envy-free when no agent prefers another's assigned house to her own. Feasibility is the **offline terminal optimum at each prefix**, allowing complete reassignment; it is not a claim of an implementable online mechanism with restricted recourse or a guarantee of zero subsidy for every realized profile. The first horizon is well-defined with \(T\ge3\).

## Proof
**Collision-elimination lemma.** Fix any finite house set \(H\) with at least three houses and three strict preference orders. Let \(f_i(H)\) be agent \(i\)'s favorite house in \(H\). If the three favorites differ, assigning each favorite to its agent gives an envy-free injection. Otherwise some house \(h\) is favorite of at least two agents. No envy-free injection using houses in \(H\) can contain \(h\): at most one of the two agents gets \(h\), and the other strictly prefers \(h\) to their allocated house and so envies whoever receives it. Therefore the existence of an envy-free injection using \(H\) is equivalent to its existence using \(H\setminus\{h\}\). Iterating terminates either at three distinct current favorites (success) or fewer than three surviving houses (failure). This gives an exact decision procedure.

**Regeneration lemma.** At any unresolved stage with \(r\) surviving houses, at least two agents currently favor a common house \(h\). Delete \(h\). Condition on all earlier revealed favorites and deletions. Each agent whose current favorite was \(h\) has an independent uniformly random favorite among the remaining \(s=r-1\) houses: an iid continuous ranking, conditioned on its previously revealed favorite prefix, has a uniform residual ranking, independently across agents. If exactly two agents favored \(h\), the third agent's distinct favorite \(y\) remains fixed. The probability that the two refreshed favorites avoid \(y\) and are distinct equals \((s-1)(s-2)/s^2\). If all three favored \(h\), their refreshed favorites are iid uniform, and the probability of three distinct favorites is again \((s-1)(s-2)/s^2\). Thus conditional on *every* possible unresolved history, the success probability at the next stage is
\[
p_s:=\frac{(s-1)(s-2)}{s^2}.
\]
At the initial stage with \(m\) houses the three favorites are iid uniform, so the same probability \(p_m\) applies. Therefore failure probability is the product of the successive conditional failure probabilities for stages \(m,m-1,\ldots,3\):
\[
\Pr(\text{no envy-free injection using the first }m\text{ houses})
=\prod_{r=3}^{m}(1-p_r)
=\prod_{r=3}^{m}\frac{3r-2}{r^2}=q_m.
\]
If a prefix of houses admits an envy-free injection, enlarging that prefix cannot invalidate it: retain the same three houses and allocation. Consequently the event of infeasibility at horizon \(m\) is exactly \(\{T>m\}\), yielding the tail identity. Subtracting successive tails gives the mass function, including the initial case \(\Pr(T=3)=2/9\).

**Closed form, tail and mean.** Writing \(3r-2=3(r-2/3)\) and using the gamma-function product identity gives the displayed closed form. The gamma-ratio asymptotic \(\Gamma(m+1/3)/\Gamma(m+1)\sim m^{-2/3}\) gives the stated superexponential tail. In particular \(T\) is almost surely finite and has all finite moments. Summing survival probabilities yields \(\mathbb ET=3+\sum_{m\ge3}q_m\). The decimal is obtained by summing positive rational terms; a certified remainder after \(m=M\) is no more than \(q_{M+1}/(1-\rho_M)\) where \(\rho_M=(3(M+1)+1)/(M+2)^2<1\), since subsequent term ratios decrease for \(M\ge3\).

## Verification
The accompanying standalone `check.py` enumerates all triples of strict preference orders, after fixing the first agent's order by house-label symmetry, for \(m=3,4,5,6\). It computes envy-free feasibility both from a direct test of all three-house subsets and from the collision-elimination procedure; these independent algorithms agree on every test. It also checks the entire distribution of the number of deletions against the exact conditional-stage product. This is finite corroboration; the proof above establishes the all-horizon conclusion.

## Relationship to prior work
Gan, Suksompong and Voudouris (2019) gave a deterministic general envy-free house-assignment algorithm based on minimal Hall violators and proved high-probability existence in a different asymptotic regime with growing agent count. The collision deletion is the special three-agent manifestation of their more general deterministic approach; the novelty claimed here is **not** the deterministic algorithm. Teh, Cohen, Celine, Yu and Wooldridge (2026) introduce sequential house allocation with subsidies and motivate asking when a zero-subsidy terminal optimum first becomes possible. The present exact law is for a random infinite house stream and unrestricted terminal reassignment, rather than competitive online subsidy minimization. The exact finite-horizon stochastic product, first-arrival distribution and expectation were not identified in the examined sources.

## Limitations
The conclusion applies to exactly three agents, iid atomless house utilities with exchangeable rankings, and envy relative only to assigned houses. Arbitrary correlated preferences, adversarial arrivals, multi-house bundles, more than three agents, constraints on recourse, and online implementability are not established. The 2026 motivating preprint's available abstract and introductory material were consulted, but a full-text access limitation prevents ruling out every appendix-level parallel statement; unindexed prior work is also possible. No independent scientific audit has been conducted.

## References
1. N. Teh, S. Cohen, K. F. Celine, B. Yu, M. J. Wooldridge, *Online House Allocation with Subsidy*, arXiv:2609.29691v1 (first publicly available 2026-08-31), https://arxiv.org/abs/2609.29691.
2. J. Gan, W. Suksompong, A. A. Voudouris, *Envy-Freeness in House Allocation Problems*, arXiv:1905.00468 (first public 2019-05-01), https://arxiv.org/abs/1905.00468; *Mathematical Social Sciences* 101 (2019), 104–106.
3. P. Manurangsi, *Envy-Free Allocations for Random Non-Additive Valuations*, arXiv:2610.34434 (2026), https://arxiv.org/abs/2610.34434. This addresses a distinct random-allocation model.
