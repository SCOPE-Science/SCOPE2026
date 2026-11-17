# Independent mathematical audit

## correctness

PASS

PASS: In Z_(p)[[x]] the expansion (1-x)^p=1-x^p-p*sum_{1<=j<p}x^j/j modulo p^2, after substituting x^(2d+1) and dividing the two series, gives C_d(p)=1-p sum_{(2d+1)j<=dp, p|(2d+1)j} j^(-1) mod p^2. Nonexceptional primes make the sum empty. If p|(2d+1), the range is j<= (p-1)/2, yielding -H_{(p-1)/2}=(2^p-2)/p mod p by binomial expansion. Boundary d=0 and Wieferich collisions handled as congruences, not strict residue inequality. Independent exact sliding-window vs inclusion-exclusion coefficient calculations tested 85 (p,d) cases, 3<=p<=13, 0<=d<=16.

## originality

PASS

PASS best-of-knowledge: Sun Lemma 2.5 gives T_p(b,c) congruent to b only modulo p for central trinomials; Mellit–Vlasenko Theorem 1 requires the origin to be the sole Newton-polytope interior lattice point, failing for Laurent x^(-d)+...+x^d when d>=2. Rudolph–Muller provides general trigonometric coefficient representations without the exact prime-square exception. No inspected result determines the all-d two-case p^2 residue. Older combinatorial congruence alias remains possible.

## value

PASS

PASS: This uniform exact p^2 classification across arbitrary odd alphabet widths has a structurally exceptional divisibility boundary p|(2d+1) and a Fermat-quotient correction independent of the alphabet quotient. It sharpens the natural central multinomial coefficient problem at prime exponents and distinguishes a genuine arithmetic resonance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
