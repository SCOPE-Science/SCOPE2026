---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For the transitive tournament on n>=1 vertices with edges i→j for i<j, each site samples its OUTGOING downstream neighbors, positive states 1..k-1 (k>=3) progress automatically, and zero is excited iff downstream state 1. If downstream suffix has excitation rounds precisely 0..b−1, the new upstream vertex follows x_i+t mod k through those b rounds. Exactly x_i≡1−b mod k adds excitation at time b; any other choice stops excitation forever. Processing suffixes n→1 yields invertible triangular recoding d_i≡x_i+b_{i+1} mod k and burst B=Σ1[d_i=1], hence exact binomial counts and distribution under uniform words. For B>=1 the last excited unit decays to zero k−2 rounds after its last excitation; B=0 words have exact zero-excitation cumulative count (t+1)^n. These cases yield the stated first-extinction polynomial, unique maximal word and fixed-k CLT by binomial convergence. Independently evolved all (k,n)=(3,4),(4,4),(5,4) words and checked the histograms; finite tests corroborate only.

## originality

PASS

The classical Greenberg–Hastings model and papers on undirected excitation and auxiliary tournament expansions do not imply the exact directed complete-feedforward extinction polynomial or triangular Hamming-weight recoding. Related cyclic successor-contact on tournaments advances colors only with contact and is a distinct update. No earlier statement giving the same all-k binomial law or sharp unique extremizer was found in the searched material. Priority remains best-of-knowledge.

## value

PASS

A finite-state directed network family with a nonlinear excitation rule has a nontrivial exact all-n,k census, a sharply attained maximal extinction clock, and a simple asymptotic distribution derived from a non-obvious triangular bijection. These are natural dynamical invariants and useful potential baselines for arbitrary acyclic graph excitation; no generalization is claimed without proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
