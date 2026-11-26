# The exact \(L^4\) heat square-function contraction boundary on complete bipartite graphs

## Finding
Let \(m,n\) be arbitrary positive integers, and let \(K_{m,n}\) have unweighted edges and counting measure on its vertices. Write \(L\) for its combinatorial graph Laplacian, \(T_t=e^{-tL}\), and \(Ff=|V|^{-1}\sum_{v\in V}f(v)\). Fix any **nonzero** real or complex Hilbert space \(\mathcal H\), including the scalar case, and put
\[
G_2(f)(v)=\left(\int_0^\infty\|t\partial_tT_tf(v)\|_{\mathcal H}^2\,\frac{dt}{t}\right)^{1/2}.
\]
Then the following condition is necessary and sufficient for the sharp \(L^4\) estimate at the \(L^2\) coefficient:
\[
\boxed{\ \|G_2(f)\|_{\ell^4(V)}\le\tfrac12\|f-Ff\|_{\ell^4(V)}\quad\text{for all }f\ }
\quad\Longleftrightarrow\quad
\boxed{\ \max\{m,n\}\le2.\ }
\]
The best constant in the contractive cases is exactly \(1/2\), attained by every nonzero mean-zero Laplacian eigenfunction. For \(\max\{m,n\}\ge3\), the operator constant is strictly greater than \(1/2\), as witnessed below. This result does not determine that larger sharp constant.

## Assumptions and scope
The two parts \(A\) and \(B\) have \(m\) and \(n\) vertices respectively. All \(mn\) edges have weight one. The Laplacian is \(Lf(v)=\sum_{w\sim v}(f(v)-f(w))\), and the \(\ell^4\) norm is taken with counting measure; uniformly normalized vertex measure gives the same ratio. In the complex case all inner products in the deficit calculation are taken with their real part. Constants are annihilated by \(G_2\), so it suffices to consider mean-zero inputs. For the excluded Hilbert space \(\{0\}\), every input is zero and the inequality is vacuous for all \(m,n\), with best nonnegative constant zero. The result concerns the vertical heat \(q=2\) square function at spatial exponent four, not a discrete-time or gradient square function.

## Proof
Write the mean-zero input uniquely as
\[
f|_A=(u_1+a,\ldots,u_m+a),\qquad f|_B=(v_1+b,\ldots,v_n+b),
\quad\sum_i u_i=0,\quad\sum_j v_j=0,\quad ma+nb=0.
\]
The three mutually orthogonal components have graph Laplacian eigenvalues \(n\) (the \(A\)-contrast), \(m\) (the \(B\)-contrast), and \(m+n\) (the between-part mode). Direct integration, using
\[
\int_0^\infty t\lambda\mu e^{-(\lambda+\mu)t}\,dt
=\frac{\lambda\mu}{(\lambda+\mu)^2},
\]
shows that at an \(A\)-vertex
\[
4G_2(f)(i)^2=\|u_i\|^2+\|a\|^2+2\rho_A\operatorname{Re}\langle u_i,a\rangle,
\quad \rho_A=\frac{4n(m+n)}{(m+2n)^2}=1-\frac{m^2}{(m+2n)^2}.
\]
At a \(B\)-vertex the analogous formula holds with \(v_j,b\) and \(\rho_B=4m(m+n)/(2m+n)^2=1-n^2/(2m+n)^2\). In particular, \(0<\rho_A,\rho_B<1\).

Define \(\beta_i=\operatorname{Re}\langle u_i,a\rangle\), \(\gamma_j=\operatorname{Re}\langle v_j,b\rangle\), and the fourth-power deficit \(\Delta(f)=\|f\|_4^4-16\|G_2(f)\|_4^4\). Expanding the preceding identities and using \(\sum_i\beta_i=\sum_j\gamma_j=0\) gives the exact formula
\[
\begin{aligned}
\Delta(f)={}&4(1-\rho_A)\sum_{i=1}^m\|u_i\|^2\beta_i
 +4(1-\rho_A^2)\sum_{i=1}^m\beta_i^2\\
 &+4(1-\rho_B)\sum_{j=1}^n\|v_j\|^2\gamma_j
 +4(1-\rho_B^2)\sum_{j=1}^n\gamma_j^2.
\end{aligned}
\]
If \(m\le2\), either every \(u_i=0\), or \((u_1,u_2)=(h,-h)\), whence \(\sum_i\|u_i\|^2\beta_i=0\). The corresponding statement applies to \(n\le2\). Hence if \(m,n\le2\), \(\Delta(f)\ge0\) for every input. Moreover, equality holds precisely when every \(\beta_i\) and every \(\gamma_j\) vanishes (the condition is vacuous on singleton parts). Equivalently, every available two-vertex within-part contrast is real-inner-product orthogonal to its between-part mode. Taking any nonzero single-eigenvalue mean-zero input gives equality and establishes sharpness; such an input exists, for instance in the between-part mode along a unit vector of \(\mathcal H\).

