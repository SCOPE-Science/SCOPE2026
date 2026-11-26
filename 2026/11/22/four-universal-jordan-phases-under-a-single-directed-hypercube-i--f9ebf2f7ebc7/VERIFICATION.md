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

Let δ=d mod 2 and H=A+δI. The commuting cube flips give H²=0, and the cube split H=[[D,I],[I,D]] with D²=I gives im H=ker H of dimension r. For E=e_u e_vᵀ, e_u is outside im H because He_u≠0, and e_vᵀ is nonzero on im H because Hᵀe_v≠0. Thus ker(H+E)=ker H ∩ ker e_vᵀ has dimension r−1. With K=H+E, a=He_u, b=Hᵀe_v and ε=e_vᵀHe_u, direct multiplication gives K²=a e_vᵀ+e_u bᵀ of rank two, K³=abᵀ+εE and K⁴=εK². The endpoint scalar ε is exactly adjacency. For ε=0, the power ranks r+1,2,1,0 select one size-four nilpotent block and r−2 size-two blocks. For ε=1, K² projects onto span(e_u,a) on which K swaps the basis, giving J2(1); on the complement K has square zero and half rank, giving only J2(0). The shift by δ swaps eigenvalues if d is odd without changing lengths. In the Fitting decomposition, entry by t requires the initial nilpotent component in ker F^t and imposes no constraint on the unipotent component. Counting its fixed spaces for powers 1,2,4 and taking differences gives the stated primitive state populations; each orbit of length ℓ has ℓ fibers of size q^(m−s). The largest nilpotent block or nonzero primitive-period count certifies the claimed sharp times and order. This handles d=2 (no spare blocks in the nonedge case) and every extension of the binary field. Independent exact replay: python3 /workspace/branches/frozen_exact_checks.py 2, covering all five binary dimension/distance cases at d=2 and 3; it matched the entry and period populations.

## originality

PASS

The closest cube perturbation records toggle both orientations, producing genuinely different operators and invariant factors. General rank-one interlacing characterizes which invariant factors can occur when vectors vary but does not choose the actual form for this ordered endpoint pair. The endpoint-sensitive Jordan selection and the resulting all-dimension census are distinct on inspected evidence; the general Fitting census method is inherited linear algebra.

## value

PASS

A one-way input defect is a natural minimal modification, different from removing or adding a bond. For an infinite symmetric family it produces only two adjacency classes and a parity switch, despite potentially large changes in exact return periods or extinction. The result resolves not only ranks or eigenvalues but the smallest extinction bound, entry-time distributions and individual basin sizes; these are useful for analyzing sensitivity to one-way input edits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
