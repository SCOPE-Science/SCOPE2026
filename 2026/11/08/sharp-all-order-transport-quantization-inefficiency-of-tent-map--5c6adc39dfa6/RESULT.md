# Sharp all-order transport quantization inefficiency of tent-map periodic points

## Finding

Let \(T:[0,1]\to[0,1]\) be the full tent map \(T(x)=2\min\{x,1-x\}\). For every integer \(n\ge1\), put \(m=2^n\) and let \(\mu_n\) be the uniform probability on the \(m\) *distinct* fixed points of \(T^n\) (including points of smaller least period). Let \(\lambda\) denote Lebesgue probability on \([0,1]\). For one-dimensional Wasserstein distances with Euclidean cost, the exact identities are

\[
W_1(\mu_n,\lambda)=\frac{2m^2-1}{6m(m^2-1)},\qquad
W_2(\mu_n,\lambda)^2=\frac1{6(m^2-1)},\qquad
W_\infty(\mu_n,\lambda)=\frac1m.
\]

For every fixed real \(1\le p<\infty\), the full spectrum has the sharp asymptotic

\[
W_p(\mu_n,\lambda)=\frac1m\left(\frac{2}{(p+1)(p+2)}\right)^{1/p}
\left(1+O_p(m^{-1})\right).
\]

In contrast, the best approximation of \(\lambda\) by **any** probability supported on at most \(m\) points, with arbitrary atom masses, has optimal error \(Q_{m,p}=1/[2m(p+1)^{1/p}]\) for finite \(p\), and \(Q_{m,\infty}=1/(2m)\). Thus the precise asymptotic *relative inefficiency* of the dynamical fixed-point measure is

\[
\lim_{n\to\infty}\frac{W_p(\mu_n,\lambda)}{Q_{m,p}}
=\left(\frac{2^{p+1}}{p+2}\right)^{1/p}
\quad(1\le p<\infty),
\qquad
\frac{W_\infty(\mu_n,\lambda)}{Q_{m,\infty}}=2.
\]

In particular, the finite-order penalties at \(p=1\) and \(p=2\) approach \(4/3\) and \(\sqrt2\), respectively. The loss is intrinsic to the selected periodic-point locations: although \(\mu_n\) converges to Lebesgue measure at the optimal *order* \(m^{-1}\), its equal-mass quantile cells are persistently off-centered.

## Assumptions and scope

All quantifiers above concern integer \(n\ge1\) and fixed real \(p\ge1\). The limit and \(O_p\) statement hold separately for each *fixed finite* \(p\) (not uniformly as \(p\to\infty\)). Distances \(W_p\) use \(|x-y|\) on the closed real interval, not circular distance. The measure \(\mu_n\) counts each point of \(\mathrm{Fix}(T^n)\) once; it is not uniform over primitive cycles. The optimization defining \(Q_{m,p}\) allows unequal atom weights and at most \(m\) support points. No regularity or randomness assumption is imposed beyond this explicit map and the defined measures.

## Proof

**1. Exact ordered periodic-point grid.** Write \(h(t)=2\min\{t,1-t\}\) for \(t\in[0,1)\), extended periodically to the circle. The identity \(T\circ h=h\circ D\), where \(D(t)=2t\pmod1\), and \(h(s)=h(t)\) iff \(s\equiv t\) or \(s\equiv-t\pmod1\), give \(T^n(h(t))=h(t)\) exactly when \(mt\equiv\pm t\pmod1\). Folding the two rational solution grids gives

\[
\mathrm{Fix}(T^n)=\left\{\frac{2k}{m-1}:0\le k\le \frac m2-1\right\}
\cup\left\{\frac{2k}{m+1}:0\le k\le\frac m2\right\}.
\]

The sets meet only at zero: since \(m\) is even, \(m-1\) and \(m+1\) are coprime. These points are in the strictly increasing order

\[
x_{2k}=\frac{2k}{m-1},\qquad
x_{2k+1}=\frac{2(k+1)}{m+1},
\qquad 0\le k\le\frac m2-1.
\]

For every \(j=0,\ldots,m-1\), direct inequalities show \(j/m\le x_j\le(j+1)/m\). In particular, exactly one periodic point lies in each natural dyadic cell, but generally not at its midpoint. The point coordinates are classical; the following transport conclusions are the new object of study.

**2. Monotone transport and exact first two costs.** Since \(\lambda\) is uniform and \(\mu_n\) assigns equal mass to its sorted points, the increasing quantile coupling (optimal for any \(p\ge1\)) sends the cell \([j/m,(j+1)/m]\) to \(x_j\). Thus

\[
W_p(\mu_n,\lambda)^p
=\sum_{j=0}^{m-1}\int_{j/m}^{(j+1)/m}|u-x_j|^p\,du
\quad(1\le p<\infty),
\]

and \(W_\infty\) is the largest cell-to-atom displacement. Define \(d_j=m[x_j-(j+1/2)/m]\). The exact normalized offsets split into two arithmetic grids:

\[
d_{2k}=\frac{2k}{m-1}-\frac12,\qquad
d_{2k+1}=\frac12-\frac{2(k+1)}{m+1},\quad
0\le k\le\frac m2-1.
\]

Elementary summation of the two arithmetic progressions yields

\[
\sum_{j=0}^{m-1}d_j^2=\frac{m(m^2+1)}{12(m^2-1)}.
\]

