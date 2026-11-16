# Scientific review

## Correctness — PASS
The claim is finite and completely specified: the nine ice-rule equations on a labelled eighteen-edge simple torus select exactly 148 binary orientations. Two independent exhaustive generators agree state-for-state. The direct sums over all 1,024 quotient frequencies agree with the full 262,144-entry exact-integer Walsh transform, the full signed histogram, and Parseval. The independently transformed Fourier-support mask has absolute kernel sum 1,822,720. Counting convolution is diagonal in Walsh characters; translation averaging proves that the displayed endpoint norm is the unrestricted minimum, not only an invariant-projector bound. Proof scope and computational bounds are explicit in `RESULT.md` and the checker.

## Originality — PASS, with bounded historical risk
The closest primary results concern finite and asymptotic periodic six-vertex partition functions with local vertex or homogeneous integrable weights (Tavares–Ribeiro–Korepin, arXiv:1501.02818, especially sections 2–3 and 7; Jacobsen–Jiang–Zhang, arXiv:1812.00447, especially sections 2, 4 and 7). The unsigned orientation count 148 is already recorded in OEIS A054759 and is expressly not new. Those inspected results do not give the full independent edge-sign Walsh distribution, the extra even-frequency nullity, or sharp unrestricted projection constant. Published mathematical-record comparisons included Eulerian orientations of squared cycles and their winding-sector counts, which are not the same graph or object, and earlier accessible related claims concern acyclic rather than Eulerian orientations. The novelty comparison is one of mathematical implications, not only matching titles. An unlocated older fully inhomogeneous signed torus calculation is a residual priority risk.

## Value — PASS
This is a natural complete finite classification at the smallest simple four-valent periodic square-ice torus, rather than an arbitrary subcase: it separates the classical unsigned count (148) from recoverable Fourier dimension (99,328), reveals 31,744 even-weight cancellations not explained by global arrow reversal, gives the sharp Hilbert-space deconvolution gap four and condition number 37, and determines the optimal endpoint projection constant. The exact full-character benchmark is useful for checking analytic or numerical treatments of inhomogeneous signed ice and for understanding information loss in finite convolution models. It does not purport to settle larger tori.

## Residual limits
The exhaustive certificate is specific to the 3-by-3 simple torus. The source search was bounded; all publication-priority conclusions remain best-knowledge and not an independent certification. No external independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
