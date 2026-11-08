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

# Verification evidence and limits

The standalone `verify.py` uses Python 3 standard library only. Invoke `python3 verify.py > observed.txt` and compare `observed.txt` with `verify_output.txt`. Its output ends in `ALL_VERIFY_OK` and `ALL_ACTIONS_OK`. The reported integral cycle generators are assembled explicitly as the eight oriented triangles in a join of three differences of vertices. For each cycle the verifier computes every signed edge coefficient and asserts its cancellation. It checks distinct unit-pivot triangles and compares the number of generators with the proposed rank. The general spanning theorem relies on the symbolic join-chain argument in `RESULT.md`, not on these finite certificates alone.

The program enumerates every face by its actual pairwise disjoint color types for seven size profiles. For small total color-size products, it independently computes ranks of the signed two-boundary modulo 2 and 3. The larger profile \((2,3,2,2,2,2)\) has all faces and 675 exhibited integral top cycles checked, but the full modular rank is not recomputed there. It also explicitly applies within-class permutations to oriented simplices and cycle bases, obtaining the full alternating chain trace and induced top-homology trace for all six single-class flips and the three-cycle where available. It checks the expected degree-one trace by the Euler–Poincaré relation. No computation purports to certify an infinite parameter range.

The topological identification and integral equivariance are justified separately in `RESULT.md`. Björner–Wachs–Welker's existing inflation theorem supplies the contextual nonequivariant wedge type, which is not part of the new claimed discovery. External independent mathematical validation remains unperformed.
