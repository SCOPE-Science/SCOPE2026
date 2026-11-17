# Independent mathematical audit

## correctness

PASS

The core inequalities reduce to all r+s resource bases because any coalition of value t contains t disjoint bases. Average payoff of a uniform base is (r/a)w_A+(s/b)w_B <=(w_A+w_B)/q=1. Since every base must pay at least one, equality forces zero pay to every nonsaturated type. For q>=2, swapping same-type elements inside a base forces equal pay within each saturated type; for q=1 no within-type equality is needed. Thus a core exists iff a=qr or b=qs. For binomial random X_m the event is the exact union of lower-tail residue X≡0 mod r and upper-tail residue m-X≡0 mod s, with a single possible overlap of O(m^-1/2). Unimodal binomial mass and fixed-modulus block variation yield tail-residue equidistribution O(m^-1/2); the triangular-array CLT yields Phi(-beta/sigma)/r+Phi(beta/sigma)/s. Independently solved all 20 small coalition LPs at quotas (2,3) and a<=6,b<=6; m=12000 binomial numeric probabilities match the predicted window within 1e-4. This corroborates, but does not prove, the full limiting law.

## originality

PASS

The previously published matroid packing core theory gives a general deterministic core decision framework that includes the submitted two-quota saturation test. The final distinct result here is the probability under IID random type allocation and the exact square-root Gaussian supply-mix window combining modulo r/s bottlenecks. Primary general matroid-packing work read does not include the IID random-supply model or congruence-window distribution; Resultary searches for stochastic aliases found no result implying this law. Best-of-knowledge originality pass is only for the finite probability and asymptotic stochastic statements, not the deterministic core algorithm or CLT lemma.

## value

PASS

Randomly supplied resources in complementarity/partition matroid games provide a natural stability question: whether the feasible payoff core survives despite integer quotas. Its nontrivial 1/r versus 1/s survival frequencies and m^-1/2 Gaussian interpolation at a rational supply balance are an informative arithmetic phase transition, not an arbitrary parameter slice or a simple general deterministic core restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
