# Sharp reentrant mean-square instability under random shear time-splitting

## Finding

Fix \(a>0\), \(k>0\) and a step size \(h>0\). Consider the unbiased random time-splitting of the two-dimensional dissipative equation \(\dot x=Ax\), with
\[
A=-aI+\frac{k}{2}\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
B_+=-aI+k\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
B_-=-aI-k\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad A=\tfrac12(B_++B_-).
\]
At each step, independently choose \(B_+\) or \(B_-\) with probability \(1/2\), and propagate **exactly** for time \(h\). The step endpoint is \(X_{j+1}=\exp(hB_{\xi_j})X_j\) for a deterministic initial state \(X_0=x\in\mathbb R^2\).

For every integer \(n\ge0\), both growth laws are **exact**:
\[
\mathbb E\|X_n\|_2^2=f(h)^n\|x\|_2^2,\qquad
\|\mathbb E X_n\|_2^2=g(h)^n\|x\|_2^2,
\]
where
\[
f(h)=e^{-2ah}\left(1+\frac{k^2h^2}{2}\right),\qquad
g(h)=e^{-2ah}\left(1+\frac{k^2h^2}{4}\right).
\]
Let \(t_*\in(0,1)\) be the unique positive solution of \(t=1-e^{-2t}\), and put
\[
R_* = \sqrt{\frac{2}{t_*(1-t_*)}}=3.514699022529\ldots,\quad
R_{*,\mathrm{mean}}=\sqrt2\,R_*=4.970535025320\ldots .
\]
Write \(R=k/a\). If \(R<R_*\), every \(h>0\) has strict mean-square contraction; if \(R=R_*\), one step size \(h=t_*/a\) is mean-square neutral and all others contract; if \(R>R_*\), there exist unique \(0<t_-<t_*<t_+\), determined by
\[
R^2=\frac{2(e^{2t_\pm}-1)}{t_\pm^2},
\]
such that the expected squared norm grows geometrically **exactly** when \(t_-/a<h<t_+/a\), and contracts for smaller or larger positive steps. The endpoint steps are neutral.

The mean obeys the same complete classification with threshold \(R_{*,\mathrm{mean}}\) in place of \(R_*\), and mean-instability roots solving \(R^2=4(e^{2t}-1)/t^2\). In particular, throughout the nonempty parameter interval \(R_*<R<R_{*,\mathrm{mean}}\), **every** positive step is mean-stable, but an open interval of steps is mean-square unstable. This is a fixed-step long-horizon distinction, not a claim about pathwise Lyapunov instability.

## Assumptions and scope

The vector space is \(\mathbb R^2\), the norm is the Euclidean norm, and \(a,k,h\) are positive real numbers. The two random generators are independently and equiprobably sampled at each full time cell. There is no forcing, control input, numerical approximation to a matrix exponential, or correlation between successive choices. The word "stable" for the mean means \(\|\mathbb E X_n\|_2\to0\) for every deterministic \(x\); "mean-square stable" means \(\mathbb E\|X_n\|_2^2\to0\) for every deterministic \(x\). Neutral means preservation of the corresponding norm for every \(n\). Individual sampled matrices \(B_\pm\) are Hurwitz, but not necessarily dissipative in the Euclidean norm. The deterministic mean generator \(A\) is strictly dissipative, since \((A+A^{\mathsf T})/2=-aI\).

## Proof

**Exact step and second moment.** Since the shear nilpotents square to zero, with \(u=kh\) and \(s=e^{-ah}\),
\[
M_+=e^{hB_+}=s\begin{pmatrix}1&u\\0&1\end{pmatrix},\quad
M_-=e^{hB_-}=s\begin{pmatrix}1&0\\-u&1\end{pmatrix}.
\]
Direct multiplication gives
\[
\frac12(M_+^{\mathsf T}M_++M_-^{\mathsf T}M_-)
=s^2\left(1+\frac{u^2}{2}\right)I.
\]
Conditional on \(X_j\), the next independent choice consequently has
\(\mathbb E[\|X_{j+1}\|_2^2\mid X_j]=f(h)\|X_j\|_2^2\). Iterating the tower property proves the first identity for every \(n\) and every \(x\), with no distributional assumptions on \(x\) beyond being deterministic.

**Exact mean.** Independence likewise gives \(\mathbb EX_n=\bar M^nx\), where
\[
\bar M=\frac{M_++M_-}{2}
=s\begin{pmatrix}1&u/2\\-u/2&1\end{pmatrix},\qquad
\bar M^{\mathsf T}\bar M=s^2\left(1+\frac{u^2}{4}\right)I.
\]
Because \(\bar M\) is a scalar multiple of an orthogonal matrix, \(\|\bar M^nx\|_2^2=g(h)^n\|x\|_2^2\) for all \(n\). Notice that \(g(h)<f(h)\) for all positive \(h,k\).

