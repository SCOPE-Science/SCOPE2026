# Sharp consensus–polarization threshold and universal logarithmic critical relaxation in a two-voter model

## Finding

For every initial half-gap \(a\in(0,1/2]\) and feedback strength \(c\in(0,1]\), the symmetric two-voter voting-dependent concatenated Friedkin–Johnsen system has exactly one critical initial stubbornness \(\theta_*(a,c)\in(0,1)\). It partitions the initial-state interval into three mathematically different outcomes:

- If \(0\le\theta_0<\theta_*\), the opinion gap converges to zero exponentially and stubbornness has a limit strictly below one.
- If \(\theta_*<\theta_0<1\), the gap approaches a strictly positive limit and the residual susceptibility decays exponentially.
- If \(\theta_0=\theta_*\), both half-gap and residual susceptibility tend to zero algebraically. There is a finite real constant \(H(a,c)\) for which

\[
\boxed{\frac1{x_n}=cn+\frac c2\log n+H(a,c)+o(1)},\qquad
1-\theta_n=\frac1n+O\!\left(\frac{\log n}{n^2}\right).
\]

The two-agent opinion gap is \(2x_n\), so \(n(2x_n)\to2/c\). The coefficient \(c/2\) of the logarithmic correction is universal across initial gaps. The critical threshold obeys
\[
\boxed{1-ca<\theta_*(a,c)<\frac1{1+ca}}.
\]

## Assumptions and scope

There are two agents with equal influence weights \(w_{ij}=1/2\), identical initial stubbornness \(\theta_0\), initial opinions symmetric around their conserved mean, and a vote at the mean after every issue. Write \(x_n\in[0,1/2]\) for either agent's distance to the mean at the start of issue \(n\). The original issue-level equilibrium and feedback rule, exactly as in equation (8) of the initiating paper, give
\[
x_{n+1}=\theta_n x_n,\qquad
\theta_{n+1}=\theta_n+c(1-\theta_n)\theta_n x_n,\qquad n\ge0.
\]
Assume \(x_0=a>0\), \(0<c\le1\), and \(0\le\theta_0<1\). When \(\theta_0=0\), consensus occurs in one issue. All nontrivial asymptotic conclusions concern \(0<\theta_0<1\). No assertion is made for asymmetric stubbornness, larger networks, different voting rules or stochastic dynamics.

## Proof

**1. Monotone coordinates and limits.** Define residual susceptibility \(u_n=1-\theta_n\). The exact recurrence becomes
\[
x_{n+1}=(1-u_n)x_n,\qquad
u_{n+1}=u_n[1-c(1-u_n)x_n].
\]
For interior initial conditions, \(x_n,u_n\) are positive, nonincreasing and bounded, with limits \(x_\infty,u_\infty\ge0\). The recurrences forbid both limits being strictly positive. If \(u_\infty>0\), \(x_n\to0\) geometrically; if \(x_\infty>0\), \(u_n\to0\) geometrically.

**2. Strict finite-time classification criteria.** Exact telescoping identities are
\[
x_n-x_{n+1}=u_nx_n,\qquad
u_n-u_{n+1}=c\theta_n(x_n-x_{n+1}).
\]
Since \(\theta_n\) is nondecreasing, summing over all subsequent issues yields
\[
c\theta_n(x_n-x_\infty)\le u_n-u_\infty\le c(x_n-x_\infty).
\]
Therefore, if \(u_n>cx_n\) at any issue, then \(u_\infty>0\) (consensus). If \(u_n<c\theta_nx_n\), then \(x_\infty>0\) (permanent disagreement). Conversely, either noncritical limit implies its respective strict inequality eventually, so both outcome basins are open in the initial stubbornness.

**3. Existence and order of a critical state.** The consensus criterion already holds at issue zero if \(\theta_0<1-ca\). The disagreement criterion holds initially if \(1-\theta_0<c\theta_0a\), equivalently \(\theta_0>1/(1+ca)\). Thus both basins are nonempty. The update is order preserving in \((x,\theta)\) because
\[
\frac{\partial x_{n+1}}{\partial x_n}=\theta_n,\quad
\frac{\partial x_{n+1}}{\partial\theta_n}=x_n,\quad
\frac{\partial\theta_{n+1}}{\partial x_n}=c\theta_n(1-\theta_n),\quad
\frac{\partial\theta_{n+1}}{\partial\theta_n}=1+cx_n(1-2\theta_n)\ge1-cx_n\ge\frac12.
\]
Hence consensus is an initial interval and disagreement a terminal interval. Their open disjoint union cannot cover the connected interval of admissible initial stubbornness; at least one initial condition is neither, and necessarily has \(x_\infty=u_\infty=0\). Both endpoint bounds are strict: at \(\theta_0=1-ca\), \(w_0=u_0-cx_0=0\) and \(w_1-w_0=cu_0^2x_0>0\), so consensus follows; at \(\theta_0=1/(1+ca)\), \(g_0=u_0-c\theta_0x_0=0\), while the exact identity \(g_{n+1}-g_n=-c^2u_n\theta_n^2x_n^2<0\) makes the subsequent state permanently disagreeing.

