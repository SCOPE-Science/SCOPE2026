---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The primary abstract confirms decomposition of every Boolean truss into a Boolean-ring truss and a rectangular truss and classification up to isomorphism. For a finite Boolean ring, the ring is \((\mathbb F_2)^r\) and its ring automorphisms permute the primitive idempotents, giving \(S_r\). A rectangular truss with left and right heap coordinates has multiplication \((g,h)(g',h')=(g,h')\); a heap-and-multiplication automorphism must preserve the two rectangular congruences and therefore acts by independent heap automorphisms on the coordinates. Heap automorphisms of a finite abelian group are affine, hence \(\operatorname{Hol}(G)\) and \(\operatorname{Hol}(H)\). The displayed product and order formula follow. The inspected brute-force script is only a small consistency check.

## originality

FAIL

The automorphism formula is a mechanical consequence of the published classification/decomposition together with standard automorphism facts for finite Boolean rings and abelian heaps. The focal source already identifies exactly the ring and rectangular factors whose independent symmetries are being multiplied. The absence of an explicit automorphism theorem in accessible metadata does not create implication-level novelty.

## value

FAIL

Computing the automorphism group of a natural class can be valuable, but here no new nonstandard obstruction or classification remains after the published product decomposition: the answer is obtained by applying standard factor automorphism groups and multiplying them. Under the same value bar used elsewhere, this is too mechanical to retain as a standalone finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
