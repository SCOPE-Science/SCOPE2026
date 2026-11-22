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

The independent sets of squared path P_n² obey signed recurrence w_m=w_(m-1)+s_m w_(m-3), with empty-prefix boundary w_-2=w_-1=w_0=1. Modulo two the companion transfer has T^7=I, yielding odd unsigned count exactly when n mod7 lies in {0,2,5,6}; then all signed Walsh coefficients are odd and nonzero. For other residues {1,3,4}, complete seed enumeration gives 1,3,6 zero frequencies. Appending signs t1..t7 with t6=-t5,t7=-1 gives exact recurrence identity w_(m+7)=-t3*t5*w_m for all previous prefixes; 32 distinct blocks preserve zero or magnitude, generating at least c_r*32^k distinct zero frequencies. Seed signed sums in each residue have sharp least nonzero magnitude 1 (odd count) or 2 (even count). Therefore convolution character eigenvalues establish inverse/pseudoinverse ℓ² norms exactly 1 or 1/2. Read frozen proof and source check_walsh_path_square.py; independent full Walsh enumeration for n<=16 and all 32 block identities confirmed, but all-n proof rests on the recurrence/block identity, not these tests.

## originality

PASS

The known multivariate independence polynomial permits evaluation at signed fugacities, but its general zero-free **polydisc** theorems and unsigned path-power counts do not yield exact cancellations at every ±1 character, the full mod-seven zero-free residue set, sharp positive gap or 32-block extension. A published period-seven result for MAXIMAL independent sets of ordinary paths is not a claim about ALL independent sets of squared paths, and has different residues. The quantified sharp classification survives these actual comparisons.

## value

PASS

Independent-set indicators of path powers are natural hard-core combinatorial objects. Classifying every dimension's full-group convolution invertibility and minimal spectral gap, with explicit exponentially growing null families, is a structural exact spectral law not inferable from their unsigned counts alone, useful for discrete harmonic recovery/conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
