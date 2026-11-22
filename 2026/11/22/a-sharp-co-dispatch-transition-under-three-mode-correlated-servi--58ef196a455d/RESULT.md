# A sharp co-dispatch transition under three-mode correlated service outages

## Finding
Consider one guaranteed periodic vehicle and three candidate vehicles whose same-period dispatch statuses belong to four specified, correlated scenarios. The unique timetable minimizing uniformly arriving passengers' mean wait is characterized for **all** positive scenario weights, not merely for a numerical instance.

Let the relative probabilities of the candidate-service patterns be \(u\) (only the first candidate operates), \(v\) (only the last two operate), \(w\) (all three operate), and \(1-u-v-w\) (none operates). Assume \(u,v,w>0\) and \(u+v+w\leq1\). Let \(a,b,c,d\geq0\) be the four consecutive scheduled gap fractions, summing to one, starting immediately after the guaranteed service. Define
\[
Q=3uv+3uw+3vw+2w^2,\qquad H=4u+3v+3w.
\]
If \(uv\geq w(u+v+w)\), the **unique** optimum is
\[
(a,b,c,d)=\left(\frac{2u+v+w}{H},0,\frac{u+v+w}{H},\frac{u+v+w}{H}\right).
\]
Otherwise it is
\[
(a,b,c,d)=\left(\frac{(3u+w)(v+w)}{2Q},
\frac{w(u+v+w)-uv}{2Q},
\frac{(u+w)(2v+w)}{2Q},
\frac{(u+w)(2v+w)}{2Q}\right).
\]
Thus, although the all-operating scenario has strictly positive probability, the first two candidate services are scheduled **at exactly the same instant** throughout the nonempty region \(uv\geq w(u+v+w)\). The boundary is sharp, including equality.

For the equal-weight partial-service regimes \(u=v=(1-w)/2\), with \(0<w<1\), the exact transition is
\[
w_c=3-2\sqrt{2}=0.1715728752538\ldots.
\]
Coincidence is optimal for \(w\leq w_c\); positive spacing is uniquely optimal for \(w>w_c\). With \(u=v=9/20\) and \(w=1/10\), the optimal gaps are \((29,0,20,20)/69\) and mean waiting time is \(29T/138\), compared with \(19T/80\) under equal quarter-period gaps. The reduction is exactly \(151/1311\approx11.5179\%\).

## Assumptions and scope
- Period \(T>0\). The guaranteed service departs at each integer multiple of \(T\). Three optional candidate departures within each cycle occur at cumulative phases \(aT\), \((a+b)T\), and \((a+b+c)T\). The remaining gap to the next guaranteed departure is \(dT\). Zero headways are allowed, and simultaneous departures count as distinct vehicles but as one boarding opportunity.
- In each period, exactly one of the four service-status patterns stated in the finding occurs with the specified probabilities. Arbitrary dependence between the three optional statuses within a period is allowed through this joint law; independence between different periods is not needed for the expected waiting-time calculation.
- Passengers arrive uniformly throughout a full period independently of service status and board the next vehicle that actually operates. Capacity is unlimited, and boarding or transfer time is negligible. Passenger anticipation, nonuniform demand, arrival lateness, fixed minimum headways, and operational costs are not modeled.
- The theorem optimizes the ordering of **labeled** candidates at their specified chronological positions. No permutation of which candidate is used in which operating mode is optimized.

## Proof
**1. A gap-squared identity.** For any fixed operating configuration, partition the period into cyclic intervals between consecutive actual departures. A uniformly arriving passenger falling in an interval of length \(L\) waits on average \(L/2\), and this interval is encountered with probability \(L/T\). Summing yields \(\sum L^2/(2T)\). A guaranteed departure exists every period, so intervals do not depend on earlier operating configurations.

Writing \(F=2W/T\), where \(W\) is expected passenger wait, and using normalized scheduled gaps gives the exact objective
\[
F=u\{a^2+(b+c+d)^2\}+v\{(a+b)^2+c^2+d^2\}
+w(a^2+b^2+c^2+d^2)+(1-u-v-w).
\]
This formula treats simultaneous departures correctly: a zero scheduled gap contributes zero and does not create an additional positive interval.

**2. Symmetry and strict convexity.** The objective is invariant under interchanging \(c\) and \(d\): the first term sees only their sum, while the remaining terms see \(c^2+d^2\). As \(v+w>0\), replacing unequal \(c,d\) by their average strictly reduces \(F\). Thus \(c=d=(1-a-b)/2\). Moreover, the term \(w(a^2+b^2+c^2+d^2)\), with \(w>0\), is strictly convex on the simplex; the other terms are convex squares of linear forms. Hence a unique global minimizer exists.

After substituting \(c=d\), ignoring the constant \(1-u-v-w\), the objective is
\[
F_0(a,b)=\frac12\big[(4u+3v+3w)a^2+(6v+2w)ab
+(3v+3w)b^2-(4u+2v+2w)a-(2v+2w)b+2u+v+w\big].
\]
Its Hessian is the positive-definite matrix
\[
\begin{pmatrix}4u+3v+3w&3v+w\\3v+w&3v+3w\end{pmatrix}.
\]
The feasible triangle is \(a\geq0\), \(b\geq0\), \(a+b\leq1\).

