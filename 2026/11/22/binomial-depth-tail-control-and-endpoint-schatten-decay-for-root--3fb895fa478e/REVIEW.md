# Review of the rooted-tree Aluthge depth-tail theorem

## Correctness

**PASS.** Orthogonality of distinct parent columns gives the exact Schatten \(p\)-energy \(\sum_v\rho_v^p\) for every \(p>0\). Direct polar decomposition yields the child-weight formula. A nonstandard but elementary branching inequality dominates the next energy vector by \(((1-t)I+t\mathcal Q)\) applied to the previous one. Unique parent paths yield an exact summation identity for the powers of \(\mathcal Q\); binomial expansion, Tonelli, and dominated convergence prove the global estimate and endpoint convergence. Chernoff gives the explicit tail rate; finite constant-weight paths prove the absence of a uniform rate. A self-contained standard-library finite checker passed 30,516 assertions; this supports computation but does not replace the infinite proof.

## Originality

**PASS, with bibliographic qualification.** The closest direct statement is Stanković (2026), Proposition 5.8, for classical unilateral weighted shifts; his Corollary 5.9 includes orthogonal direct sums of such shifts and finite blocks. The new theorem handles genuinely branching trees that cannot be in that direct-sum class, supplies a branching energy transport inequality, and controls all iterates by the initial depth distribution. Trepkowski (2014) gives the one-step tree weight formula; it is not an iterated Schatten endpoint theorem. Bala (2026) gives operator-norm convergence rather than same-class Schatten convergence. Altwaijry et al. (2024) give Schatten norm inequalities/equality criteria for transforms, not this depth-tail limit. Searches for aliases, broader coverage, special cases and indexed related claims did not reveal an implication covering the new conclusion. A full exclusion of unpublished or less-indexed results is not established.

## Value

**PASS.** The motivating 2026 result leaves equal-Schatten-class convergence outside its general theorem and treats only one-path unilateral shifts in its explicit endpoint proposition. The branching theorem gives a sharp natural class enlargement (including nonreducing infinite trees), a computable bound from the initial distribution of column norms over depth, a quantitative exponential-plus-tail estimate, and a rigorous obstruction to any distribution-free rate. These provide functional-analytic control not captured by mere operator-norm convergence or finite experiments.

## Closest sources and limitations

Closest primary sources: Stanković (arXiv:2611.07728v1), Trepkowski (arXiv:1401.4415v1), Bala (arXiv:2602.07916v1), and Altwaijry–Conde–Feki–Stanković (DOI:10.3934/cpaa.2024078). The theorem does not address rootless trees, cycles, multiple-parent graphs, backward shifts, arbitrary compact operators, or the parameter endpoint \(t=1\). Related indexed results for weighted partial permutations and finite-star shifts were compared at their published summaries rather than claimed as complete text inspections.

Self-review: passed. Independent audit: not yet performed.
