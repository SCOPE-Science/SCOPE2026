# An exact leaf-count law and Gaussian fluctuations for ladder spanning trees

## Finding

Let \(G_n=P_2\square P_n\) be the unweighted two-rail ladder with \(n\ge1\) columns, and let \(T_n\) be uniformly distributed over its spanning trees. Let \(L_n\) count the vertices of degree one in \(T_n\), and define \(P_n(z)=\sum_{T\in\mathrm{ST}(G_n)}z^{L(T)-2}\). Then, as a formal power series in \(u\),
\[
\boxed{\displaystyle
\sum_{n\ge1}P_n(z)u^n
=\frac{u\{1-(z-1)u+(z^2-1)u^2-(z-1)^3u^3\}}
{1-(z+3)u+(3-2z)u^2-(2z^2-3z+1)u^3}.}
\]
This evaluates every finite probability \(\Pr(L_n=2+j)=[z^j]P_n(z)/P_n(1)\). For example, \(P_3(z)=8+6z+z^2\) and \(P_4(z)=14+28z+14z^2\). Moreover, with the strictly positive algebraic constants
\[
\mu=2\sqrt3-3,\qquad \sigma^2=\frac{92\sqrt3}{3}-53,
\]
we have
\[
\mathbb E L_n=\mu n+O(1),\qquad
\operatorname{Var}(L_n)=\sigma^2 n+O(1),\qquad
\frac{L_n-\mu n}{\sqrt{\sigma^2 n}}\Longrightarrow N(0,1).
\]
The limiting mean and variance are per *column*, or half as large per vertex. This theorem concerns the terminal-vertex statistic, not merely the number of present rungs.

## Assumptions and scope

The graph is simple, connected and unweighted; each of the \(3n-2\) edges has unit conductance. The spanning-tree measure is uniform. Both endpoints of the unique edge count as leaves when \(n=1\); thus \(L_1=2\). All claims about exact coefficients hold for every integer \(n\ge1\); the asymptotic and central-limit statements concern \(n\to\infty\) only. No independence of vertex leaf indicators is assumed.

## Proof

**1. Rung-gap decomposition.** Each spanning tree contains a nonempty set of vertical rungs, in columns \(r_1<\cdots<r_k\). Outside this interval, every horizontal rail edge is present. Between consecutive rungs at columns differing by \(d\), exactly one of the \(2d\) rail edges is absent; every choice is allowed. Indeed, deleting zero would leave a cycle and deleting two would disconnect a side segment. Conversely, this specification gives a connected graph with precisely \(2n-1\) edges, hence a spanning tree. This elementary description agrees with the established ladder renewal picture but is used here to count a different statistic.

**2. Local branch score.** Every vertex has degree at most three. The tree identity \(L=2+N_3\) follows by summing \(\deg(v)-2\), where \(N_3\) is the number of degree-three vertices. Such vertices can only occur in columns carrying a rung. For a gap between rungs, record its missing rail edge at the left endpoint as \(\ell\in\{0,+,-\}\), with \(0\) if the missing edge does not touch that rung, and similarly at the right endpoint as \(r\in\{0,+,-\}\). At an interior rung, with an incoming mark \(r\) and outgoing mark \(\ell\), its two vertices contribute \(f(r,\ell)\) to \(N_3\), where
\[
 f(0,0)=2,\quad f(0,s)=f(s,0)=f(s,s)=1\ (s\in\{+,-\}),\quad f(+,-)=f(-,+)=0.
\]
At a rung in column \(1\) or \(n\), the contribution is zero because there is no horizontal edge on the exterior side.

**3. Exact transfer and boundary terms.** Let \(u\) mark a column and \(z\) mark a degree-three vertex. For a gap, the \(3\times3\) matrix indexed by outgoing and incoming marks \(0,+,-\) is
\[
B(u)=\begin{pmatrix}
\frac{2u^3}{(1-u)^2}&\frac{u^2}{1-u}&\frac{u^2}{1-u}\\
\frac{u^2}{1-u}&u&0\\
\frac{u^2}{1-u}&0&u
\end{pmatrix}.
\]
The \(u\) entries enumerate a gap of length one. The terms \(u^2/(1-u)\) enumerate one missing edge adjacent to precisely one rung, and \(2u^3/(1-u)^2=\sum_{d\ge3}2(d-2)u^d\) counts a cut strictly inside a longer gap. Define
\[
M_{r,r'}(u,z)=\sum_{\ell\in\{0,+,-\}}z^{f(r,\ell)}B_{\ell,r'}(u),\qquad
 a_\ell(u,z)=1+\frac{u}{1-u}z^{f(0,\ell)},\qquad
 b_r(u,z)=1+\frac{u}{1-u}z^{f(r,0)}.
\]
The summand \(1\) in each boundary factor corresponds to a rung at the corresponding physical endpoint, whose degree-three contribution is zero; the geometric-series summand corresponds to an interior first or last rung. With just one rung, the generating series is
\[
H_1(u,z)=\frac{u\{1+(z^2-1)u^2\}}{(1-u)^2}.
\]
For two or more rungs, summing the intermediate marks and the number of gaps gives the *formal* matrix series
\[
H_{\ge2}(u,z)=u\,a(u,z)B(u)\bigl(I-M(u,z)\bigr)^{-1}b(u,z).
\]
Here \(a\) is a row and \(b\) is a column. The inverse is a valid formal series since each entry of \(M\) has zero constant term. Direct rational-matrix multiplication and cancellation yields
\[
H_1+H_{\ge2}
=\frac{u\{1-(z-1)u+(z^2-1)u^2-(z-1)^3u^3\}}
{1-(z+3)u+(3-2z)u^2-(2z^2-3z+1)u^3},
\]
proving the exact law. All boundary cases, including a single rung, are included. At \(z=1\), this reduces to \(u/(1-4u+u^2)\), recovering the known ladder spanning-tree counts.

