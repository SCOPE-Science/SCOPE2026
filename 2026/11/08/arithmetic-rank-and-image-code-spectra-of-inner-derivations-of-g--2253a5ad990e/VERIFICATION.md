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
Run `python verify_binary.py`, `python verify_fields.py`, and `python verify_images.py` from a folder containing all three files. They perform independent exact field arithmetic, direct group multiplication, rank elimination, and canonical image-subspace enumeration. The binary verifier exhaustively tests all group-algebra elements for cyclic kernels of orders three, five and seven and for the elementary abelian kernel of order nine. The mixed-field verifier exhaustively tests the six-dimensional \(C_3\rtimes C_2\) group algebra over fields of orders four and five and samples the order-ten group algebra over the field of order four. The image verifier counts and de-duplicates row spaces directly. The expected success markers are `VERIFY_OK`, `VERIFY_FIELDS_OK`, and `VERIFY_IMAGES_OK`.

The machine verifiers establish exact finite cases only. The universal argument rests on the finite étale decomposition, matrix centralizers, and trace pairing, independently of enumeration. A separate external mathematical audit has not been performed.
