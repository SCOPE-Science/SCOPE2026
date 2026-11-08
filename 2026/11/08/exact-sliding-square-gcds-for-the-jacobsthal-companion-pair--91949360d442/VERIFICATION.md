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

The proof in `RESULT.md` is an all-length argument, using an integral third-order recurrence for window sums and separately proving valuations at the primes 2, 3, and all primes at least 5. The determinant of the three-window evaluation matrix is \(432\), a unit away from the primes 2 and 3. Prime 2 is handled using square residues modulo 8 and 16; prime 3 is handled via the binomial expansion of \((-8)^{k/3}\).

`verify.py` is a self-contained independent finite calculation based on the recurrences, not the closed form for each individual window. It checks 700 lengths, 12 successive starting indices and both companion sequences, making 1,400 formula comparisons. Invoke it with `python3 verify.py`; `verification_output.txt` is its captured output. Exact-integer finite tests cannot establish the universal theorem; this file does not claim an independent audit.
