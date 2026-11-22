# Three scaling regimes for the jammed-count fluctuation peak in charge-selective parking

## Finding

For the charge-dependent continuum random sequential adsorption model defined below, the unique length in the first nontrivial shell at which the **variance of the final number of adsorbed unit segments** is maximal undergoes a sharp three-regime transition as the charge-selective beta kernels approach their singular endpoint.

Write \(t=1-\lambda\downarrow0\). Fix the two external boundary charges \(\alpha,\beta\in\{+,-\}\) and independently select each incoming segment's left and right endpoint charges with \(\Pr(+)=p\in(0,1)\). Define the matching probabilities \(m_+=p\), \(m_-=1-p\), and
\[
w=1-m_\alpha m_\beta\in(0,1).
\]
For each \(0\le\lambda<1\), let \(x_*(\lambda;\alpha,\beta,p)\in(2,3)\) be the unique global maximizer, over \(2<x<3\), of \(\operatorname{Var}N_{\alpha\beta}(x)\), where \(N_{\alpha\beta}(x)\) is the terminal number of adsorbed unit segments. Put \(\delta_*(t)=x_*(1-t;\alpha,\beta,p)-2\).

The exact maximum is \(\operatorname{Var}N_{\alpha\beta}(x_*)=1/4\) for every \(t\in(0,1]\). Its location obeys precisely one of the following:

1. If \(w>1/2\), then
\[
\lim_{t\downarrow0} t\log\frac1{\delta_*(t)}=\log(2w)>0.
\]
Thus the optimal excess length is exponentially small in \(1/t\).

2. If \(w=1/2\), then
\[
\delta_*(t)\sim\sqrt{\frac{t\log(1/t)}{12}}.
\]
The square-root logarithmic scale is the unique critical crossover, not either adjacent limit.

3. If \(w<1/2\), then \(\delta_*(t)\to\delta_0\in(0,1)\), where, with \(e_0=\delta_0/(1+\delta_0)\), \(e_0\) is the unique solution in \((0,1/2)\) of
\[
6e_0^2-4e_0^3=\frac{1/2-w}{1-w}.
\]

For mixed boundary charges \((\alpha,\beta)=(+,-)\) or \((-,+)\), \(w=1-p(1-p)\ge3/4\), so only the exponential regime occurs. For equal positive boundaries, the critical mixture is \(p=1/\sqrt2\); for equal negative boundaries, it is \(p=1-1/\sqrt2\). These are exact composition thresholds for the scale on which the terminal count is maximally uncertain.

## Assumptions and scope

A gap has length \(x>0\) and fixed endpoint charges \(\alpha,\beta\in\{+,-\}\). If \(x<1\), it is jammed. If \(x\ge1\), a unit segment with charges \(\sigma,\tau\) is drawn independently, with independent endpoint probabilities \(\Pr(\sigma=+)=\Pr(\tau=+)=p\in(0,1)\). Its normalized left-end placement \(Y\in(0,1)\) has the beta distribution with shapes
\[
a=1+\lambda q_\alpha q_\sigma,\qquad b=1+\lambda q_\tau q_\beta,\qquad q_+=1,\quad q_-=-1,\quad0\le\lambda<1.
\]
The placed segment leaves gaps of lengths \((x-1)Y\) and \((x-1)(1-Y)\), which evolve recursively and independently conditional on this deposition. This is the accepted-deposition recursion, not a temporal model for rejected arrival attempts. We consider exclusively \(x\in(2,3)\), so the terminal count is either one or two. The density of the placement kernel remains strictly positive for all \(0\le\lambda<1\).

The result describes the **location of the finite-shell terminal-count variance peak**, not the bulk jamming-density variance or a correlation-time optimum. It does not assert new exact finite-shell probabilities: those are already given in the underlying 2026 source. The new assertion is the sharp three-regime singular asymptotic classification of the unique peak and its composition boundary.

## Proof

