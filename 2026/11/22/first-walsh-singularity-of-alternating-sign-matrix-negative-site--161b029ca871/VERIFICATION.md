---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

I independently enumerated every order-1 through order-6 ASM by first enumerating explicit ternary rows with alternating nonzeros starting and ending at +1, then appending rows with a last-nonzero sign test per column and requiring the final sign in each column to be +1. This generates precisely the ASMs with labelled rows/columns; no boundary site can be negative since it would start or end a nonzero row/column sequence. Counts are 1,2,7,42,429,7436 with respective distinct negative masks 1,1,2,7,41,407. I retained multiplicities and computed the full unnormalized spectrum by direct integer sums with signs 1−2·parity(s & x), rather than a butterfly. The trivial-group cases have their scalar ASM counts, n≤5 has no zeros, and n=6 has 180 zeros, 60402 positive and 4954 negative values, least nonzero magnitude 2 and greatest 7436. Thus rank=65356, nullity=180, pseudoinverse norm=1/2 and nonzero-singular-value condition ratio=3718. I checked every listed canonical zero orbit, including the unique weight-eight orbit represented by the given pattern, and all weight counts (4,8,40,96,4,28) for weights 8–13. Exactly 21 orbits have size eight and three have size four. Another direct integer parity sum over the zeros gives H(0)=180 and Σ_(x≠0)|H(x)|=689004. Under unnormalized convolution, the range projection has kernel δ_0−H/65536, giving the exact absolute kernel sum 94295/8192. Convolution attains that endpoint norm on a point mass in ℓ1 and on an aligned sign vector in ℓ∞. Averaging any projection onto the range over translations is contractive in both operator norms, still fixes the range and takes values in it, and must be the unique diagonal Walsh projection onto those characters. This proves the lower bounds without assuming translation invariance. Replay: python3 /workspace/review_evidence/asm_walsh.py with NumPy 2.5.3; see asm_walsh.log. I inspected but did not execute the frozen certificate. The result is confined to orders 1–6.

## originality

PASS

Best-knowledge pass for the first singular size of the multiplicity-weighted negative-site operator, its order-six zero locus and its evaluated endpoint norm. The underlying ASM bijections, bulk refinements, and projection-by-translation-averaging method are not new, and the same spectral methodology appears for other ASM ensembles.

## value

PASS

Injectivity is a natural first-failure question for deconvolution by the labelled minus-entry statistics of ASMs. At order six the complete missing characters describe precisely which signals cannot be recovered, beyond a single singularity witness; the optimal projection norms quantify the best endpoint cost of projecting onto the recoverable range. These are exact benchmarks for that particular natural ensemble, not a new general Walsh algorithm, asymptotic result, or assertion that the range projection inverts the convolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
