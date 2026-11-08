# A sharp seven-species transition in quorum-based functional resilience

## Finding

Suppose a community contains exactly three nonempty, disjoint functional guilds of positive integer sizes \(n_1,n_2,n_3\), with total species richness \(S=n_1+n_2+n_3\). Each species survives an environmental episode independently with the same probability \(p\in(0,1)\). A guild maintains its function if and only if **at least two** members survive. The community meets its functional-resilience target if at least **two of the three** guilds maintain their functions. Write \(R_p(n_1,n_2,n_3)\) for the target probability.

**Sharp minimal allocation switch.** For \(S\le6\), the set of maximizing allocations is independent of \(p\) (and the target is impossible if \(S\le4\)). The first budget with a probability-dependent maximizing allocation is \(S=7\): up to permuting the guilds,
\[
\begin{cases}
(1,3,3),&0<p<\tfrac12,\\
(1,3,3)\text{ and }(2,2,3),&p=\tfrac12,\\
(2,2,3),&\tfrac12<p<1.
\end{cases}
\]
Both competitors are strictly preferable to every other seven-species allocation for \(p\in(0,1)\). Their reliability difference is exactly
\[
R_p(2,2,3)-R_p(1,3,3)=2p^4(1-p)^2(2p-1).
\]

**Infinite-budget structural extension.** For every integer \(S\ge7\), compare the *two-effective-guild* allocation
\[
A_S=\left(1,\left\lfloor\frac{S-1}{2}\right\rfloor,\left\lceil\frac{S-1}{2}\right\rceil\right)
\]
with the *balanced-three-guild* allocation \(B_S\), the positive integer triple of sum \(S\) whose entries differ by at most one. There exist \(\epsilon_S,\delta_S>0\) such that
\[
R_p(A_S)>R_p(B_S)\quad(0<p<\epsilon_S),\qquad
R_p(A_S)<R_p(B_S)\quad(1-\delta_S<p<1).
\]
This extension asserts a strict ranking reversal between these two biologically interpretable allocations; it **does not** assert that they exhaust global optimizers for \(S>7\), nor that their difference has only one root.

## Assumptions and scope

All guilds are disjoint; all species have independent Bernoulli survivals with identical probability \(p\). Within-guild service is a two-survivor quorum, independent of guild size, and the landscape-level target is preservation of at least two of three services. No compensatory species movement, correlated disturbances, unequal viability, overlapping species guilds, or interaction capacities are modeled. Allocations are unordered positive triples of fixed total \(S\). The theorem concerns the **probability** of meeting the two-service target, not expected function count or variance. Every strict comparison is for \(0<p<1\); endpoint ties are excluded from uniqueness statements.

## Proof

Let \(r_n(p)\) be the probability that a guild of \(n\) species retains at least two survivors. Independence gives
\[
r_n(p)=\sum_{j=2}^n\binom njp^j(1-p)^{n-j}
=1-(1-p)^n-np(1-p)^{n-1}
\]
for \(n\ge1\), with \(r_1=0\). For three independent guild-function indicators with respective success probabilities \(r_a,r_b,r_c\), elementary inclusion-exclusion yields
\[
R_p(a,b,c)=r_ar_b+r_ar_c+r_br_c-2r_ar_br_c.\tag{1}
\]
This is a polynomial identity, so the comparisons below are exact over the entire continuous probability interval.

**The sharp finite boundary.** At most four species cannot supply two distinct guilds with two survivors each. For \(S=5\), the only positive-reliability allocation is \((1,2,2)\); \((1,1,3)\) has reliability zero. For \(S=6\), compare \((2,2,2)\), \((1,2,3)\), and \((1,1,4)\). The last has reliability zero, and
\[
R_p(2,2,2)-R_p(1,2,3)=2p^5(1-p)>0.
\]
For \(S=7\), the four unordered allocations are \((1,1,5),(1,2,4),(1,3,3),(2,2,3)\). The first has reliability zero. The two necessary comparisons factor as
\[
R_p(1,3,3)-R_p(1,2,4)=p^4(1-p)(3-p)>0,
\]
\[
R_p(2,2,3)-R_p(1,3,3)=2p^4(1-p)^2(2p-1).
\]
Finally, the remaining nonzero suboptimal competitor is dominated by the second contender too, since
\[
R_p(2,2,3)-R_p(1,2,4)=p^4(1-p)(1+5p-4p^2)>0\quad(0<p<1).
\]
Consequently the sign changes exactly once at \(p=1/2\), with the stated maximizing allocations and no earlier size-dependent switch. The equation \(R_p(1,3,3)=R_p(2,2,3)\) has no other solutions in \((0,1)\).

**Every larger budget admits a strict ranking reversal.** Set \(A_S=(1,a,b)\) with \(a\le b\) and \(B_S=(c,d,e)\) with \(c\le d\le e\). Let \(h(n)=\binom n2\). As \(p\downarrow0\),
\[
r_n(p)=h(n)p^2+O(p^3),
\]
so (1) gives
\[
R_p(A_S)-R_p(B_S)=\Delta_Sp^4+O(p^5),
\]
where
\[
\Delta_S=h(a)h(b)-h(c)h(d)-h(c)h(e)-h(d)h(e).
\]
To verify \(\Delta_S>0\) for every \(S\ge7\), write \(S=6k+r\), \(0\le r\le5\). Direct substitution and polynomial factorization give the six exact expressions:

