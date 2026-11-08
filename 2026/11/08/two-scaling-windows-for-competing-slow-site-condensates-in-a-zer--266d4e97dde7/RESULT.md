# Two scaling windows for competing slow-site condensates in a zero-range ring

## Finding

For a constant-rate, totally asymmetric zero-range process on a directed ring, two slow sites compete for the excess mass. Their asymmetry becomes observable on different scales at and above the critical density. The exact canonical formulas below establish both scaling limits, the full limiting joint occupations, and the first finite-size corrections to the stationary current.

Fix \(0<q<1\), \(\theta\in\mathbb R\), and set
\[
\mu=\frac{q}{1-q},\qquad \sigma^2=\frac{q}{(1-q)^2},\qquad
I_\theta(t)=\int_0^t e^{\theta v}\,dv.
\]
Let \(K_1,K_2\) be the occupations of the two slow sites and let \(J_L\) be the mean stationary rate of successful departures across any one directed edge. For each \(L\), there are \(L\) ordinary sites and two slow sites, with exactly \(M_L\) particles in total.

**Critical window.** Suppose \(M_L=\lfloor\mu L+h\sqrt L\rfloor\), with \(h\in\mathbb R\), and the slow-site departure rates are \(q e^{-\theta/\sqrt L}\) and \(q\). Then
\[
\left(\frac{K_1}{\sqrt L},\frac{K_2}{\sqrt L}\right)
\Longrightarrow (X,Y),
\qquad
f_{h,\theta}(x,y)=\frac{\mathbf1_{\{x,y\ge0\}}}{A_{h,\theta}}
 e^{\theta x}\,\phi_\sigma(h-x-y),
\]
where
\[
\phi_\sigma(w)=\frac{e^{-w^2/(2\sigma^2)}}{\sqrt{2\pi}\sigma},\qquad
A_{h,\theta}=\int_0^\infty I_\theta(t)\phi_\sigma(h-t)\,dt>0.
\]
The current has the exact leading correction
\[
\lim_{L\to\infty}\sqrt L\left(1-\frac{J_L}{q}\right)
=\frac{B_{h,\theta}}{A_{h,\theta}},\qquad
B_{h,\theta}=\int_0^\infty e^{\theta t}\phi_\sigma(h-t)\,dt.
\]
For equal slow rates and exactly critical density (\(h=\theta=0\)), \((X+Y)\) is Rayleigh with scale \(\sigma\), and
\[
\lim_{L\to\infty}\sqrt L\left(1-\frac{J_L}{q}\right)
=\frac{\sqrt{\pi/2}}{\sigma}.
\]

**Condensed window.** Suppose instead \(M_L=\lfloor\rho L\rfloor\) for fixed \(\rho>\mu\), set \(\alpha=\rho-\mu\), and choose slow rates \(q e^{-\theta/L}\) and \(q\). Then
\[
\left(\frac{K_1}{L},\frac{K_2}{L}\right)
\Longrightarrow (U,\alpha-U),
\quad \Pr(U\in du)=\frac{e^{\theta u}}{I_\theta(\alpha)}
\mathbf1_{[0,\alpha]}(u)\,du,
\]
and
\[
\lim_{L\to\infty}L\left(1-\frac{J_L}{q}\right)
=\frac{e^{\theta\alpha}}{I_\theta(\alpha)}.
\]
The centered bulk particle number, divided by \(\sqrt L\), converges jointly and independently of \(U\) to a normal random variable with mean zero and variance \(\sigma^2\). These are canonical stationary laws, not dynamical relaxation-time laws.

## Assumptions and scope

The system has \(L+2\) sites arranged in a directed cycle, with \(L\ge2\), and indistinguishable particles with unrestricted on-site occupancy. At each nonempty site a *single particle* hops clockwise at a rate determined by that departure site, independent of its positive occupancy. The \(L\) ordinary rates are one. The two exceptional departure rates are as stated in the respective window; for every sufficiently large \(L\) both lie strictly between zero and one. Total mass \(M_L\) is fixed, and there is no injection or removal. The finite-state chain is irreducible and has a unique stationary distribution. All limits hold with fixed \(q,\theta\), and, as applicable, fixed \(h\) or \(\rho\).

## Proof

