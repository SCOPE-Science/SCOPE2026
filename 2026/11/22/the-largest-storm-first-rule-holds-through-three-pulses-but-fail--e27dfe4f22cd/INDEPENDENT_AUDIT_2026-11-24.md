# Independent mathematical audit

## correctness

PASS

For one to three pulses, telescoping the clipped update gives R = sum(h) - (1-q) sum(s before the last pulse) - s_final. For the first-two exchange starting empty, the larger-first order lowers post-second storage by at most (1-q) times the increase in post-first storage; this gives no greater runoff by balance and no worse identical suffix by monotonicity. For the endpoint exchange z,y,x versus x,y,z, the required difference in retained/lost mass is (1-q)(c-a+B-A)+V-U in the notation of RESULT.md. I checked the unsaturated-middle Lipschitz bound, both branches with saturated middle and z≤C, and the saturated-first branches with z>C; in the last branch the bound is (1-q)(C-x)-((1-q)C-x)_+≥0. The non-strict inequalities cover ties and exact saturation. Moving a maximum from second or third to first therefore preserves optimality. In an independent exhaustive replay, storing in units of 1/64 and computing runoff from conservation, all 24 orders were evaluated: the unique minimum was (12,11,1,13) with 8/64, and the six 13-first spill numerators were 65,17,16,112,80,112, agreeing with the frozen table. The result concerns positive pulse counts and the specified deterministic finite-horizon model only; the rational grid in the supplied verifier is not a proof of the universal result.

## originality

PASS

The strongest statement-level matches treat the periodic steady state, fixed pulse order with variable timing, heterogeneous retentions, or different storage objectives. None establishes the combination of an empty-start largest-first existence theorem and its sharp four-pulse failure. This is a bounded judgment, not a historical-priority certification.

## value

PASS

The theorem gives the exact first horizon where the natural greedy starting choice ceases to be guaranteed, uniformly in depths, capacity and retention below that horizon. The initial exchange works with any common suffix, but the second exchange only justifies the three-pulse horizon. The four-pulse strict, unique optimum rules out tie artifacts and is useful for testing optimization methods for this specific clipped recurrence, without implying empirical hydrological significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
