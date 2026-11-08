# A sharp mean-growth threshold and a rigorous false-rescue window under environmental switching

## Finding

Fix positive parameters \(b>c>0\) and \(\sqrt{bc}<a<(b+c)/2\). Let a common environmental state switch at rate \(\kappa>0\) between two values. A two-component nonnegative population density \(x(t)\) evolves according to
\[
\dot x=A_{E(t)}x,\qquad
A_1=\begin{pmatrix}-a&b\\c&-a\end{pmatrix},\qquad
A_2=\begin{pmatrix}-a&c\\b&-a\end{pmatrix}.
\]
Each fixed environment is exponentially subcritical because its dominant growth rate is \(\sqrt{bc}-a<0\). Nevertheless, for every strictly positive initial population, the first-moment growth rate is exactly
\[
\Lambda_M(\kappa)=-a-\kappa+\sqrt{(b+\kappa)(c+\kappa)}.
\]
It is strictly increasing and changes sign at precisely
\[
\boxed{\kappa_*=(a^2-bc)/(b+c-2a)>0.}
\]
Moreover, there exists \(\varepsilon>0\), depending on \(a,b,c\), for which **every** \(\kappa\in(\kappa_*,\kappa_*+\varepsilon)\) has strictly positive mean growth, yet \(\lVert x(t)\rVert_1\to0\) exponentially along almost every environmental path.

There is a fully rational certificate of this discrepancy. Set
\[
(a,b,c,\kappa)=(11/5,4,1,1401/1000).
\]
Then \(\Lambda_M(\kappa)>0\), although for every strictly positive initial condition,
\[
\boxed{\limsup_{t\to\infty}t^{-1}\log\lVert x(t)\rVert_1<-1/2000\quad\text{almost surely}.}
\]
The last bound uses no sampling and no numerical approximation.

## Assumptions and scope

An environment \(E(t)\in\{1,2\}\) is a symmetric continuous-time Markov chain: independent holding times have exponential distribution of rate \(\kappa\), and every jump flips the state. Its path is exogenous and common to both populations. For each \(x(0)\in(0,\infty)^2\), the differential equation uses the current matrix. Either environmental starting state is allowed. Positive off-diagonal entries are **cross-component recruitment**, not conservative physical migration; the model is a linear low-density approximation with constant local loss \(a\). By "typical collapse" we mean exponential convergence to zero, not finite-time absorption of discrete individuals.

The expectation statement is about \(\mathbb E[x_1(t)+x_2(t)]\), and typical collapse is a pathwise almost-sure assertion on the same process. The continuous-time Markov chain and the population differential equation are coupled only by matrix selection.

## Proof

### 1. Frozen and mean growth

Both frozen matrices have eigenvalues \(-a\pm\sqrt{bc}\), so both are Hurwitz. Put \(m_e(t)=\mathbb E[x(t)\mathbf1_{\{E(t)=e\}}]\). These conditional first moments satisfy the exact autonomous four-dimensional linear system
\[
\frac{d}{dt}\binom{m_1}{m_2}=\mathcal B\binom{m_1}{m_2},\qquad
\mathcal B=\begin{pmatrix}A_1-\kappa I&\kappa I\\\kappa I&A_2-\kappa I\end{pmatrix}.
\]
The irreducible Metzler matrix \(\mathcal B\) has a unique positive Perron eigenvector. Under the simultaneous exchange of the two environment labels and the two population coordinates, \(\mathcal B\) is invariant. Its Perron eigenvector must therefore be of the form \((u,v,v,u)\). Restricting to this invariant plane gives
\[
\begin{pmatrix}-a-\kappa&b+\kappa\\c+\kappa&-a-\kappa\end{pmatrix},
\]
whose larger eigenvalue is the stated \(\Lambda_M\). Irreducibility means this rate governs the positive initial first moments, independently of the initial environment.

The derivative is
\[
\Lambda_M'(\kappa)=-1+\frac{b+c+2\kappa}{2\sqrt{(b+\kappa)(c+\kappa)}}>0,
\]
because \((b-c)^2>0\). The sign of \(\Lambda_M\) is the sign of
\[
(b+\kappa)(c+\kappa)-(a+\kappa)^2
=(b+c-2a)(\kappa-\kappa_*).
\]
This proves both the exact threshold and its uniqueness.

### 2. Pathwise entropy loss

