# The largest spoke controls fourth-order Gauss positivity on every weighted star

## Finding

Let a star have hub \(0\), \(m\ge2\) leaves, and arbitrarily chosen positive spoke conductances \(w_1,\ldots,w_m\). For the weighted combinatorial Laplacian \(L\), the completed two-stage, fourth-order Gauss--Legendre update is
\[
T(h)=R(hL),\qquad R(s)=\frac{s^2-6s+12}{s^2+6s+12},\qquad h\ge0.
\]
Write \(w_*=\max_i w_i\) and
\[
\Delta=\sum_{j:w_j<w_*}\left(\frac{w_*}{w_j}-1\right).
\]
The positivity-preserving step set is exactly \([0,H]\), where
\[
H=\begin{cases}
+\infty,&\Delta\le1,\\
\text{the unique positive root of }\displaystyle\sum_{j:w_j<w_*}
\left(\frac{w_*}{w_j}-1\right)\frac{(h w_j)^2}{(h w_j)^2+6h w_j+12}=1,&\Delta>1.
\end{cases}
\]
Consequently, all-step positivity is equivalent to the single inequality
\[
\boxed{w_*\sum_{j=1}^m\frac1{w_j}\le m+1.}
\]
At every \(0<h<H\), all entries are strictly positive. If \(H<\infty\), exactly the entries connecting the hub to maximum-weight leaves first vanish at \(H\), and those entries are negative for \(h>H\). Thus disconnected positivity windows cannot occur for this method on a positive weighted star. The all-step criterion is also equivalent to \(L^+\) having nonpositive off-diagonal entries (the group inverse is a graph Laplacian).

## Assumptions and scope

The graph is a finite undirected star \(K_{1,m}\), with \(m\ge2\) and all \(w_j\in(0,\infty)\), with no normalization on their sum. The hub is index \(0\), leaves are \(1,\ldots,m\); \(L_{00}=\sum_j w_j\), \(L_{0j}=L_{j0}=-w_j\), \(L_{jj}=w_j\), and all other entries vanish. The time step \(h\) is real and nonnegative. Entrywise positivity is a property of the *completed endpoint map*, not of its internal stages. All finite statements include tied weights, threshold equality, and zero step.

## Proof

**1. Resolvent algebra.** At \(h>0\) put \(z_j=hw_j\), \(d_j=z_j^2+6z_j+12\), \(k=3+i\sqrt3\), and
\[
U=1+\sum_j\frac{z_j^2}{d_j},\qquad V=\sum_j\frac{z_j}{d_j},\qquad E=1+\sum_j\frac{z_j}{k+z_j}.
\]
Here \(U>0\), \(V>0\), and \(E=(U+3V)-i\sqrt3V\), so \(E\ne0\). The Laplacian's hub--leaf block form gives the exact Schur-complement resolvent identities for \(G=(hL+kI)^{-1}\):
\[
G_{00}=\frac1{kE},\quad
G_{0j}=\frac{z_j}{k(k+z_j)E},\quad
G_{ij}=\frac{z_i z_j}{k(k+z_i)(k+z_j)E}\quad(i\ne j\ge1).
\]
The scalar partial fraction
\[
\frac{s}{s^2+6s+12}
=\frac{k}{k-\bar k}\frac1{s+k}
 +\frac{\bar k}{\bar k-k}\frac1{s+\bar k}
\]
and \(R(s)=1-12s/(s^2+6s+12)\) imply, by taking imaginary parts, that all off-diagonal entries of \(T(h)\) have these exact rational forms:
\[
T_{0j}(h)=\frac{12z_j B_j}{|W_j|^2},\quad
B_j=U-z_jV,\quad W_j=(k+z_j)E,
\]
\[
T_{ij}(h)=\frac{12z_i z_j B_{ij}}{|W_{ij}|^2},\quad
B_{ij}=(z_i+z_j+6)U+(12-z_i z_j)V,\quad
W_{ij}=(k+z_i)(k+z_j)E\quad(i\ne j\ge1).
\]
The denominators are positive, and the expressions remain valid with repeated conductances. The formulas follow also by multiplying \(E\) and the \(k+z_j\) factors into real and imaginary parts. They can be checked exactly against the original rational matrix update with the accompanying verifier.

**2. Only a maximum spoke controls the sign.** Let \(z_*=h w_*\). Because \(V>0\), \(B_j=U-z_jV\ge U-z_*V=:B_*\). If \(B_*\ge0\), all hub--leaf entries are nonnegative. For any leaf pair \(i\ne j\), since \(z_i,z_j\le z_*\),
\[
B_{ij}\ge (z_i+z_j+6)U-z_i z_j\frac{U}{z_*}+12V
\ge(\max\{z_i,z_j\}+6)U+12V>0.
\]
Thus leaf--leaf entries are strictly positive whenever \(B_*\ge0\). Conversely, if \(B_*<0\), at least one hub--maximum-leaf entry is negative, since \(z_*>0\). All diagonal entries are strictly positive for every \(h>0\): \(L\) is symmetric positive semidefinite and \(R(s)>0\) for every real \(s\ge0\), because its numerator is \((s-3)^2+3\). The row sums of \(T(h)\) equal one because \(R(0)=1\). Consequently, entrywise nonnegativity for positive steps is equivalent to \(B_*\ge0\).

