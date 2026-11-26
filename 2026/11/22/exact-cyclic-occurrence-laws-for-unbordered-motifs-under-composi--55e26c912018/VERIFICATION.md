---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n<m a hit forces a proper border of length m−n; otherwise overlapping hits force a border with the directed overlap shift. Compatible starts therefore have all cyclic gaps >=m and fix disjoint letters. Marking one of j starts and counting ordered excess gaps gives (n/j) binom(n−mj+j−1,j−1), including n=m and the full-tiling case; the empty case is separate. The expansion in t−1 counts these joint prescriptions, yielding the multinomial law and biased iid PGF without any assumption of independent hits. The start conflict graph is claw-free: if n<3m three disjoint m-arcs cannot exist; otherwise three mutually nonadjacent neighbors would have two successive offset gaps >=m in a span <=2m−2. The Chudnovsky–Seymour theorem then gives real zeros, and nonnegative PGF coefficients with positive constant term from any constant-letter sample make them strictly negative. The degree is achieved by a maximum separated start set of floor(n/m) positions, not merely by an arbitrary inclusion-maximal set. Normalized factors are nondegenerate Bernoulli PGFs. Independently checked 1,059 composition moments and corresponding biased iid moments for binary and ternary examples, including same-composition 0012/0102 and n<m; /workspace/branches/replay-cyclic.py. The infinite claims use the combinatorial and real-rootedness arguments.

## originality

PASS

The evaluated distinct contribution is the exact joint cyclic/content-conditioned law and its full anagram-equidistribution consequence, together with the Poisson–binomial identification for the same cyclic window model. The placement counts, general real-rootedness theorem, and linear unbordered-word Poisson–binomial law are prior; they are not individually claimed as new.

## value

PASS

Fixed composition is a natural constrained-word null model, and cyclic wrap-around changes the admissible placement counts. A full distribution rather than just the probability of avoidance or a mean is useful for finite conditional calculations; it proves the exact anagram invariance uniformly across composition classes. The iid result identifies the distribution class and nondegenerate factor count for those same circular observations. The useful fact is the joint specialization, not recomputation of known cycle-power coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
