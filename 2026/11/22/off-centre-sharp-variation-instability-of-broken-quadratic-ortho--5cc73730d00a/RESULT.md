# Off-centre sharp variation instability of broken quadratic orthogonal projection

## Finding
Let \(\{x_j\}_{j\in\mathbb Z}\) be an arbitrary strictly increasing locally finite partition of the real line, with \(x_j\to\pm\infty\) at the corresponding ends. Let \(\Pi_2\) denote the \(L^2(\mathbb R)\)-orthogonal projector onto the **discontinuous**, cellwise degree-at-most-two polynomial space on this partition. Define the variation by the total mass \(\operatorname{TV}(f)=|Df|(\mathbb R)\), including jumps at cell interfaces.

For every real \(f\in BV(\mathbb R)\cap L^2(\mathbb R)\),
\[
\operatorname{TV}(\Pi_2 f)\le K_2\operatorname{TV}(f),
\qquad
K_2=\frac{500s_*^4-1000s_*^3+648s_*^2-148s_*+5}{5(2s_*-1)}
=2.0698386217193\ldots,
\]
where
\[
s_*=\frac12\left(1-\sqrt{\frac{17+2\sqrt{41}}{125}}\right)
=0.2558432942765\ldots.
\]
The constant is the **exact attained** operator seminorm for every such grid, regardless of the cell lengths. A compactly supported interval-indicator input with its two endpoints situated at the fractional locations \(s_*\) inside two distinct cells attains equality. The only optimal single-jump fractional locations are \(s_*\) and \(1-s_*\).

This is a bounded-variation statement for a broken, not continuous, finite-element projection; the output's interelement jumps are part of its variation.

## Assumptions and scope
Every cell \(I_j=(x_j,x_{j+1})\) has positive finite length; cells have no finite accumulation. The broken polynomial space is the direct \(L^2\) sum of local quadratic polynomial spaces. On each cell the projector is defined by the three local moment equations. The input is real-valued, \(L^1\), of finite distributional variation, and square-integrable. No quasi-uniformity or upper bound on the ratios of neighboring cell lengths is required.

The step response is computed using the affine reference cell \([0,1]\). The local projection of \(H_s(t)=\mathbf1_{\{t\ge s\}}\), for \(0\le s\le1\), is
\[
p_s(t)=(1-s)+3s(1-s)(2t-1)
+5s(1-s)(2s-1)(6t^2-6t+1).
\]
Outside the cell containing the jump, the projected step equals the unaltered constants zero and one.

## Proof
**1. Single-jump reduction.** In one dimension, the distributional derivative \(Df\) of \(f\in BV(\mathbb R)\cap L^2\) is a finite signed measure and \(f(-\infty)=0\). Hence, in the locally integrable sense, \(f(t)=\int H_s(t)\,dDf(s)\). Projecting cellwise and differentiating distributionally yields \(D(\Pi_2 f)=\int D(\Pi_2H_s)\,dDf(s)\), justified first for finite jump measures and then by local polynomial moments and bounded convergence. The measure triangle inequality gives
\[
\operatorname{TV}(\Pi_2 f)
\le \left(\sup_{0\le s\le1}F(s)\right)\operatorname{TV}(f),
\qquad
F(s)=|p_s(0)|+\int_0^1|p_s'(t)|\,dt+|1-p_s(1)|.
\]
An affine rescaling of any cell leaves \(F\) invariant. The endpoint terms are the two interelement jumps of the projected Heaviside response.

