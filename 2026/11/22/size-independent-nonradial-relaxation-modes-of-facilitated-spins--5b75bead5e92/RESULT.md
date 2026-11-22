# Size-independent nonradial relaxation modes of facilitated spins on bicliques

## Finding
For every integer \(m\ge 2\), every integer \(n\ge m\), and vacancy probability \(0<q<1\), the continuous-time FA-1f process on \(K_{m,n}\), restricted to configurations with at least one vacancy, has an exact positive relaxation eigenvalue \(\lambda_m(q)<1\) independent of \(n\). Its eigenspace contains an \((n-1)\)-dimensional family of distinct contrasts between vertices of the larger shore. Writing \(p=1-q\), this eigenvalue is the unique \(\lambda\in(0,1)\) satisfying

\[
\sum_{k=0}^{m}\frac{\binom{m}{k}p^{m-k}q^k}{k+1-\lambda}=1.
\]

Consequently the spectral gap \(\operatorname{gap}(K_{m,n},q)\) is at most \(\lambda_m(q)\). The rate increases strictly with \(m\) and with \(q\), and obeys

\[
\lambda_m(q)=\tfrac{m}{2}q+O_m(q^2)\quad(q\downarrow0),\qquad
1-\lambda_m(q)\sim\tfrac{m}{m-1}(1-q)^m\quad(q\uparrow1),
\]

and, for fixed \(q\in(0,1)\), \(1-\lambda_m(q)\sim (1-q)^m\) as \(m\to\infty\). This is an exact spectral branch and upper bound, **not** an assertion that it is the full spectral gap for all sizes. The previously known star case \(m=1\) has a different high-vacancy exponent, namely \(1-\lambda_1(q)=\sqrt{1-q}\).

## Assumptions and scope
A site has spin \(0\) (vacant) or \(1\) (occupied). Every site attempts an independent refresh at rate one, replacing its spin with a Bernoulli spin that is vacant with probability \(q\) and occupied with probability \(p\). A refresh is performed only if at least one neighbor is vacant. This is the one-spin-facilitated Fredrickson–Andersen (FA-1f) heat-bath generator \(L\), acting on functions. The all-occupied state is isolated; all other configurations communicate on connected \(K_{m,n}\), forming the reversible class \(\Omega_+\). All eigenvalues refer to \(-L\) on \(\Omega_+\). No degree normalization is used.

The two shores are \(A\) and \(B\) of sizes \(m\) and \(n\), respectively. Let \(D_A=-L_A\) and \(D_B=-L_B\) be the unconstrained independent-spin heat-bath operators on each shore. Let \(P_A\) and \(P_B\) multiply a function by the indicator that the respective shore contains a vacancy. On the full product space the exact identity is

\[
-L=D_A\otimes P_B+P_A\otimes D_B.
\]

## Proof
Choose any two distinct vertices \(u,v\in B\). Write \(\chi_{uv}(\eta_B)=\eta_u-\eta_v\), where \(\eta_i\) is the occupation indicator. Independent refresh gives \(D_B\chi_{uv}=\chi_{uv}\). The contrast vanishes on the completely occupied \(B\)-configuration, so \(P_B\chi_{uv}=\chi_{uv}\). Consequently, for every function \(h\) on \(A\),

\[
(-L)(h\otimes\chi_{uv})=((D_A+P_A)h)\otimes\chi_{uv}.
\]

The span of the vertex contrasts \(\chi_{uv}\) has dimension \(n-1\) (the orthogonal complement of the all-ones vector among degree-one Bernoulli–Walsh modes). Thus each eigenvalue of \(T_m=D_A+P_A\) yields an eigenvalue of \(-L\) with at least this multiplicity. Every resulting function vanishes on the isolated all-occupied configuration and, for nonzero eigenvalue, is orthogonal to the stationary law, so the eigenvalue survives restriction to \(\Omega_+\).

In the \(L^2\) space of \(m\) independent Bernoulli spins, \(D_A\) is diagonal in the normalized Walsh basis, with eigenvalues \(k\) on its degree-\(k\) sector. If \(v\) denotes the normalized indicator of the fully occupied \(A\)-configuration, \(P_A=I-vv^*\). The squared norm of the degree-\(k\) projection of \(v\) is \(w_k=\binom{m}{k}p^{m-k}q^k\). On the \((m+1)\)-dimensional span of these degree projections, \(T_m\) is therefore unitarily equivalent to \(\operatorname{diag}(1,2,\ldots,m+1)-ww^*\), with \(w\) now the column of positive square roots \(\sqrt{w_k}\). On all remaining Walsh directions its eigenvalues are integers at least two.

