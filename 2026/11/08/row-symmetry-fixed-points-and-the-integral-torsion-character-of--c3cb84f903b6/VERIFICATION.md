---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

A geometric H-fixed simplex cannot contain a vertex in any moved row: its orbit includes two rooks in the same forbidden column. Thus only the k individually H-fixed unit-capacity rows plus the heavy row remain, yielding Y_{m,k} exactly, where k<=2 for nonidentity H<=S4. Every Y_{m,k} facet uses all capacities, has dimension m-5+k and satisfies shellability condition of Jojić–Vrećica–Živaljević Theorem 4.4: m >= (m-4+k)+(k+1)-1 = m-4+2k for k<=2. Direct face count f_{j-1}=sum_{a+b=j} C(k,a)(m)_a C(m-a,b), 0<=b<=m-4, and alternating-binomial Euler identity give beta0=C(m-1,3), beta1=mC(m-2,2)-C(m-1,3), beta2=m(m-3)+C(m-1,3). Independent face-count Euler checks for all 12 pairs 5<=m<=8,k<=2 passed. For ambient Z/3 torsion, Limonchenko–Yu arXiv:2610.37827 Theorem 5.7 and pages 19–20 explicitly prove a unique Z/3 via their integral relative cokernel (5.10), with generator tau=sum_{|D|=3}R^{(2)}_{D,min D} (5.11) and relations q^(2)=-q^(3). Transposition of second/third unit rows interchanges the (2),(3) families, mapping tau to -tau, hence full S4 sign. Every R^{(2)} summand is an exterior word with exactly one factor per column; any column permutation contributes its global sign on the m factors, and relation independence of p ensures tau transforms by sign(S_m). The two actions commute, hence product sign. This uses the actual integral presentation, not inference of action from Z/3 abstract type or mod-three sample data.

## originality

PASS

The Limonchenko–Yu 2026 paper proves the ambient Z/3 torsion and even a Moore-space wedge; that existence is expressly prior, not a new claim. The additional full S4xSm action on its unique torsion generator is extracted from (5.10)–(5.11); a known Jonsson 5x5 sign phenomenon is acknowledged as special case, not claimed original. The complete geometric fixed-space homotopy profile for all nontrivial H<=S4, all m>=5, using the shellability theorem on smaller fixed chessboards, is a separate uniform equivariant refinement. The original torsion paper does not state both of those additional conclusions in its main result as read.

## value

PASS

Connects a persistent natural 3-torsion family with a full row-and-column sign character and explains the torsion-free topology of every proper row-symmetry fixed space. This is a structural, all-parameter equivariant refinement, not a restatement of the known torsion rank; the β_k formulas give explicit geometric tests for symmetry-induced changes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
