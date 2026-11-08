# A sharp reliability threshold for dephasing-assisted capture in a quantum dimer

## Finding

For a continuously monitored, absorbing quantum dimer with sink population-decay rate exactly twice the hopping strength, the squared coefficient of variation of the first absorption time has a unique global dephasing minimizer. The minimizer is zero at small energy detuning and positive precisely beyond the sharp threshold
\[
|\Delta|/J>\delta_c=\sqrt{2\sqrt{21}-9}=0.406388225606599\ldots .
\]
For every detuning beyond this threshold, the fluctuation-optimal dephasing strictly exceeds the mean-capture-time-optimal dephasing. In particular, for \(\delta_c<|\Delta|/J\le1\), noise reduces relative capture-time fluctuations although any positive dephasing increases the mean capture time. At large detuning, the gap between these two optima approaches \(2J\) in physical rate units.

## Assumptions and scope

Fix \(J>0\), a real site-energy difference \(\Delta\), and dephasing rate \(\gamma\ge0\). The one-excitation Hamiltonian on sites \(1,2\) is
\[
H=\begin{pmatrix}\Delta/2&J\\J&-\Delta/2\end{pmatrix}.
\]
There is one irreversible Lindblad capture jump \(\sqrt{2J}\,|\mathrm{sink}\rangle\langle2|\) and two site-dephasing jumps \(\sqrt\gamma\,|j\rangle\langle j|\) for \(j=1,2\). The unnormalized survivor density matrix starts at \(\sigma(0)=|1\rangle\langle1|\). This construction has no reinjection or other loss. The first capture time is \(T\); set \(g=\gamma/J\), \(\delta=\Delta/J\) and \(\tau=JT\). Let
\[
F_\delta(g)=\frac{\operatorname{Var}(T)}{(\mathbb E T)^2}
\]
(the squared coefficient of variation). We consider all real \(\delta\) and all \(g\ge0\), with the dimensionless sink population-decay rate fixed at \(2\).

The exact mean and second moment are
\[
\mathbb E\tau=\frac{g^2+4g+\delta^2+3}{2(g+1)},\quad
\mathbb E\tau^2=\frac{[(g+1)^2+\delta^2][(g+2)(g+3)+\delta^2]}{2(g+1)^2}.
\]
Writing \(t=|\delta|\), the exact relative variance is
\[
F_\delta(g)=\frac{g^4+6g^3+12g^2+10g+3+\delta^4+\delta^2(2g^2+6g+8)}{(g^2+4g+\delta^2+3)^2}.
\]
Its globally minimizing rate is uniquely determined by
\[
g_{\mathrm{CV}}(\delta)=
\begin{cases}
0,&t\le\delta_c,\\
\text{the unique positive root of }P_t(g)=0,&t>\delta_c,
\end{cases}
\]
where
\[
P_t(g)=t^4+18t^2+10t^2g-g^4-6g^3-12g^2-10g-3.
\]
The unique mean-optimal rate is \(g_{\mathrm{mean}}(\delta)=\max\{0,t-1\}\). For every \(t>\delta_c\),
\[
g_{\mathrm{CV}}(\delta)>g_{\mathrm{mean}}(\delta),
\]
and for \(t\to\infty\),
\[
g_{\mathrm{CV}}(\delta)=t+1-\frac2t+O(t^{-2}),\qquad
g_{\mathrm{CV}}(\delta)-g_{\mathrm{mean}}(\delta)\longrightarrow2.
\]

## Proof

