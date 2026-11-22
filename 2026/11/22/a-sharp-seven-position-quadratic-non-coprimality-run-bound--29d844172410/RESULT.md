# A sharp seven-position quadratic non-coprimality run bound

## Finding

For a positive integer \(N\) with exactly three distinct prime divisors, define
\[
L(N)=\max\left\{\ell\ge0:\exists a\in\mathbb Z_{\ge0}\ \text{such that}\ \gcd((a+i)^2+1,N)>1\ \text{for every }0\le i<\ell\right\}.
\]
Then \(L(N)\le7\) for all such \(N\). This is sharp: \(L(1010)=7\). In fact, \(L(10r)=7\) for every prime \(r\equiv1\pmod4\), \(r\ne5\), providing an infinite family of extremal prime supports.

## Assumptions and scope

The variable \(a\) may be any nonnegative integer and \(N\) need not be squarefree. Exactly three distinct prime divisors are counted, regardless of multiplicities. The condition is non-coprimality of each value of the *translated polynomial* \((a+i)^2+1\), not the distinct notion of adding an arbitrary common constant to a fixed quadratic sequence. This result concerns the polynomial \(X^2+1\), not arbitrary quadratics.

## Proof

**Local two-hit lemma.** If an odd prime \(p\) divides \(u^2+1\), then \(p\equiv1\pmod4\); in particular, \(p\ge5\). Let \(0\le i<j\le7\) and \(d=j-i\). If an odd prime \(p>7\) divides both \((a+i)^2+1\) and \((a+j)^2+1\), subtracting the two quadratic congruences gives \(d(2(a+i)+d)\equiv0\pmod p\). Since \(1\le d\le7<p\), we get \(2(a+i)\equiv-d\pmod p\), and substitution gives \(p\mid d^2+4\). The seven integers \(d^2+4\), for \(1\le d\le7\), are
\[
5,\ 8,\ 13,\ 20,\ 29,\ 40,\ 53.
\]
Thus for a prime \(p\notin\{2,5\}\), two hits among eight positions can occur only at separation \(3,5,7\), respectively with \(p=13,29,53\). Every other such prime has at most one hit. In particular, a prime other than \(2\) or \(5\) can hit at most one position among any four indices of the same parity, because their separations are \(2,4,6\).

**Case \(2\mid N\).** The prime \(2\) hits exactly four of the eight indices, those with odd value \(a+i\). The other four indices have the same parity. If \(5\mid N\), the two remaining prime factors are \(5\) and another prime \(p\ne2,5\). Among those four equal-parity indices, \(5\) hits at most two, because their residues modulo \(5\) are distinct and the only roots of \(X^2+1\) modulo \(5\) are \(\pm2\); the other prime hits at most one. Therefore at least one position remains uncovered. If \(5\nmid N\), the other two prime factors each hit at most one of those four positions, again leaving uncovered positions.

**Case \(2\nmid N\).** Each prime other than \(5\) hits at most two positions, so an eight-position covering would require \(5\mid N\). Since \(5\) can hit at most four of the eight positions, covering all eight would force it to hit exactly four, with each of the two other primes hitting exactly two of the four remaining positions. For \(a\bmod5\), the only two four-hit patterns of \(5\) are \(\{0,1,5,6\}\) and \(\{1,2,6,7\}\). Their complements are, respectively, \(\{2,3,4,7\}\) and \(\{0,3,4,5\}\). By the local lemma, a prime other than \(2,5\) can hit a pair only at separation \(3,5,7\). Neither complement has a partition into two pairs with both separations in this set: in the first, the only eligible edges are \(\{4,7\}\) and \(\{2,7\}\), which share the vertex \(7\); in the second, the only eligible edges are \(\{0,3\}\) and \(\{0,5\}\), which share \(0\). This is a contradiction.

Therefore eight consecutive positions can never all be non-coprime, proving \(L(N)\le7\).

**Sharpness.** For \(N=1010=2\cdot5\cdot101\), take \(a=7\). The values at positions \(i=0,1,\ldots,6\) are
\[
50,\ 65,\ 82,\ 101,\ 122,\ 145,\ 170,
\]
all divisible by one of \(2,5,101\). For the general family, let \(r\equiv1\pmod4\) be any prime other than \(5\), and choose \(t\) with \(t^2\equiv-1\pmod r\). The Chinese remainder theorem supplies arbitrarily large nonnegative \(a\) satisfying
\[
a\equiv7\pmod{10},\qquad a+3\equiv t\pmod r.
\]
The four offsets \(i=0,2,4,6\) give even quadratic values, offsets \(1,5\) give values divisible by \(5\), and offset \(3\) gives a value divisible by \(r\). Hence all seven are non-coprime to \(10r\). Infinitely many primes \(r\equiv1\pmod4\) exist, so the bound is attained for infinitely many distinct prime supports.

## Verification

A self-contained standard-library Python program `verify.py` checks the exact eight-position local masks for \(2,5,13,29,53\), adds three independent singleton-mask placeholders for all other possible primes, and exhaustively rules out a union covering all eight with three distinct local factors. It also verifies the seven-term example and CRT witnesses for several primes. This finite checker is supplementary: the unrestricted upper bound follows from the proved local two-hit lemma and the explicit parity/matching argument above, not from testing finitely many moduli.

## Relationship to prior work

Kalmynin and Konyagin, *A polynomial analogue of Jacobsthal function* (2023 preprint), study maximal non-coprime stretches of \(x+f(i)\) as a freely chosen *additive constant* \(x\) varies. That is **not** the translated-argument condition \(f(a+i)\) studied here, nor does their large-prime-support lower bound imply this sharp three-prime cutoff. Dietmann–Elsholtz–Kalmynin–Konyagin–Maynard treat long gaps between integers representable by binary quadratic forms and a related additive polynomial shift; that is likewise not an eight-position three-factor coverage theorem. Ziller–Morack's paired Jacobsthal function concerns simultaneous linear-progressions conditions rather than the quadratic polynomial here. Comparisons to analogous results for other polynomials do not imply this one because the local two-hit factors \(d^2+4\) are specific to \(X^2+1\).

## Limitations

The theorem does not classify all moduli attaining seven, nor does it address moduli with four or more distinct prime divisors or all quadratic polynomials. Literature searches cannot exclude every unindexed earlier equivalent formulation, and independent expert validation remains outstanding.

## References

1. A. Kalmynin and S. Konyagin, *A polynomial analogue of Jacobsthal function*, arXiv:2302.00459v1, first posted 2023-02-01; journal full text https://doi.org/10.4213/im9467e .
2. R. Dietmann, C. Elsholtz, A. Kalmynin, S. Konyagin, and J. Maynard, *Longer gaps between values of binary quadratic forms*, International Mathematics Research Notices 2023(12), 10313–10349, https://doi.org/10.1093/imrn/rnac130 (first online 2022-05-30).
3. M. Ziller and J. F. Morack, *A short note on the computation of the generalised Jacobsthal function for paired progressions*, arXiv:1706.03668v1 (2017).
