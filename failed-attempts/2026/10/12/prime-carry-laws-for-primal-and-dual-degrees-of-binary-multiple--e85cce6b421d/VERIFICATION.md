---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The source uses published Hilbert degree D=(d!/Πm_j!)Πj^{m_j}. Taking v_p and applying Legendre v_p(N!)=[N−s_p(N)]/(p−1) immediately yields [Σ s_p(m_j)−s_p(d)]/(p−1)+Σm_j v_p(j), with all summands nonnegative and the iff carry-free/prime-to-p criterion. When m_1=0, Oeding’s explicit dual degree is (d+1)!/Πm_j! times Π(j−1)^{m_j}; it is exactly (d+1) times Hilbert’s formula for λ−, proving the stated bridge. An identical Legendre/Kummer substitution gives the dual local formula and binary support parity criteria. I independently checked several nontrivial partitions including (6,4,3,3,2) and multiple primes against exact integer degrees; package verification enumerates a wider finite set but is not the theorem proof. All assumptions (binary forms over C, dual hypersurface m1=0, d number of distinct roots) are consistent.

## originality

FAIL

FAIL as a standalone original research assertion: the full primary Lee–Sturmfels and Oeding sources already state the exact primal and dual integer degree formulas for every partition. Every displayed prime-carry and prime-avoidance identity is their immediate p-adic valuation with the classical textbook Legendre–Kummer theorem; the shift identity is the unaltered quotient of the two known products after j↦j−1. The alleged new formula is an obvious parameter-free corollary of directly covering stronger closed formulas plus standard arithmetic, not a new invariant theorem whose validity requires an unproved nonstandard comparison. The same method is explicitly used in a Resultary rational-normal-secant record for a different geometric degree; that different paper is NOT misrepresented as directly covering this locus.

## value

FAIL

FAIL the motivated mathematical-value bar for an independent publication claim. The full primal/dual degrees are already known exactly; p-divisibility, parity and carry-freeness are routine postprocessing via standard Legendre/Kummer and binary digit-disjointness. No independent natural new invariant, unexpected exceptional family, new structural classification, sharper unknown cutoff or problem-motivated geometric insight beyond applying a textbook valuation rule is established. The parity statements are direct substitutions, and the shift bridge is immediate cancellation; mathematically correct and reproducible recomputation alone is not sufficient value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
