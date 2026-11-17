# Exact period-two Floquet resonance and singular memory limits in a finite-memory fractional logistic map

## Finding
Consider the finite-memory Grünwald–Letnikov (GL) logistic recurrence defined below. For every fractional order \(0<q\leq1\) and every integer memory length \(M\geq2\), there is exactly **one** control value beyond the birth of its primitive two-cycle at which that two-cycle has Floquet multiplier \(-1\). This value is given by an explicit finite-sum radical, not by a nonlinear continuation solve. Its large-memory limit and first asymptotic correction also have closed forms. The limits \(q\downarrow0\) and \(M\to\infty\), when applied to these finite-memory resonance values, do not commute.

Let
\[
 g_j(q)=(-1)^j\binom qj,\quad
 P_M(z)=\sum_{j=0}^M g_j(q)z^j,\quad
 s_M=P_M(1),\quad t_M=P_M(-1),
\]
with \(g_0=1\). Define
\[
 r_1(q,M)=1+2s_M+t_M,\qquad
 K_M(q)=\bigl|t_M+iP_M(-i)\bigr|^2.
\]
The **unique period-two \(-1\) Floquet resonance** is
\[
 \boxed{r_2^{[-1]}(q,M)=1+s_M+
 \sqrt{(s_M+t_M)^2+K_M(q)}}.
\]
It satisfies \(r_2^{[-1]}(q,M)>r_1(q,M)\). The formula locates a multiplier resonance; it does **not**, by itself, establish that this is the first stability loss or that a period-four branch emerges generically at all parameters.

For fixed \(0<q<1\), set
\[
 T_q=2^q,\quad Z_q=(1+i)^q,\quad
 R_q=1+\sqrt{T_q^2+|T_q+iZ_q|^2},\quad
 A_q=\frac{1+T_q/(R_q-1)}{\Gamma(1-q)}.
\]
Then \(A_q>0\) and
\[
 \boxed{r_2^{[-1]}(q,M)=R_q+A_qM^{-q}+O_q(M^{-2q})},
 \qquad M\to\infty.
\]
Here the complex power uses the principal branch. Furthermore,
\[
 \boxed{\lim_{q\downarrow0}\lim_{M\to\infty}r_2^{[-1]}(q,M)=1+\sqrt3},
\]
whereas
\[
 \boxed{\lim_{M\to\infty}\lim_{q\downarrow0}r_2^{[-1]}(q,M)=2+\sqrt6}.
\]
These limits describe the resonance of **finite-dimensional truncated systems**, not exact periodic solutions of a genuinely infinite-memory fractional recurrence.

## Assumptions and scope
Fix \(r>0\), \(M\in\mathbb N\), \(M\ge2\), and \(0<q\le1\). A state is a real history of length \(M\), evolving by
\[
 \sum_{j=0}^{M}g_j(q)x_{n+1-j}=rx_n(1-x_n)-x_n.
\]
A primitive period-two orbit consists of two distinct phases \(x_+\), \(x_-\), repeated in alternation; the corresponding state-space orbit is obtained by stacking the last \(M\) phases. The Floquet multipliers are the eigenvalues of the derivative of the two-step state map. The term resonance means that \(-1\) is one of these multipliers, with no assumption about the other multipliers.

## Proof
**Two-cycle existence and parametrization.** For a two-periodic scalar sequence, write \(x_n=u+(-1)^nv\). The GL operator has gains \(s_M\) on the constant component and \(t_M\) on the alternating component. Substitution into the original recurrence gives
\[
 s_Mu=(r-1)u-r(u^2+v^2),\qquad
 -t_Mv=(r-1-2ru)v.
\]
For a primitive cycle \(v\neq0\), so
\[
 u=\frac{r-1+t_M}{2r},\qquad
 (2rv)^2=(r-1+t_M)(r-r_1).
\]
For \(0<q<1\), the coefficients \(g_j\) are negative for \(j\ge1\) and have total absolute sum one; at \(q=1\) they are zero except \(g_1=-1\). Consequently \(s_M\ge0\), \(t_M>1\), and \(s_M+t_M=2\sum_{0\le 2k\le M}g_{2k}>0\). Hence \(r-1+t_M>0\) for all \(r>0\). A distinct real two-cycle exists precisely for \(r>r_1\) and is unique up to phase interchange. Its phases are
\[
 x_\pm=\frac{r-1+t_M\pm\sqrt{(r-1+t_M)(r-r_1)}}{2r}.
\]
They lie strictly between zero and one: their product equals \((r-1+t_M)(s_M+t_M)/(2r^2)>0\); their sum is \(1+(t_M-1)/r<2\). Also
\[
 (1-x_+)(1-x_-)=
 \frac{r(2+s_M-t_M)+(t_M-1)(s_M+t_M)}{2r^2}>0.
\]
The last inequality follows from \(2+s_M-t_M>0\) when \(q<1\), because the total mass of the negative odd-index coefficients is smaller than one; at \(q=1\), the remaining product term is strictly positive. Positivity of the factors and the sum bound prove \(x_\pm<1\).

