# Optimal directional switching and a two-thirds cusp on a persistent-particle ring

## Finding

For one particle on the cyclic lattice \(\mathbb Z/n\), with \(n\ge4\), clockwise and anticlockwise hops at rate \(p>0\), and asymmetric changes of orientation at rates \(u(1-\delta)\) and \(u(1+\delta)\), let \(\gamma_n(u)\) denote the spectral gap of the full \(2n\)-state continuous-time Markov generator. Fix \(0<\delta<1\), and put \(\theta=2\pi/n\).

There is a **unique** switching intensity \(u_*>0\) that maximizes this gap. Let \(t_\delta\in(1,1/\delta)\) be the unique root of
\[
 t_\delta^3+t_\delta^2-t_\delta=\delta^{-2}.
\]
Define
\[
 a_\delta=\sqrt{\frac{1-\delta^2t_\delta^2}{t_\delta^2-1}},\quad
 z_\delta=t_\delta a_\delta,\quad
 c_\delta=(t_\delta-1)a_\delta.
\]
Then the **exact global optimum** is
\[
 \boxed{u_*=p\sin\theta\,z_\delta,\qquad
 \max_{u>0}\gamma_n(u)=p(1-\cos\theta)+p\sin\theta\,c_\delta.}
\]
As the directional bias is removed, the optimizer and improvement have nonanalytic small-bias laws:
\[
 z_\delta=1-\tfrac12\delta^{2/3}+O(\delta^{4/3}),\qquad
 c_\delta=1-\tfrac32\delta^{2/3}+O(\delta^{4/3}).
\]
For fixed \(\delta\in(0,1)\), the optimized gap is \(2\pi pc_\delta/n+O(n^{-2})\), whereas fixed \(u>0\) gives \(\gamma_n(u)=\Theta(n^{-2})\). The previously studied symmetric case \(\delta=0\) has \(u_*=p\sin(2\pi/n)\) and is **not claimed as new**; the contribution is the complete asymmetric optimization and sharp \(2/3\)-power bias rounding.

## Assumptions and scope

At each site \(j\in\mathbb Z/n\), the particle has orientation \(\sigma\in\{+,-\}\). At exponential rate \(p\), a \(+\) particle moves to \(j+1\) and a \(-\) particle moves to \(j-1\). Independently, \(+\to-\) occurs at rate \(r=u(1-\delta)\), while \(-\to+\) occurs at rate \(q=u(1+\delta)\). The dimensionless direction bias obeys \(0<\delta<1\); the tunable reversal scale is \(u>0\). The generator has the unique stationary eigenvalue zero. Its **full-state spectral gap** is \(\gamma_n(u)=\min\{-\operatorname{Re}\lambda:\lambda\in\operatorname{spec}Q,\lambda\ne0\}\); this is an eigenvalue decay rate, not an assertion about optimal total-variation mixing or transient nonnormal amplification.

## Proof

**1. Fourier blocks.** Fourier decomposition in \(j\) gives for \(\phi_k=2\pi k/n\), \(0\le k<n\), the blocks (on column probabilities)
\[
 Q_k=\begin{pmatrix}
 p(e^{-i\phi_k}-1)-u(1-\delta)&u(1+\delta)\\
 u(1-\delta)&p(e^{i\phi_k}-1)-u(1+\delta)
 \end{pmatrix}.
\]
Its eigenvalues are
\[
 \lambda_{k,\pm}=p(\cos\phi_k-1)-u
 \pm\sqrt{u^2-p^2\sin^2\phi_k-2i\delta up\sin\phi_k}.
\]
The displayed imaginary sign follows the chosen Fourier convention; replacing it by its conjugate changes no eigenvalue real parts. At \(k=0\), the eigenvalues are exactly \(0,-2u\).

