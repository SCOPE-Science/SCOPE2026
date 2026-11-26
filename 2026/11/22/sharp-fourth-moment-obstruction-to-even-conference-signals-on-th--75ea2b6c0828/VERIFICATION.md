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

A sum of four unit phases can vanish only in antipodal pairs: when the midpoint of a pair is nonzero it determines the unordered pair uniquely and the other pair has the negative midpoint; when it is zero each pair is antipodal. Normalize f(1)=1 and pair it with one of f(2), f(3), f(4). In each case write f=A+zB with A,B real even vectors supported on the two pairs, z unimodular. Their DFTs are real, so the power spectrum is the DFT of P+2 Re(z)R with P=A*A+B*B and R=A*B (cyclic convolution). Independently formed those integer convolutions for each partner. Parseval gives the same polynomial 9 sum_s (P_s+2 Re(z)R_s)^2 = 792+432(Re z)^2 in all three cases, and the DC term is zero. Minimum 792 occurs exactly at z=±i, equivalent to the claimed permutations up to a common phase. Plancherel gives total power 72 in the eight nonzero frequencies, with flat-spectrum energy 648. For the unit-border matrix, row orthogonality against the border is C1=0, and the lower square block of MM* is J+CC*: hence the circulant core must have squared DFT eigenvalues 9 off DC, and symmetry of the circulant core is precisely evenness. The obstruction therefore applies to the prescribed class only. Exact replay: python3 /workspace/review_evidence/algebra.py (conference block).

## originality

PASS

The even cyclic conference-signal question, the energy framework and the bordered-matrix equivalence precede this result. The closest retrieved primary paper explicitly distinguishes its observed table from an exhaustive classification. Its zero observed even entries at order nine do not give a proof, still less the exact minimizing energy and all equality cases. The exact catalog match is the identical assigned record.

## value

PASS

Order nine is not an arbitrary truncation: it is an explicit cyclic case of the literature's open even-signal question with a published nonexhaustive zero count. The exact gap proves robust separation in this energy under the specified constraints, identifies all nearest candidates in the fourth-moment sense, and rules out the normalized symmetric circulant construction in that case. This is more than recomputing a numerical count or ruling out a guessed candidate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
