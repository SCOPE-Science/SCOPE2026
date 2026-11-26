# Independent mathematical audit

## correctness

PASS

After the first choice i, staying in mode i maximizes all future costs; any different mode sends the state to zero. The geometric sum including the time-zero cost gives J. Any valid envelope covers the value 1+beta on each coordinate vector using some piece. Pigeonholing gives r coordinates covered by one piece; on their normalized sign cube the mean of that piece is at least 1+beta, while J is constant at 1+beta/r. This proves the lower bound even with arbitrary off-diagonal entries. Balanced blocks yield P_g=I+beta D_g and an upper bound because each coordinate lies in some block. With largest squared-coordinate fraction t, the largest block fraction is at most min(1,rt); the ratio bound increases to t=1/r and then decreases (the r=1 bound is one). Equal magnitudes on a largest block attain it. The source-block-to-every-target edges of label i give co-completeness, hence path-completeness by constructing paths backwards; the Bellman inequalities follow from rho^2(1+beta)=beta and support on coordinate i. This covers m=1 and m=n and the limit rho tending to one within scope. An independent hand check at n=3,m=2,rho=1/2 gives 8/7 on (1,0,1) with blocks {1,3},{2}.

## originality

PASS

Credit the general co-complete max-quadratic Bellman upper-bound construction to the prior framework. The distinct claim supported here is the sharp piece-budget frontier for this system, including a lower bound on the entire pointwise-valid envelope class and equality within the graph-restricted class. No earlier equivalent frontier was identified in the examined statements; this is not a priority certificate.

## value

PASS

The example is a fully analytic benchmark for a motivated complexity-versus-conservatism question in switched Bellman certificates. The ceiling produces exact piece-budget thresholds, and equality between the implementable co-complete construction and the unrestricted lower bound identifies the lost accuracy as intrinsic to the number of pieces, not an artifact of graph restrictions. The signed witnesses explain why allowing dense quadratic matrices cannot improve the benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
