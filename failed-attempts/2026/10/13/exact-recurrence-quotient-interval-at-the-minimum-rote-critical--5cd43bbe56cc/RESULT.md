# Exact recurrence-quotient interval at the minimum Rote critical exponent
## Finding
A complementary-symmetric Rote sequence has factor complexity \(2n\) and a language closed under exchanging the two letters. Among binary rich sequences, the minimum critical exponent is
\[
2+\frac{1}{\sqrt2}.
\]
There are exactly two complementary-symmetric Rote languages attaining this value; their associated standard Sturmian directive sequences have the form
\[
G^{a_1}(D^2G^2)^\omega,
\qquad
a_1\in\{1,3\}.
\]

Let \(v\) be any sequence with either one of these two languages, and let \(R_v(m)\) be its recurrence function: the least length such that every factor of \(v\) of length \(m\) occurs in every factor of length \(R_v(m)\).

Then the complete set of accumulation points of the normalized recurrence function
\[
\frac{R_v(m)}{m}
\]
is the closed interval
\[
[\,3+\sqrt2,\ 5+3\sqrt2\,].
\]
Consequently the recurrence quotient is
\[
\limsup_{m\to\infty}\frac{R_v(m)}m=5+3\sqrt2,
\]
and the corresponding lower recurrence quotient is
\[
\liminf_{m\to\infty}\frac{R_v(m)}m=3+\sqrt2.
\]

Thus both minimum-critical-exponent Rote languages have the same exact normalized-recurrence spectrum, even though the recurrence function itself is piecewise affine on an expanding Pell scale.

## Assumptions and scope
For the two languages above, write \(Q_N=q'_N\) for the modified convergent denominators used in the recurrence-function theorem of Dvořáková, Medková, and Pelantová. Their proof gives
\[
Q_0=1,\qquad Q_1=a_1+1,
\]
and, for \(N\ge2\),
\[
Q_N=2Q_{N-1}+Q_{N-2}.
\]
It also gives the closed form
\[
Q_N=
\frac{(a_1+\sqrt2)(1+\sqrt2)^N-(a_1-\sqrt2)(1-\sqrt2)^N}{2\sqrt2}.
\]
Hence
\[
\frac{Q_{N+1}}{Q_N}\longrightarrow 1+\sqrt2.
\]

For these same directives all relevant parity conditions are odd and every later directive exponent equals \(2\). Specializing the published recurrence-function theorem therefore gives, for every \(N\ge0\) and every integer \(n\) satisfying
\[
Q_N\le n<Q_{N+1},
\]
the exact formula
\[
R_v(n+1)=n+3Q_{N+1}+Q_N.
\]

The result concerns the two languages attaining the minimum critical exponent. It does not assert the same interval for other complementary-symmetric Rote languages.

## Proof
Put
\[
\alpha=1+\sqrt2.
\]
The closed form for \(Q_N\) implies
\[
\frac{Q_{N+1}}{Q_N}\to\alpha
\qquad\text{and}\qquad
Q_N\to\infty.
\]

Set
\[
m=n+1.
\]
For
\[
Q_N+1\le m\le Q_{N+1},
\]
the exact recurrence formula becomes
\[
\frac{R_v(m)}m
=
1+\frac{3Q_{N+1}+Q_N-1}{m}.
\]
Define
\[
A_N=\frac{3Q_{N+1}+Q_N-1}{Q_N}.
\]
Then
\[
A_N\longrightarrow 3\alpha+1.
\]

Within the \(N\)-th Pell-scale interval, put
\[
x_N=\frac{m}{Q_N}.
\]
The admissible range is
\[
1+\frac1{Q_N}\le x_N\le\frac{Q_{N+1}}{Q_N}.
\]
Hence every subsequential limit of \(x_N\) lies in
\[
[1,\alpha].
\]
Along any subsequence for which \(x_N\to x\), we obtain
\[
\frac{R_v(m)}m
=
1+\frac{A_N}{x_N}
\longrightarrow
1+\frac{3\alpha+1}{x}.
\]
Therefore every accumulation point lies in the image of \([1,\alpha]\) under the continuous decreasing map
\[
x\longmapsto 1+\frac{3\alpha+1}{x}.
\]

Conversely, fix any \(x\in[1,\alpha]\). For each sufficiently large \(N\), choose an integer \(m_N\) in
\[
[Q_N+1,Q_{N+1}]
\]
nearest to \(xQ_N\), using the appropriate endpoint when \(x=1\) or \(x=\alpha\). Then
\[
\frac{m_N}{Q_N}\to x,
\]
so the corresponding normalized recurrence values converge to
\[
1+\frac{3\alpha+1}{x}.
\]
Thus every point in the image interval is attained as an accumulation point.

At the two endpoints,
\[
1+\frac{3\alpha+1}{\alpha}
=
4+\frac1\alpha
=
3+\sqrt2
\]
because
\[
\frac1\alpha=\sqrt2-1,
\]
while
\[
1+(3\alpha+1)=2+3\alpha=5+3\sqrt2.
\]
This proves that the complete accumulation set is
\[
[\,3+\sqrt2,\ 5+3\sqrt2\,].
\]

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier treats both directive initializations \(a_1=1\) and \(a_1=3\). It reconstructs the integer sequence \(Q_N\) from the recurrence, checks the published closed form through index \(24\), evaluates the exact published recurrence formula on Pell-scale endpoints, and checks convergence to the two claimed constants.

It also samples \(101\) target points across the scale interval and, by choosing integer arguments nearest to \(xQ_N\), verifies the finite approximation to the continuous accumulation map.

These calculations check algebra and endpoint normalization. The claim for infinitely many indices follows from the exact source formula and the limiting argument in the proof, not from numerical extrapolation.

## Relationship to prior work
Dvořáková, Medková, and Pelantová determine the critical exponent and recurrence function of complementary-symmetric Rote sequences. They classify the two languages attaining the minimum binary-rich critical exponent and derive the modified-convergent recurrence above. Their Example 55 writes the recurrence function explicitly for the \(a_1=1\) language.

The inspected paper does not define or compute the recurrence quotient, does not take \(\limsup R_v(m)/m\) or \(\liminf R_v(m)/m\), and does not state the complete accumulation set of normalized recurrence values. The same argument applies uniformly to the second minimum language \(a_1=3\), because the tail recurrence and parity regime are identical and only the initial condition of \(Q_N\) changes.

The recurrence quotient is a standard quantitative invariant in combinatorics on words. Cassaigne's survey records it for Sturmian words and notes the classical phenomenon that normalized recurrence need not converge. The result here gives the full nonconvergent interval for the extremal Rote pair, not only its upper endpoint.

## Limitations
The theorem is an asymptotic consequence of the published exact recurrence-function formula; it does not replace or reprove the return-word analysis underlying that formula.

No statement is made about which recurrence-quotient intervals occur for other Rote languages, or about extremality of the constants \(3+\sqrt2\) and \(5+3\sqrt2\) among all Rote sequences.

The accumulation set is determined for the normalized recurrence function only; no second-order error distribution is claimed.

## References
1. L. Dvořáková, K. Medková, and E. Pelantová, “Complementary symmetric Rote sequences: the critical exponent and the recurrence function,” arXiv:2003.06916v1, first public 2020-03-15; Discrete Mathematics & Theoretical Computer Science 22:1 (2020), DOI 10.23638/DMTCS-22-1-20.
2. J. Cassaigne, “On extremal properties of the Fibonacci word,” RAIRO - Theoretical Informatics and Applications 42 (2008), 701–715, DOI 10.1051/ita:2008003.
