# Independent mathematical audit

## correctness

PASS

Reconstructed b-adic 1-position formula from binary j: p_j has base-b digits 0 or b-1 and g_j=(b-2)b^{v2(j)}. The central gap j=2^{k-1} is uniquely maximal. Zero-only factors and one-marker factors are transferred to the two central attractor positions; for a one-marker factor, at least one adjacent padding length <=b-2 because neighboring gap indices are consecutive, including endpoints. For multi-marker factors internal gap indices [a,c] have a unique maximal v2 gap j0 of order r; otherwise a higher-valuation multiple lies between two maxima. Their distances to j0 are <=2^r-1, permitting identical internal gap patterns at canonical j_R=J+2^r or j_L=J-2^r. If right endpoint padding fails at j_R it must be the u=2^r-1 case with original succeeding gap order at least r+2, forcing the original preceding gap order exactly r+1; the left canonical placement dominates both exterior paddings and ends at A. For r>=1 the right placement contains selected p_{j_R-1}=Z+b^r-1; for r=0 it contains p_{j_R}=Z+b-1; central-gap factors hit A or Z-1. k=2 two-marker boundary needs separate direct treatment, and k=1 uses {0,b-2}. For lower bounds, F_- and F_+ occupy disjoint opposite central-gap ends because 2((b-2)b^{k-2}+1)<= (b-2)b^{k-1} for b>=3,k>=3; each F_r=1 0^((b-2)b^r) 1 uses solely even gap indices of v2=r>=1, so its full occurrence support is disjoint from the other F_r and from the central-edge supports. The k=1 and k=2 two-support cases are immediate. Hence matching upper and lower bounds all b,k. Independent direct string-and-bitmask enumeration passed 19 instances over b=3,4,5,6,9, k<=6 (342642 distinct factor cells), with no uncovered factor or overlapping proposed lower witness supports. An independent arithmetic exterior-padding dominance check of every internal-gap interval for k=3..9 had zero counterexamples. Finite checks are auxiliary, not the proof.

## originality

PASS

The previously known complemented base-three Cantor infinite word in Cassaigne et al., Example 13, has a Theta(log n) attractor profile, but no exact finite-level minimum or all-base construction. Schaeffer–Shallit Theorem 2 gives decidability for bounded prefixes and general automatic-word asymptotic dichotomy; applying it to this family does not determine the stated unbounded sequence or witnesses. Resultary searches returned this same finding and adjacent distinct-word problems, not a predecessor that implies it. The new exact all-base optimization and matching disjoint-factor supports are therefore original to best knowledge, with explicitly recorded residual priority risk.

## value

PASS

Minimum string-attractor size for complete finite generalized Cantor iterations is a natural exact invariant of the classical sparse fractal automatic word family. The uniform b-independent max(2,k) sharpens only qualitative logarithmic profile information for the same ternary fixed point, with canonical optimal hitting sets and k independent lower-bound witnesses. The 2-adic transfer lemma identifies a reusable factor-placement mechanism; this is a nontrivial infinite base-and-depth classification, not a small numerical exercise. No downstream theorem is required for the exact optimal construction to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