**Four-phase Floquet reduction.** Along the two-cycle, the linear variational equation is
\[
 \sum_{j=0}^{M}g_jy_{n+1-j}=(r-1-2rx_n)y_n.
\]
The two-step multiplier \(-1\) is equivalent to the antiperiodic condition \(y_{n+2}=-y_n\), so every corresponding scalar sequence has four-phase form \((p,z,-p,-z)\). Write
\[
 c_M=\operatorname{Re}\bigl(iP_M(-i)\bigr),\qquad
 d_M=\operatorname{Im}\bigl(iP_M(-i)\bigr).
\]
The two independent variational equations become
\[
 \begin{pmatrix}
 c_M+t_M+2rv&d_M\\
 -d_M&c_M+t_M-2rv
 \end{pmatrix}
 \binom pz=\binom00.
\]
(The phase choice only changes the sign of \(v\).) Its determinant vanishes exactly when
\[
 (r-1+t_M)(r-r_1)=(t_M+c_M)^2+d_M^2=K_M.
\]
This equivalence is valid in both directions: any nonzero two-step multiplier eigenvector determines such a four-phase sequence, and any nonzero solution of the displayed two-by-two system reconstructs a nonzero length-\(M\) eigenvector because \(M\ge2\). Moreover \(d_M>0\), since it contains \(g_0=1\), adds the positive quantities \(-g_{4k+2}\), and subtracts only a proper subcollection of the negative \(g_{4k}\) with total magnitude less than one. Thus \(K_M>0\). The left side is strictly increasing from zero to infinity as \(r\) increases above \(r_1\). Solving the resulting quadratic gives the unique claimed radical, and proves it exceeds \(r_1\).

**Sharp memory asymptotics.** For fixed \(0<q<1\), the binomial identity and gamma ratio yield
\[
 s_M=\frac{\Gamma(M+1-q)}{\Gamma(1-q)\Gamma(M+1)}
 =\frac{M^{-q}}{\Gamma(1-q)}+O_q(M^{-q-1}).
\]
The sequence \(|g_j|\) is eventually decreasing with order \(O_q(j^{-1-q})\). Alternating-sum and fourth-root-of-unity tail estimates therefore imply
\[
 t_M=2^q+O_q(M^{-1-q}),\quad
 P_M(-i)=(1+i)^q+O_q(M^{-1-q}).
\]
Inserting these into the exact radical and Taylor-expanding at \(s_M=0\) gives
\[
 r_2^{[-1]}=R_q+\left(1+\frac{T_q}{R_q-1}\right)s_M
 +O_q(s_M^2+M^{-1-q}),
\]
which is the claimed \(A_qM^{-q}+O_q(M^{-2q})\), since \(0<q<1\). For each fixed finite \(M\), \(g_j(q)\to0\) for \(j\ge1\) as \(q\downarrow0\), so \(s_M,t_M,P_M(-i)\to1\) and the resonance tends to \(2+\sqrt6\). In the reversed order, the preceding infinite-\(M\) formula gives \(T_q\to1\), \(Z_q\to1\), \(R_q\to1+\sqrt3\). This proves noncommutation.

## Verification
Run `python3 verify.py` from the directory containing this result and the checker. It uses only the Python standard library, evaluates the original recurrence and original four-phase variational equations at the proposed resonance for a grid of orders and memory lengths, checks the unique quadratic root and strict location beyond cycle birth, and measures convergence to the sharp large-memory coefficient. The expected successful output begins `VERIFY_OK`. The analytical arguments, not finite arithmetic, prove uniqueness and the limits.

## Relationship to prior work
Dong, Li, Li, and Xie (first public preprint 20 July 2026; peer-reviewed article 23 August 2026) established a general periodic–antiperiodic Floquet equation and an exact first flip boundary, while locating higher levels including the two-cycle numerically. The present explicit radical *solves* the two-cycle \(-1\) condition for every finite memory, and proves its limiting value and sharp \(M^{-q}\) coefficient; the earlier equations supply a general implicit characterization but not these explicit nonfixed-orbit results. An earlier mathematical finding establishes the complete primitive two-cycle census and local supercriticality at its birth, which is **not** claimed as new here. Earlier full-history fractional-map analyses address asymptotic phase cycles under different memory constructions. Classical two-dimensional Hénon two-cycle formulas cover the minimal two-step memory case after an affine conjugacy, but do not supply the arbitrary-\(M\) result or its large-memory asymptotics. These distinctions concern statements and dynamical objects, not merely terminology.

## Limitations
This result identifies exactly where the primitive two-cycle has a multiplier \(-1\), but does not prove that all other multipliers are inside the unit disk, nor nondegenerate birth of a period-four orbit at the resonance, for arbitrary \(q\) and \(M\). No global attraction, other bifurcations, invariant physical domain for arbitrary histories, or exact infinite-history periodic orbit is asserted. The complex-power limit is only the limit of finite-memory resonance parameters. Publication-priority comparisons are necessarily bounded by source access; especially earlier full-history and other finite-memory fractional conventions need expert comparison.

## References
1. Z. Dong, H. Li, S. Li, and Y. Xie, *Memory-Dependent Shifts of the Period-Doubling Cascade in the Finite-Memory Grünwald–Letnikov Fractional Logistic Map*, Preprints.org, posted 2026-07-20, https://www.preprints.org/manuscript/202607.1375; *Mathematics* 14(17) (2026), 3032, https://doi.org/10.3390/math14173032.
2. S. Bhalekar and P. M. Gade, *Fractional-Order Periodic Maps: Stability Analysis and Application to the Periodic-2 Limit Cycles in the Nonlinear Systems*, *Journal of Nonlinear Science* 33 (2023), 119; https://arxiv.org/abs/2304.08208 (different full-history formulation).
3. S. E. I. Bouzeraa, R. Bououden, and M. S. Abdelouahab, *Fractional logistic map with fixed memory length*, *International Journal of General Systems* 52 (2023), 653–663, https://doi.org/10.1080/03081079.2023.2201001 (comparison limited to abstract).
4. H.-S. Hou, G.-C. Wu, R. Lozi, and Z.-W. Mo, *Asymptotically period doubling bifurcation of fractional difference equations*, *Mathematics and Computers in Simulation* 240 (2026), 982–999, https://doi.org/10.1016/j.matcom.2025.08.017 (asymptotic rather than finite-memory exact periodic cycles).
