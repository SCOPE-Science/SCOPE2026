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

Label columns j by the pair (j,j+n); only the boundary exchanges the two rows. For a zero bit in a middle column b, the three distinct neighbours give the exact test 1≤a_r+b_(1−r)+c_r≤2. Starting at (τ(c_(n−1)),c_0), the n transitions end at its row-swapped state and charge every middle-column weight once; the fixed index zero makes this a bijection with labelled subsets, not a count modulo rotation. The row swap J fixes four of the sixteen pair states and has six two-orbits, giving dimensions 10 and 6, and commutes with T. Independent exact subset-DP determinants reproduce both sector polynomials over Z[y,z]; twisted trace and the determinant logarithmic derivative agree in the bounded replay. The formal identity over Q[z] then proves the enumerator for all n≥3. Under z=t², y=w/t the exponent is 2|S|−n and all powers of t are nonnegative. For L=log(D₋/D₊), w∂_w L₀=4w²/(1−w⁴), L₁=w³(3−w²)/(1−w²), and the degree-0-mod-4 part of L₂ is 4w⁴/(1−w⁴)²; these identities were checked exactly. At 4|n the last expression contributes n at w^n before taking the Euler derivative, giving n² at order t². At odd n order t has coefficient 9 at n=3 or 2n for n≥5, and at n≡2 mod 4 order zero has coefficient 4. These are precisely the first nonzero orders and give the stated minima and multiplicities.

## originality

PASS

Credit is for the full restrained enumerator with Möbius closure, and its optimal-set counts not already explained by the efficient case. There is substantial shared machinery and even identical determinant factors with the indexed untwisted result. Its inspected statement uses only the ordinary trace and product and does not identify the determinants of the row-swap eigenspaces. The Möbius proof needs that identification and a twisted walk correspondence; no priority is inferred from same-day dates. The scalar domination minimum and efficient criterion are not treated as new.

## value

PASS

Restrained domination is an established predicate on this natural cubic family. The twist changes which small sets close up and, in particular, replaces four optimum sets in one even congruence class of the circular ladder by a quadratic count there for the Möbius ladder. The full signed-sector enumerator quantifies this boundary effect at every cardinality and gives explicit comparable data beyond the scalar minimum. The utility lies in the spectrum and parity effects, not just another proof of efficient-set existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
