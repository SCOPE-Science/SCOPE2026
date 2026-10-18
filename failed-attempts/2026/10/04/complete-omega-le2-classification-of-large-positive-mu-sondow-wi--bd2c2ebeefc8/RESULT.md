# Complete \(\Omega\le2\) classification of large positive \(\mu\)-Sondow witnesses

## Finding
Let \(\mu>0\), and let \(\mathfrak S_\mu\) denote the set of \(\mu\)-Sondow numbers. Let \(\Omega(n)\) be the number of prime factors of \(n\), counted with multiplicity.

If
\[
n>\mu
\qquad\text{and}\qquad
\Omega(n)\le2,
\]
then
\[
n\in\mathfrak S_\mu
\]
if and only if exactly one of the following three alternatives holds:

1. \(n=p\) is prime and
\[
\mu=p-1.
\]

2. \(n=p^2\) for a prime \(p\) and
\[
\mu=p(p-1).
\]

3. \(n=pq\) for distinct primes \(p<q\) and
\[
\mu=pq-p-q=(p-1)(q-1)-1.
\]

Equivalently, the squarefree semiprime case occurs precisely when
\[
\mu+1=(p-1)(q-1)
\]
for distinct primes \(p<q\).

For the difficult parameter \(\mu=673\) singled out in the source paper, none of the three alternatives is possible. Hence every possible member
\[
n>673,\qquad n\in\mathfrak S_{673},
\]
must satisfy
\[
\Omega(n)\ge3.
\]

## Assumptions and scope
A positive integer \(n\) is a \(\mu\)-Sondow number when, for every prime \(p\mid n\),
\[
p^{\nu_p(n)}\mid \frac{n}{p}+\mu.
\]
The primary source proves the equivalent characterization
\[
\frac{\mu}{n}+\sum_{p\mid n}\frac1p\in\mathbb Z.
\]

The result here assumes \(\mu>0\) and classifies only witnesses larger than \(\mu\) with at most two prime factors counted with multiplicity. It does not prove the existence conjecture for arbitrary \(\mu\), nor does it classify witnesses with \(\Omega(n)\ge3\).

## Proof
Use the source's equivalent characterization
\[
\frac{\mu}{n}+\sum_{p\mid n}\frac1p\in\mathbb Z.
\]

Because \(\mu>0\), \(n>\mu\), and \(\Omega(n)\le2\), there are exactly three possible shapes.

If \(n=p\) is prime, then
\[
\frac{\mu}{p}+\frac1p=\frac{\mu+1}{p}
\]
is a positive integer. Since
\[
0<\mu<p,
\]
we have
\[
0<\mu+1\le p.
\]
Therefore the integer is exactly \(1\), so
\[
\mu=p-1.
\]
Conversely, if \(\mu=p-1\), the displayed quotient equals \(1\), so \(p\in\mathfrak S_\mu\).

If \(n=p^2\), then
\[
\frac{\mu}{p^2}+\frac1p=\frac{\mu+p}{p^2}
\]
is a positive integer. Since
\[
0<\mu<p^2,
\]
we get
\[
0<\mu+p<p^2+p\le2p^2.
\]
Thus the integer is exactly \(1\), giving
\[
\mu=p^2-p=p(p-1).
\]
Conversely, this identity makes the displayed expression equal to \(1\), so \(p^2\in\mathfrak S_\mu\).

Finally let
\[
n=pq
\]
for distinct primes \(p<q\). Then
\[
\frac{\mu}{pq}+\frac1p+\frac1q
=
\frac{\mu+p+q}{pq}
\]
is a positive integer. Since
\[
0<\mu<pq
\]
and
\[
p+q<pq
\]
for distinct primes, the numerator is strictly between \(0\) and \(2pq\). Hence the integer is exactly \(1\), and
\[
\mu=pq-p-q=(p-1)(q-1)-1.
\]
Conversely, this identity again makes the defining rational expression equal to \(1\), proving sufficiency.

These three shapes exhaust all \(n\) with \(\Omega(n)\le2\), proving the classification.

For \(\mu=673\), the prime case would require
\[
p=674,
\]
which is composite. The prime-square case would require
\[
p^2-p-673=0,
\]
whose discriminant is
\[
2693,
\]
strictly between
\[
51^2=2601
\quad\text{and}\quad
52^2=2704,
\]
so there is no integral \(p\).

For the distinct-prime case,
\[
(p-1)(q-1)=674=2\cdot337.
\]
Up to order, the only factor pairs are
\[
(1,674)
\quad\text{and}\quad
(2,337).
\]
They would give
\[
(p,q)=(2,675)
\quad\text{or}\quad
(3,338),
\]
and the second coordinate is composite in each case. Thus no \(n>673\) with \(\Omega(n)\le2\) lies in \(\mathfrak S_{673}\).

## Verification
The accompanying `verify.py` checks the three symbolic families directly from the defining divisibility condition, verifies the converse identities over a finite regression range of primes, and exhaustively checks all \(1\le\mu<300\) and all \(n\le1500\) with \(\Omega(n)\le2\) against the classification.

It separately verifies the complete factor-pair obstruction for \(\mu=673\).

The finite regression is not used to prove the theorem. Exhaustiveness follows from the source's exact rational characterization and the three possible shapes of integers with \(\Omega(n)\le2\).

A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Grau, Oller-Marcén, and Sadornil introduced \(\mu\)-Sondow numbers and proved several equivalent characterizations, including
\[
\frac{\mu}{n}+\sum_{p\mid n}\frac1p\in\mathbb Z.
\]
They close their paper with the conjecture that, for every integer \(\mu\), there is a \(\mu\)-Sondow number larger than \(|\mu|\).

The same source reports that this conjecture was computationally verified for
\[
-145<\mu<673,
\]
while for \(\mu=673\) it found no witness in
\[
(673,10^{10}].
\]
The theorem above gives a structural explanation for part of that difficulty: no prime, prime square, or product of two distinct primes can ever be a large \(673\)-Sondow witness, regardless of search bound.

The source's propositions relating \(\mu\)-Sondow numbers to weak primary pseudoperfect and Giuga numbers do not state this low-\(\Omega\) classification. Targeted searches for semiprime \(\mu\)-Sondow numbers, the identity
\[
\mu+1=(p-1)(q-1),
\]
and the \(\mu=673\) prime-factor obstruction did not locate a prior statement of the theorem.

## Limitations
The theorem does not address numbers with three or more prime factors counted with multiplicity. In particular, it does not settle whether \(\mathfrak S_{673}\) contains any number greater than \(673\).

The source's search through \(10^{10}\) is finite computational evidence, not a nonexistence proof beyond that range. The new theorem is unbounded only with respect to the restricted condition \(\Omega(n)\le2\).

Literature non-detection does not prove that no unindexed or unpublished equivalent observation exists.

## References
1. J. M. Grau, A. M. Oller-Marcén, and D. Sadornil, “On \(\mu\)-Sondow Numbers,” arXiv:2111.14211v1, first posted 28 November 2021; *Acta Mathematica Hungarica* 169 (2023).
