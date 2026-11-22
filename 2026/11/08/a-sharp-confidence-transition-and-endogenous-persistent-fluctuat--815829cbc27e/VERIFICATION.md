---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Reconstructed both directed distances from the actual Eq.(3). The hub sees zero; each binary leaf sees p or 1-p. For eps<=min all leaves never update and iid hub recursion follows. For eps>min a 1-or-2-edge word changes some leaf; independent selection forces such a change almost surely. Geometric contraction yields stationary law/W1/moments; Borel-Cantelli long runs give liminf=0/limsup=1. For rho=1/2 independent binary digits give full support, uniformity iff p=1/2 and singular entropy dimension otherwise. Boundaries eps=min, rho=1/2, z=0/1, m=3 and p rational all inspected. Independently wrote and ran 26,928 exact directed gate/moment checks and 704 two-edge escaping witness checks; finite checks do not establish the infinite assertions.

## originality

PASS

The frozen original is NOT novel as stated: its entire three-agent P3 consensus/nonconvergence theorem was already published on 2026-10-25, with further mixed-NDW coverage on 2026-11-02. It cannot be passed unchanged. The final repaired claim excludes m=2 and describes the exact multi-leaf full-freezing threshold min(k/m,1-k/m), with biased and balanced stationary geometries for m>=3. The asymmetric star gate follows directly from the NDW definition but is not asserted or proved for this family by the inspected antecedents. Exogenous-stubborn gossip gives the stationary-law consequence AFTER closure, and Bernoulli product dimensions are classical; neither mechanism is claimed new independently. Originality of the combined endogenous multi-leaf classification is best-of-knowledge, limited and subject to priority risks.

## value

PASS

The repaired claim establishes a natural, exact and sharp group-balance boundary for permanent endogenous leaf unresponsiveness on all binary K_1,m stars with m>=3. On the same graph, imbalance controls the geometry of the stationary hub law at half compromise: uniform for balanced groups and singular but fully supported for unequal groups. This is a motivated structural classification of a graph-model mechanism beyond the covered P3 theorem, not a generic new Bernoulli-product dimension result; its short gate calculation and classical probabilistic consequences are candidly delimited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
