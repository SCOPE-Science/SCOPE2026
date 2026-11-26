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

For any length-N prefix containing k+1 ones the iterate deletes exactly the first k original ones. Equal images identify the position of the (k+1)st one by the leading zero count and identify the suffix after it. Truncating the originals at N then gives equal prefix images, so injectivity at N forces equality of the originals. For the critical finite checks I used actual factors from the recurrence f(2j)=f(j), f(2j+1)=j mod 2, rather than executing the supplied wildcard code. If P=2^r and n<=P, choose the representative start 1<=a<=2P. All nonexceptional positions are invariant on translating by 2P. The sole multiple of P, if any, has quotient 1 or 2 in that representative window; translating by 2P or 4P respectively gives quotient 3 or 6 and flips its bit. Thus starts 1 through 6P cover every factor. The scan matched all eight counts and collision classes and all four explicit witness starts. At N=13,14,25,26 the respective minima of ones are 5,5,10,11, so the lifting argument applies, and the four predecessor collisions prove sharpness. 'First injective length' in the table means onset of permanent injectivity, not necessarily the first isolated injective length.

## originality

FAIL

Exact claim and proof-level coverage in a distinct indexed record. Its stated range k=1 through 31 contains all four assignments; its periodic skeleton and all-length prefix argument prove the same sharp thresholds, with a weaker minimum-ones hypothesis. This is a finding of mathematical coverage, not a determination of which proof was first, copied, or independent. The indexed path for the broader result is later than the assigned source path. Campbell–Rampersad alone do not settle the four cases: they give the numerical predictions but not the proofs.

## value

PASS

An all-length proof of these proposed sharp stabilization cutoffs is a meaningful automatic-word problem, not just reproduction of the numerical table. Complete factor enumeration plus prefix propagation is a useful finite-to-infinite mechanism. This assesses the scientific problem and proof, not whether the assigned result adds distinct coverage to the index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
