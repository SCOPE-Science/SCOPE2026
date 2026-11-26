# A sharp global resetting threshold for simple walks on finite cycles

## Finding
For every integer \(m\ge3\), let a nearest-neighbor symmetric random walk start at vertex \(0\) of the cycle \(C_m\), and let its fixed target lie at graph distance \(1\le d\le\lfloor m/2\rfloor\). At each step, independently, with probability \(r\in[0,1)\) the walker returns to vertex \(0\), consuming the entire step, and otherwise moves to either neighboring vertex with equal probabilities. Write \(H_{m,d}(r)\) for its mean first arrival time at the target.

**Sharp global phase theorem.** Writing \(\mu=d(m-d)\), there exists a positive reset probability that strictly improves the mean hitting time if and only if
\[
m^2>5d(m-d)+5.
\]
When this strict inequality holds, all sufficiently small positive reset probabilities improve the mean. Conversely, when \(m^2\le5d(m-d)+5\), **every** \(r\in(0,1)\) strictly increases the mean, including at equality. More precisely,
\[
H_{m,d}(0)=\mu,\qquad H'_{m,d}(0)=\frac{\mu}{6}\bigl(5\mu+5-m^2\bigr).
\]
Thus for this entire family the infinitesimal sign test is also globally decisive: an unfavorable or zero first derivative excludes every improvement at larger reset probabilities. In particular, for an adjacent target \(d=1\), beneficial resetting exists exactly for \(m\ge6\).

## Assumptions and scope
The cycle has \(m\ge3\) labeled vertices, with transition probability \(1/2\) to each of the two neighbors. The target differs from the initial vertex; reflection reduces its distance to \(1\le d\le\lfloor m/2\rfloor\). Each reset **replaces a normal move and costs one discrete time unit**. Reset events are independent over time. For \(r<1\), the mean target-hitting time is finite; at \(r=1\), it is infinite, so that endpoint is excluded. The theorem concerns the mean hitting time for a single target, not a general network or other resetting protocols.

## Proof
Let \(T\) be the target-hitting time with no resetting and \(F(s)=\mathbb E[s^T]\), for \(0<s<1\). Identifying the cycle with an interval of length \(m\) whose two absorbing endpoints represent the same target, the discrete harmonic equation gives
\[
F(s)=\frac{\cosh((m/2-d)t)}{\cosh(mt/2)},\qquad \cosh t=s^{-1}.
\]
Indeed the unique solution of \(f_x=s(f_{x-1}+f_{x+1})/2\), with \(f_0=f_m=1\), is \(f_x=\cosh((x-m/2)t)/\cosh(mt/2)\). Its value at the starting point is the displayed function. Elementary gambler's-ruin differences give \(\mathbb ET=\mu=d(m-d)\).

A renewal at the first reset (each reset consumes one step) gives
\[
H_{m,d}(r)=\frac{1-F(1-r)}{rF(1-r)}\qquad(0<r<1).
\]
For an algebraic form with positive coefficients put \(\epsilon=m\bmod 2\), \(a=\lfloor m/2\rfloor\), \(b=a-d\), and \(w=r/(1-r)=\cosh t-1\). Define polynomials
\[
P_j(w)=\frac{\cosh((j+\epsilon/2)t)}{\cosh(\epsilon t/2)}
=\sum_{k=0}^j c_k(j)w^k,\qquad c_0(j)=1,
\]
with the explicit coefficient recurrence, for \(1\le k\le j\),
\[
c_k(j)=c_{k-1}(j)\,
\frac{j(j+\epsilon)-(k-1)(k-1+\epsilon)}{k(2k-1)}.
\]
All coefficients are strictly positive. To verify the recurrence independently, differentiate the defining hyperbolic function: the polynomial \(P_j(w)\) solves
\[
w(w+2)P_j''(w)+[1+(1+\epsilon)w]P_j'(w)-j(j+\epsilon)P_j(w)=0,\quad P_j(0)=1.
\]
Matching successive powers of \(w\) gives the recurrence and the degree \(j\).

Set \(\alpha=a(a+\epsilon)\), \(\beta=b(b+\epsilon)\); then \(\alpha-\beta=\mu\), \(F(1-r)=P_b(w)/P_a(w)\), and
\[
H_{m,d}(r)-\mu=\frac{N(w)}{wP_b(w)},\quad
N(w)=(1+w)(P_a(w)-P_b(w))-\mu wP_b(w).
\]
The constant and linear terms of \(N\) vanish and, directly from the coefficient recurrence,
\[
[w^2]N=\frac{\mu}{6}(\mu-4\beta+5-\epsilon)
=\frac{\mu}{6}(5\mu+5-m^2).
\]
Since \(w=r+O(r^2)\) and \(P_b(0)=1\), this proves the derivative formula. If this coefficient is negative, the difference is negative for all sufficiently small positive \(r\), proving the improving direction.

