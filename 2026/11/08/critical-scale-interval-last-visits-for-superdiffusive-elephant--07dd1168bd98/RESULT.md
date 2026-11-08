# Critical-scale interval last visits for superdiffusive elephant random walks

## Finding

For fixed \(p\in(3/4,1)\), \(q\in[0,1]\) and \(c\ge0\), put \(a=2p-1\), \(\delta=2a-1>0\), \(r_n=\lfloor c\sqrt n\rfloor\), and \(I_n=[-r_n,r_n]\cap\mathbb Z\). For the last visit to this *frozen* interval,

\[
 T_{I_n}=\sup\{m\ge0:S_m\in I_n\},
\]

we establish

\[
 \lim_{n\to\infty}n^{a-1/2}\mathbb P(T_{I_n}\ge n)=f_{q,a}(0)C_a(c),\qquad
 C_a(c)=2\mathbb E\left[\sup_{0\le u\le 1/\delta}\left(B_u+c(1-\delta u)^{a/\delta}\right)\right].
\]

Here \(B\) is standard Brownian motion and \(f_{q,a}\) is the density of the almost-sure limit \(S_m/m^a\) of the elephant walk. In particular,

\[
 C_a(0)=\sqrt{\frac8{\pi\delta}},\quad
 2c\le C_a(c)\le 2c+\sqrt{\frac8{\pi\delta}},\quad
 \lim_{c\to\infty}\frac{C_a(c)}{2c}=1.
\]

The right derivative at the zero-radius boundary is

\[
 C_a'(0+)=\frac{2\Gamma(a/\delta+1/2)}{\sqrt\pi\,\Gamma(a/\delta+1)}.
\]

Thus the first variation of the last-visit constant at the critical square-root target scale is an explicit arcsine-time moment. All limits are for each fixed admissible \(p,q,c\).

## Assumptions and scope

The one-dimensional elephant random walk has \(S_0=0\), \(S_1=1\) with probability \(q\), otherwise \(S_1=-1\). At absolute time \(m\ge1\), its next increment \(X_{m+1}\in\{-1,1\}\) satisfies

\[
 \mathbb P(X_{m+1}=1\mid S_m=x)=\frac12\left(1+\frac{ax}{m}\right).
\]

A state \((m,x)\) is admissible when \(|x|\le m\), \(x\equiv m\pmod 2\). The deterministic set \(I_n\) is held fixed for the entire path when \(T_{I_n}\) is evaluated. The standard local limit theorem and future-martingale functional limit in Trinas (2026) and Trinas–Valle (2026) are used as published inputs; their independent proof is not asserted here. The density is smooth, positive at zero, and \(f_{q,a}(0)=f_{1,a}(0)\).

Write \(V=1/\delta\) and \(\beta=a/\delta>1\). The Brownian additive boundary is \(g_c(u)=c(1-\delta u)^\beta\), with \(g_c(V)=0\).

## Proof

**1. Normalized future process.** For \(m\ge n\), define

\[
 R_{n,m}=\prod_{j=n}^{m-1}(1+a/j)^{-1},\qquad M_m^{(n)}=R_{n,m}S_m.
\]

The process \(M^{(n)}\) is a martingale under the future law started at any admissible \((n,x)\), with increments bounded by \(2R_{n,m+1}\). Its accumulated conditional variance, divided by \(n\), converges along \(x_n/\sqrt n\to z\) to

\[
 v_a(t)=\int_0^t(1+s)^{-2a}\,\mathrm ds=\frac{1-(1+t)^{-\delta}}{\delta}.
\]

The cited future-martingale functional limit gives \(M_{n+\lfloor nt\rfloor}^{(n)}/\sqrt n\Rightarrow z+B_{v_a(t)}\) in the local Skorokhod topology; also \(R_{n,n+\lfloor nt\rfloor}\to(1+t)^{-a}\) uniformly for bounded \(t\).

**2. Finite-horizon critical interval hitting.** Set \(H_{n,T}^{(c)}(x)=\mathbb P_{n,x}(\exists m\in[n,n+\lfloor nT\rfloor]:|S_m|\le r_n)\). If \(x_n/\sqrt n\to z\) and \(z>c\), nearest-neighbor motion implies the exact finite-horizon event

