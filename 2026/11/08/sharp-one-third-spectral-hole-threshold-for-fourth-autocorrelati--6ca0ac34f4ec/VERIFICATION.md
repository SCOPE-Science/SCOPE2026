---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For finite abelian G, real f with S=supp(fhat) contained in the nontrivial coset a+H of index-two H and |S|>2|H|/3: equality of fourth autocorrelations yields equal magnitudes from (s,-s,s,-s) and multiplicative Freiman-two identities r(s1)r(s2)=r(s3)r(s4). If D=(a+H)\S, 3|D|<|H| ensures simultaneous s,s+t,s+t+u in S for all t,u in H, giving well-defined character delta(t)=r(s+t)/r(s). Since -s0 in S, delta(2s0)=r(s0)^2, so delta extends across the index-two coset with value r(s0), and Fourier inversion gives a translate. At |S|=2|H|/3 the Z6 spectrum {1,5} with phases 1 vs (i,-i) has the same zero-sum quartic Fourier products yet is not a translate: i is not a sixth root. Recomputed pair/three-translate intersections for 53682 cyclic test triples and checked all six Z6 quartic products. Finite tests are corroboration, not proof of the all-group assertion.

## originality

PASS

After comparing exact statements, hypotheses, data orders and implications, no inspected stronger source subsumes the surviving precise claim; known prerequisite results and any overlapping subclaims are expressly credited. This is best-of-knowledge, not a claim of proof of historical priority.

## value

PASS

This is a natural sharp missing-frequency tolerance for recovering real signals from one fixed fourth-order autocorrelation in an index-two spectral coset. The 1/3 erasure boundary is structural (three-translate consistency) rather than an arbitrary parameter slice, and the counterexample identifies exact failure at the uniform threshold. It is not a stability or algorithmic decoding claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
