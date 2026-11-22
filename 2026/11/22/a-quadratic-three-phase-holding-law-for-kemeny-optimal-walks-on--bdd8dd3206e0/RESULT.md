# A quadratic three-phase holding law for Kemeny-optimal walks on three-generation two-bough trees

## Finding
Let \(m,\ell\) be integers at least \(2\). Form a rooted tree with two children of the root, \(m\) children of each of those two vertices, and \(\ell\) terminal leaves from each of the \(2m\) remaining internal vertices. Among **all** symmetric, nonnegative, irreducible stochastic transition matrices supported on this tree (holding allowed), there is exactly one minimizer of the inverse spectral Kemeny sum
\[
\mathcal K(P)=\sum_{j=2}^{N}\frac{1}{1-\lambda_j(P)},\qquad N=3+2m+2m\ell.
\]
Its holding probabilities at the root and at the two depth-one vertices undergo precisely three phases. For \(m\ge3\):

- If \(2\le\ell\le4m^2-8m+5\), only the root among nonterminal vertices holds with positive probability.
- If \(4m^2-8m+6\le\ell\le4m^2-6m+4\), no nonterminal vertex holds.
- If \(\ell\ge4m^2-6m+5\), exactly the two depth-one vertices among nonterminal vertices hold with positive probability.

For \(m=2\), these three ranges are respectively \(2\le\ell\le5\), \(6\le\ell\le7\), and \(\ell\ge8\). Every terminal leaf has positive holding probability in every case. The all-zero-interior-holding phase lasts for exactly \(2m-1\) consecutive integer values of \(\ell\) when \(m\ge3\). Both transition boundaries satisfy \(\ell/m^2\to4\), while their separation has order \(m\).

All three optimal edge probabilities are explicit or determined by a single strictly monotone scalar equation, as given below. These support claims apply to the unrestricted edge-by-edge optimization, not just to a symmetry-constrained subfamily.

## Assumptions and scope
Let \(x\) denote the common root-to-depth-one probability, \(y\) the depth-one-to-depth-two probability, and \(z\) the depth-two-to-leaf probability. Define
\[
s=1+m(1+\ell),\quad A=2s(s+1),\quad B=2m(1+\ell)(2s-\ell),\quad C=4m\ell s.
\]
The four types of diagonal holding probabilities are \(1-2x\), \(1-x-my\), \(1-y-\ell z\), and \(1-z\). No extra edge between distinct vertices is permitted. We permit zero holding probability and exclude zero transition probability across a tree edge, because the latter disconnects the chain and gives infinite objective.

Set \(y_0=1/(2m)\) and \(T=B-C\ell/(2m-1)^2\). The **exact optimizer** is:

1. If \(T>A/m\), let \(y\) be the unique root in \((y_0,1/m)\) of
\[
\frac{Am}{(1-my)^2}-\frac{B}{y^2}+\frac{C\ell}{(1-y)^2}=0,
\]
then \(x=1-my\) and \(z=(1-y)/\ell\). This is the positive-root-holding phase.
2. If \(0\le T\le A/m\), take \(x=1/2\), \(y=y_0\), and \(z=(1-y_0)/\ell\). Every nonterminal holding probability is zero.
3. If \(T<0\), take
\[
x=\frac12,\qquad y=\frac{\sqrt B}{\sqrt B+\sqrt{C\ell}},\qquad z=\frac{1-y}{\ell}.
\]
This is the positive-depth-one-holding phase.

In every case the minimum value is exactly
\[
\boxed{\mathcal K_* =\frac1N\left(\frac A x+\frac B y+\frac C z\right).}
\]
At an equality boundary in the scalar inequalities, the kink optimizer in item 2 applies; the integer classification above specifies all integer parameters.

## Proof
**1. Strict convexity and unrestricted symmetry.** Write \(L=I-P\), \(J=\boldsymbol1\boldsymbol1^\top/N\). On the connected domain \(L+J\) is positive definite, and \(\mathcal K(P)=\operatorname{tr}((L+J)^{-1})-1\). For a nonzero symmetric perturbation \(H\), the second directional derivative of inverse trace is
\[
2\operatorname{tr}((L+J)^{-1}H(L+J)^{-1}H(L+J)^{-1})>0.
\]
This is strictly positive by spectral diagonalization of the positive definite matrix. Different edge probabilities yield different off-diagonal entries of \(L\), so the objective is strictly convex in the edge weights. The feasible closure is compact, and every boundary point with a vanished tree edge has a zero extra Laplacian eigenvalue and infinite inverse-spectral cost. Consequently the minimizer exists, uses every edge, and is unique. The tree automorphism group permutes the two main boughs, the \(m\) depth-two branches and the \(\ell\) leaves within each branch. Uniqueness forces equality on each edge orbit, proving that \(x,y,z\) are unrestricted global optimal edge probabilities.

**2. Weighted-tree identity.** For a weighted tree, cutting an edge with transition weight \(w\) separates component orders \(a\) and \(N-a\). Its contribution to the Kirchhoff index \(\sum_{u<v}R_{uv}\) is \(a(N-a)/w\). The Kirchhoff index equals \(N\operatorname{tr}(L^+)\). The three orbit sums have coefficients \(A,B,C\) above, giving
\[
N\mathcal K(P)=A/x+B/y+C/z.
\]
Strict decrease in each individual positive weight, subject to feasibility, forces \(z=(1-y)/\ell\), and for each fixed \(y\) forces \(x=\min\{1/2,1-my\}\). Thus \(0<y<1/m\) and the problem reduces to one strictly convex function
\[
f(y)=\frac{A}{\min\{1/2,1-my\}}+\frac B y+\frac{C\ell}{1-y},
\]
with its only kink at \(y_0\). The left derivative at that kink is \(4m^2(-T)\), and the right derivative is \(4m^2(-T+A/m)\). Strict convexity gives the three scalar optimizer cases in the preceding section. If the right derivative is negative there is one root in \((y_0,1/m)\), because the right derivative strictly increases to infinity. If the left derivative is positive, the stationary point to the left is the displayed square-root expression. The optimal root and depth-one holding probabilities cannot both be positive; depth-two holding is always zero and leaf holding is always positive.

