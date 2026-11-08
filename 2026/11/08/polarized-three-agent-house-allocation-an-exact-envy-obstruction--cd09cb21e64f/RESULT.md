# Polarized three-agent house allocation: an exact envy obstruction and stock law

## Finding

Fix an integer \(m\geq3\) and houses \(h_1,\ldots,h_m\). Three agents receive exactly one distinct house each; unused houses are permitted. The first agent strictly prefers \(h_1\succ h_2\succ\cdots\succ h_m\), and the second strictly prefers the reverse order \(h_m\succ\cdots\succ h_1\). The third agent has an arbitrary complete strict ranking \(\pi\).

For a complete assignment \(A\), let \(e_i(A)\) count the other agents whose assigned houses agent \(i\) prefers to her own. Define \(E(A)=\sum_i\mathbf1_{\{e_i(A)>0\}}\) (number of envious agents), \(P(A)=\sum_ie_i(A)\) (number of ordered envy pairs), and \(X(A)=\max_ie_i(A)\) (maximum envy count). Then the *three separate optima* coincide:

\[
\min_AE(A)=\min_AP(A)=\min_AX(A)=
\begin{cases}
0,&\text{if some }i<j<k\text{ have }h_j\succ_\pi h_i\text{ and }h_j\succ_\pi h_k,\\
1,&\text{otherwise.}
\end{cases}
\]

The second case is precisely the set of rankings \(\pi\) that are **single-dipped on the displayed house axis**, equivalently those obtainable by repeatedly taking the leftmost or rightmost remaining house, from most to least preferred. Hence, when \(\pi\) is uniform over the \(m!\) rankings,

\[
\Pr\{\min_AE(A)=\min_AP(A)=\min_AX(A)=1\}=\frac{2^{m-1}}{m!}.
\]

For a coherent growing inventory \(h_1,h_2,\ldots\), keep the opposite orders on every finite prefix, and give the third agent independent atomless utilities over houses. Let \(T\) be the smallest inventory size at which an envy-free assignment of all three agents exists. Then \(T\) is finite almost surely, and for every integer \(m\geq3\),

\[
\Pr\{T=m\}=\frac{2^{m-2}(m-2)}{m!},\qquad
\mathbb ET=\frac{e^2+1}{2},\qquad
\operatorname{Var}(T)=\frac{8e^2+1-e^4}{4}.
\]

Thus the presence or absence of a single perfect assignment, the optimal values of three customary envy measures, and the required number of additional available houses all admit exact descriptions in the polarized case.

## Assumptions and scope

The agents are labeled, houses are distinguishable, and each receives exactly one house. Each ranking is complete, strict, and ordinal; no ties, monetary transfers, or capacity multiplicities are allowed. The first and second agents' orders are deterministic and opposite on the axis, while the third is unrestricted. The probability statement conditions on the two fixed orders and randomizes only the third; it is **not** the probability for three independent random preference rankings. For \(T\), the rankings on finite prefixes must be restrictions of one coherent, countably infinite preference environment. The third agent's independent atomless utilities generate uniform orders on each finite prefix.

## Proof

**1. Envy-free assignment and a middle-first triple.** Consider three selected houses with increasing indices \(i<j<k\). Within this triple, the first agent most prefers \(h_i\), and the second agent most prefers \(h_k\). In any envy-free assignment using these houses, they must receive \(h_i\) and \(h_k\) respectively; the remaining house \(h_j\) must go to the third agent. She experiences no envy exactly when \(h_j\succ_\pi h_i,h_k\). Conversely, whenever this condition holds, the indicated assignment is envy-free. This proves the zero-versus-positive criterion, with all quantifiers ranging over triples of distinct indices.

**2. The one-envy bound, simultaneously for three objectives.** Fix *any* three houses \(h_i,h_j,h_k\) with \(i<j<k\), and let \(f\) be the third agent's favorite of the three. If \(f=h_j\), give \((h_i,h_k,h_j)\) to agents \((1,2,3)\), leaving no envy. If \(f=h_i\), give \((h_j,h_k,h_i)\): only agent 1 envies agent 3. If \(f=h_k\), give \((h_i,h_j,h_k)\): only agent 2 envies agent 3. Every case has at most one ordered envy pair, hence at most one envious agent and maximum envy at most one. If Step 1 rules out envy-freeness, every allocation has at least one ordered envy pair, an envious agent, and a maximum envy count at least one. Therefore all three separate minima equal the indicator stated in the finding. Notice that the construction minimizes the three objectives *simultaneously*.

