# Negative-run normal form and exact online ranks for finite interval membership

## Finding

Let \(\mathcal I_n=\{[a,b]\subseteq[n]:1\le a\le b\le n\}\) be the class of **nonempty** contiguous intervals, with binary membership queries at individual points. The following is an exact conditional Littlestone-rank theorem, not a formula inferred from finite enumeration.

**Positive-observation case.** Every nonempty version space having at least one positive observation is a Cartesian product of a left-endpoint threshold family of size \(L\ge1\) and a right-endpoint threshold family of size \(R\ge1\). Its exact remaining Littlestone dimension is
\[
\lfloor\log_2 L\rfloor+\lfloor\log_2 R\rfloor.
\]

**Negative-only case.** After any history consisting exclusively of negative labels, let \(\lambda=(\ell_1,\ldots,\ell_t)\) be the multiset of positive lengths of maximal unqueried runs. Put \(F(\varnothing)=-1\), and for nonempty \(\lambda\) define
\[
F(\lambda)=\max\left\{0,\ \max_{1\le j\le t}\max_{1\le i\le\ell_j}\left(1+\min\!\left(\lfloor\log_2 i\rfloor+\lfloor\log_2(\ell_j-i+1)\rfloor, F(\operatorname{sort}_+(\lambda\setminus\{\ell_j\}\cup\{i-1,\ell_j-i\}))\right)\right)\right\}.
\]
Here \(\operatorname{sort}_+\) deletes zero entries and sorts the remaining positive integers; a single occurrence is removed from the multiset. The exact Littlestone dimension of every nonempty negative-only version space is \(F(\lambda)\), in particular
\[
\operatorname{Ldim}(\mathcal I_n)=F((n)).
\]
This determines every conditional online rank via a finite integer-partition recurrence. If \(p(m)\) counts integer partitions of \(m\), memoization requires at most \(\sum_{m=0}^n p(m)\) states and \(O(n^2p(n))\) query transitions, with polynomial elementary work per transition. The latter bound is a structural state bound, **not** a claim to beat all generic algorithms for explicitly represented concept classes.

**Sharp dyadic consequence.** For every integer \(k\ge0\),
\[
\operatorname{Ldim}(\mathcal I_{2^{k+1}-1})=2k.
\]
For all \(n\ge1\),
\[
2\max\{0,\lfloor\log_2((n+1)/2)\rfloor\}\ \le\ \operatorname{Ldim}(\mathcal I_n)\ \le\ \left\lfloor\log_2\frac{n(n+1)}2\right\rfloor.
\]
Thus the online dimension is \(2\log_2 n+O(1)\), although its static dimension is only two for all \(n\ge3\). In fact its shattered-support polynomial is \(1\) for \(n=1\), \(1+2z\) for \(n=2\), and \(1+nz+\binom n2z^2\) for \(n\ge3\).

## Assumptions and scope

Only nonempty ordinary intervals on the finite chain \([n]\) are hypotheses. Queries reveal membership of the queried point, not an endpoint, an interval-intersection predicate, or an ordered-pair relation. All rank claims are for every integer \(n\ge1\), all realizable finite query histories, and both binary outcomes when realizable. Infeasible version spaces are assigned sentinel rank \(-1\) solely to express the dynamic-programming recurrence; the conventional Littlestone dimension of a nonempty singleton class is zero. The recurrence is not asserted for unions of two or more intervals as individual hypotheses.

## Proof

**1. Rank of a finite threshold family.** Let \(T_m\) consist of \(m\) nested distinct initial segments on a line. Every query partitions the ordered list of hypotheses into a prefix and a suffix. A depth-\(d\) shattered tree requires at least \(2^d\) hypotheses, hence \(d\le\lfloor\log_2m\rfloor\). Conversely, query a point splitting the hypothesis list into two parts of sizes at least \(2^{d-1}\) whenever \(m\ge2^d\), and recursively use the two parts. Thus its rank equals \(\lfloor\log_2m\rfloor\).

For binary classes on disjoint query domains, the rank of a Cartesian product equals the sum of the two ranks. For the lower bound, attach an optimal mistake tree for the second factor to every leaf of an optimal tree for the first. For the upper bound, induct on the sum of factor ranks: any query acts on only one factor; among its two restrictions at least one has smaller rank than that factor, so at least one branch has product rank at most one less than the proposed sum. The same argument applies at rank zero, where one of the query branches is empty.

**2. Positive-observation normal form.** Let \(a\) and \(b\) be the first and last positively labeled positions (\(a\le b\)). Every interval consistent with the data must contain the whole segment \([a,b]\). No negative may occur inside this segment. Any negative positions left of \(a\) bound the left endpoint from below; any negatives right of \(b\) bound the right endpoint from above. Therefore consistent intervals are precisely the pairs \((l,r)\) with \(l\) in a nonempty consecutive set of \(L\) possibilities and \(r\) in a nonempty consecutive set of \(R\) possibilities. Queries strictly left of \(a\) depend only on \(l\); queries strictly right of \(b\) depend only on \(r\); all queries between them are forced positive. The factors are independent threshold families, proving the first formula.

