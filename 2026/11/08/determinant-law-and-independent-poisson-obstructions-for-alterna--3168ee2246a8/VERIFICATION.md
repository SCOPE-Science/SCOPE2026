---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Fixing one matching and contracting pairs converts the second matching into alternating cycles with logarithmic combinatorial component weight 1/(2ℓ) (including double edges) and normalizer [z^n](1−z)^−1/2. On a component, both alternating-start modal formulas hold everywhere precisely when each cyclic length-k=2d window contains a Bernoulli mark, treating short cycles by periodic extension. The k-state automaton forbids k successive unmarked bits; trace T_k^(2ℓ) sums valid closed cyclic state walks. The exponential cycle index gives exp(sum trace(T^(2ℓ)) z^ℓ/(2ℓ))=det(I−zT²)^−1/2. For q→0 and nq^k→t, only O_P(1) vertices belong to short cycles, so they contribute no failures, and the remaining O(n) length-k windows have bounded dependency degree with overlapping union >=k+1; Chen–Stein error O(nq^(2k)+nq^(k+1))→0, yielding joint independent Poisson(t) by E/F disjoint type counts. For diverging nq^k, choose Ω(n) disjoint long windows to bound success by exp(−Ω(nq^k)). Monotone reachability gives the two-point depth law; for fixed u∈(0,1), primitive T has simple Perron root ρ<1, and square-root singularity analysis gives Cρ^(2n). Independent exact-rational enumeration over matchings/valuations confirms n=1..3 and d=1..3 with q=3/5; finite evidence not asserted universal.

## originality

PASS

Standard Ewens(1/2) pairing cycle index, transfer-matrix forbidden-run traces and classical Poisson-run approximation are known separate methods. Zantedeschi 2026 establishes S5 modal exchangeability for fixed-frame representation, not a two-independent-pairing frame law. No indexed earlier theorem was found giving this exact matching-averaged determinant plus bivariate E/F obstructions and fixed-u spectral asymptotic. An equivalent old weighted pairing-cycle identity remains a real priority risk.

## value

PASS

The exact all-n all-depth probability law of a natural two-agent random-knowledge frame, and the sharp independent-obstruction critical depth law, link finite combinatorial enumeration to a new probabilistic modal-logic quantity. The combined structural law is more than merely restating standard Poisson approximation for Bernoulli runs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
