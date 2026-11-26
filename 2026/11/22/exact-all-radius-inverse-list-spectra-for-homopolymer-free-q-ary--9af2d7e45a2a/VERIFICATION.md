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

For fixed nonempty receiver y, matching greedily assigns each admissible parent a unique prefix, internal skipped blocks and suffix. A skipped block must avoid the next matched symbol; the first skipped symbol of an internal block must also differ from the previous matched symbol. A prefix of length s>0 has (q-1)(q-2)^(s-1) choices. An internal block for unequal targets has (q-2)^s choices including s=0; for equal targets it has (q-1)(q-2)^(s-1) choices and s>=1. The suffix has (q-1)^s choices. These counts respect both adjoining matched positions, so concatenation and the greedy decomposition are inverse. Multiplying gives the exact excess-length series, including m=1 and d=0, with no count of deletion masks. Coefficients a_t of (1+z)/(1-(q-2)z)^m are positive, and C(t)-(q-1)C(t-1)=a_t proves strict ordering and exact support. If d>0, either r>0 and the prefactor is at least two, or r=0 and C(d)>1. Independently choosing the initial letter and the equality locations gives the class sizes and binomial law; the LLN and the lattice-normalized binomial CLT give the threshold and stated floored window. At m>=d+1 the last nonzero class is r=d with C(0)=1. Independent finite enumeration verified each receiver size and adjacency-class multiplicity in 42 parameter configurations (8,901 receivers).

## originality

PASS

Pass for the explicit all-radius coefficient law and the resulting adjacency-ordered inverse spectrum for linear adjacency-distinct q-ary parents. Greedy matching and regular-language rationality are established ideas. The closest same-day inverse-spectrum work uses a genuinely different source constraint; no chronological priority is inferred from its date.

## value

PASS

Exact inverse-list size for a receiver is a natural uncertainty measure in a deletion channel with a nearest-neighbor constraint. The result collapses variation across q^m outputs to one easily measured statistic, gives the complete sorted nonzero sizes and their exact frequencies at every radius, and distinguishes impossible observations from possible ones, including a sharp feasibility window. Those are independently useful even though the derivation uses elementary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
