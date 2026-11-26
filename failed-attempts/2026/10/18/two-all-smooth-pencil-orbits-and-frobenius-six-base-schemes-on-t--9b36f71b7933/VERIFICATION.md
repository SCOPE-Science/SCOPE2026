---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Geometric smoothness on the blowup is equivalent to smoothness of the representing plane cubic: a singularity off the centers persists, and multiplicity at least two at a center gives an exceptional component of the anticanonical divisor meeting the strict transform (or a multiple exceptional component). A smooth plane cubic, in contrast, lifts isomorphically. Euler's identity in characteristic two identifies its singularities with the common projective zeros of the three quadratic partials. The partials have no common projective zero exactly when their degree-four multiples span all degree-four forms (regular sequence Hilbert series, and evaluation at a common zero for the converse). Exact rank enumeration returned 23 masks and 12 all-smooth binary pencils; coordinate permutations and Cremona reversal give the two six-element orbits under the split automorphism group, with the stated point multisets. The fresh exact replay checked all 12 pencils in F_64, in each case finding the three centers with distinct tangent directions for the two generators and six residual points in one length-six Frobenius orbit. Smooth cubics are geometrically integral, and distinct pencil members have no common component, so the six residual points exhaust the intersection number (-K_S)^2=6 after blowup and each is simple. Evaluating at a rational surface point would give a pencil in the kernel of any proposed all-smooth net, contrary to rational-base-point exclusion. Exhausting dimension-three subspaces by smooth triples independently gave zero. The statement is about H^0(S,-K_S), not the unrestricted space of plane cubics.

## originality

FAIL

The central theorem is mechanically implied by two distinct indexed findings. The ambient binary cubic-pencil orbit table determines the twelve pencils and the two full surface orbits. The split degree-seven reduced Frobenius theorem implies the entire residual degree-six base-scheme result by blowing up the third marked point, and the degree-seven no-net statement also restricts to this section space. These are statement-level implications, not an inference about precedence from the shared registry date.

## value

FAIL

An otherwise unknown complete Frobenius classification at the split del Pezzo boundary could be useful. Here blowing up the unique simple rational base point in the known (1,6) stratum directly gives the asserted residual scheme, and the marked orbit restriction gives the asserted catalogue. The separate count of 23 smooth sections and explicit sextic certificates give useful reproduction details, not a supported independent gap or structural theorem once those exact implications are credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
