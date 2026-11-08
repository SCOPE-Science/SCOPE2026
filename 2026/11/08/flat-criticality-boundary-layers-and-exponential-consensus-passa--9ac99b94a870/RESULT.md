# Flat criticality, boundary layers, and exponential consensus passages in a nonlinear two-zealot opinion model

## Finding

The polling-error response introduced for best-of-two collective decision-making gives a sharp, *finite-population* trichotomy when both alternatives have one permanent supporter. For any integer \(m\ge2\) and response exponent \(\alpha>0\), the number \(K\) of A-supporting susceptible agents has an explicit reversible stationary distribution. At \(\alpha=1\) the distribution is **exactly uniform** on \(\{0,\ldots,m\}\). For \(0<\alpha<1\), it has two boundary modes; for \(\alpha>1\), it has a central mode (two adjacent tied modes when \(m\) is odd).

As \(m\to\infty\), its three distinct fluctuation laws are
\[
\begin{aligned}
0<\alpha<1:&&\Pr_\pi(K=j)&\longrightarrow\frac{1-\alpha}{2}\alpha^j\quad(j\ge0\text{ fixed}),\\
\alpha=1:&& K/m&\Rightarrow\operatorname{Unif}[0,1],\\
\alpha>1:&& (K-m/2)/\sqrt m&\Rightarrow\mathcal N(0,1/4).
\end{aligned}
\]
The left boundary limit also holds at the reflected right boundary, \(\Pr_\pi(K=m-j)\to(1-\alpha)\alpha^j/2\). In particular, for \(0<\alpha<1\) the full rescaled limit is \(\frac12\delta_0+\frac12\delta_1\), even though neither boundary state is absorbing for finite \(m\).

Let \(\tau_m\) denote the number of asynchronous susceptible-agent updates until all \(m\) susceptibles support A, starting with none supporting A. Its exact expectation at the critical response is
\[
\boxed{\mathbb E_0\tau_m=m(m+1)H_m,\qquad H_m=\sum_{j=1}^{m}\frac1j.}
\]
For every fixed \(\alpha\ne1\), the same expected passage time is exponentially large:
\[
\boxed{\lim_{m\to\infty}\frac1m\log\mathbb E_0\tau_m
=\Delta_\alpha=\left|\int_0^{1/2}\log\left[\frac{1-x}{x}\,\frac{F_\alpha(x)}{1-F_\alpha(x)}\right]dx\right|>0.}
\]
The endpoint values of the displayed integrand are interpreted continuously, not as undefined logarithms. The formulas refer to *first entrance* at the all-A susceptible state; persistent consensus is impossible with an opposite permanent zealot.

## Assumptions and scope

There are \(m\ge2\) susceptible binary-opinion agents and two fixed zealots, one A and one B, all on the same complete simple undirected graph. Both options have equal quality. At each discrete step, one susceptible is chosen uniformly, independently of the past. If its current opinion is A (respectively B), it switches to B (respectively A) with probability \(F_\alpha(x)\), where \(x\) is the proportion of its *other* agents that support the opposite option. No zealot changes state.

For all \(\alpha>0\), the response function is precisely
\[
F_\alpha(x)=\frac{1+\operatorname{sgn}(2x-1)|2x-1|^\alpha}{2},\qquad 0\le x\le1,
\]
where \(F_\alpha(1/2)=1/2\). It is strictly increasing, \(F_\alpha(1-x)=1-F_\alpha(x)\), and \(F_1(x)=x\). This is a symmetric, equal-quality, two-zealot *extension* of the cited best-of-two model: the initiating zealot paper studies B-only zealots and heterogeneous networks, not the exact symmetric configuration studied here.

Given \(K=k\), the transitions per individual update are
\[
p_k=\frac{m-k}{m}F_\alpha\!\left(\frac{k+1}{m+1}\right),\qquad
q_k=\frac{k}{m}F_\alpha\!\left(\frac{m-k+1}{m+1}\right),
\]
for \(0\le k\le m\), with \(p_m=q_0=0\). The self-loop probability is \(1-p_k-q_k\). The state space is the integers from \(0\) to \(m\), not a diffusion approximation.

## Proof

**(1) Reversibility and exact finite stationary law.** Define \(x_j=j/(m+1)\), \(r_\alpha(x)=\frac{1-x}{x}\frac{F_\alpha(x)}{1-F_\alpha(x)}\) for \(0<x<1\), and
\[
w_0=1,\qquad w_k=\prod_{j=1}^k r_\alpha(x_j),\qquad
\pi_k=\frac{w_k}{\sum_{\ell=0}^m w_\ell}.
\]
A direct quotient calculation using \(F_\alpha(1-x)=1-F_\alpha(x)\) gives \(w_{k+1}/w_k=p_k/q_{k+1}\). Thus \(\pi_kp_k=\pi_{k+1}q_{k+1}\). Every permitted birth and death probability is positive; every state communicates with every other, and self-loops make the chain aperiodic. Therefore this is the unique stationary law and attracts every initial law. Symmetric fixed zealots imply \(p_k=q_{m-k}\), and uniqueness gives \(\pi_k=\pi_{m-k}\).

