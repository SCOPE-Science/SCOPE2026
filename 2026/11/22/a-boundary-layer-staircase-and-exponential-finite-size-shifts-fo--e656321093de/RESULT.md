# A boundary-layer staircase and exponential finite-size shifts for screened-path Nyström landmarks

## Finding

For the combinatorial Laplacian of the unit-weight half-line path on \(\mathbb N_0=\{0,1,2,\ldots\}\), let \(K_\mu=(\mu I+L)^{-1}\), \(\mu>0\). Define the finite **rank-one Nyström trace capture** at site \(j\) by
\[
C_j(\mu)=\operatorname{tr}\!\left(\frac{K_\mu e_j e_j^{\mathsf T}K_\mu}{(K_\mu)_{jj}}\right)=\frac{(K_\mu^2)_{jj}}{(K_\mu)_{jj}}.
\]
(The full infinite-volume trace is divergent; this finite rank-one trace is the object optimized.) Put
\[
\beta=\operatorname{arcosh}(1+\mu/2),\quad q=e^{-\beta},\quad f_a(\beta)=\frac{a}{1+e^{a\beta}},\quad a>0.
\]
Then
\[
C_j(\mu)=\frac{\cosh\beta}{2\sinh^2\beta}+\frac{f_{2j+1}(\beta)}{2\sinh\beta}.
\]
For each \(j\ge0\), there is a unique \(q_j\in(0,1)\) satisfying
\[
(2j+1)-(2j+3)q_j^2-2q_j^{2j+3}=0,
\qquad \mu_j=q_j+q_j^{-1}-2.
\]
These are strictly decreasing screening thresholds \(\mu_0=1/2>\mu_1>\mu_2>\cdots\downarrow0\). At \(\mu=\mu_j\), exactly sites \(j,j+1\) maximize capture. At any other screening, exactly one site maximizes capture: site \(0\) if \(\mu>\mu_0\), and site \(j\ge1\) precisely when \(\mu_j<\mu<\mu_{j-1}\). No nonadjacent sites tie for the maximum.

Set \(c=1+W(e^{-1})=1.278464542761\ldots\), where \(W\) is the positive real Lambert function. Then
\[
\lim_{j\to\infty}(2j+1)^2\mu_j=c^2,\qquad
j_{\mathrm{opt}}(\mu)=\frac{c}{2\sqrt\mu}+O(1)\quad(\mu\downarrow0),
\]
with either optimal index used at a tie.

For the **finite** unit path \(P_n\), \(n\ge2\), indexed from \(0\) to \(n-1\), the capture at \(j\) has exactly the same site ordering as
\[
F_{n,j}(\beta)=f_{2j+1}(\beta)+f_{2n-2j-1}(\beta).
\]
Fix \(j\ge0\). For all sufficiently large \(n\), there is exactly one global-optimum switch in a fixed neighborhood of \(\mu_j\), between the reflected site-pairs \(\{j,n-1-j\}\) and \(\{j+1,n-2-j\}\). Denote its screening by \(\mu_{n,j}\). It approaches \(\mu_j\) **from above** with the sharp asymptotic
\[
\mu_{n,j}-\mu_j
=\frac{2\sinh\beta_j\,(e^{2\beta_j}-1)}{d_j}
(2n-2j-1)e^{-(2n-2j-1)\beta_j}(1+o(1)),
\]
where \(\beta_j=-\log q_j\) and
\[
d_j=\left.\frac{\partial}{\partial\beta}\big(f_{2j+1}(\beta)-f_{2j+3}(\beta)\big)\right|_{\beta=\beta_j}>0.
\]
In particular, for the last outward transition (endpoint versus next-to-endpoint),
\[
\mu_{n,0}-\frac12\sim\frac{27}{4}(2n-1)2^{-(2n-1)}.
\]
For every fixed \(\mu\) away from the half-line thresholds, the finite-path optimum eventually consists exactly of the reflection pair of its unique half-line optimal index.

## Assumptions and scope

