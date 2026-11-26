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

Replayed RESULT.md lines 23–53 for F_q-linear multiplication-preserving maps, without a unitality condition. Each cycle is simple: multiplication by a basis vector isolates any nonzero coefficient in an ideal and iterated squares recover the basis. Projecting a homomorphism onto a target cycle, a nonzero restriction to one source cycle therefore injects and is surjective by equal dimension. Two surjective restrictions would force every product in the target to be zero because the source summands annihilate each other, a contradiction. For each active target the resulting isomorphism has one nonzero per matrix row by disjoint-product preservation and the independence of the target basis squares; the cyclic square equations force a shift and coefficients c,c²,…, with c^(2^ℓ−1)=1. Thus h=ℓg labels per source/target pair and (1+rh)^r maps. In a composition-idempotent map each selected source must select itself with the identity label, by cancellation in the group of isomorphisms; conversely these conditions suffice. With k identity loops all other targets independently have 1+kh choices, and projection onto the fixed cycles identifies the image with their direct sum, even when the image is embedded diagonally. This proves the histogram, image type and all ranks, including the zero map, singletons and characteristic two. Independently, all 65536 binary 4×4 matrices at ℓ=r=2 gave 25 homomorphisms and histogram (1,6,1) at ranks (0,2,4); ℓ=1,r=2 over F₂ gave 9 maps and (1,4,1). Replay files: /workspace/branches/e3bed96e-bee5-46fb-82aa-cd18b001524c/record2_independent_enum.py and record2_independent_enum.txt in the same directory. Frozen verify.py was read, not executed; finite checks do not establish the general theorem.

## originality

FAIL

Both findings are direct cases of distinct, inspected indexed records with arbitrary cycle lengths, not just analogous results: f14321710094 covers the normal form/count and 33c828f2883c covers the composition-idempotent rank polynomial. Their more general statements specialize without adding a hypothesis or changing the notion of rank. This is stronger-theorem coverage in the inspected corpus, not a determination of priority from the later catalogue dates.

## value

FAIL

The labelled partial-cycle formulation is useful in the broader setting, but the frozen contribution as a standalone finding is a constant-length substitution into the covered Hom and retraction classifications. The image-type observation follows by projecting onto the identity roots, and the count has the ordinary full-domain-plus-zero derivation once the labels are known. No separate unknown invariant, classification mechanism or application is established by recomputing this slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
