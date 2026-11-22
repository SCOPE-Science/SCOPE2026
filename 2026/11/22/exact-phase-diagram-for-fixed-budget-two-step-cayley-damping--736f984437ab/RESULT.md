# Exact phase diagram for fixed-budget two-step Cayley damping

## Finding

Let \(a>0\), \(b\geq0\), and \(H>0\). Apply two successive implicit-midpoint steps, of respective lengths \(tH\) and \((1-t)H\), to the constant-coefficient planar equation \(y'=Ay\), where
\[
A=\begin{pmatrix}-a&-b\\ b&-a\end{pmatrix},\qquad 0\leq t\leq1.
\]
The optimal split minimizes the squared Euclidean amplification \(\|y_{\rm out}\|^2/\|y_{\rm in}\|^2\), which is independent of nonzero initial data. Put
\[
r=\sqrt{a^2+b^2},\quad \sigma=\frac b r,\quad R=\frac{r^2H^2}{4},\quad
q_*=\min\!\left\{\frac14,\max\!\left\{0,\frac{\sqrt{R+4\sigma^2}-1}{R}\right\}\right\}.
\]
**Every** minimizing split is characterized by \(t(1-t)=q_*\); therefore, the optimal *unordered* pair of substep lengths is unique. Equivalently, the shorter fraction is \((1-\sqrt{1-4q_*})/2\).

There is a complete sharp phase diagram. If \(0\leq\sigma<1/2\), zero-length, unequal-positive, equal, and unequal-positive optimal splits occur in that order as \(R\) increases, separated respectively by
\[
R=1-4\sigma^2,\qquad R=4-8\sigma,\qquad R=4+8\sigma.
\]
Precisely, a zero substep is optimal for \(0<R\leq1-4\sigma^2\); two distinct positive substeps are optimal for \(1-4\sigma^2<R<4-8\sigma\); equal substeps are optimal for \(4-8\sigma\leq R\leq4+8\sigma\); and two distinct positive substeps are optimal for \(R>4+8\sigma\). When \(\sigma=0\), the equal-split interval degenerates to the point \(R=4\). If \(1/2\leq\sigma<1\), equal substeps are optimal exactly for \(0<R\leq4+8\sigma\), and unequal positive substeps are optimal above that interval. The frequency/damping boundary is \(b=a/\sqrt3\).

For \(b>0\), as \(H\to\infty\), the shorter optimal physical substep tends to \(2/r\), and the optimal squared amplification tends to
\[
\frac{r-a}{r+a}<1.
\]
By contrast, the equal split has squared amplification tending to \(1\). For pure real decay \(b=0\), the optimized two-step multiplier is exactly zero at every \(H\geq 2/a\).

## Assumptions and scope

The matrix is the *normal* damped planar oscillator displayed above, the coefficients are constant, and the same classical implicit-midpoint rule is used for both steps. The time budget \(H\) and number of (at most two nontrivial) midpoint solves are fixed. Zero substeps are allowed in the closed admissible class. If both lengths are required to be strictly positive, the zero-substep phase has the stated optimal **infimum**, but no minimizing positive split. The objective is amplitude damping of the numerical propagation, **not** local truncation error, physical-time accuracy, or computational speed.

## Proof

Identify the plane with the complex line. For \(z=(-a+ib)H/2\) and \(q=t(1-t)\), composition of the two Cayley factors yields
\[
G(q)=\frac{(1+tz)(1+(1-t)z)}{(1-tz)(1-(1-t)z)}
=\frac{1+z+qz^2}{1-z+qz^2}.
\]
The denominators are nonzero because \(a>0\). Set \(c=a/r>0\), \(\sigma=b/r\), and \(R=|z|^2>0\). Direct complex multiplication gives
\[
|1+z+qz^2|^2=B-T,\quad |1-z+qz^2|^2=B+T,
\]
where
\[
B=(1+qR)^2+R-4\sigma^2 qR,
\qquad T=2c\sqrt R(1+qR)>0.
\]
Thus the squared amplification is \(F(q)=(B-T)/(B+T)\). Substituting \(w=1+qR\), with \(1\leq w\leq1+R/4\), gives
\[
F=\frac{U(w)-2c\sqrt R}{U(w)+2c\sqrt R},\qquad
U(w)=w+\frac{R+4\sigma^2}{w}-4\sigma^2.
\]
Because the second expression is strictly increasing in \(U\) (with positive denominator), minimizing \(F\) is equivalent to minimizing \(U\). Now
\[
U'(w)=1-\frac{R+4\sigma^2}{w^2},\qquad
U''(w)=\frac{2(R+4\sigma^2)}{w^3}>0.
\]
Consequently, the unique minimizing \(w\) is the projection of \(\sqrt{R+4\sigma^2}\) onto \([1,1+R/4]\). Translating to \(q=(w-1)/R\) proves the formula and uniqueness up to interchanging the two lengths.

The lower endpoint is active exactly when \(R+4\sigma^2\leq1\). The upper endpoint is active exactly when
\[
\sqrt{R+4\sigma^2}\geq1+\frac R4
\quad\Longleftrightarrow\quad (R-4)^2\leq64\sigma^2.
\]
These inequalities give the stated phase diagram. For \(0\leq\sigma<1/2\), the intervals are consistently ordered because
\(1-4\sigma^2\leq4-8\sigma\), with strict inequality for \(\sigma<1/2\). For \(\sigma\geq1/2\), the zero-substep phase is empty and \(4-8\sigma\leq0\). The frequency condition \(\sigma=1/2\) is equivalent to \(b=a/\sqrt3\).

For fixed \(a,b\), at large \(H\), the unconstrained minimizing point is interior and
\[
q_*=\frac{\sqrt{R+4\sigma^2}-1}{R}=R^{-1/2}+O(R^{-1}).
\]
The shorter fraction equals \(q_*+O(q_*^2)\), hence its physical duration tends to \(H/\sqrt R=2/r\). The longer midpoint step tends to infinite length and its Cayley factor tends to \(-1\); the shorter factor has squared modulus \((r-a)/(r+a)\), proving the limit. For \(b=0\), whenever \(H\geq2/a\) one can take a substep of length \(2/a\), making its midpoint numerator zero. The strict convexity already proves the equality cases.

## Verification

The standalone program `verifier.py`, run with Python and SymPy, independently expands the complex Cayley numerator and denominator, checks the strict-convexity reduction and both boundary identities, and compares 1,200 parameter draws against 81 direct complex-amplification values each (97,200 supplementary comparisons). It also tests the phase boundaries, stiff limit, and exact extinction on real decay. Run `python verifier.py` from the extracted package directory. The recorded successful output is included in `verifier_output.txt`. Finite test grids are **not** used as the global proof; that role belongs to the exact convexity argument above.

For the concrete oscillator \(a=b=1\) and \(H=10\), the shorter optimal fraction is approximately \(0.145348129877\), with squared amplification \(0.108027069187\); the equal split gives \(0.211102994887\), and a single full-length midpoint step gives \(0.672131147541\).

## Relationship to prior work

Variable-step and composite implicit integrators are an established subject. Layton, Pei, Qin and Trenchea study stability of the distinct variable-step Dahlquist–Liniger–Nevanlinna method. Zhang, Zhang, Xing and Masarati optimize a broader composite family with trapezoidal substeps and a **general last substep**, emphasizing order, stability and controllable numerical dissipation. Their special all-trapezoidal case does not provide the sharp *fixed-total-duration*, two-identical-Cayley-substep minimization over every split and complex damped mode proved here. Zhang, Zhang and Masarati analyze equivalent multistep/single-step integrators, likewise with different tunable schemes and objectives. A separate earlier optimal-stability result by Dharmaraja, Wang and Strang uses a trapezoidal–BDF split, not two consecutive trapezoidal steps. This distinction does not establish publication priority or exclude every unindexed equivalent treatment.

## Limitations

The theorem is about a single normal spectral pair; it neither solves joint minimax allocation across an arbitrary spectrum nor addresses nonnormal transient norm amplification. The stiff-limit result is a damping observation, **not** an \(L\)-stability assertion for one fixed, budget-independent multistep method. Strong numerical damping at a very large time budget may sacrifice accuracy. The optimized split depends on the model parameters \(a,b\); no estimator or adaptive implementation is claimed. External independent verification and a comprehensive historical-priority audit have not been performed.

## References

1. W. Layton, W. Pei, Y. Qin, C. Trenchea, *Analysis of the variable step method of Dahlquist, Liniger and Nevanlinna for fluid flow*, first publicly posted 2020-01-23, https://arxiv.org/abs/2001.08640 .
2. H. Zhang, R. Zhang, Y. Xing, P. Masarati, *On the optimization of n-sub-step composite time integration methods*, publicly published 2020-10-24, https://doi.org/10.1007/s11071-020-06020-8 .
3. H. Zhang, R. Zhang, P. Masarati, *Improved second-order unconditionally stable schemes of linear multi-step and equivalent single-step integration methods*, publicly published 2020-12-07, https://doi.org/10.1007/s00466-020-01933-y .
4. S. Dharmaraja, Y. Wang, G. Strang, *Optimal stability for trapezoidal–backward difference split-steps*, 2009, https://dspace.mit.edu/entities/publication/2469bf38-ce9a-4cb3-a510-f9d3edf0cfcf .
