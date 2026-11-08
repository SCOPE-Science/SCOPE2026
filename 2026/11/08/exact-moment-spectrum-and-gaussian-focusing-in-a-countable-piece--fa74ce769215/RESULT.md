# Exact moment spectrum and Gaussian focusing in a countable piecewise isometry

## Finding

For the countable dyadic-strip piecewise translation introduced in Blank's Example 4.1 [1], its qualitative concentration on a non-invariant torus segment admits the following exact quantitative description. Let \(m\) be normalized area on \(\mathbb T^2\), let \(m_t=T^t_*m\), and let \(\nu=\delta_0\otimes m_{\mathbb T}\). Set \(d_t=1-x_t\) for a trajectory whose first coordinate lies in \((0,1)\), and define \(M_s(t)=\int d_t^s\,dm\).

**Exact moment law.** For every real \(s>0\),
\[
M_s(0)=\frac1{s+1},\qquad
M_s(1)=\frac{(3/2)^{s+1}-(1/2)^{s+1}}{(s+1)(2^{s+1}-1)},
\]
\[
M_s(t)=2^{-(s+1)}\bigl(M_s(t-1)+M_s(t-2)\bigr)\qquad(t\ge2).
\]
In particular, the exact exponential moment rate for each \(s>0\) is
\[
\lim_{t\to\infty}M_s(t)^{1/t}=\lambda_s^+
=\frac{1+\sqrt{1+2^{s+3}}}{2^{s+2}}.
\]
This is an equality of actual moments, not a bound based on finite simulation.

**Almost-sure and fluctuation laws.** Under initial normalized area, for almost every initial point,
\[
\lim_{t\to\infty}\frac{-\log_2 d_t}{t}=\frac23,
\]
while in distribution over the initial point,
\[
\frac{-\log_2d_t-2t/3}{\sqrt t}
\ \Longrightarrow\ \mathcal N\!\left(0,\frac{2}{27}\right).
\]

**Sharp measure-concentration law.** On the torus with the standard geodesic Euclidean distance, for all integers \(t\ge2\), the transport distance to the non-invariant limiting measure is precisely
\[
W_1(m_t,\nu)=M_1(t)
=A\left(\frac{1+\sqrt{17}}8\right)^t
+B\left(\frac{1-\sqrt{17}}8\right)^t,
\]
where
\[
A=\frac14+\frac{13\sqrt{17}}{204},\qquad
B=\frac14-\frac{13\sqrt{17}}{204}.
\]
Thus the exact annealed concentration rate \((1+\sqrt{17})/8\) is strictly larger than the typical-orbit factor \(2^{-2/3}\). This separates moment decay from the Lyapunov-like rate of a typical orbit although every branch of \(T\) is an isometry.

## Assumptions and scope

Identify \(\mathbb T^2\) with \([0,1)^2\), and write \(X_j=(1-2^{1-j},1-2^{-j}]\times[0,1)\) for \(j\ge1\). For \((x,y)\in X_j\), let
\[
T(x,y)=\bigl(x+2^{-j-1},y\bigr),
\]
with the first coordinate understood modulo one, although no wrap occurs on these strips. The exceptional vertical circle \(x=0\) is omitted by the displayed countable partition; for a definite single-valued extension use \(T(0,y)=(1/4,y)\). Changing this assignment on the null exceptional circle does not affect statements for \(m\)-distributed initial points or the pushforwards \(m_t\). It does affect whether the limiting measure \(\nu\) is invariant: under the chosen extension it is not.

All moment assertions concern real \(s>0\) and integer \(t\ge0\); the almost-sure law and central limit theorem concern \(m\)-random initial points. The transport identity concerns \(t\ge2\) and \(W_1\) for the geodesic Euclidean metric on \(\mathbb T^2\). The initial density is exactly normalized Lebesgue area; no claim is made for arbitrary singular initial laws.

## Proof

