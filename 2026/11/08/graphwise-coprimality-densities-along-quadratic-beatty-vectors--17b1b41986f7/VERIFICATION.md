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

# Reproducible checks and limitations

Run `python3 verify.py` in the directory containing this file and the standalone verifier. This uses the Python standard library and exact integer square roots for every Beatty coordinate, and it evaluates graph constraints using integer greatest common divisors.

The three checks at \(X=100000\) yield counts \(42810\), \(28608\), and \(11494\) for a three-vertex path, a three-vertex complete graph, and a four-vertex complete graph, respectively. The corresponding prime-truncated Euler products (primes below \(10000\)) are approximately \(0.428257912679\), \(0.286755872147\), and \(0.114890809814\). The verifier asserts that each empirical density differs from its prime truncation by less than \(0.003\); this is a sanity check, not an error bound for the infinite theorem.

The full-domain proof is mathematical. Its crucial estimates are the quadratic-irrational spacing bound for \(\|h\sqrt{u/v}\|\), the fact that any common prime divisor of two specified Beatty coordinates is \(O(\sqrt X)\), and the sum \(\sum_{B<p\ll\sqrt X}(X/p^2+1)=O(X/B+\sqrt X)\). The ratio of distinct prime square roots is quadratic irrational. No finite computation certifies the density limit, historical novelty, or an independent review.