\[
 \inf_{0\le t\le T}\left[\frac{M_{n+\lfloor nt\rfloor}^{(n)}}{\sqrt n}-\frac{r_nR_{n,n+\lfloor nt\rfloor}}{\sqrt n}\right]\le0.
\]

For \(z<-c\), use the analogous maximum with the lower boundary. For \(|z|<c\), eventually the starting state is inside the interval, giving probability one. At \(z=\pm c\), immediate Brownian oscillation through the boundary shows the same limiting probability one, even when the starting lattice state is just outside the interval. Brownian motion plus the continuously differentiable deterministic boundary on \([0,T]\) has an atomless minimum (or maximum), by absolute continuity with respect to ordinary Brownian motion after a fixed starting shift. Therefore the functional limit and continuity-set theorem yield

\[
 H_{n,T}^{(c)}(x_n)\longrightarrow h_{c,T}(z):=\mathbb P\{\exists t\in[0,T]:|z+B_{v_a(t)}|\le c(1+t)^{-a}\}.
\]

This kernel is continuous in \(z\): for \(|z|>c\), boundary extrema have atomless laws; for \(|z|\le c\), hitting occurs at time zero. Sequential convergence and compactness give uniform convergence over \(|x|\le K\sqrt n\) for each fixed \(K,T>0\).

**3. Infinite horizon and spatial localization.** Let \(m_T=n+\lfloor nT\rfloor\). If the *first* hit after time \(n\) occurs after \(m_T\), then for any \(\eta>0\), at least one of the following holds:

\[
 |M_{m_T}^{(n)}|\le\eta\sqrt n+r_nR_{n,m_T},\qquad
 \sup_{m\ge m_T}|M_m^{(n)}-M_{m_T}^{(n)}|\ge\eta\sqrt n.
\]

The first probability has \(\limsup_n\) uniformly bounded by \(C_a(\eta+c(1+T)^{-a})\) for starting states \(|x|\le K\sqrt n\), using the finite-horizon Gaussian limit and a bounded normal density. The martingale maximal \(L^2\) inequality and \(\sum_{m\ge m_T}R_{n,m+1}^2\le C_an(1+T)^{-\delta}\) bound the second by \(C_a\eta^{-2}(1+T)^{-\delta}\). Taking \(\eta=(1+T)^{-\delta/4}\) and then \(T\to\infty\) eliminates late hits uniformly on each compact starting-state window. Consequently

\[
 H_n^{(c)}(x_n)\longrightarrow h_c(z)=\mathbb P\{\exists u\in[0,V]:|z+B_u|\le g_c(u)\}.
\]

A hit from \(|x|>r_n\) requires martingale displacement at least \(|x|-r_n\). The maximal Azuma bound for \(|\Delta M_{m+1}^{(n)}|\le2R_{n,m+1}\) therefore gives

\[
 H_n^{(c)}(x)\le 2\exp\left(-\frac{(|x|-r_n)_+^2}{C_an}\right),
\]

valid for all admissible \(x\), with a harmless enlargement of the prefactor for points initially in the interval. This is an integrable Gaussian envelope outside a fixed multiple of \(\sqrt n\).

**4. Averaging using the lattice local limit theorem.** Condition on \(S_n\):

\[
 \mathbb P(T_{I_n}\ge n)=\sum_{x\equiv n\ (\mathrm{mod}\ 2)}\mathbb P(S_n=x)H_n^{(c)}(x).
\]

The uniform local limit theorem states

\[
 \sup_{x\equiv n\ (\mathrm{mod}\ 2)}\left|\frac{n^a}{2}\mathbb P(S_n=x)-f_{q,a}(x/n^a)\right|\to0.
\]

On \(|x|\le K\sqrt n\), \(x/n^a\to0\) uniformly, so \(\mathbb P(S_n=x)=2n^{-a}(f_{q,a}(0)+o(1))\). The parity lattice has mesh \(2/\sqrt n\), which cancels the factor two. Compact-kernel convergence yields a Riemann integral \(f_{q,a}(0)\int_{-K}^K h_c(z)\,\mathrm dz\). The preceding exponential spatial envelope and the global \(Cn^{-a}\) mass bound allow \(K\to\infty\), proving

\[
 \lim_n n^{a-1/2}\mathbb P(T_{I_n}\ge n)=f_{q,a}(0)\int_{\mathbb R}h_c(z)\,\mathrm dz.
\]

**5. Brownian swept-interval area.** For every continuous Brownian sample path, the set of \(z\) counted by \(h_c\) is the union

