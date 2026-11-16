# Scientific review

## Correctness — PASS

For all integers \(m\ge2\) and \(0<r<1\), even-modulation character orthogonality restricts the frame operator to exact coordinate pairs. The two adjacent translations give the explicit \(2\times2\) blocks, all with strictly positive determinant \(D=r^{2m-2}(1-r^2)^2\). Strict convexity of block traces and the endpoint inequality select the global extremal block, proving the sharp bounds. Normalizing by \(\sqrt D\) produces \(X=2\coth s\cosh((m-1)s)\); its logarithmic derivative has one root and yields the unique taper. Monotone-root convergence proves the sharp dimension limit. Rational arithmetic checked 44 determinant/trace instances and an separate direct complex synthesis calculation checked 44 full matrices; ten optimum cases and the radical endpoint were also tested. No computer experiment is used as an infinite proof.

## Originality — PASS relative to the checked sources

**Closest source:** Asipchuk–De Carli–Rodriguez, arXiv:2605.16139 (first released 2026-05-15). Full accessible HTML was examined, including its abstract, Theorem 1.1, Corollary 1.2, Theorem 1.3, and the structural development. It covers block decompositions for subgroup modulations, a general mechanism used in the proof, but does not provide the window-specific extreme eigenvalue optimization or dimension-asymptotic constant. The full online manuscript *A phase-alphabet trichotomy for critical two-translation cyclic Gabor bases* was read: its phase-only orthogonal windows and exact alphabet counts concern different input assumptions and objective. Faulhuber–Shafkulovska's *Gabor frame bound optimizations* was inspected at the introduction, propositions 2.10–2.11 and the two-sided-exponential analysis in Section 9; its continuous \(L^2(\mathbb R)\) lattices with redundancy greater than one do not imply sharp finite cyclic critical-basis bounds. A limiting hyperbolic equation appears in broader analysis and is not asserted novel by itself.

Research-index searches also considered geometric cyclic windows, finite two-translation Gabor bases, even-modulation subgroup frames, polyphase spectra and exponential-window conditioning; the closest identified results were compared by their mathematical implications rather than only titles. Residual risk: older finite polyphase or circular-exponential calculations may implicitly derive the same optimized family. Searches cannot establish absolute publication priority.

## Value — PASS

The nonflat positive graph-distance exponential is a natural localized discrete signal window, while the chosen square Gabor system is a standard critical reconstruction design. The theorem identifies a complete, nontrivial trade-off: every fixed taper is a basis, but both excessive concentration and excessively flat windows are poorly conditioned; the optimal taper is unique and depends on ambient dimension, and even the best possible stability necessarily degrades quadratically with a sharp constant. This is a useful exact finite-family design law rather than a change of notation or a routine incremental numerical estimate. It does not claim optimality among arbitrary windows.

## Limits and independent verification

The theorem is restricted to the specified window and critical sampling pattern. Historical literature beyond the inspected sources may contain an equivalent theorem. Checks are finite reproducibility tests; independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