**1. Exact binary reduction.** Put \(\delta=x-2\in(0,1)\) and \(e=\delta/(1+\delta)\in(0,1/2)\). After the first unit segment, a second one fits if and only if at least one daughter gap has length at least one. Since the total daughter-gap length is \(x-1=1+\delta<2\), these events are disjoint except for null boundary events. Hence
\[
N_{\alpha\beta}(x)=1+\mathbf1_{\{Y<e\}\cup\{Y>1-e\}}.
\]
Let \(I_e(a,b)\) denote the regularized incomplete beta function. For shapes \(a,b>0\), the probability of the indicated endpoint event is
\[
H_{a,b}(e)=I_e(a,b)+I_e(b,a).
\]
Write \(t=1-\lambda\in(0,1]\) and denote three endpoint classes:
\[
R_t(e)=H_{2-t,2-t}(e),\quad M_t(e)=H_{t,2-t}(e),\quad A_t(e)=H_{t,t}(e).
\]
Here \(R\) has two like-charge (repulsive) contacts, \(M\) one opposite-charge (attractive) contact, and \(A\) two attractive contacts. Set
\[
q=m_\alpha m_\beta,\qquad h=m_\alpha(1-m_\beta)+(1-m_\alpha)m_\beta,\qquad k=(1-m_\alpha)(1-m_\beta).
\]
Thus \(q+h+k=1\), \(w=h+k=1-q\), and the exact Bernoulli success parameter is
\[
P_t(e):=\Pr(N_{\alpha\beta}(2+\delta)=2)=qR_t(e)+hM_t(e)+kA_t(e).
\]
Consequently \(\operatorname{Var}N=P_t(e)(1-P_t(e))\). Each function \(R_t,M_t,A_t\) is strictly increasing and continuous on \((0,1/2)\), with limiting values zero at \(e=0\) and one at \(e=1/2\). Since \(q,h,k\ge0\) and sum to one, \(P_t\) is likewise strictly increasing from zero to one. Therefore a unique \(e_*(t)\in(0,1/2)\) solves \(P_t(e_*)=1/2\), and the variance attains its unique maximum \(1/4\) there; \(\delta_*(t)=e_*(t)/(1-e_*(t))\).

**2. Fixed-excess singular kernel limits.** For fixed \(e\in(0,1/2)\), beta weak convergence gives
\[
\operatorname{Beta}(2-t,2-t)\Rightarrow\operatorname{Beta}(2,2),\quad
\operatorname{Beta}(t,2-t)\Rightarrow\delta_0,\quad
\operatorname{Beta}(t,t)\Rightarrow\tfrac12(\delta_0+\delta_1).
\]
Thus
\[
R_t(e)\to G(e):=6e^2-4e^3,\qquad M_t(e)\to1,\qquad A_t(e)\to1,
\]
so \(P_t(e)\to w+(1-w)G(e)\). Since \(G\) increases strictly from zero to one on \((0,1/2)\), when \(w<1/2\) this limit crosses \(1/2\) at the unique stated \(e_0\). Monotonic root bracketing at any two fixed values surrounding \(e_0\) proves \(e_*(t)\to e_0\), and hence the third regime.

**3. Exponential window.** Fix \(s>0\) and let \(e=e^{-s/t}\). The beta integral and gamma normalization yield
\[
\begin{aligned}
M_t(e)&=\frac{e^t}{tB(t,2-t)}(1+O(te))+O(t e^{2-t}),\\
A_t(e)&=\frac{2e^t}{tB(t,t)}(1+O(te)),\\
R_t(e)&=O(e^{2-t}),
\end{aligned}
\]
where the estimates hold as \(t\downarrow0\) for the stated exponential window. Moreover \(tB(t,2-t)\to1\) and \(tB(t,t)\to2\). Therefore
\[
P_t(e^{-s/t})\longrightarrow w e^{-s}.
\]
If \(w>1/2\), put \(s_*=\log(2w)>0\). For any \(0<s_-<s_*<s_+\), the limiting probabilities satisfy \(we^{-s_-}>1/2>we^{-s_+}\). By strict monotonicity, for sufficiently small \(t\) the maximizing \(e_*(t)\) is between \(e^{-s_+/t}\) and \(e^{-s_-/t}\). Thus \(-t\log e_*(t)\to s_*\). Since \(\delta=e/(1-e)\) and \(e\to0\), \(-t\log\delta_*(t)\to s_*\), proving the first regime.

