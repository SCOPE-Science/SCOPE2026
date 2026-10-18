# Two-sided cusp law for local p-Laplacian periodic responses
## Finding
Consider the vector \(p\)-Laplacian Duffing system
\[
(\Phi_p(u'))'_j+\varepsilon\left(\sum_{k=1}^n a_{jk}u'_k+g_j(u_j)\right)=\varepsilon e_j(t),
\qquad 1\le j\le n,
\]
with \(p>2\), \(\Phi_p(\xi)=|\xi|^{p-2}\xi\), and \(g_j(s)=b_js^3+c_js^2+d_js\), under the hypotheses of Proposition 3.1 of Mawhin--Novoa. Let \(\alpha\in\mathbb R^n\) be a nondegenerate zero of the averaged equation \(\bar e_j-g_j(\alpha_j)=0\), and set
\[
\gamma=\frac1{p-1},
\qquad
w=\mathcal K(e-\bar e),
\]
where \(\mathcal K\) is the zero-mean periodic inverse constructed in the source.

For every selection of local periodic solutions \(u_\varepsilon\) in the fixed neighborhood supplied by the source for all sufficiently small \(0<|\varepsilon|\),
\[
u_\varepsilon
=
\alpha+\operatorname{sgn}(\varepsilon)|\varepsilon|^\gamma w
+o(|\varepsilon|^\gamma)
\quad\text{in }C_T^1(\mathbb R^n)
\]
as \(\varepsilon\to0\) through either sign. In particular, if \(e-\bar e\not\equiv0\), then \(w\neq0\) and
\[
\frac{\|u_\varepsilon-\alpha\|_{C^1}}{|\varepsilon|^\gamma}
\longrightarrow
\|w\|_{C^1}>0,
\]
while
\[
\left\|\frac{u_\varepsilon-\alpha}{\varepsilon}\right\|_{C^1}
\longrightarrow\infty.
\]
Thus the local response has an unavoidable two-sided odd cusp of exact displacement order \(|\varepsilon|^{1/(p-1)}\) at the unperturbed state; no local solution selection can extend differentiably through \(\varepsilon=0\) when the forcing has a nonzero oscillatory part.

## Assumptions and scope
The claim uses exactly the vector \(p\)-Laplacian Duffing setting of Proposition 3.1 of arXiv:2610.02155v1. The exponent satisfies \(0<\gamma<1\) because \(p>2\). The averaged zero \(\alpha\) is required to be nondegenerate, meaning \(g_j'(\alpha_j)\neq0\) for every component. The conclusion concerns any choice of the local solutions whose existence is supplied in the fixed neighborhoods used in the degree argument. It does not assert uniqueness of those solutions for each nonzero parameter.

The nondifferentiability conclusion additionally assumes \(e-\bar e\not\equiv0\). If the forcing is constant, then the displayed leading profile vanishes and this argument does not determine the first nonzero parameter scale.

## Proof
Write each local solution as \(u_\varepsilon=a_\varepsilon+v_\varepsilon\), where \(a_\varepsilon=Pu_\varepsilon\in\mathbb R^n\) is the mean and \(v_\varepsilon=(I-P)u_\varepsilon\) has zero mean. The source proves that local solutions satisfy the exact complementary equation
\[
v_\varepsilon
=
\mathcal K\!\left(\varepsilon(I-Q)N(u_\varepsilon)\right).
\]
Its periodic inverse obeys the exact homogeneity law
\[
\mathcal K(\lambda h)
=
\operatorname{sgn}(\lambda)|\lambda|^\gamma\mathcal K(h)
\]
for every real \(\lambda\), with \(\gamma=1/(p-1)\). The compactness argument in the proof of the nonlinear averaging theorem shows that every local solution chosen in the fixed neighborhood converges to \(\alpha\) as \(\varepsilon\to0\). Hence continuity of \(N\) and \(\mathcal K\) gives
\[
\frac{v_\varepsilon}{\operatorname{sgn}(\varepsilon)|\varepsilon|^\gamma}
=
\mathcal K\!\left((I-Q)N(u_\varepsilon)\right)
\longrightarrow
\mathcal K(e-\bar e)=w.
\]
This establishes the two-sided leading term for the zero-mean component.

It remains to control the mean component. The source solves the averaged compatibility equation by a \(C^1\) map \(a=A(v)\) near \(v=0\). In this application the averaged equation has no explicit parameter dependence. Its derivative at the origin satisfies
\[
D_vA(0)
=-F'(\alpha)^{-1}D_x(QN)(\alpha)|_{X_2}.
\]
The source also computes
\[
D_x(QN)(\alpha)w=0.
\]
Therefore \(D_vA(0)w=0\). Since
\[
v_\varepsilon
=
\operatorname{sgn}(\varepsilon)|\varepsilon|^\gamma w
+o(|\varepsilon|^\gamma),
\]
the first-order expansion of \(A\) yields
\[
a_\varepsilon-\alpha=o(|\varepsilon|^\gamma).
\]
Adding mean and zero-mean parts proves the displayed two-sided asymptotic formula.

If \(e-\bar e\not\equiv0\), then \(w\neq0\): indeed the source constructs \(\mathcal K\) so that \(M\mathcal K h=h\), and therefore \(\mathcal K h=0\) would force \(h=0\). Norm continuity now gives
\[
\|u_\varepsilon-\alpha\|_{C^1}
=
|\varepsilon|^\gamma\bigl(\|w\|_{C^1}+o(1)\bigr).
\]
Finally, because \(\gamma-1<0\), division by \(\varepsilon\) gives
\[
\left\|\frac{u_\varepsilon-\alpha}{\varepsilon}\right\|_{C^1}
=
|\varepsilon|^{\gamma-1}\bigl(\|w\|_{C^1}+o(1)\bigr)
\longrightarrow\infty.
\]
Thus no finite derivative at \(\varepsilon=0\) is possible.

## Verification
The argument uses only exact identities and local limits from the source. The sign in the negative-parameter asymptotic is forced by the exact odd homogeneity of \(\mathcal K\), not by extrapolation from positive-parameter numerics. The mean correction is smaller than \(|\varepsilon|^\gamma\) because the derivative of the averaged solution map annihilates the leading profile. The nonzero-profile condition is verified by the right-inverse identity \(M\mathcal K h=h\).

No finite experiment is used as an infinite proof. No uniqueness of the degree-produced periodic solution is assumed. The assertion is uniform over arbitrary selections from the local solution sets because the source's compactness argument forces every such local solution to converge to the same averaged zero as the parameter tends to zero.

## Relationship to prior work
Mawhin and Novoa prove existence for both signs \(0<|\varepsilon|\), construct the exact homogeneous inverse \(\mathcal K\), and state the leading profile only for \(\varepsilon\to0^+\). Their text emphasizes that the \(p\)-Laplacian inverse is not differentiable at the origin, but it does not state the two-sided solution-profile law or the resulting impossibility of a differentiable parameter continuation for nonconstant forcing.

Their companion paper arXiv:2610.02156v1 obtains unique \(C^1\) local branches by an implicit-function method under differentiability and invertibility assumptions on the complementary inverse. It explicitly notes that those assumptions exclude the \(p\)-Laplacian whenever \(p\neq2\), so it does not imply the present cusp law.

Classical periodic \(p\)-Laplacian literature, including Manásevich--Mawhin's 1998 existence theory and later degree/bifurcation results, supplies broad existence and multiplicity results but the checked material did not locate this parameter-normalized two-sided asymptotic or its differentiability obstruction.

A prior finding for the same 2026 source determines a second-order positive-parameter drift of the mean component. That statement neither implies nor is implied by the present two-sided first-order profile: the earlier result concerns the \(O(\varepsilon^{2\gamma})\) averaged displacement for \(\varepsilon>0\), whereas the present claim concerns the sign-sensitive \(O(|\varepsilon|^\gamma)\) full profile and the parameter-regularity boundary across \(\varepsilon=0\).

## Limitations
The theorem gives an exact leading scale and a nondifferentiability obstruction at the parameter origin, not uniqueness or global continuation of periodic solutions. It does not determine how different local selections separate at orders smaller than \(|\varepsilon|^\gamma\). It also does not cover the constant-forcing case \(e-\bar e\equiv0\), the linear case \(p=2\), or the regime \(1<p<2\).

Older \(p\)-Laplacian bifurcation literature is extensive, and an equivalent two-sided cusp statement could exist under different normalization or continuation terminology. The closest checked sources did not expose such a statement; this remains a bibliographic risk rather than a mathematical uncertainty in the proof above.

## References
1. J. Mawhin and J. Novoa, *An abstract averaging method for quasilinear equations*, arXiv:2610.02155v1, first submitted 2026-10-01.
2. J. Mawhin and J. Novoa, *An averaging method for periodic solutions of quasilinear equations in Banach spaces*, arXiv:2610.02156v1, first submitted 2026-10-01.
3. R. Manásevich and J. Mawhin, *Periodic solutions for nonlinear systems with \(p\)-Laplacian-like operators*, Journal of Differential Equations 145 (1998), 367--393, DOI 10.1006/jdeq.1998.3425.
4. P. Benevieri and G. Feltrin, *Atypical bifurcation for periodic solutions of \(\phi\)-Laplacian systems*, Proceedings of the Royal Society of Edinburgh Section A, published online 2025-09-03.
