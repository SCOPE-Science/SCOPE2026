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

At mass |E| and with each vertex firing exactly once in its least period, summing its firing-threshold inequalities over vertices forces each graph edge's endpoints to have distinct firing rounds and forces the unique initial load x(v)=d(v)-#neighbors with earlier firing times. A predecessor-phase neighbor is required to prevent early firings, including the last-to-first wrap. Conversely a surjective phase assignment satisfying the independent firing round and predecessor-neighbor conditions reconstructs a periodic single-pass state uniquely. On K_{n_i} each round belongs to one part, and proper cyclic part words plus ordered nonempty vertex partitions yield trace(B(z)^T) coefficients times products k_i! S(n_i,k_i). Capacity k_i<=floor(T/2), T<=N and T<=2(N-M) are necessary; choose k_i<=min(n_i,floor(T/2)) for every T in [r,min(N,2(N-M))], and Dirac's theorem on selected complete multipartite graph gives Hamilton cyclic label word, proving sufficiency. Independent full nonnegative-chip state evolution agrees exactly with independent formula for (1,1,1), (2,2,1), (2,2,2), (3,2,1), including C_{K2,2,1}(5)=40 and counts at all feasible periods. Finite checks corroborate the general phase and no-gap proofs, not substitute for them.

## originality

PASS

Best-of-knowledge PASS specifically for all-period labelled state counts by Stirling-weighted proper cyclic part words and sharp no-gap interval for r>=3. Goles–Prisner already proves orientation/chip correspondence at mass |E|, Jiang studies attainable periods, and the published complete-bipartite r=2 formula has only even alternating periods. Those precedents cover methods/special cases, not the r>=3 exact labelled census and odd periods.

## value

PASS

Exact temporal-orbit census for a natural critical-energy, single-pass sector of multipartite parallel chip firing is a substantive combinatorial invariant: it identifies all possible least periods without gaps, counts each labelled state rather than a mere witness, and explains odd-period behavior absent in the bipartite special case. The 40 period-five states of K2,2,1 is a natural motivating benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
