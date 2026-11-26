# Independent mathematical audit

## correctness

PASS

Condition on diagonal coordinate pairs (a_v,b_v) with a_v b_v=0. Each arrow equation gives a factor q times [1+(q-1)1_{a_u=b_v=0}], independently, so summation over the selected labelled arrows yields the stated q^(-2n-m) normalization and the three vertex factors 2q-1, q, 1. Bipartite source–sink orientations attain the termwise bound; one incoming and one outgoing selected arrow give strict deficiency in any other orientation. On a path only interior vertices of selected runs can change their factors: a passage gives 1 and a turn gives q. Selecting the two edges at a nonconforming vertex proves strictness, with n=1,2 separately tied. The three-state directed transfer weights are the arrow factor times the multiplicity of the next diagonal state; the alternating two-state weights are the vertex factor times (q-1) when the next edge is selected, with zero boundary indicators. Their quadratic factors give the displayed recurrences and initial values, with the zero eigenvalue in the directed matrix handled by the initial L_3 check. In the spectral comparison, P_U(lambda_L,+)=(q-1)^2(2q-1-lambda_L,+)<0 and P_U(2q-1)<0, giving strict root separation and positive leading amplitudes. Multiplying the path probabilities by q^(2(n+m)) yields the stated pair counts. A hand expansion at n=3,q=2 gives 27+24+4 versus 27+24+8 over 256.

## originality

PASS

The distinct claim is the orientation comparison with equality on bipartite multigraphs and both path extremizers with their exponential gap. The all-quiver count, the count at the source–sink orientation, and the directed bulk Perron root after scaling are covered ingredients, not standalone novelty. The checked prior records do not establish that these scores are strict extrema over competing orientations, the path endpoint normalizations, or the comparison of the two path growth rates.

## value

PASS

For a fixed underlying graph and fixed algebra dimension, the one-sided invariant can still detect how arrows are oriented. The result specifies exactly which orientations maximize it on bipartite multigraphs, and shows for paths that the difference between optimum and pessimum is exponential, not just an isolated finite example. The exact equality conditions and both path endpoint rates are the useful new content; generic annihilator counting is not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
