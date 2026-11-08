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
# Reproducibility of finite-field tests

The Python standard-library scripts `verify_commutator.py`, `verify_width.py`, and `verify_gf4.py` are self-contained. Execute them from a directory containing the six text artifacts and compare their exact stdout to `check_output.txt`, `width_output.txt`, and `gf4_output.txt`, respectively. The first script reconstructs multiplication and tests every commutator fiber in seven small examples, with loops excluded and parallel arrows allowed. The second verifies every support subset for binary complete graphs on 3, 4, and 5 vertices by independent color/decomposition construction and checks larger thresholds. The third directly enumerates all 1,048,576 ordered algebra-element pairs for a three-vertex path over the extension field \(\mathbb F_4\). No external packages, network access, or privileged files are needed.

The exact successful markers are `COMMUTATOR_SUPPORT_AND_FK_DIRECT_PASS`, `CHROMATIC_COMMUTATOR_WIDTH_PASS`, and `GF4_DIRECT_FIBERS_PASS`. These checks are finite corroboration only. The field-uniform statements are proved algebraically in `RESULT.md`. No independent mathematical audit or historical-priority certification has been undertaken.
