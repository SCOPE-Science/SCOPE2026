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
# Verification record

The Python standard-library source `verify.py` independently reconstructs the vertex-induced connected components of each candidate face, every graph automorphism and the sign of its orientation action on fixed simplices. It independently reduces all augmented simplicial boundary matrices over the two-element field, confirming 72 homology-rank profiles. For all nine graphs with \(1\le a,b\le3\) and each \(1\le r\le a+b+4\), it compares the resulting reduced Lefschetz number to the two-module character formula. The recorded output in `verification_output.txt` ends in `ALL_VERIFY_OK` with 1,136 checked identities, 1,064 nonidentity cases. Independent sources of information include a direct 0/1 subset traversal and a separate cycle-factor characteristic polynomial calculation, not a reuse of the proof's boundary matrices.

Reproduction: run `python3 verify.py` with only a standard Python 3 installation. The program terminates after exhaustive finite checks. The infinite assertion is established by the natural relative chain and Mayer--Vietoris proof in `RESULT.md`, not by this finite enumeration. No independent mathematical audit has been conducted.
