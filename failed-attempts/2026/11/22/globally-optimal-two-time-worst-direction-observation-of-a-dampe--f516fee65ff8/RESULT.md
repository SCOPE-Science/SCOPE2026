# Globally optimal two-time worst-direction observation of a damped planar rotation

## Finding
Let \(a>0\), \(b>0\), and \(T>0\). For the planar linear flow
\[
\dot u=Au,\qquad A=\begin{pmatrix}-a&-b\\b&-a\end{pmatrix},
\]
observe the first coordinate at two freely chosen times \(0\le t_1\le t_2\le T\), with independent equal-variance measurement noise. The unique pair maximizing the smallest eigenvalue of the initial-state Fisher information matrix is
\[
(t_1,t_2)=\left(0,\min\{T,z_r/b\}\right),\qquad r=a/b,
\]
where \(z_r\) is the unique root in \((0,\pi/2)\) of
\[
 r=\cot z\left(1+\frac{e^{-2rz}}{1-\Lambda_r(z)}\right),
\quad
 \Lambda_r(z)=\frac{2e^{-2rz}\sin^2z}{1+e^{-2rz}+\sqrt{(1-e^{-2rz})^2+4e^{-2rz}\cos^2z}}.
\]
The quantity \(\Lambda_r(z)\) is the smaller eigenvalue for measurements at times \(0,z/b\), after normalizing the measurement-noise variance to one. The global maximum of the normalized worst-direction information is \(\Lambda_r(\min\{bT,z_r\})\).

Among unconstrained horizons the E-optimal phase \(z_r\) is **strictly later** than the D-optimal phase \(\arctan(1/r)\). In the weak- and strong-damping limits,
\[
 z_r=\frac\pi2-\pi r^2+O(r^3)\quad(r\downarrow0),\qquad
 z_r=\frac{c_*}{r}+O(r^{-3})\quad(r\to\infty),
\]
with \(c_*=1+\tfrac12 W(2e^{-2})=1.108857552878572\ldots\), where \(W\) is the principal Lambert function. In particular, the strong-damping optimal time tends to \(c_*/a\), while the D-optimal time tends to \(1/a\).

## Assumptions and scope
The initial state \(u(0)\in\mathbb R^2\) is an arbitrary fixed unknown vector. Dynamics and \(a,b\) are known exactly; there is no process noise. Observation noise has independent centered equal components of variance \(\sigma^2>0\) at the two measurements. Repeated times are permitted in the admissible class but are not optimal when \(T>0\). Sensor direction is fixed at the first coordinate, and continuous observation times are selected nonadaptively. The Fisher information for the initial state is \(\sigma^{-2}\) times the sum of the two observation-row outer products. The E-criterion is the *least eigenvalue*; it is not trace, determinant, or average Kalman prediction loss.

## Proof
**1. Reduction of both observation times.** For any time \(t\), the observation row is \(e^{-at}(\cos bt,-\sin bt)\). Writing \(\tau=t_2-t_1\), the two-row design matrix factors as \(e^{-at_1}\) times the design matrix at \((0,\tau)\), followed by a common orthogonal rotation. Therefore its Fisher eigenvalues equal \(e^{-2at_1}/\sigma^2\) times those for \((0,\tau)\). For every positive \(\tau\), moving both times to \((0,\tau)\) strictly increases the least eigenvalue unless \(t_1=0\). Zero separation produces rank one and zero least eigenvalue, whereas arbitrarily small positive separation produces positive information. Consequently all optima start at zero.

**2. Exact scalar eigenvalue.** Set \(z=b\tau\), \(r=a/b\), \(q=e^{-2rz}\), and \(S=\sin^2z\). The normalized Gramian is the sum of outer products of \((1,0)\) and \(\sqrt q(\cos z,-\sin z)\). Its trace is \(1+q\), determinant is \(qS\), and its smaller eigenvalue \(\lambda=\Lambda_r(z)\) is the smaller root of
\[
 \lambda^2-(1+q)\lambda+qS=0.
\]
For \(0<z<\pi/2\), \(0<\lambda<q<1\), and \(\lambda\) is smooth. The rationalized root formula in the finding avoids cancellation.

**3. Existence and uniqueness of the maximizing phase.** Differentiate the characteristic equation with respect to \(z\). With \(D=1+q-2\lambda>0\),
\[
 D\lambda'=q\{S'-2r(S-\lambda)\}.
