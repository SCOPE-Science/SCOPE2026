# Gap-partition recurrence and sharp initial ranks for finite interval incidence

## Finding

Let \([n]=\{1,\ldots,n\}\) for \(n\ge0\), and let \(\mathcal I_n\) be the binary concept class consisting of the empty set and every nonempty consecutive interval of \([n]\). Its complete binary mistake-tree rank, also called Littlestone dimension or finite Shelah tree rank of interval incidence, admits an exact recurrence in integer partitions. For a multiset \(\lambda\) of positive integers define \(R(\varnothing)=0\) and

\[
R(\lambda)=\max_{m\in\lambda,\ 0\le a<m}
\left(1+\min\left\{
\lfloor\log_2(a+1)\rfloor+\lfloor\log_2(m-a)\rfloor,
R\bigl((\lambda\setminus\{m\})\cup\{a,m-a-1\}_{>0}\bigr)
\right\}\right).
\]

Here zero entries are omitted from \(\{\cdots\}_{>0}\), and the maximum over an empty index set is zero. Then \(\operatorname{Ldim}(\mathcal I_n)=R(\{n\})\) for \(n\ge1\), and \(\operatorname{Ldim}(\mathcal I_0)=0\). The number of distinct states with total gap size at most \(n\) is at most \(\sum_{s=0}^n p(s)\), where \(p(s)\) is the partition function, yielding a \(\operatorname{poly}(n)p(n)\)-time and -space exact calculation. In particular, it is subexponential in \(n\).

The first ten *sharp* dimension thresholds are:

| Required dimension \(d\) | Least \(n\) with \(\operatorname{Ldim}(\mathcal I_n)\ge d\) |
|---:|---:|
|1|1|
|2|2|
|3|4|
|4|6|
|5|9|
|6|13|
|7|19|
|8|27|
|9|39|
|10|55|

The table is a finite exact output of the proved recurrence, not a claim of a closed form at every rank.

## Assumptions and scope

The domain consists of \(n\) points with their natural linear order, and hypotheses are all intervals including the empty interval. We use the ordinary complete-binary-tree version of Littlestone dimension, with deterministic binary membership feedback. For a multiset \(\lambda\), the auxiliary concept class comprises the empty hypothesis and all intervals contained wholly in a single one of a family of pairwise separated, totally ordered blocks whose positive lengths are the entries of \(\lambda\); the blocks have disjoint query domains. Duplicated lengths are allowed. The result concerns finite ranks and exact deterministic realizable online mistake bounds. It does not claim the same recurrence for a union of two or more intervals as one hypothesis, nor any infinite-domain rank bound.

## Proof

**Step 1 (the positive branch).** For the class of all intervals of a block of length \(m\), query its point at zero-based position \(a\), with \(0\le a<m\). If the label is one, the interval necessarily contains that point and its left endpoint is one of \(a+1\) choices, while its right endpoint is one of \(m-a\) choices. Every choice of left and right endpoints is valid independently. Queries strictly to the left test a threshold in the left endpoint; queries strictly to the right test a threshold in the right endpoint. These two parameter groups act on disjoint query sets. A class of \(t\) nested thresholds has Littlestone dimension \(\lfloor\log_2t\rfloor\): cardinality gives the upper bound and repeated balanced splitting realizes the lower bound. For classes on disjoint query sets, the dimension of the Cartesian product is the sum of dimensions. The lower bound concatenates their shattered trees and the upper bound runs their optimal deterministic learners independently, adding their mistake budgets. Thus the positive branch has exact dimension

\[
P(m,a)=\lfloor\log_2(a+1)\rfloor+\lfloor\log_2(m-a)\rfloor.
\]

