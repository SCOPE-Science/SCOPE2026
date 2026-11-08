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

# Verification

The complex rank counts were checked by exact coefficient arithmetic in the cyclotomic ring of the primitive sixteenth root of unity, with determinants of every required nested minor computed by signed permutation expansion. A second checker evaluates the matrix over the eight primitive sixteenth roots in \(\mathbb F_{97}\) and takes the maximum finite-field rank. The coefficient bound \(4!<97\) proves that this maximum equals the complex rank. A third checker loops over every unordered row and column four-set directly instead of relying on translation orbits. The three procedures agreed on every total in the accompanying rank-count table.

Checked groups in order: \(C_{16}\), \(C_8\times C_2\), \(C_4^2\), \(C_4\times C_2^2\), \(C_2^4\). The respective counts of row translation-orbit representatives were 116, 120, 122, 128, and 140. In every case, the sum of rank counts was \(3{,}312{,}400\), the complete number of four-set pairs.

Reproduction: compile each `.cpp` file with a standard C++17 compiler, for example `g++ -O3 -std=c++17 checks/fourier16_exact.cpp -o fourier16_exact` followed by `./fourier16_exact`. All computations use integer arithmetic; no third-party libraries or external data are required. Compare each printed group and four rank counts to `data/rank_counts.tsv`.

Scientific limits: The certificate applies only to rank-one through rank-four restrictions of the five abelian character tables of order sixteen. It does not certify any external historical novelty priority, a higher-order pattern, or independent mathematical validation.
