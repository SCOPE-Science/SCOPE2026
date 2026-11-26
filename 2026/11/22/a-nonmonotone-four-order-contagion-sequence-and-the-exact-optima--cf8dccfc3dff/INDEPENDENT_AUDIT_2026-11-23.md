# Independent mathematical audit

## correctness

PASS

Independently generated the affine lines as cosets of the one-dimensional direction spaces and exhausted the eight candidate spaces using synchronous frontier neighbor-count waves, not the submitted bitmask routines. At the beginning of a wave the active frontier is already fixed; only after accounting for its edges can newly qualified vertices form the next frontier. This preserves exact completion times, unlike immediate in-wave activation. The zero counts immediately below the claimed minima exclude every smaller set by monotonicity under seed extension. The minima are (4,5,5,4) and their counts are (8,4572,142176,70000). The point-seed vectors at those minima are (3,4,0,0,1), (396,1224,1404,1080,396,72), (8448,32640,46080,36480,15840,2688), and (9000,32000,0,24000,5000). The q=5 round counts at 7 through 11 are (5000,23000,18000,12000,12000), with no other completion times. These are counts of unordered sets of actual vertices. The two supplied programs were inspected, not executed. Independent replay: python3 /tmp/opencode/affine_contagion_independent.py (captured output /tmp/opencode/affine_contagion_independent.out).

## originality

PASS

The finite result concerns two-neighbor vertex closure in a graph with two independently seedable shores and no line or points at infinity. Neither ordinary-graph density results, line percolation, nor the inspected exact projective-plane classification covers the affine minima and census. This is a finding within the inspected record, not a priority certification.

## value

PASS

The four orders are the first consecutive admissible orders, not a selected sample engineered around unrelated graphs. The minimum drops from five to four despite an increase in order; the q=5 exact counts show that this is compatible with four nonempty seed-composition strata but not the balanced stratum, and delimit the exact time spectrum of a canonical small geometric graph. This supplies a benchmark for affine join–meet generation with no access to directions at infinity, without implying a formula for larger fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