**2. Exact cell analysis.** The shifted Legendre polynomials \(1\), \(2t-1\), and \(6t^2-6t+1\) are mutually orthogonal, with squared norms \(1\), \(1/3\), and \(1/5\). Their step moments give the displayed \(p_s\). The symmetry \(F(s)=F(1-s)\) reduces maximization to \(0\le s\le1/2\). Write
\[
\alpha=\frac{4-\sqrt6}{10},\qquad
\beta=\frac{6-\sqrt6}{10}.
\]
For \(0\le s\le2/5\), the quadratic is concave and has an interior maximum at \(t_c=(5s-3)/(5(2s-1))\); for \(2/5\le s\le1/2\), it is increasing on the cell. The signs of \(p_s(0)\) and \(1-p_s(1)\) change at \(\alpha\) and \(\beta\), respectively. Direct integration of \(|p_s'|\) gives these four exact branches:
\[
F(s)=\begin{cases}
\dfrac{300s^4-540s^3+288s^2-38s-5}{5(2s-1)},&0\le s\le\alpha,\\[4pt]
\dfrac{500s^4-1000s^3+648s^2-148s+5}{5(2s-1)},&\alpha\le s\le\beta,\\[4pt]
\dfrac{300s^4-660s^3+468s^2-118s+5}{5(2s-1)},&\beta\le s\le2/5,\\[4pt]
12s(1-s)-1,&2/5\le s\le1/2.
\end{cases}
\]
All branch junctions agree by continuity. The first and third branches increase throughout their intervals; the fourth increases to \(F(1/2)=2\). For the central branch,
\[
F'(s)=\frac{6\bigl(500[s(1-s)]^2-216s(1-s)+23\bigr)}{5(2s-1)^2}.
\]
Set \(u=s(1-s)\). Its two critical values are \(u_{\pm}=(54\pm\sqrt{41})/250\); only \(u_-\) is attained in \((\alpha,\beta)\). There is a unique central-branch maximum at \(s=s_*\), with \(s_*(1-s_*)=u_-\). Since \(F(1/4)=331/160>2\) while every outer branch is at most \(2\), this central maximum is global and strict up to reflection.

**3. Attainment and mesh invariance.** Select any two nonadjacent cells and within them locations \(a\) and \(b\) at the same relative coordinate \(s_*\). For \(f=\mathbf1_{(a,b)}\), \(\operatorname{TV}(f)=2\). Its projected left- and right-jump disturbances occur in disjoint cells, and their variation contributions are independent. Consequently \(\operatorname{TV}(\Pi_2f)=2F(s_*)=2K_2\). This proves sharpness on every partition, including arbitrarily graded meshes.

## Verification
The accompanying standalone `CHECKER.py` rederives the three projection moment equations and the branch derivatives symbolically, checks the exact algebraic condition on \(s_*\), and tests sharp interval indicators together with 3,000 random compactly supported piecewise-constant inputs. It reports `ALL_BROKEN_QUADRATIC_BV_CHECKS_PASS` when successful. These finite tests corroborate, but do not replace, the preceding general proof.

## Relationship to prior work
Nochetto and Salgado (arXiv:1211.1069v1, publicly posted November 5, 2012) construct a **different** total-variation-diminishing, continuous multilinear interpolant through local averaging. Their construction supplies motivation for measuring variation stability of polynomial reconstruction, but gives no sharp norm for the local \(L^2\)-orthogonal quadratic projection with interface jumps. Crouzeix and Thomée (1987) address \(L^p\)/\(W^{1,p}\) stability of projections onto continuous finite-element spaces, under different norms and assumptions. Related published results on quadratic Jacobi projection concern global polynomial fits and monotone range escape; such results do not supply the broken-space total-variation norm because they omit intercell jump terms and differ in the operator and domain.

## Limitations
Only one-dimensional real-valued, unweighted distributional total variation and the cellwise \(L^2\) quadratic projector are treated. No statement is made about higher polynomial degrees, continuous finite elements, multidimensional meshes, or DG time-evolution schemes. Independent external verification and historical priority checks beyond the inspected sources have not been performed; additional older discontinuous-Galerkin literature might contain equivalent formulas.

## References
1. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069v1 (November 5, 2012), https://arxiv.org/abs/1211.1069.
2. M. Crouzeix and V. Thomée, *The Stability in \(L_p\) and \(W_p^1\) of the \(L_2\)-Projection onto Finite Element Function Spaces*, Mathematics of Computation 48 (1987), 521–532, DOI 10.2307/2007825.
3. M. Herrmann, R. Herzog, S. Schmidt, J. Vidal-Núñez and G. Wachsmuth, *Discrete Total Variation with Finite Elements and Applications to Imaging*, arXiv:1804.07477 (2018), https://arxiv.org/abs/1804.07477. This later source addresses different discrete variation functionals; full text was not retrieved for this comparison.