**3. Characterization of the obstruction.** Call a ranking endpoint-deletable if, read from best to worst, it repeatedly selects an endpoint of the axis interval of remaining houses. If the third agent's highest-ranked house \(h_j\) is interior, the triple \((h_1,h_j,h_m)\) satisfies Step 1. Therefore a ranking without such a triple must take an endpoint first. The no-triple condition remains true on the remaining interval, so induction forces endpoint deletion throughout. Conversely, in any endpoint-deletable ranking, the earliest selected member of any triple \(i<j<k\) must be \(h_i\) or \(h_k\), because both lie in the remaining interval when the first member of the triple is taken. Hence the middle cannot be the third agent's favorite on any triple. This is the strict single-dipped condition with respect to the fixed axis (allowing an endpoint as a dip), proved without appealing to a general domain theorem.

**4. Exact probability.** At each of the first \(m-1\) steps of endpoint deletion there are exactly two distinct endpoint choices; the last house is forced. These \(2^{m-1}\) sequences yield distinct strict rankings, and all such rankings fail the Step 1 criterion. Uniformity over \(m!\) possible third-agent rankings gives the stated probability. The uniform count is conditional on the first two polarized rankings.

**5. First stock size.** The existence event is monotone in inventory size because an earlier envy-free triple can remain assigned when extra houses become available. Put \(q_m=\Pr(T>m)\). For \(m\geq2\) Step 4 gives \(q_m=2^{m-1}/m!\), where \(q_2=1\) also holds because three houses are required. Additionally \(q_0=q_1=1\). Thus for \(m\geq3\),

\[
\Pr(T=m)=q_{m-1}-q_m=\frac{2^{m-2}(m-2)}{m!}.
\]

The tails tend to zero, establishing almost sure finiteness. The tail-sum identities for a positive integer-valued variable give

\[
\mathbb ET=\sum_{m\geq0}q_m=2+\frac12(e^2-3)=\frac{e^2+1}{2},
\]

\[
\mathbb ET^2=\sum_{m\geq0}(2m+1)q_m
=4+\frac12(5e^2-7)=\frac{5e^2+1}{2}.
\]

Subtracting \((\mathbb ET)^2\) gives the displayed variance. All infinite sums converge absolutely by factorial decay.

## Verification

The included `check.py` independently enumerates every third-agent permutation for \(3\leq m\leq8\), every possible injective three-house assignment, and the three envy objectives. It compares the exact minima with a separately implemented endpoint-deletion predicate, and counts the profiles whose first successful prefix is of length \(m\). The tests cover \(6,24,120,720,5040,40320\) rankings, respectively. Every tested count is exactly \(2^{m-1}\) obstructed rankings and \(2^{m-2}(m-2)\) first-success rankings. Run `python3 check.py` from a directory containing the included source. These finite tests check implementation and small cases; the all-\(m\) result follows from the five mathematical steps above, not from finite enumeration.

## Relationship to prior work

Hosseini, Roy, and Sethia (arXiv:2511.07022v1, Section 4.2, Lemma 4.10) prove that a profile which is globally single-dipped on one axis has at most two envy-free agents. Since the two polarized orders are also single-dipped, their lemma already **implies the obstruction half** of the present special case when the third ranking is single-dipped. The new assertion is the **sharp converse under two opposite rankings**, the common optimum for three different envy measures, and the exact conditional random-stock distribution. Their general domain algorithm does not state these results.

Gan, Suksompong, and Voudouris (arXiv:1905.00468v2, Section 2) give a general polynomial-time envy-free assignment decision procedure and a large-market high-probability theorem under independent preference rankings. Those results permit per-instance decisions but do not give this polarized three-agent structural characterization or exact conditioned finite-size and first-passage formulas. The elementary endpoint-order enumeration itself is familiar; the contribution concerns its exact translation into three distinct allocation objectives and a minimum-house law. No assertion is made that all random house-allocation models have this law.

## Limitations

The result is restricted to three agents, two exactly opposite strict rankings, and at most one house per agent. No robustness to deviations from opposite rankings, cardinal costs, ties, or Pareto-efficiency guarantee is established. The first-passage distribution requires an inventory-prefix coupling and independent atomless third-agent utilities. The existing globally single-dipped obstruction is prior art; the claimed extension is the sharp converse and associated optimal-envy and stock laws. An unindexed equivalent formulation in the preference-domain or random-permutation literature remains possible. No independent scientific audit has been performed.

## References

1. Hadi Hosseini, Sanjukta Roy, and Aditi Sethia, *Fair Societies: Algorithms for House Allocations*, arXiv:2511.07022v1, first publicly available 10 November 2025. https://arxiv.org/html/2511.07022v1 (notably definitions in Section 2 and Lemma 4.10 in Section 4.2).
2. Jiarui Gan, Warut Suksompong, and Alexandros A. Voudouris, *Envy-Freeness in House Allocation Problems*, arXiv:1905.00468v2, 2019. https://arxiv.org/pdf/1905.00468 (algorithm and random-market Theorem 2.3).
