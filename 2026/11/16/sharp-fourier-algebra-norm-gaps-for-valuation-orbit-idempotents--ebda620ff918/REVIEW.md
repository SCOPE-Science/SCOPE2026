# Scientific review — sharp valuation-shell Fourier-algebra norm gaps

## Correctness — PASS

The statement uses the probability-normalized Fourier transform on a finite abelian group and exactly specifies the common-index subgroup chain and all terminal layers. Restricting a function supported in a subgroup does not alter its Fourier-algebra norm because each subgroup character has equally many extensions. For the first occupied shell, splitting characters into those annihilating the next subgroup and the remaining extensions gives the exact recursion
\[
\|\mathbf1_E\|_A=2(1-q^{-1})+\|\mathbf1_F\|_A-2(1-q^{-1})\mu.
\]
The inequalities \(\|\mathbf1_F\|_A\ge1\) and \(\|\mathbf1_F\|_A\ge2\mu\) for nonempty proper \(F\) give the strict nonbinary gap. When \(q=2\), their joint equality requires \(\mu=1/2\) and \(\|\mathbf1_F\|_A=1\); radiality forces the two stated adjacent-layer choices. Annihilator character counts give the full exact formula. The standalone checker independently tested 3,556 exact rational patterns and 104 direct complex finite Fourier transforms. Those tests support, but do not replace, the arbitrary-depth proof.

## Originality — PASS relative to inspected evidence

Vujičić's 2026 orbit-hypergroup paper motivates the valuation-orbit symmetry and treats Fourier-algebra structure and amenability, not the sharp lower-end norms of radial indicator idempotents. The general coset-ring results of Green–Sanders (2008) and Sanders (2020) do not explicitly give the \(q\)-dependent equality classification; Sanders's full article was inspected for its theorem statements and subgroup-character formulas. Searches for radial shell Wiener norms, equivalent nested-chain idempotent gaps, and finite-ring Fourier projections found nearby concentration and square-residue studies but no statement implying the exact all-depth result. The classical Fourier transform of subgroup indicators is prior mathematics and is not claimed as a discovery.

The 1968 Saeki paper on small idempotent norms is an important residual risk; only its abstract and bibliographic information were accessible, not the complete proof. It may contain broader results from which part of this theorem follows. Its unavailable full text prevents a definitive historical uniqueness assertion, but the inspected evidence does not establish implication of the exact radial equality families and arbitrary common-index chains.

## Value — PASS

Valuation orbits are a natural symmetry class in local-ring harmonic analysis. The minimum nontrivial Fourier-algebra norm measures how far a nonball idempotent is from a norm-one subgroup projection. Here this has a dimension-free, depth-independent answer determined by branching index, with a genuine binary structural exception and complete minimizers. The exact rational transform formula additionally makes all indicator norms computable without enumerating the ambient group. These answers are meaningful for the explicit orbit family, not merely arbitrary small numerical examples. No larger nonradial or nonabelian statement is claimed.

Self-review: passed. Independent audit: not yet performed.
