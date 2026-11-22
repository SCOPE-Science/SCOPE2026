# Exact dissipation and a unique thermal optimum in a strongly nonreciprocal Glauber–Ising ring

## Finding
Consider the continuous-time asymmetric Glauber–Ising ring defined below, in the strongly directed regime \(K>J>0\). For every integer \(N\geq4\), the stationary entropy-production rate per spin has the exact finite-size expression
\[
\mathcal E_N(\beta)=\beta K\tanh(2\beta K)\,
 \frac{(1-z^2)(1-z^{N-2})}{1+z^N},\qquad z=\tanh(\beta J).
\]
This rate is strictly positive even though the entire stationary configuration distribution is the reciprocal Ising Gibbs distribution, independent of \(K\). It can be recovered exactly from the initial right-minus-left slope of two stationary spin correlations:
\[
\mathcal E_N(\beta)=\beta K\left.\frac{d}{dt}\Bigl[
\mathbb E_\pi(s_{j+1}(t)s_j(0))-
\mathbb E_\pi(s_{j-1}(t)s_j(0))\Bigr]\right|_{t=0^+}.
\]
In the thermodynamic limit the entropy-production density is
\[
\mathcal E_\infty(\beta)=\beta K\tanh(2\beta K)\operatorname{sech}^2(\beta J).
\]
For each fixed \(K>J>0\), it has exactly one global maximizer \(\beta_*\) over \(\beta>0\). Writing \(x_*=\beta_*J\) and \(p=2K/J>2\), this maximizer is the unique positive solution of
\[
\frac1{x_*}+\frac{2p}{\sinh(2px_*)}=2\tanh x_*.
\]
It decreases strictly with the coupling ratio \(K/J\) and obeys the sharp parameter-independent bounds
\[
0.771702319209\ldots <x_*< 0.868011761596\ldots.
\]
The lower endpoint is approached as \(K/J\to\infty\), and the upper as \(K/J\downarrow1\); neither is attained in the stated regime.

## Assumptions and scope
Let \(N\ge4\) be an integer, \(s=(s_0,\ldots,s_{N-1})\in\{-1,1\}^N\) with subscripts modulo \(N\), \(\beta,J>0\), and \(K>J\). Exactly one spin flips at a time. Spin \(j\) flips at rate
\[
w_j(s)=\frac12\left[1-\frac{s_j}{2}
 \left\{\gamma_e(s_{j-1}+s_{j+1})+\gamma_o(s_{j-1}-s_{j+1})\right\}\right],\quad
\gamma_e=\tanh(2\beta J),\quad \gamma_o=\tanh(2\beta K).
\]
The baseline attempt rate is one; multiplying all transition rates by \(\alpha>0\) multiplies all entropy-production rates and correlation slopes by \(\alpha\), without altering the maximizing temperature. For each finite \(\beta>0\), all flip rates are strictly positive. The stationary probability is \(\pi(s)\), and the entropy-production rate \(\mathcal E_N\) is the stationary forward/backward path relative-entropy rate divided by \(N\), using natural logarithms:
\[
\mathcal E_N=\frac1N\sum_s\pi(s)\sum_{j=0}^{N-1}w_j(s)
\log\frac{\pi(s)w_j(s)}{\pi(s^{(j)})w_j(s^{(j)})},
\]
where \(s^{(j)}\) differs only by flipping spin \(j\). This is path-space entropy production, not the time derivative of the stationary Shannon entropy (which is zero).

## Proof
**Stationary distribution.** Define \(\pi(s)=Z^{-1}\exp[\beta J\sum_j s_js_{j+1}]\). The rate decomposes as \(w_j=w_j^{(e)}+w_j^{(o)}\), where \(w_j^{(o)}=-\gamma_o s_j(s_{j-1}-s_{j+1})/4\). Because \(\gamma_e=\tanh(2\beta J)\), the even part \(w_j^{(e)}\) satisfies detailed balance against \(\pi\). The odd part is zero when the neighbors agree. When they disagree, \(\pi(s^{(j)})=\pi(s)\) and \(w_j^{(o)}(s^{(j)})=-w_j^{(o)}(s)\). Its contribution to the master equation at \(s\) is thus
\[
\sum_j\bigl[\pi(s^{(j)})w_j^{(o)}(s^{(j)})-\pi(s)w_j^{(o)}(s)\bigr]
=\frac{\pi(s)\gamma_o}{2}\sum_j s_j(s_{j-1}-s_{j+1})=0.
\]
The last equality is a cyclic index shift. Irreducibility makes this Gibbs distribution the unique stationary law, for every finite \(N\) and the stated parameters.

**Exact path entropy production.** If the two neighboring spins agree, their transition rates satisfy detailed balance and contribute zero to the logarithm in the definition. If they disagree, put \(u=s_js_{j-1}\in\{-1,1\}\). Then \(\pi(s^{(j)})=\pi(s)\), \(w_j(s)=(1-\gamma_o u)/2\), and
\[
\log\frac{\pi(s)w_j(s)}{\pi(s^{(j)})w_j(s^{(j)})}=-2u\operatorname{artanh}\gamma_o=-4\beta K u.
\]
Conditioned on the two opposing neighbors, \(u\) is an unbiased sign under \(\pi\), hence the mean \(w_j\)-weighted logarithm equals \(\gamma_o\operatorname{artanh}\gamma_o=2\beta K\gamma_o\). If \(C_2=\mathbb E_\pi(s_{j-1}s_{j+1})\), the probability of opposing neighbors is \((1-C_2)/2\), yielding
\[
\mathcal E_N=\beta K\gamma_o(1-C_2).
\]
The one-dimensional zero-field periodic Ising transfer matrix gives, for \(0\leq r\leq N\),
\[
\mathbb E_\pi(s_js_{j+r})=\frac{z^r+z^{N-r}}{1+z^N},\qquad z=\tanh(\beta J).
\]
Substituting the \(r=2\) case and factoring \(1-C_2\) establishes the displayed finite-size expression. It is positive for every finite \(\beta,J,K>0\). At fixed \(\beta>0\), taking \(N\to\infty\) gives \(C_2\to z^2\) and the asserted thermodynamic formula.

