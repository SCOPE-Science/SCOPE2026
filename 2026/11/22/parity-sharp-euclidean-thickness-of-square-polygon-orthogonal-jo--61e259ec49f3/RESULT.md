# Parity-sharp Euclidean thickness of square–polygon orthogonal joins

## Finding

Let \(E,F\subset\mathbb R^4\) be orthogonal two-dimensional linear subspaces. In \(E\) let \(R_4\) be a regular square of circumradius one, centred at the origin, and in \(F\) let \(R_q\) be a regular \(q\)-gon of circumradius one, also centred at the origin, with integer \(q\ge3\). Define the four-dimensional convex body
\[
P_q=\operatorname{conv}(R_4\cup R_q).
\]
For its **ordinary Euclidean minimum width**, set
\[
\operatorname{th}(P_q)=\min_{\|u\|_2=1}\bigl(h_{P_q}(u)+h_{P_q}(-u)\bigr),\qquad
h_K(u)=\max_{x\in K}\langle u,x\rangle.
\]
Put
\[
\gamma_q=\begin{cases}
\cos(\pi/q),&q\text{ even},\\
\cos(\pi/(2q)),&q\text{ odd}.
\end{cases}
\]
Then, for every \(q\ge3\),
\[
\boxed{\operatorname{th}(P_q)=\frac{2\gamma_q}{\sqrt{1+2\gamma_q^2}}.}
\]

The complete equality set consists of exactly \(2q\) **unoriented normal lines** when \(q\) is even and \(4q\) such lines when \(q\) is odd. To specify them, write \(a=1/\sqrt2\); let \(\xi\in E\) be any of the four unit outward edge normals of the square. For even \(q\), let \(\eta\in F\) range over the \(q\) unit outward edge normals of the \(q\)-gon. For odd \(q\), let \(\eta\) range over the \(2q\) unit directions that lie at angular distance \(\pi/(2q)\) clockwise or counterclockwise from a polygon vertex radius. All, and only, the minimizing **unit** normals are
\[
\boxed{u=\frac{\gamma_q\xi+a\eta}{\sqrt{\gamma_q^2+a^2}}.}
\]
This parametrization produces \(4q\) oriented normals when \(q\) is even and \(8q\) when \(q\) is odd; opposite normals determine the same line.

The (unrestricted-centre) Euclidean inradius is
\[
r(P_q)=\frac{\cos(\pi/q)}{\sqrt{1+2\cos^2(\pi/q)}}.
\]
Consequently \(\operatorname{th}(P_q)=2r(P_q)\) for every even \(q\), but \(\operatorname{th}(P_q)>2r(P_q)\) for every odd \(q\). The odd-parity excess has the sharp asymptotic law
\[
\operatorname{th}(P_q)-2r(P_q)=\frac{\pi^2}{4\sqrt3\,q^2}+O(q^{-4}),\qquad q\to\infty\text{ through odd integers}.
\]
In both parities the width tends to \(2/\sqrt3\), but the convergence deficits differ by a factor of four:
\[
\frac2{\sqrt3}-\operatorname{th}(P_q)=
\begin{cases}
\frac{\pi^2}{3\sqrt3\,q^2}+O(q^{-4}),&q\text{ even},\\
\frac{\pi^2}{12\sqrt3\,q^2}+O(q^{-4}),&q\text{ odd}.
\end{cases}
\]
For the square–pentagon four-polytope singled out by the recent nine-vertex maximum-volume theorem, this gives
\[
\boxed{\operatorname{th}(P_5)=\sqrt{\frac{20+2\sqrt5}{19}}=1.134904029214\ldots,}
\]
with exactly twenty unoriented minimizing lines.

## Assumptions and scope

Both factors have circumradius exactly one, are regular, are centred at the shared origin, and span orthogonal two-planes. The ambient Euclidean metric is the standard one, and the width is over **all real unit normals**, not lattice normals or only facet normals. No assertion is made for nonregular polygons, nonorthogonal joins, unequal radii, or an arbitrary nine-vertex four-polytope.

