# Independent mathematical audit

## correctness

PASS

Original decision: FAIL as written for the fixed-basis assertion in line 26, not for the exact table. In one fixed basis, replacing α by α⁻¹ reverses the cyclic degree sequence, and the inverse window at (t,r) has exactly the forward histogram at (−t−r+1,r); the bijective start change preserves each range. The reciprocal-polynomial comparison instead uses the two generators' different natural bases. The complete corrected RESULT.md in /workspace/repairs/5/ specifies both facts and proves the reversal identity. Fresh check of the repaired statement: independently tested irreducibility by trial division over GF(2) through degree floor(k/2), tested full multiplicative order by exact residues of powers, and counted full histograms for every start and all 1≤r≤M by direct polynomial long division and recount. The exact score uses the sum of positive deviations, equal to half the L1 total because the deviations sum to zero. The primitive-mask lists, degrees 2–4 peaks 1/3, 6/7, 8/5, and all six degree-five (peak, first r) entries (70/31,15), (68/31,14), (80/31,9), (86/31,15), (86/31,15), (80/31,9) agree. All degree-five maximizing sets are the stated smallest lengths plus their complements. At 0x25,r=15 and 0x29,r=14, the extrema in the frozen 2M normalization are respectively 30/170 at t=6/29 and 42/178 at t=2/8 (min/max scores, not ratios). The reciprocal identity follows by reversing the six coefficient bits. Every basis gives the required 2^j frequency among all nonzero vectors; the full-period score is zero and complementary windows have opposite deviations. Replay: python3 /workspace/branches/check_5.py and check_5.out beside it. The frozen verifier and VERIFICATION.md were inspected, not executed; their finite computation requires no change. Nothing is inferred about higher degrees.

## originality

PASS

Fresh comparison for the repaired finding. The distinct claim is the first degree with differing exhaustive peaks across primitive polynomials and the full first spectrum in generator-specific natural bases. The statistic itself is credited to Pääkkönen and the phase-reversal proof is an elementary correction, not a separate novelty claim. Available evidence does not establish an equivalent all-polynomial comparison; inaccessible primary text and submitted work remain risks, not proof of absence.

## value

PASS

The first failure of degree alone to determine the exhaustive envelope matters directly for interpreting one-polynomial-per-degree experiments. The full first spectrum, including a split already in a reciprocal pair's natural bases, gives a small exact benchmark for feedback and coordinate dependence, not a claim of asymptotic feedback sensitivity. The correction preserves that benchmark and distinguishes it from the elementary invariance under time reversal with coordinates held fixed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
