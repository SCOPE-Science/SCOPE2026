# Independent mathematical audit

## correctness

PASS

For a nodal step the Bernstein coefficients of (2B_n-B_n^2)s_j are 2*1_{k>=j}-q_{j,k}. The binomial kernel has derivative n*b_{n-1,j-1}(p)>0 on 0<p<1 when summed over the upper tail, so all nodal increments Delta q are strictly positive. They are also strictly less than 1 because n>=2, all n increments are positive, and they sum to 1. The consecutive differences of the response coefficients are therefore strictly negative except at k=j-1. After x=t/(1+t) and division by the common positive factor, the derivative has respectively two or one Descartes sign changes. For the interior jump the two endpoint derivative signs are negative but the integral of the derivative is 1, forcing two interior crossings and exhausting the bound with simple roots. Hence the strict minimum is below zero and the strict maximum above one. For the boundary jump the opposite endpoint signs force one simple root, giving a maximum above one at j=1 and by reflection a minimum below zero at j=n. Telescoping the nodal differences bounds the seminorm by the largest step variation times the input variation, and a pointwise real step attains equality. Summing the monotone pieces gives 2*(max-min)-1, including both endpoint cases. In degree two the first step has coefficients (0,5/4,1), maximum 25/24 at 5/6, hence K_2=13/12. For j=1 at x=u/n the response limit is 1-2 exp(-u)+exp(-a*u), a=1-exp(-1). The rescaled derivative coefficients tend for fixed k to 2*1_{k=0}-a*exp(-k); the n and n-1 binomial laws tend to Poisson uniformly on bounded u-intervals, since the finite weights converge uniformly and the tails for k>=M are bounded by sup(u)/M. The limiting derivative has its only crossing at u_*=e log(2/a), so bracketing and the finite-degree unique root give nx_n->u_* and the exact overshoot exp(-1)*(a/2)^(e-1). This gives a lower bound for liminf K_n, not the global asymptotic. Independent replay: python3 -B /workspace/branches/independent_replay.py 5. Direct polynomial composition gives g_{3,2}=(-7x+48x^2-32x^3)/9 and its two exact critical points. An independent binomial-sum calculation at n=800 gives (nx_n,Var(g))=(3.1258408620,1.1016371315) versus limiting (3.1309776982,1.1016715060); finite corroboration only. Frozen check_boolean.py was read, not executed.

## originality

PASS

The operator and standard Bernstein sign/step methods are not new. The distinct increment is the exact critical-point classification for the signed second Boolean sum, yielding its sharp unrestricted BV coefficient, and the first-step boundary limit. The closest exact BV results use different operators, boundary constraints or defects. The same-operator approximation results inspected do not supply the asserted jump profile or boundary limit. Priority is bounded by the sources actually read, especially in the older literature.

## value

PASS

The signed second Boolean sum is a classical acceleration of a positive operator; its exact multiplier on variation is a natural stability invariant for discontinuous data. Knowing the endpoints and a triangle estimate on the two Bernstein terms would not give the exact extrema and norm. The explicit Poisson limit shows a variation cost that survives mesh refinement for jumps on the boundary scale and gives its location, beyond a low-degree instability example. It makes no claim that the boundary jump maximizes the global asymptotic norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
