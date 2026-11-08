# The first clone-free effectivity obstruction: an exact three-outcome census

## Finding

For a fixed labelled finite outcome set \(O\), consider a pair \((\mathcal A,\mathcal B)\) of **nonempty families of distinct nonempty subsets** of \(O\). A *clone-free realization* is a deterministic two-player simultaneous-action table containing exactly one row per member of \(\mathcal A\) and one column per member of \(\mathcal B\), with every row's set of entries precisely its prescribed member of \(\mathcal A\), and every column's set of entries precisely its prescribed member of \(\mathcal B\).

**Theorem (sharp first failure and complete three-outcome census).** Suppose all three conditions hold:

1. Common full range \(\bigcup\mathcal A=\bigcup\mathcal B=O\).
2. Independent action neighborhoods \(A\cap B\ne\varnothing\) for all \(A\in\mathcal A\) and \(B\in\mathcal B\).
3. One-action-per-neighborhood capacity: \(|A|\le|\mathcal B|\) and \(|B|\le|\mathcal A|\).

For \(|O|=1,2,3\), the respective numbers of ordered labelled family pairs satisfying these conditions are \(1,4,282\). All \(1\) and \(4\) small pairs are clone-free realizable. Of the \(282\) three-outcome pairs, exactly \(228\) are clone-free realizable and \(54\) are not. Thus **three is the smallest outcome-set size at which the standard independence and natural per-row/per-column capacity conditions cease to suffice for realization without duplicated actions**.

## Assumptions and scope

An outcome is one of \(0,\ldots,n-1\), with \(1\le n\le3\). A neighborhood family is a set, not a multiset; the labels of the two agents and the labels of outcomes are fixed, but the order of actions within an agent is irrelevant. Rows and columns denote the entire outcome range available after the corresponding single-agent action. A clone-free realization is a complete deterministic table with one row/column for each prescribed set, no auxiliary actions and no probabilistic outcomes. The claim neither forbids repeated *outcomes* in different cells nor requires the row sets to be disjoint.

The stated conditions are necessary: full unions are the global outcome range; each cell's outcome lies in the intersection of its row and column neighborhoods; and one row has only as many entries as the other player has actions (with the analogous bound for columns).

## Proof

**Direct obstruction.** Put \(O=\{0,1,2\}\), \(\mathcal A=\{\{0,1\},\{0,2\}\}\), and \(\mathcal B=\{\{0,1\},\{1,2\}\}\). Both unions are \(O\); the four intersections, in row-major order, are \(\{0,1\},\{1\},\{0\},\{2\}\), so independence holds. Every neighborhood has size two, equal to the number of opposite actions, so capacity holds at equality. Any realizing matrix must be

\[
\begin{pmatrix}t&1\\0&2\end{pmatrix},\qquad t\in\{0,1\}.
\]

The first row must contain both \(0\) and \(1\), forcing \(t=0\); the first column must also contain both, forcing \(t=1\). This contradiction proves nonrealizability.

**Sharpness for fewer outcomes.** For one outcome, the only qualifying pair consists of the unique singleton neighborhood on both sides, realized by the one-cell table. For two labelled outcomes, the complete list of qualifying family pairs (writing \(O=\{0,1\}\)) is: \((\{O\},\{\{0\},\{1\}\})\), its transpose, \((\{\{0\},O\},\{\{0\},O\})\), and \((\{\{1\},O\},\{\{1\},O\})\). They are respectively realized by a row \((0,1)\), a column \((0,1)^{\mathsf T}\), the two-by-two table with rows \((0,0)\), \((0,1)\), and the analogous table with rows \((1,1)\), \((1,0)\). Every possible nonempty family of nonempty subsets is among the \(2^{2^2-1}-1=7\) families; direct inspection of those pairs under common full range, independence, and capacity yields exactly this list.

**Exact finite census at three outcomes.** Represent each nonempty subset of \(O=\{0,1,2\}\) as a nonzero three-bit mask. Iterate all \(2^{2^3-1}-1=127\) nonempty families of such masks, and hence all ordered pairs of families. Retain exactly those pairs satisfying common full union, independence and capacity. For a retained pair enumerate every complete matrix whose entry in row \(A\) and column \(B\) lies in \(A\cap B\), and accept a matrix if its row and column entry unions equal the prescribed sets. These are logically equivalent to clone-free realization: necessity is immediate from the definition, and sufficiency follows by treating rows and columns as distinct actions. The accompanying standalone exhaustive checker implements precisely these finite tests and yields \(282\) qualified pairs, \(228\) realizable and \(54\) nonrealizable. The algorithm tests every candidate (at most \(127^2\) family pairs) and every feasible cell filling; there is no unsearched remainder. The preceding forced-cell argument separately certifies an explicit negative instance without trusting the census.

## Verification

Execute \(`python3 checker.py`\) from the directory containing the complete standalone program. Its expected final line is \(`CLONE_FREE_FIRST_OBSTRUCTION_OK`\). It checks the complete family-pair and matrix-filling search for outcome sizes one, two and three, verifies the three exact counts and confirms the explicit obstruction. The finite search proves the finite-number statements by exhaustive, terminating loops over the entire stated finite domains; the explanatory argument establishes why its predicates are equivalent to the mathematical conditions. This verification does not address larger outcome sets.

## Relationship to prior work

Ciardelli, *Inquisitive Action Logic* (arXiv:2606.31866, June 30, 2026), Theorem 2.2, establishes that nonempty family, uniform range and independence are sufficient when the game may **duplicate** neighborhood actions. His constructive converse introduces actions with extra labels. This theorem studies the separate nonduplicating-resource constraint, adds the necessary capacity inequalities, and gives their sharp first failure and complete smallest failing-size count. The published construction permits additional actions and therefore does not deliver the asserted clone-free census.

An earlier mathematical-research record on sharp root-size action realization gives a worst-case number of action copies depending on the number of outcomes; it is an important related action-resource bound, but its available summary does not enumerate all labelled, capacity-feasible pairs with exactly three outcomes. A separate earlier census concerns *transverse partitions* of outcomes; these are disjoint within an agent and do not include the overlapping-neighborhood witness above. The numerical census and explicit obstruction are asserted only within these carefully restricted hypotheses.

## Limitations

Only two agents and at most three labelled outcomes are classified. The admissible family-pair census is conditional on **all** three necessary constraints, including the action-capacity inequalities. The construction does not characterize all higher-outcome nonrealizable families, and it does not show that the three-outcome obstruction is unique. Full historical-priority verification beyond the inspected literature and accessible indexed descriptions has not been completed; the root-size representation literature is a residual overlap risk. There has been no independent mathematical audit.

## References

1. Ivano Ciardelli, *Inquisitive Action Logic*, arXiv:2606.31866v1, first publicly submitted June 30, 2026, especially Definition 2.1 and Theorem 2.2. https://arxiv.org/abs/2606.31866
2. *Sharp root-size action realization for finite actual-effectivity frames*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-root-size-action-realization-for-finite-actual-effectivity--114a0e0912e6
