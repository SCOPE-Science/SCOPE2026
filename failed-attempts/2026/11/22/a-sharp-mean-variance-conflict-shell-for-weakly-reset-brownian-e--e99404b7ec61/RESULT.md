# A sharp mean–variance conflict shell for weakly reset Brownian escape from a ball

## Finding
Let \(d\ge1\) be an integer, \(D,R>0\), and \(x=\|z\|^2/R^2\in[0,1)\). A Brownian particle with generator \(D\Delta\) starts at \(z\) inside the ball of radius \(R\), is absorbed on its boundary, and is independently restored to \(z\) at Poisson rate \(\lambda\ge0\). Write \(T_\lambda\) for its completion (absorption) time and define
\[
P_d(x)=d^2(1-x)^2+12d(1-x)-48x(1+x),\qquad q_d=\frac{d}{d+4}.
\]
For every such \(d,D,R,z\), the right derivatives at zero reset rate exist and equal
\[
\left.\frac{d\mathbb E T_\lambda}{d\lambda}\right|_{0+}
=\frac{R^4}{D^2}\frac{(1-x)[d-(d+4)x]}{8d^2(d+2)},
\]
\[
\left.\frac{d\operatorname{Var}(T_\lambda)}{d\lambda}\right|_{0+}
=\frac{R^6}{D^3}\frac{(1-x)P_d(x)}{24d^3(d+2)(d+4)}.
\]
The polynomial \(P_d\) has exactly one root \(x_d\) in \((0,1)\), and \(0<x_d<q_d<1\). Therefore, **in the nonempty radial shell**
\[
R\sqrt{x_d}<\|z\|<R\sqrt{\frac{d}{d+4}},
\]
any sufficiently weak positive resetting strictly *increases* mean escape time but strictly *decreases* its variance. At smaller squared radii than \(x_d\), both derivatives are positive; above \(q_d\), both are negative. At either threshold the corresponding first-order derivative vanishes; no second-order sign is asserted. There is no open radial shell in which weak resetting lowers the mean while increasing the variance.

In three dimensions, the variance boundary is exactly \(x_3=5/13\), whereas the previously known mean boundary is \(q_3=3/7\). As \(d\to\infty\),
\[
x_d=1-\frac{2\sqrt{33}-6}{d}+O(d^{-2}),\qquad
q_d-x_d=\frac{2\sqrt{33}-10}{d}+O(d^{-2}).
\]
The latter is a squared-radius width, not a physical length.

## Assumptions and scope
There are no absorbing targets other than the entire spherical boundary. Resets return the whole particle position instantly to the fixed **initial** point; the diffusion restarts with independent Brownian increments, and absorption stops all resets. There is no reset overhead, drift, reaction delay, or measurement error. The claims are local in reset rate \(\lambda\downarrow0\), not global optimal-rate classifications. The center \(z=0\) is included; the boundary itself is excluded because absorption there is immediate. In one dimension, the ball is an interval with two absorbing endpoints.