**4. Critical square-root logarithmic window.** Suppose \(w=q=1/2\). Fix a constant \(c>0\), set \(e=c\sqrt{t\log(1/t)}\), and take \(t\downarrow0\). The preceding beta-integral estimates remain valid uniformly for such \(e\), with
\[
M_t(e)=e^t[1+O(t+te)]+O(te^{2-t}),\qquad
A_t(e)=e^t[1+O(t+te)],
\]
while
\[
R_t(e)=6e^{2-t}[1+O(t+e)].
\]
Since \(t\log e=-(t/2)\log(1/t)+o(t\log(1/t))\), we have
\[
M_t(e)=1-\tfrac t2\log(1/t)+o(t\log(1/t)),\quad
A_t(e)=1-\tfrac t2\log(1/t)+o(t\log(1/t)),
\]
and \(R_t(e)=6c^2t\log(1/t)+o(t\log(1/t))\). Therefore
\[
\frac{P_t(e)-1/2}{t\log(1/t)}\longrightarrow 3c^2-\frac14.
\]
The limiting expression changes sign precisely at \(c_*=1/\sqrt{12}\). Bracket the unique root between \(c_-\sqrt{t\log(1/t)}\) and \(c_+\sqrt{t\log(1/t)}\) for arbitrary \(0<c_-<c_*<c_+\). It follows that
\[
e_*(t)\sim\sqrt{t\log(1/t)/12}.
\]
As \(\delta_*=e_*/(1-e_*)\) and \(e_*\to0\), the same equivalent holds for \(\delta_*\), proving the second regime. This completes all cases and establishes the claimed sharp thresholds.

## Verification

The attached standalone program `verify.py` independently reconstructs the three beta endpoint probabilities from `scipy.special.betainc`, solves the unique median condition with bracketed root finding, tests symmetry and monotonicity, checks the limiting fixed-excess equation, and numerically compares each of the three scaling predictions over decreasing \(t\). It also checks the exact Bernoulli variance and compares direct beta-distribution simulations with the integral probability at nonsingular parameters. Run `python verify.py` with Python 3, NumPy and SciPy available. The numerical comparisons are reproducibility checks; the proof of the limiting laws is the analytic argument above, not any finite computation.

## Relationship to prior work

Palacios and Macêdo (2026), arXiv:2608.28289v1, introduce precisely the charge-dependent beta placement model, derive the four-state full-counting-statistics recursion, and explicitly give the binary second-shell law and its mean and variance. Their exact formulas are the admitted starting point and are **not** claimed here as new. The present contribution proves a three-regime asymptotic law for the location, rather than the value, of the finite-shell variance maximum as \(\lambda\uparrow1\): exponential concentration, a critical \(\sqrt{t\log(1/t)}\) window with exact coefficient, or convergence to a positive excess length. The 2026 paper's fixed-parameter figures and thermodynamic large-gap densities do not state or analyze this singular peak-location classification.

Palacios and Macêdo (2025), *Random sequential adsorption of charged segments on a line*, study an earlier deterministic charge-oriented deposition scheme; its available abstract and the 2026 source describe a different placement family and no above singular-window peak theorem. A related previously reported fixed-coupling near-integer threshold result (opaque identifier `056f1bba-c7c4-43ab-a307-3626f12c2f99`) concerns the power of \(\delta\downarrow0\) for a restricted self-renewing dipolar channel at fixed \(t>0\) and arbitrary integer shell. It neither provides a uniform \(t\downarrow0\) estimate nor locates the fluctuation maximum for the independently sampled four-type mixture. In particular, a fixed-\(t\) exponent does not yield the critical \(1/\sqrt{12}\) coefficient without singular-limit analysis.

## Limitations

The result holds only in the exactly binary terminal-count shell \(2<x<3\) and for fixed \(p\in(0,1)\). It does not give a global thermodynamic variance maximum or a scaling law when \(p\) itself approaches its critical threshold jointly with \(t\). The three regimes are asymptotic statements, not error-certified numerical approximations for arbitrary finite \(t\). Mathematical correctness does not settle independent publication priority; unindexed equivalent analyses and unavailable portions of older related literature remain possible.

## References

1. G. Palacios and A. M. S. Macêdo, *A Generalized Model for Disordered Random Sequential Adsorption with Charge-Dependent Deposition*, arXiv:2608.28289v1 (first submitted 28 August 2026). https://arxiv.org/abs/2608.28289
2. G. Palacios and A. M. S. Macêdo, *Random sequential adsorption of charged segments on a line*, Physical Review E **112**, 064128 (2025), DOI:10.1103/qtpz-3bfj. https://doi.org/10.1103/qtpz-3bfj
3. Related fixed-coupling near-threshold exponent theorem, opaque identifier `056f1bba-c7c4-43ab-a307-3626f12c2f99` (distinct restricted placement model and limit order).