**3. Negative-only normal form.** If all observed answers are negative, an admissible nonempty interval cannot cross any observed negative position, and therefore lies wholly within one maximal unqueried run. Thus the class is the disjoint union of the full nonempty-interval families on those runs, and only the multiset \(\lambda\) of run lengths matters. Querying the \(i\)-th point in run \(\ell_j\) has a positive branch with exactly \(i\) choices of left endpoint and \(\ell_j-i+1\) choices of right endpoint. By step 2 its rank is the displayed sum of floor logarithms. The negative branch retains every other run and replaces the queried run by the two residual runs of lengths \(i-1\) and \(\ell_j-i\). Its rank is the corresponding smaller \(F\)-state. The standard complete-binary-mistake-tree recursion takes one plus the minimum branch rank, maximized over queries. When the negative branch is empty, the sentinel \(-1\) makes the candidate contribution zero, as required. Induction on \(\sum_j\ell_j\) proves the full recurrence and its base case, including the nonempty-singleton case.

**4. State count.** In every negative-only recursion step exactly one unqueried position is removed; each state is specified by an integer partition of some \(m\le n\). The number of such states is at most \(\sum_{m=0}^np(m)\). At most \(m\le n\) queries are considered in each state, so the total number of transitions is at most \(n\sum_{m=0}^np(m)\le n(n+1)p(n)\). Sorting, indexing and integer logarithms add polynomial overhead. In particular the number of states is \(\exp(O(\sqrt n))\), by the standard partition-number growth bound.

**5. Dyadic equality and growth.** Fix \(k\ge0\), put \(m=2^k\), and let \(n=2m-1\). Restrict to the \(m^2\) intervals containing the central point \(m\). Their left endpoints range independently over \([m]\), and their right endpoints range independently over \(\{m,\ldots,2m-1\}\). By step 1 this subclass has online dimension \(2\log_2m=2k\). The entire interval class contains \(n(n+1)/2=m(2m-1)<2m^2=2^{2k+1}\) hypotheses, so the information bound gives online dimension at most \(2k\). For arbitrary \(n\), take the largest \(k\ge0\) with \(2^{k+1}-1\le n\), and invoke monotonicity under the embedding of the first \(2^{k+1}-1\) points. This yields the stated lower bound and, together with the information bound, the asymptotic growth.

**6. Static shattering.** Any three queried points \(a<b<c\) cannot realize the pattern \(1,0,1\) with an interval. Every two queried points can realize all four labelings when \(n\ge3\), by choosing a singleton away from the two points for \(0,0\), singletons at each point for \(1,0\) and \(0,1\), and their connecting interval for \(1,1\). The one- and two-site domains are handled directly. This gives the complete shattering polynomial and VC dimensions.

## Verification

The standalone `verify_intervals.py` reproduces the partition-state recursion, independently enumerates all interval hypotheses and their point-membership masks, and recomputes the exact general version-space rank for \(1\le n\le10\) without assuming the normal form. For all realizable three-valued query histories through eight sites (5,110 cases), it further checks the corresponding conditional rank, including histories with positive observations. It also independently checks all static shattering supports up to \(n=10\), evaluates the recurrence through \(n=40\), and tests the dyadic equalities for the cases within that range. All comparisons pass. The finite computations corroborate, but do not prove, the unrestricted statements; proofs are in the preceding section. To reproduce, run `python3 verify_intervals.py` with a standard Python 3 interpreter.

## Relationship to prior work

Manurangsi and Rubinstein (2017, arXiv:1705.09517, first posted 2017-05-26) give general complexity results and a quasi-polynomial algorithm for explicitly presented Littlestone dimension. Their general algorithm does not identify the interval-specific normal forms or the exact dyadic values here; our state count should not be advertised as better than their general asymptotic runtime. Ghazi, Golowich, Kumar and Manurangsi (2020/2021, arXiv:2007.03668) establish aggregate-class closure bounds, not an exact membership-query interval rank. Haghtalab, Roughgarden and Shetty (2021 preprint, arXiv:2102.08446, Sections 3.4 and 5) use products of separate threshold families for online lower bounds and discuss the static VC dimension of intervals. Their product construction motivates part of the dyadic lower bound but is not a formula for the exact interval class under membership queries or a conditional rank recursion. The new claim is limited to the complete positive/negative observation normal forms, exact conditional recurrence, and their consequences; generic threshold ranks, product additivity, and the information bound are acknowledged ingredients.

## Limitations

No elementary closed form for \(F((n))\) at every \(n\) is claimed. The integer-partition state complexity is not known here to be asymptotically optimal and is not compared favorably with the best general quasi-polynomial algorithms. The isolated dyadic equality follows by standard threshold-tree and cardinality arguments; its significance is as a sharp boundary case of the exact interval-specific conditional structure, not as a new general lower-bound technique. Literature search cannot exclude earlier equivalent results under terminology such as interval-query mistake trees or interval concept online rank. No independent audit has been performed.

## References

1. P. Manurangsi and A. Rubinstein, *Inapproximability of VC Dimension and Littlestone's Dimension*, arXiv:1705.09517 (first version May 26, 2017); COLT 2017. https://arxiv.org/abs/1705.09517
2. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, arXiv:2007.03668 (2020); ALT 2021. https://proceedings.mlr.press/v132/ghazi21a.html
3. N. Haghtalab, T. Roughgarden and A. Shetty, *Smoothed Analysis with Adaptive Adversaries*, arXiv:2102.08446 (2021), Sections 3.4, 5; J. ACM 2024. https://ar5iv.labs.arxiv.org/html/2102.08446
