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

The two stages give z_i^+=(1-cv_i)z_i+hω_iJz_i, and orthogonality reduces conservation to M_1-2cM_1+c²M_2=0. Both moments are strictly positive; the source's plus-root for ε gives the smaller c root, valid up to the double root M_2=M_1. At each successful step the active set is unchanged because F_i>=v_i>0. Writing r=M_2/M_1, the top factor exceeds each lower factor by c²(v_*-v_i)(v_*+v_i-r)>=(v_*-v_i)v_i/4. For v_*<=1, F_*<=2 on the near branch, so every lower-to-top ratio contracts uniformly, and total energy conservation implies the stated geometric concentration; the top group grows strictly whenever a lower group is active. For v_*>1, r<=1 forces F_*>=1+v_*(v_*-1)/4 at each successful step, giving the floor bound and ruling out indefinite feasibility. The exact example has initial M_1-M_2=3/256 and strictly negative next gap; independent symbolic reconstruction checks the discriminant scaling and witness.

## originality

FAIL

The indexed October 25 Resultary record gives the same one-step formula and global sharp feasibility boundary, identical finite-failure bound, and a one-success witness at the same frequencies; it strengthens the loss-of-feasibility result to arbitrary real-root switching. The date-coded ordering does not establish priority. The subcritical geometric cascade is not separately stated there, but follows directly by comparing factors in that record's exact modal update and using its all-step feasibility theorem. The differing energies in the witness do not supply a distinct obstruction.

## value

PASS

The combination of exact conserved total energy, systematic loss of lower-modal invariants, and sharp eventual loss of the correction above the spectral boundary is an informative warning about long integrations. The scientific usefulness of those results does not make the rederived boundary or the alternate witness an incremental contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
