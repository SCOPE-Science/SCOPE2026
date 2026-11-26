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

The theorem holds. The restriction of the inverse Fourier transform from the band to a finite observation set is Hilbert–Schmidt, and its product with its adjoint is the sinc compression. Strict positivity on the single interval ensures a simple even positive top state. Reflection on the translated interval followed by the two-component sum/difference gives the exact blocks T±C_D, with kernel K_W(D−x−y). Their isolated leading eigenvalues are the top two overall for large D because C_D=O(D⁻¹) in norm. At D=d+τ/d, put s=x+y and ε=(−1)^n. Expanding gives ε[−sin(ωs)/d+(ωτ cos(ωs)−s sin(ωs))/d²]/π with uniform operator O(d⁻³). The first-order kernel sends φ to −Aq/π and has expectation zero; the second-order expectation is (ωA²τ−2AB)/π. The reduced-resolvent term L is the same in both branches. Differentiating the kernel gives a uniform expansion of its τ derivative; taking its expectation in the normalized branch eigenvectors φ+O(d⁻¹) gives slope 2εωA²/(πd²)+O(d⁻³) for the signed gap. Opposite endpoint signs and strict monotonicity yield an exact unique crossing in the stated window, with detuning τ_*+O(d⁻¹). Leading-order unrestricted expansion gives the global sorted formula by parity. The area estimate uses bounded continuous K_W on finite sets, not global L¹: the word 'integrable' in the frozen assumptions is inaccurate if read globally, since |sin(ωt)|/|t| has divergent integral, but this is not a premise of the theorem or its proof. A new 64-node full-block and parity-matrix diagnostic at (a,W)=(1/4,1/2) and (0.6,0.3), including odd and even n=31,64,129, matched the branches, slope signs and centroid values; replay: OPENBLAS_NUM_THREADS=1 python3 /workspace/checks/frozen_review_checks.py sinc. This is numerical corroboration only.

## originality

FAIL

The exact crossing and shift are covered by the distinct Resultary record 9ba5ac6c3bc3 (in larger fixed-width windows, with a global two-term signed gap). The global leading and compact-detuning two-eigenvalue formulas, including the common second-order height, are covered in 89cae306647a with arbitrary interval length. The two papers together cover the precise claimed conclusions under explicit dilation and translation. The separate catalogue entries have later path dates; the finding is substantive overlap of the reviewed claim with the existing catalogue, not an assertion of earlier historical priority or a derivation relationship. No distinct scientific conclusion remains simply from presenting both equivalent results together.

## value

FAIL

An exact displaced degeneracy is scientifically more meaningful than a small numerical gap. Here, however, that degeneracy, its shift, and the doublet expansions are all reproducible from the overlapping findings; evaluating the common height then requires only substitution. The reviewed record determines no higher-order coefficient, additional band range or other separate invariant. There is no substantive remaining increment to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
