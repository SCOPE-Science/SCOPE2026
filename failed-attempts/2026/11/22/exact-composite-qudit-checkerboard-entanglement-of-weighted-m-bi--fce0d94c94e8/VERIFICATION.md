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

The physical even/odd matrix, with a consistent shift direction, is B=I+S⁻¹+wS^((n−1)/2). Multiplying by S gives I+wT+T² with T=S^((n+1)/2) a single n-cycle and T²=S. For f=t²+wt+1, multiplication by t on Z[t]/(f) is C=[[0,−1],[1,−w]]. The cokernel of I+wT+T² is Z[t]/(t^n−1,f)=coker(C^n−I); the n−2 extra factors are units. The recurrence gives the entry gcd g and det(C^n−I)=2−tr(C^n)=2−L_n. If g=0 the block is zero; with g>0 the second factor is |2−L_n|/g, zero if rank one, and divisibility follows from the determinantal divisors. For w=−2 the difference is n times a primitive rank-one nilpotent; w=2 gives −2I+n(C+I) and therefore gcd(2,n)=1 and determinant 4 at odd n. The remaining three weights use C³=−I, C²=−I, and C³=I for w=−1,0,1 respectively, giving the displayed periodic cases. A local Fourier transform makes the odd labels Bᵀx, so equal-sized fibers of this homomorphism give a flat reduced spectrum with rank its image size. Smith operations stay invertible over Z/dZ, including composite d, and scalar diagonal factors have image size d/gcd(d,s), with gcd(d,0)=d. The ternary deficit when 3∤n is present only if 3|d, as the stated entropy formula indicates. Fresh replay passed 135 integral Smith comparisons, 42 exact modular-image checks and 28 small direct spectral checks (tolerance 10⁻¹⁰); OPENBLAS_NUM_THREADS=1 python /workspace/replay_frozen.py 2. The bounded replay does not prove the infinite claims, and the packaged checks are not independent attestations.

## originality

FAIL

The main rank-two integral reduction is an exact specialization of Noferini–Williams, arXiv:2408.08662, Theorem 3.11. After a single cyclic shift and change of generator, putting f=t²+wt+1 and g=t^n−1 in that theorem gives the precise block I_(n−2)⊕(C_f^n−I₂), for all weights including singular ones. The reported formulas are the entry gcd and determinant of that block. The spectral translation merely reads the image size of this same map over Z/dZ by local character orthogonality. Neither the recurrence table nor the reduction to the composite-d spectrum leaves a distinct scientific claim independent of these implications. This finding is correct but mechanically covered, not rejected for an inaccessible reference or for overlap by title alone.

## value

FAIL

The cut and entropy are natural and the formulas useful as a worked application, but the asserted new invariant is mechanically implied by the known swap theorem once the physical shift is written down, followed only by the two determinantal divisors and character orthogonality. The seven weight cases just evaluate that same 2×2 formula. No additional exact invariant, boundary phenomenon independent of those calculations, or surviving nontrivial classification was established that would justify a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
