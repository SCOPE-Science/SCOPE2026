# A persistent reactivity gap between optimal opposite-drift resetting rates

## Finding

Fix any diffusion coefficient \(D>0\), reset distance \(L>0\), delta-sink strength \(k>0\), and drift speed \(v>0\). For one-dimensional drift–diffusion started and Poisson-reset to \(L\), with a partially reactive point sink at the origin, write \(r_{\mathrm{away}}(v)\) and \(r_{\mathrm{toward}}(v)\) for the Poisson reset rates that minimize the mean time to absorption under drifts \(+v\) and \(-v\), respectively. Each optimum exists, is positive and is unique, and **for every** \(v>0\),

\[
r_{\mathrm{away}}(v)>r_{\mathrm{toward}}(v).
\]

At fixed \(D,L,k\) and as \(v\to\infty\), the two optimal rates share the same leading term, but their difference has a nonzero, reactivity-dependent limit:

\[
\begin{aligned}
r_{\mathrm{away}}(v)&=\frac{v}{L}+O(v^{-1}),\\
r_{\mathrm{toward}}(v)&=\frac{v}{L}-\frac{k}{eL}+O(v^{-1}),\\
\lim_{v\to\infty}\bigl(r_{\mathrm{away}}(v)-r_{\mathrm{toward}}(v)\bigr)&=\frac{k}{eL}.
\end{aligned}
\]

The constants in the remainder terms may depend on fixed \(D,L,k\). In particular, the persistent first correction is independent of \(D\), although the full rates depend on it. The existence of the mean-time formula used below is prior work; the new proposed claim is the global paired-drift ordering and the sharp strong-drift difference.

## Assumptions and scope

Between reset events, the particle has generator \(\mathcal L_\sigma=D\partial_{xx}+\sigma v\partial_x\) on the whole real line, where \(\sigma\in\{-1,+1\}\). It starts at \(X_0=L\), is instantaneously returned to \(L\) at independent exponential times of rate \(r>0\), and is killed at rate \(k\) per unit local-time density at zero, with the delta-potential normalization \(k\delta_0\) in the forward equation. The sink strength \(k\) has units length/time, and all of \(D,L,k,v\) are finite and strictly positive. The target is **not** a perfectly absorbing boundary and there is no additional gated target state.

By the known killed-diffusion resolvent and reset-renewal formula (Mazzolo, Eq. (116)), the mean absorption time is

\[
T_\sigma(r)=\frac{1}{r}\left[\left(1+\frac{\sqrt{v^2+4Dr}}{k}\right)
\exp\left(\frac{\sigma vL+L\sqrt{v^2+4Dr}}{2D}\right)-1\right].
\tag{1}
\]

It is this fixed-parameter function, not a non-Poisson or adaptive resetting protocol, that is optimized.

## Proof

Put

\[
p=\frac{vL}{2D}>0,\qquad b=\frac{kL}{2D}>0,\qquad
u=\sqrt{p^2+\frac{rL^2}{D}}-p>0.
\]

The correspondence \(r=(D/L^2)u(u+2p)\) is strictly increasing for \(u>0\). Equation (1), after multiplying by \(D/L^2\), is equivalent to minimizing

\[
f_\sigma(u)=\frac{e^{(1+\sigma)p+u}\bigl(1+(p+u)/b\bigr)-1}{u(u+2p)},\qquad u>0.
\tag{2}
\]

**Existence and uniqueness.** Write \(d(u)=u(u+2p)\) and \(q_\sigma(u)=d(u)f_\sigma(u)=\sum_{n\ge0}c_nu^n\). The coefficients are

\[
c_0=e^{(1+\sigma)p}(1+p/b)-1>0,\qquad
c_n=\frac{e^{(1+\sigma)p}}{n!}\left(1+\frac{p+n}{b}\right)>0\quad(n\ge1).
\]

The derivative of \(f_\sigma\) has the sign of \(H(u)=dq_\sigma'-d'q_\sigma\). Multiplying out the absolutely convergent series gives

\[
\begin{split}
\frac{H(u)}{u^2}={}&-\frac{2pc_0}{u^2}-\frac{2c_0}{u}+(2pc_2-c_1)\\
&+\sum_{j\ge3}\bigl((j-3)c_{j-1}+2p(j-1)c_j\bigr)u^{j-2}.
\end{split}
\tag{3}
\]

Every coefficient in the last sum is strictly positive, so \(H(u)/u^2\) is strictly increasing on \((0,\infty)\). It tends to \(-\infty\) as \(u\downarrow0\) and to \(+\infty\) as \(u\to\infty\), already from its positive linear term. Therefore \(f_\sigma\) decreases to exactly one point and then increases; this point is its unique global minimum. The endpoint divergences also follow directly from (2).

**Comparison under drift reversal.** For the same \(p,b\), define \(F(u)=e^u(1+(p+u)/b)\) and \(G(u)=dF'-d'F\). The derivative numerators for inward and outward drift are

\[
H_-(u)=G(u)+d'(u),\qquad H_+(u)=e^{2p}G(u)+d'(u).
\]

