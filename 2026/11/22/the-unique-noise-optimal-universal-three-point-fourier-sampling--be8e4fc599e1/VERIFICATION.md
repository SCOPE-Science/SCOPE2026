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

Re-audited RESULT.md and SLOGAN.txt in repairs/4: the mathematically valid extremum is over supportwise restricted Fourier matrices. The frozen slogan's claim of recovery of every signal with unknown support from only three measurements is false if read as blind recovery. Indeed, any two different supports of a universal design have invertible maps onto the same C^3, and for generic measurements both inverse coefficient vectors have no zero entries. The replacements distinguish amplitude inversion on a supplied support from choosing the sample rows without knowing the support, and give the sharp worst noise amplification gamma(R)^(-1/2) for the former. The mathematics is unchanged: residue collisions yield a singular witness at columns {0,5,10}, and distinct residues give full spark by the prime-power theorem. Counting distinct residues gives binom(5,3)*5^3=1250. Row affine maps multiply columns by phases and transport frequency indices by the inverse multiplier when passing from the canonical row representative to an image; column translations multiply rows by phases. The independently regenerated six affine row orbits have sizes 250,500,500,500,500,50. A three-set has no nontrivial translation stabilizer in Z_25, so the column problem has 92 translation classes. A fresh exact replay (python3 /workspace/branches/f767855a-6ddc-4d34-837a-09cf1e2ca787/order25_exact_recheck.py; output order25_exact.log in the same directory) checks every class for each universal representative. Machin's formula and bounded Taylor tails give the root approximants error <10^(-9), so the Gram error has row sums and operator norm <6*10^(-9). The exact integer leading minors at shifts t+10^(-6) are positive for all 91 nonconsecutive classes per representative, for t=1/1000,1/250,1/100 respectively; at t-10^(-6) the consecutive determinant is negative. Sylvester and Weyl transfer the strict separation. The same tests at the band endpoints adjusted by the guard certify (0.00044,0.00050), (0.0017,0.0018), (0.0039,0.0040). Thus exactly 25 worst supports per representative and exactly the 500 row images of {0,1,4} maximize the stated unnormalized squared-singular-value objective. The replay is finite and exact, with a separate implementation of the enclosure method; the uploaded scripts and numerical output were inspected, not executed.

## originality

PASS

The repaired claim retains a distinct order-25 minimax spectral classification and equality sets, not a new claim of full spark, and not a blind sparse recovery result. The cited qualitative theorems and exact rank records already cover the universal-design criterion and hence the 1250 count. None of the inspected stronger-rank results, consecutive-design conditioning bounds, or fixed-mode determinant optimization supplies the comparison of the three positive minima and their complete extremizers.

## value

PASS

The exact optimum solves a meaningful finite design comparison among three inequivalent invertible layouts. If the support is supplied for inversion but is not available at the design stage, the sharp Euclidean noise gain is governed by gamma, so choosing the optimal orbit rather than the consecutive one improves the worst gain by nearly a factor of three. The complete list of worst supports and strict separation are useful beyond knowing invertibility. This value does not depend on the false blind-recovery reading excluded by the corrected files.

The dated certificate retains the supplied scientific assessment, sources and limitations.