For \(0<x<1/2\), \(F_\alpha(x)<x\) exactly when \(0<\alpha<1\), and \(F_\alpha(x)>x\) exactly when \(\alpha>1\). Because \(r_\alpha(x)<1\) is equivalent to \(F_\alpha(x)<x\), consecutive stationary masses decrease toward the middle for \(\alpha<1\) and increase toward the middle for \(\alpha>1\); reflection gives the other half. At \(\alpha=1\), all ratios equal one. This proves the precise finite-size mode assertions, including the middle ties when \(m\) is odd.

**(2) Potential and large-size stationary fluctuations.** Define the continuous function
\[
g_\alpha(x)=\log r_\alpha(x)\quad(0<x<1),\qquad
g_\alpha(0)=\log\alpha,\quad g_\alpha(1)=-\log\alpha,
\]
and its antiderivative \(G_\alpha(x)=\int_0^x g_\alpha(u)du\). The endpoint extensions follow from \(F_\alpha(x)=\alpha x+o(x)\) as \(x\downarrow0\) and symmetry. Consequently, uniformly over \(0\le k\le m\),
\[
\frac{1}{m}\log w_k=G_\alpha(k/m)+o(1),
\]
by uniform convergence of Riemann sums. Reflection yields \(G_\alpha(1-x)=G_\alpha(x)\) and \(G_\alpha(1)=0\). For \(0<\alpha<1\), \(g_\alpha<0\) to the left of \(1/2\) and \(>0\) to its right, so \(G_\alpha\) is strictly maximized at the endpoints. For \(\alpha>1\), its unique maximum is \(x=1/2\). For \(\alpha=1\), it vanishes identically.

In the boundary-dominant regime, for each fixed \(j\),
\[
\frac{w_j}{w_0}=\prod_{i=1}^{j}r_\alpha\big(i/(m+1)\big)\longrightarrow\alpha^j.
\]
For any fixed small \(\varepsilon>0\), continuity and \(r_\alpha(0)=\alpha<1\) provide a \(\rho<1\) uniformly bounding the ratios up to \(j\le\varepsilon m\). Away from both endpoints the potential gap makes masses exponentially small, uniformly. Dominated geometric summation then gives \(\sum_{k=0}^m w_k\to 2/(1-\alpha)\), and the claimed boundary masses and two-atom rescaled limit follow.

For \(\alpha>1\), write \(u=x-1/2\). The explicit response gives
\[
\log\frac{1-x}{x}=-4u+O(u^3),\qquad
\log\frac{F_\alpha(x)}{1-F_\alpha(x)}=O(|u|^\alpha),
\]
so \(g_\alpha(1/2+u)=-4u+o(|u|)\). Hence
\[
G_\alpha(1/2+u)-G_\alpha(1/2)=-2u^2+o(u^2).
\]
In fact, the Riemann-sum expansion on windows \(k-m/2=O(\sqrt m)\) is uniform after subtracting its center value: its logarithmic weight differences converge to \(-2(k-m/2)^2/m\). The global strict potential maximum supplies Gaussian tail domination. Normalizing the lattice sums yields a centered normal of variance \(1/4\). At \(\alpha=1\), finite uniformity directly implies the stated uniform limit.

**(3) Exact first-passage formula.** For any irreducible birth-death chain with the present transition convention, the standard first-step recurrence for \(h_k=\mathbb E_k\tau_m\) with \(h_m=0\) is
\[
p_k(h_k-h_{k+1})-q_k(h_{k-1}-h_k)=1.
\]
Multiply by \(w_k\), telescope from state \(0\) through state \(k\) using \(w_kp_k=w_{k+1}q_{k+1}\), and sum the differences to obtain the *exact* finite identity
\[
\mathbb E_0\tau_m=\sum_{k=0}^{m-1}\frac{\sum_{j=0}^{k}w_j}{w_kp_k}.
\]
At \(\alpha=1\), \(w_j=1\) and \(p_k=(m-k)(k+1)/[m(m+1)]\); the sum becomes
\[
m(m+1)\sum_{k=0}^{m-1}\frac{1}{m-k}=m(m+1)H_m.
\]
This counts single susceptible selections (not sweeps or continuous-time units).

