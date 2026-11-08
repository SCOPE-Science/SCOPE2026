# Complete cofinite-attractor classification for the three-shifted Euler totient map

## Finding
Let \(\varphi\) be Euler's totient function, with \(\varphi(1)=1\), and put
\[
F(n)=\varphi(n)+3\qquad(n\in\mathbb N_{>0}).
\]
Every positive orbit of \(F\) eventually enters exactly one of the following periodic orbits:
\[
(9),\qquad (11,13,15),\qquad (23,25).
\]
Their minimal periods are \(1\), \(3\), and \(2\), respectively. Define the finite sets
\[
\begin{aligned}
E_1&=\{1,2,3,4,5,6,7,8,9,10,12,14,18\},\
E_2&=\{23,25,29,31,33,44,46,50,58,62,66\}.
\end{aligned}
\]
The complete basins of attraction are precisely \(E_1\) for the fixed point \(9\), precisely \(E_2\) for the two-cycle \((23,25)\), and \(\mathbb N_{>0}\setminus(E_1\cup E_2)\) for the three-cycle \((11,13,15)\). In particular, **exactly 24 positive integers fail to reach the three-cycle, and every integer \(n\ge67\) reaches it**. The cutoff is sharp: \(66\) reaches the two-cycle.

A structural descent statement underlies the classification: for every **odd** \(n\ge29\), at least one of \(F(n),F^2(n),F^3(n)\) is strictly less than \(n\). The three-iterate horizon is sharp at \(n=29\).

## Assumptions and scope
The domain is all positive integers, and the shift is exactly three. A periodic orbit is an ordered cycle up to cyclic rotation; a basin comprises all starting values that eventually enter that cycle. Arithmetic inequalities below use only the standard product formula for the Euler totient and the fact that sufficiently large prime pairs separated by two have the intervening third member of their residue triple divisible by three.

## Proof
**1. Parity reduction and strict descent.** The values \(F(1)=F(2)=4\) and \(F(4)=5\) handle the only inputs for which Euler's totient is odd. For each \(n\ge3\), \(\varphi(n)\) is even, so \(F(n)\) is odd. Hence every orbit reaches an odd positive integer at least three.

For every composite integer \(m\), let \(p\le\sqrt m\) be its least prime factor. The product formula gives
\[
\varphi(m)\le m\left(1-\frac1p\right)\le m-\sqrt m.
\tag{1}
\]
If odd \(n\ge29\) is composite, equation (1) yields \(F(n)\le n-\sqrt n+3<n\).

Suppose instead that odd \(n=p\ge29\) is prime. The next state is \(F(p)=p+2\). If \(p+2\) is composite, then
\[
F^2(p)\le p+5-\sqrt{p+2}<p,
\]
since \(p+2\ge31>25\). If \(p+2\) is prime, both primes exceed three. The residues modulo three force \(3\mid p+4\); consequently
\[
F^3(p)=\varphi(p+4)+3\le\frac23(p+4)+3<p
\]
because \(p>17\). Thus every odd \(n\ge29\) has a smaller odd iterate within at most three steps. Repeating this operation at decreasing stopping times cannot continue forever among positive integers. Every orbit therefore reaches an odd state at most \(27\). The horizon three cannot be reduced to two: \(29\to31\to33\to23\).

**2. Complete finite attractor.** The odd states \(3,5,\ldots,27\) form an invariant set with the exact transitions

| State | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21 | 23 | 25 | 27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Next | 5 | 7 | 9 | 9 | 13 | 15 | 11 | 19 | 21 | 15 | 25 | 23 | 21 |

Direct inspection gives precisely the three advertised periodic orbits, proves that every finite-state trajectory reaches one, and excludes all other periodic orbits by step 1.

**3. Global inverse-totient cutoff.** For any odd prime \(q\) and exponent \(a\ge1\),
\[
\varphi(q^a)=q^{a-1}(q-1)\ge q^{a/2}.
\]
For a factor \(2^a\), with \(a\ge1\), one has \(\varphi(2^a)=2^{a-1}\ge2^{(a-1)/2}\). Multiplicativity proves the uniform inequality
\[
\varphi(m)\ge\sqrt{m/2}\qquad(m\ge1).
\tag{2}
\]
Therefore, for any \(0\le t\le30\), every solution of \(\varphi(m)=t\) lies in \(1\le m\le1800\) (with no solution when \(t=0\)). A second arithmetic restriction makes the finite check transparent: if \(m=\prod q^{a_q}\) has totient \(t\), then each factor \(q^{a_q-1}(q-1)\) divides \(t\). Exhaustively applying the product formula within the proven cutoff yields

