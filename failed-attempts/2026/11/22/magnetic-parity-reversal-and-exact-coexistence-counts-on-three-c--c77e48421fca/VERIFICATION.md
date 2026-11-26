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

Let k be the number of favored vertices, B their complement, and c the total monochromatic edge cost. Cubicity gives c=3(k-n)+e(B)+b(B); c>=0, and equality in c>=3(k-n) holds exactly when B is independent. Independence allows at most one selected vertex in each rung, with alternating sides away from the reversed seam; odd n has two size-n sets, even n has no size-n set and 2n size-(n-1) sets (the hole and either compatible alternating pattern). For even n, at k=n-1 the complement of a maximum independent set induces three edges, a forest by triangle-freeness, hence 2^(n-2) assignments. For k=n, cost one forces each color-zero/complement part to induce one edge. A doubled favored rung would already use its only edge and imply exactly one empty rung; one of its two neighboring rungs would then have a favored vertex, imposing a second edge. Thus all rungs are split, the unique frustrated longitudinal link has n choices and two side patterns, and the complement has 2^(n-1) proper two-color assignments. At k=n+1 the 2n independent complements each admit 2^(n-1) arbitrary assignments. The two cubic bounds eliminate all other candidates off saturation for nonnegative field, and comparing the candidate lines gives exactly the stated crossings and counts; x>3 selects the unique all-favored state. At x=3 all independent B contribute 2^|B|. In the three-state rung transfer the symmetric subspace has characteristic polynomial lambda^2-3lambda-2 and the swap-odd eigenvalue is -2, yielding the signed hard-core formula and entropy. At x=0 the six-state transfer in cyclic orientations and their reversals has diagonal blocks J_3-I_3 and off-diagonal blocks I_3; the swap-even block is J_3 and the swap-odd block J_3-2I_3. The signed trace is exactly the stated chromatic count. Direct integer enumeration independently agreed on ground energies and degeneracies at eight rational fields for each n=3,...,6 (32 cases), including ties.

## originality

FAIL

Chang–Shrock (2009), arXiv:0907.0925v2 §II.A Eq. (2.33), gives an exact arbitrary-length Möbius square-strip partition function with a single favored color, not merely a cyclic counterpart. Width 2 and q=3 are precisely this graph and spin model. The positive-field ground envelope, favored-population sectors and labelled multiplicities are initial exponents and coefficients of the exact two-variable specialization. This is verifiable broader exact coverage of the invariant, not just a similar technique or an unavailable possible source. The frozen case-by-case simplification is not asserted to appear verbatim in the 2009 paper, and the direct combinatorial interpretation is useful, but the submitted result does not frame a separate independent contribution beyond the specialized census. The 2009 antecedent is absent from the frozen comparison.

## value

FAIL

The even/odd contrast for a natural twisted ladder is well motivated, and the proof is a useful transparent extraction of ground-state data. But the exact census submitted as an independent contribution is a width/color/temperature specialization of a known exact Möbius field enumerator; the result does not establish an additional independently useful mathematical invariant beyond those census data. The elementary cubic reduction explains the extraction, not a new claim beyond it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
