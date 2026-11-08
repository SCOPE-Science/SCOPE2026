# Scientific review

## Correctness — PASS

The fixed atom-order chamber is polynomial in the independent mass parameters; its free parameter count is an upper bound on image dimension. In a concrete chamber with deterministic baseline ranking, changing one atom mass creates a unique nonidentity permutation for every alternative. The \(n\) binary and \(2n\) ternary alternatives have pairwise distinct permutations for all \(n\ge4\), giving independent Jacobian columns. Nonzero polynomial minors persist in the strictly positive mass interior, establishing the matching lower bound. The standalone standard-library checker confirms 30,465 finite scalar witness conditions and an independent exact three-variable determinant; the uniform all-order construction, not those finite checks, proves the theorem.

## Originality — PASS, subject to independent priority assessment

The direct motivating paper of Turvey (2026), Section 6, Problem 2, poses \(\dim\mathcal A_{n,k}\) as an open direction and proves only unrestricted dimensions. Babson et al. (2024/2026), §5.4, already contain a three-label example with at most three atoms and a full-rank draw matrix, so no novelty is claimed for that prior case. Their unrestricted rank theorems and small-order unrestricted table do not imply the all-order \(n\) and \(2n\) support-stratum dimensions. Comparisons with published ordering-polytopes and order-marginal identification findings found different independence assumptions and invariants. Residual risk: an equivalent finite-dice dimension theorem may exist under another formulation; no full literature census or independent priority audit was made.

## Mathematical value — PASS

The two equalities answer the first two nonconstant atom-budget cases of a specific published research question, including a uniform witness and a sharp parameter-dimensional interpretation. They are structural results for all \(n\ge4\), not arbitrary enumeration or simple substitution into unrestricted dimension formulas. They do not classify the attainable region, its boundary, or support budgets \(k\ge4\).

## Relationship to earlier results and limitations

The unrestricted dimension and Jacobian technique are prior knowledge. The novel scope is the sharp binary/ternary *support-constrained* image dimension for all \(n\ge4\). The finite checker cannot certify an infinite statement on its own. Mathematical validity is supported by the explicit general proof, and historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
