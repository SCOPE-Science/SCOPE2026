# Sharp dyadic quasiperiod collapse for rational axis cross-polytopes

## Finding
For any integer \(d\ge1\) and positive integer weights \(a_1,\ldots,a_d\), set
\[
P(a)=\operatorname{conv}\{\pm e_i/a_i:1\le i\le d\}
=\{x\in\mathbb R^d:\sum_{i=1}^d a_i|x_i|\le1\}.
\]
Write \(L_a(q)=\#(qP(a)\cap\mathbb Z^d)\) for integers \(q\ge0\). For every integer \(m>1\), let
\[
\epsilon_m(a)=\#\{i:m\mid a_i\}-
\begin{cases}
\#\{i:a_i\equiv m/2\pmod m\},&m\text{ even},\\
0,&m\text{ odd}.
\end{cases}
\]
Then the **minimum** Ehrhart quasiperiod of \(L_a\) is exactly
\[
\operatorname{lcm}\{m>1:\epsilon_m(a)>0\},
\]
where the least common multiple of the empty set is one. Only finitely many \(m\) contribute, and each contributing \(m\) divides some \(a_i\).

In particular, \(L_a\) is an ordinary polynomial if and only if **both** of the following hold: every \(a_i\) is a power of two; and, writing \(c_j=\#\{i:a_i=2^j\}\),
\[
c_{j-1}\ge\sum_{k\ge j}c_k\quad\text{for every integer }j\ge1.
\]
This is a complete criterion across all positive integer weight vectors.

If the polynomiality criterion holds and \(\max_i a_i=2^r\) with \(r\ge1\), necessarily \(d\ge2^r\). Equality occurs, up to permutation, for exactly one weight vector: \(c_r=1\) and \(c_j=2^{r-j-1}\) for \(0\le j<r\). For this extremal family, \(d=2^r\) and
\[
\sum_{q\ge0}L_a(q)z^q=\frac{1+z^d}{(1-z)^{d+1}},\qquad
L_a(q)=\binom{q+d}{d}+\binom qd.
\]
In particular, for \(r\ge1\) this ordinary polynomial is **not** the Ehrhart polynomial of any lattice polytope of any dimension. The extremal examples have arbitrarily large vertex denominator and normalized volume two.

## Assumptions and scope
The standard lattice is \(\mathbb Z^d\); all weights are strictly positive integers, and the polytope is a full-dimensional centrally symmetric rational cross-polytope. The quasiperiod is the least positive period of the coefficient functions of the Ehrhart quasipolynomial on **all** nonnegative integral dilations. The vertex denominator is \(\operatorname{lcm}(a_1,\ldots,a_d)\). The polynomiality statement includes \(d=1\), while the rigidity bound concerns maximum weight greater than one.

## Proof
**Generating series.** A signed integer coordinate of absolute value \(s\) contributes weight \(a_i s\), with multiplicity one at \(s=0\) and two at every \(s>0\). Adding a nonnegative slack integer shows directly that
\[
F_a(z):=\sum_{q\ge0}L_a(q)z^q
=\frac{1}{1-z}\prod_{i=1}^d\frac{1+z^{a_i}}{1-z^{a_i}}.\tag{1}
\]
This is also the nonequivariant specialization of the established rational-cross-polytope formula in Uchiumi, Proposition 4.1; equation (1) itself is **not** claimed as new.

**Minimal quasiperiod.** At any primitive \(m\)-th root \(\zeta\) with \(m>1\), each denominator factor \(1-z^{a_i}\) vanishes to order one precisely when \(m\mid a_i\). A numerator factor \(1+z^{a_i}\) vanishes precisely when \(m\) is even and \(a_i\equiv m/2\pmod m\). Thus the order of the pole of \(F_a\) at \(\zeta\) is \(\max\{\epsilon_m(a),0\}\). All poles are roots of unity; \(F_a\) is proper at infinity. Partial fractions imply that its coefficient sequence is a quasipolynomial with period dividing the least common multiple of the orders of its poles, and the converse holds because the generating function of a quasipolynomial of period \(T\) has poles only at \(T\)-th roots of unity. This proves the exact period formula, not merely an upper bound.

**Complete collapse criterion.** If an odd integer \(m>1\) divides a weight, then at a primitive \(m\)-th root a denominator vanishes while no numerator vanishes; therefore polynomiality is impossible. Hence every weight must be a power of two. Conversely, if all weights are dyadic, all possible nontrivial poles have orders \(m=2^j\). Their signed pole orders are
\[
\epsilon_{2^j}(a)=\sum_{k\ge j}c_k-c_{j-1}.
\]
No nontrivial poles remain if and only if all stated inequalities hold. Conversely, a polynomial coefficient sequence has no poles except at one. When all other poles cancel, equation (1) is proper, has its only pole at one with order \(d+1\), and so has the form \(H(z)/(1-z)^{d+1}\) for a polynomial \(H\) of degree at most \(d\). Coefficient extraction makes \(L_a(q)\) a polynomial in \(q\) for every \(q\ge0\), including the initial dilations.

**Sharp dimension and extremizer.** Assume the maximum weight is \(2^r\) and put \(t_j=\sum_{k\ge j}c_k\), so \(t_0=d\), \(t_r=c_r\ge1\). The collapse inequalities are equivalent to \(t_{j-1}\ge2t_j\) for \(1\le j\le r\). Iterating gives \(d=t_0\ge2^rt_r\ge2^r\). Equality forces \(c_r=1\) and equality at every intermediate step, yielding the unique multiplicities \(c_j=2^{r-j-1}\) for \(j<r\).

For these multiplicities apply \((1+z^{2^j})/(1-z^{2^j})=(1-z^{2^{j+1}})/(1-z^{2^j})^2\) to equation (1). Every intermediate factor cancels, leaving \((1+z^{2^r})/(1-z)^{2^r+1}\). Since \(d=2^r\), coefficient extraction yields the claimed binomial sum. Its numerator evaluates to two at one, proving normalized volume two.

**Failure of lattice realization.** Suppose a \(d\)-dimensional lattice polytope had the same Ehrhart polynomial for \(d=2^r\ge2\). Its ordinary Ehrhart numerator would be \(1+z^d\). The zero coefficient of \(z\) implies it has exactly \(d+1\) lattice points altogether at dilation one, whereas its top numerator coefficient one forces exactly one interior lattice point by Ehrhart reciprocity. Every full-dimensional lattice polytope already has at least \(d+1\) distinct lattice vertices, all on its boundary. This gives at least \(d+2\) lattice points, a contradiction. Any Ehrhart-equivalent lattice polytope must have dimension \(d\), by the polynomial's degree.

## Verification
Run `python3 verify.py` with only the Python standard library. The script checks the cyclotomic and dyadic characterizations on \(1{,}286\) small weight multisets; tests candidate minimum quasiperiods against exact coefficient recurrences; compares direct coordinate enumeration against the recurrence; and verifies the sharp families through exponent \(r=5\) against the binomial formula. It reports \(3{,}955\) successful exact integer assertions. Finite tests corroborate rather than replace the unrestricted proof above.

## Relationship to prior work
Uchiumi (arXiv:2610.41529, first submitted 2026-10-30, revised 2026-11-04) establishes the general generating series (1) and an equivariant numerator-effectiveness theorem. The new result concerns the **minimum** nonequivariant quasiperiod, an exact structural classification of complete collapse, and a **sharp dimension-denominator rigidity theorem** with a unique extremizer. The generating series makes this derivation possible and is explicitly credited; determining its global pole-cancellation patterns and optimizing the multiplicities are separate steps.

Clarke–Higashitani–Kölbl (arXiv:2209.00755, Section 4) already treat the subfamily with \(d-1\) unit weights and one weight two, including its two-dimensional instance, so no novelty is claimed for that subfamily alone. Woods (2005) and McAllister–Woods (2003) provide general period and period-collapse results, including rational polygons; Haase–McAllister (2007) discuss non-lattice-realizable Ehrhart polynomials. The claim here is the **complete weighted-cross-polytope classification** and its dyadic sharp extremal consequence, not the general existence of period collapse or nonrealizability.

## Limitations
This result concerns rational axis cross-polytopes with positive **integer reciprocal-axis denominators**, not arbitrary rational cross-polytopes or affine unimodular transformations of them. It classifies quasiperiods but does not classify all quasipolynomial coefficient functions. Known general generating formulas provide a close route to the theorem; independent literature and priority review could reveal an earlier implicit or explicit classification. No independent mathematical validation is asserted.

## References
1. R. Uchiumi, *Equivariant Ehrhart series for rational simplices and rational cross-polytopes*, arXiv:2610.41529, v1 2026-10-30, v2 2026-11-04, §4.2 and Proposition 4.1. https://arxiv.org/abs/2610.41529
2. O. Clarke, A. Higashitani, M. Kölbl, *The equivariant Ehrhart theory of polytopes with order-two symmetries*, arXiv:2209.00755, 2022, §4. https://arxiv.org/abs/2209.00755
3. K. Woods, *Computing the Period of an Ehrhart Quasi-Polynomial*, Electron. J. Combin. **12** (2005), R34. https://doi.org/10.37236/1931
4. T. B. McAllister, K. M. Woods, *The Minimum Period of the Ehrhart Quasi-polynomial of a Rational Polytope*, J. Combin. Theory Ser. A **109** (2005). https://arxiv.org/abs/math/0310255
5. C. Haase, T. B. McAllister, *Quasi-period collapse and GL_n(Z)-scissors congruence in rational polytopes*, arXiv:0709.4070, 2007. https://arxiv.org/abs/0709.4070
