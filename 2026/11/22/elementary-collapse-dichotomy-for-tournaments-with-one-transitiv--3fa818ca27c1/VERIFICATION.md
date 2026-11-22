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

`verify.py` was executed against the standalone code delivered with this package. It directly enumerates all faces of each directed flag complex with one distinguished transitive-deletion vertex, checks each claimed elementary collapse at the moment performed (including uniqueness of the coface), and matches the terminal simplicial complex with the theorem. Every possible orientation and every distinguished hub was checked for sizes three to nine: 4,092 total tests, 196 circle cases. It also tests a five-vertex strongly connected contractible example. The exact execution output is in `verification_output.txt`.

The finite exhaustive test does not prove the unrestricted theorem; the nested-neighborhood elementary-fold argument and its cone lift prove it for every number of vertices. No external validation or independent audit is claimed.
