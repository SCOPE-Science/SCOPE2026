---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification

The included `verify.py` computes true integer binomial coefficients and counts every ordered output residue over one full claimed least period for nine prime/exponent choices, without using the theorem to generate the observed histogram. For each tested input it checks the independently calculated digit-level congruences, then every predicted fiber, both uniform marginals, and total period mass. It prints the harmonic residues and the output-support size. The last line upon success is `ALL EXACT CHECKS PASSED`.

Checked cases: \((2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2),(7,1),(11,1)\). The periods cover 16 through 14641 indices, all exactly evaluated. These computations corroborate but cannot prove the universal statements; the infinite proof is given in `RESULT.md` Steps 1–5.

The critical p-adic denominator valuation, order of multiplication, sharp period witness, endpoint \(n=0\), and prime-two case were checked directly in the proof. Higher moduli, nonadjacent columns, and a closed formula for harmonic image sizes are not established here. No independent external audit is claimed.
