---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Using original pinned RESULT.md, four-grid DFT isolates constant D(R), first B(R)=Rh01+R³h12 and one real Nyquist Re(h02e^{2i angle}). Radial determinant rs(s²−r²) nonzero iff radii differ, angular two-by-two determinant ∝sin(2delta) gives off-diagonal vanishing; two mean equations give kernel exactly t*diag(r²s²,−(r²+s²),1), invertible for r,s>0. Equal-intensity vector difference aa*−bb* has rank at most 2 and cannot equal a nonzero kernel rank3; all coefficient vectors including zero are phase-unique. Equal radii or zero sine have explicit ambiguous polynomial pairs. If <=7 rank-one measurements on complex C³, real Hermitian kernel dimension>=2; its 2D circle of matrices has an indefinite singular element by odd determinant plus no nonzero semidefinite kernel element when samples span, giving rank-one ambiguity. Independently constructed exact SymPy lifted 8×9 matrix at r=1,s=√2,delta=pi/4 (nodes 1,i,-1,-i and (1+i) times these), verified rank8 and nullity1. Source checker inspects alias failures; finite test not a proof of all parameters.

## originality

FAIL

Decisive published coverage: October 18 all-degree theorem states universally for d>=1 the iff r!=s and sin(d(delta))!=0, so degree d=2 recovers the entire 4+4 square claim. November 1 independent all-degree theorem does likewise. A November 8 published degree-two theorem has the same lifting rank eight, exact diagonal null generator and no-seven-measurement bound. All three complete original mathematical texts were read and directly compared, including hypotheses and proofs. Neither changing to Hermitian language nor reproducing the lower-bound certificate creates novelty.

## value

FAIL

The radius–twist phase diagram is a natural and nontrivial design question in isolation, but this precise if-and-only-if classification, its Hermitian rank8 kernel and the global eight-sample minimum are already established in the fully inspected published general and same-degree theorems. Present work supplies no independently needed exact invariant, gap, improved boundary or nontrivial extension; recomputing the known result has no distinct scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