**1. Product stationary state and exact finite reduction.** For a finite directed zero-range ring with site rates \(r_i>0\), a configuration \(\eta\) of total mass \(M\) has stationary weight proportional to \(\prod_i r_i^{-\eta_i}\). Indeed, for each nonempty destination \(i+1\), the incoming flux from \(\eta+e_i-e_{i+1}\) equals \(r_{i+1}\) times the weight of \(\eta\); summing these incoming contributions balances the total outgoing flux \(\sum_{j:\eta_j>0}r_j\) times that weight. Irreducibility establishes uniqueness.

Write \(b_L=\theta/\sqrt L\) in the critical window and \(b_L=\theta/L\) in the condensed window. The two slow sites have weights \(q^{-j}e^{b_Lj}\) and \(q^{-k}\). Let \(S_L\) be a sum of \(L\) independent geometric variables \(G_i\), each with \(\Pr(G_i=m)=(1-q)q^m\) for \(m\ge0\), and let \(p_L(s)=\Pr(S_L=s)\). Summing over the ordinary-site occupancies gives the exact law, with \(p_L(s)=0\) for negative \(s\),
\[
\Pr(K_1=j,K_2=k)=\frac{e^{b_Lj}\,p_L(M_L-j-k)}{D_L},
\quad j,k\in\mathbb Z_{\ge0},\quad j+k\le M_L,
\]
\[
H_L(t)=\sum_{j=0}^{t}e^{b_Lj},\qquad
D_L=\sum_{t=0}^{M_L}p_L(M_L-t)H_L(t).
\]
The physical canonical partition function is \(Z_L(M)=q^{-M}(1-q)^{-L}D_L(M)\). The mean current across every edge is \(Z_L(M-1)/Z_L(M)\), because removal of a single particle at a specified nonempty departure site cancels its rate against one stationary-weight factor. Thus, with \(H_L(-1)=0\),
\[
\frac{J_L}{q}=\frac{D_L(M_L-1)}{D_L(M_L)}
=1-\frac{\sum_{t=0}^{M_L}p_L(M_L-t)e^{b_Lt}}{D_L}.
\tag{1}
\]
These are exact finite-size identities, including the field-dependent rate normalization.

**2. Condensed scale.** The geometric sum has mean \(\mu L\) and variance \(\sigma^2L\). For \(\rho>\mu\), the law of large numbers gives \((M_L-S_L)/L\to\alpha\) under its unconditioned distribution. Uniformly for \(t/L\) in compact intervals,
\[
L^{-1}H_L(t)\longrightarrow I_\theta(t/L)
\]
by Riemann summation. As \(0\le t\le M_L\) and \(\rho\) is fixed, the normalized sums have a uniform bound, so
\[
\frac{D_L}{L}\longrightarrow I_\theta(\alpha),\quad
\sum_{t=0}^{M_L}p_L(M_L-t)e^{\theta t/L}
\longrightarrow e^{\theta\alpha}.
\]
Conditionally on the total defect mass \(t=K_1+K_2\), the first occupation has distribution proportional to \(e^{\theta j/L}\), \(0\le j\le t\). Riemann sums yield the asserted tilted-uniform density on \([0,\alpha]\). The same normalization ratio tends to a constant on the bulk's \(\sqrt L\)-fluctuation scale; hence the ordinary geometric central limit theorem and the conditional Riemann-sum limit give their claimed joint independence. Substitution into (1) proves the \(L^{-1}\) current correction.

**3. Critical scale.** Now \((M_L-\mu L)/\sqrt L\to h\). The aperiodic local central limit theorem for geometric sums gives, uniformly on bounded nonnegative \(t/\sqrt L\),
\[
\sqrt L\,p_L(M_L-t)
\longrightarrow \phi_\sigma(h-t/\sqrt L).
\]
With \(b_L=\theta/\sqrt L\), Riemann summation gives
\[
\frac{H_L(t)}{\sqrt L}\longrightarrow I_\theta(t/\sqrt L)
\]
uniformly on the same bounded ranges. Standard geometric Chernoff bounds control the unbounded remainder: for \(|M_L-\mu L|=O(\sqrt L)\), the lower-tail probability of \(S_L\) is bounded by a constant times \(\exp[-c((t/\sqrt L)-C)_+^2]\) for \(0\le t\le M_L\), with positive constants depending on \(q,h\). This dominates the factor \((1+t/\sqrt L)e^{|\theta|t/\sqrt L}\) and yields uniform integrability. It follows that
\[
\frac{D_L}{\sqrt L}\longrightarrow A_{h,\theta},\qquad
\sum_{t=0}^{M_L}p_L(M_L-t)e^{\theta t/\sqrt L}
\longrightarrow B_{h,\theta}.
\]
Consequently the defect total \((K_1+K_2)/\sqrt L\) converges to a variable with density proportional to \(I_\theta(t)\phi_\sigma(h-t)\), \(t\ge0\). Given total \(t\), the conditional split of the first occupation has limiting density \(e^{\theta x}/I_\theta(t)\) for \(0\le x\le t\). Multiplying the two densities yields the joint density \(f_{h,\theta}\), including its normalization. Equation (1) now gives the \(L^{-1/2}\) current correction. At \(h=\theta=0\), the total-mass density is \(t\exp[-t^2/(2\sigma^2)]/\sigma^2\), the stated Rayleigh law; evaluating the two Gaussian integrals gives the displayed current constant.

