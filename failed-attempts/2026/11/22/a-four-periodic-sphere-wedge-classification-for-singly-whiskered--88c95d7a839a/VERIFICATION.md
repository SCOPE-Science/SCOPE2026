---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The exact homotopy types are correct. The leaf toggle pairs its closed star on the augmented face poset and leaves just the two choices of a full edge e={0,1} or {0,n-1}; a face outside the star cannot contain both. Filling either e forces its exterior neighbors to be omitted, leaving P_{n-4} for n>=4 and the empty graph at n=3. Contractible star(e)=e*Ind_2(G-N[e]) meets the leaf star in the boundary of e joined with the same residual, and the two edge stars intersect inside the leaf star. Collapsing the contractible leaf star, a CW subcomplex, gives a wedge of two double suspensions of the residual path complex, with a circle per arm for an empty residual. The frozen Morse proof gives the same result: on the path, an unpaired face has selected vertices 1,2 and omitted 0,3, giving the size shift by two and length decrease by four; the four bases yield the stated dimensions. Successive pivot acyclicity follows from Deshpande–Singh Proposition 2.10, or by the star being a downward-closed paired subposet with no upward matched cover leaving it at that stage. The two residual families are incomparable, so they can be patched independently. Deleting the empty face simply restricts the augmented directed graph to the remaining vertices; the wording about making the leaf terminal via an additional cover is inessential. The Morse model has one 0-cell and two equal-dimensional cells or just the vertex, which suffices for homotopy, not only homology. The uploaded verifier and expected table were inspected, not run; finite counts do not prove the classification.

## originality

FAIL

The exact result is mechanically implied by a prior one-vertex splitting theorem that does not require the graph to be chordal: Deshpande, Shukla and Singh, arXiv:2001.06775v1, Theorem 13 with Remark 1 and Proposition 18. The leaf is simplicial and its two 2-supports are precisely {0,1} and {0,n-1}. Both supports induce edges and both contain N(leaf)={0}. Thus the theorem applies to every singly whiskered cycle regardless of chordality, including the triangle. It gives two double suspensions of the published path types. The alternate toggle proof does not make the same exact classification original.

## value

FAIL

The graph family is natural, but the exact table is obtained by applying the known support theorem to two visibly identical path residuals and shifting dimensions. The frozen result supplies no further invariant or stronger structural claim (such as an equivariant or collapse statement) beyond that mechanical corollary. An alternate Morse derivation and finite confirmation of the same homotopy types do not supply a surviving new exact fact. No repair is proposed or delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
