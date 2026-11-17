# Exact liquidity and budget-vector thresholds for two-denomination envy-free division

## Finding
Let \(n\ge2\) agents have **identical additive valuations** for \(t\) goods worth \(h\) each and \(u\) goods worth \(1\) each, where \(h\ge2\) and \(t,u\) are nonnegative integers with \(t+u\ge1\). Money is transferable between agents, with no external source; each agent \(i\) may make a net payment of at most an integer budget \(b_i\ge0\). A complete allocation and a zero-sum vector of real monetary transfers are required to eliminate all envy.

Put
\[
W=ht+u,\qquad q=\lfloor W/n\rfloor,\qquad r=W-nq,\qquad c_i=q+b_i.
\]
An envy-free, budget-feasible outcome exists **if and only if** both
\[
\boxed{\ \sum_{i=1}^n b_i\ge r\quad\text{and}\quad
\sum_{i=1}^n\left\lfloor\frac{q+b_i}{h}\right\rfloor\ge t\ }.
\]
There is a linear-time construction, measured in \(n\) plus the number of goods when the allocation is written out; with multiplicity-encoded goods, it uses \(O(n)\) arithmetic operations.

There is also an exact answer if budgets can be chosen freely but their total is minimized. Write
\[
s=q\bmod h,\qquad \Delta=\max\{0,t-n\lfloor q/h\rfloor\}.
\]
The smallest **total integer payment capacity** permitting an envy-free outcome is
\[
\boxed{B_{\min}=\max\{r,(h-s)\Delta\}.}
\]
In particular, \(\Delta<n\), and a minimum-total-budget vector can be formed by giving \(h-s\) units to \(\Delta\) distinct agents, then adding any remaining \(B_{\min}-(h-s)\Delta\) units to any agent.

For an additional exact reliability consequence, suppose independently \(b_i\sim\operatorname{Bernoulli}(p)\), so an agent has one monetary unit of payment capacity with probability \(p\) and none otherwise. Write \(B=\sum_i b_i\), and \(H_0=n\lfloor q/h\rfloor\). If \(s=h-1\), feasibility is equivalent to \(B\ge\max\{r,t-H_0\}\). If \(s<h-1\), it is impossible when \(t>H_0\), and otherwise is equivalent to \(B\ge r\). Thus the exact feasibility probability is the corresponding upper binomial tail (or zero). This exhibits a residue-dependent jump in the usefulness of one-unit budgets.

## Assumptions and scope
Each good is indivisible and allocated to exactly one agent; empty bundles are allowed. An agent's value for a bundle is the sum of the common item values. An outcome consists of an allocation \((X_i)\) and payments \((p_i)\), where \(p_i>0\) means agent \(i\) receives money and \(p_i<0\) means she pays money. Feasibility requires \(\sum_i p_i=0\) and \(p_i\ge-b_i\) for every \(i\). Envy-freeness compares \(v(X_i)+p_i\) with \(v(X_j)+p_j\) for all ordered pairs \((i,j)\). There are no upper bounds on receipt of transfers. Budgets and item values are integers; transfers may be rational. The denominator \(h\) is an item value, not the number of agents.

## Proof
**Step 1 (equal effective utility).** Identical valuations make envy-freeness in both directions between every pair equivalent to equality of effective utilities: \(v(X_i)+p_i=v(X_j)+p_j\). Summing, using complete allocation and zero-sum payments, forces every effective utility to equal \(\mu=W/n\). Conversely setting \(p_i=\mu-v(X_i)\) gives zero-sum payments and envy-freeness for any complete allocation. Such transfers respect agent \(i\)'s budget precisely when \(v(X_i)\le\mu+b_i\); because all possible bundle values are integers, this is equivalent to \(v(X_i)\le\lfloor\mu+b_i\rfloor=q+b_i=c_i\).

**Step 2 (exact packing criterion).** View the \(n\) agents as bins with integer capacities \(c_i\). If \(t\) size-\(h\) goods and \(u\) size-one goods fit, necessarily \(\sum_i\lfloor c_i/h\rfloor\ge t\) and \(\sum_i c_i\ge ht+u=W\). Conversely, under these two inequalities, assign the \(t\) large goods among the bins, using at most \(\lfloor c_i/h\rfloor\) large goods in bin \(i\); this can be done greedily. The residual **integer** capacity is \(\sum_i c_i-ht\ge u\), so allocate all \(u\) unit goods greedily into those remaining slots. The resulting complete allocation and Step 1 transfers are feasible. Since \(\sum_i c_i=nq+\sum_i b_i\), the total-capacity inequality is exactly \(\sum_i b_i\ge r\).