**4. Quasi-power analysis.** Let \(D(u,z)\) denote the displayed denominator. At \(z=1\), \(D(u,1)=1-4u+u^2\) has its unique smallest-modulus root \(u_0=2-\sqrt3\). The numerator does not vanish there. Hence for complex \(z\) in a neighborhood of \(1\), the implicit function theorem and root separation give a unique simple dominant pole \(u(z)\), analytic in \(z\), with \(D(u(z),z)=0\). Uniform coefficient extraction by residues yields \(P_n(z)=c(z)u(z)^{-n}(1+O(\eta^n))\), where \(c(1)>0\) and \(0<\eta<1\) uniformly on a sufficiently small complex neighborhood. Thus, with \(z=e^t\),
\[
\log\mathbb E e^{t(L_n-2)}
=n\log\frac{u_0}{u(e^t)}+O(1),
\]
with analytic \(O(1)\) and exponentially small residual. Implicit differentiation at \((u_0,1)\) gives
\[
 u'(1)=12-7\sqrt3,\qquad u''(1)=264-\frac{457\sqrt3}{3}.
\]
Consequently, the first two derivatives at \(t=0\) of \(\log(u_0/u(e^t))\) are
\[
-\frac{u'(1)}{u_0}=2\sqrt3-3,
\quad
-\frac{u''(1)}{u_0}+\left(\frac{u'(1)}{u_0}\right)^2-\frac{u'(1)}{u_0}=\frac{92\sqrt3}{3}-53>0.
\]
Analytic differentiation gives the claimed first two moment estimates; expansion at \(t=s/\sqrt n\) of the centered moment-generating function gives convergence to \(\exp(\sigma^2s^2/2)\), which proves the stated normal limit. The constant shift of two leaves does not affect the scaling.

## Verification

`verify_ladder_leaves.py` is a standalone Python-standard-library checker. It independently enumerates all \(\binom{3n-2}{2n-1}\) candidate edge sets for \(1\le n\le7\), retaining exactly the connected acyclic ones; it compares their leaf-count histogram against coefficient polynomials from the stated rational function. It further checks the all-integer recurrence up to \(n=30\), total tree counts, positivity and exact rational variances. The checked execution returned `VERIFY_OK 99 exact checks; exhaustive n=1..7; coefficient recurrence n<=30`. This finite replay tests the algebra but does not replace the all-\(n\) transfer proof or the analytic limit argument.

## Relationship to prior work

Klenke (2017) proves the ladder-rung renewal process and the uniform missing-rail-edge location between successive rungs (Theorem 1.3 and Remark 1.4); this strong structural input and the classical total spanning-tree formula are prior work. The present result performs a global *leaf-marked* finite enumeration and evaluates the associated mean, variance and Gaussian fluctuations, none of which is asserted as a result of Klenke's cited theorems. Gantert and Klenke (2023) study biased walks on the resulting random environment, not this terminal-count law. Azimi and Farrokhi (2023) evaluate ladder Laplacian inverses and total spanning-tree counts, not leaf counts. Rapoport (2023) supplies general joint local-degree formulas, but no evaluated all-\(n\) ladder leaf-count generating series or these asymptotic constants. A published finite-volume rung-kernel result also addresses rung indicators only, not the leaf-count distribution. General formulas determine these probabilities in principle; the claimed result is the explicit evaluated rational law and its limit, not a new general spanning-tree framework.

## Limitations

No assertion is made about weighted ladders, wider strips, the least \(n\) for normal approximation accuracy, or real-rootedness of the finite leaf polynomials. The Gaussian theorem is asymptotic only and does not supply a uniform Berry–Esseen bound. A residual literature-priority risk remains because the exact rung/cut construction was known and could support an equivalent unindexed leaf enumeration; the inspected sources did not exhibit the evaluated law. Independent review has not been performed.

## References

1. A. Klenke, *The Random Spanning Tree on Ladder-like Graphs*, arXiv:1704.00182, first posted 2017-04-01, https://arxiv.org/html/1704.00182v1.
2. N. Gantert and A. Klenke, *Biased Random Walk on Spanning Trees of the Ladder Graph*, *Journal of Statistical Physics* 190 (2023), 83, https://doi.org/10.1007/s10955-023-03091-w.
3. A. Azimi and M. Farrokhi D. G., *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497, first posted 2023-06-18, https://arxiv.org/html/2306.10497v1.
4. A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992, first posted 2023-12-22, https://arxiv.org/html/2312.14992v1.
