---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

PASS applies to the replacement RESULT.md, not to the original positive-octant assertion. In the original coordinates, a=b=1 and (x,y,z)=(1,1,2) give a strictly positive H=1 point other than E_+ that maps to E_-=(1,−1,0) in one step rather than oscillating. The repaired text explicitly lists (1/b,1/√(ab),1+1/b), always positive, and E_+ only when b>1. This is exactly the intersection of the eight sign choices with the original positive octant. Rechecking the whole theorem: 1−z_{n+1}=x_n gives y_{n+3}=ab y_{n+2}y_n²; zero data force eventual zero, and other data give L_{n+3}=L_{n+2}+2L_n. The left projection w·U_0=log H and w·v=3r²−2r yield the leading r-mode, exact H power law, and strict-region limits because 1<s<r. Varying |x| locally on H=1 proves the common boundary. In the nonzero complementary mode the expanding rotation produces infinitely many strictly positive and strictly negative sinusoidal excursions, for both rational and irrational angles; its full log-vector norm diverges, precluding recurrence. Vanishing initial log vector gives exactly the eight sign cases and arrival at an E_± within two steps. Poincaré recurrence on a countable basis gives the three-Dirac probability census, and the normalized monomial log chart gives the three repelling eigenvalues at E_±. The derivative at E_0 is nilpotent.

## originality

PASS

For the replacement, the correction restricts the positive-octant statement to its exact content without removing the mathematical gain: the full-real separatrix, classification of nonexceptional and eventually fixed critical orbits, two spectral scales, and invariant probability census. Wang et al. supply the map and local analysis; the same-map Resultary theorem supplies a complete primitive-two-cycle count and therefore already excludes primitive two-cycles on this slice. Neither inspected statement contains the global result. The adjacent water-filling separatrix is for another operator. The elementary monomial logarithm and spectral tools are not themselves novel.

## value

PASS

The choice c=1 exactly cancels a delayed additive term and is a structurally motivated solvable slice of an existing polynomial map. The sharp common boundary and rank-two oscillatory critical dynamics distinguish true basin thresholds from a local stability or short-cycle census. The expanding full log norm despite a middle coordinate with vanishing subsequences is a meaningful mechanism for the complete invariant probability statement. The positive-octant repair removes an incorrect extra assertion without diminishing these conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
