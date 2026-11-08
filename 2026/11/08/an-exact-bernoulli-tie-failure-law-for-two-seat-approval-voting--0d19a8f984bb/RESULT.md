# An exact Bernoulli tie-failure law for two-seat approval voting

## Finding

In a two-seat approval election, call an approval-score-maximizing committee **bad** if it violates justified representation (JR). The existence of at least one bad maximizing committee has an exact distribution under independent Bernoulli approval culture, for every positive voter count \(n\), every number \(m\geq2\) of labeled candidates, and every common approval probability \(0<p<1\).

For odd \(n\) the probability is zero. For even \(n\), put \(h=n/2\), \(M=\binom{n}{h}\), \(L=M/2\), and
\[
a=\Pr\{\operatorname{Bin}(n,p)<h\},\quad b=\Pr\{\operatorname{Bin}(n,p)=h\},\quad F(z)=2e^z-1+z^2.
\]
Then the probability \(P_{n,m}(p)\) that **some** approval-voting maximizing committee fails JR is exactly
\[
P_{n,m}(p)=\sum_{r=0}^{m}\binom mr a^{m-r}b^r\left(1-\frac{r!}{M^r}[z^r]F(z)^L\right).
\]
Here \([z^r]\) extracts the coefficient of \(z^r\); all quantities are finite and explicitly computable. In the smallest nontrivial candidate set, \(m=3\), this becomes
\[
P_{n,3}(p)=3\binom n{n/2}[p(1-p)]^{3n/2}\quad(n\text{ even}),
\]
whereas for odd \(n\) it is zero. With uniformly random tie-breaking among all maximizing committees and \(m=3\), the failure probability is one-third of that expression. At \(p=1/2\), the latter probability is asymptotic along even \(n\) to \(\sqrt{2/(\pi n)}\,4^{-n}\).

For fixed even \(n\) and \(p\in(0,1)\), letting \(q=\Pr\{\operatorname{Bin}(n,p)\leq n/2\}\), the exact law additionally yields
\[
P_{n,m}(p)\sim q^m\quad\text{as }m\to\infty.
\]
This is an *existence of a bad tie-break* probability, not the probability that all maximizing committees fail JR: the latter is always zero for two seats.

## Assumptions and scope

There are \(n\geq1\) labeled voters and \(m\geq2\) labeled candidates. Voter \(i\) approves an arbitrary subset \(A_i\) of the candidates. A committee has exactly two distinct members. Candidate \(c\) has voter-support set \(H_c=\{i:c\in A_i\}\) and score \(s(c)=|H_c|\). Approval voting (AV) maximizes \(s(c)+s(d)\) over distinct candidates. JR means there is no group of at least \(n/2\) voters who approve a common candidate while every member approves neither elected candidate. Voters may submit empty ballots; the deterministic statement is valid for every ballot profile.

For the probability result, approval indicators are mutually independent across all voter-candidate pairs and each is one with probability \(p\in(0,1)\). An adverse tie-break is *possible* if **at least one** committee maximizing the AV score fails JR. For the separately stated three-candidate uniform-tie result, the tie-break selects uniformly among the distinct maximizing two-element committees.

## Proof

**Exact characterization of failure.** Suppose a maximizing pair \(W=\{c,d\}\) fails JR. Let \(U\) be its uncovered voters. There is a candidate \(e\notin W\) approved by at least \(n/2\) members of \(U\), so \(|U|\geq n/2\) and \(s(e)\geq n/2\). Since \(c\) and \(d\) are both top-two approval-score candidates (allowing ties), \(s(c),s(d)\geq s(e)\). Yet their approval supports avoid \(U\), so both scores are at most \(n-|U|\leq n/2\). All inequalities are therefore equalities: \(n\) must be even; \(|U|=n/2\); \(H_c=H_d=[n]\setminus U\); \(H_e=U\); and every candidate has score at most \(n/2\). Conversely, if these conditions hold for distinct \(c,d,e\), then \(\{c,d\}\) is maximizing and the complementary half of voters is jointly unrepresented. Thus a bad AV maximizing committee exists **if and only if** (i) no candidate scores above half, and (ii) for some half-sized support mask \(H\) at least two candidates have support exactly \(H\) and at least one has support exactly \(H^c\). This already proves the odd-\(n\) claim. It also shows that replacing one of \(c,d\) by \(e\) is a maximizing committee covering every voter, so no profile has every maximizing pair fail JR. The latter existence fact is previously known (Aziz et al., 2015) and is not claimed as new.

**Coefficient formula.** For even \(n\), the numbers of voters approving any fixed candidate are independent \(\operatorname{Bin}(n,p)\) variables. For the adverse event all \(m\) scores must be at most \(h\). Exactly \(r\) candidates have score equal to \(h\), with total probability \(\binom mr b^r a^{m-r}\). Conditional on these scores, the \(r\) half-sized support masks are independent and uniform on the \(M\) half-sized subsets of \([n]\). Their complement involution partitions those masks into \(L=M/2\) unordered complementary pairs. For any one pair, with occupancy numbers \((x,y)\) in the two orientations, avoiding the failure motif means \(x=0\), or \(y=0\), or \(x=y=1\). The bivariate exponential occupancy weight summed by total occupancy is therefore
\[
1+2\sum_{j\geq1}\frac{z^j}{j!}+z^2=2e^z-1+z^2=F(z).
\]
For all \(L\) pairs the weight is \(F(z)^L\). Of the \(M^r\) ordered selections of masks, precisely \(r!\,[z^r]F(z)^L\) avoid the motif (including the \(r=0\) case). Subtracting their conditional probability and summing over \(r\) proves the formula.

