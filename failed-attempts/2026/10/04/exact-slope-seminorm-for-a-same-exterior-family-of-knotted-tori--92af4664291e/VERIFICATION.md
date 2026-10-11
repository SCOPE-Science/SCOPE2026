---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The seminorm calculation is correct. Nifa's peripheral description sends the tangent coordinates to \(\lambda\) and \(\lambda^{-N}\), so \(a[\lambda_r]+b[s_r]\) represents \(\lambda^{a-Nb}\). Nifa's Theorem 6.5 proves \(\operatorname{scl}(\lambda^N)=(N-1)/2\) and also realizes \(\lambda\) as a commutator. Homogeneity gives \(\operatorname{scl}(\lambda^{a-Nb})=(N-1)|a-Nb|/(2N)\). Liu--Ni--Sun--Wang's Remark 4.5 identifies their slope seminorm with stable commutator length and extends it to real homology. The kernel and strip follow immediately. The submitted unstable sublattice formula agrees exactly with Nifa's Remark 6.8.

## originality

FAIL

The stable formula is a direct corollary of two published statements read in full. Liu--Ni--Sun--Wang identify the induced slope seminorm with stable commutator length. Nifa supplies the full peripheral exponent \(b-Nq\), proves \(\operatorname{scl}(\lambda^N)=(N-1)/2\), and proves \(\lambda\) is a commutator. Homogeneity of stable commutator length then mechanically gives the submitted absolute-value seminorm; its kernel, unit strip and independence of the filling index are immediate algebraic consequences. Moreover, Nifa's Remark 6.8 already states the exact unstable singular-genus formula on precisely the submitted index-N sublattice. Therefore the final claim is covered by prior implication even though the word 'seminorm' does not appear in Nifa's paper.

## value

FAIL

The synthesis is clear and may be useful exposition, but the complete stable formula requires only the published peripheral exponent, a published stable commutator-length value, homogeneity, and the published seminorm=scl identification. The unstable part is already stated by Nifa. Kernel, unit ball and equality across the marked family are immediate consequences, so under the stated value standard the result is a routine recombination rather than an independent mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
