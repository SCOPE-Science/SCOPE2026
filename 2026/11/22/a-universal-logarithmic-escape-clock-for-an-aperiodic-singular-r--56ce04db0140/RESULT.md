# A universal logarithmic escape clock for an aperiodic singular rational map

## Finding

The singular rational map studied numerically in Alexanian's aperiodic example admits a complete global real-orbit classification. For every real initial condition \(u_0\ne-1\), iterates of
\[
f(u)=-4+\frac{u(1-u)}{1+u}
\]
are defined at all nonnegative integer times. Defining \(t_n=(u_n+1)^2\), there is a finite, initial-condition-dependent real constant \(C(u_0)\) such that
\[
\boxed{t_n=4n+\log n+C(u_0)+o(1)}\qquad(n\to\infty).
\]
More precisely, for every integer \(n\ge0\),
\[
\operatorname{sgn}(u_n+1)=(-1)^n\operatorname{sgn}(u_0+1).
\]
Consequently the even and odd subsequences escape to opposite real infinities, both with magnitude asymptotic to \(2\sqrt n\). The map has no periodic points and supports no invariant Borel probability measure on its entire domain.

## Assumptions and scope

The state space is the real set \(D=\mathbb R\setminus\{-1\}\). The iteration is deterministic, with \(u_{n+1}=f(u_n)\) and arbitrary \(u_0\in D\). Logarithms are natural; \(\gamma\) denotes Euler's constant. The asymptotic constant depends on the fixed initial state, and the convergence is not claimed to be uniform over all initial states. No parameter perturbations or complex-plane assertions are included.

## Proof

**Exact conjugate recurrence.** Set \(w_n=u_n+1\). Direct calculation, valid for every nonzero \(w\), gives
\[
f(w-1)+1=-w-\frac2w.
\]
Thus \(w_{n+1}=-w_n-2/w_n\). Its sign is the opposite of that of \(w_n\), and \(|w_{n+1}|=|w_n|+2/|w_n|>|w_n|>0\). Induction establishes global forward existence, sign alternation, and strict increase of squared distance. Squaring yields exactly
\[
t_{n+1}=t_n+4+\frac4{t_n},\qquad t_0>0.\tag{1}
\]

**Leading bound.** Formula (1) gives \(t_n\ge t_0+4n\). Summing (1), for every \(n\ge2\),
\[
t_n=t_0+4n+\frac4{t_0}+\sum_{k=1}^{n-1}\frac4{t_k}
\le t_0+4n+\frac4{t_0}+\sum_{k=1}^{n-1}\frac4{t_0+4k}.
\]
The last sum is bounded by a constant depending on \(t_0\) plus \(\log n\). It follows that \(t_n=4n+O_{t_0}(\log n)\) as \(n\to\infty\).

**Convergent logarithmic correction.** For integers \(k\ge1\), the preceding bound and \(t_k\ge4k\) imply
\[
\left|\frac4{t_k}-\frac1k\right|
=\frac{|t_k-4k|}{k\,t_k}
=O_{t_0}\left(\frac{\log(k+1)}{k^2}\right).
\]
The series of absolute differences therefore converges. Since \(\sum_{k=1}^{n-1}1/k-\log n\to\gamma\), summing (1) proves
\[
\lim_{n\to\infty}\bigl(t_n-4n-\log n\bigr)
=t_0+\frac4{t_0}+\gamma+
\sum_{k=1}^\infty\left(\frac4{t_k}-\frac1k\right)=:C(u_0)\in\mathbb R.
\]
Combining the sign identity with \(t_n\sim4n\) gives the two parity limits and escape rate.

**Periodic points and stationary probabilities.** The strict inequality \(t_{n+1}>t_n\) excludes every finite-period orbit. For each compact \(K\subset D\), every orbit eventually leaves \(K\) permanently, because \(|u_n+1|\to\infty\). Were \(\nu\) an invariant Borel probability measure, invariance and dominated convergence applied to \(\mathbf1_K(f^n(u))\) would give \(\nu(K)=0\). The compact exhaustion \(K_m=\{u\in D: |u|\le m,\ |u+1|\ge1/m\}\), \(m\ge1\), covers \(D\), contradicting \(\nu(D)=1\).

## Verification

Exact-rational checks in `verify.py` independently compare the given rational formula with the \(w\)-recurrence at multiple initial points, and check recurrence (1) step-by-step. Floating-point tests also inspect the convergence of \(t_n-4n-\log n\) for several initial states. These tests are supplementary; the proof above establishes the assertions for infinitely many iterates and every admissible real initial state.

To execute from a directory containing the files, run `python3 verify.py`. Only the Python standard library is required.

## Relationship to prior work

Alexanian's *One-dimensional Dynamics for a Discontinuous Singular Map and the Routes to Chaos* (2022), equation (17), displays this exact map and reports a numerical aperiodic orbit with both ends of the real line appearing in its plotted behavior. The present finding proves a global, all-initial-condition description and a sharp logarithmic correction to its escape clock, neither derived in the inspected presentation of that example. The earlier article also considers other parameter families and periodic behavior; the present result does not claim anything about those families. The method uses an elementary exact change of variables and classical harmonic-sum asymptotics. General parabolic-dynamics normal forms may imply analogous asymptotics for other maps, so priority relative to that broader theory remains a risk; the result is a model-specific exact theorem.

## Limitations

The theorem concerns the single parameter choice and real domain of equation (17), excluding its pole. It does not establish novel general parabolic theory, chaoticity, or any statement about perturbations. The constant \(C(u_0)\) is given by a convergent orbit series rather than a closed elementary formula. Independently verified mathematical priority has not been established.

## References

1. M. Alexanian, *One-dimensional Dynamics for a Discontinuous Singular Map and the Routes to Chaos*, Armenian Journal of Physics **15** (2022), 151–161, DOI: 10.54503/18291171-2022.15.4-151; arXiv:2212.12033 (public preprint dated 2022-12-22), https://arxiv.org/abs/2212.12033.
2. L. Euler's harmonic-number limit \(\gamma=\lim_{n\to\infty}(\sum_{k=1}^n 1/k-\log n)\), a standard classical identity.
