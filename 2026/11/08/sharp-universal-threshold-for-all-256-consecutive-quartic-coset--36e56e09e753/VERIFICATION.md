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

# Computational verification and limits

The full exact finite calculation was replayed from the bundled `verify_quartic4.cpp` path using a C++17 compiler. The output matched `quartic4_output.txt` byte-for-byte. The code sieves all primes below 263681, filters \(p\equiv1\pmod4\), tests a primitive root using the prime factors of \(p-1\), and evaluates every consecutive four-letter coset word. It checks 11538 eligible primes and finds 144 exceptions, the last 3361. At 3361 the only missing code is 195, corresponding to \((3,0,0,3)\) with the least primitive root. At the next eligible prime 3373 all 256 words occur.

The separate `check_quartic4_independent.py` verifier was also replayed from this package and reported all 269 eligible primes through 4000, 144 exceptions, and last exceptional prime 3361. It determines cosets by constructing fourth-power sets and multiplying by powers of the least quadratic nonresidue; it does not share the primitive-root procedure. It also checks several larger selected primes. The second calculation does not independently cover every prime below 263681; the first computation does.

The infinite tail uses the explicit standard character-sum estimate derived in `RESULT.md`: \(256N_p\ge p-513\sqrt p-256\), positive from 263681. Thus the finite computation is used only for a proved exhaustive range; no inference from experiments to an infinite statement is made. The exact cutoff and source comparisons have not received a separate external audit.
