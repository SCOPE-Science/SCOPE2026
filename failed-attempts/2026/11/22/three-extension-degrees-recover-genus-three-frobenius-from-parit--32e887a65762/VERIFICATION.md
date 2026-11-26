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

The Galois-equivariant Riemann–Mumford identification gives the two parity sets of quadratic refinements of the Weil pairing over an odd field. The difference Q(Ax)−Q(x) is linear for symplectic A, giving exactly the stated affine action u↦A(u+d_A), and Arf(Q_u)=Q(u). Independent `python3 /workspace/reviews/reproduce_4.py` enumerated the ordered symplectic bases by choosing three successive symplectic pairs in orthogonal complements; all 1,451,520 matrices were covered. It tested Q_u(A^ne_i)=Q_u(e_i) on the six basis vectors (sufficient since the difference is linear) rather than using the supplied affine permutation algorithm. It found 18,24,30 distinct signatures at the three cutoffs. Because these signatures are class invariants and ATLAS gives exactly 30 classes, each third-cutoff fiber is one class. Orbit-length inversion on one representative per fiber matched both complete parity spectra and class sizes in all 30 frozen CSV rows. The class then determines the action on the nonzero vectors of J[2]. On the hyperelliptic locus the 28 odd labels are branch pairs and the even labels are the fixed pencil and complementary four-subsets. The (7,1) and (5,3) examples really have (0,1),(0,1) through degree two and (0,1) versus (3,1) at degree three, as independently checked in `reproduce_2_3_5.py`. Products of irreducibles of those distinct degrees work over every odd finite field. These checks do not imply that all abstract classes are realized on curves over a fixed field or recover a curve Weil polynomial. The frozen C++ artifact was inspected, not executed.

## originality

FAIL

The finite-group contribution is mechanically covered by published data for these very two actions, not merely suggested by an abstract class count. ATLAS explicitly identifies both standard-generator representations and supplies a representative word per class on the same generators. Thus evaluating those words on the 28 and 36 points and counting fixed points of each of three powers is a direct readout on 30 existing rows, with no need to construct or enumerate the symplectic group. The pages also identify the permutation characters as 1+27 and 1+35b, giving the equivalent character-value/power-map readout. Riemann–Mumford, in the cited primary source, already supplies the arithmetic identification for all curves in scope. The application is not printed verbatim in ATLAS; the failure is concrete implicit coverage, not an assertion that ATLAS prints the exact theorem. The arithmetic sharpness examples additionally overlap exactly with the distinct hyperelliptic record; priority between the two same-day findings is not inferred.

## value

FAIL

The inverse question uses natural arithmetic invariants and the theorem is correct. But the proposed new contribution is a narrow table readout: prior geometry identifies the two actions and the prior class-aligned standard-generator data directly determine all rows. The all-odd-field witness repeats the distinct paired record's exact sharpness result. An exhaustive recensus or rewording supplies reproducibility rather than an unknown exact invariant or an independent scientific remainder. No repair was made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