**2. The first Fourier frequency is gap-dominating apart from the homogeneous tumble mode.** Write
\[
 B_u(v)=\operatorname{Re}\sqrt{u^2-v^2+2i\delta uv}\quad(v\ge0),
\]
with nonnegative real square-root part. For \(x=v^2\),
\[
 B_u(v)^2=\frac{\sqrt{(u^2-x)^2+4\delta^2u^2x}+u^2-x}{2}.
\]
This is strictly decreasing in \(x\): if \(D=\sqrt{(u^2-x)^2+4\delta^2u^2x}\), then
\[
 \frac{d B_u^2}{dx}=\frac12\left(\frac{x+(2\delta^2-1)u^2}{D}-1\right)<0,
\]
because \(D^2-[x+(2\delta^2-1)u^2]^2=4\delta^2(1-\delta^2)u^4>0\). For wave numbers folded to \([0,\pi/2]\), both \(1-\cos\phi\) and \(-B_u(p\sin\phi)\) increase with \(\phi\), so the slowest nonzero such spatial mode is \(\theta=2\pi/n\). For wave numbers folded into \((\pi/2,\pi]\), decay is at least \(p(1-\cos\phi)\), since \(B_u(v)\le u\). Moreover the first-mode decay never exceeds
\[
 p(1-\cos\theta+\sin\theta),
\]
since \(B_u(v)\ge\sqrt{\max\{0,u^2-v^2\}}\), and the maximum of \(u-\sqrt{\max\{0,u^2-v^2\}}\) over \(u>0\) is \(v\). For \(n\ge8\), \(\theta\le\pi/4\), so \(1-\cos\theta+\sin\theta\le1\), whereas every negative-cosine mode decays at least at rate \(p\). For \(n=4,5,6,7\), direct trigonometric comparison of the smallest negative-cosine wave number gives the respective lower bounds \(2p\), \((1+\cos(\pi/5))p\), \(3p/2\), and \((1+\cos(3\pi/7))p\), each at least \(p(1-\cos\theta+\sin\theta)\). (For \(n=7\) the gap of these bounds is greater than \(0.06p\).) Consequently, **for all \(n\ge4\) and all \(u>0\)**,
\[
 \gamma_n(u)=\min\left\{2u,\ p(1-\cos\theta)+u-B_u(p\sin\theta)\right\}.
\]

**3. Optimize the nontrivial spatial mode.** Scale \(z=u/(p\sin\theta)\) and put \(a=\operatorname{Re}\sqrt{z^2-1+2i\delta z}>0\). If \(b\) is the imaginary part, then \(ab=\delta z\) and \(a^2-b^2=z^2-1\). Thus
\[
 z^2=\frac{a^2(a^2+1)}{a^2+\delta^2},\qquad
 t=\frac za=\sqrt{\frac{a^2+1}{a^2+\delta^2}}.
\]
As \(z\) increases from zero to infinity, \(t\) decreases bijectively from \(1/\delta\) to \(1\). The normalized improvement \(F_\delta(z)=z-a>0\) satisfies
\[
 F_\delta(z)^2=\frac{(t-1)(1-\delta^2t^2)}{t+1}.
\]
Its derivative with respect to \(t\) has the sign of \(1-\delta^2(t^3+t^2-t)\). Since \(t^3+t^2-t\) is strictly increasing on \((1,\infty)\), there is precisely one interior maximum, at the root \(t_\delta\) stated above. The root belongs to \((1,1/\delta)\): the derivative sign is positive at \(t=1\), and negative at \(t=1/\delta\). Thus the first-mode decay has the unique maximum stated in the Finding.

**4. Show the homogeneous mode does not spoil the optimum.** The stationarity equation gives \(a_\delta^2=1/(t_\delta^2+t_\delta-1)\), and therefore
\[
 z_\delta+a_\delta=\frac{t_\delta+1}{\sqrt{t_\delta^2+t_\delta-1}}>1.
\]
For \(n\ge4\), \((1-\cos\theta)/\sin\theta=\tan(\theta/2)\le1\), hence \(2u_*\) is no smaller than the spatial decay rate at \(u_*\). Therefore \(\gamma_n(u_*)\) attains the spatial-mode upper bound, and no other \(u\) can attain it because the spatial-mode maximum is unique.

**5. Singular-bias and size limits.** Write \(\varepsilon=\delta^{2/3}\). The root equation yields \(t_\delta=\varepsilon^{-1}(1-\varepsilon/3+O(\varepsilon^2))\); substitution gives \(z_\delta=1-\varepsilon/2+O(\varepsilon^2)\) and \(c_\delta=1-3\varepsilon/2+O(\varepsilon^2)\). For fixed positive \(u\), expanding the first Fourier eigenvalue gives
\[
 \gamma_n(u)=\left(\frac p2+\frac{(1-\delta^2)p^2}{2u}\right)\theta^2+O(\theta^4),
\]
so the optimized \(O(n^{-1})\) relaxation contrasts with the fixed-\(u\) \(O(n^{-2})\) gap. The displayed asymptotics are for \(\delta\in(0,1)\); the \(\delta=0\) endpoint recovers the established symmetric exceptional-point formula and is not the subject of the novelty claim.

