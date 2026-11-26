---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Checked the fixed three-descent convention and the classical inclusion–exclusion formula. The terms involving 2^n or 4^n vanish at the stated threshold. For n=2t the divided cubic difference (1−4(t²+ts+s²))/3 is odd; the divided exponential difference is even since v₂(9^h−1)=3+v₂(h). This proves the exact even-index isometry. For n=2t+1, subtracting V(t+4h)−V(t) and dividing by −8h gives the first term in 8ℤ₂ by v₂((9^4)^h−1)=5+v₂(h), and the other two terms are 3 and 3 mod 4 (t(t+1) is even). The normalized odd-index divided difference therefore has v₂=1, proving the isometries after division by 16, with centers 10,0,10,0 mod 16. Continuity extends these congruences to ℤ₂. A full block has 2^k samples of each parity; at k≥4 each of four odd charts contributes four counts per residue in its ball, and the even branch contributes one to each residue. Projection from a modulus-16 period gives k≤3 after dividing by the number of smaller periods. The asserted shifts preserve both charts (for k=1 use V even; for k≥2 the shift in t is divisible by 4), and odd shifts are impossible since infinitely many even indices give odd residues. An even shift 2d requires 2^k dividing d by the isometry, which proves minimality. Densities follow by division by the period, giving the stated compatible Haar density.

## originality

FAIL

The distinct Resultary record First nonuniform dyadic residue law in the three-descent Eulerian column proves the identical k≥4 histogram from the identical onset, the least period and its densities. Its actual proof also gives the even-index isometry and four odd-index charts with the same two centers, from which the low-level formulas, sufficiency from n≥4, and Haar density follow mechanically. Thus the exact frozen Finding is covered in substance. The two records have the same date; this is not a claim about priority, dependence, or copying.

## value

FAIL

The nonuniform law is a mathematically motivated contrast with the uniform two-descent column. But the separate indexed first-nonuniform-law record establishes that same contrast, exact high-level fibers, minimal period and their chart mechanism. The low moduli and the Haar-density formulation in the frozen Finding are direct consequences of the same distribution and valuation formulas, not distinct useful unknown invariants. The submitted result adds no sharp onset or other substantive further boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
