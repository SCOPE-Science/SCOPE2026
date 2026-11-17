# Scientific review: U-domain polynomial reach and first-contact phases

## Correctness — PASS
For all four positive geometric parameters, the two single-elbow rectangular offsets and the opposing-arm overlap decompose the Euclidean outer offset by exact set inclusion–exclusion. The single-elbow deficit is \(s^3/(6q)+O(s^4)\) after the depth cutoff, while the two opposed arms overlap first at half the channel width, producing an upper-half circular lens of area \((4/3)\sqrt{g}\,s^{3/2}+O(s^{5/2})\). When the depth exceeds the half-width an additional strip gives the negative linear term. These calculations independently establish all boundary cases and the claimed exact polynomial reach. The standard-library verifier passed 75 area and asymptotic checks; finite checks do not prove the theorem.

## Originality — PASS, provisional priority
The closest full-text source is Cholaquidis (2026), arXiv:2607.24487, which proves local polynomiality and handles one L-shaped reentrant corner. Cholaquidis–Cuevas–Moreno (2023), arXiv:2307.00373, defines polynomial reach and treats other examples. A single L-shaped correction does not imply the new nonlocal collision term between opposed arms. Searches for U-domain offsets, paired reentrant corners, exact reach, and half-channel contact did not identify a competing all-parameter phase diagram, but searches cannot establish priority exhaustively. In particular, a previously computed exact single-elbow result does not cover the two-arm interaction. Possible unpublished morphology calculations remain a priority risk.

## Mathematical value — PASS
The threshold \(\min\{q,g/2\}\) and the three sharp, different first-contact orders give a complete geometrically natural phase classification for connected eight-vertex nonconvex polygons. It separates local reentrant-corner rounding from a nonlocal medial-channel collision and identifies a critical coalescence at which the smoothness law changes. The dimensions and exponents make the exact result useful for tube-formula examples and estimating polynomial reach rather than merely a computation for one sample polygon.

## Limitations
The statement is restricted to equal-thickness side arms, right-angle corners, positive lengths and Euclidean outer offsets. It does not determine all subsequent collision radii, and it has not received an independent mathematical audit.

## References
- Alejandro Cholaquidis, *Conic reach and polynomial parallel volume in the plane*, arXiv:2607.24487 (2026), §§4,6,8, Appendix B. https://arxiv.org/abs/2607.24487
- A. Cholaquidis, A. Cuevas and L. Moreno, *On the notion of polynomial reach: a statistical application*, arXiv:2307.00373 (2023), §5. https://arxiv.org/abs/2307.00373

Self-review: passed. Independent audit: not yet performed.
