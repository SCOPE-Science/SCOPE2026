# A common certified Farey-parent window for all eleventh rotations

## Finding

Consider the exponential-odds-smoothing (EOS) maps
\[
 F_{a,b}(s)=s+b-\frac{1}{1+e^{-as}},\qquad a>0,\quad 0<b<1.
\]
At the **exact rational parameter** \(a=833/10\), and for each \(b=k/11\), \(1\leq k\leq10\), there exists **exactly one attracting periodic orbit**, which is hyperbolic, and its **least period** is, in increasing order of \(k\),
\[
 (10,6,7,8,9,9,8,7,6,10).
\]
For \(k=1,2,3,4,5\) the numbers of strictly positive orbit points are respectively \((1,1,2,3,4)\), so their positive-point fractions are
\[
 \frac1{10},\quad \frac16,\quad\frac27,\quad\frac38,\quad\frac49.
\]
Each fraction is the Farey parent of \(k/11\) with the larger denominator. The other five cases are obtained by reflection, with positive-point fractions \((5/9,5/8,5/7,5/6,9/10)\). Moreover, there exists \(\varepsilon>0\) such that the same assertion, including uniqueness and the indicated least periods, holds simultaneously for **every** \(a\) in \((833/10-\varepsilon,833/10+\varepsilon)\) and every \(b=k/11\), \(1\le k\le10\). No numerical value of \(\varepsilon\) is claimed.

This is a rigorous, rationally certified finite-parameter realization of the simultaneous Farey-parent window observed numerically in Section 5 of Bielawski–Chotibut–Falniowski–Misiurewicz–Piliouras (2024); that numerical observation is acknowledged as prior work.

## Assumptions and scope

All dynamics are on the full real line for \(F_{a,b}\), or equivalently on the open interval for the conjugate map
\[
 f_{a,b}(x)=\frac{x}{x+(1-x)e^{a(x-b)}},\qquad 0<x<1,
\]
via \(x=(1+e^{-as})^{-1}\). An *attracting periodic orbit* means one having an open basin of attraction; *hyperbolically attracting* means that the derivative of its least-period return has modulus strictly less than one. The endpoints \(0\) and \(1\) of the extension of \(f_{a,b}\) are repelling fixed points, not additional attracting cycles. The claim does **not** exclude other repelling periodic points or chaotic invariant sets, nor assert that all starting points converge to the attracting cycle.

## Proof

**1. An exact rational enclosure of the exponential.** Work with fixed denominator \(S=10^{55}\). An integer pair \((L,U)\) represents the closed rational interval \([L/S,U/S]\). Every primitive arithmetic operation in `verify_eos.py` rounds its lower endpoint downward and its upper endpoint upward. For nonnegative rational \(z\), choose the least integer \(h\ge0\) with \(z/2^h\le1/2\), evaluate the nonnegative Taylor terms of \(e^{z/2^h}\) through degree \(55\) using interval arithmetic, add one unit of the enclosing denominator to the upper bound, and square \(h\) times. The Taylor remainder is bounded by
\[
 2(1/2)^{56}/56!<10^{-55}.
\]
Thus every returned interval contains the exact exponential; negative arguments use its reciprocal. The sigmoid and its derivative are consequently enclosed without floating-point operations.

