---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Correctness PASS. For a=2/[b(1-b)] and x in (0,1), exact log-odds drift h(F_b(x))-h(x)=-a(x-b). A genuine two-cycle would have x+y=2b and a=integral_-1^1 h'(b+tz)dt >2h'(b)=2/[b(1-b)] by strict convexity, impossible. The classical no-period-two interval theorem gives convergence to 0,b,1, while the map's drift sign excludes endpoint limits from interior starts. Taylor coefficients F_b(b+y)-b=-y+C y³+D y⁴+E y⁵+O(y6), C=2(1-3B)/(3B²), E=2(30B²-20B+3)/(15B⁴), B=b(1-b); F²(b+y)-b=y-2Cy³+(3C²-2E)y⁵+O(y6). For even n=2j, reciprocal square u_j advances 4C+(6C²+4E)/u_j+O(u_j^-3/2). Since C>0, u_j=4Cj+O(log j); summable errors give u_j-4Cj-K log j->finite, K=(6C²+4E)/(4C). The next odd step increments reciprocal square by 2C+o(1), so the same full n-sequence constant exists. Explicit derivative makes exceptional landing preimages countable. Independent exact symbolic Taylor and K tests at b=1/5,3/10,1/2; not extrapolated finite sampling.

## originality

PASS

Originality PASS, with clearly credited covered symmetric slice. Chotibut et al. and Kryzhevich et al. established this replicator family, critical multiplier and global attraction. The published entropic congestion critical theorem and an EOS follow-up already supply a logarithmic coefficient at b=1/2 after exact coordinate conjugacy; that special case is NOT original. The surviving general theorem is for every asymmetric b∈(0,1), with an explicit b-dependent second logarithmic coefficient and shared parity constant. Prior symmetric slice and generic cubic normal-form existence do not by themselves imply this entire rational-function coefficient. No broader full-b result was identified in relevant primary literature or Resultary searches; priority remains best of knowledge.

## value

PASS

Value PASS. A universal exact two-order global relaxation law on the entire physically meaningful interior interval at neutral flip, including a model-dependent positive log correction and full-parity renormalized constant, is a meaningful sharp iteration-speed result. Its all-b rational dependence is a nontrivial quantitative advance over standard local cubic flip and known symmetric special cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
