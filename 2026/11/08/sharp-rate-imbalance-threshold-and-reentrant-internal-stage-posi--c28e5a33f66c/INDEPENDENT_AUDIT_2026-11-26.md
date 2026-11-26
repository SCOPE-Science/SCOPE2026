# Independent mathematical audit

## correctness

PASS

For the row-vector generator, Q=−(a+b)(I−Π) with each row of Π equal to (b,a)/(a+b). On the stationary component the stages and endpoint are the identity; on the other component solve the two scalar stage equations. Their factors are (1±√3 z/6)/D, D=1+z/2+z²/12, and the endpoint factor is 1−z/D. A map with factor g has nonnegative entries exactly for −1/r≤g≤1, since off-diagonals are π_j(1−g) and the smaller diagonal is π_min+(1−π_min)g when g<1. The endpoint numerator ((z−3)²+3)/12 and both strict bounds for stage 1 settle those claims. Independently put y=z/(2√3): the stage-2 factor is (1−y)/(1+√3 y+y²), with derivative numerator y²−2y−(1+√3). Its unique minimum occurs at y*=1+√(2+√3) and is −1/(2y*+√3); this yields the stated r*. The factor is <1 for y>0 and returns to zero from below; the horizontal line −1/r gives one tangency at r*, two positive crossings for r>r*, and strict positivity outside the closed failure endpoints. At a crossing exactly one diagonal is zero since r*>1. With (a,b,h)=(9,1,1), the endpoint first row is (16,27)/43; the stage-2 first component at (99,1)/100 is (697−445√3)/4300<0. The packaged checker and recorded output were inspected but not executed. Its 50 block solves are exact comparisons for the first basis input; their sampled sign tests use numerical tolerances. The analytic check, not that sample, establishes all claims.

## originality

PASS

Credit the standard Gauss tableau, rank-one stochastic-mode criterion, familiar Padé endpoint, and known possibility of negative internal stages. The surviving distinct claim is the sharp weighted two-state classification for the actual Gauss collocation stages, including the isolated zero and exact reentrant stage-2 failure while the endpoint remains positive. None of the statement-level comparisons supplies this stage boundary or covers it by a stronger result.

## value

PASS

Two states are the smallest nontrivial Markov setting and a natural controlled test of whether a positivity-preserving update certifies admissible intermediate probabilities. It does not: the exact rate contrast and two scaled step boundaries identify when endpoint monitoring misses failure and when larger steps restore positivity. This is an actionable sharp stage classification and an exact interior-input witness for a standard high-order scheme, not novelty assigned to a projector identity or the usual stability function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
