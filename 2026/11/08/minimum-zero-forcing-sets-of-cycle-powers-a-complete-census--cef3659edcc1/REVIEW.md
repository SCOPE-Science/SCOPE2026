# Review of minimum zero forcing sets of cycle powers

## Correctness — PASS
The first-force argument is an exact characterization because the graph is \(2k\)-regular and has exactly \(2k\) initially blue vertices. Reversing the argument produces a consecutive closed neighborhood which forces outward. Counting representations by overlaps of consecutive complementary arcs yields the all-parameter \((2k-1)n\) count and distinguishes all orbit types. The two boundary cases use direct complete-graph and antipodal-matching reasoning. Exhaustive graph-level enumeration for \(36\) parameter pairs and additional larger representation checks corroborated the general proof; the infinite conclusion rests on that proof.

## Originality — PASS (best-knowledge, not independently certified)
The closest scalar theorem is Abiad–Flagg–Ghasemi Nezhad–Zeijlemaker (2026), Proposition 8, preceded by Deaett–Meyer (2015/2016), Theorem 5.4; each proves \(Z(C_n^k)=2k\), not the number or type of optimal sets. Boyer et al. (2018), Theorem 1 and Propositions 3 and 6, already imply both short-cycle counts and the ordinary-cycle case, which are identified as prior. Menon–Singh (2025) proves broader coefficientwise inequalities for graph operations, with no identified exact multiplicity for these powers. Relevant exact graph-power, cyclic-circulant, coefficient and equivalent-term searches, and comparisons to available mathematical result records found no claim dominating the new classification for \(k\ge2, n\ge2k+3\). The source-access gap and unknown-literature risk are retained in AUDIT.json.

## Mathematical value — PASS
The sharp new linear count has a structural explanation that applies uniformly for two unbounded parameters: the count of initial-force descriptions is \(2kn\), and exactly \(n\) configurations are double-described. This gives precisely \(k\) dihedral optimizer orbits and exact multiplicity of the first nonzero coefficient of the zero forcing polynomial in the natural graph-power family, complementing the previously known scalar invariant. The result makes no claim about the remaining coefficients.

## Limits
No independent mathematical audit or independent literature-priority certification has been performed. Counts for the complete and near-complete cases were known implications. The coefficient result applies to standard ordinary zero forcing and labelled cycle powers, not other graph families or variants of forcing. Full text of one broad related 2025 journal source could not be comprehensively checked, although its accessible core statements concern coefficientwise inequalities and graph operations rather than the asserted exact enumeration.

Self-review: passed. Independent audit: not yet performed.
