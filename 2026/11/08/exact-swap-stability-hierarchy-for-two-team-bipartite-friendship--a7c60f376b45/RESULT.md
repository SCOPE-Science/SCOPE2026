# Exact swap-stability hierarchy for two-team bipartite friendship games

## Finding

Let two **named** teams have fixed capacities \(s\ge t\ge1\), and let \(a\ge1\) type-\(A\) and \(b\ge1\) type-\(B\) agents satisfy \(a+b=s+t\). Two agents value one another at \(1\) if and only if they have opposite types, and at \(0\) otherwise. Their utilities are sums of the values of their teammates. Write \(x\) for the number of type-\(A\) agents in the size-\(s\) team and \(d=s-t\). The feasible integers are
\[
L=\max\{0,a-t\}\le x\le U=\min\{a,s\}.
\]

For a team assignment, distinguish (i) **strict swap stability** (SSS), which forbids a swap that strictly benefits both swapped agents; (ii) **swap stability** (SS), which forbids a swap that strictly benefits at least one while weakly benefiting the other; and (iii) **transferable-utility swap stability** (SSTU), which forbids a swap increasing the *sum of the swapped agents' utilities*. Their exact occupancy criteria are:

- **SSS:** \(a-1\le2x\le a+d+1\).
- **SS:** if \(d=0\), the SSS condition; if \(d>0\), the strict inequalities \(a-1<2x<a+d+1\).
- **SSTU:** precisely the maximizers over feasible integers of
  \[
  W(x)=2\{x(s-x)+(a-x)(t-a+x)\}.
  \]
  Equivalently, choose the feasible integer(s) nearest to \(\mu=(2a+d)/4\). These are exactly the socially optimal assignments.

For each stability notion \(\mathcal S\), the **exact number of assignments of individually labeled agents to the two named teams** is
\[
N_{\mathcal S}(s,t,a,b)=\sum_{\substack{x\in\mathbb Z,\ L\le x\le U\\x\text{ satisfies }\mathcal S}}\binom ax\binom b{s-x}.
\]
For equal capacities, all three stability notions and social optimality coincide. Unequal capacities create sharp distinctions: the smallest SSS assignment that is not SS has \(3\) agents, while the smallest SS assignment that is not SSTU has \(5\) agents. At \((s,t,a,b)=(2,1,1,2)\) the SSS, SS, and SSTU assignment counts are \((3,2,2)\). At \((4,1,2,3)\) they are \((5,5,3)\), and the inefficient SS occupancy has welfare \(6\) versus optimum \(8\).

## Assumptions and scope

Teams are distinct and named even if their capacities are equal; agents are individually labeled within their types. No coalitions other than these two teams are allowed. Each agent has binary, symmetric, additive utility from its teammates, with the complete bipartite friendship graph \(K_{a,b}\). An admissible deviation exchanges one agent from each team; no transfers of utility are physically required for SSTU, which is the named sum-improvement criterion. All positive integers \(s,t,a,b\) satisfying the displayed constraints are covered. Equality in each gain inequality matters and is treated explicitly.

## Proof

**Occupancy reduction.** Both teams' type counts are determined by \(x\): the first contains \(x\) type-\(A\) and \(s-x\) type-\(B\) agents; the second contains \(a-x\) type-\(A\) and \(t-a+x\) type-\(B\) agents. A swap of same-type agents leaves all utilities unchanged. Only two directed opposite-type swaps need examination.

**Exact gain table.** If a type-\(A\) member of team 1 swaps with a type-\(B\) member of team 2, then \(x\) decreases by one. The gains for the moving \(A\) and \(B\) agents are respectively
\[
\Delta_A^-=2x-a-d-1,\qquad \Delta_B^-=2x-a-1.
\]
If a type-\(B\) member of team 1 swaps with a type-\(A\) member of team 2, then \(x\) increases by one. Their respective gains are
\[
\Delta_B^+=a-2x-1,\qquad \Delta_A^+=a+d-2x-1.
\]
The first swap is available only if \(x>L\), and the second only if \(x<U\). At the inaccessible endpoints, the corresponding strict improvement inequalities cannot hold: when \(x=L\), one has \(2x\le a+d+1\), and when \(x=U\), one has \(2x\ge a-1\). The other gain criteria similarly cannot spuriously exclude an unavailable swap.

**SSS and SS.** For both participants to gain strictly, the decreasing swap requires \(2x>a+d+1\), and the increasing swap requires \(2x<a-1\). This yields the closed SSS interval. For the weakly-improving-partner criterion, if \(d>0\), the two changes within each swap differ by the positive amount \(d\), so a swap is improving already when \(2x\ge a+d+1\) or \(2x\le a-1\). If \(d=0\), each pair's gains are identical; at equality both are zero, not an improvement. This yields the SS cases stated.

