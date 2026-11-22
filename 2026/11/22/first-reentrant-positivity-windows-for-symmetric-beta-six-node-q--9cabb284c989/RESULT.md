# First reentrant positivity windows for symmetric-Beta six-node quadrature

## Finding

Fix the six equispaced nodes \(x_j=j/5\), \(j=0,\ldots,5\), on \([0,1]\). For any reflection-symmetric probability measure \(\mu\) on \([0,1]\), let \(Q_\mu f=\sum_{j=0}^5W_j f(x_j)\) be the unique interpolatory quadrature rule exact for all polynomials of degree at most five. Put
\[
v=\int_0^1(x-\tfrac12)^2\,d\mu(x),\qquad
q=\int_0^1(x-\tfrac12)^4\,d\mu(x).
\]
Its six weights are \((A,B,C,C,B,A)\), where
\[
A=\frac{10000q-1000v+9}{768},\quad
B=-\frac{25(400q-104v+1)}{256},\quad
C=\frac{25(400q-136v+9)}{384}.
\]
Consequently, **all six quadrature weights are nonnegative if and only if**
\[
10000q-1000v+9\ge0,\qquad
400q-104v+1\le0,\qquad
400q-136v+9\ge0.
\tag{1}
\]
The admissible symmetric moment pairs are exactly \(0\le v\le\tfrac14\), \(v^2\le q\le v/4\). Every such pair is realized by a symmetric probability measure. Thus (1) is an exact positivity region across **all** reflection-symmetric probability laws, including discrete ones.

For the symmetric Beta family \(\mu_a=\operatorname{Beta}(a,a)\), with **every real** \(a>0\), define
\[
r_- =\frac{107-\sqrt{1081}}{18}=4.1178575308029\ldots,\qquad
r_+ =\frac{107+\sqrt{1081}}{18}=7.7710313580860\ldots.
\]
Then the complete positivity set is the **disconnected union**
\[
\boxed{\quad 0<a\le r_-\quad\text{or}\quad r_+\le a\le11.\quad}
\tag{2}
\]
More explicitly, the endpoint weights are negative exactly when \(r_-<a<r_+\), the next-to-endpoint weights are negative exactly when \(a>11\), and the two innermost weights are always strictly positive. At the three positive boundary values \(r_-,r_+,11\), the corresponding pair of weights vanishes and the other four are positive.

This **return of positive weights** is the first such disconnected parameter set among the closed equispaced interpolatory rules with two through six nodes: for panel counts \(1,2,3,4\), the symmetric-Beta positivity sets are respectively \((0,\infty)\), \((0,\infty)\), \((0,4]\), and \([1/2,9/2]\); for five panels (six nodes) it is (2).

## Assumptions and scope

The nodes are fixed before choosing the target integration law, the quadrature has degree-five polynomial exactness, and \(\mu\) is an arbitrary reflection-symmetric Borel **probability** measure supported on the closed unit interval. There is no assumption of an everywhere-positive density in the general moment statement. For (2), the density is \(x^{a-1}(1-x)^{a-1}/\operatorname{B}(a,a)\) on \((0,1)\), with real \(a>0\). The result concerns the signs of this unique fixed-node interpolatory rule, not the existence of some *other* positive rule with movable nodes.

## Proof

**1. Uniqueness and symmetric moment reduction.** For \(0\le j\le5\), write the Lagrange cardinal polynomial
\[
L_j(x)=\prod_{\substack{0\le k\le5\\k\ne j}}\frac{x-k/5}{j/5-k/5}.
\]
Polynomial exactness uniquely forces \(W_j=\int L_j\,d\mu\), since \(L_j(x_k)=\delta_{jk}\). If \(\mu(E)=\mu(1-E)\), then \(W_{5-j}=W_j\) and all odd centered moments vanish. Set \(z=x-1/2\). The even parts of the first three cardinal polynomials are exactly
\[
\begin{aligned}
\frac{L_0(1/2+z)+L_0(1/2-z)}2
 &=\frac{(10z-3)(10z-1)(10z+1)(10z+3)}{768},\\
\frac{L_1(1/2+z)+L_1(1/2-z)}2
 &=-\frac{25(2z-1)(2z+1)(10z-1)(10z+1)}{256},\\
\frac{L_2(1/2+z)+L_2(1/2-z)}2
 &=\frac{25(2z-1)(2z+1)(10z-3)(10z+3)}{384}.
\end{aligned}
\]
Their expectations give exactly \(A,B,C\) above. The identities also give \(2(A+B+C)=1\) for every feasible moment pair, so the rule is normalized.

