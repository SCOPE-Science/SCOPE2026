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

# Computational checks and limits

Execute `python3 verify.py` and `python3 mass_identity.py` in a directory containing both standalone programs. No nonstandard packages, external files, internet access, or random seeds are needed.

The direct checker enumerates functionals modulo the three irrelevant idempotent-dual coordinates and uses actual multiplication of basis paths to form the commutator equations. It computes stabilizers by linear algebra over the field, including a genuinely nonprime field of order four. For the three smallest tests it additionally enumerates candidate units directly, comparing the resulting stabilizer count to the linear solution count. Expected multiplicities are computed separately from Gaussian-binomial rank counts, and all obtained multiplicities and orbit sizes are compared.

The mass checker examines 288 independent choices of field order and two arrow multiplicities; it verifies integrality and both moment identities. `verification_output.txt` and `mass_output.txt` record the resulting output from the versions of the programs included alongside this document.

All finite tests terminate with `ALL_PATH_COADJOINT_FIBERS_PASS` and `ALL_PATH_ORBIT_MASS_IDENTITIES_PASS`, respectively. Finite verification does not prove an assertion for all finite fields and all arrow multiplicities; the algebraic proof supplies those quantifiers. No independent audit has been performed.
