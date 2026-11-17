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

# Verification

The mathematical proof is in `RESULT.md`. Run `python3 verify.py` using Python 3 from the directory containing the standalone script. No additional dependencies are required. The output saved in `verification_output.txt` was produced by executing that script.

The verifier independently enumerates Alexander-dual faces fixed by selected nonidentity group elements for thirty permitted pairs of graph parameters, then separately constructs the ordinary cut complex by closing all complement-of-disconnected-triple facets downward. For five small cases it compares every dihedral group element against the stated character using a direct signed face trace. Finally it verifies invariant dimensions by character averaging. The recorded results are 165 dual-orbit character tests, 122 direct cut-complex character tests, and 30 invariant dimension tests, all passed.

These finite checks do not establish the theorem for infinitely many graph powers and lengths. The proof of the orbit-axis lemma and signed Alexander duality supplies the infinite argument. The published shellability theorem is required to conclude that the top homology is the only nonzero reduced rational homology. Integral dihedral module structure and small lengths are outside the scope. Independent external review has not been performed.