**2. Feasibility of the moment region.** Since \(0\le z^2\le1/4\), Jensen's inequality gives \(q\ge v^2\) and the pointwise bound \(z^4\le z^2/4\) gives \(q\le v/4\). Conversely, if \(v>0\) and these inequalities hold, let \(c=q/v\in(0,1/4]\) and \(p=v^2/q\in(0,1]\). Put probability \(1-p\) at \(z=0\) and probability \(p/2\) at each of \(z=\pm\sqrt c\). This symmetric distribution has exactly the prescribed second and fourth moments. For \(v=0\), necessarily \(q=0\), realized by a point mass at the midpoint. The signs of the three explicit pair weights are therefore both necessary and sufficient throughout the entire feasible moment domain, proving (1).

**3. Exact symmetric-Beta substitution.** For \(X\sim\operatorname{Beta}(a,a)\), standard beta moments or direct integration give
\[
\mathbb E(X-1/2)^2=\frac1{4(2a+1)},\qquad
\mathbb E(X-1/2)^4=\frac3{16(2a+1)(2a+3)}.
\]
Substituting in the three moment formulas and clearing positive denominators yields
\[
\begin{aligned}
A(a)&=\frac{9a^2-107a+288}{192(2a+1)(2a+3)},\\
B(a)&=\frac{25a(11-a)}{64(2a+1)(2a+3)},\\
C(a)&=\frac{25a(9a+1)}{96(2a+1)(2a+3)}.
\end{aligned}
\tag{3}
\]
The numerator of \(A\) has positive leading coefficient, discriminant \(1081\), and distinct positive roots \(r_-<r_+\). Hence \(A(a)<0\) precisely between those roots. For all \(a>0\), \(C(a)>0\), and \(B(a)<0\) precisely for \(a>11\). Because \(r_+<11\), the negative-pair intervals are disjoint, proving (2) and the claimed boundary cases without any numerical root inference.

**4. Minimality among the first five panel counts.** For each panel count \(n\in\{1,2,3,4\}\), form the cardinals at \(j/n\), integrate them against the same \(\operatorname{Beta}(a,a)\) law, and simplify. Writing weights from left to right gives
\[
\begin{array}{c|l}
n &\text{weights (symmetric order)}\\\hline
1&(1/2,1/2)\\
2&(E,F,E),\quad E=\frac1{2(2a+1)},\quad F=\frac{2a}{2a+1}\\
3&(E,F,F,E),\quad E=\frac{4-a}{8(2a+1)},\quad F=\frac{9a}{8(2a+1)}\\
4&(E,F,G,F,E),\quad E=\frac{9-2a}{6(2a+1)(2a+3)},\quad
F=\frac{16a}{3(2a+1)(2a+3)},\quad
G=\frac{2a(2a-1)}{(2a+1)(2a+3)}.
\end{array}
\]
All denominators are positive for \(a>0\); inspecting the displayed numerators gives the four connected positivity sets in the finding. The five-panel rule (3) is therefore the first disconnected instance in this finite hierarchy.

