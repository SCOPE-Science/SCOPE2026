# A universal extinction-probability threshold for functional-redundancy variance under balancing

## Finding

In a community of \(S\ge F\ge2\) species divided into \(F\) nonempty, disjoint functional groups, suppose each species independently disappears with the same probability \(q\in(0,1)\). A function survives if at least one species in its group survives, and \(Y\) denotes the total number of surviving functions. A *balancing move* replaces two group sizes \(a,b\), where \(1\le a\le b-2\), by \(a+1,b-1\) while holding all other group sizes fixed. For each such move,

\[
\operatorname{Var}(Y_{\rm before})-\operatorname{Var}(Y_{\rm after})
=(1-q)(q^a-q^{b-1})[1-(1+q)(q^a+q^{b-1})].
\]

Thus every individual balancing move has exactly one crossover probability in \((0,1)\), and its effect on variance is determined by the sign of the final bracket. By contrast, every move strictly increases expected surviving functional richness.

Let \(\rho\in(0,1)\) be the unique solution of
\[
\rho(1+\rho)^2=1,
\qquad \rho=0.465571231876768\ldots.
\]
**Sharp universal threshold:** for every pair of integers \(S\ge F\ge2\), and every admissible group-size allocation, balancing to groups whose sizes differ by at most one minimizes \(\operatorname{Var}(Y)\) when \(0<q\le\rho\). The minimizer is unique up to group permutations when \(0<q<\rho\); at the boundary equality with other profiles can occur. The bound is optimal uniformly in \(S,F\): for every \(q>\rho\), the two-group, four-species allocations \((1,3)\) and \((2,2)\) have the reverse variance ordering.

For every *fixed* \(S,F\), sufficiently high extinction probability instead makes the balanced allocation a variance *maximizer*. For example, if \(S\ge4\) and \(q^{S-3}(1+q)^2>1\), every nontrivial balancing move increases variance, so the balanced allocation is the unique maximizer up to permutation whenever nonbalanced allocations exist.

Even at a single fixed \(q,S,F\), balancing can have opposite effects on variance: at \(q=1/2\), with \(S=9,F=3\),
\[
V(1,3,5)-V(2,2,5)=-\frac1{64},\qquad
V(2,4,3)-V(3,3,3)=\frac7{256},
\]
where \(V(s_1,\ldots,s_F)=\operatorname{Var}(Y)\). Both transfers increase \(\mathbb E[Y]\), but the first increases variance and the second decreases it.

## Assumptions and scope

There are finitely many species and precisely \(F\) designated functional groups; every species belongs to exactly one group. Each group has a positive integer size \(s_i\), with \(\sum_{i=1}^F s_i=S\). The species-extinction indicators are mutually independent Bernoulli variables with common extinction probability \(q\). Surviving species fully substitute for one another within a group. The count \(Y\) concerns surviving *group functions*, not abundance, network cascades, or total ecosystem performance. The distribution of \(Y\) is Poisson-binomial, and the claim covers all integer allocations with these constraints.

The boundary cases \(q=0\) and \(q=1\) yield zero variance for all allocations and are not included in strict statements. When \(S=F\) or \(S=F+1\), there is only one allocation up to permutation, so statements comparing distinct profiles are vacuous.

## Proof

Write \(I_i\) for the survival indicator of group \(i\). Since the groups are disjoint and losses are independent, the \(I_i\) are independent Bernoulli variables, with \(\Pr(I_i=0)=q^{s_i}\). Thus
\[
\mathbb E[Y]=\sum_{i=1}^F(1-q^{s_i}),\qquad
V(s_1,\dots,s_F)=\sum_{i=1}^F h_q(s_i),\quad h_q(t)=q^t-q^{2t}.
\]
For a balancing move on \(a,b\), the mean change is
\[
\mathbb E[Y_{\rm after}]-\mathbb E[Y_{\rm before}]
=(1-q)(q^a-q^{b-1})>0.
\]
To compute the variance change, note that
\[
h_q(t+1)-h_q(t)=(1-q)q^t\big((1+q)q^t-1\big).
\]
Subtracting the increments at \(a\) and \(b-1\) and factoring the difference of two squares yields the displayed identity. Since \(a<b-1\) and \(0<q<1\), the factors \(1-q\) and \(q^a-q^{b-1}\) are strictly positive. The function \(q\mapsto(1+q)(q^a+q^{b-1})\) increases strictly from \(0\) to \(4\) on \((0,1)\); consequently its level \(1\) occurs exactly once, and the variance-effect sign changes exactly there.

