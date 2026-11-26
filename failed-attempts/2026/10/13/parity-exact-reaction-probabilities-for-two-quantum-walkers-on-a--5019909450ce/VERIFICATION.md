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

With every coincidence rate positive, ker Q is the orthogonal complement of the full coincidence diagonal. The largest H-invariant subspace D in ker Q reduces H and Q. On its complement the imaginary-part identity for any K-eigenpair forces strict negativity, since a real eigenvalue there would give a dark H-eigenvector. Thus the complement decays and the asymptotic absorption operator is the orthogonal projector on the H-cyclic span of the coincidence diagonal, for arbitrary allowed rates and any initial density matrix. Common translation splits this span into the cyclic spans of the coincidence Fourier vectors. In a nonflat total momentum k the energy cosines agree only on q↔k−q exchange orbits, and the coincidence vector projects nontrivially on the unique symmetric direction of each orbit. At even n and k=n/2 all energies are zero, leaving just one bright vector; the lost symmetric dimension is (n+f)/2 with f=#{q:2q=n/2}, namely f=2 for 4|n and 0 for n=2 mod 4. Subtracting that dimension and adding one from the full symmetric rank gives exactly the three ranks. On a distinct ordered pair the symmetric weight is 1/2; the removed symmetric π-momentum weight is [1+1_{2d=0 mod n}(−1)^d]/(2n), by common translation of the reversed pair. The replacement coincidence vector is orthogonal to distinct pairs, and all coincident pairs are fully bright. The factor two for normalized distinct-site bosonic states and zero for antisymmetric states follow directly. Independent Fourier-sector checks for n=3..8 matched all 199 ordered diagonals and all six ranks; see /workspace/branches/36da69d4-00f3-4fc0-92c1-e16b541a1641/reproduce_cycle.py and repro-small.log. The frozen verify.py was inspected, not executed: its reported finite-time counter counts propagations, not 24 separately enforced accuracy inequalities, and its sitewise comparisons are numerical. Neither check replaces the all-n argument.

## originality

FAIL

A distinct indexed magnetic-cycle theorem gives the full bosonic dark projector, ranks and localized pair laws in the exact frozen model at Φ=0. In the ordered space the remaining sector is exchange-antisymmetric and completely dark, so adding it, or projecting the input onto the symmetric sector, gives every ordered formula without a further spectral claim. This is demonstrable current coverage, not a finding of earlier priority against the frozen record. The magnetic paper's own prior-work section credits an earlier exact zero-flux analysis without identifying it there; that acknowledgement is consistent with the frozen finding originating the special case and does not resolve provenance.

## value

FAIL

The mod-four antipodal law and rate-independent flat-sector deduction are meaningful for the natural reaction model. In the current comparison they are already supplied by the exact zero-flux sector of a verified catalog theorem. The difference of using ordered instead of symmetric inputs adds only a known loss-free block and a fixed symmetric weight; it supplies no further uncovered exact invariant or phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