All edges have unit conductance, and the screened operator has a **uniform strictly positive** scalar shift. The half-line graph has a degree-one endpoint at \(0\) and degree-two vertices thereafter; \(L\) is the bounded nonnegative self-adjoint combinatorial Laplacian on \(\ell^2(\mathbb N_0)\). The finite graph is the ordinary (not Dirichlet-pinned) path, with its two degree-one endpoints. Every finite \(\mu>0\) is covered. The finite-size switching assertion is for each **fixed** \(j\) and all sufficiently large \(n\), not a claimed globally ordered phase diagram for every small \(n\). All displayed \(o(1)\) terms are with \(j\) fixed and \(n\to\infty\); the low-screening asymptotic is on the infinite half-line.

## Proof

**1. Rank-one trace identity.** For positive self-adjoint \(K_\mu\), its rank-one Nyström approximation at \(j\) is \((K_\mu e_j)(K_\mu e_j)^{\mathsf T}/(K_\mu)_{jj}\). Its trace is \(\|K_\mu e_j\|_2^2/(K_\mu)_{jj}\). The resolvent identity gives \(\partial_\mu (K_\mu)_{jj}=-(K_\mu^2)_{jj}\), hence
\[
C_j(\mu)=-\partial_\mu\log (K_\mu)_{jj}.
\]
This identity is valid on the half-line because \(\mu>0\) puts the resolvent in the bounded-operator class and each column in \(\ell^2\).

**2. Exact half-line Green diagonal.** The decaying solution of the interior resolvent recurrence has ratio \(q=e^{-\beta}\), with \(\mu=q+q^{-1}-2\). Imposing the degree-one boundary equation at site \(0\) gives the method-of-images kernel
\[
(K_\mu)_{ij}=\frac{q^{|i-j|+1}+q^{i+j+2}}{1-q^2}\quad (i,j\ge0).
\]
Substitution checks both the tridiagonal recurrence and the boundary row; exponential decay makes it the unique resolvent kernel. Thus
\[
(K_\mu)_{jj}=\frac{1+q^{2j+1}}{2\sinh\beta},
\qquad\partial_\mu\beta=\frac1{2\sinh\beta}.
\]
Differentiating its logarithm proves the capture formula.

