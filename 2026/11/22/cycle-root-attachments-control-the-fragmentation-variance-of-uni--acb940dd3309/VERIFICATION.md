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

Let S and E be the numbers of surviving vertices and edges, and Z the indicator that all cycle vertices survive. The surviving induced graph has cycle rank Z, including on the empty outcome, so K=S−E+Z and the mean follows from the host having n edges. In Var(E), only pairs sharing one vertex contribute off-diagonal terms, adding 2W p³(1−p) to n(p²−p⁴); Cov(S,E)=2n p²(1−p). For cycle covariance, each cycle vertex contributes p^ℓ(1−p) to Cov(S,Z). An edge on the cycle contributes p^ℓ(1−p²) to Cov(E,Z), and a cycle-to-off-cycle edge contributes p^(ℓ+1)(1−p). Every other edge is independent of Z; in particular a chord cannot exist. Subtraction gives Cov(S−E,Z)=−(ℓ+h)p^(ℓ+1)(1−p). Together with Var(Z) this proves the stated variance and sign, including zero variance at p=0,1. For n≤5, any possible h disagreement requires a triangle and two noncycle vertices; the one-attachment pendant chain has one leaf, while the two-attachment alternatives each have two leaves. For the displayed six-vertex pair the cycles are 345 and 124, and h=1 and 2 respectively at identical degrees. An independent union-find enumeration found labeled counts 1, 15, 222, 3,660 by order, and verified both raw moment polynomials by grouping retained subsets by size (7,796 exact equalities). Direct half-retention variances of the pair were 31/64 and 27/64. The proof, not the census, establishes the all-order law.

## originality

PASS

General induced-component laws and the tree variance mechanism are existing coverage. The distinct result supported here is the reduction of unicyclic variance to the attachment count after degree and cycle-length matching, including strict all-p ranking and the sharp minimum pair. This is an exact structural comparison, not a new general procedure to compute the component law or a historical priority certification.

## value

PASS

When mean fragmentation and degree inventory agree, knowing the number of branches incident to the cycle is sufficient to order fluctuations strictly at every nondegenerate survival probability. This is a structural invariance and identifiability statement useful for comparing small redundant networks, not just two evaluated graphs. The six-vertex minimum identifies exactly when that distinction can first arise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