**4. Exact critical expansion and logarithmic correction.** For any orbit with \(x_\infty=u_\infty=0\), define \(w_n=u_n-cx_n\). The update yields the polynomial identity
\[
w_{n+1}-w_n=c u_n^2x_n>0.
\]
Since \(w_n\to0\), this gives
\[
-c^2x_n^2\le-c u_nx_n\le w_n<0,
\]
by summing \(w_{k+1}-w_k\) and using \(\sum_{k\ge n}u_kx_k=x_n\), together with \(u_n\le cx_n\). The precise sum is
\[
w_n=-c\sum_{k\ge n}u_k(x_k-x_{k+1}).
\]
Substituting \(u_k=cx_k+w_k\), and using
\[
\sum_{k\ge n}x_k(x_k-x_{k+1})=\frac{x_n^2}{2}+\frac12\sum_{k\ge n}(x_k-x_{k+1})^2,
\]
shows that
\[
\boxed{u_n=cx_n-\frac{c^2}{2}x_n^2+O(x_n^3)}.
\]
Indeed, \(\sum_{k\ge n}(x_k-x_{k+1})^2\le cx_n^3\), and \(\sum_{k\ge n}|w_k|(x_k-x_{k+1})\le c^2x_n^3\), since \(x_k-x_{k+1}=u_kx_k\le cx_k^2\). Thus the remainder is bounded in absolute value by \(3c^3x_n^3/2\).

The reciprocal half-gap increment has the asymptotic expansion
\[
\frac1{x_{n+1}}-\frac1{x_n}=
\frac{u_n}{x_n(1-u_n)}
=c+\frac{c^2}{2}x_n+O(x_n^2).
\]
Since \(u_n/x_n\to c\), Cesàro averaging first gives \(1/x_n\sim cn\), hence \(x_n=O(1/n)\). Summation then gives \(1/x_n=cn+O(\log n)\), and consequently
\[
x_n=\frac1{cn}+O\!\left(\frac{\log n}{n^2}\right).
\]
The sequence \(1/x_n-cn-(c/2)\log n\) has successive differences \(O(\log n/n^2)\): subtract the increment \((c/2)\log(1+1/n)\) from the reciprocal increment and use the last bound. These differences are absolutely summable, proving convergence to a finite constant \(H(a,c)\). Substituting back into the boxed expansion yields \(u_n=1/n+O(\log n/n^2)\).

**5. Uniqueness of the critical initial state.** Suppose two distinct critical initial stubbornness values satisfy \(\theta_0^{(L)}<\theta_0^{(H)}\) for the same \(a,c\). Order preservation gives \(x_n^{(L)}\le x_n^{(H)}\) and \(\theta_n^{(L)}<\theta_n^{(H)}\). Consequently
\[
\frac{u_{n+1}^{(L)}}{u_{n+1}^{(H)}}
=\frac{u_n^{(L)}}{u_n^{(H)}}
\frac{1-c\theta_n^{(L)}x_n^{(L)}}{1-c\theta_n^{(H)}x_n^{(H)}}
\ge\frac{u_n^{(L)}}{u_n^{(H)}}>1.
\]
But step 4 implies \(n u_n^{(L)}\to1\) and \(n u_n^{(H)}\to1\), forcing their ratio to one. This contradiction gives a unique critical initial stubbornness. The ordered open basins occupy all initial states on either side, proving the complete trichotomy.

## Verification

The self-contained `verify.py` checks exact polynomial increment identities and the cancellation of terms in the center-orbit expansion with SymPy. It also evaluates finite-time sufficient classification criteria using rational arithmetic and numerically locates a representative transition. Finite tests do not establish the infinite-time theorem; the proof above supplies the limiting arguments. To replay: `python verify.py` in a Python environment with SymPy installed.

## Relationship to prior work

Ohlin, Bencherki and Tegling derived exactly this two-agent feedback system as their equation (8) in the 2022 conference paper. Their Theorem 3.1 establishes only the sufficient consensus condition \(cx_0+\theta_0<1\) and their Remark 3.1 observes that this condition does not capture the complete consensus basin. The theorem here determines a unique implicit basin boundary and supplies a universal critical logarithmic correction. Published concatenated Friedkin–Johnsen work with prescribed time-varying interaction weights and multidimensional stubbornness concerns other update mechanisms and does not directly imply this feedback-specific threshold.

## Limitations

No elementary closed formula for \(\theta_*(a,c)\) is claimed. The result requires equal weights, identical two-agent stubbornness, and deterministic median-vote feedback. It does not generalize to arbitrary network sizes. The originating publication is a 2022 proceeding and an author's full-text PDF is hosted in a path containing `2022/11`, but the first day of its circulation cannot be independently confirmed from that path. The date 2023-01-19 in metadata is the first independently verified **day-stamped public catalogue record** consulted, not the historical first circulation day. Possible unindexed equivalent analyses remain a priority risk.

## References

1. D. Ohlin, F. Bencherki, E. Tegling, *Achieving consensus in networks of increasingly stubborn voters*, 2022 IEEE Conference on Decision and Control, pp. 3531–3537 (2022). DOI: https://doi.org/10.1109/CDC51059.2022.9992899. Full text: https://tegling.se/wp-content/uploads/2022/11/cdc22_1182_fi.pdf. Later arXiv edition: https://arxiv.org/abs/2405.13703.
2. Lund University Publications, day-stamped entry for reference 1 added 2023-01-19: https://lup.lub.lu.se/search/publication/ecb8ff2e-7dd6-4a96-88f1-10348073951b.
3. Y. Wang et al., *Achieving consensus in spite of stubbornness: time-varying concatenated Friedkin–Johnsen models*. Bibliographic information: https://www.researchgate.net/publication/358319538_Achieving_consensus_in_spite_of_stubbornness_time-varying_concatenated_Friedkin-Johnsen_models.