**Step 3 (sharp minimum aggregate budget).** Put \(g=\lfloor q/h\rfloor\) and \(s=q-hg\). An agent with budget \(b_i\) supplies \(g+\lfloor(s+b_i)/h\rfloor\) size-\(h\) slots. Let \(a_i=\lfloor(s+b_i)/h\rfloor\). If \(a_i\ge1\), then \(b_i\ge ha_i-s\ge(h-s)a_i\), and the same bound trivially holds when \(a_i=0\). Therefore obtaining the additional \(\Delta=\max\{0,t-ng\}\) slots requires \(\sum_i b_i\ge(h-s)\Delta\). Step 2 independently requires \(\sum_i b_i\ge r\). Moreover
\[
\Delta\le\max\{0,(ns+r)/h\}<n
\]
when positive, because \(s\le h-1\) and \(r<n\). Grant \(h-s\) budget units to each of \(\Delta\) distinct agents: each gains one large-good slot, achieving the requisite total of at least \(t\). If necessary add \(r-(h-s)\Delta\) budget units to one agent. This establishes the bound constructively, including when \(\Delta=0\).

**Step 4 (random unit budgets).** If every \(b_i\in\{0,1\}\), a one-unit increment crosses a multiple of \(h\) in \(q+b_i\) precisely when \(s=h-1\). Hence the total number of large-good slots is either \(H_0+B\) in that residue class or exactly \(H_0\) otherwise. Combine with the necessary and sufficient total budget threshold \(B\ge r\); independence yields the stated binomial tails.

## Verification
Run `python3 check.py` in the same directory. The standard-library-only verifier independently enumerates assignments of large and unit goods into bounded-capacity bins and compares with both inequalities on 11,232 small parameter/budget-vector cases, exhaustive minimum-total-budget checks across 725 budget levels, and 480 exact Bernoulli-enumeration comparisons. The general theorem is established by the preceding construction; the finite enumeration is a cross-check, not the justification for arbitrary \(n,h,t,u\).

For example, take \((n,h,t,u)=(3,3,2,0)\). Then \(q=2\), \(r=0\), and \(B_{\min}=2\), even though total value \(6\) is divisible by \(3\). The equal-total-budget vectors \((1,1,0)\) and \((2,0,0)\) have opposite feasibility outcomes: the first supports loads \((3,3,0)\) and transfers \((-1,-1,2)\), whereas the second has only one bin capable of accepting a size-three good. Under independent unit budgets of probability \(p\), feasibility is exactly \(3p^2-2p^3\). More generally, for \((n,h,t,u)=(4,10,2,0)\), the formula gives \(B_{\min}=10\) although \(r=0\), exhibiting a strict indivisibility-induced liquidity premium.

## Relationship to prior work
Bredereck, Deltl, Inamdar, Jain and Pandey introduce envy-free allocation with budget-balanced, individually constrained payments and show equal effective utilities for identical valuations. Their 2025 workshop version and 2026 extended preprint provide parameterized algorithms for identical valuations with a constant number of good types; neither inspected special-case treatment provides the two-denomination pair of scalar feasibility inequalities, a sharp aggregate-budget formula, or the random one-unit-budget threshold. The present theorem is a closed-form specialization in their model, not a new general complexity result. The packing step is elementary because one denomination is one unit; this is essential and is not claimed for arbitrary two item sizes.

Aziz studies balanced transfers without individual payment ceilings; that does not imply low-budget feasibility. Brustle and collaborators give external-subsidy guarantees, rather than this exact zero-sum heterogeneous-budget criterion. The primary comparison of statements is therefore between general feasibility algorithms or subsidy guarantees and an explicit, sharp, all-population threshold under individual caps.

## Limitations
The result assumes every agent has the **same** additive valuation, every good has value exactly \(1\) or the same integer \(h\), and budgets are nonnegative integers. It does not describe heterogeneous valuations, arbitrary real denominations, additional item denominations, constraints on money **received**, or universal feasibility when budgets are fixed independently of item counts. The 2025 source is dated by a documented public workshop presentation; an earlier public draft may exist. The relationship-to-prior-work assessment is qualified by unindexed or differently phrased results in classical integer bin packing. The mathematical proof is self-contained; independent validation and publication-priority determination have not been performed.

## References
- R. Bredereck, E. Deltl, T. Inamdar, P. Jain and P. Pandey, *Envy-free Allocations with Individual Payments*, M-PREF 2025 workshop paper (Bologna, October 25, 2025), https://events.mpref.org/MPref2025/download/0014.pdf . Expanded preprint arXiv:2610.09610 (October 7, 2026), https://arxiv.org/abs/2610.09610 .
- H. Aziz, *Achieving Envy-freeness and Equitability with Monetary Transfers*, arXiv:2003.08125 (2020); AAAI 2021, https://arxiv.org/abs/2003.08125 .
- J. Brustle, J. Dippel, V. Narayan, M. Suzuki and A. Vetta, *One Dollar Each Eliminates Envy*, arXiv:1912.02797 (2019), https://arxiv.org/abs/1912.02797 .