**Sharp shape of the step-size instability window.** Write \(t=ah>0\), \(R=k/a\), and define
\[
F(t)=\frac{2(e^{2t}-1)}{t^2}.
\]
Then \(f(h)>1\) exactly when \(R^2>F(t)\). The derivative is
\[
F'(t)=\frac{4}{t^3}\big((t-1)e^{2t}+1\big).
\]
The sign is that of \(H(t)=t-1+e^{-2t}\). We have \(H(0)=0\), \(H'(0)=-1\), and \(H''(t)=4e^{-2t}>0\). Moreover \(H(t)>0\) for all \(t\ge1\). Strict convexity therefore yields precisely one additional zero \(t_*\in(0,1)\); \(F\) decreases before this zero and increases after it. Also \(F(t)\to\infty\) as \(t\downarrow0\) and \(t\to\infty\). At the minimizer, \(e^{2t_*}=1/(1-t_*)\), so
\[
\min_{t>0}F(t)=F(t_*)=\frac{2}{t_*(1-t_*)}=R_*^2.
\]
Every asserted mean-square sign region and uniqueness of both roots follows. Since \(g(h)>1\) exactly when \(R^2>2F(t)\), the mean classification is identical with threshold \(\sqrt2 R_*\). For \(R_*<R<\sqrt2R_*\), \(R^2>F(t_*)\) but \(R^2<2F(t)\) for all \(t>0\), proving strict separation. At the critical ratios the multiplier equals one only at \(t_*\); at the window endpoints it equals one, giving the neutral cases. This also proves that no other disconnected instability windows exist.

**Concrete separation.** Choosing \(a=1\), \(k=4\), and \(h=4/5\) gives \(f(h)=1.235606690127\ldots>1\) and \(g(h)=0.718751604061\ldots<1\). The two mean-square instability endpoints solve the stated equation and are \(t_-=0.370425214890\ldots\) and \(t_+=1.421336706484\ldots\). In contrast, the exact baseline semigroup is \(e^{tA}=e^{-at}\) times a rotation, contracting at every positive elapsed time.

## Verification

The included standalone file `check.py` uses exact rational arithmetic to enumerate all \(2^n\) shear choices for several rational \(u=kh\), non-axis-aligned initial states, and all \(0\le n\le7\). It compares the enumerated second moment and mean vector with the identities above, then numerically brackets the unique critical point and the two sample roots. Run `python check.py` with Python 3 and no third-party packages. This finite checker confirms algebraic instances and numerical values; it is not a substitute for the preceding all-parameter, all-iteration proof.

## Relationship to prior work

Veldman and Zuazua [1] define independent-per-cell randomized generator sampling, including the half-probability two-submatrix case (Example 1); their convergence results concern a fixed horizon as the temporal grid is refined, and their Remark 9 notes exponential-in-time bounds without the sampled dissipativity assumption. Here the focus is instead the exact fixed-step infinite-horizon classification in a two-generator specialization. The mean generator is strictly dissipative, while the sampled generators cease to be dissipative precisely when \(k>2a\). Sturman and Thiffeault [2] analyze random products of positive and negative shear matrices with bounds on ordinary and generalized Lyapunov exponents; their negative-shear results supply closely related dynamics but do not state these explicit damped time-splitting mean/mean-square thresholds in the inspected text. Gog and collaborators [3] establish noise-driven destabilization for nonnormal shears and exhibit stability windows under alternating or symmetry-related switching. Thus *reentrant shear instability in general is known*; the specific claim here is the exact complete phase diagram for **independently sampled** balanced shear generators and its strict first/second-moment separation. Standard moment-product methods could conceivably yield equivalent facts by specialization.

## Limitations

The threshold concerns mean-square and mean growth of grid-point iterates for exact independently drawn shear subflows. It is not a criterion for almost-sure Lyapunov growth, general nonlinear systems, correlated draws, unequal selection probabilities, arbitrary matrix splittings, time discretization error with fixed terminal time, or closed-loop optimal-control performance. The exact second-moment identity exploits a special isotropy of the equal-magnitude opposite shears. Publication precedence has not been independently established, and general moment-radius theory might imply some conclusions without stating this normalization.

## References

[1] D. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, first available 28 September 2021, https://arxiv.org/abs/2109.13798 .

[2] R. Sturman and J.-L. Thiffeault, *Lyapunov Exponents for the Random Product of Two Shears*, published online 21 September 2018, https://doi.org/10.1007/s00332-018-9497-3 .

[3] J. R. Gog, I. Oprea, M. R. E. Proctor, and A. M. Rucklidge, *Destabilization by noise of transverse perturbations to heteroclinic cycles: a simple model and an example from dynamo theory*, 1999, https://doi.org/10.1098/rspa.1999.0498 .
