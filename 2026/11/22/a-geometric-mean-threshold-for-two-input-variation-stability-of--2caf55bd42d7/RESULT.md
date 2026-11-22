# A geometric-mean threshold for two-input variation stability of moving weighted isotonic regression

## Finding

Fix three positive observation weights \(a,b,c\). At each vertex of a finite cycle, fit a nondecreasing triple by weighted least squares and return its **middle fitted coordinate**. For every cycle length \(n\ge8\), the sharp global two-input Lipschitz constant in cyclic adjacent total variation is

\[
\boxed{K(a,b,c)=\max\left\{1,\;2\left(\frac{a}{a+b}+\frac{c}{b+c}\right)-1\right\}.}
\]

It is attained by two distinct finite real input vectors for every positive weight triple. Consequently the filter is nonexpansive in variation between any two inputs **if and only if** \(b^2\ge ac\). In the amplification phase \(ac>b^2\), its exact gain is

\[
K(a,b,c)=1+\frac{2(ac-b^2)}{(a+b)(b+c)}>1.
\]

This is a *two-input* statement: it controls the variation of the difference between two filtered signals, not merely the variation of one filtered signal.

## Assumptions and scope

Let \(n\ge8\), and use cyclic indices \(i\in\mathbb Z/n\mathbb Z\). Define

\[
V_n(z)=\sum_{i=0}^{n-1}|z_{i+1}-z_i|.
\]

For a real input \(x=(x_i)_{i=0}^{n-1}\), at each position \(i\), let \((u_-,u_0,u_+)\) be the unique minimizer of

\[
a(u_--x_{i-1})^2+b(u_0-x_i)^2+c(u_+-x_{i+1})^2
\]

subject to \(u_-\le u_0\le u_+\). Define \((T_{a,b,c}x)_i=u_0\). The weights are fixed by **position within each window**, not by absolute vertex; no globally ordered fit on the cycle is assumed. Set

\[
\operatorname{Lip}_{V_n}(T)=\sup_{V_n(x-y)>0}\frac{V_n(Tx-Ty)}{V_n(x-y)}.
\]

The theorem asserts \(\operatorname{Lip}_{V_n}(T_{a,b,c})=K(a,b,c)\). The upper inequality also holds when \(n<8\), but sharpness at those smaller sizes is not asserted.

## Proof

**1. Exact local branches.** Weighted pool-adjacent-violators regression on three sites has just four possible middle-coordinate formulas, according to the active pooling blocks: the untouched center \(x_i\); the weighted mean of the left pair; the weighted mean of the right pair; or the weighted mean of all three. More explicitly, for a triple \((r,s,t)\):

- if \(r\le s\le t\), the output is \(s\);
- if \(r>s\) and \((ar+bs)/(a+b)\le t\), it is \((ar+bs)/(a+b)\);
- if \(s>t\) and \(r\le(bs+ct)/(b+c)\), it is \((bs+ct)/(b+c)\);
- otherwise it is \((ar+bs+ct)/(a+b+c)\).

These exhaust the weighted isotonic partitions and coincide on their common boundaries. Hence \(T\) is globally continuous and piecewise affine. On each full-dimensional differentiability chamber its Jacobian \(A\) has the form

\[
(Ah)_i=\alpha_i h_{i-1}+(1-\alpha_i-\gamma_i)h_i+\gamma_i h_{i+1},
\]

where \(0\le\alpha_i\le A_*=a/(a+b)\), \(0\le\gamma_i\le C_*=c/(b+c)\), and \(\alpha_i+\gamma_i\le1\). In the four branches, \((\alpha_i,\gamma_i)\) is respectively \((0,0)\), \((A_*,0)\), \((0,C_*)\), or \((a/(a+b+c),c/(a+b+c))\). The latter entries respect the bounds because all weights are positive.

**2. Sharp uniform upper bound for every Jacobian.** Write \(d_i=h_{i+1}-h_i\). Direct subtraction of consecutive Jacobian rows gives

\[
(Ah)_{i+1}-(Ah)_i
=\alpha_i d_{i-1}+(1-\gamma_i-\alpha_{i+1})d_i+\gamma_{i+1}d_{i+1}.
\]

For a fixed input-edge coordinate \(d_j\), the total absolute coefficient across all output edges is

\[
\gamma_j+|1-\gamma_j-\alpha_{j+1}|+\alpha_{j+1}
=\max\{1,\,2(\gamma_j+\alpha_{j+1})-1\}
\le K(a,b,c).
\]

