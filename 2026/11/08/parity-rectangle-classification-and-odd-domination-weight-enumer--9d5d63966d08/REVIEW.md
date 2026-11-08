# Scientific review

## Correctness — PASS

For all integers \(m,n\ge2\), let \(r_i,c_j\) be the binary row and column sums of a selected-board indicator matrix \(x_{ij}\). The closed-neighborhood rule is equivalent to \(x_{ij}=1+r_i+c_j\) over \(\mathbb F_2\). Re-summing gives \((n+1)r_i=n+T\), \((m+1)c_j=m+T\), with \(T\) the common total row/column parity. The four parity cases are necessary and sufficient; in the odd--odd case the row/column parity vectors uniquely identify the two diagonal rectangles. Binomial counting then gives every coefficient. The fixed-\(b\) affine weight argument establishes the global minimum and all equality cases.

The direct closed-neighborhood exhaustive checker passed on all nine boards \(2\le m,n\le4\); a separate binary Gauss--Jordan affine solver passed on all thirty-six boards \(2\le m,n\le7\), including the exact \(5\times5\) histogram. Source paths and reproduction instructions appear in VERIFICATION.md. These finite tests cross-check but do not prove arbitrary dimensions.

## Originality — PASS, with historical uncertainty

The 2013 Giffen--Parker original article (entire sixteen-page published PDF inspected) develops parity domination and Lights Out on complete bipartite graphs, not on their line graphs. The 2017 Peters--Goldwasser--Young Cartesian-product article concerns universal solvability; the abstract was inspected but full text was not obtained. The 2021 Berman--Borer--Hungerbühler full-text HTML concerns general linear-algebra solvability and minimum-press hardness, not a displayed rook-board enumerator. Targeted searches of rook graph, odd domination, Lights Out, switching, and weight-enumerator terminology did not uncover the present formula. The latter absence is evidence only within searched sources, not a proof of historical priority.

A pre-existing Hamming-product Lights Out nullity result already gives the *number* of all-on solutions for these graphs. That value is not newly claimed: it is the evaluation \(W_{m,n}(1)\). Knowing just nullity/total counts does not fix the weight enumerator or the unique two-rectangle parameterization. The main theorem is thus stated as the full weight distribution and structural solution classification, and its minimum-profile consequences. Inaccessible full 2017 text and unindexed computations are residual risks.

## Value — PASS

The exact number of all-on winning button sets does not reveal how many presses are needed. The full size enumerator on the natural line-graph/rook-board family answers that optimization-and-multiplicity question simultaneously in all board sizes. It exposes a strong parity transition: even-by-even boards have only the full-board press pattern, whereas odd-side boards admit exponentially many, with shortest patterns consisting of full rows or columns. The diagonal-rectangle description identifies the entire binary affine solution code geometrically, so the contribution is structural rather than a finite table or routine restriction to a tiny graph.

## Limits

The 2017 paper remains a plausible inaccessible source for special cases; the priority assessment is consequently best-knowledge only, not independent certification. Nonbinary rules, arbitrary initial lightings, and products with more than two complete factors remain unaddressed.

Self-review: passed. Independent audit: not yet performed.
