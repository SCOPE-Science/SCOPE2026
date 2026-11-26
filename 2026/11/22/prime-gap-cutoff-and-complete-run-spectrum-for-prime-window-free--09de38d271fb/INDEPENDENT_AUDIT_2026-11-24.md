# Independent mathematical audit

## correctness

PASS

The allowed residues modulo each window prime p are the proper nonempty cyclic arc {k+1,...,p−1,0}. CRT identifies the admissible endpoints with their Cartesian product. A period preserves that product and therefore each projection; a nonzero translation cannot preserve a proper nonempty subset of a prime cycle. For r consecutive endpoints the tested intervals have union of length k+r−1, leaving max(p−k−r+1,0) residues modulo p. Summing the indicator of r ones bracketed by zeros gives its second difference, also for runs crossing the period boundary. The smallest p produces the exact cutoff g_k. For r<g_k, choose distinct window primes and use one to put a multiple immediately before, and the other immediately after, the central tested interval; both periods exceed its length plus one, and each remaining prime has an admissible central residue. CRT realizes both boundaries simultaneously. A single prime gives one cyclic arc. The known R_2=11 applies at x=2k for k≥6 (2k is not prime); k=2,3,4,5 have window primes {3},{5},{5,7},{7} respectively. Thus only 3 and 5 miss a length. The exception list uses R_2=11 in addition to the basic Bertrand nonemptiness input; clarify this if interpreting the final limitation as saying Bertrand alone is invoked. Independent replay: `python3 /workspace/review_calculations/small_cases.py windows` marks forbidden endpoints from multiples and measures the gaps between consecutive zeros over 18 complete periods. It checks all candidate prime-index period reductions and reproduces the k=7 histogram (2,2,2,3) and all exact frequencies against the formula. The replay is finite, not the proof for all k.

## originality

PASS

Credit the one-point density and CRT box to Tang and the generic correlation-to-runs technique to prior work. The supported distinct claim is the least period and complete prime-window maximal-run distribution, particularly its exact support and two exceptions for this indicator. Neither the same-object density and first-hit results nor the inspected distinct residue-run theorems cover it as a stated or mechanically evaluated case.

## value

PASS

The Erdős admissibility condition motivates a natural exact question about local clustering. The gap parameter controls the sharp cutoff, and two primes can independently impose both boundaries, giving a uniform full-support theorem apart from two exact exceptions. These distinguish where and at what lengths eligibility can persist in a cyclic window, information unavailable from the individual endpoint density. No claim about the first hit or distribution in a short interval follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
