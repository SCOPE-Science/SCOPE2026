# Independent Audit — 2026/09/17/sharp-reciprocal-critical-point-diameter-bound--db97b9e9d71d

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `deb748f84aa0a8db8b262452a36eefc18079fb4b`
- Disposition: **FAILED**

## Correctness

**PASS** — The collinear diameter inequality is mathematically sound. After rotating the common zero line to R, reciprocal critical points can be represented by the spectrum of the real-symmetric matrix similar to D_0(I+J). The Ky Fan sign-subspace compression yields the displayed two-sided lower bounds on the positive and negative reciprocal spectral masses; the diameter argument then forces sum |a-zeta|^{-1} >= 2(N-1)/D, with strictness for zeros on both sides. Power means give every lambda>=1, and the equality analysis for the endpoint cluster and for lambda>1 is correct. Independent random real-root stress tests performed during the audit found no counterexample.

## Originality

**FAIL** — The headline theorem is prior-covered. Teng Zhang's public website currently hosts a manuscript titled “Sharp Reciprocal-Moment Inequalities for Critical Points of Polynomials with Collinear Zeros” whose abstract and Theorem 1.2 state the same scale-invariant inequality, the same sharp constant, the same equality cases, and the same implication for the Tang-Zhang conjecture. More decisively for chronology, the GitHub history of zhangteng2000/zhangteng2000.github.io contains a commit dated 2026-08-16 deleting `files/Sharp_Reciprocal_Moment_Inequalities_Collinear_Zeros.pdf`; fetching that path at the parent revision succeeds. Thus a public manuscript with the exact theorem title existed more than a month before this SCOPE record's 2026-09-17 publication. The present proof may use a different matrix route, but the research claim itself was not new.

## Scientific value

**FAIL** — The theorem is mathematically worthwhile—it resolves the reciprocal-moment conjecture for collinear zeros—but that scientific value belongs to an already public prior result. The submitted record adds at most an alternative matrix/Ky-Fan proof and a stronger-looking intermediate estimate without demonstrating a new consequence beyond the already established sharp theorem. As an independent finding it therefore lacks sufficient incremental scientific value.

## Sources

- Sharp Reciprocal-Moment Inequalities for Critical Points of Polynomials with Collinear Zeros (Teng Zhang): https://zhangteng2000.github.io/files/Sharp_Reciprocal_Moment_Inequalities_Collinear_Zeros.pdf — Current public manuscript states the exact same diameter theorem and equality cases.
- GitHub commit deleting the prior reciprocal-moment manuscript (Teng Zhang website repository): https://github.com/zhangteng2000/zhangteng2000.github.io/commit/50a8af21975196bde9eb359fe1ad61fb4000fd4e — Commit timestamp 2026-08-16T03:09:33Z deletes the PDF with the exact theorem-title filename; the file is retrievable at the parent revision, establishing pre-2026-09-17 public existence.
- Sharp Schoenberg type inequalities and the de Bruin--Sharma problem (Q. Tang; T. Zhang): https://arxiv.org/abs/2508.10341 — Source of the reciprocal-distance conjecture and companion-matrix framework.

## Limitations

- The rejection does not challenge the submitted proof or its intermediate Ky Fan estimate; it is based on prior coverage of the main scientific theorem.
- The old August PDF blob differs from the current website blob, so this audit does not assert byte-for-byte identity of versions; the exact title/filename and pre-record public existence, combined with the current exact-overlap theorem, are the priority evidence.
- No claim is made about which proof was discovered independently; the audit assesses originality of the deposited research claim.

GitHub was read only as evidence; no repository mutation was performed. Open-access/preprint sources were checked first. Oxford Download was not needed for this record.
