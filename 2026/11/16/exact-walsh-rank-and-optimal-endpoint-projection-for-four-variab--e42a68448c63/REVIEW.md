# Scientific review: antichain Fourier support and projection constant

## Correctness

The object and normalization are explicit: unnormalized Walsh transform of the 168 incidence vectors of antichains of the sixteen-element Boolean lattice. Two independent exhaustive methods compute all 65,536 Fourier coefficients; the second uses direct character summation without a butterfly algorithm. Their complete 79-level signed histograms agree. The projected-kernel histogram is independently recovered both by a second butterfly transform and by direct summation over the 6,611 exact Fourier zeros. The 48-automorphism symmetry test independently verifies the orbit structure. Parseval identities and exact integer sums are checked. Translation averaging analytically proves sharpness among arbitrary real or complex endpoint projections. No probabilistic or floating-point inference is used.

## Originality

The known Dedekind number 168 is explicitly separated from the evaluated spectrum. Stephen--Yusun (2012) counts functions by equivalence and profiles, and De Causmaecker--De Wannemacker--Yellen (2016) treats antichain interval partitions. Bshouty--Tamon (1995) treats harmonic analysis of *individual* monotone functions on an input Boolean cube; that is a different Fourier transform from this ensemble-indicator transform. The exact nullity, symmetry-orbit distribution, signed multiplier histogram and evaluated projection constant are not implied by these inspected statements. Related indexed results on spectra of six- and eight-point binary sets and on all four-variable Boolean functions concern different objects and do not contain the 168-point ensemble. Searches do not prove priority; residual historical risk remains.

## Value

The sixteen-element Boolean lattice is the smallest order with 168 antichains and a nontrivial 65,536-frequency ensemble Fourier calculation. The exact 6,611-dimensional convolution kernel quantifies which signals cannot be recovered from antichain convolution; its sharp endpoint projection norm gives the optimal amplification when extracting recoverable components. The full two-sided symmetric orbit census reduces the zero-frequency set to 199 orbits and allows systematic comparison of the spectral phenomenon with Dedekind enumeration at other orders. These are natural intrinsic harmonic invariants of a canonical finite combinatorial family, not a selected arbitrary frequency slice. This finding does not claim a general theorem for larger lattices.

## Limitations

All evaluated constants are specific to four input variables. Symmetry orbits are a finite exhaustive certificate, not a structural formula for higher dimensions. The historical literature comparison is bounded, and independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
