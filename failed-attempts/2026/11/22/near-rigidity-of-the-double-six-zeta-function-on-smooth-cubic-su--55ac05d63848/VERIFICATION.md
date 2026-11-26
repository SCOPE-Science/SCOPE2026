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

I independently recomputed the matched line/double-six spectra, class sizes, Picard traces and fixed ranks for every class. Starting with the blow-up intersection lattice, a 6-cycle and transposition of the E_i generate S₆ and a Cremona reflection completes W(E₆). A simultaneous orbit compares the 36 root lines {r,−r} to the 36 unordered double-sixes, starting from the root 2H−ΣE_i whose reflection exchanges the E_i sixer with its conic sixer. I checked the Schläfli incidence of all orbit pairs and the equivariant bijection on that orbit. Two actions give 51,840 elements with 25 conjugacy classes. The independent Picard calculation uses H=E₁+E₂+L₁₂ to get the trace and the average trace over powers to get the invariant rank. All 25 rows of the frozen CSV match as a multiset in class size, both spectra, trace and rank. Sole duplicate: 1²2³4⁷, with (class size, line spectrum, trace, rank) = (1620, 1⁵2¹4⁵, 3, 4) and (3240, 1¹2³4⁵, 1, 3). Adding the rational-line count separates all 25. Replay: `python3 -B /workspace/review-evidence/double_six.py <path-to-frozen-certificate.csv>`. From a finite étale zeta function the fixed counts of all powers are recovered by its logarithm, then the cycle multiplicities by Möbius inversion. The standard geometric identification works in every characteristic; the result is a statement on the Weyl-class universe, not that all classes occur over every field. Das Table 5 confirms (1²,4)=4D=C₁₈ and (2,4)=4B=C₅ by label and size. Loughran–Trepalin Theorem 1.1 applies to both for q≥7 as claimed (indeed q≥3 for this pair). The point counts use 1+q·tr+q² for a smooth cubic surface. The frozen verifier was inspected, not executed.

## originality

FAIL

Exact earlier ATLAS actions encode the two spectra used in the main finding. I extracted the published degree-36 and degree-27 standard generator arrays and mechanically queried the joint class spectra; they give the entire frozen comparison, not merely some compatible orders or a potential database hit. The geometric action identifications are the corresponding standard coset actions. The only ambiguous types also appear as a collision in the same-day restricted blow-up table, independently of relative priority on that day. The arithmetic distinctions and occurrence are determined by the already tabulated class labels and realization theorem.

## value

FAIL

Unordered double-sixes and Frobenius recovery motivate a useful question. Here the precise answer is a routine query of established finite permutation data followed by standard arithmetic interpretation. Re-enumeration from a geometric realization is a good reproducibility check but contributes no new invariant or mathematical obstruction beyond the already encoded spectra and class arithmetic. The rational-line repair is precisely the fixed-count column of the companion published action. No distinct valuable corrected claim was found.

The dated certificate retains the supplied scientific assessment, sources and limitations.