Write the survivor state as \(\sigma=\begin{psmallmatrix}p&x+iy\\x-iy&q\end{psmallmatrix}\). In the rescaled time \(s=Jt\), the Lindblad equation gives the exact linear system
\[
\frac{d}{ds}\begin{pmatrix}p\\q\\x\\y\end{pmatrix}
=L\begin{pmatrix}p\\q\\x\\y\end{pmatrix},\quad
L=\begin{pmatrix}0&0&0&-2\\0&-2&0&2\\0&0&-(g+1)&\delta\\1&-1&-\delta&-(g+1)\end{pmatrix}.
\]
The initial vector is \(u=(1,0,0,0)^{\mathsf T}\), and survival probability is \(S(s)=c e^{Ls}u\) with \(c=(1,1,0,0)\). Trace loss is \(-S'(s)=2q(s)\ge0\). If a physical trajectory has zero cumulative trace loss then \(q=0\) throughout; positivity forces both coherence components to vanish, and the coherence equation then forces \(p=0\). Thus no nonzero density operator can remain nonabsorbing. More concretely, for any nonzero positive initial state the analytic function \(q(s)\) cannot vanish on an interval: otherwise positivity enforces zero coherence and the equation for \(y\) enforces \(p=0\). Therefore every trace-one positive initial state loses strictly positive mass by scaled time \(s=1\). Compactness of the trace-one positive-state set and continuity of the survivor semigroup give a uniform survival factor strictly smaller than one over each unit-time interval. Hence survival decays exponentially uniformly, capture occurs with probability one, \(A\) is invertible, and all capture-time moments are finite.

Let \(A=-L\). Direct solution of \(Aw_1=u\) gives
\[
w_1=\begin{pmatrix}
(\delta^2+g^2+3g+2)/(2(g+1))\\
1/2\\\delta/(2(g+1))\\1/2
\end{pmatrix}.
\]
Since \(\mathbb E\tau=\int_0^\infty S(s)\,ds=cA^{-1}u\) and \(\mathbb E\tau^2=2\int_0^\infty sS(s)\,ds=2cA^{-2}u\), solving \(Aw_2=w_1\) gives the two moment identities in the Finding section. Subtraction yields \(F_\delta(g)\) exactly.

The denominator in
\[
\frac{dF_\delta}{dg}=-\frac{2P_t(g)}{(g^2+4g+t^2+3)^3}
\]
is strictly positive. Let \(z=t^2\). The constant term is \(P_t(0)=z^2+18z-3\), whose only nonnegative root is \(z_c=2\sqrt{21}-9\), satisfying \(0<z_c<1\). When \(0\le z\le z_c\), all nonconstant coefficients of \(P_t\) are strictly negative and the constant is nonpositive, so \(F_\delta\) increases strictly on \(g>0\), with unique minimum at zero. If \(z>z_c\), the constant coefficient is positive, the coefficients of the cubic, quadratic, and quartic powers are negative, and the linear coefficient can have either sign. In descending order this coefficient sequence has exactly one sign change, so Descartes' rule of signs shows that \(P_t\) has exactly one positive root, counting multiplicity. It is simple; the derivative of \(F_\delta\) changes from negative to positive there. The limit \(F_\delta(g)\to1\) as \(g\to\infty\) makes this minimum global and unique.

The derivative of the mean simplifies to \(\tfrac12[1-t^2/(g+1)^2]\), giving \(g_{\mathrm{mean}}=\max\{0,t-1\}\). For \(t\in(\delta_c,1]\), \(g_{\mathrm{mean}}=0<g_{\mathrm{CV}}\). For \(t>1\), direct substitution yields \(P_t(t-1)=8t^2(t+1)>0\), so the unique positive root is strictly to its right. Moreover \(P_t(t+1)=-8(t^2+7t+4)<0\), hence \(t-1<g_{\mathrm{CV}}<t+1\). Expanding \(P_t(t+a+b/t)\) in descending powers of \(t\) shows the leading coefficients are \(-4(a-1)t^3\) and \(-2(3a^2+4a+2b-3)t^2\). The unique root therefore has \(a=1\) and \(b=-2\). On the interval \(t-1<g<t+1\), the derivative \(\partial_gP_t=-4t^3+O(t^2)\) uniformly, so the Taylor remainder in locating the root is \(O(t^{-2})\). This also proves the limiting two-unit gap.

## Verification

The package contains `verify.py`. Running `python verify.py` reconstructs the exact four-by-four survivor generator, solves the first and second resolvent systems over symbolic parameters, checks the displayed formulas and derivative polynomial, and verifies the optimizer-comparison identities. An independent numerical route uses matrix exponentials and numerical integration of survival probabilities at 16 parameter pairs (32 integrals); all checks succeeded. The symbolic proof, rather than finite sampling, establishes the global statements.

For example, at \(|\Delta|/J=1\), \(g_{\mathrm{mean}}=0\), but \(g_{\mathrm{CV}}\approx0.9311424638\). The minimum relative variance is approximately \(0.604647\), compared to \(0.75\) at zero dephasing.

## Relationship to prior work

Mülken and Schmid (2010) study detuned, dephased dimers with irreversible trapping. They compute the survival probability and introduce decay-window lifetimes and the longest relaxation scale; these are not the first two full first-capture moments or their relative-variance optimizer. Their dynamical equation is a direct precursor, and the present moment formulas are in principle derivable from a sufficiently complete solution of that equation. Wu, Silbey and Cao (2013) analyze mean first-passage-time scaling in exciton transport, rather than relative-variance optimization. Coates, Lovett and Gauger (first public version 2022) analyze multiple noise-assisted maxima of steady-state transport efficiency on disordered quantum networks with injection and extraction. That efficiency is distinct from the coefficient of variation of one continuous absorption event. Projective repeated-measurement first-detection methods likewise have a different detection protocol. The specific threshold, unique quartic optimizer, and strict separation from the mean optimizer are the claims assessed here, not novelty of Lindblad modeling, detuned dimers, or noise-assisted transfer generally.

## Limitations

The sink rate is fixed at \(2J\). The pure-dephasing jumps are Markovian and act independently on the two sites. There is exactly one excitation, no injection, no recombination or other loss, and an initially localized donor. The results do not classify arbitrary sink strengths, finite-temperature non-Markovian baths, or projective time-sampled detection. The first two moments and relative variance do not determine the full detection-time law. Priority remains subject to possible unrecognized implicit derivations or equivalent published optimization results.

## References

- O. Mülken and T. Schmid, *Environment-assisted quantum transport and trapping in dimers*, Phys. Rev. E 82, 042104 (2010), arXiv:1008.4022, https://arxiv.org/abs/1008.4022.
- J. Wu, R. J. Silbey and J. Cao, *Generic mechanism of optimal energy transfer efficiency: a scaling theory of the mean first-passage time in exciton systems*, Phys. Rev. Lett. 110, 200402 (2013), https://doi.org/10.1103/PhysRevLett.110.200402.
- A. R. Coates, B. W. Lovett and E. M. Gauger, *From Goldilocks to Twin Peaks: multiple optimal regimes for quantum transport in disordered networks*, arXiv:2210.11875, first posted 2022-10-21, https://arxiv.org/abs/2210.11875.
- H. Friedman, D. A. Kessler and E. Barkai, *Quantum walks: the first detected passage time problem*, arXiv:1611.05676 (2016), https://arxiv.org/abs/1611.05676 (different measurement protocol).
