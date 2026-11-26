# Independent mathematical audit

## correctness

PASS

For each witness t<x the defining divisibility is equivalent to y being a multiple of P(x)/gcd(P(x),P(t)); removing divisible moduli preserves the union. For two abscissae, simultaneous multiples use their least common multiple, and pairwise compatibility of residue differences 1,1,2 is sufficient and necessary by the generalized CRT. Independently, python3 /workspace/reproductions/5.py (NumPy) marked the original t-witness multiples directly for all residues modulo lcm(P(x),P(x+1)), without antichains or CRT triples. It found no three consecutive simultaneously invisible ordinates, including wraparound, at any x=1 through 229. At x=230 the full period 6163080 gave exactly 759044 and 781724 plus 0,1,2,3 times 1540770; hence the smaller-period two-class classification for all positive y follows. The direct witnesses at the first corner and gcd(231,759046)=1 were also checked. This is lexicographic and the shape is two abscissae by three ordinates.

## originality

PASS

Best-of-knowledge pass for the exact first 2-abscissa by 3-ordinate block and two complete boundary classes for the fixed polynomial. The strongest same-polynomial precedent gives a smaller square; the strongest first-occurrence table uses a different visibility relation.

## value

PASS

This is a natural rectangular extension of the motivating same-polynomial square example and of classical first-occurrence studies. It answers a specific larger-block existence problem by giving a sharp, lexicographic boundary and the complete set of starting ordinates there. The all-ordinate exclusion is useful exact data under the genuinely different polynomial predicate; no large-size or density conclusion is needed to make that finite cutoff meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
