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

# Reproduction and verification

Run `python3 verify_matrix.py` and `python3 verify_bitsets.py` with a standard Python 3 installation. Both scripts reconstruct all twenty-eight-vertex graphs from first principles and use no external datasets. The first exhaustively checks \(193264\) support/family pairs across all support sizes through four, confirms the strongly regular parameters, and tests maximality of every shattered triple. The second separately constructs bitset adjacency and enumerates all traces, obtaining identical polynomials and maximal-triple counts. Both actual outputs appear in `verification_output.txt`.

A class of only twenty-eight center concepts cannot shatter five queries because five queries require thirty-two distinct trace realizations. Thus all higher coefficients vanish independently of the finite enumeration. The ordinary source code and output permit replay, but program agreement is not an independent external mathematical audit.
