---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The proof reduces every successful initial set on proper double star D_(a,b), a,b≥2, to at most one initially unfilled leaf on either side: with two white leaves at the same hub that hub has at least two white neighbors indefinitely and cannot force. Each initially filled ordinary leaf of a white hub contributes exactly alpha in round 1. The weighted synchronous kernel on two hubs and ≤2 omitted leaves preserves weights, simultaneous thresholding, and one-use directed forces. A white hub fills by round ≤2 or never; an omitted leaf fills by ≤3 or never. Counting (p,q,h,g)∈{0,1}^4 gives coefficient binom(a,p)binom(b,q)E and exponent a+b-p-q+h+g; beta≤alpha gives z^(a+b-2)(z+a)(z+b)(1+z)^2. Independent labeled exhaustive checks on D_(2,2), D_(3,3), D_(2,4) over multiple exact-rational parameters corroborated all-seed enumeration. In D_(2,2), alpha=4/5,beta=1, the specified three-leaf seed succeeds and adding hub y fails, because the required final force is only 4/5. The proof, not finite tests, supports all alpha,beta∈(0,1].

## originality

PASS

No examined earlier source determines this positive-parameter all-seed transmission forcing polynomial for proper double stars. Ordinary zero forcing fort and power-domination results study different propagation rules; the original transmission framework provides definitions and some solved graph families, not this quotient census. Priority is best-of-knowledge; full original arXiv text was inaccessible.

## value

PASS

The all-seed generating polynomial is an exact natural invariant for a standard diameter-three tree family; the constant-size kernel works uniformly in arbitrary leaf multiplicities and transmission parameters, identifies a three-step cutoff and a genuine nonmonotone seed-augmentation witness. These are mathematically motivated structural and classification results rather than a mere renaming of ordinary zero forcing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