It remains to prove a **global** statement when \([w^2]N\ge0\). For \(b=0\) or \(b=1\), all coefficients of \(N\) of degree at least three are nonnegative by inspection of the formula and the fact that \(P_b\) has degree at most one. The degree-two coefficient is nonnegative by assumption, and at least one higher or degree-two coefficient is positive.

Now suppose \(b\ge2\) and \([w^2]N\ge0\). The inequality \(\mu\ge4\beta-5+\epsilon\) forces \(\mu\ge3\beta\), as follows. For \(\epsilon=1\), \(\beta=b(b+1)\ge6\); for \(\epsilon=0\), \(b\ge3\) gives \(\beta=b^2\ge9\); and in the remaining case \(\epsilon=0,b=2\), the assumption demands \(\mu\ge11\), whence \(a\ge4\) and \(\mu=a^2-4\ge12=3\beta\). Therefore \(\alpha/\beta\ge4\).

For \(3\le j\le b+1\), write \(q=(j-1)(j-1+\epsilon)\) and \(D=j(2j-1)\). The recurrence yields
\[
[w^j]N=c_{j-1}(a)\left(1+\frac{\alpha-q}{D}\right)
-c_{j-1}(b)\left(1+\mu+\frac{\beta-q}{D}\right).
\]
The ratio of positive coefficients satisfies
\[
\frac{c_{j-1}(a)}{c_{j-1}(b)}
=\prod_{h=0}^{j-2}\frac{\alpha-h(h+\epsilon)}{\beta-h(h+\epsilon)}
\ge(\alpha/\beta)^{j-1}\ge4^{j-1}>D.
\]
The last strict inequality holds for every integer \(j\ge3\), beginning with \(16>15\) and continuing by induction. On the other hand, because \(q\le\beta\),
\[
\frac{1+\mu+(\beta-q)/D}{1+(\alpha-q)/D}
=1+\frac{\mu(D-1)}{D+\alpha-q}\le D.
\]
Combining the two inequalities proves \([w^j]N>0\) for \(3\le j\le b+1\). For \(j\ge b+2\), the coefficients of \(P_b\) involved vanish, and \([w^j]N=c_j(a)+c_{j-1}(a)\ge0\), interpreting out-of-range coefficients as zero. The highest-degree coefficient \([w^{a+1}]N=c_a(a)>0\). Hence \(N(w)>0\) for every \(w>0\), since all coefficients from degree two onward are nonnegative and at least one is strictly positive. The denominator \(wP_b(w)\) is positive. This proves strict worsening for **every** positive reset probability and completes the classification.

## Verification
Run the standalone `verify.py` using Python 3. It reconstructs the recurrence in exact rational arithmetic, checks its coefficient positivity and the derivative identity for every \(3\le m\le100\) and every admissible \(d\), evaluates the identity at two nonzero rational reset probabilities, and independently solves the finite linear first-hitting-time equations using exact Gaussian elimination for every \(3\le m\le11\) and four reset probabilities. The checks are finite consistency tests only; the coefficient argument above proves the unrestricted assertion.

## Relationship to prior work
Riascos, Boyer, Herringer, and Mateos (arXiv:1910.13568) derive exact network-resetting mean passage times, including spectral ring formulas. Riascos, Boyer, and Mateos (arXiv:2110.15437), Sections 3.2 and 4.1, establish a general **infinitesimal sufficient test** for beneficial discrete-time resetting and numerically determine optima on rings. Bonomo and Pal (arXiv:2102.00895) establish renewal results and a beneficial-restart criterion for discrete confined walks with absorbing endpoints. These prior formulas underpin the setting; the present claim is the explicit arithmetic **if-and-only-if phase line for every finite ring and target distance**, including its global no-advantage assertion at all positive resetting rates and the equality boundary. A general moment criterion alone does not rule out a lower mean at a larger reset probability when the derivative at zero is nonnegative. The new ingredient here is the positive-coefficient proof establishing that exclusion for all finite cycles.

## Limitations
The result does not claim the underlying network MFPT or generic renewal formula as new; it does not characterize the number or uniqueness of interior minimizers when restarting helps, nor the full hitting-time distribution. It excludes zero-time resets, biased or lazy walks, multiple targets, nonuniform graphs, and resets to a point other than the origin. An equivalent phase criterion may be implicit in earlier spectral formulas; independent historical-priority auditing has not been performed.

## References
1. A. P. Riascos, D. Boyer, P. Herringer, J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568 (first submitted 29 October 2019), Section III and Eqs. (15)–(16). https://arxiv.org/abs/1910.13568
2. A. P. Riascos, D. Boyer, J. L. Mateos, *Discrete-time random walks and Lévy flights on arbitrary networks: when resetting becomes advantageous?*, arXiv:2110.15437 (first submitted 28 October 2021), Sections 3.2 and 4.1. https://arxiv.org/abs/2110.15437
3. O. L. Bonomo and A. Pal, *First passage under restart for discrete space and time: application to one dimensional confined lattice random walks*, arXiv:2102.00895 (first submitted 1 February 2021). https://arxiv.org/abs/2102.00895