**2. Five rigorous contracting return boxes.** Put \(a=833/10\) and \(b=k/11\). For \(k=1,\ldots,5\), define \(n_k=(10,6,7,8,9)_k\), and closed rational intervals \(J_k=[c_k-10^{-13},c_k+10^{-13}]\), where
\[
\begin{aligned}
 c_1&=0.0259590514290001113607894,\\
 c_2&=0.0526797410255004507704518,\\
 c_3&=0.2077771717296020928651274,\\
 c_4&=0.2986863240202197734575438,\\
 c_5&=-0.4805045058691037711644633.
\end{aligned}
\]
Each decimal is a **terminating rational number**, not an approximate real-input specification. The checker encloses each image \(F^j(J_k)\) through \(j=n_k\) by the interval mean-value bound
\[
 F(I)\subset F(c)+F'(I)(I-c),\qquad c=\tfrac12(\inf I+\sup I),
\]
where derivative intervals use the monotonicity of \(\sigma(as)(1-\sigma(as))\) on the two half-lines. It proves the strict inclusions \(F^{n_k}(J_k)\subset\operatorname{int}J_k\), and proves the enclosed derivative product satisfies \(-1<(F^{n_k})'<1\) on \(J_k\). In fact all five return-multiplier enclosures lie strictly between \(0.0605\) and \(0.0644\). The contraction theorem gives a unique attracting fixed point of \(F^{n_k}\) inside each \(J_k\).

The same checker proves that the \(n_k\) phase intervals \(J_k,F(J_k),\ldots,F^{n_k-1}(J_k)\) are pairwise disjoint, none meets zero, and exactly \((1,1,2,3,4)_k\) are strictly positive. The cycles therefore have **least**, not merely dividing, period \(n_k\). The exact identities \(\lvert 11p_k-kn_k\rvert=1\) and \(n_k>11-n_k\) identify the larger-denominator Farey parents.

**3. Capturing both critical points and excluding other sinks.** For \(a>4\), the two critical points of \(F_{a,b}\) are opposite simple roots of
\[
 1-a\sigma(as)(1-\sigma(as))=0,
 \qquad \sigma(z)=(1+e^{-z})^{-1}.
\]
The checker proves that the negative and positive critical points both lie in rational intervals of radius \(10^{-35}\) about respectively
\[
 -0.052797055092220912165465066376786927
 \quad\text{and}\quad
 +0.052797055092220912165465066376786927.
\]
Each critical interval is propagated, with exact outward enclosures, until its image lies strictly inside one of the \(n_k\) contracting phase intervals. For \(k=1,2,3,4,5\) the certified entrance times, negative critical point first, are
\[
 (61,104),\quad(162,48),\quad(43,117),\quad(49,214),\quad(126,55).
\]
These are rigorous *upper bounds on capture time*, not assertions that earlier captures cannot occur.

The conjugate interval map \(f_{a,b}\) has negative Schwarzian for \(a>4\), as proved in Chotibut–Falniowski–Misiurewicz–Piliouras (2018), Proposition 3.2. In particular, for \(a=833/10\) its two critical points are exactly those just captured by the same attracting orbit. The negative-Schwarzian critical-basin theorem states that each attracting or neutral cycle must have a critical point in its immediate basin, or be an attracting boundary cycle. Both interval endpoints are repelling, because their derivatives are \(e^{ab}>1\) and \(e^{a(1-b)}>1\). The two available critical points both belong to the basin of the **one** constructed sink, so there can be no further attracting or neutral periodic orbit. The conjugacy transfers this uniqueness to \(F\) on \(\mathbb R\).

**4. The remaining numerators and the common open window.** The identity
\[
 F_{a,1-b}(-s)=-F_{a,b}(s)
\]
is exact, so the five cases \(k=6,\ldots,10\) have the same least periods, reflected cyclic phase sets, and unique hyperbolic sinks. Every inclusion, derivative bound, phase separation and critical-capture inequality in Steps 2–3 is strict and involves only finitely many continuous functions of \(a\); the critical points also depend continuously on \(a\) near \(833/10\). Therefore all checks remain valid simultaneously on some common open interval about \(833/10\). The 2018 Schwarzian inequality remains valid there since \(a>4\).

## Verification

The complete standalone `verify_eos.py` program is part of this package. Run it using Python 3 and the standard library only. It prints five `CERT` entries with the period, rational-inclusion intervals rendered for readability, return-derivative enclosure and two critical-point capture times, followed by `FIVE_FAREY_PARENT_CYCLES_AND_SINGER_BASINS_CERTIFIED`. **All logical decisions use exact integer/rational arithmetic; floating-point numbers appear only in diagnostic printing.** The finite enumeration certifies five specific rational return boxes and finite critical orbits; the infinite dynamical conclusions require the contraction and negative-Schwarzian arguments in the proof. The explicit Taylor remainder bound provides the transcendental input. The reflected cases and common open interval follow analytically.

## Relationship to prior work

Bielawski et al. (2024), *Interval maps mimicking circle rotations*, Theorem 3.3 and Sections 4–5, established the existence of attracting period-eleven orbits for sufficiently large \(a\) and **numerically observed** the common earlier Farey-parent windows for \(b=k/11\), including the specific illustrative choice \(a=83.3, b=3/11\) (their Figure 6). They explicitly did not rigorously prove those observed finite-parameter windows. The novel assertion here is an *exact open-parameter certification with unique sinks and all ten numerators*, not the empirical sighting, original map, Farey arithmetic or the negative-Schwarzian theorem. Chotibut et al. (2018) established the negative-Schwarzian and critical-point basin facts used above.

Related published results on strong-smoothing \(a\to\infty\) half-grid selection concern period-eleven orbits in the large-\(a\) regime and do not imply the finite \(a=833/10\) shorter-period coexistence across parameters. A published exact finite-parameter certificate under another parametrization is still a priority risk to be checked by further independent literature review.

## Limitations

The proof provides existence but not a numerical width for the common open \(a\)-interval. It does not determine the complete parameter windows, exclude repelling cycles or chaotic invariant subsets, prove pointwise global convergence, or certify any other denominators. The time counts for capturing critical points are bounded stopping times rather than minimal entrance times. The independent mathematical audit has not been performed.

## References

1. J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Interval maps mimicking circle rotations* (2024), arXiv:2411.01495v1, https://arxiv.org/html/2411.01495v1 , especially Sections 4–5 and Figures 5–6.
2. T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Family of chaotic maps from game theory* (2018), arXiv:1807.06831, https://arxiv.org/abs/1807.06831 , especially Proposition 3.2 and its negative-Schwarzian critical-basin consequence.
3. D. Singer, *Stable orbits and bifurcation of maps of the interval*, SIAM Journal on Applied Mathematics 35 (1978), 260–267 (negative-Schwarzian attracting-cycle theorem, used through [2]).
