# Scientific assessment

## Correctness — PASS
The finite real least-squares problem is projection onto a closed convex polyhedron and therefore has a unique solution. Each full-dimensional affine selection region has a Jacobian that averages on consecutive blocks, even when a positive upper-slope cap is active, because bound-saturating increments contribute fixed affine offsets. Arbitrary prescribed consecutive block partitions are attained on strictly complementary regions with lower bounds active and strictly positive separation between blocks. Thus the unrestricted nonlinear Lipschitz problem reduces exactly to the corresponding finite set of linear seminorm problems, not merely to a one-sided estimate.

For block means the nonzero difference map has nonnegative entries, maximum column sum one and an interblock row sum equal to half the sum of the neighboring block lengths. Three or more blocks give squared operator norm at most \((n-1)/2\). Two-block row norms have the exact value \(n/3+(1/a+1/b)/6\), controlling the small-size exceptions. Local witnesses attain all stated sharp bounds. The verifier checks 1013 partitions and small exact KKT projections. The proof, rather than finite enumeration, handles arbitrary dimensions and caps.

## Originality — PASS, qualified
The earliest inspected foundational source is the 2009 LPAV paper by Yeganova and Wilbur. Its complete open-access PDF describes constrained regression and algorithms, not this discrete-gradient two-input norm. Agarwal, Phillips and Sadri's 2009 preprint treats path/tree Lipschitz isotonic algorithms, not sharp Sobolev stability. Yang and Barber (2017) characterize when an isotonic projection is contractive in a given seminorm, but this noncontractive first-difference quadratic seminorm lies outside their contraction conclusion; their primary full text does not state the present complete quantitative formula. The closest indexed quantitative result on isotonic projection treats coordinatewise \(\ell_p\) norms, or weighted **absolute** edge variation rather than squared first-difference energy. Such statements do not imply the exact bound here, particularly its two nontrivial finite exceptions and cap-independence.

The relevant primary literature was inspected materially, and the retrieved indexed summaries were compared by implication, not merely title. The residual historical-priority risk is an unindexed independent treatment of the same Sobolev seminorm or an unnoticed general operator estimate. No assertion of absolute uniqueness or priority is made.

## Value — PASS
A bounded-slope fit is nonexpansive in the ordinary Euclidean fitting metric. Its ability to amplify **difference gradients** is operationally different from, and not controlled by, unweighted path total variation. The theorem quantifies this instability exactly: growth as \(\sqrt{n/2}\), a transition to a two-boundary extremizer at length five, and complete invariance under arbitrary positive, nonuniform slope caps. This supplies a sharp stability limit for a classical shape-constrained smoothing method and explains an explicit mechanism by which gradual input perturbations can create concentrated output jumps. The dimension-dependent distinction is substantive rather than a parameter renaming or a numerical example.

## Limitations and outstanding risks
The formula is restricted to equal least-squares observation weights, finite chains and strictly positive upper caps, possibly infinite. Other graph topologies, observation masses and alternate gradient powers are outside the claim. The primary literature comparison is not a universal novelty proof. Independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
