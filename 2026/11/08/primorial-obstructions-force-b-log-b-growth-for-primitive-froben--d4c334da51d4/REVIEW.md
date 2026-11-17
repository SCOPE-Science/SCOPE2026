# Independent mathematical audit

## correctness

PASS

For fixed a≥3 and (a,b)=1, define P_a(K)=product of primes p≤K with p∤a. CRT gives N≡0 mod P_a(K), N≡−b mod a and Kb−aP_a(K)<N≤Kb whenever Kb>aP_a(K). If N=ax+by with x,y≥0, then y≡−1 mod a, hence y≥a−1≥2 and gcd(y,a)=1; y≤K. Any prime p|y is ≤K, p∤a and p|N, forcing p|x and forbidding gcd(x,y)=1. The PNT yields log P_a(K)=K+o(K); with K=floor((1−ε)log b), P_a(K)=o(b) so g(a,b)/(b log b)≥1−ε−o(1) along all large coprime b. Letting ε→0 yields liminf≥1. A separate exact CRT representation enumeration checked (a,b,K)=(3,101,5),(4,105,7),(5,101,7) and found no primitive representations. The infinite bound depends on PNT, not that finite test.

## originality

PASS

The specific fixed a≥3 lower-growth result is not implied by the October 18 published primorial theorem, which assumes BOTH generators exceed a growing primorial and therefore cannot apply when a stays fixed. The original Ding–Wang–Zhang general bounds allow the result but do not imply a uniform fixed-a liminf≥1; an earlier limsup statement, if applied, likewise does not imply a liminf. Jaffe and Shimizu study the same primitive two-generator invariant, but the accessible statements concern finiteness, Farey relations and a fixed-factor lower bound. This is best-of-knowledge originality; the highly relevant Jaffe full text was inaccessible and the priority risk is explicitly preserved.

## value

PASS

The primitive Frobenius number is a natural modification of the classical two-generator problem; fixing one generator is a fundamental regime. Proving g(a,b)/b→∞ at rate at least log b for every fixed a≥3 is a substantive qualitative transition from the known linear a=1,2 cases and from prior constant-factor bounds. The CRT witness captures every possible primitive representation rather than just examples, providing a useful structural asymptotic obstruction without requiring a matching upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
