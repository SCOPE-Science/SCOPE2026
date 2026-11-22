# Review of the positive geodesic-mixture Fourier theorem

## Correctness — PASS
The exact claim quantifies over every integer \(N\ge1\), every finite positively weighted family of complete primitive torus geodesics, and every signal in the full square Fourier band. The proof reduces off-diagonal Parseval constraints to one perpendicular direction per nonzero Fourier difference, then uses identity Toeplitz moments to force the directional loop counts. The equality case and unique global optimizer follow from strict lattice-length arithmetic. The reproducing program tests 51 complete Gram systems and finite exact length inequalities; the analytic proof supplies the all-parameter quantifiers. Risks: numerical examples cannot replace the proof, and the result is only for complete geodesic components.

## Originality — PASS with historical-priority qualification
The closest previous single-slope result treats parallel geodesics with equal weights and does **not** establish no-cancellation between distinct slopes. Original primary works on Euclidean mobile sampling (Rashkovskii–Ulanovskii–Zlotnikov, 2020) and spherical t-design curves (Ehler–Gröchenig, 2023) were inspected in relevant full HTML sections. Later torus design curve work (Kunis, 2026; Ehler, 2026) was inspected at abstract level only; no accessible statement directly covers the full positive-mixture theorem. Literature-index searches on Fourier geodesic mixtures, aliases and optimization did not return an equivalent claim. Residual priority risk: unread later full texts or unindexed classical design equivalences.

## Mathematical value — PASS
The result settles exact energy-preserving multi-trajectory acquisition over the natural finite-geodesic measurement class, including arbitrary positive relative weights and all primitive slopes. It gives a universal additive per-direction arclength lower bound, attained simultaneously for both coordinate slopes but strictly exceeded when at least three slope classes are used, and proves that no directional hybrid outperforms the simple coordinate design. This is a structural and design-relevant obstruction, not merely another small computed example. It does not optimize arbitrary rectifiable paths or sensor relocation.

Self-review: passed. Independent audit: not yet performed.
