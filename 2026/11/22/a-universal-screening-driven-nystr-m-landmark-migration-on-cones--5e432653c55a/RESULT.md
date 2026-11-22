# A universal screening-driven Nyström landmark migration on cones over walk-regular graphs

## Finding

**Theorem (unique hub-to-periphery migration).** Let \(H\) be a finite, connected, noncomplete, simple **walk-regular** graph on \(m\ge4\) vertices, and let \(G=K_1\vee H\) denote its unweighted graph cone with distinguished universal vertex \(o\). Walk-regular means that for each nonnegative integer \(r\), the diagonal of the adjacency power \(A_H^r\) is constant. Let

\[
0=\nu_0<\nu_1\le\cdots\le\nu_{m-1}\le m
\]

be the Laplacian eigenvalues of \(H\), with multiplicity, and put \(c_j=m-\nu_j\) and \(b_j=1+\nu_j\) for \(1\le j<m\). At least one \(c_j\) is positive and all are nonnegative. For every real \(\mu>0\), define the strictly positive matrix

\[
K_\mu=(\mu I+L_G)^{-1}
\]

and the standard rank-one Nyström trace error of selecting a vertex \(v\) by

\[
\mathcal E_v(\mu)=\operatorname{tr}\!\left(K_\mu-
\frac{K_\mu e_v e_v^{\mathsf T}K_\mu}{e_v^{\mathsf T}K_\mu e_v}\right).
\]

All peripheral vertices have the same error, denoted \(\mathcal E_p(\mu)\). There exists **exactly one** positive transition \(\mu_*(H)\), characterized as the unique zero of

\[
\Phi_H(\mu)=\sum_{j=1}^{m-1}
\frac{(m-\nu_j)(1+\nu_j-\mu^2)}{(\mu+1+\nu_j)^2}.
\]

For \(0<\mu<\mu_*(H)\) the hub alone minimizes error; for \(\mu>\mu_*(H)\) precisely the \(m\) peripheral vertices minimize error; at \(\mu=\mu_*(H)\) all \(m+1\) vertices tie. The transition satisfies

\[
\min_{j:c_j>0}\sqrt{1+\nu_j}\ \le\ \mu_*(H)\ \le\
\max_{j:c_j>0}\sqrt{1+\nu_j},
\]

with strict inequalities whenever there are two distinct contributing eigenvalues.

**Diagonal-ranking reversal.** Although the hub uniquely minimizes Nyström trace error for all sufficiently weak screening, its Green diagonal is **strictly smaller** than every peripheral Green diagonal for every \(\mu>0\). Thus selecting the largest diagonal of \(K_\mu\) does not in general select the best single Nyström column.

**Wheel specialization.** For \(H=C_m\), \(m\ge4\), write \(\mu_m=\mu_*(C_m)\). Then

\[
\nu_j=2-2\cos(2\pi j/m),\qquad
\Phi_{C_m}(\mu)=\sum_{j=1}^{m-1}
\frac{(m-\nu_j)(1+\nu_j-\mu^2)}{(\mu+1+\nu_j)^2}.
\]

In particular, \(\mu_4=\sqrt3\). For growing wheel rims,

\[
\mu_m=\sqrt6-1+\frac{\gamma}{m}+O(m^{-2}),
\]

where, with \(x=\sqrt6-1\) and \(D=(x+1)(x+5)\),

\[
\gamma=\frac{D\bigl(x(x+1)^2-2\sqrt D\bigr)}{2(x+1)^3}
=0.401808147027\ldots>0.
\]

## Assumptions and scope

All graphs are finite, undirected, simple and unweighted; the Laplacian is combinatorial \(L=D-A\), not degree-normalized. The join adds one universal vertex with conductance one on every new edge. The parameter \(\mu>0\) applies **uniformly to every vertex** as a diagonal shift. The selected columns are exactly one **unrescaled** principal Nyström column, and the loss is the trace of the positive semidefinite residual, not a Frobenius or operator norm. The base is connected, walk-regular and not complete. Complete bases are a genuine boundary: if \(H=K_m\), then \(G=K_{m+1}\) and all columns tie at every \(\mu>0\).

