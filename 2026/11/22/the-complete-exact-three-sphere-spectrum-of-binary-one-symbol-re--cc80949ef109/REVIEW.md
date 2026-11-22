# Review of the three-duplication sphere spectrum

## Correctness
PASS. The proof distinguishes output sets rather than ordered histories, proves the two-step terminal-membership criterion, and obtains a disjoint-set recurrence for exact-three descendants. All quantifiers cover every positive source length and every binary source. The forward verifier exhausts 2046 sources at lengths one through ten; the structurally different reverse-deletion verifier checks 510 sources through length eight. The induction, rather than those finite tests, proves the infinite result.

## Originality
PASS relative to inspected sources. The closest fixed-error published result determines the exact-two maximum for odd reverse-complement block lengths, and the closest earlier binary spectrum gives \(\binom{n+1}{2}+r\) for **two**, not three, duplications. The new proof resolves overlaps created by a third duplication and yields a full all-length spectrum with \(\binom r2\) curvature. The 2025 source on unbounded-error capacity, the September 2026 manuscript on finite-error coding bounds and two-error spheres, and the February 2026 correcting-code preprint do not state this exact-three spectrum in the inspected material. The 2021 full text was not inspected; an equivalent unindexed derivation remains possible.

## Value
PASS. A fixed-error descendant-sphere law is a natural channel-geometric invariant: its volume enters packing and decoding-complexity assessments. The three-error classification reveals a complete spectrum and exact extremizers, whereas the general odd-block result supplies only the maximum for two errors. It is a meaningful all-length theorem, not an arbitrary short-length census or an unproved extrapolation.

## Scientific limitations
Only fixed-point-free binary complement, one-symbol duplications, exactly three sequential operations. No claimed optimal correction code or multi-letter alphabet extension. No independent audit.

Self-review: passed. Independent audit: not yet performed.
