# Consecutive Dedekind-psi collisions at multiplicative complexity two
## Finding
Let
\[
\psi(n)=n\prod_{p\mid n}\left(1+\frac1p\right)
\]
be the Dedekind psi function, and let
\[
\Omega(n)
\]
denote the number of prime factors of \(n\), counted with multiplicity.

If
\[
\psi(n)=\psi(n+1),
\qquad
\Omega(n)\le2,
\qquad
\Omega(n+1)\le2,
\]
then
\[
n\in\{4,14\}.
\]

Equivalently, the complete list of consecutive collisions in the first two multiplicative-complexity layers is
\[
\psi(4)=\psi(5)=6
\]
and
\[
\psi(14)=\psi(15)=24.
\]

The pair
\[
(14,15)
\]
is the unique collision in which both consecutive integers are squarefree semiprimes. The pair
\[
(4,5)
\]
is the unique collision involving a prime square and a prime.

## Assumptions and scope
The Dedekind psi function is multiplicative and satisfies
\[
\psi(p^a)=p^{a-1}(p+1)
\]
for prime powers.

The theorem concerns positive integers \(n\) for which both \(n\) and \(n+1\) have at most two prime factors counted with multiplicity. Thus each number is one of
\[
1,\quad p,\quad p^2,\quad pq
\]
with primes \(p\ne q\).

No claim is made about collisions in higher multiplicative-complexity layers. Such collisions are plentiful in the public collision sequence.

## Proof
The values needed in the allowed factorization types are
\[
\psi(p)=p+1,
\]
\[
\psi(p^2)=p^2+p,
\]
and, for distinct primes \(p,r\),
\[
\psi(pr)=(p+1)(r+1)=pr+p+r+1.
\tag{1}
\]

The cases \(n=1\) and \(n=2\) are immediate and give no collision.

Suppose first that \(n\) is prime. Then
\[
\psi(n)=n+1.
\]
If \(n+1\) is composite with \(\Omega(n+1)\le2\), formula (1) or the prime-square formula gives
\[
\psi(n+1)>n+2.
\]
Thus no collision has a prime on the left.

Now suppose \(n+1\) is prime and \(n\) is composite. If
\[
n=p^2,
\]
then equality gives
\[
p^2+p=p^2+2,
\]
so \(p=2\), yielding
\[
(n,n+1)=(4,5).
\]
If
\[
n=pr
\]
with distinct primes, then
\[
\psi(n)=n+p+r+1>n+2=\psi(n+1),
\]
so there is no further solution.

It remains to treat the case in which both \(n\) and \(n+1\) are composite.

Two prime squares cannot be consecutive. Suppose
\[
n=p^2,\qquad n+1=qr
\]
with distinct primes \(q,r\). Equality of psi values gives
\[
p=q+r+2.
\]
But then
\[
p^2+1=qr
\le
\frac{(q+r)^2}{4}
=
\frac{(p-2)^2}{4}
<
p^2+1,
\]
a contradiction.

Conversely, suppose
\[
n=pr,\qquad n+1=s^2,
\]
where \(p,r\) are distinct primes and \(s\) is prime. Equality gives
\[
p+r=s.
\]
Yet
\[
s^2-1=pr
\le
\frac{(p+r)^2}{4}
=
\frac{s^2}{4},
\]
which is impossible for \(s\ge3\).

The final case has two squarefree semiprimes:
\[
n=pr,\qquad n+1=qs.
\]
From (1) and
\[
qs=pr+1,
\]
the equality of psi values is equivalent to
\[
p+r=q+s+1.
\tag{2}
\]

If \(n\) is even, write
\[
p=2.
\]
Then \(q,s\) are odd primes. Equation (2) gives
\[
r=q+s-1,
\]
and the consecutive-product relation gives
\[
qs=2r+1=2q+2s-1.
\]
Hence
\[
(q-2)(s-2)=3.
\]
Ordering \(q<s\) forces
\[
q=3,\qquad s=5,\qquad r=7.
\]
This yields
\[
(n,n+1)=(14,15).
\]

If instead \(n\) is odd, then \(n+1\) is the even squarefree semiprime, so write
\[
n=pr,\qquad n+1=2s
\]
with \(p,r,s\) odd primes. Equality of psi values gives
\[
p+r=s+3.
\]
Together with
\[
pr+1=2s,
\]
this implies
\[
(p-2)(r-2)=-3,
\]
impossible because both factors on the left are positive.

All factorization types have now been exhausted. Direct substitution verifies the two surviving collisions.

## Verification
The accompanying checker independently evaluates \(\Omega\) and the Dedekind psi function by exact integer factorization for every
\[
1\le n<100000.
\]
Among the pairs satisfying
\[
\Omega(n)\le2,\qquad \Omega(n+1)\le2,
\]
it finds exactly
\[
(4,5)
\quad\text{and}\quad
(14,15).
\]

This finite calculation is only a stress test. The unrestricted theorem follows from the factorization-type proof above, which exhausts every integer with \(\Omega\le2\).

## Relationship to prior work
Solé and Planat study the Dedekind psi function as a multiplicative arithmetic function, relate it to the divisor-sum and Euler-totient functions, and prove extremal-value results. Their paper gives the prime-power normalization used here and lists primary classifications \(11N56\), \(11A25\), and \(11M06\). It does not study consecutive equal values.

The exact database A291043 is devoted specifically to the equation
\[
\psi(n)=\psi(n+1).
\]
It begins
\[
4,8,14,15,32,44,45,62,\ldots
\]
and records that \(14\) is the smallest collision whose two members are both products of two distinct primes. That database supplies exact examples and extensive finite data, but it does not state that the only collisions with
\[
\Omega(n),\Omega(n+1)\le2
\]
are \(4\) and \(14\).

The squarefree collision
\[
(14,15)
\]
also satisfies
\[
\sigma(14)=\sigma(15)
\]
because \(\psi=\sigma\) on squarefree integers. The extra collision
\[
(4,5)
\]
is genuinely specific to the Dedekind psi function.

## Limitations
The theorem closes only the first two \(\Omega\)-layers. It does not constrain collisions once either member has three or more prime factors counted with multiplicity.

The public collision database contains many higher-complexity examples, so the result is not a statement of global injectivity or rarity.

The proof is elementary, and the principal residual originality risk is that the same low-\(\Omega\) classification may have appeared as an unindexed observation attached to computations of consecutive Dedekind-psi collisions.

## References
1. P. Solé and M. Planat, “Extreme values of the Dedekind \(\Psi\) function,” arXiv:1011.1825, first submitted 8 November 2010; later *Journal of Combinatorics and Number Theory* 3 (2011), 33–38.
2. OEIS Foundation, A001615, “Dedekind psi function.”
3. OEIS Foundation, A291043, “Numbers \(n\) such that \(\psi(n)=\psi(n+1)\),” authored 16 August 2017.
