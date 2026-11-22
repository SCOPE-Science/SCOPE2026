# Independent mathematical audit

## correctness

PASS

Theorem is about labelled circular configurations returning after t synchronous Rule-110 steps, not preimage sets or eventual basins, including n=1,2. Verified local map f(a,b,c)=(110>>(4a+2b+c))&1 and the radius-t block overlap/closed-walk bijection, valid even n<=2t by cyclic repetition. Inspected exact code verify_graph.py: it enumerates every 2^(2t+1) candidate edge for t=1..5, finds cyclic strongly connected components, and uses exact Newton trace/determinant coefficients, not numeric recurrence fitting. Component sizes 1; (1,4);(1,9);(1,4);(1,64), giving det(I-zA5)=(1-z)(1-2z^5)(1+z^5-z^10)^2 and log traces. Independently reimplemented graph edges and root closed-walk trace counts for all t=1..5 and n=1..20 (edges 5,17,66,250,1042); every value matches a1=1, a2=a4=1+4[4|n], a3=1+9[9|n], a5=1+5(2^m+2(-1)^m L_m) for n=5m, else 1. For prime period 5 all nonzero returning states are primitive 5, with absences exactly m=1,3 by Lucas recurrence and positive growth thereafter; the formal trace/determinant identity proves all circumferences, not a finite extrapolation.

## originality

PASS

Best-of-knowledge distinct all-circumference time-five fixed-iterate/lucas-zeta theorem; Rule-110 extended de Bruijn phase tools and other one-step spatial zetas are precedents, but not this exact temporal return set.

## value

PASS

Temporal return hierarchies for a universal elementary CA are natural; the sharp first exponentially populated fifth-return class, two exceptional ring lengths and rational zeta supply a complete non-obvious all-size invariant. The exact t<=4 comparison shows a structural jump, not merely a recomputation of a few finite rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