**Three candidates and asymptotics.** If \(m=3\), the only possible failure pattern is exactly two labeled candidates with identical half-sized support and the remaining candidate with complementary support. There are \(3\binom n{n/2}\) distinct labeled profiles of this form. Each profile has probability \([p(1-p)]^{3n/2}\), giving the closed form. It has three maximizing committees and exactly one is bad, proving the uniform-tie factor \(1/3\). The central binomial coefficient estimate \(\binom{n}{n/2}\sim 2^n\sqrt{2/(\pi n)}\) gives the displayed \(p=1/2\) asymptotic.

Finally fix even \(n\). The event that all candidate scores are at most \(h\) has probability exactly \(q^m\). Conditional on that event, candidates remain independent and each of the \(M\) half-sized masks has strictly positive conditional probability. As \(m\to\infty\), the counts in any fixed complementary pair both diverge in probability, so the probability of the failure motif conditional on the event tends to one. This proves \(P_{n,m}(p)/q^m\to1\), with \(0<q<1\).

## Verification

`verify.py` is a complete Python-standard-library checker. It enumerates every labeled candidate-support profile for ten finite \((n,m)\) cases, independently enumerates every AV-optimal committee and tests JR directly. The combined profile count is \(374{,}592\). It separately evaluates the exact complementary-mask generating-function formula with rational arithmetic and compares probabilities against exhaustive enumeration. Its finite checks include odd and even populations, \(m=3,4,5,6\), all tied maximizers, and verification that every instance admits a JR-maximizing committee. Additional exact weighted profile-enumeration checks use \(p=1/3,2/5,1/4\). Run `python3 verify.py`. All reported tests pass. The universal identities, parity obstruction, and asymptotics rely on the analytic proof above, not on finite enumeration.

## Relationship to prior work

Aziz et al. (2015), Theorem 3, explicitly prove that AV with two seats can select a JR committee by favorable tie-breaking and that for at least three seats AV can fail JR. The deterministic existence part is therefore **prior art**. The specific complementary-support characterization above is used to count all adverse tie situations; the new asserted result is the exact all-candidate Bernoulli failure law, including its generating function, three-candidate uniform-tie formula, and fixed-population asymptotic.

Elkind et al. (2021) analyze justifying groups and their behavior under impartial culture, without an exact probability for the adverse AV tie event in the inspected results. Jin, Liu, and Tao (2026) study incompatibility of ex-ante fractional efficiency and ex-post JR in general multiwinner lotteries, not this two-seat random AV event. Becker et al. (2026) characterize fractional Pareto-optimality in multiwinner voting; they do not provide the probabilistic two-seat tie law. An AV-maximizing committee is fractionally Pareto-efficient because its total voter approval utility is maximal, but this is a routine consequence of welfare maximization, not an independent novelty claim. The literature comparisons cannot rule out equivalent unindexed classifications.

## Limitations

The Bernoulli model assumes full independence and common approval probability. The event concerns the *existence* of a violating maximizer, not behavior under every fixed deterministic tie-breaking rule. Only when \(m=3\) is the uniform-among-maximizers failure probability explicitly given; for more candidates the existence probability does not by itself determine the distribution of failures under random tie-breaking. The fixed-\(n\) asymptotic does not provide a joint \(n,m\) threshold. An independent scientific audit is not yet performed.

## References

- Aziz, H.; Brill, M.; Conitzer, V.; Elkind, E.; Freeman, R.; Walsh, T. (2015). *Justified Representation in Approval-Based Committee Voting*. AAAI. Theorem 3. https://arxiv.org/abs/1407.8269 ; https://users.cs.duke.edu/~conitzer/justifiedAAAI15.pdf
- Elkind, E.; Faliszewski, P.; Igarashi, A.; Manurangsi, P.; Schmidt-Kraepelin, U.; Suksompong, W. (2021). *Justifying Groups in Multiwinner Approval Voting*. https://arxiv.org/abs/2108.12949
- Becker, P.; Boehmer, N.; Frank, F.; Glessen, L. (2026). *Fractional Pareto-Optimality in Multiwinner Voting*, first publicly posted June 9, 2026. https://arxiv.org/abs/2606.11160
- Jin, J.; Liu, X.; Tao, B. (2026). *Limitations of Best-of-Both-Worlds Solutions in Approval-Based Multiwinner Elections*, first publicly posted August 3, 2026. https://arxiv.org/abs/2608.01830
- Dong, C. (2026). *Jointly Satisfying Pareto Optimality and Justified Representation is NP-Hard in Approval-Based Multiwinner Voting*, first publicly posted September 8, 2026. https://arxiv.org/abs/2609.08357