**Directional time-arrow identity.** Under the generator \(L\),
\[
Ls_j=-s_j+\frac{\gamma_e}{2}(s_{j-1}+s_{j+1})+
\frac{\gamma_o}{2}(s_{j-1}-s_{j+1}).
\]
Using stationarity and the reflection symmetry of equal-time Gibbs correlations, the right-minus-left derivative at lag zero is exactly \(\gamma_o(1-C_2)\). Multiplication by \(\beta K\) recovers \(\mathcal E_N\). This identity is for a right time derivative of stationary lagged correlations, not an equilibrium fluctuation-dissipation identity.

**Unique macroscopic optimum.** With \(x=\beta J\) and \(p=2K/J>2\), the positive function to maximize is proportional to \(x\tanh(px)\operatorname{sech}^2x\). Its logarithmic derivative is
\[
F_p(x)=\frac1x+\frac{2p}{\sinh(2px)}-2\tanh x.
\]
For every \(p>0\), this is strictly decreasing in \(x>0\), tends to \(+\infty\) as \(x\downarrow0\), and tends to \(-2\) as \(x\to\infty\). Thus it has one zero, which is the global maximizer because the objective tends to zero at both endpoints. For fixed \(x>0\), the function \(2p/\sinh(2px)\) decreases strictly in \(p\) since \(\tanh y<y\) for \(y>0\). Consequently the zero \(x_*(p)\) decreases strictly as \(p\) increases. Its limits solve \(x\tanh x=1\) at \(p\downarrow0\), and \(2x\tanh x=1\) at \(p\to\infty\). On the required \(p>2\) domain, the upper limiting value is the root for \(p=2\), giving the stated sharp bounds. The approximate numbers are illustrative; all uniqueness and inequalities are exact.

## Verification
A standalone standard-library Python checker, `check.py`, independently enumerates all \(2^N\) spin configurations for \(N=3,\ldots,8\), builds the transition rates and Gibbs probabilities, checks every stationary master-equation residual, and computes the path entropy rate by its defining forward/reverse sum. It compares this independently computed value with the closed finite-size expression and checks the directional-lag slope identity. Across 152 deterministic checks it also tests optimal-root monotonicity, strict local optimality and both limiting constants. This finite verification is supplementary; it is not a proof for unbounded ring lengths or parameters. Run with `python check.py` using Python 3 and its standard library.

## Relationship to prior work
Godrèche's *Dynamics of the directed Ising chain* (2011, arXiv:1102.0141) gives the Gibbs-invariant directed-Glauber model and its time-dependent correlation equations, with a one-parameter bias \(V\) bounded by one. The strongly directed independent-coupling regime \(K>J\) considered here lies beyond that nonnegative-weight bias parameterization. Weiderpass, Sharma and Sethi's 2024 preprints (arXiv:2410.23615 and arXiv:2411.00059) treat two independently tunable couplings and the underdamped region, and give the exact transition equations. Those source contributions are assumed, not re-claimed. The cited texts do not state the finite-ring path entropy expression or the unique thermodynamic temperature optimum established here; the directional slope identity combines their generator with an explicit entropy calculation. Aguilera, Moosavi and Shimazaki (2021) discuss entropy production of generally asymmetric **parallel-update** kinetic Ising models, which differs from these continuous-time single-spin-flip rates. Godrèche and Luck (2018) obtain entropy production for a spatially asymmetric **Gaussian** spin model, not this binary Ising chain.

## Limitations
The entropy formulas and exact lag identity are valid for each \(N\ge4\); the maximizing-temperature theorem is established for the thermodynamic-limit entropy density only, not for each finite-ring curve. The statement assumes homogeneous periodic boundaries, strictly positive temperature, positive ferromagnetic reciprocal coupling, strong directional coupling \(K>J\), and single-spin continuous-time rates. At infinite temperature or zero temperature the rate vanishes only as a limit, not as a positive-temperature stationary equality. The source literature supplies the generator and the Gibbs-invariance mechanism, so neither is claimed as new. Independent expert audit and exhaustive publication-priority verification have not been performed; a formally equivalent older unindexed treatment remains possible.

## References
1. C. Godrèche, *Dynamics of the directed Ising chain* (2011), arXiv:1102.0141, https://arxiv.org/abs/1102.0141.
2. G. A. Weiderpass, M. Sharma, S. Sethi, *Solving the Kinetic Ising Model with Non-Reciprocity* (first public 2024-10-31), arXiv:2410.23615, https://arxiv.org/abs/2410.23615.
3. G. Weiderpass, M. Sharma, S. Sethi, *An Exact Solution for the Kinetic Ising Model with Non-Reciprocity* (first public 2024-10-31), arXiv:2411.00059, https://arxiv.org/abs/2411.00059.
4. M. Aguilera, S. A. Moosavi, H. Shimazaki, *A unifying framework for mean-field theories of asymmetric kinetic Ising systems* (2021), https://doi.org/10.1038/s41467-021-20890-5.
5. C. Godrèche and J.-M. Luck, *Characterising the nonequilibrium stationary states of Ornstein–Uhlenbeck processes* (2018), arXiv:1807.00694, https://arxiv.org/abs/1807.00694.
