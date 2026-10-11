---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For two identical repulsive delta interactions, simplicity and positivity of the one-dimensional ground state force reflection symmetry through the two sites, hence equal positive endpoint amplitudes on both complementary arcs. Solving \(-u''=k^2u\) on an arc of length \(L\) with equal endpoint value gives the cosine profile and positivity forces \(0<kL<\pi\). The two delta jumps combine to \(lpha=k[\tan(ka/2)+\tan(kb/2)]\), which is strictly increasing in \(k\) on the positive branch. Strict convexity of \(\tan\) and \(a+b=2\pi\) then gives the unique antipodal maximizer for every \(lpha>0\). This is an analytic proof, not an inference from the finite transfer-matrix tests.

## originality

FAIL

The final claim is strictly covered by another frozen SCOPE result in the same inventory: the assigned all-\(N\) equidistant theorem proves Exner's repulsive-loop conjecture for every \(N\ge2\) and every positive coupling. Setting \(N=2\) makes equal spacing exactly antipodal placement, so the present claim is an immediate special case. Exner 2019 itself leaves the all-coupling statement conjectural, but that does not restore originality once the broader current theorem is present.

## value

FAIL

As a standalone scientific claim, the N=2 optimizer no longer fills a mathematical gap once the same frozen corpus contains a proof for every \(N\ge2\). The shorter two-site symmetry argument may be pedagogically pleasant, but it adds no new classification, boundary, invariant or parameter range beyond the broader theorem, so it does not clear the value bar as a separate result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
