# Sharp envy-free workload conductor and exact census for budgeted unit chores

## Finding

Fix integers \(n\ge 2\), \(m\ge0\), and agent capacities \(b_1,\ldots,b_n\ge1\). In the budgeted indivisible-chores model of Elkind, Igarashi and Teh [1], suppose that the \(m\) distinct chores all have size and disutility one. Every chore is assigned to exactly one of the \(n\) labeled agents or to the housekeeper. Define
\[
B=\max_i b_i,\qquad S=\sum_i b_i,\qquad F(t)=\sum_{i=1}^n\min(b_i,t),\qquad R(t)=|\{i:b_i\ge t\}|.
\]

**Complete classification.** An assignment is exactly envy-free (EF) if and only if its load vector \((a_1,\ldots,a_n,h)\), including the housekeeper load \(h\), has one of the following forms:

1. **All full:** \(a_i=b_i\) for every \(i\), with \(h=m-S\ge0\).
2. **Common water level:** for one integer \(0\le t<B\), \(a_i=\min(b_i,t)\) for every \(i\), with \(h=m-F(t)\) satisfying \(0\le h\le t\).

The listed load vectors are distinct. Consequently, the **exact number of allocations of the individually distinguishable chores to the labeled agents and housekeeper** is
\[
\begin{aligned}
N_{\mathrm{EF}}(m;\mathbf b)=m!\bigg[&\mathbf{1}_{\{m\ge S\}}
\frac{1}{(m-S)!\prod_{i=1}^n b_i!}\\
&+\sum_{t=0}^{B-1}\mathbf{1}_{\{F(t)\le m\le F(t)+t\}}
\frac{1}{(m-F(t))!\prod_{i=1}^n\min(b_i,t)!}\bigg].
\end{aligned}
\]
The indicator convention makes factorials in inactive summands irrelevant.

**Sharp eventual-feasibility threshold.** Let
\[
t_* = \max\{t\in\{1,\ldots,B\}:R(t)\ge t+1\},\qquad T(\mathbf b)=F(t_*).
\]
The set defining \(t_*\) is nonempty. An EF assignment exists for **every** integer \(m\ge T(\mathbf b)\), but none exists for \(m=T(\mathbf b)-1\). More precisely, the full existence spectrum is
\[
\left(\bigcup_{t=0}^{B-1}\bigl([F(t),F(t)+t]\cap\mathbb Z\bigr)\right)
\cup\bigl([S,\infty)\cap\mathbb Z\bigr).
\]
Thus \(T(\mathbf b)\) is the least workload after which EF is guaranteed for *all* larger workloads with the same capacities. With equal capacities \(b_i=b\), this becomes the sharp formula \(T= n\min(b,n-1)\).

For example, four agents with capacities \((5,5,5,5)\) have \(t_*=3\) and \(T=12\). There is no EF allocation of eleven unit chores, whereas twelve chores admit exactly \(12!/(3!)^4=369600\) EF allocations.

## Assumptions and scope

The agents have *identical additive* disutilities, each chore has objective size \(1\) and disutility \(1\), all capacities are positive integers, and the housekeeper has no capacity restriction. Empty agent bundles are permitted. EF means Definition 1 of [1]: for every source bundle \(A_i\), where the source may be the housekeeper, every genuine agent \(j\), and every subset \(Q\subseteq A_i\) whose total size is at most \(b_j\), the disutility of \(Q\) is at most that of agent \(j\)'s bundle. This is **exact EF**, not EF1 or EFX. The count treats chores as distinct; it does not quotient by agent or chore permutations.

The source paper appeared online on 31 August 2024 [1], before the open arXiv version of 31 October 2024. Its public-release date is not to be confused with the latter date.

## Proof

**Lemma 1 (load form).** If the source bundle has load \(x\) and genuine agent \(j\) has load \(a_j\), the worst eligible subset has cardinality \(\min(x,b_j)\). Consequently EF is equivalent to
\[
\min(a_i,b_j)\le a_j\quad(i=1,\ldots,n+1;\ j=1,\ldots,n),
\]
with \(a_{n+1}=h\), and feasibility requires \(a_j\le b_j\).

If every agent is at capacity, all the inequalities hold, regardless of the housekeeper load. Otherwise select an unsaturated agent \(j\), for whom \(a_j<b_j\). If any source load \(x>a_j\), then the integer \(\min(x,b_j)\) exceeds \(a_j\), contradicting EF. Hence an unsaturated agent's load is a global maximum over all agent and housekeeper loads. In particular all unsaturated agents share some load \(t\), all saturated agent loads are at most \(t\), and the housekeeper has load at most \(t\). An agent whose capacity exceeds \(t\) must be unsaturated with load \(t\), while an agent whose capacity is at most \(t\) must be saturated. Thus \(a_i=\min(b_i,t)\), \(0\le t<B\), and \(h=m-F(t)\in[0,t]\). Conversely, in any load pattern of this form, a saturated agent satisfies every EF comparison trivially, while an unsaturated agent has load \(t\) and all source loads are at most \(t\). The all-full case also satisfies EF. This proves the classification, including \(m=0\).