## Verification

Run `python verify.py` with `numpy` and `scipy` installed (versions are not critical for exact formulas). The checker separately constructs the complete \(2n\times2n\) real Markov generator, computes numerical eigenvalues, and compares the full spectral gap to all Fourier blocks for \(4\le n\le27\), seven bias levels and eight switching-rate ratios: **1,344 matrix comparisons**. It also numerically maximizes the full spectral-gap expression near the predicted optimum for each tested \((n,\delta)\), and checks the \(2/3\)-power asymptotics. These are finite tests, **not** the all-size proof: that is the preceding algebraic argument. The code and this document are self-contained; no external dataset or hidden transcript is needed.

## Relationship to prior work

Slowman, Evans and Blythe (arXiv:1601.00954, first public 2016-01-05) introduced an interacting periodic-lattice run-and-tumble process with symmetric reversals. Mallmin, Blythe and Evans (arXiv:1810.00813) explicitly solved the **symmetric** one-particle spectrum and showed that optimizing its spatial relaxation gives the exceptional-point threshold \(u=p\sin(2\pi/n)\); that result is prior, despite the paper's later revision. Mallmin, Blythe and Evans (arXiv:1905.10260) already give the **exact general two-rate Fourier/generating block** for the directionally asymmetric lattice run-and-tumble walker (their Eqs. (2.10)–(2.11)); substituting equal left/right hop magnitudes produces the Fourier matrix used in Step 1 above. Their main results concern infinite-line velocity/occupation large deviations (and include a finite-ring numerical spectrum illustration), but do **not** state the unique finite-ring global gap optimum, its monotone cubic characterization, or the singular bias-cusp rounding. Singh, Sabhapandit and Kundu (arXiv:2004.11041) study *asymmetric* direction reversals but in a position-dependent one-dimensional unbounded-medium model, not the uniform finite-ring spectral-gap optimization. Thus the novelty is **the global full-generator gap optimum** and an explicit cusp-rounding exponent \(2/3\). The symmetric optimization is not repackaged as a new finding.

## Limitations

The theorem concerns one particle, homogeneous nearest-neighbor cyclic jumps, fixed bias fraction \(0<\delta<1\), \(n\ge4\), and the spectral gap of the full generator. It does not assert total-variation, cutoff, entropy-production, interacting-particle, or arbitrary graph optimality; the spectral-gap optimization alone does not control transient nonnormal effects. It is not a claim about uniqueness in all literature: historical source indexing and older spectral studies may be incomplete. The finite numerical checks support but cannot replace the analytic proof. Independent scientific audit has not been performed.

## References

1. A. B. Slowman, M. R. Evans, R. A. Blythe, *Jamming and Attraction of Interacting Run-and-Tumble Random Walkers*, arXiv:1601.00954 (v1 2016-01-05), https://arxiv.org/abs/1601.00954 .
2. E. Mallmin, R. A. Blythe, M. R. Evans, *Exact spectral solution of two interacting run-and-tumble particles on a ring lattice*, arXiv:1810.00813 (v1 2018-10-01), https://arxiv.org/abs/1810.00813 .
3. P. Singh, S. Sabhapandit, A. Kundu, *Run-and-Tumble particle in inhomogeneous media in one dimension*, arXiv:2004.11041 (v1 2020-04-23), https://arxiv.org/abs/2004.11041 .
4. E. Mallmin, R. A. Blythe, M. R. Evans, *A comparison of dynamical fluctuations of biased diffusion and run-and-tumble dynamics in one dimension*, arXiv:1905.10260 (v1 2019-05-24), https://arxiv.org/abs/1905.10260 .
5. M. Diaconis, S. Holmes, R. M. Neal, *Analysis of a nonreversible Markov chain sampler*, Ann. Appl. Probab. 10 (2000), https://doi.org/10.1214/aoap/1019487508 .