**(4) Exponential first-passage law outside criticality.** For each fixed \(\alpha>0\), a constant \(c_\alpha>0\) satisfies \(p_k\ge c_\alpha/m^2\) for all \(m\ge2\) and \(0\le k<m\), by monotonicity of \(F_\alpha\), its linear behavior at zero, and \((m-k)/m\ge1/m\). Trivially \(p_k\le1\). The exact finite sum, the uniform potential limit, and the elementary Laplace principle for sums of polynomially many positive terms therefore give
\[
\lim_{m\to\infty}\frac1m\log\mathbb E_0\tau_m
=\max_{0\le y\le x\le1}\big(G_\alpha(y)-G_\alpha(x)\big).
\]
For \(0<\alpha<1\), the maximum is the drop from the left endpoint to \(1/2\), equal to \(-G_\alpha(1/2)\). For \(\alpha>1\), it is the drop from \(1/2\) to the right endpoint, equal to \(G_\alpha(1/2)-G_\alpha(1)\). Since \(G_\alpha(1)=G_\alpha(0)=0\), both are \(\Delta_\alpha=|G_\alpha(1/2)|>0\). This establishes the exponential result and its exact variational barrier, without assuming an uncontrolled diffusion or Kramers approximation.

## Verification

Run `python3 verify.py` with Python 3 standard library; no third-party packages or network access are needed. The checker constructs the exact rational transition matrices for exponents \(\alpha=1\) and \(\alpha=2\) and sizes \(2\le m\le11\), independently solves the absorbing first-passage linear systems over rationals, and compares them with the product-form reversible hitting formula and critical harmonic identity. It also tests detailed balance, state reflection, stationary mode changes, finite-size boundary/geometric limits, Gaussian variances, and numerical quadrature of the noncritical exponential barrier. The supplied checker returned `VERIFY_OK 2352 exact and numerical checks`.

These are finite numerical and rational cross-checks. The all-size and asymptotic results follow from the preceding analytical arguments rather than any assertion that finitely many tests certify infinitely many instances.

## Relationship to prior work

Reina, Njougouo, Tuci, and Carletti introduced the polling-error response as a continuous interpolation between majority and voter copying; their later zealot study used the same response with **one opinion's zealots**, asymmetric option qualities, and heterogeneous networks. This work considers a specifically stated symmetric two-zealot, equal-quality complete-graph extension, for which their results do not provide this finite stationary law or first-passage limit.

Mobilia's finite-population nonlinear \(q\)-voter model already studies **opposing zealots**, bimodal stationary laws, and long switching times. That analysis uses unanimity sampling and transition rates proportional to powers of neighbor fractions, rather than the present polling-error response \(F_\alpha\). The reversible birth-death method and qualitative metastability are therefore established tools, **not** claimed as novel here. The proposed distinguishing contribution is the exact response-specific critical uniformity, geometric versus Gaussian scaling, harmonic first passage, and explicit general-\(\alpha\) barrier.

The noisy voter literature also contains zealot-induced stationary transition phenomena under differing linear herding and independent-noise rates. No claim of novelty is based merely on a change of notation or on the existence of a reversible distribution.

## Limitations

The theorem is exact only for one fixed zealot of each opinion, equal option qualities, a complete undirected graph, asynchronous single-susceptible updates, \(m\ge2\), and fixed \(\alpha>0\). It does not assert a phase diagram for heterogeneous graphs, one-sided zealots, arbitrary quality ratios, or jointly scaled \(\alpha=\alpha(m)\). The results give asymptotic rates of mean first entrance times, not full exponential waiting-time laws or mixing times. Opposing zealots prevent permanent unanimity in the full population.

The mathematical proof and reproducible finite checks are not independent external validation. An unindexed prior proof for a general response-function class might encompass the specific formulas; source comparison does not establish absolute publication priority.

## References

1. A. Reina, T. Njougouo, E. Tuci, and T. Carletti, *Studying speed-accuracy trade-offs in best-of-n collective decision-making through heterogeneous mean-field modeling*, arXiv:2310.13694, originally submitted 2023-10-20. https://arxiv.org/abs/2310.13694
2. T. Njougouo, A. Reina, E. Tuci, and T. Carletti, *On the role of zealots in a best-of-n problem on a heterogeneous network*, arXiv:2401.00114, originally submitted 2023-12-30. https://arxiv.org/abs/2401.00114
3. M. Mobilia, *Nonlinear \(q\)-voter model with inflexible zealots*, arXiv:1506.04911 (2015). https://arxiv.org/abs/1506.04911
4. N. Khalil, M. San Miguel, and R. Toral, *Zealots in the mean-field noisy voter model*, arXiv:1707.04087 (2017). https://arxiv.org/abs/1707.04087
