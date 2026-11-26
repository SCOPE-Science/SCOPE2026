# Independent mathematical audit

## correctness

PASS

An increasing interval homeomorphism has monotone or constant forward orbits, each converging to a singleton fixed point. At a limit point of K, fixed-point secants give multiplier 1, including at ambient endpoints with one-sided derivatives. At an isolated p in K, a multiplier above 1 excludes every converging orbit except p itself; K minus p is still closed and has full basin, contradicting minimality. For sufficiency the two gap cubics have endpoint slopes (-A,R) and (R,-B) by differentiating s(1-s) and evaluating at 0 and 1, where A=-log d(a), B=-log d(b), R=log rho_J. Their signs are strict on the open pieces even when A or B is zero. The factor L cancels under differentiation, so for example each slope magnitude is bounded by 2(A+B+R), independently of either split length. At p in K', endpoints of any sequence of shrinking adjacent gaps approaching p converge to p, and A,B,R tend to zero. Finitely many nonshrinking or outer gaps can approach p only at endpoints with zero prescribed slope. For x outside K near p, compare with its gap endpoint between x and p; the mean-value bound is o(|x-p|). This gives derivative zero and continuous gluing at p; isolated points glue by the prescribed common slope. The compact C1 field vanishes at 0 and 1; uniqueness gives a complete interval flow, and its equilibrium derivative is exp(v'(q)). Only the countably many added repellers have limits outside K. Every ambient neighborhood of a point in K either contains a positive-measure subset of its interior or contains an endpoint in K of a bounded or outer gap (take an adjacent endpoint between a nearby point outside K and the given point). Those endpoints attract a positive-length interval; thus each neighborhood of each point of K is required in any closed full-basin set. Finally, from any sequence of distinct shrinking gaps whose repeller derivatives stay away from 1, compactness gives a limit of their repellers in K', a contradiction to continuity. K=[0,1], singleton K and all endpoint conventions are included. The finite script was inspected, not run; its two sign evaluations per mesh location are converted to float, despite the exact-sign description, so analytically verified signs, not that label, support the theorem.

## originality

PASS

The supported increment is the necessary-and-sufficient multiplier profile with arbitrary, independently specified gap split points and compatible repeller multipliers in an autonomous C1 flow, not arbitrary closed-attractor realizability alone. The closest actual indexed statements concern topological realization or are self-matches. Known flow embeddings and unconstrained first-jet extension do not by themselves enforce the signed gap dynamics. Primary passages of the cited preprint could not be retrieved; this decision is about the distinct supported assertion, not a priority certificate.

## value

PASS

The classification determines which attraction rates can be prescribed while independently placing every bounded-gap basin boundary, including arbitrarily asymmetric splits and infinitely many gaps. The necessary decay criterion identifies exactly the obstruction when arbitrarily short gaps accumulate; a topological existence statement supplies neither this obstruction nor a quantitative derivative bound independent of gap geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
