# Sharp mutation threshold and re-entrant infectivity variance in a bimodal evolving SIR model

## Finding
For the continuum evolutionary SIR equations of Lamata-Otín et al. [1] on the entire trait line, two initially Gaussian infectivity modes of the **same positive within-mode variance** remain an exact two-Gaussian mixture. Denote their mean separation by \(\Delta>0\), the contact coefficient by \(k>0\), the initial susceptible fraction by \(s_0\in(0,1)\), and the effective trait diffusion by \(\mathcal D>0\). For every initial high-mode fraction \(0<p_0<1\), the exact trait variance is strictly increasing at every positive time if
\[
\mathcal D\geq\mathcal D_{\mathrm{crit}}:=\frac{k s_0\Delta^3}{6\sqrt3}.
\]
This uniform threshold is sharp: for each smaller positive diffusion coefficient, choosing \(p_0=(1+1/\sqrt3)/2\) makes variance initially decrease and then attain exactly one strict minimum before increasing forever. Moreover, an explicit positive-parameter example has variance **first increasing, then decreasing, then increasing again** at three finite observation times; therefore it has at least two distinct turning points. These are results about the full susceptible-depletion-coupled model, not a fixed selection environment.

## Assumptions and scope
Let \(\lambda\in\mathbb R\) be an unrestricted mathematical infectivity coordinate, and let the infected density \(\rho(\lambda,t)\), recovered fraction \(r(t)\), infected fraction \(i(t)=\int_{\mathbb R}\rho(\lambda,t)\,d\lambda\), and susceptible fraction \(s(t)=1-i(t)-r(t)\) obey
\[
\partial_t\rho=(k s(t)\lambda-\mu)\rho+\frac{\mathcal D}{2}\partial_{\lambda\lambda}\rho,\qquad r'(t)=\mu i(t),
\]
with \(k,\mu,\mathcal D>0\). This is Equation (1)–(2) in [1], taken **literally on the full real trait line**, without a finite-domain truncation or probability cap on \(\lambda\). For \(v>0\), set \(\phi_v(y)=(2\pi v)^{-1/2}\exp[-y^2/(2v)]\). Take
\[
\rho(\lambda,0)=i_0\big[(1-p_0)\phi_{v_0}(\lambda-a)+p_0\phi_{v_0}(\lambda-a-\Delta)\big],\quad
r(0)=0,\quad s_0=1-i_0,
\]
where \(i_0,p_0\in(0,1)\), \(v_0,a,\Delta>0\). All inequalities and uniqueness statements below quantify over every such \(i_0,p_0,v_0,a,k,\mu,\Delta,\mathcal D\) satisfying their explicit restrictions. The variance is conditioned on infection: \(V(t)=\int(\lambda-\bar\lambda(t))^2\rho(\lambda,t)\,d\lambda/i(t)\).

