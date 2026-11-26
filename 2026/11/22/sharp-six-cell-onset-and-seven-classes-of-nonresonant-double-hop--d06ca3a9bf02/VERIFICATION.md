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

Every row sums to two, so the eigenvalue 2 excludes orders below five by degree. At five, division by the monic integer factor z-2 leaves an integer even quartic z^4+Sz^2+P with S,P>0; S>=2 follows from P>=1. Thus tr(A^2)=4-2S<=0, inconsistent with tr(A^2)>=sum of squared diagonal entries>=tr(A)=2. At six the extra real eigenvalue r=tr(A)-2 is an integer in [-2,2]. Division again gives integer S,P, and distinct squared frequencies imply S^2>4P and S>=3. For r=-1,0,1,2, the upper bound 4+r^2-6 on tr(A^2) is strictly below 2+r; r=-2 is forced. The trace gives zero loops, and nonnegative tr(A^2) forces S<=4. These restrictions precede the census and do not presuppose strong connectivity or a bipartition. Independent replay: python3 /workspace/branches/c0dfdede-93b8-4be8-9137-996d62a6a60b/independent_census.py (NumPy; full output in full_census.txt). It tests all 15^6 loop-free input multisets using exact integer trace identities; checks strong connectivity, directed period, and all 720 vertex relabelings of the accepted matrices. Only (S,P)=(3,1),(3,2),(4,2) occur, with labeled counts 720,3600,720 and class counts 1,5,1. All accepted matrices are strongly connected of period two (thus bipartite), and each simultaneous-relabelling orbit has size 720. Solving for the two positive squared frequencies gives the three displayed irrational ratios. In the displayed witness the upper and lower off-diagonal blocks have product with characteristic polynomial (z-4)(z+1)(z+2), verifying the witness quartic despite the row-separator typesetting issue. The admissible Jacobian is mu I+bA at the zero equilibrium, so both imaginary pairs cross at mu=0 while the other two eigenvalues are ±2b there. This verifies only a linear spectral coincidence, not nonlinear double-Hopf dynamics.

## originality

PASS

The exact onset and exhaustive seven-class census for the distinct nonresonant double-imaginary condition are the supported contribution. Available comparisons identify closely related zero-Hopf classifications and general coupled-cell spectral tools, but not an implication establishing this onset and census. No priority within the same-day records is inferred.

## value

PASS

The first size of a simultaneous nonresonant crossing is a natural question in the homogeneous valency-two family, and dimension counting alone gives only five as a lower bound. Integral positivity rules out that apparent boundary. The precise smallest-network classification supplies a finite, small family for further coupled-cell analysis and shows that all minimal examples force an additional structural pattern (strong connectivity and period two). Neither arbitrary spectral coincidences nor a nonlinear bifurcation claim is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
