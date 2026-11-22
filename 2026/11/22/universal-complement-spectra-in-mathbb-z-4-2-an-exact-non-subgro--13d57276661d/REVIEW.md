# Scientific review: universal complement spectra in \(\mathbb Z_4^2\)

## Correctness — PASS
The complete classification is tested twice with exact integer operations. `verify_all.py` exhausts all \(6{,}907\) normalized potential tiles, enumerates every normalized tiling complement by disjoint-cover recursion, forms intersections of Gaussian-integer Fourier-zero masks, finds a common character clique, and tests each eligible subgroup. Its output proves \(715\) normalized tiles with \(460\) lacking subgroup spectra. `verify_orbits.py` independently enumerates all possible complements by direct subset selection for \(19\) representative tiles and verifies their witness bases, all subgroup candidates, and full affine-orbit coverage. Translating sets scales counts by \(16/|A|\), giving \(2{,}155\) and \(1{,}168\). All witnesses and logs are embedded; no approximate character sum or unchecked extrapolation is used.

## Originality — PASS, bounded comparison
The older \(\mathbb Z_4^2\) Fuglede census establishes that \(2{,}155\) sets tile and are individually spectral, in \(19\) affine classes. The new statement quantifies a common basis across **all** complements for each tile and shows that \(1{,}168\) cases have no common spectrum that is a subgroup coset. Lagarias–Wang's general equivalence of a proposed spectrum and common complement zero conditions is a criterion, not these values; their existence results are explicitly cyclic. Farkas–Matolcsi–Móra establish an equivalence across every group of a fixed generating dimension, not an implication confined to the same group. Zhou's studied specific rank-two subgroup complements do not account for the full \(19\) classes. The exact statement, rather than just its title, was compared against the nearby published finite census and primary manuscripts. Residual risk is an unindexed equivalent computation or an implicit stronger classification not identified in the material inspected.

## Value — PASS
Universal spectra ask for one stable collection of frequencies that works over every possible complement, a stronger natural sampling demand than a separate exponential basis for each complement. The finding identifies a substantial and exhaustive obstruction to using subgroup/annihilator-only designs even when universal bases do exist: \(1{,}168\) of \(2{,}155\) tiles force a non-subgroup choice. The finite result is a reproducible boundary example in a rank-two exponent-four group and explains which of its \(19\) affine geometries require non-subgroup frequency sets. No general theorem over all prime-power groups is asserted.

## Scope and risks
The classification is confined to \(\mathbb Z_4^2\). The original occurrence of a published equivalent classification cannot be excluded entirely. The integer certificate is self-contained and reviewed, but an independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
