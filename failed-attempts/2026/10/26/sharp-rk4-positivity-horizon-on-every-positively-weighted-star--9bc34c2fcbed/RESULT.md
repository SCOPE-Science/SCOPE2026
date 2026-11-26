# Sharp RK4 positivity horizon on every positively weighted star

## Finding

Let \(m\ge1\) be any integer. On the star with hub \(0\), leaves \(1,\ldots,m\), and **arbitrary positive real** edge conductances \(w_1,\ldots,w_m\), let \(L\) denote the combinatorial weighted Laplacian. Set
\[
A=\sum_{i=1}^{m} w_i,\qquad B=\sum_{i=1}^{m}w_i^2,\qquad C=\sum_{i=1}^{m}w_i^3,\qquad w_* =\max_i w_i.
\]
For a candidate edge weight \(w>0\), define
\[
T_w=A+w,\qquad U_w=A^2+B+Aw+w^2,
\]
\[
V_w=A^3+2AB+C+(A^2+B)w+Aw^2+w^3,
\]
and the cubic
\[
F_w(h)=1-\frac{T_w}{2}h+\frac{U_w}{6}h^2-\frac{V_w}{24}h^3.
\]
The classical four-stage, fourth-order explicit Runge–Kutta endpoint diffusion map is
\[
P(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24}.
\]
**Theorem.** The cubic \(F_{w_*}\) is strictly decreasing for \(h\ge0\) and has a unique positive real root \(H\). For every \(h\ge0\),
\[
\boxed{P(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad0\le h\le H.}
\]
In fact \(H>1/A\), the forward-Euler positivity step bound. At \(h=H\), the only vanishing off-diagonal entries are hub-to-leaf entries corresponding to edges of maximum conductance \(w_*\); all other entries of \(P(H)\) are strictly positive. For every \(h>H\), those maximum-conductance hub-to-leaf entries are negative. If \(w_i>w_j\), then the normalized hub-to-leaf factors satisfy \(F_{w_i}(h)<F_{w_j}(h)\) for every \(h>0\). The theorem includes the two-vertex star \(m=1\).

## Assumptions and scope

All \(m\) conductances are strictly positive and finite real numbers, not necessarily rational, equal, or commensurate. The numerical map refers to the **completed** RK4 step for the linear diffusion equation \(u'=-Lu\), and not to the signs of intermediate stages. Matrix entrywise positivity means a nonnegative map on every nonnegative input vector. As \(L\mathbf1=0\), \(P(h)\mathbf1=\mathbf1\) for all \(h\); thus an entrywise-nonnegative \(P(h)\) is a stochastic matrix. The theorem concerns one complete step, not error bounds, absolute stability, or arbitrary graphs.

## Proof

**1. Exact off-diagonal formulas.** Fix a spoke of weight \(w_i\). Direct multiplication of the star Laplacian gives, for \(k=1,2,3,4\),
\[
(L^k)_{0i}=-w_i\,(1,T_{w_i},U_{w_i},V_{w_i})_k.
\]
Consequently \(P(h)_{0i}=P(h)_{i0}=h w_iF_{w_i}(h)\). For two different leaves \(i\ne j\), put
\[
W_{ij}=A^2+B+A(w_i+w_j)+w_i^2+w_iw_j+w_j^2.
\]
The corresponding matrix entry is
\[
P(h)_{ij}=w_iw_j h^2\left[\frac12-\frac{A+w_i+w_j}{6}h+\frac{W_{ij}}{24}h^2\right].
\]
The bracket is strictly positive for all real \(h\), since its positive leading coefficient and constant term have negative discriminant:
\[
3W_{ij}-(A+w_i+w_j)^2
=2A^2+3B+A(w_i+w_j)+2w_i^2+w_iw_j+2w_j^2>0.
\]
Therefore every leaf-to-leaf off-diagonal entry is positive for every \(h>0\).

**2. Positivity of all diagonal entries.** The Laplacian is real symmetric positive semidefinite. The scalar fourth Taylor polynomial
\[
r_4(-z)=1-z+\frac{z^2}{2}-\frac{z^3}{6}+\frac{z^4}{24}
\]
is strictly positive for \(z\ge0\), because its even-order Taylor remainder gives \(r_4(-z)\ge e^{-z}>0\). By the spectral theorem, \(P(h)\) is positive definite for all \(h\ge0\), so all its diagonal entries are strictly positive.

**3. The heaviest spoke controls every possible sign loss.** The exact difference between two spoke factors is
\[
F_{w_i}(h)-F_{w_j}(h)
=-\frac{(w_i-w_j)h}{2}\left[1-\frac{A+w_i+w_j}{3}h+\frac{W_{ij}}{12}h^2\right].
\]
The bracket is twice the strictly positive leaf-to-leaf bracket from step 1, so \(w_i>w_j\) implies \(F_{w_i}(h)<F_{w_j}(h)\) for all \(h>0\). Thus all off-diagonal signs are controlled by \(F_{w_*}\).

**4. A unique crossing.** To show that **each** \(F_w\) is strictly decreasing on \([0,\infty)\), it suffices to show \(9T_wV_w>4U_w^2\), which makes the quadratic derivative
\[
F'_w(h)=-\frac{T_w}{2}+\frac{U_w}{3}h-\frac{V_w}{8}h^2
\]
negative for all real \(h\). Put \(x=w/A\), \(t=B/A^2\) and \(c=C/A^3\). Because \(0<x\le1\), \(0<t\le1\), \(c>0\), exact expansion yields
\[
\begin{aligned}
\frac{9T_wV_w-4U_w^2}{A^4}={}&9(1+x)c-4t^2+t(x^2+19x+10)\\
&+5x^4+10x^3+6x^2+10x+5>0.
\end{aligned}
\]
Indeed \(10t-4t^2\ge6t>0\) and every other displayed term is nonnegative. Hence \(F_w(0)=1\), \(F_w\) is strictly decreasing, and its negative leading coefficient implies \(F_w(h)\to-\infty\) as \(h\to\infty\), proving existence and uniqueness of its positive zero.

**5. Sharpness and improvement over forward Euler.** Steps 1–4 prove the stated positivity interval and identify the first entries to vanish. For \(0<h\le1/A\), the matrix \(M=I-hL\) is nonnegative and row-stochastic. The exact identity
\[
P(h)=\frac38 I+\frac13 M+\frac14 M^2+\frac1{24}M^4
\]
proves positivity; at \(h=1/A\), every hub-to-leaf entry is strictly positive because \(M_{0i}=w_i/A>0\). Since the leaf-to-leaf and diagonal entries are also strictly positive there, \(F_{w_*}(1/A)>0\). Its unique zero therefore satisfies \(H>1/A\). This completes the proof.

## Verification

Run `python verify.py` with the dependency recorded in `requirements.txt`. The standalone checker performs six direct symbolic identities for three independently weighted spokes, verifies the positivity-polynomial discriminant identity, and checks thousands of exact rational matrix-entry identities with additional numerical sign tests for one through five leaves. It reports `VERIFY_OK 6324 symbolic polynomial and exact rational graph identities, numerical sign spotchecks` when successful. Finite checks corroborate but do not substitute for the proof above. This theorem's real-parameter quantifiers and unique-root statement follow analytically.

## Relationship to prior work

The archival work of Ketcheson, Gottlieb and Macdonald (arXiv:1106.3626v1, 18 June 2011) develops strong-stability-preserving theory for two-step Runge–Kutta methods, including the relationship between forward-Euler restrictions and higher-order methods. Its scope is method design and general SSP inequalities, rather than graph-specific sharp positivity of the **completed classical one-step RK4 stability polynomial**. It neither gives this exact weighted-star cubic nor establishes the maximum-spoke ordering. The 2001 review by Gottlieb, Shu and Tadmor likewise provides general SSP context; a general sufficient timestep condition cannot supply the necessary-and-sufficient weighted-star bound and precise first sign loss. Published related classifications for Radau IIA, Gauss–Legendre Padé and third-order explicit RK maps concern different stability functions or different graph classes and are not used as novelty claims here. Literature searches and the available mathematical-record comparisons did not identify the present classification; this absence is not proof that no equivalent historical result exists.

## Limitations

The bound is for final-stage nonnegativity, not positivity at every intermediate RK4 stage, and says nothing about accuracy, repeated-step global errors, or absolute-stability optimization. The result is for symmetric weighted stars with strictly positive spokes and cannot be transplanted to arbitrary weighted graphs without additional proof. Historical uniqueness has not been independently certified; incompletely indexed specialized literature remains a novelty risk.

## References

1. D. I. Ketcheson, S. Gottlieb and C. B. Macdonald, *Strong Stability Preserving Two-Step Runge–Kutta Methods*, arXiv:1106.3626v1, first posted 18 June 2011, https://arxiv.org/abs/1106.3626 ; SIAM J. Numer. Anal. 49 (2011), 2618–2639, DOI 10.1137/10080960X.
2. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112, DOI 10.1137/S003614450036757X.