**3. The unconstrained stationary point.** Solving the two linear derivative equations produces
\[
a_I=\frac{(3u+w)(v+w)}{2Q},\quad
b_I=\frac{w(u+v+w)-uv}{2Q},\quad
c_I=d_I=\frac{(u+w)(2v+w)}{2Q}.
\]
Since \(Q>0\), \(a_I,c_I,d_I\) are positive and \(a_I+b_I+2c_I=1\). The point is feasible precisely when \(w(u+v+w)\geq uv\). In that regime strict convexity proves its unique global optimality, including the equality case where \(b_I=0\).

**4. The co-dispatch boundary.** If \(uv>w(u+v+w)\), the stationary point would have \(b_I<0\). Set \(b=0\) and minimize the remaining strictly convex quadratic. The resulting \(a_B=(2u+v+w)/H\) and \(c_B=d_B=(u+v+w)/H\) are positive and sum to one. The derivative toward the interior at this boundary point is
\[
\left.\frac{\partial F_0}{\partial b}\right|_{(a_B,0)}
=\frac{2\{uv-w(u+v+w)\}}{H}>0,
\]
while the tangential derivative is zero. These are the exact Karush–Kuhn–Tucker inequalities on the simplex; strict convexity proves unique global optimality. No other boundary can minimize, as the certified point already satisfies the global convex optimality conditions.

**5. The radical threshold.** Under \(u=v=(1-w)/2\), the boundary inequality becomes \((1-w)^2\geq4w\). On \(0<w<1\), it holds exactly when \(w\leq3-2\sqrt2\). The gap \(b\) changes continuously from zero to positive across this threshold. Direct substitution at \(w=1/10\) gives the quoted rational optimum, exact waiting times, and reduction.

## Verification
Run `python3 verify.py` with Python 3 and no nonstandard dependencies. Its exact `fractions.Fraction` arithmetic checks the stated optimizer, positivity, simplex normalization, stationarity or boundary KKT inequalities, the Hessian determinant, and many feasible competing timetables for 165 distinct rational probability triples. It also checks both stated rational benchmark cases. The executable is supplementary finite evidence, not a replacement for the all-real-parameter convexity and algebraic proof above.

## Relationship to prior work
The basic random-arrival headway-squared waiting-time identity is classical. Zhao, Dessouky and Bukkapatnam (2006) optimize timetable slack under stochastic vehicle travel times; their exposed abstract does not give the discrete correlated service-pattern classification here. Gkiotsalitis (2020), in the accessible full article, develops a constrained bus dispatch formulation with vehicle availability and capacity; the relevant objectives and Sections 3–6 do not formulate the four-mode, exact quadratic classification. Dou and Li (2023), in their accessible full article, optimize timetable coordination under stochastic travel times via sampled mixed-integer programming, rather than prescribed jointly present/absent service outcomes with one guaranteed anchor.

Two earlier mathematical records in this topic establish, respectively, an exact timetable for independently cancelled services and a correlated two-candidate phase optimizer. The independence assumption of the first does not hold for these operating modes, and the two-candidate statement of the second does not cover a guaranteed anchor plus three correlated optional departures. Their results are not claimed again here. The contribution is the complete *three-optional-mode* classification and its positive-cooccurrence co-dispatch phase, not the elementary headway identity or the use of a quadratic program.

## Limitations
This is an exact result for a deliberately simplified correlated-service operating law, not a claim of optimality for arbitrary joint dispatch distributions, arbitrary permutations of labeled services, actual timetables with nonzero minimum headways, capacity constraints, coordinated passenger arrival behavior, delay distributions, or costs. Allowing zero gaps is essential to the exact coincidence regime. The result does not estimate any real service-mode probabilities or demonstrate deployment benefits. More general stochastic scheduling literature might contain an equivalent special case; an independent bibliographic priority assessment has not been performed.

## References
1. J. Zhao, M. Dessouky and S. Bukkapatnam, *Optimal Slack Time for Schedule-Based Transit Operations*, Transportation Science 40 (2006), 529–539, first online 2006-11-01, https://doi.org/10.1287/trsc.1060.0170.
2. K. Gkiotsalitis, *Bus scheduling considering trip-varying travel times, vehicle availability and capacity*, IET Intelligent Transport Systems 14 (2020), 1594–1605, https://doi.org/10.1049/iet-its.2019.0725.
3. X. Dou and T. Li, *Multi-Objective Bus Timetable Coordination Considering Travel Time Uncertainty*, Processes 11 (2023), article 574, https://doi.org/10.3390/pr11020574.
4. Earlier independent-cancellation design result, record `823a3384-8ec8-4e13-a9b3-6a5ef8ed7179`; and correlated two-candidate design result, record `5690be0c-1bb0-4d68-ad4d-4e4598ea12cf` (statement-level comparisons only).