\]
The characteristic identity also gives \(S-\lambda=S(1-\lambda)/(1+q-\lambda)\). Hence the sign of \(\lambda'\) is the sign of
\[
 F(z)=\cot z\left(1+\frac{q}{1-\lambda}\right)-r.
\]
This continuous function tends to \(+\infty\) as \(z\downarrow0\) and to \(-r\) as \(z\uparrow\pi/2\), because \(1-\Lambda_r(\pi/2)=1-e^{-\pi r}>0\). At *every* zero of \(F\), \(\lambda'=0\), so direct differentiation yields
\[
 F'(z)=-\csc^2z\left(1+\frac{q}{1-\lambda}\right)
 -2r\cot z\frac{q}{1-\lambda}<0.
\]
Thus every zero crosses strictly from positive to negative; continuity and differentiability preclude a second zero. The unique zero \(z_r\) is consequently the unique maximizer on \((0,\pi/2)\).

For all \(z\ge\pi/2\), the Rayleigh quotient on the unit vector perpendicular to the first observation row shows \(\Lambda_r(z)\le q\sin^2z\le e^{-\pi r}=\Lambda_r(\pi/2)\). Because \(\lambda\) is already strictly decreasing just before \(\pi/2\), \(\Lambda_r(z_r)>\Lambda_r(\pi/2)\). Therefore no later oscillatory lobe can compete. With a finite horizon, monotonicity before \(z_r\) gives the claimed unique clipped optimum.

**4. Distinct E- and D-optimal timing.** The determinant \(q\sin^2z\) is uniquely maximized on the first half-period when \(\cot z=r\), giving \(z_D=\arctan(1/r)\); later periods are inferior by exponential damping. At the E-optimal stationary point, \(r=\cot z_r[1+q/(1-\lambda)]>\cot z_r\), implying \(z_r>z_D\). For a finite horizon, both criteria clip their optimal phases at \(bT\).

**5. Asymptotics.** When \(r\downarrow0\), the inequality \(z_D<z_r<\pi/2\) gives \(\delta=\pi/2-z_r=O(r)\). The exact eigenvalue formula gives
\[
0\le q-\lambda\le\frac{q\cos^2z}{1-q}.
\]
Since \(1-q=\Theta(r)\) near the last quarter-period, first \(1-\lambda=O(r)\). The stationary equation then forces \(\delta=O(r^2)\), sharpening the eigenvalue difference to \(q-\lambda=O(r^3)\). Thus \(1-\lambda=\pi r+O(r^2)\), and the stationarity equation gives \(\delta=\pi r^2+O(r^3)\).

When \(r\to\infty\), write \(z=c/r\). Uniformly for \(c\) in compact subsets of \((0,\infty)\),
\[
 r^2\Lambda_r(c/r)=\frac{c^2}{1+e^{2c}}+O(r^{-2}).
\]
The bound \(0\le r^2\Lambda_r(z)\le(rz)^2e^{-2rz}\) and a fixed positive comparison value at \(c=1\) keep maximizing \(c=rz\) away from zero and infinity. The limiting function has one strictly nondegenerate maximum, at \(c_*>1\) satisfying \(c_*-1=e^{-2c_*}\), equivalent to the stated Lambert expression. Smooth expansion of the stationary equation around this nondegenerate maximum yields \(rz_r=c_*+O(r^{-2})\), hence the claimed \(O(r^{-3})\) phase remainder.

## Verification
A standalone standard-library Python verifier is included as `verify.py`, with its captured `verification_output.txt`. It directly constructs the two-row Gramian independently of the scalar formula, checks 17,000 independent arbitrary-time comparisons, and checks 22,000 additional finite-horizon/phase comparisons over ten damping ratios. It confirms the example \(a=b=1\): \(z_r=0.873069765204006\ldots\), normalized information \(0.094889681334842\ldots\). The quarter-period choice gives only \(e^{-\pi}=0.043213918263772\ldots\). All finite checks supplement, but do not establish, the continuous-domain proof above.

## Relationship to prior work
Bopardikar, *Sensor Selection via Randomized Sampling* (arXiv:1712.06511, first posted 2017-12-18), studies selection of spatial sensors and probabilistic approximation of observability Gramians, including their smallest eigenvalue. Its full preprint studies random subsets at prescribed times, not analytic optimization of two freely chosen temporal observation instants in one damped oscillator. Aspeel, Legay, Jungers and Macq (2021) study combinatorial timing for average Kalman prediction error, and analyze the scalar case; their objective is not least-eigenvalue information about a fixed two-dimensional initial state. Javeed and Hooker (2019) study adaptive timing to estimate a diffusion's model parameters; their accessible abstract does not resolve this initial-state information problem. Wu (2002) gives classical E-optimal trigonometric-regression designs on partial cycles, including weighted approximate designs; the studied regression does not have the fixed exponentially decaying amplitude and exactly two equally weighted observations imposed here. Its work illustrates a plausible path to an earlier equivalent optimal-design formulation, which remains a publication-priority risk. Indexed related results on three-time oscillator D-optimality, phaseless sampling, and jittered-time observability concern different sampling counts or criteria, and are not claimed to resolve the present theorem.

## Limitations
The result is for a known stable normal planar generator, no process noise, a fixed scalar output, exactly two equal-precision observations, and initial-state E-optimality. It does not optimize an arbitrary posterior Bayesian covariance or jointly estimate damping and frequency. A general E-optimal-design principle for regression might yield an equivalent earlier formulation; available comparisons cannot establish publication priority or novelty conclusively. The result is a closed classification for a narrow but canonical system, not an empirical performance guarantee in a physical device. Independent validation has not been performed.

## References
- S. D. Bopardikar, *Sensor Selection via Randomized Sampling*, arXiv:1712.06511 (initial public date 2017-12-18), https://arxiv.org/abs/1712.06511.
- A. Aspeel, A. Legay, R. M. Jungers, and B. Macq, *Optimal measurement budget allocation for Kalman prediction over a finite time horizon by genetic algorithms*, EURASIP J. Adv. Signal Process. (2021), https://doi.org/10.1186/s13634-021-00732-8.
- A. Javeed and G. Hooker, *Timing observations of diffusions*, Stat. Comput. (first published 2019-08-03), https://doi.org/10.1007/s11222-019-09883-z.
- H. Wu, *Optimal designs for first-order trigonometric regression on a partial cycle*, Statistica Sinica **12** (2002), https://www3.stat.sinica.edu.tw/statistica/oldpdf/A12n314.pdf.