**3. Unique horizon and boundary cases.** Using \(z_j=hw_j\), and observing that the summand for a maximum weight is zero,
\[
B_*(h)=1-\sum_{j:w_j<w_*}\left(\frac{w_*}{w_j}-1\right)\psi(hw_j),\qquad
\psi(x)=\frac{x^2}{x^2+6x+12}.
\]
For \(x>0\), \(0<\psi(x)<1\), and \(\psi\) is strictly increasing, since \(\psi'(x)=6x(x+4)/(x^2+6x+12)^2>0\). Therefore \(B_*(h)\) is nonincreasing from \(1\) to \(1-\Delta\), and strictly decreasing whenever not all weights are equal. If \(\Delta\le1\), \(B_*(h)>0\) for all finite \(h>0\). If \(\Delta>1\), continuity and strict monotonicity give exactly one finite zero \(H\), with a strict sign change. At this zero, the hub entries vanish exactly on spokes whose weights equal \(w_*\); all other off-diagonal and all diagonal entries stay positive by the displayed strict inequalities. At \(h=0\) the update equals \(I\).

Finally, \(\Delta=\sum_j(w_*/w_j-1)=w_*\sum_j1/w_j-m\), proving the boxed all-step criterion.

**4. Pseudoinverse equivalence.** Let \(N=m+1\), \(r_j=1/w_j\), and \(S=\sum_jr_j\). The effective resistances of a star are \(R_{0j}=r_j\) and \(R_{ij}=r_i+r_j\). Double centering of the resistance matrix yields
\[
(L^+)_{0j}=\frac{S-Nr_j}{N^2},\qquad
(L^+)_{ij}=\frac{S-N(r_i+r_j)}{N^2}\quad(i\ne j\ge1).
\]
All off-diagonal entries of \(L^+\) are nonpositive if and only if every \(Nr_j\ge S\), which reduces to \(w_* S\le N\). Indeed the hub--leaf inequalities imply the leaf--leaf inequalities, proving equivalence. Consistently, on the nonconstant eigenspaces \(R(hL)=I-(12/h)L^++O(h^{-2})\), so the sign obstruction is visible at large steps.

## Verification

The accompanying `verify_star_gauss.py` computes the full rational matrix directly from the weighted Laplacian and independently from the displayed hub--leaf and leaf--leaf formulas. The executable performs exact-rational matrix identities, positivity and mass checks across different positive weights and step sizes, and checks that the general criterion reduces to the exact two-valued-spoke interval. Run from a directory containing the script with `python verify_star_gauss.py` (requires Python 3 and SymPy). Its completed replay returned `VERIFY_OK 1537`. These finite tests do not establish the for-all quantifiers; the preceding algebraic sign proof does.

## Relationship to prior work

General SSP and RK positivity theory provides broad method-dependent step-size conditions. Ketcheson, Gottlieb and Macdonald [1] study such stability constraints, while Blanes, Iserles and Macnamara [2] explain why positivity, unlike linear stability, is a separate constraint in Laplacian-structured dynamics. Horváth's earlier works [3,4] study general Runge--Kutta positivity thresholds, though their full manuscripts were not accessible in this examination; no absence-of-coverage claim is based on those abstracts alone.

A prior exact **one-exceptional-spoke** classification for the same fourth-order method gave \(1/2\le t\le m/(m-1)\) when the weights are \((a,\ldots,a,at)\) and \(m\ge4\). That classification is not repeated as new: the present arbitrary-positive-weight theorem subsumes it and newly classifies all failure horizons, ties, and independent multi-spoke heterogeneity. A separate published eight-state example concerns nonreversible pure-birth chains, not positive symmetric star Laplacians [5]. The condition is a graph-specific property of the endpoint update and does not assert unconditional SSP for general ODEs or other graphs.

## Limitations

The theorem is limited to symmetric weighted stars, this precise two-stage Gauss--Legendre *endpoint* map and positive edge weights. It does not guarantee internal-stage positivity, positivity for nonlinear dynamics, or positivity on arbitrary graphs. A fully independent publication-priority audit has not been performed. In particular, older RK positivity literature [3,4], accessible only in bibliographic/abstract form, could contain a general theorem implying part of this classification; that risk is recorded rather than presented as a cleared comparison.

## References

[1] D. I. Ketcheson, S. Gottlieb, C. B. Macdonald, *Strong stability preserving two-step Runge–Kutta methods*, arXiv:1106.3626, initially public 2011-06-18, https://arxiv.org/abs/1106.3626 .

[2] S. Blanes, A. Iserles, S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242, initially public 2021-02-16, https://arxiv.org/html/2102.08242v2 .

[3] Z. Horváth, *Positivity of Runge-Kutta and diagonally split Runge-Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, DOI:10.1016/S0168-9274(98)00050-6.

[4] Z. Horváth, *On the positivity step size threshold of Runge-Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, DOI:10.1016/j.apnum.2004.08.026.

[5] *Eight-state barrier for Markov positivity of the [2/2] Padé map*, published mathematical record 2026/9/20, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
