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

Run `python3 verify_triples.py` with Python 3 standard library, without external dependencies. It reconstructs the 17 reachable root-intersection states and the full integer transfer from the eight three-bit vertex colors, and checks exactly each coordinate of

\[
\mathbf 1(T^4-8T^3+16T^2-12T+2I)=0.
\]

It verifies the four initial terms needed for the generating functions, the numerator of the type-\(D\) series, and the difference numerator with type \(A\). Independently, it brute-enumerates three-subset support triples using graph connected components rather than transfer states for path ranks 2–6 and type-\(D\) ranks 4–6; it also enumerates and compares commuting-pair counts. A successful run prints `HECKE_TYPE_D_TRIPLE_CERTIFICATE_OK` and the exact sample counts.

The infinite proof uses the component characterization, the rooted-state transition rule and the exact matrix identity. The finite brute-force counts do **not** extrapolate the sequence by themselves. This is a reproducible self-review, not independent mathematical certification or a historical-priority guarantee.
