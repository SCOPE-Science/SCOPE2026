---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction of exact finite checks

The package contains three standalone C++17 source files and `CHECK.sh`. Run `sh CHECK.sh` in this directory with a C++17-capable `g++`. No external datasets, prior-run binaries, computer algebra systems or third-party libraries are needed. Integer arithmetic is exact.

`cograph_fourier.cpp` examines every labelled graph for each order \(n\in\{4,5,6,7\}\), rejects any induced \(P_4\) by the four-vertex degree pattern \(1,1,2,2\) with exactly three edges, then performs the complete Walsh–Hadamard butterfly transform.

`cograph_recursive.cpp` uses the recursive cograph characterization (disconnect the graph or its complement) rather than induced path matching, and independently repeats the complete Walsh transform. At six vertices it takes the full relabelling orbits of the frequency complements of \(P_4\sqcup2K_1\) and \(C_5\sqcup K_1\) and asserts equality with the set of all even-support zeros.

`cograph_mod32.cpp` uses recursive cograph recognition and counts, exactly once per pair \((T,G)\), each prescribed edge set \(T\) of size at most four within every cograph \(G\) of order seven. It verifies all 7,547 residue tests required for the uniform modulo-32 conclusion.

Expected independent Fourier signatures:

| Order | Cographs | Odd zeros | Extra even zeros | Rank | Least positive magnitude |
|---|---:|---:|---:|---:|---:|
| 4 | 52 | 32 | 0 | 32 | 4 |
| 5 | 472 | 512 | 0 | 512 | 8 |
| 6 | 5504 | 16384 | 252 | 16132 | 16 |
| 7 | 78416 | 1048576 | 0 | 1048576 | 16 |

Expected modular signatures: sizes \(k=0,1,2,3,4\) have respectively \(1,21,210,1330,5985\) edge patterns, each with zero residue-check failures; total cographs \(78416\). The two exceptional six-vertex frequency orbits total \(252\) masks and exactly equal all even-support zeros.

This verifies a finite theorem only, not claims for higher orders. The primary literature comparison is distinct from code execution. Independent mathematical review has not been performed.
