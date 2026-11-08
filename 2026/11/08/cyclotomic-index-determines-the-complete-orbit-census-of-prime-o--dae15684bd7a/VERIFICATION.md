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
# Verification of cyclotomic generalized Paley automata

From a directory containing the accompanying standard-library scripts, run `python3 verify_matrix.py`, `python3 verify_moments.py`, and `python3 verify_orbits.py`. Captured exact standard output appears in `verify_matrix.out`, `verify_moments.out`, and `verify_orbits.out` respectively; each script ran successfully from its packaged source and generated exactly its captured output.

`verify_matrix.py` constructs the undirected prime-order adjacency matrix and checks the full nilpotent rank filtration and selected exact iterate fixed-space dimensions in 15 eligible parameter families with primes at most 43. `verify_moments.py` independently checks root-of-unity power sums, first surviving binomial coefficient, and integrality of the period counts in 89 eligible families with odd primes at most 127. `verify_orbits.py` enumerates the entire 823,543-state functional graph for the seven-vertex cycle endpoint over \(\mathbb F_7\), verifying its 1/16/39,214 orbit counts at least periods 1/3/21.

No finite computation is claimed to prove the universally quantified statement. The characteristic-\(p\) subgroup moment identity and nilpotent-shift argument in `RESULT.md` supply the proof for all allowed primes, indices, and finite state fields. Historical priority and independent external validation remain open.