Because \(a\ge1\) and \(b-1\ge2\),
\[
(1+q)(q^a+q^{b-1})\le q(1+q)^2.
\]
The right side increases strictly from zero to four. For \(0<q<\rho\), every balancing move strictly decreases variance; at \(q=\rho\), every move weakly decreases it. Every integer group-size profile can be transformed into one with sizes differing by at most one by repeated balancing moves (the sum of squared sizes strictly decreases at each nontrivial move). This proves universal minimality and strict uniqueness below the boundary.

For sharpness, use \(a=1,b=3\), for which equality holds in the bound. The exact difference is
\[
V(1,3)-V(2,2)
=q(1-q)^2\bigl[1-q(1+q)^2\bigr].
\]
It is positive for \(q<\rho\), zero at the root, and negative for \(q>\rho\). Thus a larger universal minimization interval is impossible.

For the high-extinction assertion, observe that any move in a profile of total size \(S\), with at least two nonempty groups, satisfies \(a\le S-3\) and \(b-1\le S-2\). Hence \(q^a+q^{b-1}\ge q^{S-3}+q^{S-2}=q^{S-3}(1+q)\). Under the stated sufficient inequality the final bracket in the transfer identity is strictly negative, so each balancing step strictly increases variance. The sufficient inequality holds for all \(q\) sufficiently close to one for each fixed \(S\). Finally, at \(q=1/2\) direct substitution into \(h_q\) gives the two displayed exact contrasts. Their transfer steps occur in communities with the same \(S,F\), proving nonuniformity of the variance order beyond the universal threshold.

## Verification

Run \(\texttt{python3 CHECK.py}\) in a directory containing the accompanying standalone checker (Python standard library only). It verifies 370 polynomial transfer identities with integer-coefficient polynomial arithmetic, directly enumerates all independent-loss patterns for six group profiles (at most nine species), confirms the exact nine-species contrasts, rationally brackets the root, and checks 1,234 finite balanced-minimum comparisons for small community sizes and two rational extinction probabilities. The universal proof above is algebraic; no finite test is used to infer an infinite assertion.

## Relationship to prior work

Nijs and Impens, *Biological diversity and probability of local extinction of ecosystems*, establish the independent-species-loss function-reliability model, including the probability \(1-q^s\) that a group function is maintained. Fonseca and Ganade, *Species functional redundancy, random extinctions and the stability of ecosystems*, study function-richness expectations and variance under a fixed retained-species count, a distinct sampling regime, and emphasize functional evenness. Thus the Bernoulli survival model, basic reliability formula, and importance of variance are all prior work. The claim here is **only** the complete sign law for a redistribution of group redundancy, the sharp universal probability threshold, and the same-size reversal of variance responses; it does not claim that the underlying probability or elementary moment formulas are new. More general reliability-allocation theory may provide alternative formulations, and historical priority for this particular sign classification has not been independently established.

## Limitations

These results do not cover correlated extinctions, uneven species-specific extinction rates, species belonging to several functions, compensatory changes in survival probabilities, fixed-number species removal without replacement, temporal dynamics, or interaction-mediated coextinction. The high-extinction sufficient condition is not claimed to be necessary for a particular fixed community size. The variance order does not imply a stochastic order of the full surviving-function distribution. Its conservation relevance is a mathematical benchmark for uncertainty of functional richness, not an empirical performance guarantee.

## References

1. I. Nijs and I. Impens, *Biological diversity and probability of local extinction of ecosystems*, Functional Ecology **14** (2000), 46–54, https://doi.org/10.1046/j.1365-2435.2000.00394.x.
2. C. R. Fonseca and G. Ganade, *Species functional redundancy, random extinctions and the stability of ecosystems*, Journal of Ecology **89** (2001), 118–125, https://doi.org/10.1046/j.1365-2745.2001.00528.x.
3. *On optimal grouping and stochastic comparisons for heterogeneous items*, Journal of Multivariate Analysis (2017), https://doi.org/10.1016/j.jmva.2017.06.006 (abstract/accessible landing material checked; full text not inspected).
