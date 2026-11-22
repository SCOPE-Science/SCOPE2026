# A universal Laplace-profile correction for rapid stochastic returns

## Finding

For a one-dimensional search which alternates between Ornstein–Uhlenbeck exploration and target-visible Ornstein–Uhlenbeck home returns, the **entire one-parameter family of first-passage Laplace transforms**, not only the mean, has a sharp large-reset-frequency correction. For every fixed Laplace parameter \(s>0\),
\[
\boxed{\lim_{r\to\infty}r^{3/2}\{\mathbb E(e^{-sT_r})-\phi_s(0)\}
 =(k_2-k_1)\,\frac{\sqrt\pi\,s\phi_s(0)}{C_s}
 \frac{\mathbb E[W^2]}{\mathbb E[\sqrt W]}.}
\]
Here \(W/r\) is an arbitrary independent positive renewal interruption clock with finite second moment, \(\phi_s(0)\) is the Laplace transform of the uninterrupted *return* process's hitting time of the target, and \(C_s>0\) is the derivative jump of an explicitly defined discounted return-to-home probability at the resetting position. The entire \(s\)-dependent coefficient separates into one **clock factor** and one **diffusion response profile**. In particular, at equal mean interruption intervals, Poisson and periodic clocks have correction amplitudes in the universal ratio \(4/\sqrt\pi\) **simultaneously for every fixed \(s>0\)**. For equal search and return stiffness, the full completion-time distribution equals the uninterrupted return hitting-time distribution for every clock scale, not just asymptotically.

## Assumptions and scope

Fix \(k_1\ge0\), \(k_2>0\), and an independent random variable \(W>0\) almost surely with \(\mathbb E[W^2]<\infty\). All variables are dimensionless. A search excursion begins at \(0\), evolves according to
\[
dX_t=-k_1X_t\,dt+\sqrt2\,dB_t,
\]
and terminates at its first hit \(\tau=\inf\{t\ge0:X_t=1\}\) of the absorbing target \(1\), or at an independent alarm \(R_r=W/r\), whichever occurs first. On alarm before absorption, a return excursion begins from the current position, follows
\[
dY_t=-k_2Y_t\,dt+\sqrt2\,d\widetilde B_t,
\]
and stops on reaching \(0\) or \(1\); if the starting point is negative, the return first reaches \(0\) before it could reach \(1\). Arrival at \(1\) in *either* phase ends the search. Arrival at \(0\) in return triggers a new independent search excursion with new Brownian noise and a new independent copy of \(W\). Let \(T_r\) be the total time to the target, including the durations of all return stages. Each independent cycle has strictly positive probability of success and finite mean length, so \(T_r<\infty\) almost surely and has finite mean at fixed \(r>0\).

Fix \(s>0\). Let \(\mathcal L_j=\partial_x^2-k_jx\partial_x\). Define, for \(x<1\), the increasing solution
\[
\phi_s(x)=\mathbb E_x^{(2)}[e^{-s\tau_1}]
\quad\text{of}\quad \mathcal L_2\phi_s=s\phi_s,\qquad
\phi_s(1)=1,\quad\lim_{x\to-\infty}\phi_s(x)=0.
\]
It is smooth, positive, strictly increasing, and satisfies \(0<\phi_s(0)<1\). Define the discounted return-to-home probability
\[
q_s(x)=\mathbb E_x^{(2)}[e^{-s\tau_0};\ \tau_0<\tau_1],\qquad x<1,
\]
where for \(x<0\) the event \(\tau_0<\tau_1\) holds automatically. Thus \(q_s(0)=1\), \(q_s(1)=0\), and \(q_s\) is smooth on \(( -\infty,0)\) and \((0,1)\), but has a cusp at \(0\). Set
\[
C_s=q_s'(0-)-q_s'(0+)>0.
\]
These definitions do not rely on a special-function convention. They also give a self-contained numerical method: solve the two return-ODE boundary problems for \(\phi_s,q_s\) and evaluate the one-sided slopes.

## Proof

**1. Discounted first-cycle renewal.** Let \(h_s(x)=\mathbb E_x^{(2)}[e^{-s\tau_1};\tau_1<\tau_0]\), with \(h_s(x)=0\) for \(x\le0\). The strong Markov property at the first return hit gives, for every \(x<1\),
\[
\phi_s(x)=h_s(x)+q_s(x)\phi_s(0).
\]
Put \(\Phi_r(s)=\mathbb E[e^{-sT_r}]\) and
\[
Q_{r,s}=\mathbb E[e^{-sR_r}q_s(X_{R_r});\ R_r<\tau],
\]
\[
B_{r,s}=\mathbb E[e^{-s\tau};\tau<R_r]
 +\mathbb E[e^{-sR_r}h_s(X_{R_r});\ R_r<\tau].
\]
The completed search consists of one successful cycle or one unsuccessful cycle followed by an independent copy. Therefore \(\Phi_r=B_{r,s}+Q_{r,s}\Phi_r\), giving \(\Phi_r=B_{r,s}/(1-Q_{r,s})\). Since \(s>0\) and a return can terminate at either boundary, \(0\le Q_{r,s}<1\).