## Proof
Set \(\tau=T_0\), \(m_j=\mathbb E\tau^j\), and let \(\phi(s)=\mathbb E e^{-s\tau}\). Since Brownian escape from a bounded ball has an exponentially decreasing survival tail, all moments and the required derivatives around \(s=0\) exist. For a Poisson clock, the standard renewal equation gives the Laplace transform of survival under resetting,
\[
\widetilde S_\lambda(s)=\frac{1-\phi(s+\lambda)}{s+\lambda\phi(s+\lambda)}.
\]
Consequently, for \(\lambda>0\),
\[
\mathbb ET_\lambda=\frac{1-\phi(\lambda)}{\lambda\phi(\lambda)},\qquad
\operatorname{Var}(T_\lambda)=\frac{1-\phi(\lambda)^2+2\lambda\phi'(\lambda)}{\lambda^2\phi(\lambda)^2}.
\]
Expand \(\phi(s)=1-m_1s+\frac12m_2s^2-\frac16m_3s^3+O(s^4)\). Differentiation at zero yields the general, independently checkable sensitivity identities
\[
\left.\frac{d\mathbb ET_\lambda}{d\lambda}\right|_{0+}=m_1^2-\frac12m_2,
\]
\[
\left.\frac{d\operatorname{Var}(T_\lambda)}{d\lambda}\right|_{0+}=-2m_1^3+3m_1m_2-\frac23m_3.
\]
These are sensitivity identities, not an assumption of a Gaussian completion-time law.

To calculate the three *unreset* moments, put \(a=R^2/D\), \(x=\|z\|^2/R^2\), and \(m_n=a^n u_n(x)\). The backward equations \(D\Delta m_n=-nm_{n-1}\), \(m_n(R)=0\), and regularity at the center give
\[
4x u_n''(x)+2d u_n'(x)=-n\,u_{n-1}(x),\qquad u_0=1,\qquad u_n(1)=0.
\]
Integrating successively gives
\[
u_1=\frac{1-x}{2d},\qquad
u_2=\frac{(1-x)[d(1-x)+4]}{4d^2(d+2)},
\]
\[
u_3=\frac{(1-x)[d^2(1-x)^2+12d(1-x)+48]}{8d^3(d+2)(d+4)}.
\]
Insertion into the two sensitivity identities, followed by factoring, produces precisely the two displayed formulas. This calculation fixes the diffusion normalization \(D\Delta\), not \(\frac D2\Delta\).

Finally,
\[
P_d(0)=d(d+12)>0,\quad P_d(1)=-96<0,\quad
P_d'(x)=-2d^2(1-x)-12d-48(2x+1)<0
\]
throughout \([0,1]\), so there is one root. At the known mean threshold, direct substitution gives
\[
P_d(q_d)=-\frac{32d^2}{(d+4)^2}<0,
\]
proving \(x_d<q_d\). For \(d=3\), \(P_3(x)=-3(13x-5)(x+3)\), so \(x_3=5/13\). For the large-d expansion, put \(x=1-c/d+O(d^{-2})\) in \(P_d(x)=0\); the unique positive solution of \(c^2+12c-96=0\) is \(c=2\sqrt{33}-6\). These algebraic facts prove the complete first-order phase ordering, including the strict conflict shell.

## Verification
`CHECK.py` symbolically reconstructs the moment recurrences, derivatives, sign polynomial, and the exact three- and four-dimensional roots. As a separate calculation, it uses the independent free-exit Laplace transform
\[
\phi(s)=\frac{{}_0F_1(;d/2;\,s\|z\|^2/(4D))}{{}_0F_1(;d/2;\,sR^2/(4D))}
\]
with high-precision numerical differentiation to test the full reset moment formulas at small positive rates in dimensions \(1,2,3,4,8,20\), inside all three sign regimes. Reproduce using `python CHECK.py` with `sympy` and `mpmath`. The observed checker output is `PASS 97 assertions`. The analytic sign and root arguments, not numerical testing, prove the statements uniformly in \(d\) and \(x\).

## Relationship to prior work
Chen and Huang (first public preprint 23 September 2021) derived the full survival-resolvent relation and the mean-benefit boundary \(q_d=d/(d+4)\) for precisely this absorbing ball. Neither the renewal identity nor the mean boundary is claimed as new. The addition is a **third-moment-based sharp variance boundary** and the strict ordering \(x_d<q_d\), which identifies a nonempty region of opposing mean and variance responses in *every* dimension. Méndez, Flaquer-Galmés and Campos (2024) investigate first-passage variance and coefficient of variation for distributed resetting of a one-dimensional unbounded searcher, not the weak-reset variance/mean shell in an absorbing ball. General work on restarting and fluctuating first-passage times supplies the broader context but does not itself state this ball-specific sign classification. The result is an explicit consequence of general prior transforms after new higher-moment and sign analysis, and publication priority for such consequences requires independent assessment.

## Limitations
Only the derivative at \(\lambda=0+\) is classified. Strict signs guarantee the corresponding change for sufficiently small \(\lambda>0\) **at each fixed interior starting point**, without a uniform reset-rate interval as the starting point approaches either threshold. No claim is made about global optima, the coefficient of variation, finite resetting overhead, partial absorption, or annular boundaries. The algebraic shell classification is not an independently audited or formally certified theorem. The exact full completion-time transform in earlier literature means implicit prior coverage remains a genuine priority risk.

## References
1. H. Chen and F. Huang, *First passage of a diffusing particle under stochastic resetting in bounded domains with spherical symmetry*, arXiv:2109.11101 (first posted 2021-09-23), Phys. Rev. E **105**, 034109 (2022). https://arxiv.org/abs/2109.11101
2. V. Méndez, R. Flaquer-Galmés, and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (2024). https://arxiv.org/abs/2401.01125
3. S. Reuveni, *Optimal Stochastic Restart Renders Fluctuations in First Passage Times Universal*, Phys. Rev. Lett. **116**, 170601 (2016). https://doi.org/10.1103/PhysRevLett.116.170601
4. S. Belan, *Median and mode in first passage under restart*, Phys. Rev. Research **2**, 013243 (2020). https://arxiv.org/abs/1906.05619
