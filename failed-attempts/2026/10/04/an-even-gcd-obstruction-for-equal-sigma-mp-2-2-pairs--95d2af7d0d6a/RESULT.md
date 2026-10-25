# An even-gcd obstruction for equal-sigma MP(2,2) pairs

## Finding
Let \(m,n\) be positive integers satisfying
\[
\sigma(m)^2=\sigma(n)^2=m^2+n^2.
\]
Then
\[
\sigma(m)=\sigma(n)
\]
is even, and
\[
2\mid m,\qquad 2\mid n.
\]
Consequently
\[
\gcd(m,n)\ge2.
\]

Thus Dimitrov's equal-sigma MP(2,2) question has no primitive or coprime solution, and no solution whose common divisor sum is odd.

## Assumptions and scope
Here
\[
\sigma(r)=\sum_{d\mid r}d
\]
is the ordinary sum-of-divisors function. The variables \(m,n\) are positive integers. The finding is a necessary condition only: it does not prove or disprove the existence of an imprimitive pair with both entries even.

Write
\[
c=\sigma(m)=\sigma(n).
\]
The defining equation becomes
\[
m^2+n^2=c^2,
\]
so \((m,n,c)\) is an integer right triangle.

## Proof
We first recall and prove the parity criterion for the divisor sum.

Let
\[
r=2^e\prod_{j=1}^s p_j^{a_j},
\]
where the \(p_j\) are odd primes. Since
\[
\sigma(2^e)=2^{e+1}-1
\]
is always odd, while
\[
\sigma(p_j^{a_j})=1+p_j+\cdots+p_j^{a_j}
\]
is a sum of \(a_j+1\) odd terms, multiplicativity gives
\[
\sigma(r)\ \text{odd}
\quad\Longleftrightarrow\quad
a_j\ \text{even for every }j.
\]
Equivalently,
\[
\sigma(r)\ \text{odd}
\quad\Longleftrightarrow\quad
r\ \text{is a square or twice a square}.
\]

Assume for contradiction that \(c\) is odd. From
\[
m^2+n^2=c^2
\]
and reduction modulo \(4\), exactly one of \(m,n\) is odd and the other is even. But
\[
\sigma(m)=\sigma(n)=c
\]
is odd, so both \(m\) and \(n\) are each a square or twice a square.

The odd leg cannot be twice a square. After interchanging \(m,n\) if necessary, write
\[
m=x^2
\]
with \(x>0\).

There are now exactly two possibilities for the even leg.

If
\[
n=y^2,
\]
then
\[
x^4+y^4=c^2.
\]
Fermat's classical fourth-power descent theorem states that this equation has no solution in positive integers.

If instead
\[
n=2y^2,
\]
then the right triangle with legs
\[
x^2,\qquad 2y^2
\]
has area
\[
\frac{x^2\cdot2y^2}{2}=(xy)^2,
\]
a nonzero perfect square. Fermat's right-triangle theorem states that no integer-sided right triangle has square area. This is again impossible.

Both possibilities contradict \(c\) odd. Therefore
\[
2\mid c.
\]

Finally,
\[
m^2+n^2=c^2\equiv0\pmod4.
\]
A square modulo \(4\) is \(0\) or \(1\). The only way for two squares to sum to \(0\pmod4\) is for both to be \(0\pmod4\). Hence
\[
2\mid m,\qquad2\mid n.
\]
This proves the claim.

## Verification
The accompanying `verify.py` independently computes the divisor-sum function for every integer through \(200000\).

It verifies the parity criterion
\[
\sigma(r)\ \text{odd}
\quad\Longleftrightarrow\quad
r\ \text{is a square or twice a square}
\]
through that range. It also searches all equal-\(\sigma\) fibers in the same range for a pair satisfying
\[
m^2+n^2=\sigma(m)^2
\]
and confirms that no such pair occurs.

As a definition regression, it checks the five MP(2,2) examples
\[
(1,2),\ (13,21),\ (13,27),\ (17,175),\ (45,123)
\]
displayed in Dimitrov's paper and confirms that each satisfies
\[
\sigma(m)^2+\sigma(n)^2=2(m^2+n^2)
\]
while none has equal divisor sums.

These finite computations are not used as an infinite proof. The theorem follows from the symbolic parity reduction and the two classical Fermat descent obstructions.

## Relationship to prior work
Dimitrov introduced MP(p,q)-amicable tuples and, for MP(2,2), explicitly asked whether there exists a pair \((m,n)\) with
\[
\sigma(m)=\sigma(n),
\]
equivalently
\[
\sigma(m)^2=\sigma(n)^2=m^2+n^2.
\]
The first public version of that paper appeared on 14 August 2024, and its primary 2020 Mathematics Subject Classification is \(11A25\).

The current OEIS entry A384255 records the larger components of MP(2,2) pairs and repeats this equal-sigma question. It reports that no example has been found with the larger component at most \(10^8\), but it does not state an evenness or gcd obstruction.

The result here is structural rather than another search extension: it proves that the entire primitive Pythagorean branch is impossible. Any future search or construction for Dimitrov's question may therefore restrict immediately to pairs with both entries even.

Targeted searches for the defining equation, the equal-sigma formulation, primitive solutions, parity restrictions, and Pythagorean reformulations did not locate a published statement implying this obstruction.

## Limitations
The result does not settle Dimitrov's existence question. It leaves open the possibility of solutions with
\[
2\mid m,\qquad2\mid n.
\]

The proof uses two classical nonexistence theorems from Fermat's method of infinite descent: there are no positive integer solutions of
\[
x^4+y^4=z^2,
\]
and no integer-sided right triangle has nonzero square area. Those theorems are not reproved here.

Because the parity argument is elementary, an equivalent observation may exist in an unindexed note, comment, or computational discussion even though it was not found in the inspected sources.

## References
1. S. I. Dimitrov, “Generalizations of amicable numbers,” arXiv:2408.07387v1, first public 14 August 2024.
2. OEIS A384255, integers occurring as larger components of MP(2,2)-amicable pairs; current comments include the equal-sigma question and the search bound \(10^8\).
3. Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory*, 2nd edition, Springer; Chapter 2, Problem 17 records the criterion that \(\sigma(r)\) is odd exactly for squares and twice-squares.
4. Fermat's classical infinite-descent theorems for fourth powers and square-area right triangles.
