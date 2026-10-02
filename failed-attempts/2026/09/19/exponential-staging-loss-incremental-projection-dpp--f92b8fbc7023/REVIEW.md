# Review status

Fresh independent mathematical audit: **failed**.

- Correctness: **PASS** — The singleton-stage construction is correct. In the codimension-one projection-DPP model, the final sample omits one coordinate and the omission weights are the squared coordinates of the null vector. The hierarchical Givens choice makes each newly introduced weight negligible relative to every old omission weight, so the conditional inverse-weight expectation gains a factor \(2+o(1)\) at each stage. At final rank, the Schur-complement identity gives normalized orthogonal CSS error \(1/(a_j+\sigma^2 b_j)\); because \(\sigma^2/\min_j a_j	o0\), this is uniformly \(a_j^{-1}(1+o(1))\). Hence the staged expectation tends to \(2^d\), while one-shot projection DPP has omission law \(a_j\) and expectation tending to \(d+1\).
- Originality: **FAIL** — A published September 18 result, 'Worst-case sharpness of multistage adaptive randomized pivoting', was read in full and strictly covers the assigned theorem. It proves sharpness of \(\prod_i(k_i+1)\) for every stage partition, proves the same sharpness for actual orthogonal CSS, and states the singleton-stage corollary \(2^d\) versus \(d+1\) on the same final subspace. The assigned distinct-leading-singular-value refinement removes a basis-degeneracy nuisance but does not change the covered scientific conclusion.
- Value: **FAIL** — The mathematical phenomenon is worthwhile, but this September 19 record is a special-case rederivation of a stronger September 18 published theorem. The extra choice of distinct leading singular values is a robustness normalization, not an independently motivated new invariant or boundary. Under the shared bar, the record adds no separate scientific value.

Detailed structured comparisons and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
Earlier scientific assessment evidence is retained in `AUDIT.json` as historical evidence.