**1. Exact Bernoulli renewal coding.** Let \(J_0=j\) be the strip label of the initial point. The strip lengths give \(\Pr(J_0=j)=2^{-j}\). Conditional on \(J_0=j\), let
\[
u=2^j(1-x_0)\in[1,2),\qquad v=u-1\in[0,1).
\]
Then \(u\) is uniform on \([1,2)\), independent of \(J_0\). If \(v<1/2\), one iteration decreases the distance to the right boundary by \(2^{-j-1}\), moves from strip \(j\) to \(j+1\), and sends \(v\) to \(2v\). If \(v\ge1/2\), the first iteration stays in strip \(j\), the next moves to strip \(j+1\), and the new normalized coordinate is \(2v-1\). Equality at \(v=1/2\) and dyadic endpoints affects only a null set; the tie is assigned consistently by the stipulated half-open strips.

The new normalized coordinate after every strip gain is therefore \(2v\pmod1\). The successive binary digits \(\varepsilon_i\in\{0,1\}\) of a Lebesgue-uniform \(v\) are independent fair Bernoulli variables. Each gain of one strip index takes exactly \(W_i=1+\varepsilon_i\) iterations. Write \(S_k=\sum_{i=1}^kW_i\) and \(K_t=\max\{k:S_k\le t\}\). It follows that
\[
J_t=J_0+K_t,\qquad
2^{-J_t}\le d_t<2^{1-J_t}.
\]
The last inequality holds both during a one-step gain and during the intermediate step of a two-step gain.

**2. Exact moment recurrence.** Fix \(j\) and define \(g_s(t)\) to be the mean of \(\bigl(2^jd_t\bigr)^s\) over a uniform normalized initial \(u\in[1,2)\). The first step always sends \(u\) to \(u-1/2\), hence direct integration yields
\[
g_s(0)=\int_1^2u^s\,du=\frac{2^{s+1}-1}{s+1},\qquad
g_s(1)=\int_1^2(u-1/2)^s\,du
=\frac{(3/2)^{s+1}-(1/2)^{s+1}}{s+1}.
\]
Split the uniform initial \(u\) into the two half-intervals corresponding to \(\varepsilon_1=0,1\). On each half the renormalized coordinate after one strip gain is again uniformly distributed on \([1,2)\), and the physical distance is scaled by \(1/2\). The required elapsed time is respectively one or two steps. For every integer \(t\ge2\),
\[
g_s(t)=\frac{2^{-s}}2\bigl(g_s(t-1)+g_s(t-2)\bigr).
\]
The conditional moment in strip \(j\) is \(2^{-js}g_s(t)\). Averaging over \(J_0\) gives
\[
M_s(t)=\sum_{j=1}^\infty2^{-j}2^{-js}g_s(t)
=\frac{g_s(t)}{2^{s+1}-1},
\]
which proves the initial conditions and recurrence, including all real \(s>0\).

The roots of \(\lambda^2=2^{-(s+1)}(\lambda+1)\) are
\[
\lambda_s^\pm=\frac{1\pm\sqrt{1+2^{s+3}}}{2^{s+2}}.
\]
They satisfy \(0<|\lambda_s^-|<\lambda_s^+<1\). Writing \(M_s(t)=A_s(\lambda_s^+)^t+B_s(\lambda_s^-)^t\), the leading coefficient is
\[
A_s=\frac{M_s(1)-\lambda_s^-M_s(0)}{\lambda_s^+-\lambda_s^-}>0.
\]
Thus no cancellation can remove the leading root. At \(s=1\), the displayed values of \(A,B\) follow by substituting \(M_1(0)=1/2\), \(M_1(1)=1/3\).

