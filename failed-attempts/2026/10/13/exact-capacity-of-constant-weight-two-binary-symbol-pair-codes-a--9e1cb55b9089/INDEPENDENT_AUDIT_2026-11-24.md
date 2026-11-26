# Independent mathematical audit

## correctness

PASS

For distinct supports P and Q, a cyclic read at i differs exactly when i or i+1 is in T=P symmetric difference Q, so the distance is |T union (T-1)|. Disjoint supports have distance at least four. For supports with one common position, distance three occurs exactly when the two other positions are adjacent on the coordinate cycle. Consequently each neighborhood of the support graph must be cycle-independent, giving degree at most floor(n/2) and the claimed upper bound by summing degrees. The even-length parity graph attains the bound. At odd length 2k+1 with even k, the signed odd steps give circular gaps 2 and 3 and k neighbors. For odd k>=3, the smaller signed odd step set has a gap of 5; one displacement plus or minus k splits it into 2 and 3. A size-k matching of the step-k cycle supplies at most one such displacement per vertex (gcd(k,2k+1)=1), with total edge count (nk-1)/2. At k=1 it supplies a singleton code. Independent direct cyclic-read conflict enumeration at n=3 through 8 gave 1, 4, 5, 9, 10, 16, respectively; method and run record at /workspace/branches/0d375549-ae25-4fba-96cf-732b4ac3954e/record4-evidence.md. The symbolic reduction and constructions, not the finite enumeration, prove all lengths.

## originality

FAIL

The entire maximization is exactly the independence number of the two-token graph of a cycle. De Alba, Carballosa, Leaños and Rivera, Theorem 1.3 (2020), gives the identical formula, including n=3 and explicit extremizers in all parity classes. This is established prior coverage, independent of the unresolved coding papers.

## value

FAIL

The fixed-weight question is natural, but its audited maximum and all-length attainability are established by an exact relabeling of a known conflict graph, and the parity constructions re-express prior extremizers. No further independently useful unknown invariant or classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
