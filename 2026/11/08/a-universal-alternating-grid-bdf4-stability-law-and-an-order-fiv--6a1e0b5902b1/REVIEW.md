# Review of a universal alternating-grid BDF4 stability law

## Correctness — PASS

For standard polynomial-interpolation BDF4 on an exact two-periodic mesh, the Lagrange-derivative coefficients produce a three-dimensional difference recurrence. The displayed rational one-step transfer leads to the characteristic polynomial with coefficients \(D,A,B,C\). The four explicit strictly positive Schur/Jury numerators prove that all parasitic two-step multipliers have modulus below one for **every** \(q=r+r^{-1}\ge2\), not merely for enumerated ratios. The limiting monodromy polynomial \(\lambda^2(\lambda+1)\) proves the unattained sharp spectral-radius supremum. An independent rational reconstruction for BDF5 at \(r=10\) yields a quartic negative at \(-1\) and positive toward \(-\infty\), rigorously witnessing an eigenvalue smaller than \(-1\). The embedded exact-rational checker passes 169 assertions. Finite checks confirm identities but do not replace the universal polynomial proof.

## Originality — PASS, qualified

The directly relevant 2018 smooth-grid BDF article proves stability when successive ratios tend to one as the grid is refined; its hypotheses exclude fixed alternating ratios away from one. The 2022 variable-grid stability paper treats only BDF2/BDF3, not orders four and five. The 1990 variable-order/variable-step BDF paper describes sufficient bounds for general mesh ratios, not an identifiable exact unrestricted alternating-grid result in its accessible abstract; attempts to access its full text were unsuccessful. The new fourth-order characteristic polynomial, global all-ratio sign certificate, sharp limiting boundary, and explicit fifth-order obstruction are not implied by the accessible reviewed statements. Residual risk: an older specialist periodic-grid theorem, potentially in the unavailable 1990 full text, could contain overlapping results; specialist review is warranted. Absence of a database hit is not treated as proof of novelty.

## Value — PASS

Zero-stability is a prerequisite for reliable linear multistep integration. Common sufficient restrictions on arbitrary step-ratio sequences can be highly misleading for structured alternating grids. The exact no-ceiling fourth-order result, coupled to an order-five counterexample and an unattained limiting spectral boundary, distinguishes cancellation over two steps from an unsafe general-grid extrapolation. This is a structurally motivated higher-order stability boundary, not an arbitrary numerical slice or small parameter improvement.

## Literature and limitations

The primary inspected works were Söderlind–Fekete–Faragó, arXiv:1804.04553 (full open-access HTML), and Li–Liao, arXiv:2201.00527 (full open-access HTML). Calvo–Grande–Grigorieff, *Numerische Mathematik* 57 (1990), DOI:10.1007/BF01386395, was inspected at the abstract/metadata level only; full-text access failed. The stability theorem holds for each fixed two-periodic ratio, not all nonperiodic grids and not uniformly as the ratio becomes extreme. It is a zero-equation result; it gives no nonzero-test-equation absolute-stability theorem.

Self-review: passed. Independent audit: not yet performed.
