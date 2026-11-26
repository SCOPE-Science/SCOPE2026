# Independent mathematical audit

## correctness

PASS

For each unit undirected cycle, L is symmetric positive semidefinite with L1=0. The denominator polynomial of R has positive values on the nonnegative spectrum, so the exact step is a symmetric circulant matrix with row sums one. Rotation and reflection reduce the seven positive orders C3–C9 to 26 distance entries. The independent rational computation reconstructed the Laplacians and Q⁻¹B without running the supplied verifier: it checked all 26 cycle entries and also all 34 path entries of the original. Across those 60 entries there were 390 numerator and 390 denominator coefficients, all nonnegative, with every numerator nonzero and the minimum denominator coefficient 2. Each repaired claim of strict positivity follows for all h>0, not merely checked steps; h=0 is the identity. At distance five, powers below five have zero entry and (L⁵)ᵤᵥ is minus the number of shortest walks, so the Taylor coefficient 1/108 of x⁵ gives a strictly negative leading coefficient. This is independent of any finite cycle enumeration and covers every n≥10; the boundary check on C10 gives (L⁵)₀,₅=−2. Replay: /workspace/branches/83b8351e-6190-4d31-82dd-3f81bf65d746/exact_replay.py and exact_replay.json. The original mathematical claims checked; the repair is a scope and attribution change, with cycle-only RESULT.md and matching scientific verification notes.

## originality

PASS

The original bundle does not pass as a distinct contribution: both the unit-path cutoff and the distance-five lemma are prior, the latter already in a stronger positive-conductance form. The repaired result credits these and claims only the all-step cycle classification as a contribution. Its negative half and small/large-step positivity statements are also prior; the surviving advance is closing the intermediate-step gap for the entire positive side of the cycle classification. This is not a finding of global priority.

## value

PASS

The repair settles a natural, motivated gap left by the known small-step cycle barrier. Finite cycle heat flows are standard periodic diffusion tests; unconditional entrywise positivity of a classical high-order step is strictly stronger than positivity in both asymptotic regimes. The exact signs prove that none of the possible short rings has an intermediate failure, so the already-known necessary boundary is also sufficient in this whole graph family. This value does not depend on the removed path claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
