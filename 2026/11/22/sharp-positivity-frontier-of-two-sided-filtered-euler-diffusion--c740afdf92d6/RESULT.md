# Sharp positivity frontier of two-sided filtered Euler diffusion on a weighted three-site path

## Finding

Let \(a,b>0\), and let \(L\) be the weighted Laplacian of the three-vertex path with edge conductances \(a\) and \(b\). The matched two-sided filtered Euler heat step of Wu--Shu is
\[
 T_\tau=I-\tau (I+\tau L/2)^{-1}L(I+\tau L/2)^{-1},\qquad \tau\ge0.
\]
Define \(m=\min(a,b)\) and \(M=\max(a,b)\). Every \(T_\tau\) is symmetric, mass conserving and Euclidean nonexpansive, with spectrum in \([1/2,1]\). Its **complete entrywise-positivity classification** is:

- If \(M\le2m\), then \(T_\tau\) has strictly positive entries for every \(\tau>0\).
- If \(M>2m\), then \(T_\tau\) is entrywise nonnegative **if and only if**
\[
 0\le \tau\le\tau_*(a,b):=\frac{2}{\sqrt{m(M-m)}-m}.
\]
At \(\tau=\tau_*\), precisely the two symmetric transitions across the stronger edge vanish. At larger steps they are strictly negative, and all other entries remain positive. No reentry is possible.

Thus the sharp all-steps Markov-positivity boundary is the conductance ratio \(M/m=2\). The phenomenon first becomes possible on three vertices when arbitrary positive edge weights are admitted: the analogous two-vertex weighted path is positive for all steps.

## Assumptions and scope