This completes both limits for every allowed fixed parameter choice.

## Verification

Run `python3 verify.py` from this package. The checker uses only the Python standard library. It tests exact rational stationary balance and current identities for 28 finite labeled-state systems, checks finite two-defect probabilities, and compares canonical sums with the limiting current and occupation formulas on sequences of increasing sizes. The implementation replays finite-state invariance directly, rather than assuming the product state in those tests. This is numerical and finite verification; the infinite claims rest on the argument above.

## Relationship to prior work

The zero-range product form, canonical partition-function framework, single-defect condensation, and homogeneous/heterogeneous Bose-gas analogy are established results, not claimed here. Angel, Evans and Mukamel (2004) study a *single* special site with occupation-dependent rates. Evans, Majumdar and Zia (2005 preprint) develop canonical condensate distributions in factorized states, concentrating on homogeneous site weights. Schwarzkopf, Evans and Mukamel (2008) study multiple condensates arising from occupancy-dependent nonmonotone rates, rather than two deterministic constant-rate defects. Mailler, Mörters and Ueltschi (2015) study weak random site disorder and typically a single condensate chosen from many sites. Rafferty (2016 thesis, accessible abstract and indexed excerpts) studies relaxation for one and two **equal-rate** defects. The new narrowly scoped statements are the joint near-critical and supercritical *two-site weak-asymmetry laws with their differing strength scales* and the exact leading current correction in each window. No claim is made that the symmetric two-site model or product stationary measure was first introduced here.

## Limitations

No spectral gap, mixing time, transient growth law, or thermodynamic Gibbs-state transition is asserted. The infinite-limit conclusions require \(q\) fixed in \((0,1)\) and the stated fixed-parameter scalings; arbitrary simultaneous changes of \(q\), the density, or the bias are not covered. Finite verification cannot establish an infinite-size theorem. Historical novelty is assessed against accessible sources; the complete text of the highly relevant 2016 two-defect thesis was not reliably retrievable, so an unobserved equivalent finite-size statement remains a priority risk.

## References

- A. G. Angel, M. R. Evans and D. Mukamel, *Condensation transitions in a one-dimensional zero-range process with a single defect site*, arXiv:cond-mat/0401262 (first public posting 2004-01-15); https://arxiv.org/abs/cond-mat/0401262.
- M. R. Evans, S. N. Majumdar and R. K. P. Zia, *Canonical analysis of condensation in factorised steady states*, arXiv:cond-mat/0510512 (first public posting 2005-10-19); https://arxiv.org/abs/cond-mat/0510512.
- Y. Schwarzkopf, M. R. Evans and D. Mukamel, *Zero-Range Processes with Multiple Condensates: Statics and Dynamics*, arXiv:0801.4501 (first public posting 2008-01-29); https://arxiv.org/abs/0801.4501.
- C. Mailler, P. Mörters and D. Ueltschi, *Condensation and symmetry-breaking in the zero-range process with weak site disorder*, arXiv:1509.07672 (first public posting 2015-09-25); https://arxiv.org/abs/1509.07672.
- T. Rafferty, *Dynamic properties of condensing particle systems*, PhD thesis, University of Warwick (2016); https://wrap.warwick.ac.uk/91746/.
- S. Sethuraman and J. Xue, *Condensation, boundary conditions, and effects of slow sites in zero-range systems*, *Annals of Probability* 52 (2024), 1048–1092; https://doi.org/10.1214/24-AOP1684.
