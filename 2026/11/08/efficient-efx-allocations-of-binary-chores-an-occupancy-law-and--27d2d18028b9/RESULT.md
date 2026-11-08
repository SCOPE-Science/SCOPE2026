# Efficient EFX allocations of binary chores: an occupancy law and a free-chore parity reversal

## Finding

**Exact occupancy theorem.** Fix an integer \(n\geq2\), integers \(u\geq0\) and \(h_1,\ldots,h_n\geq0\). There are \(u\) individually distinguishable *common* chores of cost \(1\) to every agent. In addition, agent \(i\) has \(h_i\) individually distinguishable *private-zero* chores: each has cost \(0\) to agent \(i\) and cost \(1\) to every other agent. Every item is assigned to exactly one agent, and costs are additive. Write \(e_i=1\) if \(h_i=0\), and \(e_i=0\) otherwise.

A complete allocation is Pareto optimal (PO), or fractionally Pareto optimal (fPO), **if and only if** every private-zero chore is assigned to its zero-cost agent. Among these allocations, let \(c_i\) denote the number of common chores assigned to agent \(i\). The allocation satisfies envy-freeness up to *any* owned chore (EFX), including zero-cost owned chores, **if and only if**

\[
 c_i-e_i\leq c_j+h_j\qquad\text{for every }i\ne j.
\]

Consequently the exact number of labeled allocations satisfying both EFX and PO (equivalently, EFX and fPO) is

\[
 N_n(\mathbf h,u)=
 \sum_{\substack{c_1,\ldots,c_n\geq0,\ \sum_i c_i=u\\
                   c_i-e_i\leq c_j+h_j\ (i\ne j)}}
 \frac{u!}{c_1!\cdots c_n!}.
\]

There are exactly \(n^u\) PO/fPO allocations in this instance.

**Sharp monotonicity reversal.** For two agents and \(u\geq1\), adding one private-zero chore for agent 1 to an instance containing only \(u\) common chores has opposite effects according to parity. If \(u=2m+1\), the count changes from \(2\binom{2m+1}{m}\) to \(\binom{2m+1}{m}\): the new, zero-cost-to-its-recipient chore **halves** the number of EFX–fPO allocations. If \(u=2m\) with \(m\geq1\), the count instead increases from \(\binom{2m}{m}\) to \(\binom{2m}{m}+\binom{2m}{m-1}\). These statements apply to all positive odd and even \(u\), not just a finite search.

**Prevalence threshold.** If \(h_1=\cdots=h_n=h\geq1\), EFX–fPO is exactly the occupancy-range condition

\[
 \max_i c_i-\min_i c_i\leq h.
\]

Uniformly sample one of the \(n^u\) efficient allocations. For fixed \(n\ge2\), if \(h=h(u)\ge1\) and \(h/\sqrt u\to\lambda\in[0,\infty)\), the probability of EFX tends to

\[
 F_n(\sqrt n\,\lambda),\qquad
 F_n(t)=n\int_{-\infty}^{\infty}\phi(x)
       \bigl(\Phi(x+t)-\Phi(x)\bigr)^{n-1}\,dx,
\]

where \(\phi,\Phi\) are the standard normal density and distribution function. The limit is \(0\) for \(h=o(\sqrt u)\) and \(1\) for \(h/\sqrt u\to\infty\); for \(0<\lambda<\infty\) it lies strictly between \(0\) and \(1\). Thus \(\sqrt u\) is the precise scale on which private-zero chores make EFX typical among efficient assignments.

For completeness, if \(h\ge1\) is fixed, \(u=nm+r\), \(0\le r<n\), and

\[
 \mathcal D_{n,r,h}=\{\mathbf d\in\mathbb Z^n:
 \sum_i d_i=r,\ \max_i d_i-\min_i d_i\le h\},
\]

then along this residue class,

\[
 \frac{N_n((h,\ldots,h),u)}{n^u}
 \sim |\mathcal D_{n,r,h}|\,
 \frac{n^{n/2}}{(2\pi u)^{(n-1)/2}}.
\]