The graph is a *three-vertex undirected path*, with positive fixed edge conductances \(a\) and \(b\) and symmetric combinatorial Laplacian
\[
 L=\begin{pmatrix}
 a&-a&0\\-a&a+b&-b\\0&-b&b
 \end{pmatrix}.
\]
The diffusion is \(u'=-Lu\), the resolvent splitting is exactly \(S=L\), and the numerical step is the first-order matched *two-sided* filtered formula shown above, in exact arithmetic. Entrywise nonnegativity means preservation of nonnegative input vectors. The time step is any real \(\tau\ge0\); positivity means all matrix entries strictly positive for finite \(\tau>0\). No claim concerns variable splitting, different Runge--Kutta formulas, or arbitrary graphs.

## Proof

Put \(x=\tau/2\) and \(D=1+2(a+b)x+3abx^2\). Since \(x\ge0\) and \(a,b>0\), \(D>0\). Direct inversion of \(I+xL\) and multiplication give the exact off-diagonal entries:
\[
 (T_\tau)_{12}=\frac{2ax\,[1+2bx+b(2b-a)x^2]}{D^2},\qquad
 (T_\tau)_{23}=\frac{2bx\,[1+2ax+a(2a-b)x^2]}{D^2},
\]
\[
 (T_\tau)_{13}=\frac{4abx^2[1+(a+b)x]}{D^2}.
\]
The matrix is symmetric, so these determine all six off-diagonal entries. Because \(L\mathbf 1=0\), also \(T_\tau\mathbf 1=\mathbf1\). For any eigenvalue \(\lambda\ge0\) of \(L\), let \(y=\tau\lambda/2\). The corresponding multiplier is
\[
 f(y)=1-\frac{2y}{(1+y)^2}=\frac{1+y^2}{(1+y)^2}\in[1/2,1].
\]
Indeed, \((1+y)^2\ge4y\). Thus \(T_\tau\succeq I/2\), so each diagonal entry is at least \(1/2\). Consequently entrywise nonnegativity is equivalent to nonnegativity of the two adjacent-edge expressions: the remote-edge entry is positive for every \(x>0\).

The two relevant quadratics are
\[
 q_{12}(x)=1+2bx+b(2b-a)x^2,\qquad q_{23}(x)=1+2ax+a(2a-b)x^2.
\]
If \(a\le2b\) then \(q_{12}(x)>0\) for all finite \(x\ge0\); otherwise \(q_{12}\) is a concave quadratic with exactly one positive zero and is negative at all larger \(x\). Solving its zero explicitly gives
\[
 x_*=\frac{1}{\sqrt{b(a-b)}-b}\qquad (a>2b).
\]
For \(a>2b\), the other polynomial \(q_{23}\) is strictly positive, since \(2a-b>0\). Exchanging \(a,b\) gives the alternative failure mode for \(b>2a\). The inequalities \(a>2b\) and \(b>2a\) are mutually exclusive. Multiplying \(x_*\) by two gives the claimed sharp \(\tau_*\), proves the all-step classification, and excludes positivity reentry. At the threshold the unique offending edge entry is zero, while all remaining entries are strictly positive.

For the two-vertex path with conductance \(c>0\), direct diagonalization gives its only off-diagonal transition \(2cx/(1+2cx)^2>0\) at \(x>0\). This proves the minimal weighted-path size statement. Finally, defining the Crank--Nicolson matrix \(C_\tau=(I-\tau L/2)(I+\tau L/2)^{-1}\), one has the exact equivalent spectral representation
\[
 T_\tau=\tfrac12(I+C_\tau^2).
\]
This identity does not by itself guarantee that \(T_\tau\) is entrywise nonnegative, because \(C_\tau\) need not be entrywise nonnegative.

## Verification

A standalone Python 3 standard-library exact-rational script, `verify.py`, constructs the full resolvent matrix by Gauss--Jordan inversion for an independently coded set of conductance and step values. It verifies the three explicit off-diagonal rational formulas, row sums, symmetry, diagonal lower bounds and sign criteria, for a total of 3,586 successful assertions. As a cross-method check, for \((a,b,\tau)=(3,1,6)\), the present step has \((T_\tau)_{12}=-9/2809\), whereas the **different** two-stage fourth-order Gauss--Legendre heat step has its corresponding entry \(18/1621>0\). Thus the finite-step boundary is specific to the present filter, even though the two methods share an all-step conductance-ratio condition.

The finite tests are reproducibility checks, not proof of the universally quantified result; the displayed rational formulas and sign argument supply that proof.

## Relationship to prior work

Wu and Shu (arXiv:2611.02282, Proposition 3.1, formula (3.5)) introduce the two-sided resolvent method and prove unconditional \(L^2\) stability. This finding studies the separate nonnegative-cone property, restricted to a weighted three-vertex diffusion path. A prior analysis of symmetrically filtered Euler heat steps establishes the all-step positivity property for **unweighted** graphs of at most three vertices and identifies a four-vertex obstruction, as well as a general long-step pseudoinverse obstruction on weighted graphs. Those facts do not provide the exact positive-step interval at unequal weights on three vertices.

Public mathematical records on the fourth-order Gauss--Legendre step establish an all-step weighted-three-path ratio of two. The scalar rational filter differs from the present method, and the explicit \((3,1,6)\) computation above rules out transferring its finite-step positivity horizon to the filtered Euler step. The general Crank--Nicolson identity stated in the proof does not identify the entrywise sign threshold without further analysis.

## Limitations

This is an exact-arithmetic finite-dimensional classification for one fixed matched splitting. It does not establish a maximum principle for general nonlinear or PDE spatial discretizations, robustness under floating-point solves, or all-step positivity on larger weighted graphs. The claimed originality is based on inspected accessible literature and claim-level database comparisons, not proof that no earlier equivalent specialist result exists. In particular, relevant public record summaries were accessible even where the underlying full text could not be inspected. Independent review has not been performed.

## References

1. Yue Wu and Chi-Wang Shu, *Unconditionally \(L^2\)-stable explicit--implicit--null filtered Runge--Kutta methods for general nonlinear degenerate parabolic equations*, arXiv:2611.02282, first version November 1, 2026, Proposition 3.1: https://arxiv.org/abs/2611.02282.
2. *Unconditional fourth-order Gauss positivity on weighted paths: a four-vertex cutoff*, public mathematical record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unconditional-fourth-order-gauss-positivity-on-weighted-paths-a--73910250a06c.
3. *A sharp positivity dichotomy for the fourth-order Gauss step on three-site weighted diffusion networks*, public mathematical record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-positivity-dichotomy-for-the-fourth-order-gauss-step-on--2f0ca4adbadc.
