# Mathematical review

## Correctness — PASS

The classical Apéry Lucas congruence and the explicit eleven initial digit values isolate precisely the forbidden digit \(5\). The two-state carry matrix enumerates every ordered pair modulo \(11^r\). Its row sums are either \(9\) or \(10\), with both carry states positive after any first target digit other than \(10\); this gives the exact minimum \(9^r\), its \(10\cdot9^{r-1}\) maximizing-target complement, the unique maximum \(10^r\) at \(-1\), and full target coverage. The signed-difference carry matrix is reconstructed from an exact two-digit correlation and has symmetric-sector characteristic polynomial \(z^2-923z+12150\), proving the energy recurrence. Finally, finite-state ergodicity proves biased limiting digit frequencies (hence singularity), and a positive matrix eigenvalue yields the exact cylinder-correlation dimension. Independently recomputed finite spectra and the underlying matrix entries in `CHECK.py` support but do not replace these proofs.

## Originality — PASS, with specified residual risks

Gessel's 1982 congruence supplies the arithmetic digit law. Luca–Shparlinski (online 2008-07-08) addresses distribution of large factors in Apéry values; Malik–Straub (arXiv:1508.00297) studies Lucas congruences, nondivisibility and periodicity; Rowland–Yassawi–Krattenthaler studies congruences of Apéry values modulo prime squares. Those statements do not imply the exact *additive convolution of indices* without a new digit-carry analysis. The closest accessible published digital-convolution result (record 0a6383f8b10e) has a different digit set, base, group, and ordinary-integer rather than modular equality. Semantic searches covered aliases such as digit-deleted Cantor sets, two-sum fibers and additive energy. A previously published general finite-type framework could potentially derive this special calculation, and archival unpublished equivalents cannot be excluded; those risks are not treated as established novelty.

## Mathematical value — PASS

The index set is determined arithmetically, not chosen as an arbitrary digital slice. The output is a complete, exact and usable prime-power additive representation criterion for that set, with sharp target-by-target extremes and a closed all-depth fourth-moment recurrence. A full-support but singular \(11\)-adic convolution with dimension extremely close to one provides a structural contrast between additive coverage and measure regularity. These invariants refine the known nondivisibility digit law; they are not merely a restatement of it.

## Scope and remaining limitations

Results are for the classical Apéry indices at eleven. The correlation dimension refers to square cylinder masses in \(\mathbb Z_{11}\), not Euclidean correlation. No optimal higher \(L^p\) or Fourier properties are claimed. The historical origin of Gessel's 1982 result is recorded without inventing its exact first-public day. Supporting primary sources and an exact prior digital-convolution comparison are itemized in `AUDIT.json`. Computation is finite and independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