In particular, uniformly adding one private-zero chore to **every** agent leaves the EFX–fPO count exactly unchanged from the instance with no private-zero chores: both have \(\max_i c_i-\min_i c_i\le1\).

## Assumptions and scope

The agents and chores are labeled. An item's cost is precisely \(0\) or \(1\), as specified above; there are no transfers, capacities, partial allocations, unequal entitlements, or random valuations. **PO** excludes integral Pareto improvements; **fPO** excludes even fractional Pareto improvements. Under chore EFX, for every pair of distinct agents \(i,j\) and **every** item \(g\) in \(i\)'s own bundle, agent \(i\)'s cost after removing \(g\) must not exceed the cost of agent \(j\)'s entire bundle as evaluated by \(i\). Zero-cost items are included in this quantifier. Empty own bundles satisfy EFX vacuously. The asymptotic assertions keep \(n\) fixed as \(u\to\infty\).

## Proof

**1. Efficiency.** If a private-zero item for agent \(i\) is assigned to any other agent \(j\), move that item from \(j\) to \(i\). Agent \(j\)'s cost strictly decreases by \(1\), while agent \(i\)'s cost is unchanged. Therefore no PO allocation misassigns a private-zero item. Conversely, assigning every such item to its designated agent realizes total social cost exactly \(u\), the absolute lower bound because every common chore has cost \(1\) no matter who receives it. A fractional allocation also has total cost at least \(u\); an improvement in at least one cost with no deterioration in any cost would contradict this lower bound. Thus these and only these allocations are simultaneously PO and fPO.

**2. EFX residual.** Under efficiency, agent \(i\)'s own cost equals \(c_i\), while her cost assessment of agent \(j\)'s bundle equals \(c_j+h_j\) for \(i\ne j\). If \(h_i>0\), removing one of her own zero-cost items leaves cost \(c_i\), which is the largest possible residual over removal of any owned item. If \(h_i=0\) and \(c_i>0\), removing any owned item leaves \(c_i-1\); if \(h_i=c_i=0\), there is no removal requirement. This is equivalent for every distinct pair to \(c_i-e_i\le c_j+h_j\), even when \(c_i=0\) because then the inequality with \(e_i=1\) holds automatically.

**3. Enumeration.** For a fixed nonnegative common-item occupancy vector \(\mathbf c\) of sum \(u\), each private-zero chore has its uniquely prescribed owner. The \(u\) labeled common chores can be assigned with exactly \(u!/(c_1!\cdots c_n!)\) choices. Summing over precisely the vectors characterized in Step 2 proves the exact census. With no fairness restriction, each common chore has \(n\) choices, giving \(n^u\).

**4. Two-agent parity reversal.** If \((h_1,h_2)=(0,0)\), the two inequalities are \(c_1-c_2\le1\) and \(c_2-c_1\le1\). If \((h_1,h_2)=(1,0)\), they are \(c_1\le c_2\) and \(c_2-1\le c_1+1\). Writing \(c_1=x\), \(c_2=u-x\), the latter become \(u-2\le2x\le u\). Counting the permitted integer values of \(x\) and the corresponding labeled subsets gives the stated odd and even formulas, including the boundary \(u=1\).

**5. Symmetry and Gaussian scaling.** For \(h_i=h\ge1\), every \(e_i=0\), so the EFX inequalities assert exactly \(\max_i c_i-\min_i c_i\le h\). Under uniform efficient allocation, the random common occupancies have the multinomial distribution \(\operatorname{Multinomial}(u;1/n,\ldots,1/n)\). The multinomial central limit theorem gives

\[
 \frac{(c_1-u/n,\ldots,c_n-u/n)}{\sqrt u}
 \Rightarrow
 \frac{(G_1-\overline G,\ldots,G_n-\overline G)}{\sqrt n},
\]

