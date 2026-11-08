# A sharp relationship-strength separatrix for two-agent coevolving opinions

## Finding
Consider two people whose mutual influence weight follows logistic reinforcement while the effect of opinion disagreement decays exponentially. Despite the interaction function being strictly positive at every finite disagreement, there is an exact critical *initial relationship strength* separating eventual consensus from persistent disagreement. At criticality the residual opinion gap decays toward a strictly positive threshold as the inverse of time, while the relationship strength vanishes as the inverse square of time.

Let \(\alpha>0\), \(0<d_0\le2\), and \(0<w_0<1\). Define
\[
 d_c=\frac{\log 2}{\alpha},\qquad
 H_\alpha(d)=\frac12\operatorname{Ei}(\alpha d)-\log d,
\]
where \(\operatorname{Ei}(z)=\gamma+\log z+\int_0^z(e^u-1)/u\,du\) for \(z>0\) is the real exponential integral and \(\gamma\) is Euler’s constant. When \(d_0>d_c\), put
\[
 w_c=\tanh\!\bigl(H_\alpha(d_0)-H_\alpha(d_c)\bigr).
\]
Then \(0<w_c<1\). The exact limit \((d_\infty,w_\infty)\) is:

- If \(d_0\le d_c\), or \(d_0>d_c\) and \(w_0>w_c\), then \((d_\infty,w_\infty)=(0,1)\): full consensus and strengthened relationship.
- If \(d_0>d_c\) and \(w_0=w_c\), then \((d_\infty,w_\infty)=(d_c,0)\). More precisely,
\[
 d(t)-d_c\sim\frac{2}{\alpha t},\qquad
 w(t)\sim\frac{2}{(\log2)t^2}.
\]
- If \(d_0>d_c\) and \(w_0<w_c\), then \((d_\infty,w_\infty)=(d_*,0)\), where \(d_*\in(d_c,d_0)\) is the unique solution of
\[
 H_\alpha(d_*)=H_\alpha(d_0)-\operatorname{artanh}(w_0).
\]
In this last regime the tie weight vanishes exponentially fast, with exponent \(1-2e^{-\alpha d_*}>0\).

Thus for \(d_0>d_c\) the long-run opinion gap jumps from a one-sided limiting value \(d_c>0\) to \(0\) across the threshold \(w_c\). The threshold is a universal function of the dimensionless starting disagreement \(s=\alpha d_0\):
\[
 w_c(s)=\tanh\left[\tfrac12\bigl(\operatorname{Ei}(s)-\operatorname{Ei}(\log2)\bigr)-\log\frac{s}{\log2}\right],\qquad s>\log2.
\]

## Assumptions and scope
There are precisely two agents with opinions \(x_1(t),x_2(t)\in[-1,1]\), initially distinct. Their self-weights are fixed at one and their symmetric off-diagonal weight is \(w(t)\in(0,1)\). Interaction strength is \(\phi(d)=e^{-\alpha d}\), with \(d(t)=|x_2(t)-x_1(t)|\). The continuous-time system is the exact two-agent specialization of the normalized opinion flow and logistic tie dynamics defined by Nugent, Gomes and Wolfram:
\[
 \dot x_1=\frac{w e^{-\alpha d}}{1+w}(x_2-x_1),\qquad
 \dot x_2=\frac{w e^{-\alpha d}}{1+w}(x_1-x_2),\qquad
 \dot w=w(1-w)(2e^{-\alpha d}-1).
\]
The initial separation is \(d(0)=d_0\) and the initial link strength is \(w(0)=w_0\). The restrictions \(d_0>0\), \(0<w_0<1\) exclude trivial invariant boundary trajectories. This is a two-agent dynamical theorem, not a general-network classification.