The same trace error can be written as

\[
\mathcal E_v(\mu)=\operatorname{tr}\bigl[(\mu I+L_G)_{-v,-v}^{-1}\bigr],
\]

where the subscript means the principal matrix retaining all vertices except \(v\). This is a **uniformly screened grounded** trace objective, and is not the unscreened perfect-leader problem.

## Proof

1. **Spectral reduction.** The cone Laplacian has eigenvalues \(0\), \(m+1\), and \(1+\nu_j\) for \(1\le j<m\). The first two modes span the constant vector and the hub-versus-base contrast, respectively; the other modes have zero hub coordinate. Walk-regularity implies equal diagonals of every spectral projector of \(L_H\); hence each peripheral vertex has spectral weight \(1/m\) per eigenvalue occurrence when multiplicities are counted. This gives, with \(h=(K_\mu)_{oo}\) and \(r=(K_\mu)_{pp}\),

   \[
   h=\frac{\mu+1}{\mu(\mu+m+1)},\qquad
   r-h=\frac1m\sum_{j=1}^{m-1}
   \left(\frac1{\mu+1+\nu_j}-\frac1{\mu+m+1}\right).
   \]

   For any simple graph \(H\), the complement identity \(L_H+L_{\overline H}=mI-J\) shows that every nonzero Laplacian eigenvalue of \(H\) is at most \(m\). All \(c_j\) are therefore nonnegative. They cannot all vanish unless \(H\) is complete (because that would force the nonzero spectrum of \(L_H\) to be entirely \(m\), hence \(L_H=mI-J\)).

2. **Exact positive diagonal ratio.** Dividing the preceding formula by \(h\) yields

   \[
   Q(\mu):=\frac rh=1+\frac1m\sum_{j=1}^{m-1}
   \frac{c_j\mu}{(\mu+1)(\mu+b_j)}>1.
   \]

   Thus the peripheral diagonal is always larger than the hub diagonal, strictly.

3. **Trace-error comparison and unique zero.** For every positive definite resolvent \(K_\mu\),

   \[
   -\frac{\mathrm d}{\mathrm d\mu}\log(K_\mu)_{vv}
    =\frac{(K_\mu^2)_{vv}}{(K_\mu)_{vv}}=:T_v(\mu).
   \]

   Since \(\mathcal E_v=\operatorname{tr}K_\mu-T_v\), the hub is better exactly when

   \[
   T_o-T_p=\frac{\mathrm d}{\mathrm d\mu}\log Q(\mu)>0.
   \]

   Direct differentiation gives

   \[
   Q'(\mu)=\frac{\Phi_H(\mu)}{m(\mu+1)^2}.
   \]

   Every summand of \(\Phi_H\) with \(c_j>0\) is strictly decreasing in \(\mu\):

   \[
   \frac{\mathrm d}{\mathrm d\mu}
   \frac{b_j-\mu^2}{(\mu+b_j)^2}
   =-\frac{2b_j(\mu+1)}{(\mu+b_j)^3}<0.
   \]

   Also \(\Phi_H(0)>0\), whereas \(\lim_{\mu\to\infty}\Phi_H(\mu)=-\sum_jc_j<0\). Continuity and strict monotonicity give one and only one positive zero, and the claimed strict inequalities and ties follow. The stated root bounds follow because every summand changes sign at \(\sqrt{b_j}\).