**5. Exact operational meaning of the signs.** For nodal data \(0\le f(x_j)\le1\), the smallest possible computed quadrature value is \(\sum_{W_j<0}W_j\); this is attained by assigning value one at the negative-weight nodes and zero elsewhere. A continuous nonnegative piecewise-linear function realizes those values, so a negative quadrature value is not merely a formal array artifact. For \(\mu_a\), the sharp minimum equals \(2A(a)\) on \((r_-,r_+)\), equals \(2B(a)\) for \(a>11\), and equals zero otherwise. The exact operator norm on bounded nodal data is \(\sum_j|W_j|\), equal to one exactly in (2) and strictly larger elsewhere; as \(a\to\infty\), this norm tends to \(89/64\).

## Verification

Run `python verify.py` using only the Python standard library. The script independently expands the six cardinal polynomials over exact rational coefficients; checks all three even-part identities and their normalization; clears the parameter denominators to check all Beta numerator polynomials as exact identities; and reconstructs all weights for panel counts one through five directly from independent raw Beta moments. It then tests exact polynomial reproduction for every monomial through the corresponding degree, for fourteen distinct positive rational shape parameters, a total of **280 exact monomial equalities**, plus exact rational phase witnesses and the root discriminant. The script is supplementary: the symbolic derivation and sign proof above establish the real-parameter and general-measure conclusions.

## Relationship to prior work

General moment-based expressions for arbitrary weighted Newton–Cotes coefficients are established by Masjed-Jamei, Milovanović and Jafari (2013), Theorem 2.1. Those general coefficient identities are prior art and are not claimed here. Masjed-Jamei, Milovanović and their collaborators (2005) also introduce Jacobi-weighted closed Newton–Cotes rules, including a two-node formula and Chebyshev-weight experiments. Van den Bos and Sanderse (2019) explain positive-weight interpolatory quadrature through Vandermonde geometry, including examples involving a symmetric Beta distribution, but address adding or replacing nodes rather than the fixed six-site density-parameter classification. Trefethen (2021/2022) discusses the distinction between polynomial exactness and stability of classical quadrature, including Newton–Cotes coefficients.

The claim here is **not** a new general construction of weighted coefficients. Its precise addition is the sharp feasible symmetric-moment sign region at the fixed six sites, the two exact disconnected Beta-concentration positivity windows, the proof that no such disconnection occurs at lower panel counts, and the sharp negative-output consequence for nonnegative data. These phase statements were not found in the inspected portions of the cited primary sources; full historical priority is not independently established.

## Limitations

The six-site moment classification assumes reflection symmetry. The symmetric-Beta sign windows apply to the unique closed equispaced interpolatory rule, and not to optimized or moving-node quadrature or arbitrary nonsymmetric Jacobi weights. Minimality is proved only among closed equispaced rules with panel counts one through five; nothing is asserted about higher panel counts. The result concerns positivity and norm, not approximation order beyond exactness, adaptive accuracy, or asymptotic convergence for changing node count. The general weighted-coefficient identity is known, and an earlier specialization to this exact Beta family may exist outside the literature material inspected. An independently performed originality or mathematical audit is not claimed.

## References

1. L. M. M. van den Bos and B. Sanderse, *A geometric approach for the addition of nodes to an interpolatory quadrature rule with positive weights*, arXiv:1902.07477 (first public 2019-02-20), https://arxiv.org/abs/1902.07477.
2. M. Masjed-Jamei, G. V. Milovanović and M. A. Jafari, *Closed expressions for coefficients in weighted Newton–Cotes quadratures*, *Filomat* 27 (2013), 649–658, https://doi.org/10.2298/FIL1304649M; open text https://www.pmf.ni.ac.rs/filomat-content/2013/27-4/F27-4-15.pdf.
3. M. Masjed-Jamei and collaborators, *The first kind Chebyshev–Newton–Cotes quadrature rules (closed type) and its numerical improvement*, *Applied Mathematics and Computation* 168 (2005), 479–495, https://doi.org/10.1016/j.amc.2004.09.048.
4. L. N. Trefethen, *Exactness of Quadrature Formulas*, arXiv:2101.09501 (2021), *SIAM Review* 64 (2022), https://arxiv.org/abs/2101.09501.
