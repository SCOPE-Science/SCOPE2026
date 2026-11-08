# Exact two-shift pseudoperiod classification for every Sturmian word

## Finding

Fix any irrational \(\alpha\in(0,1)\), any intercept \(\rho\in[0,1)\), and define the binary mechanical word
\[
s_{\alpha,\rho}(n)=\lfloor(n+1)\alpha+\rho\rfloor-\lfloor n\alpha+\rho\rfloor,\qquad n\ge0.
\]
For distinct positive integers \(p<q\), call \(\{p,q\}\) a two-shift pseudoperiod if, for every \(n\ge0\), at least one of \(s(n+p),s(n+q)\) equals \(s(n)\). Write \(\{x\}\) for fractional part, and put \(m=\min\{\alpha,1-\alpha\}\). Then the following is an exact necessary and sufficient condition:
\[
\boxed{\ \{p,q\}\text{ is a pseudoperiod}\quad\Longleftrightarrow\quad
\big|\{p\alpha\}-\{q\alpha\}\big|\ge 1-m=\max\{\alpha,1-\alpha\}.\ }
\]
In particular, the answer does **not** depend on \(\rho\). This describes all two-shift pseudoperiods for every irrational mechanical word, rather than only exhibiting one pair. In fact every such word has infinitely many distinct two-shift pseudoperiods, while no one-shift pseudoperiod exists.

## Assumptions and scope

The slope \(\alpha\) is irrational and strictly between zero and one; the intercept \(\rho\) is arbitrary in \([0,1)\). Both shifts are positive and distinct; the word is one-sided and the defining condition quantifies over **all** starting positions, not merely a limiting density. The term pseudoperiod means equality with one of two shifted symbols, not an ordinary period, Abelian period, or covering quasiperiod. Both standard half-open mechanical coding conventions obey the same condition by the identical circle argument.

## Proof

Write \(x_n=\{n\alpha+\rho\}\). The letter \(s(n)\) indicates membership of \(x_n\) in the half-open arc \([1-\alpha,1)\) of length \(\alpha\) on the unit circle. Swap the binary labels if necessary and rotate the circle so that the *shorter* of the two coding arcs becomes \(I=[0,m)\), of length \(m\le1/2\); denote its complement by \(J=[m,1)\). Equality and inequality of letters are invariant under both operations.

For \(0<t<1\), let \(E_t=\{x:1_I(x+t\bmod1)\ne1_I(x)\}\). Put \(a=\{p\alpha\}\) and \(b=\{q\alpha\}\), which are nonzero since \(\alpha\) is irrational. The claimed pseudoperiod holds at each position precisely when \(x_n\notin E_a\cap E_b\). We now characterize this intersection for the *entire circle*.

If \(t\in[m,1-m]\), the interior of \(I\) is disjoint from its translate by \(t\), so \(E_t\) contains the interior of \(I\). Every nonzero other shift \(u\) changes the membership of points in a nonempty open subset of \(I\). Thus \(E_t\cap E_u\) contains a nonempty open arc; no valid pair can contain such a shift. If both \(a,b\in(0,m)\), each mismatch set contains the final interval of \(I\) of the corresponding length, so their intersection has nonempty interior. Similarly, if both \(a,b\in(1-m,1)\), the mismatch sets contain initial intervals of \(I\) and overlap in an open arc.

It remains to take, after possibly exchanging the two shifts, \(a=u\in(0,m)\) and \(b=1-v\) with \(v\in(0,m)\). A direct calculation gives the **exact half-open interval identities**
\[
E_u\cap I=[m-u,m),\qquad E_{1-v}\cap I=[0,v),
\]
\[
E_u\cap J=[1-u,1),\qquad E_{1-v}\cap J=[m,m+v).
\]
The two mismatches overlap on \(I\) in a nonempty open interval exactly when \(u+v>m\). If \(u+v\le m\), they are disjoint on \(I\) (including the meeting endpoint), and they are disjoint on \(J\), since \(u+v\le m\le1-m\). Thus the simultaneous mismatch set is empty **if and only if** \(u+v\le m\). The other cases above have a nonempty open simultaneous-mismatch set.

The irrational rotation orbit \(\{x_n:n\ge0\}\) is dense in the circle for every \(\rho\). Consequently, every pair with a nonempty open simultaneous-mismatch set fails at some (indeed infinitely many) starting positions. Conversely, the empty-set case works at every position and for every intercept. Finally, in the only possible successful orientation, \(\lvert a-b\rvert=1-u-v\), so \(u+v\le m\) is equivalent to \(\lvert\{p\alpha\}-\{q\alpha\}\rvert\ge1-m\), as asserted.

To see that valid pairs are infinite, use density of positive multiples of \(\alpha\) modulo one to choose infinitely many distinct indices with fractional parts in \((0,m/4)\) and in \((1-m/4,1)\). Any index from the first set paired with an index from the second set satisfies the strict inequality. Finally, an ordinary period would force a one-shift equality for every index, but the density of ones in a mechanical word is the irrational number \(\alpha\), whereas a periodic binary word has rational letter frequencies.

## Verification

The standalone `verify.py` uses exact rational arithmetic to build every discontinuity of the two shift-comparison functions and then checks all endpoints and one interior point of each interval. For six rational test rotation angles (denominators greater than the tested shifts), every one of the \(6\binom{80}{2}=18{,}960\) shift pairs agrees with the claimed circular interval criterion. Rational test angles are used solely for exact finite stress tests; the mathematical proof above supplies the irrational all-position theorem. Run `python3 verify.py` with Python's standard library.

## Relationship to prior work

Meleshko, Ochem, Shallit and Shan (arXiv:2207.10171, publicly available July 20, 2022), Proposition 9, prove that every Sturmian word has **some** two-shift pseudoperiod; their Example 8 produces a 28-state automaton recognizing **all** two-shift pseudoperiods of the Fibonacci word. Those results are prior coverage and are not claimed as new here. The present claim instead provides a single explicit necessary-and-sufficient *arithmetic inequality* for **all** irrational Sturmian slopes and intercepts, classifying every pair without constructing a slope-dependent finite automaton. The familiar circle-coding characterization of Sturmian words is used as background.

## Limitations

The result is specific to two-symbol codings of an irrational rotation by two complementary intervals; it does not classify arbitrary two-shift pseudoperiods of higher-alphabet interval exchanges, nor codings with disconnected pieces. The special Fibonacci-word case is already decided by an earlier automaton, so the contribution is the uniform all-slope closed criterion, not that special case. No assertion of independent validation or exhaustive bibliographic uniqueness is made. An equivalent derivation could exist in literature not indexed or accessible in the consulted searches.

## References

- J. Meleshko, P. Ochem, J. Shallit and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171 (first public 2022-07-20), especially Example 8 and Proposition 9, pp. 5–6, https://arxiv.org/abs/2207.10171.
- J. Berstel and A. de Luca, *Sturmian words, Lyndon words and trees*, Theoretical Computer Science 178 (1997), for classical combinatorics of Sturmian words (background only).
- M. Lothaire, *Algebraic Combinatorics on Words*, Cambridge University Press, 2002, Chapter 2, for mechanical and rotation codings (background only).