4. **Sharp wheel-size expansion.** For the wheel rim, put \(\nu(\theta)=2-2\cos\theta\) and \(f_\mu(\nu)=(1+\nu-\mu^2)/(\mu+1+\nu)^2\). Dividing the threshold equation by \(m\) and using the periodic trapezoidal rule for its analytic integrands gives, locally uniformly in \(\mu>0\),

   \[
   \frac{\Phi_{C_m}(\mu)}{m^2}=I(\mu)-\frac{f_\mu(0)+J(\mu)}m+O(e^{-c_\mu m}),
   \]

   where \(I(\mu)=(2\pi)^{-1}\int_0^{2\pi}f_\mu(\nu(\theta))\,\mathrm d\theta\) and \(J(\mu)=(2\pi)^{-1}\int_0^{2\pi}\nu(\theta)f_\mu(\nu(\theta))\,\mathrm d\theta\). The standard elementary cycle-resolvent integral is

   \[
   \frac1{2\pi}\int_0^{2\pi}\frac{\mathrm d\theta}{\mu+3-2\cos\theta}
   =\frac1{\sqrt{(\mu+1)(\mu+5)}}.
   \]

   Differentiating this integral gives

   \[
   I(\mu)=\frac{(\mu+1)(5-2\mu-\mu^2)}{[(\mu+1)(\mu+5)]^{3/2}}.
   \]

   Its unique positive root is \(x=\sqrt6-1\), with \(I'(x)=-2(x+1)^2/D^{3/2}<0\). At that root, \(J(x)=1-x(x+1)/\sqrt D\) and \(f_x(0)=(1-x)/(1+x)\). The implicit function expansion therefore gives

   \[
   \mu_m=x+\frac{f_x(0)+J(x)}{mI'(x)}+O(m^{-2}),
   \]

   whose coefficient simplifies to \(\gamma\) above. It is strictly positive because, after squaring the positive sides, \(x(x+1)^2>2\sqrt D\) reduces to \(57>22\sqrt6\). For \(m=4\), the only contributing nonzero eigenvalue is \(2\), so \(\Phi_{C_4}\) vanishes at \(\sqrt3\) exactly.

This proves the entire statement for every admissible graph and every \(\mu>0\), without relying on finite enumeration.

## Verification

The included standalone `verify_cone.py` constructs eleven example base graphs (cycles, complete bipartite graphs, the triangular prism and the Petersen graph), computes exact rational Green matrices, verifies the spectral diagonal ratio, the derivative/capture identity, and the equality to screened grounded inverse trace. It also checks the exact four-rim transition and the wheel asymptotic coefficient numerically. Run `python verify_cone.py` with SymPy, NumPy and SciPy installed. The executable reports 1483 assertions; these tests corroborate the analytic proof rather than certifying all graphs or real screening values.

## Relationship to prior work

The single-column Nyström approximation and trace-loss objective belong to the established SPSD matrix sketching framework; see Gittens and Mahoney (2013). Noise-free leader selection and grounded-Laplacian inverse-trace criteria were studied by Lin, Fardad and Jovanović (2013), and a graph centrality interpretation of one unscreened leader was established by Fitch and Leonard (2014). The present statement concerns a *uniformly shifted* cone Laplacian, all positive shifts, and every connected noncomplete walk-regular base. It supplies a unique transition, its spectral equation, strict diagonal-ranking reversal and the wheel-size expansion. Altering peripheral edge weights with no uniform shift is a different matrix family and does not directly provide this shift-driven theorem.

## Limitations

This classification is for a single column and trace error only. Walk-regularity is used to identify all peripheral columns; general irregular bases may have multiple peripheral types. Exact thresholds require base Laplacian eigenvalues and may not have radical closed forms. The wheel expansion holds with fixed unit edge conductances and large rim size, not arbitrary weighted cones. No claim is made about independently verified publication priority or optimal multi-column selection.

## References

- Fu Lin, Makan Fardad and Mihailo R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first posted 2013-02-03), https://arxiv.org/abs/1302.0450 .
- Alex Gittens and Michael W. Mahoney, *Revisiting the Nyström Method for Improved Large-Scale Machine Learning*, arXiv:1303.1849 (first posted 2013-03-07); ICML 2013, https://proceedings.mlr.press/v28/gittens13.html .
- Katherine E. Fitch and Naomi Ehrich Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first posted 2014-07-07), https://arxiv.org/abs/1407.1569 .
