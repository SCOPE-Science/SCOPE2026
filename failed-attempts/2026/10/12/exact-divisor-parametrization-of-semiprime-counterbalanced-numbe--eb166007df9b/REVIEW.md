# Independent mathematical audit

## correctness

PASS

If n=p^2, s(n)=p+1 cannot divide phi(n)=p(p-1). If n=pq with p<q primes, d=p+q+1=s(pq) and phi(pq)=(p-1)(d-p-2)=(p-1)d-(p-1)(p+2). Therefore phi(n)/s(n) is integral iff d|(p-1)(p+2); d>2p+1 enforces q>p and q=d-p-1 prime. This is a correct iff and covers every Omega(n)=2 case. Independently checked representative prime pairs and direct arithmetic for 133 and other database examples; no extrapolation from finite tests.

## originality

FAIL

FAILED: Banks and Luca (2007) already establish s(Pm)|(2 sigma(m)-m)phi(m) for counterbalanced Pm with P>prime factors of m (their equation 2.13). Specializing m=p and P=q gives p+q+1|(p+2)(p-1), the precise assigned divisor condition. The reverse implication is the immediate rewrite of phi(pq) modulo p+q+1; writing q=d-p-1 and d>2p+1 merely reparametrizes the criterion. The claim is thus the elementary special case and reverse algebraic restatement of an earlier theorem, not an independent original classification.

## value

FAIL

FAILED: Although semiprime counterbalanced integers are a natural layer, this proposed exact divisor parametrization has no nontrivial new sieve, count, distribution, obstruction, or sharp case beyond the direct specialization of Banks–Luca equation (2.13) and elementary division. Correctness and naturality alone do not give independent scientific value; examples duplicate OEIS A055940.

The dated certificate retains the supplied scientific assessment, sources and limitations.
