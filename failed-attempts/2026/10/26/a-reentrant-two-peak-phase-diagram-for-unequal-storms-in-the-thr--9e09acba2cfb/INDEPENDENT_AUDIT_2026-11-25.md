# Independent mathematical audit

## correctness

PASS

Three cascaded unit-rate linear stages have impulse response x^2 exp(-x)/2 on x>=0, and the dimensional outlet is V1/K times the normalized superposition. The derivative is continuous at the second arrival since h'(0)=0. For d<2 the pre-arrival derivative is positive and the post-arrival, after factoring out exp(-x)/2, is a downward quadratic positive at d, with exactly one subsequent sign reversal. At d=2 the post-arrival derivative has the sign of z[2(M-1)-(1+M)z] for z=x-d>0 and M=m exp(d): the unique maximum is at arrival if M<=1 and strictly later if M>1. For d>2 the first maximum is at 2 and the derivative is negative at arrival and after d+2. For d<x<d+2 put y=1-(x-d); the derivative is positive iff 1+M>d(d-2y)/(1-y^2). The right side diverges at both endpoints, and its derivative has sign -1+dy-y^2, so its unique minimum is at y0=(d-sqrt(d^2-4))/2, with value d/y0=1+1/y0^2. This derives the stated strict threshold, and equality only touches zero, giving no extra maximum. The quadratic has exactly two roots after arrival above the threshold, of which the later is a strict maximum. The logarithmic derivative of C is 2/sqrt(d^2-4)-1, with unique maximum of C at 2 sqrt(2), and the limits are e^-2 at the left and zero at infinity. These facts give the asserted reentrance, including both fold equalities. The three example inequalities hold using the recorded explicit elementary bounds; the C values are also approximately 0.229891, 0.341246 and 0.154679.

## originality

FAIL

A distinct indexed finding exactly covers the strict peak-count criterion, its fold equality, and the reentrant sequence in the same shifted Erlang-3 model. The matching record is dated November 2, later than the frozen record. This is a finding of exact overlapping content in the comparison corpus, not a finding that the frozen record lacked historical priority or was derived from that record. No distinct residual theorem remains here. The older sources inspected do not by themselves establish that exact coverage.

## value

PASS

As a mathematical statement this is an informative, complete boundary for a natural impulse model. In particular, the nonmonotone threshold shows that more separation can remove a second strict peak before restoring it. This is not a sample observation or a routine single-parameter evaluation. It does not, however, provide an increment over the distinct indexed result covering the same diagram, so no repair to a new claim is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
