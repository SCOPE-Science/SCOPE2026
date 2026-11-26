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

The positive unit exchange on the three-excitation block is the symmetric adjacency on 560 three-subsets: each accepted edge move flips exactly one occupied bit and one empty bit, uniquely. Independently generated both Cayley bases on Z4² and lifted undirected edges by this bit transposition; checked degree six, two common base neighbors for each distinct pair, four-clique counts 8 and 0, and symmetric zero-diagonal token adjacency with 8736 directed entries. For each root computed rows of powers only up to H^4 and used the Frobenius product of H^k with H^(k-1) and itself for traces at 2k-1 and 2k. This exhaustive arbitrary-precision integer replay returns the shared traces [560,0,8736,17472,407040,2680320,39058944,437090304] and eighth traces 6117992448 (rook), 6115799040 (Shrikhande). Their difference is 2193408. Dividing by 560 times 8! gives exactly 17/175. Finite-dimensional exponentiation gives the entire series and analytic O(z^9) remainder; (-1)^8=(-i)^8=1, so both specified substitutions have the same leading distinguishing order and coefficient.

## originality

PASS

The three-token sector is a known symmetric cube, and qualitative spectral distinction in that sector is not novel. The claim that survives is the first differing normalized trace coefficient being exactly 17/175 at order eight. Neither the strongest inspected symmetric-power computations nor the earlier same-pair Ising expansion determine that coefficient or the seven preceding cancellations for this Hamiltonian.

## value

PASS

The rook/Shrikhande pair is the canonical strongly regular comparison, and the symmetric-cube block is a natural common setting for its known spectral distinction. The first unequal trace fixes the earliest distinguishability for the normalized high-temperature and short-time trace observables, including seven nontrivial-order tests of cancellation through order seven with order zero fixed by dimension. The exact order and coefficient answer a sharper question than the known existence of separation, and the matched Ising order does not make the quantum conclusion redundant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