**2. Exact discounted-potential identity.** The generator difference applied to the return hitting transform is
\[
(\mathcal L_1-s)\phi_s(x)
 =(k_2-k_1)x\phi_s'(x).
\]
Apply discounted Dynkin's formula to \(\phi_s(X_t)\) stopped at \(\tau\wedge R_r\). Boundary values and the decomposition in step 1 yield
\[
\boxed{\Phi_r(s)-\phi_s(0)=
(k_2-k_1)\frac{A_{r,s}}{1-Q_{r,s}},}\qquad
A_{r,s}=\mathbb E\int_0^{\tau\wedge R_r}
 e^{-st}X_t\phi_s'(X_t)\,dt.
\]
There is no Poisson-memoryless assumption in this identity. The stopped formula is legitimate by localization and dominated convergence: \(x\phi_s'(x)\) is bounded on \(( -\infty,1)\), and the stopped search duration is at most \(R_r\) with finite expectation.

**3. Short-excursion numerator.** Let \(f_s(x)=x\phi_s'(x)\). The return ODE gives \(\phi_s''(0)=s\phi_s(0)\), hence \(f_s(0)=0\) and \(f_s''(0)=2s\phi_s(0)\). For the centered search OU diffusion starting at \(0\), its small-time variance is \(2t+O(t^2)\). A Taylor/short-time semigroup expansion, together with the exponentially small probability of hitting \(1\) before time \(t\), proves
\[
g_s(t):=\mathbb E_0[f_s(X_t);\tau>t]
 =2s\phi_s(0)t+o(t)\quad(t\downarrow0).
\]
The function \(f_s\) is bounded on the killed domain and its centered small-time expectation is \(O(t)\), so \(|g_s(t)|\le C_s^{\mathrm{num}} t\) for all \(t>0\), for a finite constant dependent on fixed diffusion parameters and \(s\). Conditioning on \(W\) and using \(\mathbb E W^2<\infty\), dominated convergence gives
\[
\lim_{r\to\infty}r^2 A_{r,s}
 =\lim_{r\to\infty}r^2\mathbb E\int_0^{W/r}e^{-st}g_s(t)\,dt
 =s\phi_s(0)\mathbb E[W^2].
\]
This displays why the search stiffness drops out of the leading numerator: the drift is zero at the resetting point, while the local diffusion coefficient is fixed.

**4. The discounted return-to-home cusp.** Let \(u_s(t)=\mathbb E_0[e^{-st}q_s(X_t);\tau>t]\). A Brownian displacement at short time is approximately centered normal with variance \(2t\). The one-sided first-order Taylor expansions at the cusp give
\[
q_s(x)=1+q_s'(0-)x+O(x^2)\quad(x<0),\qquad
q_s(x)=1+q_s'(0+)x+O(x^2)\quad(x>0).
\]
Since \(\mathbb E(X_t)_+=\sqrt{t/\pi}+O(t^{3/2})\) and \(\mathbb E(X_t)_-=-\sqrt{t/\pi}+O(t^{3/2})\) for the centered OU search, and boundary hits are exponentially unlikely on short intervals,
\[
1-u_s(t)=\frac{C_s}{\sqrt\pi}\sqrt t+O(t).
\]
Here \(q_s'(0-)>0\) (discounted time to reach \(0\) decreases as a starting point approaches \(0\) from the left) and \(q_s'(0+)<0\) (discounted home-before-target probability decreases as a starting point approaches \(1\)), so \(C_s>0\). The bound \(0\le 1-u_s(t)\le C_s^{\mathrm{den}}\sqrt t\) holds for all \(t>0\), after enlarging the constant for \(t\ge1\), by \(0\le q_s\le1\), local Lipschitz regularity and Gaussian search moments. As \(Q_{r,s}=\mathbb E[u_s(W/r)]\), dominated convergence with \(\mathbb E\sqrt W<\infty\) yields
\[
\lim_{r\to\infty}\sqrt r(1-Q_{r,s})
 =\frac{C_s}{\sqrt\pi}\mathbb E[\sqrt W].
\]

**5. Ratio, sharpness, and clock comparison.** Dividing the limits of steps 3 and 4 in the exact step-2 identity yields the announced \(r^{-3/2}\) transform profile for every fixed \(s>0\). Every factor on the right except \(k_2-k_1\) is strictly positive, so the asymptotic coefficient is nonzero and has sign \(\operatorname{sgn}(k_2-k_1)\) whenever the stiffnesses differ. This makes the exponent sharp. For a unit-mean exponential \(W\), \(\mathbb EW^2=2\) and \(\mathbb E\sqrt W=\sqrt\pi/2\), hence the clock factor is \(4/\sqrt\pi\). For periodic \(W=1\), that factor is \(1\). Thus the ratio is exactly \(4/\sqrt\pi\) at every fixed Laplace argument, not merely at its derivative at zero. For \(k_1=k_2\), the exact step-2 identity gives \(\Phi_r(s)=\phi_s(0)\) for every \(r,s>0\); uniqueness of Laplace transforms gives equality of the whole hitting-time laws.

## Verification

Run `python CHECKER.py` with Python, SciPy and NumPy installed. The standalone checker evaluates the return-OU fundamental solutions using parabolic-cylinder functions; checks their boundary data, positivity and backward ODE; integrates the exact killed Brownian resolvent for exponential clocks; and independently constructs each finite-rate completion transform from the discounted search-success and return-success renewal numerator. It repeats the calculation for deterministic clocks using the exact killed Brownian heat kernel. It checks the predicted \(r^{-3/2}\) amplitude at several \(s\) and \(r\), the convergence trend, and the universal clock ratio. In the delivered numerical run, **217 deterministic checks passed**, including comparisons of two independent finite-rate integral representations. These tests are illustrative: no finite grid proves the limit for arbitrary \(W\), arbitrary search stiffness or all \(s\). Those cases are established by the preceding dominated-convergence argument.

## Relationship to prior work

Dubey and Pal (arXiv:2610.18814v1; first public 13 October 2026) introduced the two-stiffness switching-harmonic search/return model and derived its **Poisson-clock mean first-passage time**. Biswas, Kundu and Pal (arXiv:2307.16294) formulated general stochastic-return renewal equations; the renewal idea itself is established prior work. Biswas, Dubey, Kundu and Pal (arXiv:2406.08975v1) examined mean times for drifted search with finite stochastic returns. Frydel (arXiv:2511.14646v1) analyzed related harmonic on/off and search-by-return protocols and their mean first-passage behavior. None of their inspected claims asserts a pointwise \(s>0\) high-rate *full completion-time transform* response for arbitrary positive clocks.

Most importantly, the published published-finding corpus record **“Sharp \(r^{-3/2}\) clock-moment law for stochastic-return Ornstein–Uhlenbeck search”** already proves the \(r^{-3/2}\) **mean** correction with the same clock factor \(\mathbb EW^2/\mathbb E\sqrt W\) in this same model, and it is not new here. Its coefficient is recovered as the formal \(s\downarrow0\) consistency check using \(C_0=[\int_0^1e^{k_2y^2/2}dy]^{-1}\). That prior mean statement does not determine the nonconstant \(s\)-dependent function \(\sqrt\pi s\phi_s(0)/C_s\), the entire Laplace-response profile, or the simultaneous across-\(s\) clock comparison. The present claim is strictly about this previously uncovered transform-level assertion, not a restatement of the known mean coefficient. Its novelty assessment is based on inspected sources rather than a claim of exhaustive uniqueness in all literature.

## Limitations

The limit is pointwise in each **fixed** \(s>0\), at fixed \(k_1\), fixed \(k_2>0\), and fixed independent law of \(W\) with finite second moment. Uniformity in \(s\), inversion into a signed density expansion, precise total variation bounds, and sharp higher moments are **not proved**. The clock factor can be infinite when \(\mathbb EW^2=\infty\), a case not considered here. The result does not cover non-Gaussian search increments, time-varying return stiffness, nonzero search drift at the home position, or target-blind returns. The numerical example covers free Brownian search and harmonic returns; it is not a computational certificate for all parameters. A general renewal formula can in principle be specialized further; an earlier unnoticed transform-level asymptotic remains a genuine publication-priority risk.

## References

1. A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814v1 (13 October 2026), https://arxiv.org/abs/2610.18814 .
2. A. Biswas, A. Kundu and A. Pal, *Search with stochastic home-returns can expedite classical first passage under resetting*, arXiv:2307.16294 (2023), https://arxiv.org/html/2307.16294v3 .
3. A. Biswas, A. Dubey, A. Kundu and A. Pal, *Drift-diffusive resetting search process with stochastic returns: speed-up beyond optimal instantaneous return*, arXiv:2406.08975v1 (13 June 2024), https://arxiv.org/html/2406.08975v1 .
4. D. Frydel, *Search by Return: Stochastic Resetting in Fluctuating Harmonic Potentials*, arXiv:2511.14646v1 (18 November 2025), https://arxiv.org/html/2511.14646v1 .
5. *Sharp \(r^{-3/2}\) clock-moment law for stochastic-return Ornstein–Uhlenbeck search*, published-finding corpus public finding (8 November 2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-r-3-2-clock-moment-law-for-stochastic-return-ornstein-uhle--1c82f789b3f9/RESULT.md .
