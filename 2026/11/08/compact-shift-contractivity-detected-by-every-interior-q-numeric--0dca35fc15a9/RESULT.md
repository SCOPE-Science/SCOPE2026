# Compact-shift contractivity detected by every interior \(q\)-numerical radius

## Finding
Let \(S e_j=e_{j+1}\) be the unilateral forward shift on the complex Hilbert space \(H=\ell^2(\mathbb N_0)\), and let \(K\) be any compact complex-linear operator on \(H\). Put \(T=S+K\). For each real \(0<q<1\) set
\[
w_q(T)=\sup\bigl\{|\langle Tx,y\rangle|:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\bigr\}.
\]
Then
\[
\boxed{\quad w_q(T)=1\ \Longleftrightarrow\ \|T\|\le1,\qquad w_q(T)>1\ \Longleftrightarrow\ \|T\|>1.\quad}
\]
The restriction \(q<1\) is sharp. For the weighted shift \(T_t e_0=t e_1\), \(T_t e_j=e_{j+1}\) for \(j\ge1\), one has \(\|T_t\|=t\) when \(t>1\), but
\[
\boxed{\quad w_1(T_t)=1\ \text{for}\ 1<t\le\sqrt2,\qquad w_1(T_t)>1\ \text{for}\ t>\sqrt2.\quad}
\]
Thus every interior overlap parameter detects failure of contractivity for all compact perturbations of the unilateral shift, whereas the classical numerical radius misses an entire noncontractive interval even among rank-one perturbations.

## Assumptions and scope
All spaces and operators are complex. Compactness means norm compactness of the image of the unit ball. The numerical-radius definition uses the convention that the Hilbert product is linear in the first variable, and the prescribed overlap is the positive real number \(q\). The result holds for every compact \(K\), without positivity, self-adjointness, rank, or norm restrictions. The endpoint example concerns only the displayed family of one-edge weighted shifts.

## Proof
**1. Hilbert-space overlap formula.** Fix a unit vector \(x\), put \(a=\langle Tx,x\rangle\), \(b=\|Tx\|\), and \(s=\sqrt{1-q^2}\). Any unit \(y\) with \(\langle x,y\rangle=q\) is of the form \(y=qx+sz\) for a unit \(z\perp x\). Aligning the free phase of \(z\) gives
\[
\sup_{\substack{\|y\|=1\\\langle x,y\rangle=q}}|\langle Tx,y\rangle|
=q|a|+s\sqrt{b^2-|a|^2}.
\tag{1}
\]
In particular, if \(|a|=q\) and \(b>1\), the right side is strictly larger than \(q^2+(1-q^2)=1\).

**2. The universal essential lower bound.** For \(0\le r<1\) and an integer \(N\ge0\), define
\[
\xi_{N,r}=\sqrt{1-r^2}\sum_{j=0}^{\infty}r^j e_{N+j}.
\]
These are unit vectors, and \(\langle S\xi_{N,r},\xi_{N,r}\rangle=r\). As \(N\to\infty\), \(\xi_{N,r}\rightharpoonup0\) and \(\|K\xi_{N,r}\|\to0\). For \(r=q\), take \(y=S\xi_{N,q}\); then \(\langle\xi_{N,q},y\rangle=q\) and
\[
|\langle T\xi_{N,q},y\rangle|\longrightarrow1.
\]
Hence \(w_q(T)\ge1\) for every compact \(K\). The elementary inequality \(w_q(T)\le\|T\|\) now yields \(w_q(T)=1\) whenever \(\|T\|\le1\).

**3. Detecting any norm inflation.** Suppose \(\|T\|>1\). By density, choose a finitely supported unit vector \(v\) with \(b_0=\|Tv\|>1\); write \(a_0=\langle Tv,v\rangle\). Choose \(0<\delta<1\) so small that
\[
\delta|a_0|<q,\qquad \delta(1+|a_0|)<1-q.
\]
Then choose \(R\) with \(q<R<1\) sufficiently close to one that
\[
(1-\delta)R-\delta|a_0|>q.
\tag{2}
\]
Let \(Q_N\) denote projection onto coordinates numbered at least \(N\). Compactness implies \(\|KQ_N\|\to0\), since \(K^*\) is compact and \(Q_NK^*\to0\) in norm. Uniformly in \(0\le r\le R\), the unit vectors \(\xi_{N,r}\in Q_NH\) satisfy
\[
\|K\xi_{N,r}\|\to0,\quad
\langle Tv,\xi_{N,r}\rangle\to0,\quad
\langle Tv,T\xi_{N,r}\rangle\to0.
\tag{3}
\]
The latter two limits follow because the tail of any fixed Hilbert vector tends to zero, and \(T\xi_{N,r}=S\xi_{N,r}+K\xi_{N,r}\). For \(N\) larger than the support of \(v\), define
\[
x_{N,r}=\sqrt{\delta}\,v+\sqrt{1-\delta}\,\xi_{N,r},
\qquad \|x_{N,r}\|=1.
\]
Using (3) and \(\langle S\xi_{N,r},\xi_{N,r}\rangle=r\), uniformly on the compact interval \([0,R]\),
\[
\begin{aligned}
\langle Tx_{N,r},x_{N,r}\rangle&=\delta a_0+(1-\delta)r+o_N(1),\\
\|Tx_{N,r}\|^2&=\delta b_0^2+1-\delta+o_N(1).
\end{aligned}
\tag{4}
\]
By (2) and the first inequality in the choice of \(\delta\), for all sufficiently large \(N\), the continuous map \(r\mapsto|\langle Tx_{N,r},x_{N,r}\rangle|\) takes a value below \(q\) at \(r=0\) and above \(q\) at \(r=R\). Some \(r_N\in(0,R)\) therefore has modulus exactly \(q\). The second identity in (4) ensures \(\|Tx_{N,r_N}\|>1\), because \(b_0>1\). Formula (1) gives \(w_q(T)>1\). This proves both equivalences.

