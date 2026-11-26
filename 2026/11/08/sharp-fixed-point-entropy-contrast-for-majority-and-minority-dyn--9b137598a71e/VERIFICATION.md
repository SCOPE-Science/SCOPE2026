---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

With the hub fixed, a degree-one leaf copies its parent for majority and opposes it for minority. The two rim encodings in the finding then give cyclic exclusion of 010 and 111, respectively, with the common at-most-half restriction exactly from hub stability; this holds for n=3 and on hub ties at even n. Marking a zero in minority counts each word z times and marking a one-run start in majority counts it r times, giving the two sums for labelled words, without a rotation quotient. The weighted pair-state traces enumerate exactly these words before the hub weight cutoff. For minority the logarithmic mean density at y=1 is (τ+2)/(τ²+2τ+3)<1/2; a small positive weight tilt exponentially bounds the removed tail, while τ is simple dominant in the unrestricted trace. For majority the displayed cubic at y0=3/4 has Perron root 3/2; implicit differentiation gives L'=1, L''=2/9 and log-scale variance 1/3. The loops 00 and 11 force any equality of twisted spectral radii to have both global phase 1 and exp(iθ)=1, by irreducibility and triangle equality. Thus the trace integral off a neighborhood of 0 is exponentially small; the centered eigenvalue near zero has Gaussian decay with variance 1/3. This proves the local limit for deviations O(log n) and an O(n^-1/2) coefficient bound after exponential untilting uniform in k. Summing from floor(n/2) down contributes y0^((n mod 2)/2)/(1−y0), and the two hub colors give the stated factor 8. Dividing logs by 2n+1 gives the stated distinct entropies. Independent full-state sign-margin computation at n=3–7 reproduced both counts; parity-normalized exact majority counts at n=800,801 were about 0.96233 and 0.95659 (private replay: python3 /workspace/branches/independent_checks.py, helm_check). These are finite diagnostics; uploaded programs were read, not executed.

## originality

PASS

Best-of-knowledge pass for the exact two-rule helm counts and especially the sharply different majority/minority asymptotics including the majority parity factor. The cyclic-word method is classical, but the closest inspected results do not impose the same local and hub constraints together. A named older report and scanned ring paper could not be inspected at the decisive passage level.

## value

PASS

The helm's hub turns a local fixed-state rule into a global density filter on a natural graph family. This filter is exponentially negligible for one rule but changes both the exponential growth and the polynomial/parity scale for the other. Exact counts and the sharp constants quantify a structural difference not captured by the bare existence of exponentially many equilibria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
