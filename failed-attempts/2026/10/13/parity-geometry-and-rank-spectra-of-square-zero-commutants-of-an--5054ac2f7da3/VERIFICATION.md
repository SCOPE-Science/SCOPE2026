---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

On R⊕K with R=K[t]/(t^n), direct composition of a commuting map (av+bwt^(n−1),c v(0)+dw) gives the four equations in the source. In their radical lie d and a_0, and then inductively a_s for 2s<n−1, from the degree-2s equations. The remaining ideal bc or u²+bc is radical after every field extension (the latter is primitive and linear in b over K[u,c]), proving the claimed reduced isomorphisms, not just a pointwise equality over a finite field. The odd cone has only the vertex as its geometric singular set even in characteristic two; this is a reduced-locus assertion, not a claim about the Jacobian subscheme. For nonzero a of valuation s with c=0, the image is aR; with c≠0, a(t)tR contributes n−s−1 dimensions and the image of (1,0) adds one, and any extra b-column belongs to a(t)tR in the odd branch s=(n−1)/2. Counting these valuations and the a=0 rank-one maps gives the stated polynomial and totals. An independently written direct matrix check over F2 (n=2..6), F3 and F4 (n=2..4) matched; F2 ambient enumeration at n=2,3 also verified centralizer sizes and ranks. Replay: python3 /workspace/branches/51dcc762-c654-478a-ac7b-7fb3df1b9951/independent_rank_check.py; see full_run.txt in that directory. The finite test is corroboration only. The frozen standalone script was read, not executed.

## originality

FAIL

A distinct indexed finding states the same reduced varieties, with the same field and characteristic scope, and the identical complete rank polynomial for every n≥3. The isolated n=2 boundary addition does not establish a distinct material contribution. This is a comparison with verified existing coverage; it does not establish who first derived the result or that the October 26 record predates the frozen finding.

## value

FAIL

The parity change in geometry and full finite-field rank counts would have structural value if distinct. After the direct catalog overlap, the only additional block size, n=2, has a single nonzero rank and falls out immediately from bc=0. No separate mathematical use or meaningful new boundary phenomenon is established for that remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
