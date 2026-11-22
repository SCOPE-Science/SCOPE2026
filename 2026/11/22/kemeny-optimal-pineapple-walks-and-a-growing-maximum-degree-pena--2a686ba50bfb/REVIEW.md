# Scientific review

## Correctness — PASS

The claim applies to all \(n\ge3\) and \(r\ge1\), with arbitrary symmetric nonnegative stochastic weights on allowed edges and connected support. The Kemeny convention is explicitly defined. The strictly convex trace-inverse objective yields global uniqueness, after which automorphism invariance is compulsory rather than assumed. Three invariant spectral blocks give an exact rational objective; saturation of two independent row budgets and a strictly convex scalar reduction prove the unique all-positive weights. For fixed \(r\), the scalar limiting optimization and direct maximum-degree substitution give the \(r+1\) regret. An extracted standalone script completed 585 exact and numerical assertions on actual package contents. No finite experiment is treated as an infinite proof.

## Originality — PASS on inspected evidence

Boyd–Diaconis–Xiao (2004) supplies a *different* fastest-mixing objective, and a small single-pendant example; Patel–Agharkar–Bullo (2015) supplies general Kemeny convex design, but not this evaluated clique–star family; Faught–Kempton–Knudson (2021) supplies fixed simple-walk 1-separation formulas with a degree-weighted stationary law. Two highly related published pineapple fastest-mixing result files were read in full and address SLEM, not Kemeny optimality. An earlier exact Kemeny design on leaf coronas covers a different attachment scheme, with leaves at **every** core vertex; it does not imply the localized-star optimum. One-leaf clique and double-clique fastest mixing are likewise distinct optimization questions. Queries covered aliases including lollipop, clique with pendant leaves, pineapple, inverse spectral trace and mean hitting-time design. The residual risk is an unindexed weighted-pineapple inverse-trace classification or a specialized equivalent consequence not identified by available searches.

## Value — PASS

The result gives the unrestricted optimal transition design on the natural family of clique–star one-vertex attachments for every clique size and number of leaves, determines support and holding behavior, and exactly quantifies an unbounded-in-\(r\) large-clique loss of the familiar maximum-degree design. Its essential distinction from SLEM-optimal pineapple design is that the inverse-spectral-sum objective forces all internal clique edges to carry positive mass. These are structural design and benchmark facts, not just a computation of an arbitrarily chosen parameter value.

## Scope and limits

The strict theorem assumes uniform stationary law and symmetric transitions. The limiting regret fixes \(r\) before sending \(n\) to infinity. No independent mathematical audit or external priority certification was performed; unchecked equivalent literature remains possible.

Self-review: passed. Independent audit: not yet performed.