## Proof
**Exact invariant mixture.** Define four scalar functions \(i,r,p,z\) by
\[
\begin{aligned}
 i'&=i\{ks(a+z+\Delta p)-\mu\},&r'&=\mu i,\\
 p'&=ks\Delta p(1-p),&z'&=ks(v_0+\mathcal Dt),\\
 s&=1-i-r,&(i,r,p,z)(0)&=(i_0,0,p_0,0).
\end{aligned}
\]
Then the exact infected-density solution is
\[
\rho(\lambda,t)=i(t)\left[(1-p(t))\phi_{v(t)}(\lambda-a-z(t))
+p(t)\phi_{v(t)}(\lambda-a-z(t)-\Delta)\right],\quad v(t)=v_0+\mathcal Dt.
\]
Indeed, each component has mass \(M_j\), mean \(m_j=a+z+j\Delta\) for \(j=0,1\), and common variance \(v\). Direct differentiation of a normalized Gaussian shows that it solves the PDE whenever \(v'=\mathcal D\), \(m'_j=ksv\) and \(M'_j=(ksm_j-\mu)M_j\). With \(M_0=i(1-p)\), \(M_1=ip\), these are precisely the displayed scalar equations. Gaussian integration gives the mean \(\bar\lambda=a+z+\Delta p\), and hence
\[
\boxed{V(t)=v_0+\mathcal Dt+\Delta^2p(t)(1-p(t)),\qquad
V'(t)=\mathcal D-ks(t)\Delta^3p(t)(1-p(t))(2p(t)-1).}
\]

**Global admissibility and depletion.** The scalar equations preserve \(i,r\geq0\), \(0<p<1\), \(s>0\), and \(i+r+s=1\): specifically \(s'=-ks i(a+z+\Delta p)<0\). Also \(0\leq z'(t)\leq k(v_0+\mathcal Dt)\); boundedness on each finite time interval proves global existence and keeps \(i(t)>0\). In fact \(s(t)\to0\). Otherwise \(s(t)\geq s_\infty>0\), so \(z'\geq ks_\infty(v_0+\mathcal Dt)\), whence \(z(t)\to\infty\). The infected growth rate \(i'/i=ks(a+z+\Delta p)-\mu\) would eventually exceed a positive constant, implying \(i(t)\to\infty\), contrary to \(i\leq1\). Thus \(s_\infty=0\) and \(V'(t)\to\mathcal D>0\).

**Sharp universal boundary.** Write \(g(p)=p(1-p)(2p-1)\). Its maximum on \([0,1]\) is \(1/(6\sqrt3)\), attained uniquely at \(p_*=(1+1/\sqrt3)/2\); this follows by differentiating the cubic. As \(s(t)\leq s_0\), if \(\mathcal D\geq\mathcal D_{\mathrm{crit}}\) then \(V'\geq0\). For every \(t>0\), the strict inequality \(s(t)<s_0\) actually gives \(V'(t)>0\), including at the threshold. If instead \(0<\mathcal D<\mathcal D_{\mathrm{crit}}\) and \(p_0=p_*\), then \(V'(0)<0\). Since \(p'>0\), the function \(g(p(t))\) decreases strictly for \(p(t)>p_*\), and so does \(s(t)g(p(t))\). It tends to zero because \(s(t)\to0\), so the equation \(V'(t)=0\) has exactly one solution, at a strict global minimum. Hence the uniform diffusion cutoff is both sufficient and necessary.

**Certified double reversal.** Set
\[
k=10,\quad\mu=1,\quad a=\frac15,\quad\Delta=\frac1{10},\quad
v_0=\frac1{100000},\quad\mathcal D=\frac1{1600},\quad
p_0=\frac35,\quad i_0=10^{-6}.
\]
Here \(k\Delta=1\) and \(k\Delta^3=1/100\). Since \(g(3/5)=6/125\),
\(V'(0)>1/1600-(1/100)(6/125)>0\). For \(0\leq t\leq2\), \(z(t)\leq k(2v_0+2\mathcal D)=127/10000\), so \(k\bar\lambda(t)<4\). The equations imply \(i(t)\leq10^{-6}e^{4t}\) and \(s(t)\geq1-10^{-6}e^{4t}>0.99\), using \(e^8<3^8\). The logistic equation gives
\[
\log\frac{p(2)}{1-p(2)}-\log\frac{p_0}{1-p_0}=\int_0^2s(t)\,dt>1.8>\log\frac83.
\]
Consequently some \(t_*\in(0,2)\) has \(p(t_*)=4/5\). Because \(g(4/5)=12/125\) and \(s(t_*)>0.9\),
\[
V'(t_*)<\frac1{1600}-\frac1{100}\frac9{10}\frac{12}{125}<0.
\]
Finally \(V'(t)\to1/1600>0\). Continuity yields at least one local maximum before \(t_*\) and at least one local minimum after it, with strictly alternating observed derivative signs. No numerical root count or unproved uniqueness of these extrema is asserted.

## Verification
The accompanying standalone `verify.py` checks the Gaussian PDE residual algebraically using \(v'=\mathcal D\), \(m'=ksv\) and component mass equations; the exact mixture-variance derivative; the cubic maximizer; and all rational inequalities in the explicit double-reversal certificate. Numerical integration of the four-dimensional closure and independent quadrature of the evolving Gaussian mixture also agree with the exact formulas, with derivative signs \(+,-,+\) at times \(0,0.6,3\). Execute `python verify.py` with Python 3, SymPy, SciPy and NumPy. The infinite-time result comes from the foregoing analytic proof, not the numerical tests.

## Relationship to prior work
The originating epidemic paper [1], especially its supplementary moment calculation, derives \(\bar\lambda'=ksV\) and approximates \(V\simeq\mathcal Dt\) when distributional skewness is negligible. Its derivation explicitly notes the third central moment in the exact variance equation. The present two-mode result instead keeps that skewness **exactly**, obtaining a sharp all-initial-mixture-weight threshold and a rigorously certified increase–decrease–increase example in the coupled epidemic.

General linear-fitness replicator–mutator solution techniques and Gaussian propagation are established in [2] and [3], and multimodal evolutionary distributions are analyzed more broadly in [4]. The novelty claimed here is **not** Gaussian closure or the general mutation–selection method, but the sharp uniform susceptibility-dependent threshold, its necessity and the re-entrant two-turning-point phenomenon for the specific endogenous epidemic equations. The comparison is literature-bounded, not a claim of independently established publication priority.

## Limitations
The exact assertions hold for a formal continuum trait coordinate \(\lambda\in\mathbb R\). Gaussian components have nonzero tails for negative \(\lambda\) and values above one, so this is not an exact physical probability-valued infectivity distribution on \([0,1]\). Reflecting/absorbing boundaries, discrete mutation, intervention changes, finite stochastic populations and empirically estimated pathogen diversity are **not** covered. The two-extrema witness proves existence of at least two turning points, not that there are exactly two. Positive mean infectivity, and hence the scalar susceptible monotonicity used in the proof, follow from \(a>0\) and \(z,p\geq0\). No independent scientific audit has been performed.

## References
1. S. Lamata-Otín, A. Arenas, J. Gómez-Gardeñes and D. Soriano-Paños, *Interplay between evolutionary and epidemic time scales challenges the outcome of control policies*, first public arXiv version 19 March 2026, https://arxiv.org/abs/2603.18801 ; full October 2026 version https://arxiv.org/html/2603.18801v2 , particularly Equations (1)–(2) and Supplementary Note 2.
2. M. Alfaro and R. Carles, *Explicit solutions for replicator-mutator equations: extinction vs. acceleration*, 2014, https://arxiv.org/abs/1405.2768 .
3. M. Alfaro and M. Veruete, *Density dependent replicator-mutator models in directed evolution*, 2019 preprint, https://arxiv.org/abs/1901.07848 ; journal DOI https://doi.org/10.3934/dcdsb.2019224 .
4. S. Lion, A. Sasaki and M. Boots, *Extending eco-evolutionary theory with oligomorphic dynamics*, Ecology Letters 26 (2023), https://doi.org/10.1111/ele.14183 .
