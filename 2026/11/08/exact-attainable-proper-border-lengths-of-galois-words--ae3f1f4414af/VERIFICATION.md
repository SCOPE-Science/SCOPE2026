---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The definition uses strict alternating lexicographic rotation minimality and forces primitive words. The elementary even-border parity contradiction compares two rotations after an even shared border. If an even-length Galois word has odd period d<=n/2, two rotations starting at kd and (k-1)d (n=kd+r) produce the same first differing letters at positions r+j and d+r+j of opposite parity, contradiction; proper powers excluded. Therefore any proper border b is odd and even n forces 2b<n. Odd n witnesses (01)^((n-1)/2)0 have every odd proper border; even n b=1 uses 010^(n-2) and b>=3 uses 010^(d-1)10^(b-2) with d=n-b, and strict rotation comparisons prove all witnesses Galois. Independently exhaustively enumerated all binary words n=2..13 and directly tested explicit witnesses for all allowed n<=69; both match. The infinite proof rests on the two-rotation obstruction and generic witnesses, not finite enumeration.

## originality

PASS

Best-of-knowledge PASS for the *complete attainable* proper-border-length spectrum. Reutenauer 2006 Proposition 3.1 and Dolce–Restivo–Reutenauer 2019 Lemma 35 establish odd border parity only; Hendrian–Köppl–Yoshinaka–Shinohara 2024 Lemmas 11–16 analyze shortest odd/even periods and roots for pre-Galois words, but neither state nor directly imply the half-length restriction for even Galois words plus explicit all-allowed binary realizations. Checked full 2024 primary PDF, not just an abstract. An unindexed equivalent characterization remains a risk.

## value

PASS

A natural combinatorial structural invariant of alternating-order Lyndon/Galois words: closes the gap from known border parity to the exact all-length existence spectrum, including a sharp new forbidden half-length region for even n and binary witnesses for every allowed odd b. It supplies a complete infinite-parameter classification valid for all ordered alphabets of size >=2, not an arbitrary finite slice or solely a restatement of old parity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
