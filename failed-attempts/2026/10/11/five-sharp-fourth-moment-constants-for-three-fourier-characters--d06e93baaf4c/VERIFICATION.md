---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Frozen RESULT.md 9dcaf63eb0957ffe85412f11ab962f084360f51c and checker.py 23d777a87ea7774b197018f4621a9af8547fb62c inspected. Reconstructed the orthogonality identity ||f||4^4=||f²||2²=sum_s|sum_{chi+psi=s}a_chi a_psi|² and the six unordered pair sums of three distinct characters. Independent Python enumeration for G=Z3,Z4,Z6,Z7,Z8,Z11,Z2²,Z2³,Z2xZ4,Z3² yielded exactly six collision-count patterns (midpoints, equal doubles) (3,0),(1,1),(1,0),(0,1),(0,0),(0,3), with explicit witnesses. Bounding each quadratic fiber by triangle inequality and optimizing squared coefficient masses yields respectively 3,7/3,15/7,2,5/3,7/3. Generic equality all equal magnitudes; single involution equal antipodal pair with third coefficient 0 and aligned squares; ordinary progression masses 2:3:2 with midpoint phase coherence; cyclic-four and Klein-four equal masses plus simultaneous quadratic phase equations; cyclic-three quotient point masses. Pairwise-collision classification is exhaustive by elementary rank/torsion, and the cyclic-three and Klein-four special cases reduce to normalized point-mass and mean-zero Fourier transforms. Finite enumeration corroborates, but algebra proves the arbitrary finite-group statement.

## originality

FAIL

FAIL due to decisive pre-existing joint implication, not a failed search: the already published complete three-character cyclic Lambda(4) theorem proves all five values and every equality case using ONLY pair-sum collision algebra; thus the proof applies verbatim to every non-Klein three-character collision pattern in any finite abelian group. The only genuinely noncyclic collision type is a rank-two 2-torsion triple, a coset of the three nontrivial characters on Z2². The already published general co-singleton-spectrum theorem, applied at N=4 to this Fourier quotient, gives K4^4=4-2+1/3=7/3 AND complete coefficient phases. Consequently these two existing precise theorems and the routine classification of the six pair-sum patterns imply the entirety of the claimed six-regime noncyclic extension; do not mark original by wording/general-group parameter alone.

## value

FAIL

FAIL. Although general finite-abelian three-mode constants are natural, all quantitative values, extremizers and remaining Klein case follow by direct specialization/reuse of the pre-existing cyclic five-case table and the four-point co-singleton theorem. The new package supplies only the routine collision-pattern reduction and repackaging of known sharp statements; it does not isolate an independently motivated new invariant, nontrivial structural lemma, or genuinely unknown boundary classification. Reproducibility and a full proof cannot rescue this covered theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