\[
 \bigcup_{0\le u\le V}[-B_u-g_c(u),\,-B_u+g_c(u)].
\]

It is an interval: it is the continuous image of the connected rectangle \([0,V]\times[-1,1]\) under \((u,v)\mapsto-B_u+vg_c(u)\). Its length is

\[
 \sup_u(-B_u+g_c(u))+\sup_u(B_u+g_c(u)).
\]

Tonelli's theorem and Brownian reflection symmetry show its expected length equals \(2\mathbb E\sup_u(B_u+g_c(u))=C_a(c)\). For \(c=0\), the reflection principle gives \(2\mathbb E\sup_{u\le V}B_u=\sqrt{8V/\pi}\). The pointwise inequalities \(0\le g_c(u)\le c\), and \(B_0=0\), establish \(2c\le C_a(c)\le2c+C_a(0)\), including the large-radius ratio.

**6. First-order motion of the constant.** Brownian motion on \([0,V]\) has almost surely a unique time \(\tau\) attaining its maximum; \(\tau/V\) has the classical arcsine law. The supremum functional is directionally differentiable under the continuous perturbation \(c\mapsto cg_1\). For almost every Brownian path, its right derivative at zero equals \(g_1(\tau)=(1-\delta\tau)^\beta\). Since \(0\le g_1\le1\), dominated convergence yields

\[
 C_a'(0+)=2\mathbb E(1-\delta\tau)^\beta
 =\frac2\pi\int_0^1\frac{(1-s)^\beta}{\sqrt{s(1-s)}}\,\mathrm ds
 =\frac{2\Gamma(\beta+1/2)}{\sqrt\pi\Gamma(\beta+1)}.
\]

This completes the proof.

## Verification

The standalone program `verify.py` uses exact rational arithmetic to check the future-walk transition, martingale and conditional-variance identities, and compares finite-horizon interval hitting by dynamic programming with a complete finite path enumeration. It also uses a fixed random seed for Brownian-grid diagnostics of the zero-radius value, arcsine derivative and swept-interval width identity. Run `python3 verify.py` with Python 3 and NumPy. The program does *not* prove the functional limit, local limit theorem or infinite-horizon statement; those are handled by the analytic argument and cited established results.

## Relationship to prior work

Hélio Trinas, *The Prodigal Elephant Returns: Last-Return Laws in the Superdiffusive Regime* (arXiv:2611.01279v1, first submitted 2026-10-31) proves the fixed-site constant and extends it to target diameters \(o(\sqrt n)\); Section 10 expressly points to target locations or diameters comparable with \(\sqrt n\) as an unresolved range. We use its future-martingale FCLT, local hitting controls and presentation of the Trinas–Valle LLT, not any claim of independent derivation of those prerequisites. This result adds the critical-width profile \(C_a(c)\), its Brownian swept-interval representation, and the explicit small-width derivative. Earlier critical-memory \(p=3/4\) work concerns a different scaling regime and does not imply this fixed superdiffusive-parameter result.

## Limitations

The target is the *symmetric complete integer interval*, centered at zero, with a radius of fixed multiple \(\sqrt n\); asymmetric or disconnected target sets, moving targets during each trajectory, and scales larger than \(\sqrt n\) are not classified. The parameter \(p\) is fixed strictly between \(3/4\) and \(1\); no parameter-uniform transition is asserted. No error rate in \(n\) is established. The inputs from the cited preprints and classical Brownian results are relied on as mathematical assumptions. The finding has not undergone an independent mathematical audit or historical-priority certification.

## References

- H. Trinas, *The Prodigal Elephant Returns: Last-Return Laws in the Superdiffusive Regime*, arXiv:2611.01279v1 (2026-10-31). https://arxiv.org/html/2611.01279v1. Particularly Theorem 3.4, Lemmas 4.3–4.4, Corollary 8.2 and Section 10.
- H. Trinas and G. Valle, *A Superdiffusive Local Limit Theorem for the Elephant Random Walk and the Breakdown of Log-Concavity*, arXiv:2609.14753v1 (2026-09-13). https://arxiv.org/abs/2609.14753. The local limit theorem is quoted in Trinas (2026), Proposition 2.1.
- P. Mörters and Y. Peres, *Brownian Motion*, Cambridge University Press (2010). Reflection principle and arcsine law.
