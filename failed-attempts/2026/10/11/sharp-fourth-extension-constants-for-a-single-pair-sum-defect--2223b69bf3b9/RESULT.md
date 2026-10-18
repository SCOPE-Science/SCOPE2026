# Sharp fourth-extension constants for a single pair-sum defect
## Finding
Let \(\Gamma\) be a finite abelian group of odd order \(N\), and let \(S\subset\Gamma\) have \(m\ge3\) elements. Assume that the unordered pair-sum map
\[
\{\xi,\eta\}\longmapsto \xi+\eta
\]
on two-element multisets from \(S\) has exactly one fiber of size two and every other fiber has size one. Give \(S\) normalized counting measure and \(\widehat\Gamma\) counting measure, and put
\[
E_S f(x)=\frac1m\sum_{\xi\in S} f(\xi)\xi(x).
\]

Exactly one of the following occurs.

1. The collision is \(a+b=c+d\) between two off-diagonal pairs. The four elements are necessarily distinct, and
\[
\|E_S\|_{L^2(S)\to L^4(\widehat\Gamma)}^4=\frac{9N}{4m^2}.
\]
For a nonzero \(f\), equality holds exactly when \(f\) vanishes off \(\{a,b,c,d\}\), the four moduli are equal, and
\[
f(a)f(b)\overline{f(c)f(d)}>0.
\]

2. The collision is \(2a=b+c\) between one diagonal and one off-diagonal pair. The three elements are necessarily distinct, and
\[
\|E_S\|_{L^2(S)\to L^4(\widehat\Gamma)}^4=\frac{15N}{7m^2}.
\]
For a nonzero \(f\), equality holds exactly when \(f\) vanishes off \(\{a,b,c\}\),
\[
|f(a)|^2:|f(b)|^2:|f(c)|^2=3:2:2,
\]
and
\[
f(a)^2\overline{f(b)f(c)}>0.
\]

Thus the first possible failure of pair-sum uniqueness has a universal sharp fourth-extension penalty determined only by whether the repeated sum is a proper parallelogram or a midpoint relation.

## Assumptions and scope
The group operation on \(\Gamma\) is written additively. An unordered two-element multiset permits repetition, so \(\{\xi,\xi\}\) is allowed. The hypothesis says that precisely one sum in \(\Gamma\) has two such representations and every other sum has one or zero.

The odd-order assumption is structural. Multiplication by \(2\) is then injective, so two different diagonal pairs cannot collide. Two different off-diagonal pairs with the same sum cannot share exactly one endpoint. Consequently the unique nonsingleton fiber is necessarily one of the two types stated above.

The claim is conditional on the one-defect hypothesis; it does not classify which subsets of which groups have that additive structure.

## Proof
Write
\[
T=\sum_{\xi\in S}|f(\xi)|^2,\qquad
Q=\sum_{\xi\in S}|f(\xi)|^4.
\]
Character orthogonality gives
\[
\frac{\|E_Sf\|_4^4}{\|f\|_2^4}
=\frac{N}{m^2}\frac{A(f)}{T^2},
\]
where
\[
A(f)=\sum_{s\in\Gamma}
\left|\sum_{\xi+\eta=s}f(\xi)f(\eta)\right|^2.
\]
If every unordered pair sum were unique, each diagonal contributes \(|f(\xi)|^4\) and each off-diagonal pair contributes \(4|f(\xi)f(\eta)|^2\), so the baseline is
\[
A_0(f)=2T^2-Q.
\]

For the proper-parallelogram defect \(a+b=c+d\), merging the two off-diagonal fibers adds exactly
\[
8\operatorname{Re}\!\left(f(a)f(b)\overline{f(c)f(d)}\right).
\]
Put \(x_\xi=|f(\xi)|^2\), and let
\[
y=x_a+x_b+x_c+x_d.
\]
The phase term is at most \(8\sqrt{x_ax_bx_cx_d}\). By Cauchy--Schwarz and arithmetic--geometric mean,
\[
x_a^2+x_b^2+x_c^2+x_d^2\ge\frac{y^2}{4},
\qquad
\sqrt{x_ax_bx_cx_d}\le\left(\frac y4\right)^2.
\]
Hence the contribution of these four coordinates to \(-Q\) plus the collision term is at most \(y^2/4\), with equality exactly when the four \(x\)-values are equal and the collision phases align. If there are coordinates outside the defect, then
\[
\sum_{\xi\notin\{a,b,c,d\}}x_\xi^2
\ge
\frac{(T-y)^2}{m-4}.
\]
Therefore, for \(m>4\),
\[
\frac{A(f)}{T^2}
\le
2+\frac14\left(\frac yT\right)^2
-\frac1{m-4}\left(1-\frac yT\right)^2
\le \frac94.
\]
The last expression is strictly increasing in \(y/T\) on \([0,1]\), so equality forces \(y=T\). The case \(m=4\) is the same calculation without the outside term. This proves both the constant and the full equality class.