**Lemma 2 (count).** For a prescribed load vector \((a_1,\ldots,a_n,h)\) summing to \(m\), exactly \(m!/(h!\prod_i a_i!)\) allocations assign the \(m\) distinct chores to the \(n+1\) labeled bundles. The water-level vectors for different integers \(0\le t<B\) differ, because \(F(t+1)>F(t)\): at least one capacity exceeds \(t\). No water-level vector is all-full. Summing the disjoint multinomial counts gives the displayed formula.

**Lemma 3 (the sharp conductor).** For \(0\le t<B\), the possible workload interval at water level \(t\) is \(I_t=[F(t),F(t)+t]\cap\mathbb Z\). At level \(B\), the all-full case allows all workloads in \(I_B=[S,\infty)\cap\mathbb Z\). The starts \(F(t)\) increase strictly until level \(B\), and
\[
F(t+1)-F(t)=R(t+1).
\]
The gap between \(I_t\) and \(I_{t+1}\) is nonempty exactly when
\[
F(t+1)>F(t)+t+1
\quad\Longleftrightarrow\quad R(t+1)\ge t+2.
\]
Because \(R(u)\) decreases weakly with \(u\), while \(u\) increases, once this gap condition fails it fails at every subsequent level. It holds at \(u=1\) since \(R(1)=n\ge2\). Therefore \(t_*\) is exactly the index of the **last nonempty gap**, situated immediately before \(I_{t_*}\). The integer \(F(t_*)-1\) belongs to that gap, and the intervals from \(I_{t_*}\) onward meet or overlap, ending with \(I_B\), so they cover all integers at least \(F(t_*)\). This proves the sharp threshold. For equal budgets, \(R(t)=n\) for \(1\le t\le b\), giving \(t_*=\min(b,n-1)\).

These lemmas prove all asserted formulas for every parameter choice in scope.

## Verification

The accompanying standalone `verify.py` independently checks EF by iterating over every subset-size comparison in the integer-unit reduction \(\min(a_i,b_j)\le a_j\), rather than testing the water-level formula. It enumerates every labeled assignment for 1206 finite parameter settings, covering 6,066,226 assignments, and matches the exact counting formula without discrepancies. It also checks the equal-capacity conductor for 182 settings and the heterogeneous conductor for 19,525 ordered capacity vectors. These finite tests supplement but do not replace the preceding proof.

Reproduce using `python3 verify.py` with Python 3 and no third-party dependencies. The theorem needs no floating-point computation or external dataset.

## Relationship to prior work

Elkind, Igarashi and Teh [1] introduce the housekeeper and the budget-sensitive EF definition used here and establish EFX for general indivisible chores, efficient EF2 in general, EF1 for homogeneous special cases, and exact EF for **divisible** chores. Their inspected Sections 2–7 and proof material do not state the present *indivisible-unit* exact EF load classification, count, or last-gap threshold.

Barman, Khan, Shyam and Sreenivas [2] analyze the mathematically close budgeted **goods** model, including identical-value and identical-size special cases, but their inspected theorem statements address EF2/EF1, rather than this exact EF census or sharp feasibility conductor. Since goods and chores can produce the same integer inequalities under identical values, this mathematical reduction was considered explicitly in assessing priority; different item labels alone provide no novelty. The claimed contribution is specifically the complete load-vector enumeration and strict-Durfee last-gap law for the housekeeper-inclusive exact-EF definition.

## Limitations

The theorem does not apply to heterogeneous chore sizes or disutilities, non-integer budgets, nonadditive preferences, unbudgeted fairness definitions, or EF1/EFX enumeration. It does not establish independent external priority or certification. Unindexed equivalent results or a stronger exact characterization in other literature remain a residual publication-priority risk; negative search results alone cannot establish uniqueness.

## References

[1] Edith Elkind, Ayumi Igarashi and Nicholas Teh, *Fair Division of Chores with Budget Constraints*, Algorithmic Game Theory (SAGT 2024), pp. 55–71, first online 31 August 2024, https://doi.org/10.1007/978-3-031-71033-9_4 . Public full-text version: https://arxiv.org/html/2410.23979v1 (posted 31 October 2024).

[2] Siddharth Barman, Arindam Khan, Sudarshan Shyam and K. V. N. Sreenivas, *Finding Fair Allocations under Budget Constraints*, first arXiv release 17 August 2022, https://arxiv.org/abs/2208.08168 ; AAAI 2023, https://doi.org/10.1609/aaai.v37i5.25681 .
