# A fixed-weight strict decimal digit-sum divisor ray without trailing zeroes

## Finding

Let \(s_{10}(n)\) denote the sum of the decimal digits of a nonnegative integer \(n\). For every integer \(k\ge12\), put
\[
N_k=448999(10^k+1).
\]
Then
\[
s_{10}(N_k)=86,\qquad s_{10}(N_k^2)=43,\qquad N_k\equiv9\pmod{10}.
\]
Consequently, \(s_{10}(N_k^2)\) is a **proper divisor** of \(s_{10}(N_k)\), with constant quotient \(2\), and the \(N_k\) are infinitely many distinct integers not divisible by \(10\). In particular, there exists a fixed unequal pair of decimal digital weights that occurs infinitely often among square arguments without trailing zeroes.

## Assumptions and scope

Integers are positive unless stated otherwise, decimal digits are written without leading zeroes, and \(k\) ranges over all integers \(k\ge12\). The result concerns exact digital sums, not usual arithmetic divisor sums. No assertion is made about other pairs of weights, minimality of the displayed weights, or the density of these integers.

## Proof

**Separated-block lemma.** If \(a\) and \(k\) are positive integers with \(a<10^k\) and \(2a^2<10^k\), and \(n=a(10^k+1)\), then no carries cross the three blocks in
\[
n^2=a^2\,10^{2k}+2a^2\,10^k+a^2.
\]
Therefore
\[
s_{10}(n)=2s_{10}(a),\qquad
s_{10}(n^2)=2s_{10}(a^2)+s_{10}(2a^2).
\]
This follows directly by writing each summand in blocks of length \(k\): \(a^2,2a^2<10^k\) guarantee disjoint positions. The formula also covers leading zeroes inside a block, since inserting zero digits changes no digit sum.

For the explicit seed \(a=448999\), exact integer multiplication yields
\[
a^2=201600102001,\qquad 2a^2=403200204002.
\]
Direct addition of their digits gives
\[
s_{10}(a)=43,\qquad s_{10}(a^2)=13,\qquad s_{10}(2a^2)=17.
\]
Both \(a^2\) and \(2a^2\) have \(12\) decimal digits, hence \(2a^2<10^{12}\le10^k\) and \(a<10^k\) whenever \(k\ge12\). Applying the lemma,
\[
s_{10}(N_k)=2\cdot43=86,
\qquad s_{10}(N_k^2)=2\cdot13+17=43.
\]
Because \(43\mid86\) and \(43<86\), the required division is proper. As \(10^k\) is divisible by \(10\), \(N_k\equiv a\equiv9\pmod{10}\). Finally \(N_k\) is strictly increasing in \(k\), so the family is infinite. This completes the proof.

## Verification

The standalone Python 3 script `checker.py` redoes the seed multiplications and decimal digit sums with integer arithmetic, checks the separated-block certificate, and verifies each instance for \(12\le k\le100\). The algebraic proof above, rather than that finite experiment, establishes the assertion for all \(k\ge12\). Run the script as `python3 checker.py` without additional dependencies.

## Relationship to prior work

OEIS A268135 records the condition \(s_{10}(n^2)\mid s_{10}(n)\) and a question posted on March 16, 2016, about infinitely many strict-divisor examples not divisible by \(10\). The present result is an explicit **fixed-weight** family. The weaker statement that infinitely many such integers exist is not asserted to be original: earlier general digital-sum constructions can imply it.

Hare, Laishram and Stoll (2010, arXiv:1001.4169) prove arbitrarily small square-to-input digit-sum ratios, using a construction where the square's weight can remain bounded while the argument's weight grows. Their construction supplies the unrestricted existence phenomenon by suitable congruence choices, but does not establish a fixed *unequal* weight pair as in the present claim. The same authors (2010, arXiv:1001.4170) prove infinite fixed-weight **equalities** \(s_q(n)=s_q(n^2)\) for sufficiently large permissible weights; these are not proper-divisor equalities. Their noninterfering-block identity is classical and is acknowledged here. The contribution is the explicit fixed, unequal pair of digital weights occurring infinitely often without trailing zeroes, not the splitting identity itself.

## Limitations

The result neither classifies all such pairs nor proves this is the smallest possible fixed unequal pair. The block-splitting device is standard and the main finite ingredient is a specific certified seed, so this is a focused existence result rather than a new general structural theory. Literature searches and inspection do not exclude a differently presented earlier explicit fixed unequal-weight construction.

## References

- OEIS, A268135, *Numbers n such that the digit sum of n² is a divisor of the digit sum of n*, created 26 January 2016; question by Chai Wah Wu, 16 March 2016: https://oeis.org/A268135
- K. G. Hare, S. Laishram, T. Stoll, *Stolarsky's conjecture and the sum of digits of polynomial values*, arXiv:1001.4169v1, 23 January 2010: https://arxiv.org/abs/1001.4169
- K. G. Hare, S. Laishram, T. Stoll, *The sum of digits of n and n²*, arXiv:1001.4170v1, 23 January 2010: https://arxiv.org/html/1001.4170v1
