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

For a smooth plane quartic, the restriction of cubics is the complete |3K|; writing a bitangent contact divisor as θ₀+v converts the sum of six such divisors to 3K plus their binary XOR. Similarly a conic through three bitangents' contact pairs exists precisely when the residual theta class θ₀+u+v+w is effective. A degree-two theta class on a nonhyperelliptic genus-three curve is effective precisely when odd, giving the stated triad test. I independently enumerated all six-subsets and compared class bitmasks directly for intersection size four, rather than using the frozen checker/tetrad index. The affine theta transvections, computed by choosing v+w whenever it is odd, give full orbits of sizes 1008 and 5040 and preserve the edge test. Exact factor-by-factor application gives P(G)e₀=0, hence P(G)=0 by transitivity. The seven traces were independently reproduced, from 1008 through 5215177324964880; rational elimination gives (105,280,168,330,1,35,27). The nonsquare discriminants 4329 and 3465 force equal multiplicities within each conjugate pair. Sorting the real roots gives the claimed positive least, simple largest and second-largest eigenvalues; direct degree checks give 45, 9, and 45360 edges, so division by 405 gives the asserted gap (0.5754762338135238). Replay `python /workspace/branches/audit_hexad_reproduction.py`. The supplied certificate and verification note were inspected, not executed, and the note is self-review rather than independent attestation.

## originality

PASS

The classification and graph are prior art. The exact Gram characteristic polynomial, injectivity and two-step spectral gap are distinct from the inspected prior finite geometry, orbit tables and intersection rows. No exact prior evaluation was found in the checked sources.

## value

PASS

This is a naturally defined finite incidence operator in classical quartic geometry. The exact least singular value certifies stable reconstruction from the opposite class, while the second eigenvalue quantifies convergence of the canonical two-step walk. Neither lower-spectrum fact is implied by connectedness, and both are concrete uses for the exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