The matrix determinant lemma gives the secular equation displayed above for eigenvalues below one. Its left side at \(\lambda=0\) is strictly below one; it increases strictly with \(\lambda\) and diverges as \(\lambda\uparrow1\) because \(w_0=p^m>0\). Hence exactly one eigenvalue lies in \((0,1)\), which is simple for \(T_m\). This proves the eigenvalue, the multiplicity lower bound, and the gap upper bound.

For fixed \(q\) and increasing \(m\), a binomial random variable of parameters \((m,q)\) is strictly stochastically increasing; since \(k\mapsto(k+1-\lambda)^{-1}\) is strictly decreasing, the secular left side strictly decreases, forcing \(\lambda_m(q)\) strictly upward. The same binomial comparison as \(q\) grows gives strict increase in \(q\).

For \(q\downarrow0\), expansion at \(\lambda=0\) gives the secular left side \(1+\lambda-mq/2+O_m(q^2+q\lambda+\lambda^2)\), hence \(\lambda_m(q)=mq/2+O_m(q^2)\). Writing \(\varepsilon=1-\lambda_m(q)\), the secular identity becomes

\[
\frac{p^m}{\varepsilon}+\sum_{k=1}^m\frac{\binom{m}{k}p^{m-k}q^k}{k+\varepsilon}=1.
\]

At fixed \(m\ge2\) as \(p\downarrow0\), the second term converges to \(1/m\); this proves \(\varepsilon\sim mp^m/(m-1)\). At fixed \(q\in(0,1)\), the second term tends to zero as \(m\to\infty\) because the binomial count tends to infinity in probability, yielding \(\varepsilon\sim p^m\).

## Verification
The self-contained script `verify_fa_biclique.py` constructs the unconstrained block operator independently of its secular equation, checks the Bernoulli similarity transformation, then constructs the full configuration-space generator and confirms the product contrast eigenfunctions. Tests comprise \(35\) triples of parameters: \(q\in\{0.1,0.25,0.5,0.75,0.9\}\) and \((m,n)\in\{(2,2),(2,3),(2,5),(3,3),(3,4),(4,4),(4,5)\}\). Every finite residual is below \(2\cdot10^{-9}\); the symbolic proof above is what establishes the result for arbitrary integers and real \(q\).

## Relationship to prior work
Fredrickson and Andersen introduced facilitated spin kinetics in 1984. Cancrini, Martinelli, Roberto and Toninelli (arXiv:0712.1934, especially §6) proved general-graph spectral-gap comparisons and formulated the restricted nonempty-vacancy dynamics. Shapira (2020) obtained finite-graph spectral-gap scaling bounds. These do not directly assert the stated exact biclique nonradial eigenbranch or its all-parameter secular equation in the inspected material. The exact star-graph gap \(1-\sqrt{1-q}\) is existing related work; it covers \(m=1\), not the asserted \(m\ge2\) rates, exponent \(m\), or \((n-1)\)-dimensional biclique contrast modes.

## Limitations
The existence of the eigenbranch does not prove that it is the smallest positive eigenvalue of the full generator; no lower bound or full spectrum is claimed. The precise applicability is classical FA-1f with one-neighbor facilitation, uniform unit-refresh clocks, and complete bipartite coupling. Literature priority beyond the sources inspected is not certified. Numerical checks are finite illustrations, not a substitute for the general proof.

## References
- G. H. Fredrickson and H. C. Andersen, *Kinetic Ising Model of the Glass Transition*, Phys. Rev. Lett. 53, 1244 (1984), https://doi.org/10.1103/PhysRevLett.53.1244.
- N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, *Facilitated spin models: recent and new results*, arXiv:0712.1934 (12 December 2007), https://arxiv.org/abs/0712.1934.
- N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, *Kinetically constrained spin models*, arXiv:math/0610106 (3 October 2006), https://arxiv.org/abs/math/0610106.
- A. Shapira, *A Note on the Spectral Gap of the Fredrickson–Andersen One Spin Facilitated Model*, J. Stat. Phys. 181 (2020), https://doi.org/10.1007/s10955-020-02666-1.