**3. Exact staircase.** The only site-dependent capture term is \(f_a(\beta)\) at positive odd integers \(a=2j+1\). For fixed \(\beta>0\),
\[
\frac{\partial^2}{\partial a^2}\log f_a(\beta)
=-\frac1{a^2}-\frac{\beta^2e^{a\beta}}{(1+e^{a\beta})^2}<0.
\]
Consequently its odd-index sequence is strictly log-concave: an optimizer is unique or consists of two neighboring odd indices. The sign of \(f_a-f_{a+2}\) is exactly the sign of
\[
P_a(q)=a-(a+2)q^2-2q^{a+2}.
\]
Since \(P_a(0)=a>0\), \(P_a(1)=-4<0\), and \(P'_a(q)<0\) on \((0,1)\), it has a unique simple root \(q_a\). The strict log-concavity implies \(f_{a+2}>f_{a+4}\) at \(q_a\), hence \(q_a<q_{a+2}\); thus all successive crossings are strictly ordered. Since \(f_a\to0\) as \(a\to\infty\) for each \(\beta>0\), an optimizer exists. For each fixed \(q<1\), eventually \(f_a>f_{a+2}\), which implies \(q_a\to1\). Setting \(a=1\), \(P_1(q)=(1-2q)(1+q)^2\), so \(q_1=1/2\) and \(\mu_0=1/2\).

**4. Boundary-layer scale.** The continuous function \(a\mapsto f_a(\beta)\) rises then falls, because its derivative vanishes exactly where \(t=a\beta\) solves \(t=1+e^{-t}\). This equation has the unique positive root \(c=1+W(e^{-1})\). Applying Rolle's theorem between \(a\) and \(a+2\) at their crossing gives \(c/(a+2)<\beta_a<c/a\). The relations \(\mu=2(\cosh\beta-1)=\beta^2+O(\beta^4)\) and the fact that optimal odd indices lie within bounded distance of \(c/\beta\) yield both asymptotic assertions.

**5. Finite paths and exponential shift.** For the ordinary finite path, direct solution of the same tridiagonal recurrence at both reflecting endpoints gives
\[
(K_{n,\mu})_{jj}
=\frac{q(1+q^{2j+1})(1+q^{2n-2j-1})}{(1-q^2)(1-q^{2n})},
\quad 0\le j<n.
\]
Differentiating its logarithm shows that its capture differs from \(F_{n,j}(\beta)/(2\sinh\beta)\) by a common site-independent quantity. For indices \(0\le j\le\lfloor(n-1)/2\rfloor\), the second summand in \(F_{n,j}\) tends uniformly to zero on any compact positive-\(\beta\) interval, at rate \(O(n e^{-n\beta_{\min}})\). This uniform convergence and the strict gap from nonoptimizing half-line sites show that near a fixed transition \(\beta_j\), for all large \(n\) only the two indicated reflected site-types can win.

Write \(a=2j+1\), \(b=2n-a\), and \(D_a(\beta)=f_a(\beta)-f_{a+2}(\beta)\). Their finite comparison is
\[
D_a(\beta)+f_b(\beta)-f_{b-2}(\beta).
\]
At \(\beta_j\), \(D_a=0\) and \(d_j=D_a'(\beta_j)>0\) because \(P_a\) has a simple positive-to-negative crossing as \(q\) increases. For fixed \(\beta_j>0\),
\[
f_b(\beta_j)-f_{b-2}(\beta_j)
=-(e^{2\beta_j}-1)b e^{-b\beta_j}(1+o(1)).
\]
The implicit-function argument (the derivative correction is \(O(b^2e^{-b\beta_j})\)) yields a unique local switch and
\[
\beta_{n,j}-\beta_j=\frac{e^{2\beta_j}-1}{d_j}\,b e^{-b\beta_j}(1+o(1))>0.
\]
Multiplication by \(\partial_\beta\mu=2\sinh\beta_j\) gives the stated screening shift. At \(j=0\), \(\beta_0=\log 2\), \(d_0=2/3\), and \(2\sinh\beta_0=3/2\), producing the coefficient \(27/4\). Away from thresholds, the same uniform-tail comparison ensures the stable reflected finite-path optimum.

## Verification

The standalone `checker.py` independently inverts exact rational finite-path matrices and confirms both the Green diagonal and all pairwise landmark-gain orderings on \(2\le n\le12\) for four rational values of \(q\). It also checks existence/order and asymptotic root brackets for 51 odd-index thresholds and compares the exponentially small finite-size first transition against high-precision root solutions. Run `python checker.py`; its recorded output is in `checker_output.txt`. The exact analytic proof, rather than a finite parameter grid, establishes the universal statements.

## Relationship to prior work

Gittens and Mahoney (2013) analyze Nyström approximation and trace-norm error bounds for general symmetric positive matrices; their results motivate the landmark-selection objective but do not specify the optimal site or phase thresholds for the screened half-line Green matrix. Fornace and Lindsey (2024), especially Section 2.1, explicitly formulate the general captured-trace objective \(\operatorname{tr}((K^2)_{SS}K_{SS}^{-1})\) and study general-purpose selection methods and inverse graph-Laplacian reduction. Their objective is **exactly** the one used here, not a novel identity; their inspected structural results do not establish the boundary-index staircase, Lambert constant, or sharp finite-path threshold shift. Standard one-dimensional Green recurrence methods supply the matrix entries, while the optimization classification and finite-size switch analysis are the finding.

## Limitations

This result covers one exact Nyström column, the ordinary unit-weight path, uniform positive screening, and the half-line plus its finite-path boundary limit. It does not prove the full finite-\(n\) phase diagram at all screenings, handle multiple simultaneous columns, claim optimality for arbitrary weighted paths, or make a claim about convergence of the divergent infinite trace. Source indexing is incomplete, so unindexed equivalent optimizer results remain a publication-priority risk. Independent audit has not been performed.

## References

1. A. Gittens and M. W. Mahoney, *Revisiting the Nyström Method for Improved Large-Scale Machine Learning*, first posted 2013-03-07, arXiv:1303.1849, https://arxiv.org/abs/1303.1849. Relevant: introduction and Section 4.1.5 on trace-norm errors.
2. M. Fornace and M. Lindsey, *Column and row subset selection using nuclear scores: algorithms and theory for Nyström approximation, CUR decomposition, and graph Laplacian reduction*, first posted 2024-07-01, arXiv:2407.01698, https://arxiv.org/abs/2407.01698. Relevant: Sections 1, 2.1 and 2.4 and mathematical appendices.
