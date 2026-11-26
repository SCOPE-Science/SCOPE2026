---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The characteristic-not-two geometric incidence rules in RESULT.md agree with Gonzalez-Hernandez §2.2: the origin and branch pairs are the nodes, the branch singletons and complementary triples are the tropes, and each pair–partition incidence marks the unique third element in the half containing the pair. These descriptions are equivariant, so a flag over an extension is exactly a fixed geometric flag, not a rational point on a conic. The three disjoint flag species have sizes 6, 30, 60; the fixed counts for a permutation with f fixed labels and t transposed pairs are respectively f, f(f-1), and binom(f,2)(f-2)+ft. This proves the general extension formula. The seven branch types with a fixed point are already separated by their distinct positive first counts (96,32,12,8,4,2,1); the four fixed-point-free types have second counts 96,8,0,0, and the final collision 3+3 versus 6 is split by the third counts 96 versus 0. For the node scheme the fixed count is 1+binom(f,2)+t. The incidence matrix is rationally invertible (row inner products are 6 on the diagonal and 2 elsewhere), so it intertwines the node and trope actions and explains their equal cycle multisets. Independent enumeration on all 720 six-label permutations confirmed the table, including exactly the two separate-spectrum collisions 1+1+2+2 versus 2+2+2 and 1+1+4 versus 2+4. Each length-d orbit contributes (1-T^d)^(-1) to the zeta function. There are at least two irreducible cubics and at least one irreducible sextic over every odd finite field, so squarefree sextics of both sharpness types exist there; no assumption that all abstract types occur over each field is needed. The frozen code and CSV are supporting evidence; the uploaded code was not executed.

## originality

PASS

The node/trope actions, incidence rules and substantial base-field counts are already explicit in prior work. In particular separate node/trope spectra are obtainable from those known actions by powering, and are not independently credited. The distinct contribution is the equivariant fixed-incidence count and sharp inverse statement for the first three extension counts, including the uniform realization of the two-count ambiguity. No examined prior statement tabulates or dominates that reconstruction for the 96 Kummer flags.

## value

PASS

Incident supports are a natural arithmetic observable on the classical Kummer configuration. The sharp inverse result identifies exactly how many extension counts suffice to recover the branch splitting, whereas all counts for either marginal scheme can still lose distinctions. It is an exact identifiability theorem for reduced supports in odd characteristic, not a claim to reconstruct the curve, its moduli, or point counts on the quartic itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
