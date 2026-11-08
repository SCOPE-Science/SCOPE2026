# Sharp magic-positivity cutoff for polar book-graph symmetric-edge polytopes

## Finding

Let \(G_q=K_{1,1,q}\), the graph with two adjacent hubs joined to \(q\) independent leaves. If \(Q_q\) is the lattice polar of its symmetric edge polytope, then its degree-\(q+1\) Ehrhart polynomial has the exact formula
\[
L_q(t)=(2t+1)^q+2\sum_{s=1}^{t}(2t+1-s)^q\quad(t\in\mathbb Z_{\ge0}).
\]
In the unique magic expansion
\[
L_q(t)=\sum_{j=0}^{q+1}a_j(q)t^j(t+1)^{q+1-j},
\]
**all coefficients are strictly positive if and only if \(1\le q\le6\)**. For each \(q\ge7\), at least one coefficient is negative, so magic positivity never returns.

## Assumptions and scope

The graph \(G_q\) has vertices \(u,v,w_1,\ldots,w_q\) and edges \(uv,uw_i,vw_i\) for all \(i\). Its symmetric edge polytope is \(P_q=\operatorname{conv}\{\pm(e_a-e_b):ab\in E(G_q)\}\) in \(H=\{x\in\mathbb R^{q+2}:\sum x_i=0\}\), with root lattice \(H\cap\mathbb Z^{q+2}\). The polar \(Q_q\) is defined in the **dual lattice**; its points are integer vertex potentials modulo a common additive constant satisfying \(|f(a)-f(b)|\le1\) on every graph edge. Here \(q\) is any positive integer and \(t\) is any nonnegative integer. All assertions concern the polar \(Q_q\), not the original symmetric edge polytope.

## Proof

**1. Exact enumeration and degree.** Fix the hub potential \(f(u)=0\). In \(tQ_q\), the other hub has an integer potential \(s=f(v)\) with \(-t\le s\le t\). Each leaf potential belongs to the intersection of two integer intervals, \([-t,t]\cap[s-t,s+t]\), which contains exactly \(2t+1-|s|\) integers. Leaf choices are independent. Summing over \(s\) gives the formula in the Finding. By the Bernoulli power-sum identity this extends to a polynomial in \(t\) of degree \(q+1\), as also follows from Ehrhart's theorem for the full-dimensional lattice polytope \(Q_q\).

**2. Low magic coefficients.** Write \(B_m\) for Bernoulli numbers with \(B_1=-1/2\). Bernoulli-polynomial summation gives the polynomial identity
\[
L_q(t)=(2t+1)^q+\frac{2}{q+1}\bigl(B_{q+1}(2t+1)-B_{q+1}(t+1)\bigr).
\]
For \(q\ge5\), the coefficients of \(t,t^2,t^3\) in this polynomial are, respectively,
\[
2q+2B_q,\qquad 2q(q-1)+3qB_{q-1},\qquad \frac43q(q-1)(q-2)+\frac73q(q-1)B_{q-2}.
\]
The constant coefficient equals one. Comparing ascending powers against the magic basis by triangular elimination yields
\[
\begin{aligned}
a_1(q)&=q-1+2B_q,\\
a_2(q)&=\frac{q(q-3)}2+3qB_{q-1}-2qB_q,\\
a_3(q)&=\frac{q(q-1)}6\bigl(q-5+6B_q-18B_{q-1}+14B_{q-2}\bigr).
\end{aligned}
\]
The second and third formulas are used only where \(q\ge5\).

**3. An infinite obstruction in each residue class.** For every even \(m\ge14\), Euler's identity \(|B_m|=2m!\zeta(m)/(2\pi)^m\) implies
\[
\frac{|B_{m+4}|}{|B_m|}=\frac{(m+1)(m+2)(m+3)(m+4)}{(2\pi)^4}\frac{\zeta(m+4)}{\zeta(m)}
>\frac{15\cdot16\cdot17\cdot18}{2(44/7)^4}>2.
\]
Indeed \(\zeta(m)<2\), \(\zeta(m+4)>1\), and \(\pi<22/7\). The same ratio bound holds for larger even \(m\) because the factorial factor increases. For each base parameter used below, \(q-C\ge10\), so the positive affine threshold \(c(q)=q-C\) grows by a factor less than two under \(q\mapsto q+4\). This property persists at larger parameters, and therefore each strict base inequality propagates by steps of four:

