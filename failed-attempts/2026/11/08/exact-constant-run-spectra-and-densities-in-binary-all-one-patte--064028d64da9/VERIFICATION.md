---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The valuation formula T_d(x)=[f_d(x-1)!=f_d(x)]=((v2(x)-d+1)_+ mod 2) xor [v2(odd(x)+1)>=d] follows from replacing the terminal 0/ones binary carry and counting deleted/created length-d blocks. In each M=2^d block, the transitions at (k+1)M-2^j with j up to min(d-1,v2(k+1)), and a valuation/XOR boundary event, give exactly the listed gap lengths. Conditioning on v2 and odd residue classes yields all rational per-length frequencies and the sum 8(M-1)/(3M^2). Independently checked 458752 transitions for d=2..8 plus exact frequency mass and mean identities. This is correct mathematics, but it was already published.

## originality

FAIL

FAIL decisive direct prior coverage: published 12 October 2026 Resultary theorem “Complete constant-run spectra and exact frequencies for all-one block-parity words” proves for every k>=2 the identical same word, full same length set, every per-length rational frequency, total density 8(H-1)/(3H^2), and an exact binary-carry transition criterion. Setting k=d,H=M and dividing the prior per-H-block frequencies by H reproduces each submitted coefficient exactly, including duplicate-length convention d=2. The submitted different valuation notation is an equivalent reformulation, not a novel result. That earlier theorem also completes Hendel Conjecture 8 on zero-runs.

## value

FAIL

FAIL as an independent contribution: while the object and invariant are mathematically motivated and the theorem is correct, the full spectrum and all exact densities are a direct known-table/theorem recomputation from the previously published 12 October classification. The rederived carry criterion and arithmetic restatement do not add a distinct motivated new invariant or stronger result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
