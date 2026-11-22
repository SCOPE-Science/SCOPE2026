# Scientific review: slope-sensitive shattering of Sturmian factors

## Correctness

**PASS.** The theorem specifies a one-sided binary Sturmian factor language with the symbol-one frequency equal to the irrational rotation slope. Its zero-padding convention matches the variable-length set family rather than the classical fixed-length mask family. A phase-cell argument shows that every relevant trace is realized by a dense rotation orbit, including handling coincident arc endpoints. For small slope, two short translated arcs restricted to a last-positive arc yield at most three traces, excluding all triples. For large slope, three earlier arc indicators on a last-positive arc have at most seven trace cells, excluding all quadruples. Explicit overlapping and disjoint complementary arcs furnish a shattered triple. The pair and triple criteria follow from the same phase argument. An independent exact-arithmetic finite checker passed 7,808 comparisons; its use is corroborative only. A direct golden-ratio-slope triple witness was also checked. No infinite conclusion is based solely on computation.

## Originality

**PASS, with recorded access and priority qualifications.** The closest definitional source is Hunter Johnson, *Binary strings of finite VC dimension* (arXiv:2101.06490, 2021), which distinguishes full variable-length VC dimension from equal-length mask dimension by at most one and does not determine the exact Sturmian slope transition. Earlier work by M.-P. Muller (2005), according to its accessible abstract, proves the Sturmian *mask* VC dimension equals two; this is credited and expressly excluded from the originality claim. Combining these results already implies a full VC upper bound of three: that deduction is also excluded from novelty. The exact two/three slope dichotomy, pair-support arithmetic criterion, three-support arc criterion, and asymptotic pair density are the assessed claims. Relevant semantically searched research records concern related Sturmian shift factors and forbidden-block shattering but not an implication covering this exact result. The complete Muller preprint was inaccessible, and undetected alternative terminology or unindexed work may limit priority.

## Value

**PASS.** This settles the exact cardinality for a natural variable-length Sturmian factor concept class on both sides of a sharp symbol-frequency boundary, classifies all supports rather than only a scalar dimension, and yields an arithmetic limit for the density of shattered pairs. The difference under binary symbol complementation isolates a genuine distinction between classical fixed-window shattering and variable-length factor shattering. The theorem is motivated directly by a published mathematical question and its adjacent, previously established two-sided bound; it is not a rephrasing of that bound.

## Limitations and closest literature

The theorem does not give a simple closed finite-horizon count of large-slope shattered triples or any online-learning dimension. The 2005 Muller document is cited on accessible abstract evidence without falsely claiming its complete contents were checked; future full-text comparison could change historical attribution. The original 2021 Johnson paper's definitions, general inequality and question were inspected in its PDF. The finite checker uses rational rotations as tests only. Independent mathematical audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.
