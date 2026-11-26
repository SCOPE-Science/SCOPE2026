# Independent mathematical audit

## correctness

PASS

In homogeneous coordinates (t,u,v,w) on e1=0, write (X0,...,X4)=(t+u,t+v,t+w,t-u-v-w,t). Then e2=Q and e3=3tQ+C in characteristic five; thus the scheme is globally the projective cone over (Q,C), not just its displayed affine chart. The Gram matrix of Q is nonsingular modulo five, and each of the three cubic factors cuts the conic in two simple rational points; no pair of factors shares a point on the conic. The CI ideal is saturated, so the six reduced points give exactly six reduced projective lines and the vertex is the only singular point. The graded normalization is the product of six k[s], so the Hilbert series (1-t²)(1-t³)/(1-t)³ gives normalization length 5+3+1=9. The normalization of the projective fibre and count 1+6·5=31 follow. Replay: independent_check_1.py independently evaluates the equations on all 625 parameter quadruples modulo five and returns the six listed directions and 31 projective points; the scheme and length conclusions are algebraic, not inferred from finite points. Frozen checker inspected, not run. Frozen attestation, audit and Lean fields record not_performed.

## originality

FAIL

An earlier distinct Resultary record establishes the same characteristic-five scheme and local invariants under the equivalent power-sum presentation; it also gives the conductor. Normalization and the finite point count add only immediate consequences of the same six rational concurrent lines.

## value

FAIL

The bad-fibre structure and local invariants would be worthwhile for this natural model, but those computations are already covered. The point count and normalization are immediate from the prior rational-line description; the frozen record supplies no distinct scientific gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