## Proof

**1. Reduction to directional support values.** Any unit \(u\in\mathbb R^4\) can be written \(u=r\xi+s\eta\) with \(r,s\ge0\), \(r^2+s^2=1\), and unit \(\xi\in E\), \(\eta\in F\); at a zero component its unit direction is arbitrary. The support function of a convex hull is the maximum of its constituents' support functions. Thus if \(a_\xi=h_{R_4}(\xi)=h_{R_4}(-\xi)\) and \(b=h_{R_q}(\eta)\), \(c=h_{R_q}(-\eta)\),
\[
w_{P_q}(u)=\max(a_\xi r,bs)+\max(a_\xi r,cs).\tag{1}
\]
The square is centrally symmetric and \(a_\xi\ge a=\cos(\pi/4)=1/\sqrt2\), with equality exactly for its four outward edge normals. For \(r>0\), the right-hand side of (1) is nondecreasing in \(a_\xi\), and the global optimum described below occurs with \(r,s>0\); hence an optimum exists with \(a_\xi=a\). Its equality classification follows by strictness in the relevant positive components.

**2. The one-variable minimax lemma.** Suppose \(0<m\le M\), and set \(b=m,c=M\) in (1). For \(s>0\) write \(\alpha=ar/s\); then \(r=\alpha/\sqrt{a^2+\alpha^2}\), \(s=a/\sqrt{a^2+\alpha^2}\), and
\[
W(\alpha)=\frac{a\bigl(\max(\alpha,m)+\max(\alpha,M)\bigr)}{\sqrt{a^2+\alpha^2}}.
\]
For \(0\le\alpha\le m\) this is strictly decreasing; for \(\alpha\ge M\) it is strictly increasing. On \([m,M]\), its derivative has the sign of \(a^2-\alpha M\), so any interior stationary point is a maximum, not a minimum. The boundary \(s=0\) gives \(2a\) and cannot improve the value at \(\alpha=M\). Therefore
\[
\min_{r^2+s^2=1} w_{P_q}(r\xi+s\eta)
=\min\left\{\frac{a(m+M)}{\sqrt{a^2+m^2}},
\frac{2aM}{\sqrt{a^2+M^2}}\right\}.\tag{2}
\]
If \(m=M\), equality is possible only at \(\alpha=m=M\), namely \(ar=ms\).

**3. Even polygon.** When \(q\) is even, \(R_q\) is centrally symmetric, so \(b=c\) and \(b\ge c_q=\cos(\pi/q)\); equality occurs exactly at the \(q\) outward edge normals. By (2), the optimized width is \(2ab/\sqrt{a^2+b^2}\). This is strictly increasing in both positive \(a\) and \(b\), and yields the displayed formula with \(\gamma_q=c_q\). It also proves the full equality-normal description and the count \(4q/2=2q\) unoriented lines.

