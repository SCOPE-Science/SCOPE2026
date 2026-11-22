---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Every nine-point E in F2^5 has affine rank at least 4. Full-rank affine configurations correspond via their augmented columns to even dimension-3 binary length-nine relation codes of minimum weight≥4. Their generator-column multiplicity vectors form exactly 11,440 weak compositions and 148 admissible vectors; GL(3,2) basis changes produce six classes. Independently reconstructed all six rank-5 representative dual-code Walsh histograms and exact stabilizer orbit sizes, matching 27,339,520 labeled sets, including the (15,13,3,0,1) duplicate with orbit sizes 6,666,240 and 2,222,080. Independently enumerated all 11,440 nine-subsets in F2^4 under translations and elementary linear shears, finding rank-4 orbits 240,6,720,4,480 and 62 unique affine hyperplanes. Total 27,339,520+62*11,440=28,048,800=binomial(32,9). The original verifier independently checks direct Walsh sample histograms against relation dual weights and all six rank-5 code classes; the proof reduces to these complete finite sets. Different column-multiplicity multisets prove the two classes inequivalent.

## originality

PASS

Danielsen–Parker short binary-code equivalence and graph ELC methods give classifying infrastructure, but the inspected primary work does not tabulate precisely these 9-point F2^5 Walsh-magnitude histograms, their sole double fiber and labeled prevalence. Published 6-, 7-, and 8-point Walsh profiles concern different support cardinalities; 8-point Fourier nonzero-support counts do not dominate the full nine-point odd-support magnitude profile. An old short-code weight-enumerator database could implicitly encode the six rank-5 types, and explicit transformations remain a residual novelty risk.

## value

PASS

The unlabeled Walsh absolute-magnitude histogram is a natural phaseless invariant of sparse binary supports. Its exact injectivity failure and two inequivalent witnesses, complete nine-class census and count of 8,888,320 ambiguous sets give a substantive finite inverse-spectral classification, not an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
