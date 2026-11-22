# Independent mathematical audit

## correctness

PASS

Reconstructed original Akima rule with g_i=|d_{i+1}-d_i| and local derivative a_i=(g_i d_{i-1}+g_{i-2} d_i)/(g_i+g_{i-2}) except zero-weight midpoint fallback. Only critical knots g_{i-2}=g_i=0 and d_{i-1}!=d_i permit nonunique limits; elsewhere slopes converge uniquely. At finitely many critical knots the ratio constraints involve pairs of zero gap indices (i-2,i), whose graph is a disjoint union of finite paths, so arbitrary endpoint/interior ratios can be achieved simultaneously by recursively chosen positive gaps vanishing at suitable rates. Integrate perturbed secants to data, then Hermite interpolation maps independent critical slopes to nonoverlapping two-cell basis bumps psi_i. Each bump has sharp sup 4/27 and TV 16/27, and critical indices differ by at least two; hence exact independent product box, sup diameter (4/27) max|Delta_i|, TV diameter (16/27) sum|Delta_i|, and iff continuity criterion in C1_loc. Inspected actual RESULT.md blob c44b4cc9f1e3c7d51cf9f2bf1ec6fc8b58de0ae4 and exact rational checker verify_akima_clusters.py blob dd7b3264e86ac0cc688598eb499ab3b264b1f832. Independently verified two neighboring critical ratio choices t=1/3,u=2/5 and exact 4/27,16/27 Hermite constants; infinite simultaneous statement rests on the acyclic gap-graph construction.

## originality

PASS

Best-of-knowledge PASS for complete simultaneous all-knot cluster set and both exact global norm diameters. Original Akima (1970) and Moler–Ionita (2019) already explicitly show the zero-denominator convention and qualitative one-corner discontinuity; candidate does not take credit for that. The published 2/27 monotone range defect concerns deviation of one interpolated curve from one data range, not the set of all perturbation limits nor total variation between cluster curves. Highly relevant original 1969 and 1970 full reports unavailable; retain an unindexed historical equivalent risk without automatic failure.

## value

PASS

This is a natural numerical-analysis stability/continuity classification of the canonical Akima interpolant at all finite collections of degenerate slope weights. The path-graph compatibility lemma turns potentially coupled neighboring weight ratios into independently selectable critical derivatives. The sharp simultaneous sup/TV diameters quantify method sensitivity beyond the known one-corner anecdote; this is a meaningful finite-dimensional structural result relevant to shape interpolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