* If \(q\equiv0\pmod4\) and \(q\ge20\), then \(a_1(q)=q-1-2|B_q|<0\), beginning with \(|B_{20}|=174611/330>(20-1)/2\).
* If \(q\equiv1\pmod4\) and \(q\ge17\), then \(a_2(q)=q((q-3)/2-3|B_{q-1}|)<0\), beginning with \(|B_{16}|=3617/510>(17-3)/6\).
* If \(q\equiv2\pmod4\) and \(q\ge18\), then \(a_2(q)=q((q-3)/2-2B_q)<0\), beginning with \(B_{18}=43867/798>(18-3)/4\).
* If \(q\equiv3\pmod4\) and \(q\ge19\), then \(a_3(q)=q(q-1)(q-5-18B_{q-1})/6<0\); the stronger base \(q=15\) uses \(B_{14}=7/6>(15-5)/18\) and propagates by four.

Here the Bernoulli sign pattern is \(B_{4r}<0\), \(B_{4r+2}>0\), and \(B_{2r+1}=0\) for \(r\ge1\). These four cases cover every integer \(q\ge17\).

**4. The sharp finite cutoff.** Exact rational triangular elimination from the lattice-count polynomial gives the following complete magic coefficient vectors for \(q=1,\ldots,6\) (entries ordered from \(a_0\) to \(a_{q+1}\)):

| \(q\) | Complete magic coefficient vector |
|---:|---|
| 1 | \((1,1,1)\) |
| 2 | \((1,4/3,4/3,1)\) |
| 3 | \((1,2,3/2,2,1)\) |
| 4 | \((1,44/15,34/15,34/15,44/15,1)\) |
| 5 | \((1,4,9/2,2,9/2,4,1)\) |
| 6 | \((1,106/21,61/7,71/21,71/21,61/7,106/21,1)\) |

For \(q=7,\ldots,16\), the pairs \((j,a_j(q))\) providing strict negative witnesses are
\[
\begin{array}{c|rrrrrrrrrr}
q&7&8&9&10&11&12&13&14&15&16\\
\hline
j&4&4&5&5&6&6&7&7&8&8\\
a_j(q)&-5/4&-14/15&-198/5&-662/11&-399&-286772/455&-156612/35&-35441/5&-548685/8&-5493182/51
\end{array}
\]
Each entry is an exact rational identity, obtainable from the coefficient of \(t^j\) using \(a_j=[t^j]L_q-\sum_{k<j}\binom{q+1-k}{j-k}a_k\). The attached standard-library verifier computes all these from an independent Newton interpolation of integer lattice counts. The finite checks are exhaustive for the finitely specified \(q\)'s; the separate Bernoulli argument proves the infinite tail. Combining both proves the theorem.

## Verification

Run `python verify.py` (Python 3 standard library only). It constructs the original count for every \(1\le q\le16\), interpolates with exact rational Newton forward differences, converts independently to the magic basis, verifies the displayed rational vectors/witnesses, verifies the first three Bernoulli coefficient identities, and tests independent integer values beyond the interpolation range. It also checks the four Bernoulli bases and several ratio inequalities. The program reports `VERIFY_OK 344 exact assertions`. The infinite sign argument is analytic; sampling does not certify its universal range.

## Relationship to prior work

Higashitani and Mori (2026) identify \(K_{1,1,q}\) as one of exactly three families of connected graphs whose symmetric edge polytopes can be Minkowski decomposable, making its polar's coefficient behavior a natural missing invariant. Kounoike (2024) proves Stasheff and some graph-polar magic-positivity results and tabulates complete bipartite cases, but not the present book-graph family. Ohsugi and Tsuchiya (2026) establish broad positive theorems for polars of pseudo-symmetric **simplicial** reflexive/smooth Fano polytopes and graph-cycle polars; those hypotheses do not imply magic positivity for these book-graph polars, which are demonstrably non-magic-positive for \(q\ge7\). The separate complete bipartite graph thresholds do not imply this tripartite classification. The present result supplies the exact coefficient cutoff for the remaining structurally distinguished graph family.

## Limitations

This is a classification only for \(K_{1,1,q}\) graph polars and the specified magic basis; it does not claim that their Ehrhart coefficients or \(h^*\)-coefficients become negative, nor that the original (unpolarized) symmetric edge polytopes have the same behavior. Literature priority is not independently certified. The computational check covers only the stated finite range, with the infinite tail justified analytically.

## References

1. A. Higashitani and A. Mori, *Minkowski decomposability of symmetric edge polytopes*, arXiv:2608.02445, first publicly posted 2026-08-03. https://arxiv.org/abs/2608.02445
2. H. Ohsugi and A. Tsuchiya, *Magic positivity for polar duals of pseudo-symmetric smooth Fano polytopes*, arXiv:2610.06419, first publicly posted 2026-10-05. https://arxiv.org/abs/2610.06419
3. M. Kounoike, *A new class of magic positive Ehrhart polynomials of reflexive polytopes*, arXiv:2409.16648, first publicly posted 2024-09-25. https://arxiv.org/abs/2409.16648
4. Euler's formula for the even Bernoulli numbers and the classical Bernoulli-polynomial power-sum identity (standard identities).
