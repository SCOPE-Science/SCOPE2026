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

On the crown K_{n,n}−M each deleted pair has closed sums B+a_i−b_i and A+b_i−a_i adding to W, so W≥2. At W=2 their equality to one gives (n−2)(1−B)=0 and duplication with common sum 1. For n≥4, such a vector has at least two negatives; opposite-shore positive total 1+r with r≥2 supplies rescue for every −1 and, after subtracting its paired 1, for every 1. Examples at n=4 and 5 extend by appending a duplicated −1,1 block at each two-size increment. At W=3, n≤3+(n−2)B≤2n gives B=1 or 2 for n≥4. In the B=1 orientation the differences are 0 or 1 and sum to 1, allowing only (2,1) or (3,2). The common vectors sum to 0 or −1 and have at least two negatives, so both total positive sums are ≥3; the unmatched 1, where present, sees positive sum r≥2. Counts follow by shifting each common label by 1, including the 2n choice of mismatch shore and slot. A duplicated weight-2 vector obeys the Roman rescue tests exactly when a 3 or at least two 2s occur; counting the other cases gives the parity formula. The table's 'Excluded Roman minima' header means Italian minima excluded from the Roman class, not Roman minima. At n=3 and W=3, B may also be 0 or 3, but B=0 would require all three differences to be exactly 1, forcing b_i≥1 and contradicting B=0, and B=3 is symmetric. With B=1 only the (2,1) mismatch can have two common labels with the prescribed sum, namely (−1,1) in either order, and the mismatched 1 then fails rescue; B=2 is symmetric. The n=3 W=2 possibilities leave only permutations of (−1,−1,3). Replay: RESULT.md 29–41 and python3 /workspace/reproductions/crown.py, which independently groups the shores by sum to enumerate weight 2–4 for 3≤n≤6 and checks both predicates on explicit graph neighborhoods. Its weight-2 (Italian,Roman) counts are (3,3),(12,0),(40,30),(90,30), and Italian weight-3 counts 0,48,140,420. For n=4 the script finds no Roman functions at weights 2,3 and 42 at weight 4. Supplied code and transcript were inspected, not executed.

## originality

PASS

The surviving new contribution on inspected evidence is the signed Italian layer classification and enumeration, especially the one-mismatch next layer; the Roman minimum and its weight-2 duplicated structure, and the scalar Italian minimum where implied by it, are credited as known. The exclusion formula quantifies the Italian-versus-Roman difference, not a new Roman minimum theorem.

## value

PASS

The exact low-weight classification on an infinite canonical family improves on a scalar minimum: every optimum synchronizes the deleted matching and every next-layer labeling has exactly one constrained defect. The parity-dependent split from Roman optimality explains concretely how the two established predicates differ on crowns. The classification does not pretend to give the entire polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
