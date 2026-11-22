# Review: equal-orbit sampling in unitriangular radical braces

## Correctness — PASS
The actual theorem concerns one orbit uniformly among distinct \(\lambda\)-orbits, with \(q\) fixed and \(n\to\infty\). The proof identifies an orbit-invariant suffix-rank increment set and proves the exact weight \(\prod_i(q^{m_i-i+1}-1)\). Each orbit has exponent \(\binom{k}{2}+\delta\), where \(\delta\) is a partition deficit. The upper partition-generating-function bounds and the lower latest-increment weight together imply uniform expectations of \(|k-n/2|\) and \(\delta\). The resulting \(O_q(n)\) exponent-error bound is a true all-dimension theorem; independent finite enumerations of small orbits were used only as cross-checks. Characteristic and \(n=2\) boundary cases are included.

## Originality — PASS, with residual risk
The left action, old exact finite transfer, and \(q\)-Stirling total and rank marginals are **not new**. In particular an existing same-family finite size transfer already calculates every orbit-size multiplicity, so merely reproducing that census would be covered. The final claim is instead the uniform-in-dimension \(L^1\) theorem for **equal-orbit sampling**, and the bounded partition-defect mechanism. The earlier uniform-*point* law neither states nor proves this opposite-measure asymptotic. Properzi–Van Antwerpen, Yan, Cai–Ehrenborg–Readdy, and Bevan–Cheon–Kitaev were inspected; no matching uniform-orbit concentration theorem was found in those works or the examined related research records. An unlocated equivalent analytic corollary remains possible, so no independent historical priority is asserted.

## Value — PASS
Uniform sampling of symmetry classes and uniform sampling of labeled objects are two natural, inequivalent ensembles. In this family, the first yields exponent coefficient \(1/8\) and the second \(1/2\), a macroscopic fourfold bias. The tight partition defect and tight half-rank fluctuations supply structural reasons for this difference, beyond a routine finite count. The contrast may guide interpretation of orbit statistics in other finite algebraic actions.

## Limitations and sources
The constant depends on the fixed field order; no sharp \(n\)-scale limit distribution is proved. Key sources: Properzi–Van Antwerpen (arXiv:2306.12415); Yan (arXiv:1004.2674); Cai–Ehrenborg–Readdy (DOI:10.37236/6829); Bevan–Cheon–Kitaev (arXiv:2311.08023); and OEIS A135922/A139382. Earlier finite enumeration and prior uniform-point asymptotics are explicitly excluded from the novelty claim. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