**4. Sharp failure at the classical endpoint.** For \(t>1\), the one-edge shift \(T_t\) is \(S+(t-1)e_1\otimes e_0^*\), a rank-one perturbation, with \(\|T_t\|=t\). For every \(x=(x_j)\in H\), the exact identity
\[
\|x\|^2-\operatorname{Re}\langle T_tx,x\rangle
=\frac12\sum_{j\ge1}|x_{j+1}-x_j|^2
+|x_0|^2+\frac12|x_1|^2-t\operatorname{Re}(x_0\overline{x_1})
\tag{5}
\]
holds by telescoping. The final quadratic form is positive semidefinite exactly for \(t\le\sqrt2\). For those \(t\), \(\operatorname{Re}\langle T_tx,x\rangle\le\|x\|^2\) for every \(x\); the same holds after arbitrary complex phase alignment because the diagonal unitary \(U_\theta e_j=e^{ij\theta}e_j\) conjugates \(T_t\) to \(e^{-i\theta}T_t\). Thus \(w_1(T_t)\le1\), and the essential-tail argument gives equality. If \(t>\sqrt2\), choose \(x_0=(t/2)x_1\ne0\) and \(x_j=r^{j-1}x_1\) for \(j\ge1\). As \(r\uparrow1\), the gradient term in (5), divided by \(|x_1|^2\), tends to zero while the remaining quadratic form equals \(1/2-t^2/4<0\). Hence \(\operatorname{Re}\langle T_tx,x\rangle>\|x\|^2\) for \(r\) sufficiently close to one. Normalizing yields \(w_1(T_t)>1\).

## Verification
The proof is analytical and covers all complex compact perturbations, not only finite-rank ones. The attached `verify.py` independently evaluates the fixed-vector overlap formula on explicit geometric weighted-shift witnesses at multiple \(q\)-parameters and excess weights; it also checks the exact quadratic-form decomposition (5) for rational finite vectors. Finite tests are diagnostics, not an exhaustive verification of compact operators. The argument uses no unproved spectral-theoretic conjecture.

## Relationship to prior work
Kaunisto–O'Loughlin–Virtanen (2026) study unitary dilation and complete spectral-set constants under containment of the **scaled** set \(\Omega_q(T)=q^{-1}W_q(T)\) in the unit disk; this does not yield the present **unscaled** threshold \(w_q(S+K)=1\), since the normalizations and geometric hypotheses differ. Patra–Roy (2024) give general numerical-radius bounds and operator-matrix calculations, not this compact-shift contraction criterion. Chien–Nakazato (2007) study periodic weighted shifts, while the shift perturbations considered here can be arbitrary compact operators, including non-shifts. Earlier work on ordinary numerical radii of one-edge shifts supplies overlapping endpoint geometry; only the interior-parameter, all-compact-perturbation equivalence is claimed as the principal new conclusion. See review for access qualifications.

## Limitations
The assertion is **not** made for \(q=0\), for arbitrary operators with essential norm one, for general essentially unitary operators, or for Banach-space spatial numerical ranges. The endpoint calculation concerns exactly the one-edge family. An older article on \(q\)-numerical radii of periodic weighted shifts was accessible by abstract but not in complete text; the possibility of differently formulated stronger coverage remains a publication-priority risk. Same-model proof and literature review do not constitute independent verification.

## References
1. M. Kaunisto, R. O'Loughlin, J. Virtanen, *Dilation Theory for Scaled \(q\)-Numerical Ranges*, arXiv:2610.00443 (version 1 submitted 2026-09-30 UTC). https://arxiv.org/abs/2610.00443
2. A. Patra and F. Roy, *On the Estimation of \(q\)-Numerical Radius of Hilbert Space Operators*, 2024, publicly available article.
3. M.-T. Chien and H. Nakazato, *The \(q\)-numerical radius of weighted shift operators with periodic weights*, Linear Algebra Appl. (2007), DOI: 10.1016/j.laa.2006.09.017.
4. M.-T. Chien and H. Nakazato, *Perturbation of \(q\)-numerical radius of a weighted shift operator*, J. Math. Anal. Appl. 345 (2008), 954–963.
5. M. H. M. Rashid, *New Properties and Refined Bounds for the \(q\)-Numerical Range*, arXiv:2512.13719 (2025).