For fixed \(\kappa\) put \(u=\sqrt{c+\kappa}\), \(v=\sqrt{b+\kappa}\), \(h_1=(u,v)^\top\), and \(h_2=(v,u)^\top\). Direct multiplication gives
\[
A_e^\top h_e+\kappa(h_{3-e}-h_e)=\Lambda_M h_e\quad(e=1,2).
\]
Define \(H(t)=e^{-\Lambda_Mt}h_{E(t)}^\top x(t)\), and the pre-jump multiplier
\[
Z(t)=\frac{h_{3-E(t)}^\top x(t)}{h_{E(t)}^\top x(t)}.
\]
The multiplier always lies between \(u/v\) and \(v/u\), so its logarithm is bounded. Between jumps the logarithmic derivative of \(H\) equals \(-\kappa(Z-1)\); a switch adds \(\log Z\). If \(N\) is the flip-count process, then the compensated Poisson integral
\[
M(t)=\int_0^t\log Z(s-)\,[dN(s)-\kappa ds]
\]
is a martingale with bounded jumps and predictable quadratic variation \(O(t)\). The martingale strong law yields \(M(t)/t\to0\) almost surely. The exact identity is
\[
\log\frac{H(t)}{H(0)}
=M(t)-\kappa\int_0^t\{Z(s)-1-\log Z(s)\}\,ds.
\tag{1}
\]
The entropy integrand \(G(z)=z-1-\log z\) is nonnegative, vanishing only at \(z=1\). The strictly positive entries of the two fixed vectors make \(h_{E(t)}^\top x(t)\) uniformly comparable with \(\lVert x(t)\rVert_1\). Consequently any positive asymptotic time-average of \(G(Z)\) creates a strict gap below \(\Lambda_M\) for the sample-path growth.

### 3. Uniform strict gap at the mean threshold

Set \(r(t)=x_1(t)/x_2(t)\) and \(R=\sqrt{b/c}>1\). While the first environment is active, \(\dot r=b-cr^2\); while the second is active, \(\dot r=c-br^2\). The interval \([R^{-1},R]\) is forward invariant under both flows. Every initially positive ratio reaches it in finite almost-sure time: above \(R\), a sufficiently long second-environment sojourn pushes it below \(R\); below \(R^{-1}\), a sufficiently long first-environment sojourn pushes it above \(R^{-1}\). Such sojourns occur almost surely in the independent exponential sequence; on either exterior interval the appropriate drift has a nonzero inward bound until entry.

Choose \(\delta\in(0,R-1)\). By the explicit monotone Riccati flows, there exists finite \(L>0\) such that every first-environment interval of length at least \(2L\) has \(r\ge1+\delta\) after time \(L\), and every analogous second-environment interval has \(r\le(1+\delta)^{-1}\) after time \(L\). Writing \(q=v/u>1\), we have
\[
Z=\frac{qr+1}{r+q}\quad(E=1),\qquad
Z=\frac{r+q}{qr+1}\quad(E=2).
\]
Thus both types of long interval contribute at least \(L G(1+\eta)\) to the integral in (1), for some \(\eta>0\) fixed for \(\kappa\) in a compact neighborhood of \(\kappa_*\). By the strong law of exponential renewal times, the number of holding intervals of length at least \(2L\) per elapsed unit time tends to \(\kappa e^{-2\kappa L}\). It follows that, uniformly throughout that compact neighborhood,
\[
\liminf_{t\to\infty}\frac1t\int_0^t G(Z(s))ds
\ge L\kappa e^{-2\kappa L}G(1+\eta)>0\quad\text{almost surely}.
\]
At \(\kappa=\kappa_*\), \(\Lambda_M=0\), so (1) shows strict negative sample-path logarithmic growth. The positive lower bound remains uniform in a sufficiently small closed interval to its right, whereas \(\Lambda_M(\kappa)\downarrow0\) as \(\kappa\downarrow\kappa_*\). Choosing a sufficiently small \(\varepsilon>0\) proves the claimed nonempty false-rescue interval.

### 4. An exact rational-rate certificate

