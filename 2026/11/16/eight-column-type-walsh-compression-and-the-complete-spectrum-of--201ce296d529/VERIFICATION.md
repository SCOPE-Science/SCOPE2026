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
# Reproducibility and checks

Execute `python3 verify_eulerian_k46.py` beside `data/eulerian_k46_orbits.csv` using Python 3.9 or later. The program reconstructs all 1716 eight-type orbits, every integer coefficient and its frequency multiplicity; it checks that their frequencies total \(2^{24}\), their squared coefficients satisfy Parseval with exactly 1860 supports, their zero count is \(2^{23}\), and their minimum nonzero magnitude is 4. It independently enumerates all 1860 balanced matrices by row masks and evaluates direct character sums at 256 deterministic frequencies. The expected success marker is `EULERIAN_K46_WALSH_ORBIT_PASS orbits=1716 frequencies=16777216 direct=256`.

The proof that these 1716 cases exhaust all \(2^{24}\) frequencies is the column-gauge and column-permutation bijection in `RESULT.md`, followed by the explicit integer dynamic-programming invariant. The 256 direct sums cross-check the implementation but are not the basis for exhaustiveness. The certificate uses no floating point, downloaded data, or external packages. The number of independent mathematical audits is zero; unseen historical work may overlap.
