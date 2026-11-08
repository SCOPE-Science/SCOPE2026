# A universal seed-shape threshold for kurtosis reversal under stochastic-noise resetting

## Finding

Consider a harmonically confined particle whose *driving Brownian noise*, but not its position, resets at independent Poisson times. At every noise reset, the driving coordinate is restarted from an independent, symmetric, possibly discrete probability law. Its stationary positional excess kurtosis has a sharp classification determined solely by the restarting law's normalized fourth moment and a dimensionless variance.

Put \(\beta=r/\mu>0\), \(w=rs^2/(2D)>0\), and \(\chi=\mathbb E[R^4]/s^4\ge1\). Here \(r\) is noise-reset rate, \(\mu\) is trap relaxation rate, \(D\) is noise diffusivity, and \(s^2=\mathbb E[R^2]\). The unique stationary position satisfies

\[
\operatorname{Var}(X)=\frac{2D\beta(1+w)}{\mu(\beta+1)},\qquad
K=\frac{6\left(\big[(\beta+1)\chi-(2\beta+3)\big]w^2+5\beta w+7\beta+3\right)}{(\beta+2)(\beta+3)(1+w)^2},
\]

where \(K=\mathbb E[X^4]/\mathbb E[X^2]^2-3\) is excess kurtosis, and symmetry gives \(\mathbb E[X]=0\). Set \(\chi_c=(2\beta+3)/(\beta+1)\). For every \(\chi\ge\chi_c\), excess kurtosis is strictly positive at all finite \(w>0\). For \(1\le\chi<\chi_c\), it changes sign at exactly one positive variance ratio,

\[
 B=(2\beta+3)-(\beta+1)\chi>0,\qquad
 w_*=\frac{5\beta+\sqrt{25\beta^2+4B(7\beta+3)}}{2B}.
\]

Precisely, \(K>0\) for \(0<w<w_*\), \(K=0\) at \(w=w_*\), and \(K<0\) for \(w>w_*\). Thus \(\chi\le2\) admits negative excess kurtosis for every \(\beta>0\) at sufficiently large \(w\); if \(2<\chi<3\), this is possible exactly when \(\beta<(3-\chi)/(\chi-2)\); and if \(\chi\ge3\), it is impossible. Every \(\chi\ge1\) is realized by a symmetric three-point restart law, so none of these shape regimes is empty.

## Assumptions and scope

Let \(\mu,r,D>0\). Between Poisson events of rate \(r\), let \(dY_t=\sqrt{2D}\,dB_t\) and \(dX_t=(-\mu X_t+rY_t)\,dt\). At each independent event, replace \(Y\) by an independent draw \(R\), leaving \(X\) continuous and unchanged. The draws are independent of the Brownian motion and the reset clock. Assume \(R\stackrel d=-R\), \(0<s^2=\mathbb E[R^2]<\infty\), and \(\mathbb E[R^4]<\infty\). All statements concern the unique stationary probability law with finite fourth moments, not the transient distribution. The notation \(w>0\) excludes the zero-seed case, which is a continuous boundary limit of the formula.

The particle is not directly reset, the noise has no restoring drift between events, and the harmonic force is one-dimensional and linear. No claim is made for nonsymmetric restart seeds or nonlinear confinement.

## Proof

**Existence and finite moments.** Let \(T_n\) be iid exponential waiting times of rate \(r\). Between noise resets, the exact position update is

\[
X_n=e^{-\mu T_n}X_{n-1}+\frac{rR_n}{\mu}(1-e^{-\mu T_n})+G_n(T_n),
\]

where, conditionally on \(T_n=t\), the final term is centered Gaussian with variance

\[
\operatorname{Var}(G_n(t))=\frac{2Dr^2}{\mu^2}\left[t-\frac{2(1-e^{-\mu t})}{\mu}+\frac{1-e^{-2\mu t}}{2\mu}\right].
\]

The affine coefficient lies strictly between zero and one and has strictly negative mean logarithm. The innovations have finite fourth moment under the stated hypotheses. Standard contraction of this affine recurrence yields a unique invariant law with finite fourth moment at reset epochs; the stationary Poisson-age construction yields the unique finite-fourth-moment physical-time law. Symmetry forces its odd moments to vanish. The independent reset clock permits stationary generator identities.

**Moment hierarchy.** Rescale time by \(\mu^{-1}\) and both position coordinates by \(\sqrt{D/\mu}\). Retain the symbols \(x,y\) for rescaled coordinates and \(\beta=r/\mu\). Write \(\rho_j=\mathbb E[(R/\sqrt{D/\mu})^j]\), so that \(\rho_2=2w/\beta\), \(\rho_4=\chi\rho_2^2\), and odd \(\rho_j\) vanish. The generator is

