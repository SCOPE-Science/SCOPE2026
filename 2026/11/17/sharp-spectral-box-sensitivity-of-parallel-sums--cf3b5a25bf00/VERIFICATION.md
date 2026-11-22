---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS. The Fréchet derivative of Φ(A,B)=B-B(A+B)^-1 B is H↦C H C* with C=B(A+B)^-1 and exactly ||C||² induced norm on self-adjoint perturbations via rank-one positive H and approximate singular vectors. Integration on the convex spectral box controls all finite differences; perturbing an interior approximation to a boundary pair gives reverse sharpness. For every unit z, u=Az,v=Bz, constraints ||u-cz||,||v-cz||≤r with c=(κ+1)/2,r=(κ-1)/2 yield ||u+v||≥sqrt(2||v||²+K)-r where K=(κ²+6κ+1)/4. Scalar Fκ(a)=a/(sqrt(2a²+K)-r), a∈[1,κ], switches its maximizer at κ=2+sqrt5 and yields precisely Lκ=(κ/(κ+1))² or (κ+6+κ^-1)/16. Explicit 2×2 real reflections with eigenvalues 1 and κ saturate Fκ, commuting on the first branch and noncommuting on the second; Lκ>1 iff κ>5+2sqrt6. Independent reflection matrices for κ=2,4,5,9,12 reproduce formula to floating precision and spectra; proof dimension-free and infinite-dimensional by operator estimates, not finite test. κ=1 excluded; dimension one separately gives commuting branch.

## originality

PASS

PASS with older parallel-sum optimization risk. The pointwise perturbation coefficient ||(A+B)^-1B||² is known from Luo–Song–Xu/Anderson–Duffin, but their theorems do not evaluate its exact worst case on the common spectral interval. Alwadani addresses set-valued monotonicity; Naik–Johnson addresses complementability/block-structured inequalities. The two transition values and explicit noncommuting extremizers survive these comparisons.

## value

PASS

PASS. Noncommutativity changes the sharp global Lipschitz behavior of the basic electrical/operator parallel sum at a nontrivial κ transition, with a second exact threshold where it becomes locally expansive. These phase boundaries and explicit small-dimensional witnesses are meaningful perturbation theory, not a simple renaming of the known pointwise coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
