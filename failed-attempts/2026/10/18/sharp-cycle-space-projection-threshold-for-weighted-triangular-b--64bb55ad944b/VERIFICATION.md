---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The m independent circulations e_xi+e_yi−e_c span by cycle rank. Averaging over hub interchange and leaf permutations preserves the projection and does not increase its weighted ℓ1 norm. Fixing each circulation gives spoke coefficients (1+u)/2 and u/2 and the hub image u times the sum of circulations. The weighted column maximum is max{m(2+t)|u|/t, |1+u|+(m−1)|u|+(t/2)|1+mu|}. For u≥0 it is at least 1+t/2. For −u>1/m the hub column alone exceeds 1+2/t≥1+t/2. In 0≤v=−u≤1/m the hub line is increasing from zero and the spoke line has slope m(1−t/2)−2. A nonnegative slope gives the u=0 minimum; a negative slope gives a unique intersection at v=t(t+2)/[m(t²+4)+4t] in the stated interval. This also proves the asserted optimal hub-coordinate behavior. Equality gives the same value from both formulas, and at t=2 the retained coordinate gives 2m/(m+1). The values at t=1 follow directly. Independent full matrix LPs after isometric diagonal scaling reproduced the formula at seven points straddling the threshold, including 1.495, 1.500 and 1.502479229200 for m=4 at t=0.99,1,1.01. Replay: python3 branches/independent_checks.py 3 (NumPy/SciPy).

## originality

FAIL

The exact weighted formula, including the switch, follows mechanically from Blatter and Cheney's classical ℓ1 hyperplane projection theorem. The pairwise spoke averaging is a contraction onto the subspace where the two spoke coordinates on each page agree, and the cycle space lies in that subspace. Restriction and extension by this contraction preserve the projection infimum. In scaled coordinates the cycle space is therefore isometric as a relative projection problem to ker(1,h,…,h) in ordinary ℓ1^{m+1}, with h=t/2. The primary formulas give the two branches by direct substitution, and the hub-column condition follows by testing the coordinate annihilator. A distinct indexed result also exactly covers the unweighted slice as a complete split graph. Neither the same-date weighted metric-distortion result nor no-spine diamond work is asserted to prove this result.

## value

FAIL

The role of the retained spine in a graph complementability problem is natural, but the proposed exact invariant is a two-valued coefficient substitution in the already solved hyperplane problem after a contractive compression. Even the spine-annihilation threshold is exactly the feasibility of the coordinate annihilator at the known optimum. The unweighted observation is also a substitution into the published split-graph formula. No independently useful unresolved quantity remains in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
