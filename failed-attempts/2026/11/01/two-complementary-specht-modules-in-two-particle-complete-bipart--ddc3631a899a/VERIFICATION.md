---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two-particle subdivision criteria apply directly; inclusion of the deleted-product model is natural under relabelings. In its ordered model orient graph edges from the m-side to the n-side. A top chain is an array indexed by i,k on the m-side and j,l on the n-side, zero for i=k or j=l. The cellular boundary equations are exactly zero sums in each of the four coordinates, so top cycles are Z_m tensor Z_n, where Z_s is the space of zero-diagonal s-by-s arrays whose row and column sums vanish. Under transpose the symmetric part of Z_s is the kernel of the unordered-pair row-sum map P_s to U_s (surjective for s>=3 since sums of two distinct basis vectors span). It is B_s, including zero at s=3. The skew part is the kernel of contraction by augmentation in exterior degree two, namely the exterior square of the standard representation, C_s. Particle interchange negates simultaneous transpose because it exchanges the two oriented square directions. Rational transfer therefore gives precisely B_m tensor C_n plus C_m tensor B_n. Graph part exchange swaps those distinct summands at equal sizes, giving trace zero and the index-two induced module; at m=n=3 the homology is zero. The character and dimension follow by counting fixed unordered pairs with the proper symmetric/skew signs. Independently, the frozen Euler proof uses the correct Ko–Park H1 rank, and its equivariant total-trajectory map is surjective by moving a particle around a generating four-cycle with a spectator outside it.

## originality

FAIL

Distinct Resultary d4b214ea3d72 explicitly states the same H2 representation, boundary cases, Betti formula, character and part-exchange trace. Its actual scope is all m,n>=3 despite the word balanced in its title. The index-two induction description follows from that exact restricted representation, since the part exchange interchanges its two inequivalent summands. A separate indexed theorem also supplies the same module by ordered-to-unordered rational transfer.

## value

FAIL

An unknown complete symmetry decomposition on this natural graph family would have structural value. Here the same representation, character and full-group action are already supplied by exact indexed coverage. This formulation offers no distinct invariant or new consequence beyond character arithmetic and routine induction from the covered representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
