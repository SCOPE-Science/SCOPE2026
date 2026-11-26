---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Reconstructed the isometries and the two-sided block equivalence directly: a coefficient at index k in V_n e_j contributes to output floor(k/m), whereas V_n V_m^* is constant on that output block. This gives (H-J)/sqrt(mn), where J is all ones. For n>=m the row at floor(nr/m) meets column r positively and no later column, proving full column rank for H; transpose for m>n. The common constant is an orthogonal singular direction, and the full shared step-function space has dimension gcd(m,n), so centering removes one unit level and one rank. A unit top right vector of one block copied to successive blocks is weakly null, proving equality of essential and ordinary norms (and noncompactness, since the rank is positive). For n=m+1 the two entries per column give the displayed second-difference operator; binomial expansion cancels degree j+1 and gives coefficient 2j+j(j-1)=j(j+1) at degree j. Polynomial evaluation gives all levels, including the constant mode removed by centering. The levels converge as Riemann sums under t->sqrt(1-t^2), yielding the stated density and beta moments. Checked RESULT.md lines 27–55 and inspected check_adjacent.py without running it; its numerical rank tests are supplementary, not the proof. This includes equal bases and divisibility cases.

## originality

FAIL

The decisive distinct Resultary record d9f30fffe04e supplies the same finite overlap Gram data, not just a similarly parameterized commutator spectrum. Its Definition and Proof §§1–4 identify E_k=V_k V_k^*, give the principal-cosine matrix I-L/n for the reduced interval pair and diagonalize L when the reduced bases are ±1 modulo the smaller base, including adjacency. In the frozen Hardy semigroup K=V_m^*(I-E_mn)V_n, since V_m^* V_mn=V_n and V_mn^* V_n=V_m^*. The global constants on each mn-cell are the range of E_mn; the only change to the known cross-Gram block is deleting that one shared direction. The adjacent levels, rank, gcd unit multiplicity and norm and the elementary limiting law follow mechanically. Thus the scientific content is already covered by a distinct stronger result in combination with the known semigroup identity; the shared publication date does not establish which result came first.

## value

FAIL

The exact invariant is well motivated in the Hardy semigroup, but after the stronger overlap-compression analysis the difference is one known constant projection per cell. Rank, unit-level arithmetic, adjacent hierarchy, and weak limit need only this identity and elementary spectral transfer or Riemann sums. No independently useful unknown exact invariant survives in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