**Transferable utility and welfare.** Total welfare is \(W(x)\) because every same-team cross-type friendship contributes one unit to each endpoint. The sum of the two moving agents' gains for a decreasing swap is \(4x-2a-d-2\), and for an increasing swap it is \(2a+d-4x-2\). Direct expansion shows
\[
W(x-1)-W(x)=2(4x-2a-d-2),\qquad
W(x+1)-W(x)=2(2a+d-4x-2).
\]
The welfare is a strictly concave quadratic with
\[
W(x)=W(\mu)-4(x-\mu)^2,\qquad \mu=(2a+d)/4,
\]
where the expression at real \(\mu\) denotes the polynomial extension. Hence a feasible integer assignment has no adjacent welfare-improving step if and only if it globally maximizes welfare. This is exactly SSTU. The maximizing integers are the feasible integer(s) closest to \(\mu\).

**Counts and sharp minima.** At occupancy \(x\), independently choose the \(x\) of the \(a\) labeled type-\(A\) agents and the \(s-x\) of the \(b\) labeled type-\(B\) agents in team 1; all others must join team 2. This proves the sum. At equal capacities \(d=0\), the SSS closed interval consists exactly of the feasible integers nearest to \(a/2=\mu\); all three sets coincide. For populations of size at most four, the only unequal capacity pairs with at least one agent in each team are \((2,1)\) and \((3,1)\); direct substitution into the exact inequalities gives \(\mathrm{SS}=\mathrm{SSTU}\) for every possible \(a\). The first SSS/SS difference is \((2,1,1,2)\), where occupancies \(0,1\) are SSS but only \(1\) is SS. The first SS/SSTU difference is \((4,1,2,3)\): occupancies \(1,2\) are SS, but only \(2\) is SSTU. The other capacity partition at size four is equal-capacity, already covered. Thus the two claimed minima are sharp.

## Verification

Run `python3 verify.py` using only the Python standard library. The checker constructs every labeled two-team assignment for all \(155\) parameter triples with total population \(2\) through \(10\), positive numbers of both types, and \(s\ge t\). It directly computes the utilities of all individually labeled agents and every cross-team pairwise swap; it tests each of the three definitions against the closed-form criteria and checks the binomial multiplicities. The included checker passed \(9{,}588\) complete labeled assignments. These finite checks supplement but do not replace the preceding all-parameter proof.

## Relationship to prior work

Bilò, Monaco and Moscardelli (2022) define the three swap-stability notions for symmetric additively separable hedonic games with fixed-size coalitions, prove broad existence and convergence facts, and derive general efficiency bounds. The result here restricts the friendship network to \(K_{a,b}\) and the number of named teams to exactly two, but determines **every** equilibrium of all three notions, counts labeled equilibria, identifies the exact welfare optimizers, and gives sharp first separations of the three equilibrium sets. The general existence and broad price-of-anarchy results alone do not supply these exact occupancy and multiplicity formulas. The stronger source-comparison limitation is stated below.

## Limitations

Only complete bipartite binary friendship graphs with two fixed teams are considered. Different group sizes or additional teams are not covered by these formulas. An equivalent published specialization may be unindexed. Parts of the initiating paper's full text were unavailable to the literature comparison despite successful inspection of its introduction, stated contributions, formal definitions, and accessible opening pages; its uninspected technical sections remain a specific priority risk. No inference about all possible literature or independent validation is made.

## References

- Bilò, V., Monaco, G., and Moscardelli, L. (2022). *Hedonic Games with Fixed-Size Coalitions*. AAAI, 9287–9295. DOI: https://doi.org/10.1609/aaai.v36i9.21156 ; proceedings PDF: https://ojs.aaai.org/index.php/AAAI/article/download/21156/20905 . Public AAAI presentation dated 2022-02-24: https://aaai-2022.virtualchair.net/poster_aaai1121 .
- Bullinger, M., Dunajski, A., Elkind, E., and Gilboa, M. (2025). *Single-Deviation Stability in Additively Separable Hedonic Games with Constrained Coalition Sizes*. https://arxiv.org/abs/2510.12641 . This concerns single-agent moves under size bounds rather than the two-agent exchange classification here.
- Gairing, M., and Savani, R. (2019). *Computing Stable Outcomes in Symmetric Additively Separable Hedonic Games*. Mathematics of Operations Research 44, 1101–1121. https://doi.org/10.1287/moor.2018.0960 .
