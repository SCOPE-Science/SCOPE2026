# Independent mathematical audit

## correctness

PASS

For every odd b≥3, the 2b+1 low parts L_j=1+j(b−1) have digit sum 1 only at j=0,1,b+1 and digit sum b elsewhere; checked this independently for b=3,5,9,15. CRT avoidance is feasible even at q=2 because 2 divides b−1 and both P,Q≡−1 mod q, while q|b gives P≡1,Q≡2 mod q. Choosing P,Q rough to U, H=ord_{PQ}(b), and a=(P+b)/(b−1), R=P−b−a≥0 yields high block C with s_b(C)=P−b and C≡2P mod PQ. With N=C b^m+1, m a multiple of H and ≥3, the desired s_b(N+jd) equals P or Q and is coprime to its term. Varying m yields infinitely many distinct starts. No finite search is needed to establish existence in all odd bases.

## originality

PASS

Best-of-knowledge original composite-odd-base completion of the fixed-step (b−1), length (2b+1) anti-Niven progression construction. The inspected published theorem proves odd prime bases only, while even-base sharpness applies only to even b; conditional short-even-stride results cannot cover d=b−1 because every prime dividing b−1 also divides d.

## value

PASS

The fixed difference b−1 and target length 2b+1 are natural parameters in the existing anti-Niven progression problem; extending the known odd-prime construction to all odd composite bases resolves a substantive missing family without claiming sharpness for odd bases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
