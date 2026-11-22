# Self-review

## Correctness — PASS

The normalization counts each of the four undirected edges once and uses all centered radii zero, one and two. The reduction from complex input to nonnegative moduli is nonexpansive for edge energy, and all output branch choices are exhausted by the three \(y\)-intervals and two \(x\)-intervals. The proof states all six exact quadratic expressions and gives strict cone inequalities except for the single top-eigenvector ray of the low-\(y\), high-\(x\) branch. Direct rational recalculation of every region in `checker.py`, exact radical consistency, and the equality witness passed; 5,000 samples are supplemental only. Boundary cases and common-phase rigidity follow from the cone proof and equality in the modulus inequality. The result does not assert an infinite graph or two-input theorem.

## Originality — PASS relative to inspected record

The closest original result of González-Riquelme, Kovač and Madrid (arXiv:2603.12462v1, Theorem 2, §3.1) gives sharp first variation \(3/4\) on \(C_4\); its objective is edge \(\ell^1\), not squared-gradient energy. Lu and Zhao (arXiv:2611.24180v1) give general graph bounds and exact star constants, not this specific quadratic constant. Liu, Lian and Wang (arXiv:2611.15377v1) similarly treat stars and complete-graph/fractional variants. The two most relevant published structured records were read in full: one is weighted first variation on small cycles, the other is the strong \(\ell^2\) **vertex** norm on \(C_4\); neither statement implies the new edge seminorm quotient. An accessible older claim treats an *uncentered contiguous-arc* cycle operator, which has different averaging sets. Search queries and actual closest IDs, precise comparisons and inspection material are in AUDIT.json. Remaining bibliographic risk: an unindexed equivalent result may exist; other less relevant matches were not all inspected in full.

## Mathematical value — PASS

The unweighted four-cycle is the first nontrivial two-connected bipartite model of regularity for centered finite-graph maximal operators. Unlike the known \(p=1\) coincidence of all four-vertex sharp constants at \(3/4\), the sharp \(p=2\) values separate: this cycle has \(\sqrt{(41+\sqrt{1537})/144}\), the complete graph has \(3/4\), and the four-vertex star has \(\sqrt{11}/4\). The exact finite cone decomposition and complete equality classification identify the mechanism for this difference. The advance is a complete natural exact model rather than a claim about arbitrary cycle sizes.

Self-review: passed. Independent audit: not yet performed.
