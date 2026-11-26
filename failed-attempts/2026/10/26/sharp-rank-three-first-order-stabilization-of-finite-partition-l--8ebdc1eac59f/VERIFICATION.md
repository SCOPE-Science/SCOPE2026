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

The pure order EF argument is sound. For a comparable strict pair P<Q, an atom below Q but not P gives (I,L) when P is not bottom; the coatom dual gives (G,I). A pair separated by Q supplies an atom incomparable to both if P is interior and Q is not top. In the incomparable case, meet/join supply the two common strict bounds. The pairs needed for the asymmetric cases come from an atom below exactly one partition or a coatom above exactly one, with strictness controlled by its rank or corank. A pair separated by both exists: otherwise every pair crossing P-blocks would lie in a Q-block, and transitivity would make Q top. Its atom is incomparable to both. This checks the non-chain entries of the extension table. At n≥5 each interior point has an incomparable atom, coatom and middle rank-two point: for an atom pick a triple disjoint from its defining pair, at rank two pick a different rank-two point, and at higher rank merge a triple crossing its blocks. Comparable extension signatures only see clipped height/corank at 3, and the ability to have strict chains of one, two or three steps on each side recovers them; third-point signatures determine the rank-two pointed types by the EF recursion. Since h+c=n−1, the clipped pairs saturate at n=7. The two inner witnesses in the three-step pointed chain test sit in separate branches, so the rank-three separation sentences give all six boundaries and cannot be mistaken for four nested quantifiers. B₇=877 is a minimum within the family only.

## originality

FAIL

A distinct existing indexed record, 5c33f5d07b6d, states the same iff, in the same signature and quantifier-rank regime, with the same seven classes and the same optimal in-family representative size. It also has the same two-point extension table. There is no materially distinct finding in the reviewed claim. This is verified equivalent coverage, not a determination of which record obtained the result first; the matching record has a later listed date.

## value

PASS

As mathematics the classification gives an exact, uniform small-model cutoff for all rank-three sentences in a natural infinite family, with explicit splitting sentences and no enrichment of the signature. It provides more than computing small Bell numbers or sampling logical types. This merits value as a result but not a separate acceptance of a materially covered claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
