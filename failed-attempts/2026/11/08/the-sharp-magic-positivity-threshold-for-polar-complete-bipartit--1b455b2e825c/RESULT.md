# The sharp magic-positivity threshold for polar complete-bipartite symmetric edge polytopes

## Finding
Let \(G_q=K_{2,q}\), with integer \(q\ge1\). Let \(P_{G_q}\) be the symmetric edge polytope of the graph and \(P_{G_q}^{\vee}\) its lattice polar. Write \(d=q+1\) and expand its Ehrhart polynomial uniquely as
\[
L_{P_{G_q}^{\vee}}(t)=\sum_{i=0}^{d}a_i(q)t^i(t+1)^{d-i}.
\]
**Theorem.** Every magic coefficient \(a_i(q)\) is strictly positive if and only if \(1\le q\le8\). For every \(q\ge9\), at least one magic coefficient is strictly negative. In particular, the entire positive range, including the exceptional boundary case \(q=8\), and all infinite negative tails are determined exactly.

## Assumptions and scope
Use the root lattice \(M=\{x\in\mathbb Z^{q+2}:\sum x_i=0\}\) in the hyperplane \(H=\{x\in\mathbb R^{q+2}:\sum x_i=0\}\). Set
\[
P_{G_q}=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G_q)\}\subset H.
\]
Its polar is taken in \(N=\operatorname{Hom}(M,\mathbb Z)\cong\mathbb Z^{q+2}/\mathbb Z\mathbf1\), so its lattice points are integral vertex-potential assignments modulo simultaneous integral translation, with \(\lvert x_u-x_v\rvert\le t\) on edges. The graph is connected, hence \(P_{G_q}\) has dimension \(q+1\); its polar is a lattice polytope. A polynomial of degree \(d\) is **magic positive** if all coefficients in the basis \(\{t^i(t+1)^{d-i}\}_{i=0}^{d}\) are nonnegative. Our conclusion is stronger on the positive side (all coefficients strictly positive). No result is claimed for other complete bipartite sizes \(K_{p,q}\) with \(p\ge3\), or for standard monomial Ehrhart positivity.

## Proof
**1. Exact lattice-point formula.** Denote the two vertices of the first bipartition class by \(u_1,u_2\), and the remaining \(q\) vertices by \(w_1,\ldots,w_q\). Normalize the potential by translating so that \(\min(x_{u_1},x_{u_2})=0\), and put \(r=\lvert x_{u_1}-x_{u_2}\rvert\). For \(r=0\), each potential \(x_{w_j}\) has \(2t+1\) choices. For \(1\le r\le2t\), there are two orders for \((x_{u_1},x_{u_2})=(0,r)\) or \((r,0)\), and each \(x_{w_j}\) must lie in the common interval \([r-t,t]\), which has \(2t-r+1\) integer values. For \(r>2t\) the interval is empty. Thus for all nonnegative integers \(t\),
\[
\boxed{L_q(t)=(2t+1)^q+2\sum_{s=1}^{2t}s^q.}\tag{1}
\]
Faulhaber's polynomial identity makes the right side a polynomial of degree \(q+1\), and uniqueness of Ehrhart polynomials extends identity (1) to formal \(t\).

**2. Coefficients controlled by Bernoulli numbers.** Define \(B_j\) by \(z/(e^z-1)=\sum_{j\ge0}B_jz^j/j!\), and \(B_m(x)=\sum_{j=0}^m\binom{m}{j}B_jx^{m-j}\). Then
\[
L_q(t)=(2t+1)^q+\frac{2}{q+1}\bigl(B_{q+1}(2t+1)-B_{q+1}(1)\bigr).\tag{2}
\]
Let \(c_j\) denote the ordinary coefficient of \(t^j\) in \(L_q\). Expanding the magic basis gives the triangular relations
\[
a_0=c_0=1,\quad a_1=c_1-(q+1),\quad
a_2=c_2-\binom{q+1}{2}-q a_1,
\]
\[
a_3=c_3-\binom{q+1}{3}-\binom q2a_1-(q-1)a_2.\tag{3}
\]
By (2) and \(B_{2j+1}=0\) for \(j\ge1\), direct simplification yields, for even \(q\ge4\),
\[
\boxed{a_1=q-1+4B_q,\qquad a_2=q\left(\frac{q-3}{2}-4B_q\right).}\tag{4}
\]
For odd \(q\ge5\),
\[
\boxed{a_1=q-1,\quad a_2=q\left(\frac{q-3}{2}+4B_{q-1}\right),\quad
a_3=\frac{q(q-1)}6\left(q-5-24B_{q-1}\right).}\tag{5}
\]
These are exact identities for all indicated integers; no asymptotic approximation is used.

**3. Four infinite residue classes.** The Euler--zeta formula and the sign rule for even Bernoulli numbers are
\[
B_{2m}=(-1)^{m+1}\frac{2(2m)!}{(2\pi)^{2m}}\zeta(2m).
\]
For every even integer \(j\ge14\), using \(1<\zeta(j+2)\), \(\zeta(j)<2\), and \(\pi^2<10\), one has
\[
\frac{|B_{j+2}|}{|B_j|}
=\frac{(j+2)(j+1)}{4\pi^2}\frac{\zeta(j+2)}{\zeta(j)}
>\frac{(j+2)(j+1)}{8\pi^2}\ge\frac{240}{8\pi^2}>3.
\]
Consequently \(\lvert B_{j+4}\rvert>9\lvert B_j\rvert\). The exact anchor values are
\[
B_{14}=\frac76,\qquad B_{16}=-\frac{3617}{510},\qquad B_{18}=\frac{43867}{798}.
\]
For each residue class, the displayed coefficient is negative at the first indicated integer by (4)--(5), and remains negative as \(q\) increases by four: the relevant Bernoulli magnitude grows by a factor greater than nine, while the competing positive linear quantity grows by a factor smaller than two.

