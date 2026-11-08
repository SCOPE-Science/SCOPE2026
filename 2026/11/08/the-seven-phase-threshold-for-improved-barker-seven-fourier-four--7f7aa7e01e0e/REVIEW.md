# Scientific review

## Correctness
**PASS.** The Parseval identity reduces the torus fourth moment to aperiodic base energy. Common and linear phase modulations reduce each finite phase alphabet uniquely to the 29007 normalized arrays counted across the six alphabets. Each profile has exactly 91 ordered contributions and exact dihedral symmetry in the residue index; the rational enclosure argument separates every nonwinning profile from the exact winner, so the computation is finite *and exhaustive*. Independent derivation of the sixth-root and seven-root representative autocorrelation profiles confirms the values. The checker replays from the complete supplied Python source; its rational bounds on \(\pi\) and cosines are proved by alternating and Taylor remainders. No infinite-domain claim is inferred from finite sampling.

## Originality
**PASS, provisional.** Syms–Noorwali (2022) study small phase alphabets 2, 3, 4, 6 but optimize peak sidelobes and code pairs, not the single-sequence integrated energy through alphabet 7. Raei et al. (arXiv 2104.03303v1) study integrated sidelobe optimization under finite alphabets by iterative methods, without these exact length-seven values, counts, or the sharp first-alphabet transition. Borwein–Ferguson (2005) give *numerical continuous-phase* energies and not exact \(q\)-restricted optima. Closest published five- and six-tap results are shorter-domain statements, and the nine-frequency square result concerns a different two-dimensional aperture. Nothing inspected directly yields the present seven-tap classification or algebraic minimum. There remains a plausible historical-priority risk in specialized short PSK code catalogs.

## Mathematical value
**PASS.** Seven taps are the classical Barker-seven regime. The result proves that the popular alphabets 2–6 cannot beat the binary integrated-sidelobe baseline, while the first additional integer resolution that can do so, seven phases, achieves a concrete strict improvement with complete phase rigidity. The exact threshold, optimal energies, and multiplicities are motivated finite-waveform invariants useful as checkable performance benchmarks; novelty is not based on repeating a known table. No general asymptotic theorem is claimed or required.

## Limits and closest literature
The 2022 short-code application treats peak and multiuser correlations rather than exact single-array integrated sidelobe minima. Prior continuous-phase energies are not lower bounds for phase-restricted classes and cannot certify the seven-phase minimizer. Numerical optimization of larger waveforms does not supply an exhaustive length-seven certificate. The conclusion is confined to the six specified finite alphabets; unknown historical exact tables remain the main originality risk.

Self-review: passed. Independent audit: not yet performed.