The triangle inequality, followed by summation over input-edge coordinates, therefore yields \(V_n(Ah)\le K(a,b,c)V_n(h)\). Integrate the piecewise-constant Jacobians along the straight segment from \(y\) to \(x\); continuity of \(T\), finitely many polyhedral chambers and the seminorm triangle inequality give

\[
V_n(Tx-Ty)\le K(a,b,c)V_n(x-y)
\]

for all inputs (including boundaries, by continuity).

**3. Exact finite-pair attainment.** Let \(n\ge8\). Set \(x_i=0\) at even \(i<8\), \(x_i=1\) at odd \(i<8\), and \(x_i=0\) at every remaining position \(i\ge8\). Let \(h_i=1\) for \(2\le i\le5\) and zero otherwise, and take \(y=x+\varepsilon h\) with sufficiently small \(\varepsilon>0\). Along the strictly downward base edges \(1\to2\) and \(5\to6\), the local center at vertices \(1,5\) pools with its right neighbor and the center at vertices \(2,6\) pools with its left neighbor. Thus \(\gamma_1=\gamma_5=C_*\), \(\alpha_2=\alpha_6=A_*\) throughout the small perturbation. The edge differences of \(h\) are \(d_1=1\), \(d_5=-1\), and zero elsewhere; the corresponding output-edge packets have disjoint supports \(\{0,1,2\}\) and \(\{4,5,6\}\). Every packet has absolute sum \(\max\{1,2(A_*+C_*)-1\}=K(a,b,c)\). Therefore

\[
V_n(Ty-Tx)=2\varepsilon K(a,b,c),\qquad V_n(y-x)=2\varepsilon.
\]

This proves the global sharpness **with finite pairs**, in both parameter phases. Finally,

\[
\frac{a}{a+b}+\frac{c}{b+c}-1
=\frac{ac-b^2}{(a+b)(b+c)},
\]

which establishes the geometric-mean threshold.

## Verification

Run \(\texttt{python3 check_weighted_local_isotonic.py}\) in the directory containing the standalone checker. The checker uses only the Python standard library and exact rational arithmetic; it checks the four branch formulas, 5,000 random pairs over four lengths and variable positive rational weights, and 30 finite attaining pairs including critical and unstable weights. Output:

```text
EXACT_PAV_BRANCH_CHECKS_PASS 4
EXACT_TWO_INPUT_VARIATION_INEQUALITIES_PASS 5000
EXACT_FINITE_PAIR_SHARPNESS_PASS 30
ALL_WEIGHTED_LOCAL_ISOTONIC_CHECKS_PASS
```

Finite tests are corroboration only. The universal bound, weight threshold and attainment follow from the analytic argument above.

## Relationship to prior work

Classical weighted isotonic regression and its pooling formula are described by Kearsley (2006); the present operator instead fits overlapping three-site windows and retains only their middle coordinate. Harten's and Tadmor's TVD frameworks supply methods for establishing stability of local schemes, while Dubois (2010, originally researched in 1990) treats total-variation-diminishing nonlinear interpolation in conservation-law algorithms. Those works provide conceptual and technical antecedents, including incremental-form estimates, but their inspected statements do not specify the exact two-input variation gain of this weighted local isotonic filter or the attained threshold \(b^2=ac\). The proof uses a derivative-level variation estimate, which is distinct from a one-input TVD estimate.

## Limitations

The theorem concerns real signals on finite cycles of length at least eight, positive stationary within-window least-squares weights, and three-point nondecreasing local fits. It does not determine smaller-cycle sharp constants, extend to arbitrary window widths or graph geometries, or claim historical-priority certification. The sharpness construction is not a classification of all equality cases.

## References

1. A. J. Kearsley, *Projections Onto Order Simplexes and Isotonic Regression*, J. Res. Natl. Inst. Stand. Technol. **111** (2006), 121–125. https://doi.org/10.6028/jres.111.011 (published March–April 2006; NIST public listing March 31, 2006).
2. F. Dubois, *Nonlinear Interpolation and Total Variation Diminishing Schemes*, arXiv:1006.3921 (posted June 20, 2010; archival original dated June 1990). https://arxiv.org/abs/1006.3921.
3. E. Tadmor, *Convenient Total Variation Diminishing Conditions for Nonlinear Difference Schemes*, SIAM J. Numer. Anal. **25** (1988), 1002–1014. https://doi.org/10.1137/0725057.
4. A. Harten, *High Resolution Schemes for Hyperbolic Conservation Laws*, J. Comput. Phys. **49** (1983), 357–393. https://doi.org/10.1016/0021-9991(83)90136-5.
