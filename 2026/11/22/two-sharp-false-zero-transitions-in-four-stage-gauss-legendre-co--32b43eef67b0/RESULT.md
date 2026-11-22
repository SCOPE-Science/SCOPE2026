# Two sharp false-zero transitions in four-stage Gauss–Legendre collocation

## Finding

For the positive scalar decay equation \(y'=-\lambda y\) with \(y(0)=1\), consider its **unmodified**, four-stage Gauss–Legendre collocation polynomial on one step of length \(h>0\), with \(x=\lambda h\). Let \(Y_x(t)\), \(0\le t\le1\), be the polynomial evaluated at relative time \(t\). There are exactly two positive transition values \(0<x_1<x_2\), characterized by

\[
 x_1=\sqrt{z_1}=5.154532574215791\ldots,\qquad
 x_2=\sqrt{z_2}=10.24493035684646\ldots,
\]
where \(z_1\in(26,27)\) and \(z_2\in(104,105)\) are the only positive roots of
\[
 F(z)=z^6-180z^5+12180z^4-588000z^3+18110400z^2-460992000z+6453888000.
\]

For \(0\le x<x_1\), \(Y_x\) is strictly positive at every relative time. At \(x=x_1\), it is nonnegative and has one interior double zero, at the **fourth** Gauss node \(c_4\). For \(x_1<x<x_2\), it has exactly two simple zeros in \((0,1)\), enclosing one strictly negative interval. At \(x=x_2\), it also has an interior double zero at the **second** Gauss node \(c_2\), while the first two simple zeros persist. For \(x>x_2\), it has exactly four simple zeros in \((0,1)\), enclosing two disjoint strictly negative intervals. The step-end output \(Y_x(1)\) nevertheless remains strictly positive for **every** finite \(x\ge0\).

In particular, **the exact positivity interval for the entire raw collocation polynomial is \(0\le x\le x_1\)**, although the endpoint has no positivity restriction. The failure creates one, then two pairs of false zero-crossing events for a strictly positive exact solution. The claim is limited to scalar decay and this particular four-stage raw collocation polynomial.

## Assumptions and scope

Let \(\lambda>0\), \(h\ge0\), \(x=\lambda h\). The exact initial condition is positive and normalized to \(1\); any other positive initial value simply multiplies all values. The four Gauss nodes are the distinct zeros of the shifted Legendre polynomial
\[
 L_4(t)=70t^4-140t^3+90t^2-20t+1.
\]
Ordered from left to right, they are
\[
 c_{1,4}=\frac{1\mp\sqrt{(3+2\sqrt{6/5})/7}}2,
 \qquad c_{2,3}=\frac{1\mp\sqrt{(3-2\sqrt{6/5})/7}}2.
\]
Here \(Y_x\) is the unique real polynomial of degree at most four satisfying
\(Y_x(0)=1\) and the four collocation equations
\(Y'_x(c_i)=-xY_x(c_i)\). This is the *raw collocation extension*, not a separate Hermite or spline quasi-interpolant.

## Proof

**1. Explicit polynomial and endpoint.** Set
\[
 D(x)=x^4+20x^3+180x^2+840x+1680,
\]
\[
\begin{aligned}
P(x,t)={}&D(x)
 +t(-20x^4-180x^3-840x^2-1680x)\\
 &+t^2(90x^4+420x^3+840x^2)\\
 &+t^3(-140x^4-280x^3)+70t^4x^4.
\end{aligned}
\]
Direct expansion gives \(P(x,0)=D(x)\) and
\[
 \partial_tP(x,t)+xP(x,t)=x^5 L_4(t).
\]
Because \(D(x)>0\) for \(x\ge0\), the polynomial \(Y_x(t)=P(x,t)/D(x)\) satisfies every collocation condition and the initial condition. Uniqueness follows from Gaussian quadrature positivity: if \(V\) is the difference of two degree-at-most-four solutions, \(V(0)=0\) and \(V'(c_i)+xV(c_i)=0\). The four-node Gauss rule has positive weights \(b_i\) and is exact through degree seven. Multiplying each equation by \(b_iV(c_i)\) and summing gives \[\frac{V(1)^2}{2}+x\sum_{i=1}^4b_iV(c_i)^2=0.\] For \(x>0\), every term is nonnegative, so \(V(c_i)=0\) for all four nodes; together with \(V(0)=0\), this forces \(V\equiv0\). For \(x=0\), the same collocation equations imply \(V'\equiv0\), and the initial condition again gives \(V\equiv0\). At the endpoint,
\[
 P(x,1)=x^4-20x^3+180x^2-840x+1680
       =(x^2-10x+30)^2+20(x-6)^2+60>0.
\]
Thus the completed step is positive for all \(x\ge0\).

**2. Collision polynomial and exact root count.** A root can enter or leave the open time interval only through a zero at an endpoint or an interior repeated root. Both endpoint values are always positive. The exact time-variable discriminant is
\[
 \operatorname{disc}_tP=6048000\,x^{12}F(x^2).
\]
The exact Sturm sequence of \(F\), evaluated at \(z=0,26,27,104,105,+\infty\), has respective sign-variation counts \(4,4,3,3,2,2\). Thus \(F\) has *exactly* two positive roots, with one in each stated rational interval, and neither is repeated. No triple time-root occurs at either threshold: an exact elimination gives
\[
 \operatorname{Res}_t(P_t,P_{tt})
 =-8467200000\,x^{14}(x^2-56)(x^4-28x^2+784).
\]
The last factor is strictly positive on the real line and \(F(56)\ne0\). Therefore at each nonzero discriminant threshold exactly one pair of simple time-roots collides into one double time-root.

Sturm counts for \(P(x,\cdot)\) at the rational test parameters \(x=1,6,12\) give \((V(0),V(1))=(2,2),(3,1),(4,0)\), respectively. Thus the root counts on \((0,1)\) are \(0,2,4\). As \(x\) varies, no additional crossing is possible away from the two discriminant thresholds. Consequently the counts are \(0\), \(2\), and \(4\) throughout the three open parameter regions, and only the respective described double zeros occur at the thresholds.

**3. The collision sites and negative intervals.** The identity in step 1 implies
\[
 \frac{d}{dt}\big(e^{xt}Y_x(t)\big)
 =\frac{x^5e^{xt}}{D(x)}L_4(t).
\]
Hence \(e^{xt}Y_x\) is strictly monotone between successive Gauss nodes for \(x>0\). Any interior double zero of \(Y_x\) is therefore at a Gauss node. Exact algebraic sign tests at the four nodes in order give
\[
\begin{array}{c|c}
 x & \operatorname{sgn}(P(x,c_1),P(x,c_2),P(x,c_3),P(x,c_4))\\\hline
 1 & (+,+,+,+)\\
 6 & (+,+,+,-)\\
 12 & (+,-,+,-)
\end{array}
\]
Together with the unique collisions and root counts, these signs identify the first zero as the minimum at \(c_4\) and the second as the minimum at \(c_2\). They also locate the one, then two, negative intervals, each bounded by simple zeros, and establish the exact nonnegative frontier including the first equality case.

**4. A general collocation check principle.** For any scalar decay collocation polynomial on ordered nodes \(0<c_1<\dots<c_s<1\), the residual \(Y'+xY\) is a constant times \(\prod_i(t-c_i)\). Thus the integrating-factor product \(e^{xt}Y(t)\) is monotone on each of the \(s+1\) intervals cut out by the Gauss nodes. It follows, without an assumption of global monotonicity of \(Y\), that the full polynomial is nonnegative if and only if its values at \(0,c_1,\dots,c_s,1\) are nonnegative. This lemma applies in particular to the four-stage classification.

## Verification

The standalone file `verify.py` checks the exact polynomial residual, positivity sum-of-squares endpoint identity, discriminant factorization, Sturm sign tables and rational isolating intervals for both positive roots, the two critical-node sign changes, and the exact root counts at \(x=1,6,12\). It also checks the elimination condition excluding triple roots. Numerical root values are reported for orientation only; the infinite parameter-range conclusions follow from the exact Sturm and continuity arguments. Run with `python verify.py` and a compatible installed version of SymPy.

## Relationship to prior work

The classical Gauss collocation equations and the positive scalar \([4/4]\) diagonal Padé endpoint are standard. The 2023 paper by Falini, Mazzia and Sestini discusses the raw collocation polynomial and higher-accuracy spline quasi-interpolated dense output, with the Gauss–Legendre examples of two and three stages. Its Section 5.2 does not give a four-stage scalar-decay all-time positivity frontier or a two-threshold false-zero classification. The 2016 work by Ketcheson, Lóczi, Jangabylova and Kusmanov analyzes SSP dense-output constraints for other Runge–Kutta families; its nonexistence results require an SSP property across broader problems and do not imply this scalar four-stage phase diagram. General positivity-preserving adaptive Runge–Kutta strategies are distinct from an exact sign census for a fixed unmodified collocation extension. Related published finite-stage Gauss Markov-positivity calculations concern completed propagators or specific internal stages of different systems and do not assert the present four-stage scalar dense-output root-count theorem. No claim of complete historical-priority certification is made.

## Limitations

The result concerns one step, scalar linear decay, exact arithmetic and a specifically normalized raw four-stage Gauss collocation polynomial. It does not establish invariant-domain preservation for nonlinear/vector differential equations, sensitivity to roundoff, positivity of separately constructed spline dense-output formulas, or relative error bounds at very large steps. Numerical approximations to the two algebraic thresholds are not substitutes for their exact definitions. Published-equivalence risk remains despite searches of pertinent literature and related findings; independent audit has not been performed.

## References

1. A. Falini, F. Mazzia and A. Sestini, “Hermite–Birkhoff spline Quasi-Interpolation with application as dense output for Gauss–Legendre and Gauss–Lobatto Runge–Kutta schemes,” *Applied Numerical Mathematics* 200 (2024), 273–285. First publicly online 28 July 2023. https://doi.org/10.1016/j.apnum.2023.07.023
2. D. I. Ketcheson, L. Lóczi, A. Jangabylova and A. Kusmanov, “Dense output for strong stability preserving Runge–Kutta methods,” arXiv:1605.02429 (2016). https://arxiv.org/abs/1605.02429
3. S. Nüßlein, H. Ranocha and D. I. Ketcheson, “Positivity-Preserving Adaptive Runge-Kutta Methods,” arXiv:2005.06268 (2020). https://arxiv.org/abs/2005.06268