At the unique inward minimizer \(u_-\), \(H_-(u_-)=0\), hence \(G(u_-)=-d'(u_-)\) and

\[
H_+(u_-)=(1-e^{2p})d'(u_-)<0.
\]

As \(H_+\) changes sign from negative to positive at just one point, its zero satisfies \(u_+>u_-\). Strict monotonicity of \(u\mapsto r\) proves the rate comparison.

**Sharp strong-drift separation.** The logarithmic-derivative stationarity equation, valid at either optimum, is

\[
1+\frac1{p+b+u}=\left(\frac1u+\frac1{2p+u}\right)
\left(1-\frac{b e^{-(1+\sigma)p-u}}{p+b+u}\right).
\tag{4}
\]

For fixed \(b\), the left minus right side converges on each compact subset of \(u>0\) to \(1-1/u\) as \(p\to\infty\). At any fixed \(0<a<1<c\), its signs at \(a,c\) are eventually negative and positive, respectively. Since the unique root lies between them, \(u_\sigma\to1\). Now set \(u=1+A_\sigma/p+O(p^{-2})\) in (4). At order \(p^{-1}\), the equation reads

\[
A_\sigma+\frac12+\mathbf1_{\{\sigma=-1\}}\frac{b}{e}=0.
\]

Smooth implicit expansion near \(u=1\) gives the stated remainder for the inward branch, and the outward branch has an exponentially small additional \(e^{-2p}\) factor. Consequently,

\[
\begin{aligned}
u_+&=1-\frac1{2p}+O(p^{-2}),\\
u_-&=1-\frac{1/2+b/e}{p}+O(p^{-2}).
\end{aligned}
\]

Finally substitute into \(r_\sigma=(D/L^2)u_\sigma(u_\sigma+2p)\), use \(2Dp/L^2=v/L\) and \(2Db/L^2=k/L\), and subtract. This proves the three claims.

## Verification

Run `python3 CHECK.py` with Python 3 standard library. It checks coefficient expansions against the closed derivative, finite root brackets and strict paired inequalities over positive parameter grids, direct objective minima, and the high-drift limiting coefficient. One reference output is `PASS 590 deterministic numerical and coefficient checks`.

For \(D=L=1\), \(k=2\), \(v=6\) (hence \(p=3\), \(b=1\)), the two numerical rates are \(r_{\mathrm{toward}}\approx5.820584260045\) and \(r_{\mathrm{away}}\approx6.561093459193\). The asymptotic difference is \(2/e\approx0.735758882343\); the finite-speed gap here is about \(0.740509199148\).

These finite numerical checks are reproducibility aids, not proofs of the universal quantifiers. Equations (1)–(4) and their analytic sign and expansion arguments establish the theorem.

## Relationship to prior work

Mazzolo (2026), arXiv:2609.22527, derives the exact general drifted survival resolvent and mean time (Eq. (116)); its Appendix A.5 reduces the optimization to one dimension, computes the perturbation near zero drift, and numerically illustrates nonmonotonicity on the drift-toward side. We credit that model, formula, and its prior observations fully. The present theorem identifies a strict **paired opposite-drift comparison at every nonzero speed** and a **nonvanishing, exact high-speed offset**; these are not supplied as proved statements by the inspected optimization section.

Whitehouse, Evans and Majumdar (2013) analyze partially absorbing targets without drift. Ray, Mondal and Reuveni (2018) analyze drift with a perfectly absorbing target. Biswas, Pal, Mondal and Ray (2023) analyze a dynamically gated target rather than constant delta killing. Those models do not already furnish the finite-\(k\), opposite-drift separation as stated. Nevertheless, the exact known formula (1) strongly constrains the problem, and an earlier unindexed asymptotic extraction remains a genuine originality risk.

## Limitations

All reactivity statements assume fixed **finite** \(k>0\) before taking \(v\to\infty\). The expansion is not asserted uniformly in \(k\), and it must not be interchanged without justification with the perfectly absorbing limit \(k\to\infty\). The comparison is for mean absorption time under independent Poisson resetting, not survival at every time, optimal deterministic restart, multiple absorbing sites, or general spatially varying drifts. Numerical experiments do not establish the global theorem. Independent external validation has not been performed.

## References

1. A. Mazzolo, *Diffusion with stochastic resetting in the presence of a delta killing trap: Drift-controlled survival regimes*, first public preprint 2026-09-18, arXiv:2609.22527, https://arxiv.org/abs/2609.22527 ; Phys. Rev. E **114**, 044105 (2026).
2. J. Whitehouse, M. R. Evans and S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, arXiv:1301.2489 (2013), https://arxiv.org/abs/1301.2489 .
3. S. Ray, D. Mondal and S. Reuveni, *Péclet number governs transition to acceleratory restart in drift-diffusion*, arXiv:1811.08239 (2018), https://arxiv.org/abs/1811.08239 .
4. A. Biswas, A. Pal, D. Mondal and S. Ray, *Rate enhancement of gated drift-diffusion process by optimal resetting*, arXiv:2304.10605 (2023), https://arxiv.org/abs/2304.10605 .