**3. Almost-sure rate and central limit law.** Since \(W_i\) are independent with mean \(3/2\) and variance \(1/4\), the strong law for \(S_k\), inversion, and \(J_t=J_0+K_t\) give \(K_t/t\to2/3\) almost surely. Inverting the standard central limit theorem for the strictly increasing \(S_k\) gives
\[
\frac{K_t-(2/3)t}{\sqrt t}
\Longrightarrow \mathcal N\!\left(0,\frac{\operatorname{Var}(W_1)}{\mathbb E(W_1)^3}\right)
=\mathcal N\!\left(0,\frac{2}{27}\right).
\]
For completeness, the inversion follows by rewriting \(\{K_t\ge k\}=\{S_k\le t\}\) with \(k=\lfloor(2/3)t+z\sqrt t\rfloor\) and using the ordinary iid central limit theorem; this yields the stated variance and Gaussian distribution function. As \(-\log_2d_t-J_t\) is bounded between \(-1\) and \(0\), and \(J_0\) is finite almost surely, both conclusions transfer from \(K_t\) to \(-\log_2d_t\).

**4. Exact transport identity.** Every initial point outside the null exceptional circle reaches a strip of index at least two by time two, and later indices only increase. Consequently \(x_t\ge1/2\) for \(t\ge2\), and its geodesic distance on \(\mathbb T\) from \(0\) equals \(d_t=1-x_t\). Since \(T\) leaves \(y\) unchanged, the coupling \((x_t,y)\mapsto(0,y)\) of \(m_t\) and \(\nu\) incurs exactly mean cost \(M_1(t)\). Conversely, the function \(\phi(x,y)=\operatorname{dist}_{\mathbb T}(x,0)\) is one-Lipschitz and vanishes \(\nu\)-almost everywhere; its expectation under \(m_t\) is \(M_1(t)\). The primal and dual estimates coincide, proving equality. Finally \(T_*\nu=\delta_{1/4}\otimes m_{\mathbb T}\ne\nu\) for the chosen exceptional assignment. The resulting positive coefficient \(A\) and unequal bases show the claimed difference between typical and moment rates. Strictness follows from \(2^{-2/3}<16/25<(1+\sqrt{17})/8\): the first inequality holds after cubing, since \(4\cdot4096>15625\), and the second follows from \(17\cdot625>103^2\).

## Verification

The standalone exact-arithmetic script `verify_focusing.py` computes \(M_s(t)\) independently by integrating each piecewise translation over all dyadic cylinders of depth \(t\), then sums exactly over all starting strips. It checks the result against the renewal recurrence for \(s\in\{1,2,3,4\}\) and \(0\le t\le10\). It independently tests strip-gain clocks against binary digits at rational starting points, and checks the right-half-plane condition used by the transport argument. Execute `python3 verify_focusing.py` from the directory containing this file. The finite tests corroborate the exact algebra only; the proof above establishes all real moment orders, all times, and the limiting laws.

## Relationship to prior work

Blank [1, Example 4.1] gives exactly this countably partitioned torus translation and proves qualitative focusing onto a segment whose forward image leaves the segment. The original paper does not supply a renewal representation, a moment recurrence or spectrum, a central limit law for the focusing rate, or a quantitative transport distance. Blank [2, Section 4] studies weak ergodicity without invariant measures in other examples, not this dyadic map or these quantitative identities. The Bernoulli renewal central limit theorem and elementary optimal-transport duality used in the proof are standard mathematical tools, not newly claimed general theorems. The contribution is their exact coupling to the particular noncontracting, countably piecewise-isometric dynamical system, producing the all-order moment and sharp transport formulas.

## Limitations

The countable partition is essential to this example: no analogous classification for arbitrary finite-partition piecewise isometries is asserted. The Gaussian law concerns randomness in the initial Lebesgue point, not stochastic perturbations of the deterministic dynamics. The moment identities concern \(d_t\), while the transport identification is asserted only for \(t\ge2\), when that distance equals torus geodesic distance. The non-invariance of the limit requires a boundary assignment moving \(x=0\) away, as specified. A full exhaustive priority search across unindexed publications has not been performed; no independent mathematical audit is claimed.

## References

[1] M. Blank, *Invariant measures of torus piecewise isometries*, arXiv:2106.16021, first posted 2021-06-30, Example 4.1. https://arxiv.org/abs/2106.16021

[2] M. Blank, *Ergodic averaging with and without invariant measures*, arXiv:1709.06327, first posted 2017-09-19, Section 4. https://arxiv.org/abs/1709.06327