Take \(a=11/5\), \(b=4\), \(c=1\), and \(\kappa=1401/1000\). Then \(\kappa_*=7/5\), and
\[
(4+\kappa)(1+\kappa)-(a+\kappa)^2=3/5000.
\]
Rationalization gives
\[
0<\Lambda_M=\frac{3/5000}{\sqrt{(4+\kappa)(1+\kappa)}+a+\kappa}<1/12000.
\tag{2}
\]
After a finite almost-sure time, \(r\in[1/2,2]\). In the first environment, \(\dot r=4-r^2\). Starting at \(1/2\), after time \(1/2\) we have \(r>3/2\), because \(\tanh1>3/4\), equivalently \(e^2>7\). In the other environment the reciprocal \(1/r\) solves that same Riccati equation, so after time \(1/2\) we have \(r<2/3\). Each holding interval of length at least one therefore contributes at least half a unit of time on which the switch multiplier is at least
\[
Z\ge\frac{3q+2}{2q+3}\ge\frac{27}{25},\qquad
q=\sqrt{\frac{4+\kappa}{1+\kappa}}>\frac{31}{21}.
\]
The elementary logarithmic inequality \(\log(1+y)\le y-y^2/2+y^3/3\) for \(y\ge0\) yields
\[
G(27/25)=2/25-\log(27/25)\ge142/46875>3/1000.
\]
The renewal strong law makes the limiting frequency of holding intervals of length at least one equal to \(\kappa e^{-\kappa}\). Since \(7/5<\kappa<3/2\) and \(e^{3/2}<5\), (1) and the martingale law imply
\[
\limsup_{t\to\infty}t^{-1}\log\lVert x(t)\rVert_1
\le\Lambda_M-\frac{\kappa^2 e^{-\kappa}}2\cdot\frac3{1000}
<\frac1{12000}-\frac{147}{250000}< -\frac1{2000}.
\]
All inequalities are strict; no simulation is invoked for the proof.

## Verification

Run \(\texttt{python3 verify.py}\) from the extracted package directory. It uses only the Python standard library. It performs exact rational checks of the explicit threshold, the determinant identity, the entropy and renewal constants, and finite parameter checks of the general identity, plus a separately implemented four-state Perron numerical sanity check. A successful run reports 942 passing checks. These tests support reproducibility; the universal and almost-sure claims are established by the analytic proof above, the renewal strong law, and the bounded-jump martingale strong law.

## Relationship to prior work

Tuljapurkar, Horvitz and Pascarella (2003) already distinguish expected-population and stochastic growth in Markovian population environments and establish their possible inequality. The present claim does **not** claim discovery of that general distinction. Their inspected original paper treats discrete-time structured-population transition matrices, derives growth-rate relationships and elasticities, and illustrates a seven-environment, eight-stage plant model. It does not state this two-environment continuous-time transposed-recruitment threshold, its all-parameter strict switching window, or the above exact rational almost-sure loss bound.

Ogura and Preciado (2015) give general mean-stability machinery for Markov regenerative switched linear systems; the explicit four-state moment generator used here is a special instance of established methodology. Their inspected preprint does not give this model's closed-form ecological threshold or the particular quantitative counterdirection between mean and almost-sure growth. Bao and Shao (2016) treat regime-switching nonlinear predator–prey extinction and permanence, but their accessible abstract does not establish this particular linear two-patch criterion. No claim is made that these general analytical methods are new. Published literature may contain equivalent unlocated specializations; independent priority review remains necessary.

## Limitations

The dynamics are linear density dynamics with no demographic noise, carrying capacity, finite-time extinction, or finite population size. Exponential mean growth is an ensemble first-moment statement, not probability of persistent positive population along a single realization. The switching is symmetric, Markovian, and exogenous; the two matrices have exactly swapped recruitment rates and common loss. The concrete almost-sure bound is deliberately conservative, not the exact top Lyapunov exponent. The model does not by itself recommend ecological management choices. Self-review and literature inspection do not constitute independent scientific audit.

## References

- Tuljapurkar, S., Horvitz, C. C., and Pascarella, J. B. (2003), *The Many Growth Rates and Elasticities of Populations in Random Environments*, The American Naturalist 162(4), 489–502, first published online 2003-10-16, https://doi.org/10.1086/378648. Author-uploaded full text: https://www.researchgate.net/publication/5403853_The_Many_Growth_Rates_and_Elasticities_of_Populations_in_Random_Environments
- Ogura, M., and Preciado, V. M. (2015), *Stability of Markov regenerative switched linear systems*, original arXiv preprint arXiv:1501.03474, https://arxiv.org/abs/1501.03474
- Bao, J., and Shao, J. (2016), *Permanence and Extinction of Regime-Switching Predator-Prey Models*, SIAM J. Math. Anal. 48(1), 725–739, https://doi.org/10.1137/15M1024512