For the midpoint defect \(2a=b+c\), merging the diagonal and off-diagonal fibers adds
\[
4\operatorname{Re}\!\left(f(a)^2\overline{f(b)f(c)}\right).
\]
Set
\[
t=x_a,\qquad s=x_b+x_c,\qquad y=t+s.
\]
For fixed \(t\) and \(s\),
\[
x_b^2+x_c^2\ge \frac{s^2}{2},
\qquad
\sqrt{x_bx_c}\le\frac s2.
\]
Thus the three defect coordinates contribute at most
\[
-t^2-\frac{s^2}{2}+2ts.
\]
With \(s=y-t\), this concave quadratic is maximized uniquely at
\[
t=\frac{3y}{7},\qquad x_b=x_c=\frac{2y}{7},
\]
and its maximum is \(y^2/7\). For \(m>3\), the coordinates outside the defect satisfy
\[
\sum_{\xi\notin\{a,b,c\}}x_\xi^2
\ge
\frac{(T-y)^2}{m-3}.
\]
Consequently
\[
\frac{A(f)}{T^2}
\le
2+\frac17\left(\frac yT\right)^2
-\frac1{m-3}\left(1-\frac yT\right)^2
\le \frac{15}{7}.
\]
Again the final expression is strictly increasing on \([0,1]\), so equality forces \(y=T\), the ratio \(3:2:2\), equality in the phase bound, and no mass outside the defect. The case \(m=3\) is immediate from the same three-variable optimization.

## Verification
The proof above is exact and does not depend on finite enumeration. A standalone checker, `verify.py`, independently reconstructs the ordered-pair convolution for every one-defect subset of \(\mathbb Z_N\) with \(N\in\{5,7,9,11,13\}\) and subset size at most \(6\), and compares it with the two claimed energy identities for deterministic Gaussian-integer coefficient vectors. It found \(199\) proper-parallelogram examples and \(613\) midpoint examples and completed \(1624\) exact energy comparisons.

The same checker evaluates the two scalar equality optimizations with exact rational arithmetic and verifies strict localization on a rational grid whenever outside mass is present. Its successful output is
`VERIFY_OK P_sets=199 M_sets=613 exact_energy_checks=1624 cyclic_orders=5,7,9,11,13`.

These computations corroborate the algebra and collision taxonomy; they are not used as a substitute for the universal proof.

## Relationship to prior work
Mockenhaupt and Tao introduced the finite-field restriction framework and, for even exponents, reduce extension estimates to additive representation counts; their pair-count argument supplies general bounds from a maximum multiplicity but does not give the sharp weighted optimization or equality class for a single repeated sum. See G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234.

Allison Lewko and Mark Lewko study \(B_2[g]\) sets and \(\Lambda(4)\) structure, making repeated sums \(a+b=c+d\) a standard object in this setting. Their results concern structural decompositions and general \(\Lambda(4)\) control rather than the two exact one-defect constants and the extremizer localization proved here. See A. Lewko and M. Lewko, *On the Structure of Sets of Large Doubling*, arXiv:1003.4561.

The result isolates the first deviation from a Sidon-type pair-sum pattern and shows that diagonal and off-diagonal defects have genuinely different sharp extension costs.

## Limitations
The theorem assumes odd group order and exactly one double fiber of the unordered pair-sum map. Multiple collisions can interact and are not covered. Even-order groups admit additional diagonal behavior because doubling need not be injective. The theorem also does not classify the ambient sets satisfying the one-defect hypothesis.

A residual literature risk remains that an equivalent one-collision optimization may occur in older \(\Lambda(4)\), \(B_2[g]\), or finite Fourier-restriction literature under different notation. Searches for the exact constants, the single repeated-sum hypothesis, and the corresponding extremizer classes did not locate such a statement.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first public 2002-04-18.
2. A. Lewko and M. Lewko, *On the Structure of Sets of Large Doubling*, arXiv:1003.4561, first public 2010-03-24.