**4. Odd polygon.** Let \(q\ge3\) be odd and write \(\delta=\pi/q\). By the dihedral symmetry of the regular polygon and by swapping \(u\) and \(-u\), it suffices to consider an angle \(0\le\theta\le\delta/2\) from a vertex radius. The larger and smaller opposite support values are then, respectively,
\[
M(\theta)=\cos\theta,\qquad m(\theta)=\cos(\delta-\theta).
\]
Both are positive, \(m\le M\), and
\[
mM=\tfrac12\bigl(\cos\delta+\cos(\delta-2\theta)\bigr)
\ge\cos\delta\ge\tfrac12=a^2.\tag{3}
\]
The two candidate expressions from (2) are
\[
F_m(\theta)=\frac{a(m+M)}{\sqrt{a^2+m^2}},\qquad
F_M(\theta)=\frac{2aM}{\sqrt{a^2+M^2}}.
\]
The second decreases strictly on \((0,\delta/2)\), since \(M'= -\sin\theta<0\) and \(2aM/\sqrt{a^2+M^2}\) increases with \(M>0\). For the first,
\[
F_m'(\theta)=\frac{a\{m'(a^2-mM)+M'(a^2+m^2)\}}{(a^2+m^2)^{3/2}}\le0,
\]
with strict negativity for \(0<\theta<\delta/2\) by (3), \(m'=\sin(\delta-\theta)>0\) and \(M'<0\). Both candidates are therefore uniquely minimized at \(\theta=\delta/2\), where \(m=M=\beta=\cos(\pi/(2q))\). Formula (2) becomes \(2a\beta/\sqrt{a^2+\beta^2}\), the asserted odd formula. Precisely \(2q\) oriented polygon directions attain \(m=M=\beta\); combining these with the four square edge normals yields \(8q\) oriented unit directions or \(4q\) unoriented lines. At every minimum \(r,s>0\), so no zero-block or off-edge square directions are hidden.

**5. Inradius and asymptotics.** For the concentric insphere, minimize \(h_{P_q}(u)=\max(ra_\xi,sb)\). The two independently minimized factor supports are \(a\) and \(c_q=\cos(\pi/q)\), giving radius \(ac_q/\sqrt{a^2+c_q^2}=c_q/\sqrt{1+2c_q^2}\). Rotations by \(\pi/2\) in \(E\) and \(2\pi/q\) in \(F\) are symmetries of \(P_q\) with common fixed-point set \(\{0\}\). Averaging any admissible ball centre over these finite rotations yields the origin without decreasing the radius, proving that this is the unrestricted Euclidean inradius. Because \(\gamma_q>c_q\) for odd \(q\) and \(z\mapsto2z/\sqrt{1+2z^2}\) is strictly increasing for positive \(z\), the strict odd gap follows. Taylor expansion at \(z=1\), where the derivative is \(2/(3\sqrt3)\), yields all stated \(q^{-2}\) coefficients and \(O(q^{-4})\) remainders. For \(q=5\), the exact identity \(\cos^2(\pi/10)=(5+\sqrt5)/8\) yields the stated radical. \(\square\)

## Verification

The proof above is an all-integer-\(q\) analytic argument. The attached Python-standard-library program `check.py` separately evaluates the original vertex support functions, constructs the predicted equality normals, and performs deterministic pseudorandom directional lower-bound spot checks for each integer \(3\le q\le30\) (4,000 samples per \(q\)). It also compares the \(q=5\) value with its radical form. All checks passed in the saved package. These finite tests support the formulas but are not the proof of global optimality or completeness of directions; those rest on Steps 1–5.

## Relationship to prior work

Medgyes's 2026 nine-vertex volume-maximization theorem identifies \(P_5\) (up to orthogonal motion) as the unique maximizer of four-volume among inscribed nine-vertex four-polytopes. The cited paper defines and proves that volume result for the orthogonal polygon join; its accessible full text does not give an ordinary minimum-width formula or a complete set of minimizing width normals for the square–polygon family. Standard convex support-function identities provide equation (1), but the even/odd global equality classification is the result of the optimized scalar and angular arguments above. Related published records for polygon joins concern normal-cone selection probabilities and spherical nearest-vertex gaps, not the antipodally paired support sum \(h(u)+h(-u)\). Search coverage cannot certify absence from all prior literature; the priority assessment is provisional.

## Limitations

The theorem concerns minimum Euclidean width, not minimum lattice width, and is restricted to exactly orthogonal, centred, equal-circumradius regular polygon factors. Widths under anisotropic scaling or nonorthogonal perturbation are not classified. It gives no new global nine-vertex volume-maximization theorem. Historical novelty remains subject to review, especially if an unlocated general free-sum thickness result implies this classification. No independent mathematical audit has been conducted.

## References

1. Csaba Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1 (first submitted 6 November 2026), Sections 2.4, 5, and 7, https://arxiv.org/abs/2611.10078.
2. *On Convex Bodies that are Characterizable by Volume Function*, 2020, Section 2.2 (standard support and directional-width identities), https://link.springer.com/article/10.1007/s40598-020-00132-0.
