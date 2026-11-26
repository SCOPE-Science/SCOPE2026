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

The finite extension property realizes the admissible diagrams over the named base, and ultrahomogeneity makes the diagram determine the complete ordered type. For each new point, transitivity is exactly the downset/upset conditions and strict cross-comparability between its L and U. Partition into the core K (three choices per index) and the lower-heavy D and upper-heavy E, each of size R_n: a heavy pattern has an ordinary nonempty subset of the corresponding extreme level or an exceptional singleton b_j (dually a_j) lacking only its matching element on the other level. For x<y, L_x⊆L_y and U_y⊆U_x are necessary and sufficient by inspecting the new two-edge paths. K,K gives 6^n; K,D and E,K each give (2^n−1)3^n+2n3^(n−1); D,D and E,E each give 3^n−2^n+n2^(n−1)+n (ordinary inclusions, then exceptional-to-ordinary, then exceptional identity); E,D gives R_n², and the other channels are impossible. For x∥y the two cross intersections U_x∩L_y and U_y∩L_x must be empty and this is sufficient. K,K gives 9^n; each core/heavy orientation gives 5^n−3^n+2n3^(n−1), counting a factor of two instead of three at each excluded index; same-heavy pairs give R_n² each, and opposite-heavy pairs give n each because only matched exceptional indices can avoid intersection. Summing gives the displayed formulas, with x<y just one orientation. The leading terms are 3·6^n and 9^n, proving 2C_n/T_n∼6(2/3)^n. For the complete height-two contrast, the core has independent lower and upper subsets: core pairs contribute 9^n to C_n and 16^n to I_n; all pairs involving a heavy profile number O(8^n), giving the claimed 2(9/16)^n. I inspected the frozen code and its recorded output, without executing it. An independent bounded replay, python3 /workspace/branches/reproduce_pair_counts.py, checked adjacency rows for transitivity directly and gave (one-point count,C_n,I_n)=(19,161,247),(47,870,1543),(119,4721,10331) at n=2,3,4. This is corroboration, not the all-size proof.

## originality

PASS

The all-size closed pair formulas and sharp comparability asymptotic are the supported distinct claims. Neither the one-point spectrum nor the n=2 disjoint-chain specialization is novel here. The closest distinct catalogue records cover the same pair question for other bases, and one covers the same base for one point; none of the inspected statements already determines the all-n pair result.

## value

PASS

Standard examples form a natural test family for finite extension counts over named parameters. The closed spectrum isolates the effect of removing a perfect matching from the complete height-two base: it changes both the comparability decay base and the leading factor, with explicit exceptional terms. This is an all-size structural comparison for logical types, not an extrapolation from the already covered two-chain instance or a probability measure on sampled points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
