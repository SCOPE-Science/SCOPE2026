# Review: Induced-matching edge-pivot mobility in squared cycles

## Correctness — PASS

Every selected edge of a squared cycle occupies a consecutive block of selected endpoints, and a cyclic gap of at least two unselected separator vertices separates it from the next selected edge. Hence each clockwise edge has length one or two and consumes four units plus one optional length unit and a nonnegative slack gap. It follows that every induced matching has at most \(\lfloor n/4\rfloor\) edges, attained by periodically spaced short edges. Exact counting of binary lengths and weak compositions yields the four-residue state formula. For zero slack the four possible phases have no legal incident-edge pivot. Positive slack allows elimination of long edges, transfer of units between adjacent gaps, and a constructive all-edge one-step cyclic shift, establishing connectedness for the other three residues. The argument covers the small one-edge cases \(n=5,6,7\). Direct exhaustive compatibility-clique and independent gap-generation/pivot traversals corroborate the theorem in their stated finite ranges. These experiments are not used as infinite proofs.

## Originality — PASS, qualified by historical-priority risk

The comparison is about implications, not shared keywords. Maximum independent *vertex* sets in squared cycles are distinct from maximum induced *edge* matchings. Existing induced-matching algorithms provide maximum size methods and extremal counts in other graph classes, not the exact incident-edge pivot graph. Reconfiguration of ordinary matchings by edge token jumping, as in Bousquet and collaborators (arXiv:1812.05419), does not preserve the stronger induced-matching constraint and imposes no incident-edge rule. General token-sliding of independent *vertex* sets acts on adjacency of the state graph's underlying vertices, whereas the present move requires an incident pair of original-graph edges and preserves the stronger induced-matching constraint. Full-text versions of the accessible arXiv papers on maximal induced matchings and independent-set reconfiguration and the token-sliding tree paper were inspected in relevant sections; the original 2003 induced-matching algorithm paper was not fully accessible. No equivalent complete theorem was identified in the available literature or semantic mathematical records. Nonappearance is not a proof of priority: inaccessible sources and alternative terminology remain risks.

## Value — PASS

The theorem separates two natural questions: how many optimum noninterfering edge placements exist, and whether one optimum can be changed locally without losing optimality. It supplies a sharp all-orders rigidity-versus-mobility boundary and exact optimum-state counts for a canonical cyclic network family. The obstruction is structural—absence versus transferability of slack—not a narrow ad hoc computation. No diameter or further dynamics are asserted.

## Independent assessment and limitations

The source date is the independently verifiable first arXiv posting of the 2013 literature lead; supporting more recent reconfiguration literature is used only for comparisons. Residual historical-priority risk and the absence of independent scholarly validation are explicit. The 2003 publisher-hosted full text could not be fully inspected.

Self-review: passed. Independent audit: not yet performed.
