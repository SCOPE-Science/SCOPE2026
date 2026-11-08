# Exact four-to-five-good feasibility transitions for two-center delegated fairness

## Finding

Consider two centers, each with two lower-level agents, and a complete allocation of indivisible goods. Every agent has the same strictly positive additive singleton values. Require **inter-EF1** among all four agents and **EFX** between the two centers, where a center values a collection of goods by their total common value. This is the common-valuations specialization of all four standard potential/realized, item-/bundle-based center conventions.

Let \(F_m\) denote existence of an allocation satisfying both requirements with \(m\) goods. Writing the positive values in descending order, the exact feasibility criteria for the first two potentially obstructed sizes are

\[
\begin{aligned}
F_4&\iff a\le b+c,&&a\ge b\ge c\ge d>0,\\
F_5&\iff a\le b+c+e,&&a\ge b\ge c\ge d\ge e>0.
\end{aligned}
\]

For at most three goods a jointly fair allocation always exists. When a fifth positive good is appended to four, feasibility can both appear and disappear. **Disappearance is possible only if the appended good is at least as large as the previous maximum**; in particular, adding a strictly submaximum good cannot destroy feasibility. Both transitions occur for distinct positive values.

Suppose five valuations are sampled independently from one common continuous distribution, with the fifth sampled value interpreted as the added resource. For \(u,v\in\{0,1\}\), let \(p_{uv}=\Pr(F_4=u,F_5=v)\). The full joint laws are

| Value law | \(p_{00}\) | \(p_{01}\) (rescue) | \(p_{10}\) (loss) | \(p_{11}\) |
| --- | ---: | ---: | ---: | ---: |
| Uniform\((0,1)\) | \(3/40\) | \(7/40\) | \(1/120\) | \(89/120\) |
| Exponential, any positive rate | \(41/105\) | \(22/105\) | \(4/105\) | \(38/105\) |

Thus \(\Pr(F_4)=3/4\), \(\Pr(F_5)=11/12\) for uniform values, versus \(\Pr(F_4)=2/5\), \(\Pr(F_5)=4/7\) for exponential values. These are unconditional joint probabilities, not conditional transition probabilities.

## Assumptions and scope

There are exactly four distinct labeled agents, partitioned into two fixed groups of two. Each good is assigned in its entirety to one agent. The same \(v(g)>0\) applies to every agent, and each agent values a bundle by \(\sum_{g\in B}v(g)\). There are no restrictions on the size of an agent's bundle beyond those forced by fairness.

An allocation is inter-EF1 when, for every ordered pair of agents \(i,j\) with nonempty \(B_j\), some \(g\in B_j\) satisfies \(v(B_i)\ge v(B_j\setminus\{g\})\); comparisons with an empty bundle are automatic. Center-EFX means that for each ordered pair of centers \(C,D\), and **every** item \(g\) held by \(D\), \(v(C)\ge v(D\setminus\{g\})\). Identical agent valuations make the alternative center-valuation conventions coincide with total bundle value. In the probability statements, all draws are independent, and a continuous law ensures unique ranks almost surely.

## Proof

**1. Bundle shapes.** If an agent is empty and another agent holds at least two positive-valued goods, the empty agent envies after any single deletion, violating inter-EF1. Hence for four goods each of the four agents must receive exactly one good. For five goods all agents must be nonempty, and exactly one agent receives a two-good bundle while each remaining agent receives one good. Every one-good-per-agent allocation is inter-EF1. In the five-good case, the two-good bundle \(\{s,t\}\) is compatible with inter-EF1 precisely when each singleton is worth at least \(\min(s,t)\); thus the smallest good can be put in that bundle, swapping equal-valued goods if necessary.

**2. Four goods.** Let \(a\ge b\ge c\ge d>0\). The center containing the largest good \(a\) has two goods. For the other center to be EFX toward it, the other's two goods must have total value at least \(a\) (remove the smaller good from the center holding \(a\)); their sum is at most \(b+c\). Hence \(a\le b+c\) is necessary. Conversely put \(\{a,d\}\) in one center and \(\{b,c\}\) in the other, assigning one good to each agent. The first center has value at least \(b\), while the second has value at least \(a\) by hypothesis. These are the two required EFX comparisons, so the condition suffices.

**3. Five goods.** Write \(a\ge b\ge c\ge d\ge e>0\). Put a minimum good \(e\) in the sole two-good agent bundle. That agent's center holds three goods \(\{s,t,e\}\), with one of \(s,t\) bundled with \(e\), and the other center holds two goods \(\{u,v\}\). The EFX inequalities between centers are exactly

\[
u+v\ge s+t,\qquad s+t+e\ge\max(u,v).
\]

If \(a\in\{u,v\}\), the second inequality yields \(a\le s+t+e\le b+c+e\). If instead \(a\in\{s,t\}\), the first inequality yields \(a\le u+v\le b+c\), proving necessity. For sufficiency, if \(a+d\le b+c\), assign the triple \(\{a,d,e\}\) to one center with \(\{a,e\}\) as the double bundle, and assign \(\{b,c\}\) as singletons to the other. The EFX inequalities follow from \(b+c\ge a+d\) and \(a+d+e\ge b\). Otherwise assign \(\{b,c,e\}\) as the triple with \(\{b,e\}\) doubled, and \(\{a,d\}\) as the other pair. Then \(a+d>b+c\) and \(b+c+e\ge a\) supply the EFX inequalities. Every singleton is worth at least \(e\), so inter-EF1 holds. Ties are allowed.

