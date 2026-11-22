---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For all a,b>=3 and 0<=t<=min(a,b), the selected defect edges form one fixed ordered matching. Every mixed face has at most two vertices per shore. After collapsing the fixed contractible shore simplices separately, the resulting two-pole CW decomposition is naturally the unreduced suspension of the square complex Q_t with vertices e_ij, added star edges for deleted diagonals and square cells for each deleted-edge pair; because all shore inclusions and cell labels are fixed, these equivalences commute with t-inclusions. Q_0 has ab isolated vertices; for t>=1 it has a single main component plus (a-t)(b-t) isolates, so reduced H0 differences give degree-one integral basis surviving precisely while both indices >t. In the connected core, leaves collapse and every filled quadrilateral collapses across one path, leaving a subdivision of K_t; the star-at-1 integral fundamental cycles zeta_ij for 2<=i<j<=t are primitive. They are literally retained under inclusion; hence all H1 maps split surjectively, all H2 split injectively, and barcodes [0,1)^(a+b-2), [0,k)^(a+b-2k+1), [t,infty)^(t-2). Independent direct counts for (3,3),(3,4),(4,5) match stage ranks. Source verify_persistence.py constructs actual simplicial filtrations and mod-two finite barcodes for six a,b<=5, but does not on its own prove universal integral functoriality.

## originality

PASS

PASS best-of-knowledge for coherent inclusion-induced integral maps and complete barcode, despite known static homotopy group ranks for each partially deleted-matching stage. The previously recorded two static results were not retrievable in full this execution, so residual risk that their proofs already encode natural maps is explicitly retained. Distinct Carnero forest filtration changes degree threshold, not edges.

## value

PASS

Biclique matching faults are a natural graph filtration. The exact persistence maps and simultaneous primitive integer bases answer a different mathematical question from stagewise homotopy types; they distinguish ephemeral H1 deaths from permanent H2 births and work uniformly in both unequal shore sizes and finite endpoints. The full family result has plausible future utility without requiring a general theorem for arbitrary graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