Conversely, assume first that \(m\ge3\). On three \(A\)-vertices take the real scalar contrast \((u_1,u_2,u_3)=(2,-1,-1)\), with all other contrasts zero. Set \(a=-\delta\) and \(b=m\delta/n\), where \(\delta=1/4\). Thus \(f\) is mean-zero, with no \(B\)-contrast. Because \(\sum_i u_i^3=6\) and \(\sum_i u_i^2=6\), the exact deficit is
\[
\Delta(f)=24(1-\rho_A)\delta\bigl((1+\rho_A)\delta-1\bigr)
=-\frac32(1-\rho_A)(3-\rho_A)<0.
\]
Consequently \(\|G_2(f)\|_4^4>\|f\|_4^4/16\). If instead \(n\ge3\), interchange the two parts. The real scalar witness works in every nonzero real or complex Hilbert space by multiplying by a fixed unit vector.

## Verification
The standalone standard-library file `checker.py` uses the closed-form spectral coefficients to compare the two fourth-power deficit formulas and check the strict witness with exact rational arithmetic on ordered pairs \((m,n)\) with \(1\le m,n\le20\) and \(\max\{m,n\}\ge3\). It separately compares sample complex deficits with floating-point tolerances in the four contractive part-size cases. These are finite checks of the algebra and examples, not an independent evaluation of the heat integral or a proof of the all-size classification. The heat integral is evaluated in the proof.

## Relationship to prior work
Lai, Li and Li, *Optimal orders for Hilbert-valued Littlewood–Paley functions of symmetric semigroups*, arXiv:2611.10710, study the vertical square function and general spatial \(L^p\) bounds, including the exact \(L^2\) coefficient \(1/2\). Those general estimates do not decide when the same coefficient works at spatial exponent four on complete bipartite graphs. Feneuil, arXiv:1404.1353, studies discrete graph Littlewood–Paley functionals under graph hypotheses. A related small-graph classification treats graphs of order at most three and an amplifying four-vertex path. A related cycle classification also concerns the case \(K_{2,2}=C_4\) and reports a general cubic obstruction. A sufficient obstruction from a nonzero mixed moment \(\sum u^3v\) of unequal positive heat eigenvalues can explain failure on the larger bicliques, using the same cubic moment as in the witness here. The exact deficit calculation above gives the positive direction, the full Hilbert-valued equality condition there, and the size-dependent witness deficit in one identity.

## Limitations
The sharp norm in the amplifying cases is not computed. This is a classification only for complete bipartite graphs with the combinatorial Laplacian and the vertical \(q=2\) heat square function at spatial \(p=4\). It does not classify general connected graphs, normalized-degree Laplacians, other graph weightings, other \(p,q\), or discrete-time Littlewood–Paley functions. The exact extent of overlap with related classifications is not settled by catalogue summaries or bibliographic descriptions.

## References
1. X. Lai, B. Li, J. Li, *Optimal orders for Hilbert-valued Littlewood–Paley functions of symmetric semigroups*, arXiv:2611.10710. https://arxiv.org/abs/2611.10710
2. J. Feneuil, *Littlewood–Paley functionals on graphs*, arXiv:1404.1353. https://arxiv.org/abs/1404.1353
3. *Four vertices are necessary and sufficient for fourth-norm amplification*, related catalogue record. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-four-vertices-are-necessary-and-sufficient-for-fourth-norm-ampli--10b68babaeff
4. *A cubic spectral obstruction and the exact heat square-function boundary on finite cycles*, related catalogue record. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-cubic-spectral-obstruction-and-the-exact-heat-square-function--8c9eaae9692f