| Residue class | Starting \(q\) | Strictly negative witness | Starting inequality |
| --- | ---: | --- | --- |
| \(q\equiv3\pmod4\) | 15 | \(a_3\) | \(B_{14}>(15-5)/24\) |
| \(q\equiv0\pmod4\) | 16 | \(a_1\) | \(-B_{16}>(16-1)/4\) |
| \(q\equiv1\pmod4\) | 17 | \(a_2\) | \(-B_{16}>(17-3)/8\) |
| \(q\equiv2\pmod4\) | 18 | \(a_2\) | \(B_{18}>(18-3)/8\) |

The inductive comparison is valid because each right-hand side is proportional to \(q-5\), \(q-1\), or \(q-3\), respectively, and those positive linear quantities increase by less than a factor of two under \(q\mapsto q+4\). This proves failure for every \(q\ge15\).

**4. Exact finite boundary.** The complete magic coefficient vectors for \(q=1,\ldots,8\), in increasing index order, are as follows; all are strictly positive:

| \(q\) | \((a_0,\ldots,a_{q+1})\) |
| ---: | --- |
| 1 | \((1,2,1)\) |
| 2 | \((1,5/3,5/3,1)\) |
| 3 | \((1,2,2,2,1)\) |
| 4 | \((1,43/15,38/15,38/15,43/15,1)\) |
| 5 | \((1,4,13/3,8/3,13/3,4,1)\) |
| 6 | \((1,107/21,59/7,79/21,79/21,59/7,107/21,1)\) |
| 7 | \((1,6,44/3,10,2/3,10,44/3,6,1)\) |
| 8 | \((1,103/15,316/15,1252/45,2/15,2/15,1252/45,316/15,103/15,1)\) |

For \(9\le q\le14\), the following exact single negative coefficient suffices in each case:

| \(q\) | Index \(i\) | \(a_i(q)\) |
| ---: | ---: | ---: |
| 9 | 5 | \(-144/5\) |
| 10 | 5 | \(-598/11\) |
| 11 | 6 | \(-892/3\) |
| 12 | 6 | \(-262324/455\) |
| 13 | 4 | \(-27967/105\) |
| 14 | 5 | \(-21971/15\) |

All entries follow by exact rational polynomial arithmetic from (1) (algorithm below). Together with step 3, this finishes the classification.

## Verification
The standalone `verify.py` uses only Python's standard library. It forms the degree-\(q+1\) polynomial from the exact integer values in (1) by Newton finite differences, converts to ordinary powers and then to the magic basis using the triangular relations. It checks the complete vectors at \(q=1,\ldots,8\), the six finite negative certificates at \(q=9,\ldots,14\), Bernoulli starting values and inequalities, and the coefficient identities at further values \(15\le q\le32\). Every computed fraction is exact. Executing `python3 verify.py` gives `VERIFY_OK 176 exact rational checks`. The proof for the infinite tail is the Bernoulli-ratio argument of step 3; finite computation alone would not suffice.

## Relationship to prior work
Konoike's *A new class of magic positive Ehrhart polynomials of reflexive polytopes* (arXiv:2409.16648, §4, table on p. 7) explicitly reports a finite table of graph-polar magic positivity for complete bipartite graphs, including the positive \(K_{2,8}\) exception and negative examples at \(K_{2,9}\), \(K_{2,10}\), and \(K_{2,11}\). That table does **not** state or prove a classification for all \(q\ge12\). Its exact finite observations are prior work, not new contributions. The new content here is the all-integer theorem, the exact graph-potential formula (1) in this presentation, and the four-residue Bernoulli obstruction proving the infinite tail.

Ohsugi and Tsuchiya's *Magic positivity for polar duals of pseudo-symmetric smooth Fano polytopes* (arXiv:2610.06419, first public October 5, 2026) establishes general positivity for its structural Fano classes and every cycle graph. Its cycle theorem does not cover the present family of complete bipartite graph polars. The older work of Higashitani, Kummer and Michałek on *interlacing Ehrhart polynomials of reflexive polytopes* and complete-bipartite symmetric edge polytopes concerns the original (primal) graph polytopes and their \(h^*\) data; it is not a magic-positivity classification of the polars.

## Limitations
Only the \(K_{2,q}\) family is classified. The classification does not assert that magic negativity forces failure of ordinary Ehrhart positivity or failure of \(h^*\)-real-rootedness: those are distinct properties. The exact finite table in the 2024/2025 prior work is acknowledged. The historical priority of the infinite classification is based on inspected sources and searches, not independent exhaustive bibliographic certification; independent mathematical audit has not been performed.

## References
1. H. Ohsugi and A. Tsuchiya, *Magic positivity for polar duals of pseudo-symmetric smooth Fano polytopes*, arXiv:2610.06419 (2026), especially Theorems 1.2 and 1.4 and the graph-polar discussion. https://arxiv.org/abs/2610.06419
2. M. Konoike, *A new class of magic positive Ehrhart polynomials of reflexive polytopes*, arXiv:2409.16648 (first posted 2024; version 2, 2025), §4 and its complete-bipartite numerical table. https://arxiv.org/pdf/2409.16648
3. A. Higashitani, L. Kummer and M. Michałek, *Interlacing Ehrhart polynomials of reflexive polytopes*, Selecta Mathematica (2017), arXiv:1612.07538, especially the primal symmetric-edge cases. https://arxiv.org/abs/1612.07538