| \(t\) | All \(m\ge1\) satisfying \(\varphi(m)=t\) |
|---|---|
| \(0\) | none |
| \(1\) | \(1,2\) |
| \(2\) | \(3,4,6\) |
| \(4\) | \(5,8,10,12\) |
| \(6\) | \(7,9,14,18\) |
| \(20\) | \(25,33,44,50,66\) |
| \(22\) | \(23,46\) |
| \(26\) | none |
| \(28\) | \(29,58\) |
| \(30\) | \(31,62\) |

The standalone exact-integer program `verify.py` independently constructs this complete table for all \(m\le1800\). It is an **exhaustive finite computation after the analytic cutoff (2)**, not an extrapolation from test data.

**4. Reverse basin closure.** Since \(F(m)=s\) is equivalent to \(\varphi(m)=s-3\), the table gives every possible predecessor of each state in the exceptional cycles and their predecessor trees. The complete backward closure of \(9\) is
\[
9\leftarrow\{7,9,14,18\},\quad
7\leftarrow\{5,8,10,12\},\quad
5\leftarrow\{3,4,6\},\quad
4\leftarrow\{1,2\}.
\]
No other predecessor exists: \(3\) has no predecessor (it would require totient zero), and \(F(m)\) cannot be even except at \(4\). Thus this closure is exactly \(E_1\).

For the two-cycle,
\[
\begin{aligned}
23&\leftarrow\{25,33,44,50,66\},\
25&\leftarrow\{23,46\},\
33&\leftarrow\{31,62\},\
31&\leftarrow\{29,58\}.
\end{aligned}
\]
The state \(29\) has no predecessor because \(26\) is not a totient, and no even state listed here has any predecessor. This closure is exactly \(E_2\). The sets are disjoint. Every other starting integer reaches one of the three cycles by steps 1–2 and cannot reach the first two by these exhaustive predecessor classifications. It must therefore enter \((11,13,15)\). The greatest exception is \(66\), proving the sharp cutoff.

## Verification
The reproducible standalone script `verify.py`, run with Python 3 and no third-party dependencies, constructs Euler totients by a prime sieve. It computes the entire odd transition table independently using greatest-common-divisor counts; checks the one-to-three-step descent for every odd input through \(99999\); exhaustively verifies all ten inverse-totient rows through the analytically sufficient cutoff \(1800\); and checks the global basin classification for all starts through \(100000\). The actual output is saved in `verify_output.txt`. These finite regression tests are auxiliary to the unrestricted descent proof and the mathematically justified inverse-totient enumeration.

## Relationship to prior work
Leonetti and Luca (2023) prove eventual periodicity for every shifted Euler totient map \(n\mapsto\varphi(n)+k\), for all integer shifts \(k\ge0\). Their Theorem 2 and proof use the composite estimate (1), but do not determine the periodic orbits or global basins at the shift \(k=3\). A separate published result, *Sharp period-size bound and extremal structure for shifted Euler cycles*, bounds the maximum term of a period-\(T\) orbit by \([T(k-1)+1]^2\) and explicitly records the cycle \((23,25)\) at this shift. The present result **does not claim that two-cycle as new**. That conditional period-size bound cannot classify arbitrary periods or determine the exact basins, and does not imply that all but 24 starts reach \((11,13,15)\).

OEIS A051953 tabulates the cototient \(n-\varphi(n)\), an equivalent description of the one-step map, but the inspected entry does not give these dynamic basins or the exceptional finite set. The explicit cofinite-attractor classification is the contribution asserted here.

## Limitations
The classification is specific to the shift three and makes no assertion about other shifts. It gives the eventual orbit, not an exact closed formula for the number of iterations to reach it from an arbitrary large integer. The inverse-totient table depends on the provided exact bounded computation, which can be independently repeated. Unindexed equivalent treatments of this shift remain a possible originality risk.

## References
1. P. Leonetti and F. Luca, *On the iterates of shifted Euler's function*, arXiv:2302.01783v1 (3 February 2023), especially Theorem 2 and its proof; journal DOI 10.1017/S0004972723000394.
2. *Sharp period-size bound and extremal structure for shifted Euler cycles*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-period-size-bound-and-extremal-structure-for-shifted-euler--02d25ffc40ae .
3. OEIS A051953, *Cototient(n) := n - phi(n)*, https://oeis.org/A051953 .