**Step 2 (the negative branch).** Before a positive answer has occurred, all previous negative membership answers exclude their query points from every nonempty viable interval. Therefore a surviving nonempty interval must be wholly inside one connected gap of the unexcluded chain. The zero branch of a query at position \(a\) in a block of length \(m\) replaces that gap by gaps of lengths \(a\) and \(m-a-1\), deleting length zero. All other gaps remain unchanged; the empty interval remains viable. Permutations of whole blocks preserve the concept class up to relabeling, so only the multiset of gap lengths matters.

**Step 3 (the recurrence).** Every nontrivial finite concept class obeys the exact game-rank identity \(\operatorname{Ldim}(H)=\max_x[1+\min\{\operatorname{Ldim}(H_{x=0}),\operatorname{Ldim}(H_{x=1})\}]\), with branches that are empty omitted and the singleton base case equal to zero. Steps 1 and 2 identify both branch ranks for every possible query of every surviving gap. The displayed recurrence follows. Its recursive argument has total gap size exactly one smaller than the parent state. Thus induction on total gap size proves the formula at all finite lengths, without relying on the subsequent computation.

**Step 4 (state complexity and thresholds).** Every state is an integer partition of some \(s\le n\). The recurrence examines at most \(s\le n\) query positions in each state, and constructs each successor by bounded tuple operations. The partition-count bound implies subexponential running time and storage. The accompanying code calculates exact ranks of \(R(\{n\})\) and checks each threshold \(n_d\) using \(R(\{n_d-1\})=d-1\), \(R(\{n_d\})=d\). Dimension is nondecreasing in \(n\), because hypotheses on \([n]\) extend by zero at point \(n+1\), so these adjacent checks prove the stated *least* sizes.

## Verification

Run `python3 verify_finite_interval_littlestone.py` with a standard Python 3 interpreter. The script implements the well-founded partition recurrence and separately computes the original hypothesis-subset recurrence for every length \(1\le n\le16\), obtaining full agreement. For each of the ten proposed sharp thresholds, it checks the rank on both sides and explicitly constructs a complete depth-\(d\) shattered binary tree. It exhaustively checks every leaf path against an actual interval or the empty hypothesis, up to 1024 paths at depth ten. All checks completed successfully; the captured output is in `verification_output.txt`. Finite execution verifies only the displayed ten threshold pairs; the all-\(n\) recurrence is established by the proof in the preceding section.

## Relationship to prior work

Malliaris and Moran's 2021 preprint (later published as *Model Theory and Agnostic Online Learning via Excellent Sets*) develops the relation between model-theoretic stability and Littlestone dimension and proves structural results about stable classes, rather than a finite-chain interval rank formula. Ghazi, Golowich, Kumar and Manurangsi (2021) give general Littlestone closure bounds; they do not calculate the exact interval rank. Attias, Hanneke and Ramaswami (2025) study online algorithms for \(k\)-interval classes and cite asymptotic \(O(k\log n)\) ranks; their inspected interval section does not give this gap-partition recurrence or the ten exact cutoffs. Unlike general finite-hypothesis recurrence, the present result compresses all negative-answer version spaces into integer partitions and all positive-answer spaces into products of two thresholds.

## Limitations

The exact ranks beyond the first ten depth thresholds are computable by the recurrence but have not been enumerated or assigned a closed formula here. The table is not a proof of a guessed dyadic pattern at arbitrary depth. The originality claim is relative to literature actually inspected and semantic searches; unindexed work on finite-domain online interval learning could contain an equivalent partition recursion or tabulation. The proof of the all-length recurrence does not depend on scripts, and no claim of independent scientific certification is made.

## References

1. M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, first public preprint 2021-08-12, arXiv:2108.05569, https://arxiv.org/abs/2108.05569 .
2. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, ALT 2021, PMLR 132, https://proceedings.mlr.press/v132/ghazi21a.html .
3. I. Attias, S. Hanneke and A. Ramaswami, *Tradeoffs between Mistakes and ERM Oracle Calls in Online and Transductive Online Learning*, arXiv:2506.00135, 2025, https://arxiv.org/abs/2506.00135 .
