# Sharp unconditional positivity threshold for fourth-order Gauss–Legendre diffusion on weighted complete split graphs

## Finding

Let \(p,q\ge2\) be integers, \(b>0\), and \(t\ge0\). Form the weighted complete split graph \(K_p\vee\overline{K_q}\), assigning conductance \(b\) to all \(pq\) clique-to-independent edges and \(tb\) to every clique edge. Denote the symmetric combinatorial weighted Laplacian by \(L\). For the two-stage, order-four Gauss–Legendre Runge–Kutta method applied to \(\dot{z}=-Lz\), the **completed** transition matrix is
\[
T(h)=F(hL),\qquad F(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad h\ge0.
\]
Then the exact unconditional positivity region is
\[
\boxed{T(h)\ge0\text{ entrywise for all }h\ge0\quad\Longleftrightarrow\quad 0\le t\le 2+\frac pq.}
\]
For any allowed \(t\), \(T(h)\) is **strictly positive entrywise** for every \(h>0\), and is symmetric and stochastic at every nonnegative step. If \(t>2+p/q\), every transition joining distinct clique vertices becomes negative after exactly one positive crossing time; all other off-diagonal classes stay positive at all positive times.

Writing \(\alpha=pt+q\), the crossing time in the forbidden region is
\[
\boxed{h_* =\frac{3+\sqrt{9+12t(qt-p-2q)/\alpha}}{b(qt-p-2q)}.}
\]
All distinct clique transitions vanish at this time, are positive for \(0<h<h_*\), and negative for \(h>h_*\). At \(h=0\), \(T(0)=I\) even in the forbidden region.

## Assumptions and scope

The vertex sets are the clique \(C\) of size \(p\) and independent set \(I\) of size \(q\), both at least two. All crossing edges have exactly the same strictly positive conductance \(b\); all internal clique edges have exactly the same nonnegative conductance \(tb\); and there are no edges between distinct vertices of \(I\). The method is applied to a fixed linear autonomous equation. This is an exact-arithmetic, all-step theorem about \(F(hL)\), not about positivity of internal stages, floating-point implementations, arbitrary edge weights, or alternative numerical methods. The boundary value \(t=0\) is allowed and gives the complete bipartite graph.

## Proof

Set \(n=p+q\), \(x=bh\), and \(\alpha=pt+q\). Let \(J_{rs}\) denote the all-ones \(r\)-by-\(s\) matrix and \(J_r=J_{rr}\). Decompose \(\mathbb R^n\) orthogonally into constants; vectors supported on \(C\) whose clique coordinates sum to zero; vectors supported on \(I\) whose independent coordinates sum to zero; and the one-dimensional subspace spanned by \((q\mathbf 1_p,-p\mathbf1_q)\). The Laplacian eigenvalues on these four summands are respectively
\[
0,\qquad b\alpha,\qquad bp,\qquad bn.
\]
The corresponding orthogonal projectors are \(E_0=J_n/n\),
\[
E_C=\begin{pmatrix}I_p-J_p/p&0\\0&0\end{pmatrix},\qquad
E_I=\begin{pmatrix}0&0\\0&I_q-J_q/q\end{pmatrix},
\]
and
\[
E_B=\begin{pmatrix}
\frac{q}{pn}J_p&-\frac1n J_{pq}\\
-\frac1n J_{qp}&\frac{p}{qn}J_q
\end{pmatrix}.
\]
These projectors remain orthogonal even when some displayed eigenvalues coincide. Hence
\[
T(h)=E_0+F(\alpha x)E_C+F(px)E_I+F(nx)E_B.
\]
For convenience set \(D_s(x)=s^2x^2+6sx+12\). It is strictly positive for \(s\ge0\), \(x\ge0\), and \(F(sx)=((sx-3)^2+3)/D_s(x)>0\). Therefore \(T(h)\) is positive definite and all its diagonal entries are positive; also \(T(h)\mathbf1=\mathbf1\) and \(T(h)\) is symmetric.

For vertices in different parts, the projector formula gives
\[
T_{CI}(h)=\frac{1-F(nx)}n=\frac{12x}{D_n(x)}>0\quad(x>0).
\]
For two distinct vertices of the independent set,
\[
T_{II}(h)=\frac1n-\frac{F(px)}q+\frac{pF(nx)}{qn}
=\frac{12px^2((q+2p)x+6)}{D_p(x)D_n(x)}>0\quad(x>0).
\]
For two distinct clique vertices,
\[
\begin{aligned}
T_{CC}(h)&=\frac1n-\frac{F(\alpha x)}p+\frac{qF(nx)}{pn}\\
&=\frac{12x\left[\alpha(p+2q-qt)x^2+6\alpha x+12t\right]}{D_\alpha(x)D_n(x)}.
\end{aligned}
\]
The factorization follows by placing the three fractions over their positive common denominator and collecting powers of \(x\); it is checked symbolically in the accompanying verifier. If \(0\le t\le(p+2q)/q\), all coefficients in the bracket are nonnegative, its linear coefficient is strictly positive, and consequently it is positive for \(x>0\). This proves sufficiency, including both boundary cases.

If \(t>(p+2q)/q\), write \(u=qt-p-2q>0\). The clique bracket is \(-\alpha u x^2+6\alpha x+12t\), a concave quadratic with positive constant and linear terms. Its two real roots have opposite signs, so it has exactly one positive root. Solving gives \(x_*=[3+\sqrt{9+12tu/\alpha}]/u\). The bracket is positive for \(0<x<x_*\) and negative for \(x>x_*\), yielding the stated unique crossing time \(h_*=x_*/b\), and also proving necessity. There are no other potential negative entry classes. \(\square\)

## Verification

`artifacts/verify.py` uses exact symbolic rational arithmetic. It checks the three off-diagonal rational identities and directly computes the full completed matrix through polynomial matrix inversion for \(384\) rational parameter/time combinations with clique and independent-set sizes from \(2\) to \(5\), including \(t=0\), internal ratios below, at, and above the threshold. Every matrix is checked for symmetry, unit row sums, positive diagonals, and agreement with the closed-form entry classes. Another \(108\) rational/algebraic checks establish explicit negative witnesses beyond the threshold. A representative exact failure is \(p=q=2\), \(b=1\), \(t=4\), \(h=10\), where the transition between distinct clique vertices is \(-10140/1228339\). All finite tests are supporting checks; the universal statement is proved algebraically above.

To replay from a standalone package extracted into a directory, run `python artifacts/verify.py` with Python 3 and SymPy installed; see `VERIFICATION.md`.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten studied diagonal Padé discretization of positive systems and showed that high-order diagonal Padé approximants can fail positivity, even at arbitrarily small steps for appropriate Metzler matrices. Their results give general sufficient step-size conditions but not the present exact all-step split-network conductance classification [1]. Lóczi and Ketcheson determined absolute-monotonicity bounds for rational Runge–Kutta stability functions and note that the unique \([2/2]\) Padé function of order four has absolute-monotonicity radius zero [2]. This worst-case fact neither forces failure nor yields a sharp coupling threshold for this restricted graph family.

A later study of complete split graph Laplacian spectra concerns spectral determination of unweighted complete split graphs, not endpoint positivity under variable clique-to-cross conductance ratios [3]. The published eight-state Markov-Padé finding [4] concerns a directed pure-birth generator and a small-step failure dimension, rather than symmetric graph heat flow and the all-step weighted threshold here. The unweighted split case and other special cases are not independently claimed as discoveries; the principal claim is the complete sharp weighted ratio boundary and unique post-boundary crossing law.

## Limitations

The theorem applies only to the edge-orbit-uniform weighted complete split graph, with \(p,q\ge2\) and positive crossing rate. It says nothing about heterogeneous spoke conductances, stage positivity, nonlinear positivity preservation, or whether a floating-point discretization exhibits roundoff-level sign violations. It establishes a new exact statement relative to the materials inspected; it does not assert exhaustive novelty across unpublished or unindexed literature. The full text of the 2016 spectral-determination paper was not accessible in the inspected sources; only its publication abstract and bibliographic record were available. That paper is not a decisive competing positivity claim, but it remains part of the publication-priority uncertainty.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications **436** (2012), 3425–3442. DOI: https://doi.org/10.1016/j.laa.2011.12.021 ; lawful full-text preprint: https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf .
2. L. Lóczi, D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, LMS Journal of Computation and Mathematics **17** (2014), 159–205; first arXiv appearance March 26, 2013, https://arxiv.org/abs/1303.6651 ; DOI: https://doi.org/10.1112/S1461157013000326 .
3. K. C. Das, M. Liu, *Complete split graph determined by its (signless) Laplacian spectrum*, Discrete Applied Mathematics **205** (2016), 45–51. https://doi.org/10.1016/j.dam.2016.01.003 .
4. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, available public research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab/RESULT.md .