## Proof
**Reduction and first integral.** The opinion mean \((x_1+x_2)/2\) is constant, the initial order never reverses, and the separation satisfies
\[
 \dot d=-\frac{2w e^{-\alpha d}}{1+w}d<0,
 \qquad \dot w=w(1-w)(2e^{-\alpha d}-1).
\]
On the open state rectangle, direct differentiation gives
\[
 \frac{d}{dd}\operatorname{artanh} w
 =\frac{\dot w}{(1-w^2)\dot d}
 =\frac{e^{\alpha d}/2-1}{d}=H_\alpha'(d).
\]
Consequently every orbit lies on the exact invariant curve
\[
 \operatorname{artanh}w(t)-H_\alpha(d(t))
 =\operatorname{artanh}w_0-H_\alpha(d_0).
\]
The flow preserves \(0<w<1\) at every finite time and the separation is decreasing, so \(d\) has a nonnegative limit. The derivative \(H_\alpha'(d)=(e^{\alpha d}/2-1)/d\) is negative below \(d_c\), zero at \(d_c\), and positive above \(d_c\). Hence \(H_\alpha\) has a unique strict minimum at \(d_c\), and \(H_\alpha(d)\to+\infty\) as \(d\downarrow0\).

**Classification.** If \(d_0\le d_c\), the separation decreases through the region where \(\dot w>0\); the only possible asymptotic state is \((0,1)\). If \(d_0>d_c\), the invariant curve gives
\[
 \operatorname{artanh}w=\operatorname{artanh}w_0+H_\alpha(d)-H_\alpha(d_0).
\]
As \(d\) decreases toward \(d_c\), the right-hand side has its smallest value there. When this value is positive (\(w_0>w_c\)), the orbit crosses \(d_c\), after which \(w\) increases and \(d\to0\). When it is zero (\(w_0=w_c\)), \(d\) approaches \(d_c\) while \(w\downarrow0\): the invariant curve cannot be continued through \(d_c\) with a negative \(\operatorname{artanh}w\). When it is negative (\(w_0<w_c\)), the orbit encounters the unique larger zero at \(d_*>d_c\), so \(w\to0\) and \(d\to d_*\). These limits follow from positivity of the vector field's separation speed away from the boundary and monotonicity of \(H_\alpha\) on \((d_c,d_0)\).

**Critical asymptotics.** On the critical invariant curve Taylor expansion gives, as \(z=d-d_c\downarrow0\),
\[
 \operatorname{artanh}w=H_\alpha(d)-H_\alpha(d_c)
 =\frac{\alpha^2}{2\log2}z^2+O(z^3).
\]
Since \(\operatorname{artanh}w=w+O(w^3)\), we obtain \(w\sim \alpha^2 z^2/(2\log2)\). Substitution into the separation equation gives \(\dot z=-(\alpha/2)z^2(1+o(1))\), whence \(z\sim2/(\alpha t)\) by integrating the derivative of \(1/z\). Combining the two expansions yields \(w\sim2/((\log2)t^2)\). On the polarized branch, \(d\to d_*>d_c\) and the weight equation linearizes to \(\dot w=-(1-2e^{-\alpha d_*})w+o(w)\), which establishes its exponential decay exponent.

## Verification
Run `python verify.py` using Python 3 with NumPy and SciPy. The program checks the first-integral derivative on a parameter grid, numerically integrates the original two-dimensional ODE in all three regimes, checks first-integral conservation away from floating-point saturation, evaluates the predicted polarization limits by independent scalar root finding, and checks critical inverse-time and inverse-square leading constants. The mathematical statements for all positive parameters follow from the proof, not from these finite checks.

For a reproducible example, take \(\alpha=2\) and \(d_0=1\). Then \(d_c\approx0.3465735903\), \(w_c\approx0.7137933377\). Starting from \(w_0=0.4\) gives \(d_*\approx0.8147591761\), whereas \(w_0=0.8\) gives consensus.

## Relationship to prior work
Nugent, Gomes and Wolfram [1] introduce the normalized continuous opinion flow and logistic tie reinforcement, and identify numerical transitions between disagreement and consensus for exponential interactions. Their equations (8), (12), and discussion in Section 3.4 supply the exact model studied here, but their displayed results do not specify this two-agent global separatrix, its exponential-integral formula, or the critical algebraic relaxation constants. The new result identifies an exact, initial-condition-dependent basin boundary inside that model.

Wang, Luo and Gao [2] study coevolving signed appraisals and structural balance, with distinct update equations and objective; their sign-balance statements do not imply a threshold for the positive logistic edge in [1]. Bhalla, Lechowicz and Musco [3] study a discrete edge-added/deleted Friedkin–Johnsen process, rather than continuous logistic weights. Broad consensus and polarization phenomena in those models do not themselves determine the present continuous-time critical threshold.

## Limitations
The theorem is restricted to two agents, symmetric ties, a unit self-loop, the exact degree normalization, exponential influence, and logistic weight reinforcement. It does not establish phase diagrams for larger networks or different normalization conventions. The endpoints \(w_0=0\) or \(w_0=1\) are excluded from the trichotomy. Numerical integration close to the separatrix requires care because convergence is algebraically slow. Priority relative to unindexed or inaccessible equivalent analyses has not been independently settled.

## References
[1] A. J. Nugent, S. N. Gomes and M.-T. Wolfram, *On evolving network models and their influence on opinion formation*, Physica D 456 (2023), 133914. First public preprint 2023-05-16. https://arxiv.org/abs/2305.09483 ; https://doi.org/10.1016/j.physd.2023.133914 ; lawful open access: https://wrap.warwick.ac.uk/id/eprint/180170/7/1-s2.0-S0167278923002683-main.pdf

[2] H. Wang, F. Luo and J. Gao, *Co-evolution of Opinion and Social Tie Dynamics Towards Structural Balance*, 2021, https://arxiv.org/abs/2107.05796 .

[3] N. Bhalla, A. Lechowicz and C. Musco, *Local Edge Dynamics and Opinion Polarization*, 2022 preprint, https://arxiv.org/abs/2111.14020 .
