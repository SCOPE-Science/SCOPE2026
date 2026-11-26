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

The graph includes all length-(n−1) words, with equal in/out degrees q for the zero-containing vertices and 1 otherwise; paths via 0^(n−1) prove strong connectivity. Edges are distinct permitted windows, including loops, so fixing the unique 0^n edge is exactly choosing one rotation, not choosing an extra labeled start. For m=n−1 set a=x+q and b=q−1. The de Bruijn shift adjacency B has B^m=J, is q on constants and nilpotent on the zero-sum subspace; the b-ary subshift B_T obeys the corresponding identities. For a T-to-T walk of length j<m each appended symbol persists to the end, so none is zero and the restricted block of B^j is B_T^j. For j≥m this block is q^(j−m)J_T, versus b^(j−m)J_T for B_T. Thus the compressed resolvent and that for aI−B_T differ only in the all-ones term, which C=bI−B_T annihilates. The determinant lemma now multiplies x(x+q)^(q^m−1) by det((a−b)(aI−B_T)^(−1))=(x+1)^(b^m−1)/(x+q)^(b^m−1), including b=1 and m=1. This proves the determinant identity over the rational function field and hence at all x. By the row-Laplacian matrix-tree theorem the linear coefficient is the sum of rooted in-tree counts. Strong connectivity and the zero row and column sums give identical diagonal cofactors (the adjugate is proportional to the all-ones matrix). Dividing q^(q^m−b^m) by q^m and multiplying by the BEST product for a fixed first edge gives the formula. The supplied verifier computes a single principal cofactor in each test case, despite the broader wording in RESULT.md line 86; equality of all rooted counts is justified by balance and rank in the proof, not by that finite test.

## originality

PASS

Existence is already covered, the binary case is mechanically the classical binary de Bruijn count, and an earlier exact catalogue theorem gives the entire q≥3,n=3 count. The supported distinct contribution is the general-alphabet, all-order closed enumeration beyond those covered cases, and the full Laplacian factorization on the deleted-subalphabet graph beyond the known regular/loop-only cases. The existing weight-two enumeration does not give the count for the broader family at n>3, and generic tree and tour formulas do not compute this characteristic determinant.

## value

PASS

For a natural language with one mandatory letter, existence does not quantify the number of exact cyclic indexes. The closed all-order formula avoids an exponentially growing determinant in the genuinely larger nonbinary cases; the full characteristic determinant gives a structural explanation of the simple product and all rooted tree counts. This goes beyond the already covered binary and order-three counts or the trivial order-two star.

The dated certificate retains the supplied scientific assessment, sources and limitations.