For \(m\le3\), assign at most one good to each agent; for three goods, put the largest good alone in one center and the next two goods in the other. Both center-EFX and agent inter-EF1 follow directly.

**4. Addition of a good.** If four values \(a\ge b\ge c\ge d\) satisfy \(a\le b+c\), appending any \(t\le a\) retains \(a\) as a largest value and cannot decrease the sum of the second- and third-largest values. Since the new minimum is positive, the five-good inequality holds. Strict witnesses in the other two directions are: the feasible four values \((5,4,3,2)\) become infeasible after appending \(20\); the infeasible four values \((12,6,5,4)\) become feasible after appending \(3\).

**5. Exact random transition.** For five ordered observations \(U_1<\cdots<U_5\), put \(G_i=U_i-U_{i-1}\) with \(U_0=0\). The position \(R\) of the fifth labeled observation among all five is uniform on \(\{1,\ldots,5\}\) and independent of the ordered values. The four-good original sample has the five-good sample with its rank-\(R\) item removed. By Step 4, loss is possible only when \(R=5\). On \(R=5\), four-good feasibility is \(G_4\le G_1+G_2\), and five-good infeasibility is \(G_5>2G_1+G_2+G_3\). Therefore

\[
\Pr(F_4=1,F_5=0)=\frac15\Pr\bigl(G_4\le G_1+G_2,\ G_5>2G_1+G_2+G_3\bigr).
\]

For exponential items of any fixed rate (set the rate to one by scaling), independent ordered gaps have respective rates \((5,4,3,2,1)\). Conditional integration of \(G_4,G_5\) gives

\[
\frac15\left[\frac57\frac45\frac34-\frac59\frac47\frac34\right]=\frac4{105}.
\]

Also \(\Pr(F_4=1)=1-(4/5)(3/4)=2/5\) and \(\Pr(F_5=1)=1-(5/7)(4/5)(3/4)=4/7\).

For uniform \((0,1)\) items, the six spacings (including \(1-U_5\)) have the Dirichlet\((1,1,1,1,1,1)\) law. They equal six independent rate-one exponential variables divided by their common positive sum. All preceding inequalities are homogeneous, so the normalizing sum cancels. The same integration yields

\[
\Pr(F_4=1,F_5=0)=\frac15\left[\frac13\frac12\frac12-\frac14\frac13\frac12\right]=\frac1{120},
\]

and \(\Pr(F_4=1)=1-(1/2)^2=3/4\), \(\Pr(F_5=1)=1-(1/3)(1/2)^2=11/12\).

Finally, for either distribution, \(p_{11}=\Pr(F_4)-p_{10}\), \(p_{01}=\Pr(F_5)-p_{11}\), and \(p_{00}=1-p_{01}-p_{10}-p_{11}\). Substitution gives the complete tables above. The exponential-spacing and uniform-Dirichlet representations hold for all sample sizes specified here, not as approximations.

## Verification

The standalone `verify.py` checks the fairness definitions directly by enumerating all \(4^m\) labeled agent assignments on each test profile, without using the proposed feasibility formulas in the allocation test. It exhausts positive integer multiset profiles with values from \(1\) through \(7\), for \(m=1,2,3,4,5\), respectively \(7,28,84,210,462\) profiles, and checks \(600\) additional seeded positive rational profiles of sizes four and five. The program separately evaluates the exact spacing-Laplace identities using rational arithmetic and confirms the stated transition matrices and deterministic witnesses. Execute `python verify.py` with Python 3; no third-party dependencies or external files are required.

## Relationship to prior work

Deligkas, Fasoulakis, Ioannidis, Mancho, and Markakis (2026, arXiv:2607.27743v1) define the two-level center/agent fairness conventions. Their Theorem 9 gives a four-good impossibility witness with one much more valuable good, and Theorem 10 proves NP-hardness of the general feasibility problem. Neither result states the complete four- and five-good value inequalities or their exact coupled resource-addition probabilities. Scarlett, Teh, and Zick (2023, arXiv:2302.06958) study group-weighted EFX; when group sizes are equal and valuations identical, this has the same group comparison here. Their Proposition 3.2 independently establishes incompatibility by an unbalanced four-good example, not the parameter-space classification or random transition. Lucet, Benabbou, Beynier, and Maudet (2025, arXiv:2512.24105) study a multilevel model with matroid-rank preferences and mainly local hierarchical fairness, rather than this cardinal identical-value joint EFX/inter-EF1 feasibility question.

## Limitations

The classification is restricted to two centers with two agents each, common strictly positive additive values, and four or five goods. It does not cover different agents' valuations, zeros, larger markets, alternative group entitlements, or arbitrary dependence among random values. Uniform and exponential transition matrices are distribution-specific and do not imply universal probabilities. They characterize the existence of a suitable reallocation after adding a good, **not** whether an existing allocation can be maintained without changing prior assignments.

## References

- A. Deligkas, M. Fasoulakis, S. D. Ioannidis, A. Mancho, E. Markakis, *Delegated Fair Division*, first posted July 30, 2026, arXiv:2607.27743v1. https://arxiv.org/abs/2607.27743
- J. Scarlett, N. Teh, Y. Zick, *For One and All: Individual and Group Fairness in the Allocation of Indivisible Goods*, arXiv:2302.06958, first posted February 14, 2023. https://arxiv.org/abs/2302.06958
- M. Lucet, N. Benabbou, A. Beynier, N. Maudet, *Multilevel Fair Allocation*, arXiv:2512.24105, first posted December 30, 2025. https://arxiv.org/abs/2512.24105
