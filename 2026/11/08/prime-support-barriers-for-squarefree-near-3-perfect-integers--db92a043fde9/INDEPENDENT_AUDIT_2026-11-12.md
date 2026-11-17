# Independent mathematical audit

## correctness

PASS

For squarefree n, sigma(n)/n=prod_{p|n}(1+1/p). If even, sigma(2) forces 3|n, and a further p=2 (mod 3) would make 9|d|n, impossible. Hence n=6P with P supported on p=1 (mod 3), and d=6D, D=2sigma(P)-3P>0 dividing P. D mod 3 forces odd r=omega(P). Monotonicity of abundance bounds all r<=9 by the first ten eligible primes. At r=11, any missed one of the first ten reduces abundance below 3; if all ten occur, q=97,103,109 are the only positive-surplus final primes, and exact Euclidean gcds rule out D|P. Thus r>=13, omega(n)>=15. For odd squarefree n the 3-adic sieve permits at most one p=2 (mod3), so the maximally abundant 121-prime support 3,5 and the first 119 primes 1 (mod3) has ratio below 3; omega>=122. Independently reproduced the exact products, q119=1567, q120=1579 and three gcd obstructions. A finite arithmetic certificate validates only the reduced inequalities, not hypothetical existence.

## originality

PASS

The lower bounds and exact even boundary obstruction apply to ALL squarefree solutions of sigma(n)=3n+d, rather than prior small fixed-exponent families. Full primary 2017 paper and OEIS special-form table do not supply this global consequence; related omitted-divisor models have different defining equations. Historical priority remains best-of-knowledge.

## value

PASS

A nontrivial universal prime-support obstruction for a natural unsolved divisor-sum existence problem, combining 3-adic local constraints with an exact extremal abundance sieve. The sharp elimination of the only positive-surplus 13-support options is substantive; no false existence or optimality is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
