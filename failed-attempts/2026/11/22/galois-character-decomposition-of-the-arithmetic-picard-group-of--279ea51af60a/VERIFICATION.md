---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The indicated rational linear change gives the smooth signed diagonal quartic. Each pair of coordinate equations yields cancellation: the first and third families pair terms with opposite coefficient signs and use even exponents, and the middle family pairs terms with equal coefficient signs and uses odd exponents. RESULT line 44 reverses those verbal sign descriptions, but its line equations and the actual incidence calculation are correct. To see exhaustiveness directly, restrict the four coordinates to a projective line. Fourth powers of at most four distinct proportionality classes of nonzero binary linear forms are linearly independent (normalize the first coefficient in suitable coordinates and use the first rows of a Vandermonde matrix). Each represented class must therefore contain at least two nonzero forms for its signed contribution to cancel; a line requires at least two classes to span the two parameters. This forces two pairs and precisely the listed types. Adjunction gives self-intersection −2; distinct intersecting lines have distinct tangent directions and intersection number one. Independently, for each pair of lines I treated their defining equations as a graph of exponent differences modulo eight. A common projective point exists exactly when at least one connected component's exponent-difference constraints are consistent (all coordinates in inconsistent components must vanish). Using this Gram matrix and the coordinate exponent permutations, elimination modulo 101 gave lower bounds 20 for the Gram rank and 9,7,2,2 for its character parts. These are exact rational ranks: the geometric K3 upper bound is 20, the four rational isotypic subspaces are disjoint, and their lower bounds sum to 20. This is a proved upper/lower-bound argument, not an assumption that modular rank always equals rational rank. The group traces and the counts of line orbits and singleton orbits agree with all five stated fields. The geometric Picard group is torsion-free, so the factorization through L on the rational span also holds integrally. Its character action on Gal(L/Q) is faithful, giving the minimal field of trivial action. There is no further descent obstruction for invariant classes here: Y has the rational point (1:1:0:0), hence Br(K)→Br(Y_K) is injective for the fields in question. This proves the stated ranks and supports the field-of-definition interpretation.

## originality

FAIL

Bright's 2002 thesis gives a stronger coefficient-to-integral-Galois-module and fixed-Picard-rank classification for diagonal quartics. It applies directly to (1,−1,1,−1), a rational model of the very surface in the frozen record, not to a merely analogous Fermat surface. The signed quartic's rational ranks and character multiplicities are mechanically recoverable from that classification and its fixed-part algorithm; the prior line permutations also give the ancillary line counts. This is a failure for coverage by an actual stronger result, not a claim that a table row printing the exact four numbers was found.

## value

FAIL

The BHK equation motivates asking about arithmetic descent, and the numerical character table is correct. But the invariant is a routine specialization of the earlier explicit, stronger integral Picard-action classification. The line counts are likewise a small calculation from the existing coefficient-to-line permutations. No further lattice, descent, or mirror-symmetry question is answered that needs a distinct result here. No worthwhile independent narrowed claim was established, so no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
