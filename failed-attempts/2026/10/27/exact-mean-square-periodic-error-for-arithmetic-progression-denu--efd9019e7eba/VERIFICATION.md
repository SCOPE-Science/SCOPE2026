---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For odd a coprime to d, the three moduli are pairwise coprime. At z=1, equivalently using z=exp(-w), each factor expands as 1/(mw)+1/2+mw/12+O(w^3); taking the residue with exp(tw) reproduces the stated quadratic and constant. All other poles are simple; the root-of-unity waves have mean zero and disjoint nonzero frequencies on Z/(abc), so Parseval gives the sum with weight 1/(16m^2). Reindex by d: the residue pairs are (1,2) up to sign at the odd outer moduli and (1,1) up to sign at the middle modulus. For odd m, sec^2(j pi/m) = csc^2(pi/2+j pi/m) and the csc^2 multiplication formula at pi/2 gives m^2-1 after removing j=0. The pointwise mixed-product identity then gives the outer polynomial; the quartic sum gives the middle polynomial. The empty modulus-one term is zero, and (1+4+1)/2880=1/480 is the fixed-d leading variance coefficient. As a separate finite replay, for each residue t loop over z=0..floor(t/c) and y=0..floor((t-cz)/b), counting when a divides t-cz-by; sum the integer residuals scaled by 12abc and their squares. This reproduced mean zero and variances 209/5184, 953/12544, 238069/2592000 and 740134/4465125 at (a,d)=(1,1),(1,3),(3,1),(5,2), respectively. The frozen verifier was inspected, not executed; neither its reported 66 cases nor the separate spot checks prove the infinite claim.

## originality

FAIL

No separately stated identical variance was established. The failure is mechanical prior implication, not evidence of an earlier verbatim headline: the published denumerant wave formula gives all Fourier coefficients, pairwise coprimality makes their supports disjoint, and the AP residues force only the classical quartic moment and a direct double-angle reduction to quadratic and quartic moments. These operations already determine every coefficient and the RMS corollary.

## value

FAIL

An exact L2 error for a canonical approximation is a well-motivated diagnostic. Under these AP hypotheses, however, its evaluation is a routine substitution into the previously explicit coefficient formula followed by standard moment identities, not a substantive independent exact invariant under the required acceptance bar. The parity restriction makes the doubled-angle evaluation directly accessible and the fixed-d asymptotic just adds the leading quadratic terms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
