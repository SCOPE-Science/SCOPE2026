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

For the finite open chain with positive alternating a,b, T* T has diagonal a²+b² and off-diagonal ab. The orthonormal sine vectors give simple positive singular values E_l, paired eigenvectors (Tv_l/E_l,±v_l)/√2, and a single A-only vector with w_(x+1)=−(a/b)w_x. The span of clean eigenvectors zero on all lossy sites reduces both H and the loss matrix. An eigenstate on its orthogonal complement cannot have real eigenvalue under K: taking the imaginary part forces it to vanish at every monitored site, making it a clean dark eigenstate. Thus the complement decays even with Jordan blocks, and total survival is the dark-projector trace. For the B monitors the common sine-node indices are l=tn/g by Bézout; the sine-square sum is zero when g divides x and g/n otherwise, giving the asserted weights and dimension. The A-input finite sum follows from the left components and the normalized zero mode. A single A absorber sees the zero mode everywhere; consecutive sine factors cannot both vanish, so a nonzero pair survives exactly at the stated positive ratios. Endpoints see all eigenvectors. At n=6,j=2 the positive roots of b/a=−2 cos(πl/6) are 1 and √3, with one pair each. The example correctly asserts √3 is locally isolated, not that it is the only resonance. The maximally mixed formula follows from the projector trace. Frozen verification files were inspected, not executed.

## originality

FAIL

A distinct indexed result verifies exact coverage of the principal minority-sublattice theorem: same odd open Hamiltonian, arbitrary nonempty even-site monitor set, positive alternating hoppings and rates, 2g−1 dimension, lone zero mode iff g=1, exact same sitewise plateau, and even the dark energies. The even physical sites are B_j=2j, and absorption is one minus the displayed survival. The common 10/12 catalogue date does not establish priority in either direction, but the mathematical overlap is exact. The remaining single-A catalog is obtained by directly imposing the pre-existing nodal trapping criterion on the explicitly known odd-chain eigenvectors and solving a single linear equation for b/a per index; the frozen record does not resolve collisions of ratios beyond counting the qualifying indices. The two parts do not establish a distinct combined theorem beyond the exact overlap and this spectral substitution.

## value

FAIL

The exact gcd plateaux are worthwhile physics and mathematics, but that substantial exact classification is already represented by the matched record. As a remainder, the A branch applies the node criterion to a known coordinate amplitude and expresses its roots by direct division, without a further classification of ratio collisions, counts, or other structure. A combined presentation is useful exposition but does not supply a separately valuable surviving new mathematical gap result at this scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