\[
\mathcal L f(x,y)=(-x+\beta y)\partial_x f+\partial_{yy}f+\beta\left(\mathbb E[f(x,R/\sqrt{D/\mu})]-f(x,y)\right).
\]

For stationary moments \(m_{ij}=\mathbb E[x^iy^j]\), with \(m_{00}=1\), its exact polynomial identity is

\[
(i+\beta)m_{ij}=i\beta m_{i-1,j+1}+j(j-1)m_{i,j-2}+\beta\rho_jm_{i0}\quad(j>0),
\qquad m_{i0}=\beta m_{i-1,1}\quad(i>0).
\]

Terms multiplied by a vanishing prefactor are omitted. Apply the recurrence at total degrees two and four. First obtain \(m_{02}=\rho_2+2/\beta\), \(m_{11}=\beta m_{02}/(1+\beta)\), and \(m_{20}=\beta m_{11}=2\beta(1+w)/(1+\beta)\). At degree four the exact chain is

\[
\begin{aligned}
m_{04}&=\rho_4+12\rho_2/\beta+24/\beta^2,\\
m_{13}&=(\beta m_{04}+6m_{11})/(1+\beta),\\
m_{22}&=(2\beta m_{13}+(2+\beta\rho_2)m_{20})/(\beta+2),\\
m_{31}&=3\beta m_{22}/(\beta+3),\\
m_{40}&=\beta m_{31}.
\end{aligned}
\]

Substitute the second-moment identities and \(\rho_4=\chi\rho_2^2\) to obtain exactly the displayed \(K=m_{40}/m_{20}^2-3\). This also proves that no higher moment or additional feature of the symmetric seed law enters the result.

**Sharp sign boundary.** The denominator of \(K\) is positive. Its numerator divided by six is the quadratic

\[
P(w)=\left[(\beta+1)\chi-(2\beta+3)\right]w^2+5\beta w+7\beta+3.
\]

If the quadratic coefficient is nonnegative, all three coefficients are nonnegative and the constant is strictly positive. Otherwise write the leading term as \(-Bw^2\) with \(B>0\): the polynomial starts positive, is strictly concave, tends to minus infinity, and has precisely one positive root, explicitly \(w_*\). Solving \(\chi<2+1/(\beta+1)\) gives the three seed-shape regimes in the finding. Finally, the law placing probability \(1-1/\chi\) at zero and \(1/(2\chi)\) at each of \(\pm s\sqrt\chi\) has variance \(s^2\) and fourth-moment ratio \(\chi\) for every \(\chi\ge1\), proving attainability of all shape regimes.

## Verification

The accompanying standalone `verify.py` evaluates stationary moments by exact-rational generator recurrences, independently evaluates the Gaussian affine-reset recursion using numerical quadrature for six parameter triples, and tests signs on both sides of the calculated thresholds. Running `python3 verify.py` with a standard Python interpreter returns `PASS: 577 finite deterministic checks`. The exact proof above, not these finite checks, supports the general theorem. No external data or external numerical libraries are required.

## Relationship to prior work

Gueneau, Majumdar and Schehr, arXiv:2306.09453, develop the same harmonically confined model driven by resetting Brownian noise and the affine Kesten recursion. Their detailed Brownian calculations focus on resetting the driver to the origin; those dynamics, their renewal method, and the corresponding zero-seed moment identities are established prior work, not new claims. The result here instead classifies how arbitrary nondegenerate symmetric random *driver* restart seeds switch the stationary positional excess kurtosis, including the exact seed-shape obstruction and the unique variance boundary.

Olsen, arXiv:2310.04840, gives complete moment identities for a particle whose *position* resets to a random distribution under harmonic dynamics. This is a different generator: the present particle position survives resets while its driving noise is redrawn. Shee, arXiv:2409.06920, analyzes kurtosis and non-Gaussianity for a trapped active Brownian particle under joint position and orientation resets; its propulsion and resetting mechanisms likewise differ. Both are relevant comparators rather than proofs of the present classification.

## Limitations

The proof covers symmetric seed distributions with finite fourth moment and positive variance, and no broader class. Zero excess kurtosis is a fourth-moment equality, not a claim that the full stationary law is Gaussian. No tail asymptotic, optimal control prescription, experimental validation, or universality for nonlinear traps is asserted. The claim's publication priority may be affected by unindexed analyses of randomized Brownian-driver restart amplitudes; comparison with the closest known sources is documented separately. The result has not undergone an independent scientific audit.

## References

- M. Gueneau, S. N. Majumdar and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, first public 2023-06-15, https://arxiv.org/abs/2306.09453.
- K. Stølevik Olsen, *Steady-state moments under resetting to a distribution*, first public 2023-10-07, https://arxiv.org/abs/2310.04840.
- A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, first public 2024-09-11, https://arxiv.org/abs/2409.06920.
