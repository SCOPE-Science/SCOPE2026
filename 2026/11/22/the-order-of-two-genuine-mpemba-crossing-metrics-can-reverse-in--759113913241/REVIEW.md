# Review: metric-order reversal in a reversible three-level thermal gate

## Correctness — PASS

The forward generator has exact independent slow middle-occupation and fast outer-imbalance modes, with rates \(a\) and \(ar+c(1-r)\). Weighted orthogonality gives the squared Hilbert distance, while sign analysis gives a different piecewise-affine total-variation distance. Under strict slow-mode inversion, each distance has one and only one positive crossing. Two exact rational examples certify opposite timing orderings, including root-region checks. `checker.py` recomputes the generator relations, modal and variation identities, and witness inequalities in exact arithmetic; analytic proofs supply the unrestricted quantifiers. The existence threshold is a derivative calculation and is acknowledged as a specialization of known modal geometry.

## Originality — PASS (qualified)

The core comparison concerns the order of *two distinct genuine distance metrics*, not the existence of Markovian Mpemba relaxation itself. Lu–Raz (2017) and Gelbwaser-Klimovsky (2026) establish the broader three-level slow-mode geometry. Pardhi–Abbas–Das (2026) cover a genuine Hilbert metric in continuous-state diffusion; Taye (2026) analyzes relative-entropy timing and energy. An accessible previous finite-state Hilbert zero-count result implies the Hilbert uniqueness, but has no TV crossing-time comparison. Exact scans of relevant public statements and literature did not find both rationally certified opposite metric orders for this gate. Full-text access to one earlier 2026 necessary-conditions paper was incomplete; a stronger later full paper was inspected. Wider implicit-prior coverage remains possible. Failed searches are not novelty certificates.

## Value — PASS

Comparative Mpemba timing is sensitive to the measuring distance even when both are true and contractive. The explicit sharp contrast, two complete exact examples, and analytical hinge criterion make this a meaningful boundary for selecting a relaxation diagnostic; the new value is not the known general condition for existence. This is a finite-state mathematical benchmark, not a prediction for physical water cooling or noisy observation.

## Closest sources and limitations

Primary sources and the accessible full-text comparisons are listed in `RESULT.md` and `AUDIT.json`. The proof is limited to a three-level canonical Gibbs gate, \(0<a<c\), with a fixed bath for each pair. A different source may implicitly contain equivalent results. No independent audit or experimental verification is claimed.

Self-review: passed. Independent audit: not yet performed.