On an interval of length \(1/m\) centered at \((j+1/2)/m\), whose selected atom lies inside it, the absolute first moment is \(1/(4m^2)+d_j^2/m^2\). Consequently

\[
W_1=\frac1{4m}+\frac1{m^2}\sum_jd_j^2
=\frac{2m^2-1}{6m(m^2-1)}.
\]

The second moment of the same cell is \(1/(12m^3)+d_j^2/m^3\), so

\[
W_2^2=\frac1{12m^2}+\frac1{m^3}\sum_jd_j^2
=\frac1{6(m^2-1)}.
\]

All atoms lie inside their assigned cells, giving \(W_\infty\le1/m\); the first atom \(x_0=0\) serves the full interval \([0,1/m]\), so equality holds.

**3. Transport law for all finite powers.** Rescale a cell around its midpoint. The exact identity is

\[
m^pW_p^p=\frac1m\sum_{j=0}^{m-1}F_p(d_j),
\qquad F_p(v)=\int_{-1/2}^{1/2}|t-v|^p\,dt.
\]

Both offset grids in step 2 become uniform on \([-1/2,1/2]\) as \(m\to\infty\), with quadrature error \(O_p(m^{-1})\) for the Lipschitz function \(F_p\). Thus

\[
m^pW_p^p=\int_{-1/2}^{1/2}\int_{-1/2}^{1/2}|t-v|^p\,dt\,dv+O_p(m^{-1})
=\frac{2}{(p+1)(p+2)}+O_p(m^{-1}).
\]

The double integral uses the triangular density \(1-|w|\) of the difference of two independent unit uniforms. Taking positive \(p\)-th roots gives the claimed sharp \(W_p\) asymptotic and the exact leading coefficient.

**4. Comparison with unrestricted \(m\)-atom approximation.** Let \(\nu\) be any probability with \(r\le m\) atoms, with no restriction on positive weights. In the quantile parametrization, the atoms correspond to consecutive intervals of lengths \(\ell_1,\ldots,\ell_r\) summing to one. The least possible \(p\)-cost on an interval of length \(\ell_i\) is attained at its midpoint and equals \(\ell_i^{p+1}/[2^p(p+1)]\). Convexity gives

\[
W_p(\lambda,\nu)^p\ge\frac1{2^p(p+1)}\sum_{i=1}^r\ell_i^{p+1}
\ge\frac1{2^p(p+1)m^p}.
\]

Equal weights and midpoints attain equality. For \(p=\infty\), covering a unit interval by at most \(m\) radius-\(R\) balls forces \(R\ge1/(2m)\), attained by the same midpoints. Dividing steps 2–3 by these sharp optima proves the inefficiency ratios for every finite \(p\) and \(p=\infty\). \(\square\)

## Verification

A standalone pure-Python checker (`verify.py`) builds the \(2^n\) inverse affine branches of \(T^n\) without using the displayed periodic-point formula, solves for their fixed points in exact rational arithmetic, and reconstructs the monotone transport cost directly from cell integrals. It checks the sorted-grid identity, exact \(W_1\), exact \(W_2^2\), exact \(W_\infty\), and maximum nearest-neighbor gap for all \(1\le n\le10\), plus rational third- and fourth-moment convergence bounds. These checks are finite corroboration; the proof above establishes the all-\(n\), all-\(p\) statements.

## Relationship to prior work

Fuhrmann, Gröger and Passeggi (2026) study the rigidity information carried by periodic orbit sets of interval maps, motivating quantitative questions about how much spatial information finite periodic-point collections capture. Their reported results concern topological reconstruction and are distinct from Wasserstein quantization error. Chen and Dong (2010) explicitly state the two rational forms of fixed points of iterated full tent maps and analyze coincidences of orbit barycenters. Their coordinates are **prior art**, not claimed here; the new conclusions concern exact optimal-transport errors, the continuum of sharp limiting \(p\)-dependent penalties, and comparison to unrestricted optimal atomic quantizers. Pollicott (2026) addresses effective intrinsic ergodicity for expanding interval maps, a different quantitative aspect of statistical approximation. No inspected publication was found stating the present transport-cost spectrum. This is a scoped literature comparison, not a certification of global historical priority.

## Limitations

The result is specific to the full-slope tent map and the all-fixed-point counting measure, not to a general tent-map parameter, primitive-period-only measures, or arbitrary interval dynamics. The finite-\(p\) error term is not uniform in \(p\). The recent rigidity paper's complete preprint could not be inspected through accessible mirrors; its abstract and identified theorems concern topological rigidity rather than quantitative transport, but full historical priority remains subject to further examination. The older directly relevant barycenter paper was inspected at full-text level. Independent scientific review has not been performed.

## References

1. G. Fuhrmann, M. Gröger and A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435 (first public submission 2026-10-05), https://arxiv.org/abs/2610.07435.
2. K.-C. Chen and X. Dong, *On the barycenter of the tent map*, Proceedings of the American Mathematical Society **138** (2010), 4025–4035, author-hosted text https://www.math.nthu.edu.tw/~kchen/papers/ChenDongTentCenter.pdf.
3. M. Pollicott, *Effective intrinsic ergodicity for expanding interval maps*, arXiv:2606.12081 (first public submission 2026-06-10), https://arxiv.org/abs/2606.12081.