| \(r\) | \(\Delta_{6k+r}\) |
|---|---|
| \(0\) | \(3k(k-1)(11k^2-9k+2)/4\) |
| \(1\) | \(k^2(33k^2-38k+13)/4\) |
| \(2\) | \(k^2(33k^2-16k-5)/4\) |
| \(3\) | \(3k^2(11k^2+2k-1)/4\) |
| \(4\) | \(k(3k+2)(11k^2+2k-1)/4\) |
| \(5\) | \(k(3k+1)(11k^2+13k+4)/4\) |

For \(S\ge7\) one has \(k\ge1\), except that \(r=0\) requires \(k\ge2\). Every displayed expression is then strictly positive: the quadratic factors are positive at their smallest permitted integer and increasing thereafter. Thus \(A_S\) strictly wins for sufficiently small positive \(p\).

For survival close to one, let \(q=1-p\). A guild of \(n\ge2\) loses its service with probability
\[
f_n(q)=q^{n-1}\bigl(n-(n-1)q\bigr).
\]
For \(A_S=(1,a,b)\), since the singleton cannot maintain function, the event of meeting the two-function target requires both remaining guilds to succeed. Its failure probability is
\[
1-R_p(A_S)=f_a+f_b-f_af_b=\Theta(q^{a-1}).
\]
For the balanced triple, failure of the two-function target requires at least two guild failures and therefore
\[
1-R_p(B_S)=f_cf_d+f_cf_e+f_df_e-2f_cf_df_e
=\Theta(q^{c+d-2}).
\]
For every \(S\ge8\), the elementary floor/ceiling formulas give \(c+d-2>a-1\). Hence \(B_S\) has strictly smaller failure probability for all sufficiently small \(q>0\), proving the opposite ranking near \(p=1\). At \(S=7\), the exponents coincide; \(1-R_p(A_7)\sim6q^2\) while \(1-R_p(B_7)\sim4q^2\), again favoring \(B_7\). This completes the proof of both assertions.

## Verification

The accompanying Python program `verify.py` uses only the standard library. It independently sums the exact Bernoulli probability polynomial over each of the \(2^S\) survivor subsets for all eleven unordered three-guild allocations with \(3\le S\le7\). It compares these polynomials with (1), checks each critical factorization, and evaluates the six-residue leading-coefficient and exponent inequalities at 294 additional integer budgets. The finite checks reproduce the algebra; the proof of the unbounded budget assertion is the six-residue polynomial argument and exponent comparison above, **not** the bounded numerical loop. Run `python3 verify.py`; the expected output starts with `PASS:`.

## Relationship to prior work

Nijs and Impens explicitly model functional redundancy and functions requiring a minimum number of surviving species; their worked quorum extension analyzes reliability for a **single** guild, not optimization of a two-of-three guild-level target over all positive integer allocations. Fonseca and Ganade analyze random loss of functional groups and the species-to-function richness curve, with group presence defined by at least **one** surviving representative and a fixed-count removal model. Neither directly implies the strict seven-species global optimum switch in the two-quorum, two-service setting.

The same survival event can be represented as a two-stage coherent reliability system. Hwang studies assignment of **heterogeneous component reliabilities to fixed-size subsystems**; that problem does not itself select the three integer guild sizes under equal component survival probability. Ding, Fang and Zhao study grouped \(k\)-out-of-\(n\) reliability and component selection strategies. Their accessible abstract is structurally relevant, but a full-text implication comparison could not be completed; this is a genuine historical-priority limitation, not evidence of novelty. The theorem is not presented as a new probability-calculus technique: its proposed contribution is the sharp ecology-motivated allocation boundary and an all-budget reversal mechanism.

## Limitations

The result is a theoretical comparison within an idealized independent and homogeneous species-loss model, not a prediction for observed ecosystems. The seven-species result is a complete classification only for this precise target and allocation class; for larger budgets the theorem establishes a pairwise ranking reversal but does not classify every optimizer or every crossing. Stronger prior results for general hierarchical system reliability may imply this result despite not stating the same ecological wording. Historical originality therefore remains provisional pending independent literature review and access to the full Ding–Fang–Zhao paper. Independent scientific validation has not been performed.

## References

1. Nijs, I., and Impens, I. *Biological diversity and probability of local extinction of ecosystems*. Functional Ecology 14, 46–54 (2000), first accessible publication date reported as 2001-12-25. DOI: https://doi.org/10.1046/j.1365-2435.2000.00394.x. Full HTML sections inspected, including “Functions that require more than one species.”
2. Fonseca, C. R., and Ganade, G. *Species functional redundancy, random extinctions and the stability of ecosystems*. Journal of Ecology 89, 118–125 (2001). DOI: https://doi.org/10.1046/j.1365-2745.2001.00528.x. Full HTML model and discussion inspected.
3. Hwang, F. K. *Optimal Assignment of Components to a Two-Stage k-Out-of-n System*. Mathematics of Operations Research 14, 376–382 (1989). DOI: https://doi.org/10.1287/moor.14.2.376. Abstract and problem statement inspected; full text not obtained.
4. Ding, W., Fang, R., and Zhao, P. *Reliability analysis of k-out-of-n systems based on a grouping of components*. Advances in Applied Probability 51, 339–357 (2019). DOI: https://doi.org/10.1017/apr.2019.22. Abstract and bibliography inspected; full text not obtained.
