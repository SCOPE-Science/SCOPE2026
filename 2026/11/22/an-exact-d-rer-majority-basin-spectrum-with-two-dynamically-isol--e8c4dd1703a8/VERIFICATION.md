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

# Reproduction and scope

The Python and C++17 programs in `verification/` each exhaustively classify all \(4096\) labelled binary states on the Dürer graph under synchronous open-neighbor majority. One constructs \(GP(6,2)\) directly and uses indegree peeling; the other uses the published twelve-entry LCF encoding and first-repetition path tracing. The C++17 check also verifies the explicit isomorphism to the generalized Petersen representation. Both complete basin spectra and all first-periodic-entry times agree exactly. The Python check verifies the full dihedral automorphism group and two Burnside incidences. See `verification/replay.txt` for the actual successful transcript.

Execute from the folder containing `RESULT.md`:

```sh
python3 verification/majority_gp.py
g++ -std=c++17 -O2 -Wall -Wextra verification/majority_lcf.cpp -o majority_check
./majority_check
```

The symbolic nonfinite-extension statement, that the two polarized fixed configurations have singleton basins on every simple cubic \(GP(n,k)\) in the stated range, follows from the explicit inequalities in `RESULT.md`, not from enumerating additional circumferences. Finite exhaustive experiments alone would not prove that general lemma. External independent validation has not been carried out.
