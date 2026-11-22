# Certified diagonal coercivity for eight-, nine-, and ten-stage Radau IIA collocation

## Finding

For the standard right-Radau IIA collocation matrices with stage counts \(s\in\{8,9,10\}\), explicit positive diagonal weights make the symmetrized inverse-stage matrix **strictly positive definite**. More precisely,

\[
W_s=10^{-5}\operatorname{diag}(k_{s,1},\ldots,k_{s,s}),\qquad
C_s=\tfrac12\bigl(W_s A_s^{-1}+A_s^{-\mathsf T}W_s\bigr)
\succ \frac{19}{20000}I_s.
\]

The complete integer weight vectors, in increasing collocation-node order, are

\[
\begin{aligned}
k_8&=(11631,19596,20636,18091,14101,9725,5356,865),\\
k_9&=(9292,16551,18497,17283,14532,11191,7711,4255,688),\\
k_{10}&=(7580,14096,16509,16200,14383,11864,9087,6262,3460,560).
\end{aligned}
\]

The overall scale of each positive diagonal may be changed, with a corresponding scale change in its positive-definiteness bound. The stated constants refer to the displayed unnormalized vectors.

## Assumptions and scope

For each of the three **finite** stage counts, let \(c_1<\cdots<c_{s-1}<c_s=1\) be the right-Radau IIA nodes in \((0,1]\). Equivalently, the first \(s-1\) nodes are the distinct roots in \((0,1)\) of the shifted Jacobi polynomial \(P_{s-1}^{(1,0)}(2t-1)\). Let \(\ell_j\) be the Lagrange cardinal polynomial of degree at most \(s-1\) at these nodes. The collocation matrix is defined precisely by

\[
(A_s)_{ij}=\int_0^{c_i}\ell_j(t)\,dt,\qquad 1\le i,j\le s.
\]

All matrices and comparisons are real, all weight entries are strictly positive, and \(X\succ Y\) denotes positive definiteness of \(X-Y\). There are no unspecified spatial discretization assumptions in the matrix claim.

## Proof

**1. Inverse matrix without numerical inversion.** Define degree-\(s\) polynomials

\[
\psi_j(t)=\frac{t}{c_j}\prod_{k\ne j}\frac{t-c_k}{c_j-c_k}.
\]

These are cardinal at the positive Radau nodes and vanish at zero. Given \(u_j\), the polynomial \(q(t)=\sum_j u_j\psi_j(t)\) satisfies \(q(0)=0\) and \(q(c_j)=u_j\). Since \(q'\) has degree at most \(s-1\), the exact quadrature-collocation identity \(q(c_i)=\sum_j(A_s)_{ij}q'(c_j)\) gives \(A_s^{-1}=(\psi_j'(c_i))_{ij}\). In particular, the inverse entries are rational functions of the distinct nonzero nodes, with

\[
(A_s^{-1})_{ii}=\frac1{c_i}+\sum_{k\ne i}\frac1{c_i-c_k},
\]

and, for \(i\ne j\),

\[
(A_s^{-1})_{ij}=\frac{c_i}{c_j(c_j-c_i)}
\prod_{k\notin\{i,j\}}\frac{c_i-c_k}{c_j-c_k}.
\]

**2. Algebraic isolation of the nodes.** The shifted Jacobi polynomial is evaluated in the exact binomial form

\[
P_m^{(1,0)}(2t-1)=\sum_{k=0}^{m}\binom{m+1}{k}\binom{m}{m-k}(t-1)^{m-k}t^k.
\]

For every required interior root, `check.py` supplies a consecutive rational interval with denominator \(10^{12}\). The exact polynomial values at its two endpoints have opposite signs. These \(s-1\) disjoint intervals therefore contain all \(s-1\) roots of the degree-\(s-1\) polynomial, in order. The final node is exactly one. No approximate root-finding outcome is used as a proof premise.

**3. Interval enclosure and coercivity certificate.** Apply exact rational interval operations to the displayed inverse-entry formulas. Because all necessary denominator intervals avoid zero, each exact \((A_s^{-1})_{ij}\) lies inside its computed interval. With the stated rational weights, the computed interval matrix encloses each entry of \(C_s\). Define a symmetric rational central matrix \(C_{0,s}\) by rounding the midpoint of each enclosing entry interval to the nearest multiple of \(10^{-5}\). The checker proves by exact fractions that

\[
\|C_s-C_{0,s}\|_{\infty}<\frac1{20000}
\quad\text{and}\quad
C_{0,s}-\frac1{1000}I_s\succ0.
\]

For the latter claim, the checker performs an unpivoted \(LDL^{\mathsf T}\) decomposition of the *rational* symmetric matrix \(C_{0,s}-I_s/1000\), verifies each pivot is strictly positive, and thus proves positive definiteness by Sylvester's criterion. Since both \(C_s\) and \(C_{0,s}\) are symmetric, \(\|C_s-C_{0,s}\|_2\le\|C_s-C_{0,s}\|_\infty\). Weyl's eigenvalue bound yields

\[
\lambda_{\min}(C_s)>
\frac1{1000}-\frac1{20000}=\frac{19}{20000},
\]

as claimed. The code verifies all three cases separately and contains the complete data and tests; no external package or hidden table is needed.

## Verification

Run `python3 check.py` with any standard Python 3 interpreter. The script is standalone, uses only `fractions.Fraction` and `math.comb`, and makes all critical comparisons using exact integers and rational numbers. It verifies root sign changes, root ordering, divisor separation, all weight signs, rational interval error row sums, and every strict rational \(LDL^{\mathsf T}\) pivot. Successful execution prints a PASS line. Its decimal diagnostics are informational only.

## Relationship to prior work

Henríquez, Lee and Rhebergen introduce the positive-definite symmetrized inverse-stage criterion as a sufficient hypothesis for their stage-weighted Radau IIA coercivity lemma. Their reported choice of weights succeeds for two through seven stages, but the paper reports negative smallest eigenvalues at eight, nine and ten stages and explicitly observes that another diagonal weight matrix would be needed. The present finite constructive certificates provide such matrices at exactly those three stages, without reproving or claiming the paper's general preconditioning theorem.

Classical Runge–Kutta algebraic stability gives nonnegative weighted forms but not the present **strict** positive-definiteness certificate for these particular positive diagonal entries. Banjai and Lubich study a related convolution-quadrature coercivity problem with a different differentiation symbol and, for higher orders, a shifted spectral parameter. Neither is an identified explicit positive diagonal certificate for the above three fixed inverse-stage matrices. The originality assessment retains priority risk from less accessible numerical-analysis and matrix-scaling literature.

## Limitations

Only stage counts \(8,9,10\) and the standard right-Radau IIA nodes are covered. No general formula for arbitrary stage count, optimal conditioning, high-order floating-point stability, or measured mesh-independent Krylov iteration rate is asserted. The bound on \(C_s\) is a matrix-level sufficient certificate, not an independent proof of every hypothesis of a full Stokes preconditioning result. Exact-arithmetic verification does not assert that a floating-point implementation has the same certified lower bound without rounding control. Independent validation has not been performed.

## References

- E. Henríquez, J. J. Lee and S. Rhebergen, *Preconditioning for the time-dependent Stokes equations: stage-weighted Radau IIA and weighted discontinuous Galerkin time-stepping*, arXiv:2611.08429v1, first public 2026-11-05. https://arxiv.org/abs/2611.08429
- L. Banjai and C. Lubich, *Runge–Kutta convolution coercivity and its use for time-dependent boundary integral equations*, arXiv:1702.08385v1, first public 2017-02-27. https://arxiv.org/abs/1702.08385
