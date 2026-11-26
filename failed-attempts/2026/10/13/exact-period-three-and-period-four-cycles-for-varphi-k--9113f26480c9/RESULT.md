# Exact period-three and period-four cycles for \(\varphi_k\)
## Finding
Let \(P(n)\) be the largest prime divisor of a composite integer \(n\ge 4\), and for \(k\ge1\) define \(\varphi_k(n)=n+k\) when \(n\) is prime and \(\varphi_k(n)=P(n)\) when \(n\) is composite. The exact cycles of lengths three and four are as follows. An exact three-cycle exists if and only if \(k=2^a-1\) for some \(a\ge1\) with \(2^a+1\) prime, and then the unique three-cycle is \((2,2^a+1,2^{a+1})\). Every exact four-cycle is of exactly one of two types: (I) a one-composite cycle, which occurs exactly when \(k=3^a-1\) with \(a\ge1\) and both \(3^a+2\) and \(2\cdot3^a+1\) prime, giving \((3,3^a+2,2\cdot3^a+1,3^{a+1})\); or (II) an alternating prime-composite cycle \((p,p+k,q,q+k)\), where \(p\ne q\) are primes and there is an integer \(t\ge1\) such that \(k=pqt-p-q\), \(pt-1\ge2\), \(qt-1\ge2\), \(P(pt-1)\le q\), and \(P(qt-1)\le p\). Conversely every parameter set satisfying the stated conditions gives the corresponding exact cycle. In particular, Bertrand's postulate gives infinitely many parameters with an exact four-cycle: for any odd prime \(p\), choose a prime \(q\) with \(p<q<2p\), put \(t=1\) and \(k=pq-p-q\).

The period-three criterion is equivalent to saying that the admissible parameters are \(k=F_m-2\) whenever the Fermat number \(F_m=2^{2^m}+1\) is prime. Thus the existence of further period-three parameters beyond those currently produced by known Fermat primes is tied exactly to the Fermat-prime problem.

## Assumptions and scope
The domain is the positive integers greater than \(1\), and \(k\) is a positive integer. For a composite integer \(n\), \(P(n)\) denotes its largest prime divisor. A cycle has exact period \(r\) when it contains \(r\) distinct states before returning. The result classifies only exact periods \(3\) and \(4\); it does not claim a classification of longer cycles or resolve the existence of every possible period.

## Proof
A composite state is always followed by a prime state, because \(P(n)\) is prime. Hence no cycle contains two consecutive composite states.

For an exact three-cycle, after rotation the only possible primality pattern is prime, prime, composite. Write the states as \(p\), \(p+k\), and \(p+2k\). The last state maps back to \(p\), so \(p\mid p+2k\), hence \(p\mid 2k\). Since \(p+k\) is prime, \(p
mid k\); therefore \(p=2\). Thus \(k\) is odd. The condition \(P(2+2k)=2\) forces \(2(k+1)\) to be a power of \(2\), so \(k+1=2^a\). The intermediate state is prime exactly when \(2^a+1\) is prime. This gives the asserted cycle, and the same implications run backward for the converse.

For an exact four-cycle, there are either one or two composite states.

If there is one composite state, rotate the cycle to \(p,p+k,p+2k,p+3k\), with the first three states prime and the last composite. Since the last state maps to \(p\), one has \(p\mid p+3k\), hence \(p\mid3k\). Again \(p+k\) prime implies \(p
mid k\), so \(p=3\). Because \(3+k\) is a prime larger than \(3\), \(k\) is even. Now \(P(3+3k)=3\) means every prime factor of \(k+1\) is at most \(3\); since \(k+1\) is odd, \(k+1=3^a\). The two intermediate primality conditions are precisely that \(3^a+2\) and \(2\cdot3^a+1\) are prime. This proves type (I) and its converse.

If there are two composite states, rotate the cycle to \(p,C,q,D\), where \(p
e q\) are prime, \(C=p+k\), \(D=q+k\), \(P(C)=q\), and \(P(D)=p\). Put \(A=C/q\) and \(B=D/p\). Since \(C,D\) are composite, \(A,B\ge2\). The two expressions for \(k\) give
\[q(A+1)=p(B+1).\]
Because \(p\) and \(q\) are distinct primes, there is an integer \(t\ge1\) with \(A+1=pt\) and \(B+1=qt\). Therefore
\[k=pqt-p-q,\qquad A=pt-1,\qquad B=qt-1.\]
The largest-prime-divisor requirements are exactly \(P(pt-1)\le q\) and \(P(qt-1)\le p\). Conversely these conditions imply \(P(q(pt-1))=q\) and \(P(p(qt-1))=p\), hence give the asserted exact four-cycle.

For the infinite family, let \(p\) be any odd prime and choose a prime \(q\) with \(p<q<2p\) by Bertrand's postulate. With \(t=1\), one has \(P(p-1)<p<q\) and \(P(q-1)\le(q-1)/2<p\), so type (II) applies. The resulting \(k=(p-1)(q-1)-1\) is positive and unbounded as \(p\) grows.

## Verification
The accompanying verifier independently enumerates all cycles reached from every prime at most \(k^2/2\) for each \(1\le k\le180\), using the published small-prime entry bound to cover every cycle in that parameter range. It compares every exact three-cycle against the closed classification and checks every exact four-cycle against one of the two classified forms. It also checks \(1502\) independently generated alternating parameter tuples and \(24\) Bertrand-family instances. The run returned `VERIFY_OK` after \(123838\) starting-prime orbit checks, seeing \(3\) exact three-cycles and \(39\) exact four-cycles. These finite checks supplement, rather than replace, the symbolic proof.

## Relationship to prior work
Das introduced the map, proved eventual periodicity, bounded the number of loops for each fixed \(k\), displayed examples of distinct periods, and ended with the open issue of realizing every period. The paper does not classify the low-period cycles. Dubickas later proved stronger boundedness statements for a wider class of prime-step/composite-contraction recurrences, recovering periodicity of the same largest-prime-divisor map as a special case, but does not derive the exact period-three or period-four parameter conditions above. Targeted searches found no prior statement linking all exact three-cycles to Fermat primes or parameterizing all exact four-cycles by the two cases above.

## Limitations
The result does not imply that there are infinitely many exact three-cycle parameters, because that would require infinitely many Fermat primes. It does not classify periods \(5\) and above. The period-four type-(II) parameterization may describe the same directed cycle after swapping \(p\) and \(q\); this is a representation symmetry, not an additional cycle.

## References
1. A. Das, “A Family of Iterated Maps on Natural Numbers,” arXiv:2312.06629, first public version 11 December 2023; Experimental Mathematics 33 (2024), 776–780, DOI 10.1080/10586458.2023.2294184.
2. A. Dubickas, “A Class of Bounded Iterative Sequences of Integers,” Axioms 13 (2024), 107, DOI 10.3390/axioms13020107.
