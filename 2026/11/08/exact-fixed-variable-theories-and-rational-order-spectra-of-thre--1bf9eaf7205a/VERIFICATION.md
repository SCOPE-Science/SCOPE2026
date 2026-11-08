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

# Reproduction and limits

Run `python3 verify_finite_variable.py` and `python3 verify_spectra.py` with Python 3, using only its standard library. The supplied `verify_finite_variable_output.json` and `verify_spectra_output.json` are the expected exact program outputs. They were regenerated from these bundled scripts and compared byte-for-byte.

The first program constructs **all** unlabelled threshold graphs via binary creation words up to orders seven, six and five at widths two, three and four, respectively. It computes stable tuple colors under coordinate substitution, taking the set of response colors rather than counting their multiplicities, and groups graphs by the resulting sentence types. It independently compares those groups to their truncated extremal-peeling signatures. These are complete checks only within those finite bounds. There are no reported disagreements.

The second program constructs all binary creation words through order twelve and compares the number of distinct capped signatures at each order, plus their unique minimum sizes, against coefficients derived independently from the proposed rational series for widths two through six. All tested coefficients agree. The program is not a symbolic proof of the rational identity, which is derived in `RESULT.md` by canonical block enumeration.

Both programs have no external dependencies, no network operations and no reliance on earlier files. They certify only reproducibility of these finite tests. Arbitrary-size and unlimited-quantifier-depth claims are proved in `RESULT.md`, not by extrapolating the observed finite results. Priority and correctness have not undergone independent mathematical audit.