**3. Exact integer phase cutoffs.** Define two sign polynomials
\[
G_0=m(2m-1)^2\left(\frac{C\ell}{(2m-1)^2}-B\right),\quad
G_1=m(2m-1)^2\left(\frac{C\ell}{(2m-1)^2}+\frac A m-B\right).
\]
After expansion as polynomials in \(\ell\), their coefficients in descending order are respectively
\[
\begin{split}
G_0:&\quad 4m^3,\; -2m^2(8m^3-12m^2+4m-3),\\
&-2m^2(2m-1)^2(4m+1),\; -4m^2(m+1)(2m-1)^2;\\
G_1:&\quad4m^3,\;-8m^2(2m^3-4m^2+2m-1),\\
&-2m(m-1)(2m-1)^2(4m+3),\;-2(m+1)(2m-1)^2(2m^2-m-2).
\end{split}
\]
For every integer \(m\ge2\), each polynomial has the coefficient signs \((+,-,-,-)\). Descartes' rule of signs, together with its negative constant and positive leading coefficient, shows exactly one positive root of each, with strictly negative values before it and positive values after it. When \(m\ge3\), direct polynomial expansion gives the strict bracketing signs
\[
\begin{array}{l}
G_1(m,4m^2-8m+5)<0<G_1(m,4m^2-8m+6),\\
G_0(m,4m^2-6m+4)<0<G_0(m,4m^2-6m+5).
\end{array}
\]
For complete reproducibility, in descending powers of \(h=m-3\), the coefficient lists of these four expressions, in the order displayed, are
\[
\begin{split}
&(-64,-1056,-7472,-29432,-69776,-99616,-79276,-27080),\\
&(32,464,2864,9684,18998,20594,9712),\\
&(-32,-368,-1672,-3732,-4032,-1620),\\
&(64,1152,8944,38968,103260,166996,153204,61812).
\end{split}
\]
Each list is uniformly signed, proving the bracketing inequalities for all \(h\ge0\), not merely sampled integers. When \(m=2\), direct substitution yields \(G_1(2,5)<0<G_1(2,6)\) and \(G_0(2,7)<0<G_0(2,8)\). Since \(G_1\) has the sign of the right derivative and \(G_0\) has the sign of the left derivative, the claimed integer phase partition follows. Subtracting the two cutoff expressions gives exactly \(2m-1\) consecutive kink-phase values, and dividing by \(m^2\) proves both quadratic boundary laws.

## Verification
Run `python VERIFY.py` with Python, SymPy and NumPy installed. The script reconstructs both symbolic cubic polynomials, verifies the universal signed \(h=m-3\) coefficient certificates, checks all adjacent phase boundaries and recomputes direct eigenvalue sums on representative weighted trees. It also checks a legal edge-asymmetric feasible perturbation. Its finite diagnostics are supplemental to the displayed infinite-parameter polynomial proof; numerical eigenvalues alone are not an infinite proof.

## Relationship to prior work
Catral, Kirkland, Neumann and Sze (2010) develop general representations and convex perturbation considerations for Kemeny constants. Patel, Agharkar and Bullo (2015) give a general convex/semidefinite formulation for minimizing weighted Kemeny constants under stationary-distribution and graph constraints. Kirkland and Zeng (2016) establish tree random-walk formulas and investigate Braess edge effects, for the degree-driven random walk rather than unrestricted transition-probability optimization. Durastante, Gnazzo and Meini (2026) treat general structure-preserving Kemeny minimization algorithms and regularization, without these particular exact integer phase boundaries in the examined text. None of those general results is being claimed new here. The additional statement is the exact three-phase, all-parameter support classification and its quadratic branching window for the specifically defined three-generation tree.

## Limitations
The optimization requires a symmetric (uniform-stationary) stochastic matrix and the specified tree support. It does not characterize nonsymmetric chains, arbitrary stationary distributions, weighted travel times, or deeper trees. This is a same-model proof and comparison, not an independent audit. A complete global literature search cannot establish publication priority; unknown equivalent work remains possible. The exact cutoffs depend on the defined model and do not follow from numerical checks alone.

## References
- M. Catral, S. J. Kirkland, M. Neumann, N.-S. Sze, *The Kemeny Constant For Finite Homogeneous Ergodic Markov Chains*, Journal of Scientific Computing **45** (2010), 151–166. Lawful institutional-repository manuscript: https://mural.maynoothuniversity.ie/id/eprint/2185/1/SK_kemeny0209_revised.pdf ; repository deposit dated 2010-10-13.
- R. Patel, P. Agharkar, F. Bullo, *Robotic Surveillance and Markov Chains with Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control **60** (2015), 3156–3167. https://motion.me.ucsb.edu/pdf/2014b-pab.pdf
- S. Kirkland, Z. Zeng, *Kemeny's Constant and an Analogue of Braess' Paradox for Trees*, Electronic Journal of Linear Algebra **31** (2016), 444–464. https://emis.de/ft/34491
- F. Durastante, M. Gnazzo, B. Meini, *Kemeny's constant minimization for reversible Markov chains via structure-preserving perturbations*, BIT Numerical Mathematics **66** (2026), article 59. https://doi.org/10.1007/s10543-026-01152-6
