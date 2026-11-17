# Independent mathematical audit

## correctness

PASS

The endpoint reachability Gramian for a single coordinate activation at backward time s is diagonal with w_i=integral_{sigma=i} exp(-2lambda_i s)ds; worst Euclidean target energy is 1/min_i w_i when each positive, infinite otherwise. Monotone primitive F_lambda ensures unique ordered cuts having identical integrals m. The dual p_i>0 chosen at adjacent switch crossings makes g_i(s)=p_i exp(-2lambda_i s) the unique upper envelope on its intended interval (all nonneighbor crossings are convex combinations of intervening cuts). For every other measurable schedule, min_i w_i<=sum p_i w_i<=integral max_i g_i=sum p_i m=m. Equality in the strict envelope except finite crossings forces the same schedule almost everywhere. Independent double-precision bisection for n=2,(lambda1,lambda2,T)=(2,1,1) gave cut 0.3397459832093852,m=0.18576957648171977,1/m=5.383012756657723 and correctly ordered dual envelope on 1000 points. Numerical tests only support the exact global proof.

## originality

PASS

Best-of-knowledge: existing discrete-time time-varying sparse actuator design papers establish problem motivation and inverse Gramian objectives, but do not state the exact continuous-time ordered n-interval unique schedule under pointwise one-channel support. The dual weighted upper envelope is elementary minimax control, which is not credited as a new general framework. A stronger unindexed optimal-design/bang-bang rearrangement theorem could imply this specialization; explicitly retained as risk.

## value

PASS

The exact unique time allocation among an uncountable class of measurable one-actuator schedules solves a natural worst-case controllability-energy design problem. The scalar bisection and strict one-pass ordered switching rule replace generic high-dimensional combinatorial scheduling and offer an analytically sharp benchmark for diagonal control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
