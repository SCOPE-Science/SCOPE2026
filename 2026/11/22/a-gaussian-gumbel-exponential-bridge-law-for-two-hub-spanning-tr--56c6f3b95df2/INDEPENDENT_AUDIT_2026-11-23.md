# Independent mathematical audit

## correctness

PASS

A spanning tree must have one incidence at each peripheral and q+1 edges total, so exactly one double-incidence peripheral connects the hubs. Fixing it and optimizing the others proves the support identity for all weights, ties included. Any two edges lie on a common 4-cycle (q>=2), so tree exchanges span the sum-zero edge-coordinate directions and the dimension is 2q-1. The joint marked density follows by selecting the winning pair, ordering its two entries and requiring all other minima to lie below t; integrating the mark gives the derivative of (1-Q(t)^2)^q, with Q the normal survival. The mark tail given the bottleneck is Q(t+z)/Q(t). Mills ratios give a_q~1/(2b_q), a squared-survival exponent -x for t=b_q+a_q x and the mark exponent -u for z=u/b_q, uniformly on compact bottleneck windows. For any fixed such window L>t entails both weights exceed t; the truncated |U|^k moment removed is at most twice Q(t) times the corresponding truncated normal moment, O(b_q^k/q). Given the chosen pair and value, the q-1 nonwinners are independent conditioned on L<=t. Their aggregate normalized mean error is O(b_q/sqrt(q)), variance tends to one and their third moments are bounded uniformly; the winner contributes o_P(1). Uniform conditional characteristic-function convergence on compact mark windows and tightness give three-way independence. For uniform integrability of the normalized bottleneck, the right tail is at most exp(-2b_q a_q x) using the normal hazard >=t for t>=b_q; for 0<=t=b_q-a_q x<=b_q, the squared survival ratio is at least exp(b_q a_q x), yielding a double-exponential left bound. Below t=0, the remaining integrated left tail is bounded by (3/4)^(q-1) times the finite integral of F(t)=1-Q(t)^2 over t<=0, divided by a_q. These estimates justify E B_q=b_q+gamma a_q+o(a_q); solving Q(b_q)=q^(-1/2) gives the stated log log and log(2pi) factors. The width is Gaussian opposing support, not normalized spherical width.

## originality

PASS

The exact support can be viewed as a maximum-weight tree identity or a union of fixed-bridge cubes. Standard optimization and order-statistic theorems supply ingredients, not a previously evaluated two-hub marked law plus width expansion in the material inspected. This does not claim novelty for finding a maximum spanning tree, for the unmarked Gumbel theorem, or for the tree count in isolation.

## value

PASS

The simplest complete bipartite graphs beyond stars separate the extensive contribution of leaf choices from a mandatory inter-hub bridge. The explicit width correction measures the price of that bridge under Gaussian support, and the joint independent limit quantifies three distinct fluctuations for the same optimizing tree. This is more informative than the standard tree count or applying a scalar Gaussian-maxima approximation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
