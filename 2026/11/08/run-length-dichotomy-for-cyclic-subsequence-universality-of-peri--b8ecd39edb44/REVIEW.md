# Independent mathematical audit

## correctness

PASS

For q>=3 distinct cyclic runs and k>=1, greedy complete arches exactly equal scattered-subsequence universality. From a phase in run j, the first completing run is j+q-1 and subsequent arch endpoints advance q-1 for a nonsingleton endpoint or q for a singleton endpoint. Counting endpoint indices within the half-open k-period factor gives k+floor((k-1+delta)/(q-1)) when all runs are nonsingleton. In the singleton case the bounded deficiency E_r=rq-(J_r-j) lies in [1,q], with equality at q only for a run-start boundary, excluding a (k+1)th arch: the index is k in every phase. All maximizing-phase counts follow; q>=3, positive lengths and position rotations are essential. Independently scanned 16,200 (word, phase, repetition) cases for q=3,4,5 with run lengths 1..3 and k=1..5, matching the formulas; this finite check corroborates the full recurrence proof.

## originality

PASS

Best-of-knowledge: explicit singleton obstruction, no-transient q-1 floor law, and full phase maximizing census are not directly supplied by inspected general circular-universality bounds or power algorithms.

## value

PASS

The cyclic run-word family is a natural family of unbounded length and alphabet size. An exact singleton-run obstruction, a sharp q-1 staircase and a count of all optimal position cuts are structurally useful, not a numerical variant of a general algorithm. A future analysis of power universality and circular cuts can directly use these formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
