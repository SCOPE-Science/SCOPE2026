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
# Reproducibility

Run `python3 verify_moore.py` using Python 3 and only its standard library. The checked finite instances are \((q,N)=(2,3),(3,3),(2,4)\) (the \(N=3\) examples are boundary checks, not part of the new theorem's \(N\ge4\) claim). The program constructs polynomial determinants and derivatives independently, checks Moore factorization, all gradient/minor identities, and the expected degree. It additionally exhausts the \(585\) projective points over \(\mathbb F_8\) for \(N=4,q=2\), including a direct rank-two transverse-regularity witness. Its expected output is provided verbatim in `verification_output.txt`.

These computations do not establish the infinite family. The proof in `RESULT.md` is symbolic and uses the Moore rank criterion, the height-two Hilbert--Burch theorem, generic reducedness plus Serre's criterion, and the flatness of Frobenius on regular rings. No external proof assistant or independent audit is claimed.