where the \(G_i\) are independent standard normals and \(\overline G\) is their mean. The range of this limiting vector is \((\max_i G_i-\min_i G_i)/\sqrt n\). Its distribution is continuous; conditioning on the unique minimum of \(n\) independent standard normals yields the displayed integral for \(F_n\). The continuous mapping theorem gives the finite-\(\lambda\) limit, including \(\lambda=0\). For diverging \(h/\sqrt u\), Chebyshev's inequality and a union bound on pairwise differences (each having variance \(2u/n\)) give probability tending to \(1\).

**6. Fixed-width local limit.** With \(u=nm+r\), each admissible occupancy has the form \(c_i=m+d_i\), with \(\mathbf d\in\mathcal D_{n,r,h}\). This set is finite and independent of \(u\). By Stirling's formula, for each of its vectors,

\[
 \frac{u!}{n^u\prod_i(m+d_i)!}
 \sim\frac{n^{n/2}}{(2\pi u)^{(n-1)/2}}.
\]

Summing over the finite set proves the fixed-width asymptotic. Finally, without private-zero chores all residual paid costs are \(c_i-1\), which yields the range bound \(1\); the same bound applies for exactly one private-zero chore per agent, proving the stated plateau.

## Verification

Run `python3 verification.py` using Python 3's standard library only. It enumerates all complete allocations independently of the occupancy formula, computes their agents' cost vectors, eliminates Pareto-dominated vectors, and directly tests EFX for every owned chore—including zero-cost chores. It verifies **174** small instances comprising **81,620** complete labeled allocations. It additionally verifies the two-agent parity formulas for \(1\le u\le8\) and compares the general counting formula with the symmetric occupancy formula in **176** parameter combinations. The finite checks do not prove the general theorem; Steps 1–6 supply the infinite proof.

## Relationship to prior work

Tao, Wu, Yu and Zhou, *On the Existence of EFX (and Pareto-Optimal) Allocations for Binary Chores* (2023), introduce the binary-cost EFX/PO framework and prove guaranteed existence with a constructive algorithm. Their EFX definition includes removal of zero-cost chores. The present result **does not claim** a new existence theorem: it specializes to a balanced private-zero/common-cost family and gives the exact set and number of efficient EFX allocations and their prevalence.

Lin, Wu and Zhou, *Revisiting EFX and fPO Allocations for Binary Chores* (2026), prove stronger existence guarantees with weighted entitlements and explicitly note that an owned zero-cost chore can strengthen EFX to EF. That observation is correctly credited here; it does not itself give the precise parity reversal, the all-parameter occupancy count, or the Gaussian prevalence threshold. Neoh and Teh, *Understanding EFX Allocations: Counting and Variants* (2025), provide independent motivation for counting fair allocations but study EFX of goods, not this chore instance. He and Tao (2026) study existence and incompatibility for more general positive-valued chores, not the present binary count.

## Limitations

The count is specific to one common unit-cost class and private-zero items uniquely assigned to zero-cost agents in every efficient outcome; it makes no claim for arbitrary binary cost matrices or weighted EFX. The free-item count comparison changes the item universe, and is about the number of labeled outcomes, not the probability under a uniform distribution on *all* allocations. The Gaussian limit assumes a fixed number of agents. Searches and inspected sources revealed no equivalent exact census, but cannot establish global publication priority or eliminate unindexed literature. The result has not undergone independent external audit.

## References

1. B. Tao, X. Wu, Z. Yu and S. Zhou, *On the Existence of EFX (and Pareto-Optimal) Allocations for Binary Chores*, first version August 23, 2023, arXiv:2308.12177v1. https://arxiv.org/html/2308.12177v1
2. Z. Lin, X. Wu and S. Zhou, *Revisiting EFX and fPO Allocations for Binary Chores*, September 12, 2026, arXiv:2609.13970v1. https://arxiv.org/abs/2609.13970
3. T. Y. Neoh and N. Teh, *Understanding EFX Allocations: Counting and Variants*, April 4, 2025, arXiv:2504.03951v1. https://arxiv.org/abs/2504.03951
4. W. He and B. Tao, *EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence*, June 7, 2026, arXiv:2606.08872v1. https://arxiv.org/abs/2606.08872
