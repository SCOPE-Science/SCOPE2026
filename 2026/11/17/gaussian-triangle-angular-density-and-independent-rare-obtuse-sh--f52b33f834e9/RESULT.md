# Gaussian-triangle angular density and independent rare-obtuse shape fluctuations

## Finding
Let \(A_d,B_d,C_d\) be three independent standard Gaussian points in \(\mathbb R^d\), with integer \(d\ge2\). Let \(\alpha\), \(\beta\), and \(\gamma\) be the angles at \(B_d\), \(C_d\), and \(A_d\), respectively, so that \(\gamma=\pi-\alpha-\beta\). The joint density of the first two angles is
\[
f_d(\alpha,\beta)=\frac{(d-1)2^{d-1}3^{d/2}}{\pi}\,
\frac{[\sin\alpha\sin\beta\sin(\alpha+\beta)]^{d-1}}
{[\sin^2\alpha+\sin^2\beta+\sin^2(\alpha+\beta)]^d},
\qquad \alpha>0,\ \beta>0,\ \alpha+\beta<\pi,
\]
and zero outside this open triangle. This proves the all-dimensional angle-density formula conjectured by Finch (2014); the formula itself was already proposed there.

There is also a joint rare-event shape law. Define the three squared edge lengths
\[
x_d=\|B_d-A_d\|^2,\qquad y_d=\|C_d-A_d\|^2,\qquad z_d=\|B_d-C_d\|^2,
\]
with \(T_d=(x_d+y_d+z_d)/3\). Set
\[
\Delta_d=\frac{z_d-x_d-y_d}{x_d+y_d+z_d},\quad
S_d=\sqrt d\,\frac{x_d-y_d}{x_d+y_d},\quad
V_d=\frac{T_d-2d}{2\sqrt d}.
\]
Conditional on the angle at \(A_d\) being strictly obtuse, as \(d\to\infty\),
\[
\boxed{(d\Delta_d,S_d,V_d)\ \Longrightarrow\ (E,N_1,N_2),}
\]
where \(E\sim\operatorname{Exp}(1)\), \(N_1,N_2\sim N(0,1)\), and **the three limiting variables are mutually independent**. In particular, the angle itself has an exponential boundary layer:
\[
\boxed{d(\gamma-\pi/2)\ \Longrightarrow\ 2E\quad\text{conditional on }\gamma>\pi/2.}
\]
The normalized squared-edge excess, leg imbalance, and total scale therefore fluctuate on distinct scales even after conditioning on an exponentially rare obtuse triangle.

## Assumptions and scope
The Gaussian coordinates are independent and have variance one. A common deterministic translation leaves all conclusions unchanged; a different common isotropic variance leaves the angle and the first two conditional variables unchanged, but the definition of the scale variable \(V_d\) must be adjusted accordingly. The triangle is nondegenerate almost surely for every integer \(d\ge2\). The conditional limit concerns the event that the **specified labelled vertex** \(A_d\) is obtuse; any other specified vertex has the same law by exchangeability. No assertion is made for collinear one-dimensional triangles.

## Proof
**1. The exact angle density.** Set \(X=B_d-A_d\), \(Y=C_d-A_d\), and let
\[
G=\begin{pmatrix}X\cdot X&X\cdot Y\\X\cdot Y&Y\cdot Y\end{pmatrix}.
\]
For each coordinate, \((X_j,Y_j)\) is a centered Gaussian vector with covariance
\(\Sigma=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\). Therefore \(G\) has a two-by-two Wishart distribution with \(d\) degrees of freedom and scale matrix \(\Sigma\). With respect to Lebesgue measure in its three distinct entries, its density on the positive-definite cone is
\[
f_G(G)=\frac{\det(G)^{(d-3)/2}}
{2^d3^{d/2}\Gamma_2(d/2)}
\exp\left[-\frac{G_{11}+G_{22}-G_{12}}3\right],
\quad\Gamma_2(t)=\sqrt\pi\,\Gamma(t)\Gamma(t-1/2).
\]
Writing \(x=\|X\|\), \(y=\|Y\|\), and \(\gamma=\angle(X,Y)\), the change of variables
\(G_{11}=x^2\), \(G_{22}=y^2\), \(G_{12}=xy\cos\gamma\) has absolute Jacobian \(4x^2y^2\sin\gamma\), and \(\det G=x^2y^2\sin^2\gamma\). Thus the density in \((x,y,\gamma)\) is
\[
\frac4{2^d3^{d/2}\Gamma_2(d/2)}
 x^{d-1}y^{d-1}(\sin\gamma)^{d-2}
 \exp[-(x^2+y^2-xy\cos\gamma)/3].
\]

Let \(t>0\) be the common sine-law scale. Since the angles at \(B_d\) and \(C_d\) are \(\alpha\) and \(\beta\),
\[
x=t\sin\beta,\quad y=t\sin\alpha,\quad \gamma=\pi-\alpha-\beta.
\]
The absolute Jacobian from \((t,\alpha,\beta)\) to \((x,y,\gamma)\) is \(t\sin\gamma\). The cosine law gives
\[
x^2+y^2-xy\cos\gamma
=\frac{t^2}2\left(\sin^2\alpha+\sin^2\beta+\sin^2\gamma\right).
\]
Consequently, writing \(Q=\sin^2\alpha+\sin^2\beta+\sin^2\gamma>0\), integrating \(t\) by
\[
\int_0^\infty t^{2d-1}e^{-Qt^2/6}\,dt
=\frac{\Gamma(d)}2\left(\frac6Q\right)^d
\]
yields a constant \(2\,3^{d/2}\Gamma(d)/\Gamma_2(d/2)\). The gamma duplication formula reduces this to \((d-1)2^{d-1}3^{d/2}/\pi\), proving the displayed density. Because all transformations are one-to-one off null boundaries and the Wishart law is a probability density, normalization is exact, not merely numerical.

**2. Exact independent shape coordinates.** Orthogonally diagonalize the covariance by defining
\[
Z=(X+Y)/\sqrt2,\qquad W=(X-Y)/\sqrt2.
\]
Then \(Z\sim N_d(0,3I_d)\) and \(W\sim N_d(0,I_d)\) are independent. Set
\[
U=\|Z\|^2/3,\quad K=\|W\|^2,\quad T=U+K,\quad H=U/T,
\quad J=\frac{Z\cdot W}{\|Z\|\|W\|}.
\]
Here \(U,K\) are independent \(\chi^2_d\). Gamma-beta algebra and rotational invariance show that
\[
H\sim\operatorname{Beta}(d/2,d/2),\quad T\sim\chi^2_{2d},\quad
J\ \text{has the cosine law of two independent uniform sphere directions},
\]
with **\(H,T,J\) mutually independent**. Moreover,
\[
\begin{split}
x_d&=\frac T2[1+2H+2\sqrt{3H(1-H)}\,J],\\
y_d&=\frac T2[1+2H-2\sqrt{3H(1-H)}\,J],\\
z_d&=2T(1-H).
\end{split}
\]
It follows exactly that \(T=T_d\), \(\Delta_d=(1-4H)/3\), and
\[
S_d=\sqrt d\,\frac{2\sqrt{3H(1-H)}}{1+2H}\,J.
\]
The cosine law says \(\gamma>\pi/2\) precisely when \(z_d>x_d+y_d\), equivalent to \(H<1/4\). Thus conditioning on obtuseness changes the law of \(H\) alone; \(T\) and \(J\) retain their independent, unconditional laws.

**3. The boundary layer and joint independence.** Put \(k=d/2\). On \((0,1/4)\) the conditional density of \(H\) is proportional to \([h(1-h)]^{k-1}\). Set \(Y_d=d(1/4-H)\). Since the derivative of \(\log[h(1-h)]\) at \(1/4\) is \(8/3\), the density ratio at \(h=1/4-y/d\) relative to its value at \(1/4\) tends to \(e^{-4y/3}\) for each fixed \(y\ge0\). Concavity of \(\log[h(1-h)]\) gives the uniform exponential upper bound needed to integrate this limit, so
\[
Y_d\mid(H<1/4)\Longrightarrow\operatorname{Exp}(4/3).
\]
As \(d\Delta_d=4Y_d/3\), this gives \(d\Delta_d\Rightarrow\operatorname{Exp}(1)\).

For independent uniform unit vectors in \(\mathbb R^d\), the dot-product \(J\) satisfies \(\sqrt d J\Rightarrow N(0,1)\); indeed, after rotating one direction to the first basis vector, \(J\) has the law of \(G_1/(\sum_{i=1}^dG_i^2)^{1/2}\) for independent standard normal \(G_i\). The usual chi-square central limit theorem gives \((T-2d)/(2\sqrt d)\Rightarrow N(0,1)\). These two quantities are independent of each other and of \(H\), including under the event \(H<1/4\). Finally, the continuous prefactor
\(2\sqrt{3H(1-H)}/(1+2H)\) tends in conditional probability to \(1\), because \(H\to1/4\). Joint convergence and mutual independence follow from these exact finite-dimensional independences and Slutsky's theorem.

For the angle, the cosine law gives
\[
\cos\gamma=-\frac{3T\Delta_d}{2\sqrt{x_dy_d}}.
\]
Under the same conditioning, \(T/d\to2\), \(x_d/d\to3/2\), and \(y_d/d\to3/2\) in probability. Hence \(3T/(2\sqrt{x_dy_d})\to2\). Since \(\gamma-\pi/2=-\arcsin(\cos\gamma)\), and \(d\Delta_d\) is tight, it follows that \(d(\gamma-\pi/2)-2d\Delta_d\to0\) in conditional probability. This proves the exponential angular-excess law.

## Verification
The standalone `verify_angles.py` requires Python 3, NumPy and SciPy and can be run using `python verify_angles.py`. It numerically integrates the exact two-angle density for dimensions \(2,3,4,7\); all four integrals equal \(1\) within \(2\times10^{-11}\). It also checks the one-vertex obtuse integral against the known regularized-beta value \(I_{1/4}(d/2,d/2)\), verifies the exact three-edge factorization on independently generated Gaussian triples in dimensions \(2,5,17\), and compares the exact finite-dimensional conditional deficit tails in dimensions \(20,80,320,1000\) with the predicted exponential limit. These computations are supporting checks; the proof of every dimension and of the limit is analytic.

## Relationship to prior work
Steven Finch explicitly conjectured the all-dimensional formula for the **pure** Gaussian-triangle two-angle density (2014, page 8); the present result proves that stated conjecture rather than originating the formula. Edelman and Strang's account of Gaussian random triangles (2015, Section 3.4) already establishes the beta distribution of one normalized squared side and the associated acute/obtuse probabilities, and mentions Wishart techniques; its Section 3.6 also sketches the angular-density Jacobian for planar triangles. Those established marginal facts are used here, not claimed as new. The separately identified joint conditional exponential–Gaussian–Gaussian shape limit adds information about the correlation structure, the two perpendicular leg fluctuations, and the total size of a rare obtuse triangle.

The earlier Eisenberg–Sullivan paper on random triangles in dimension \(d\) is relevant to historical priority. Its complete text was unavailable for this comparison, and it is **not** claimed to omit these results. More general shape-distribution formulas may imply aspects of the calculation after substantial transformations. No independent priority determination has been made.

## Limitations
Only standard isotropic Gaussian vertices, fixed labels, integer dimensions at least two, and the stated conditional event are treated. The limit theorems are weak convergence, with no quantitative error rates. The all-dimensional angle formula was previously conjectured, and its numerical normalization alone would not be proof. The independent joint limit is distinct from the already-known one-dimensional beta marginal, but unresolved historical overlap remains possible, especially through comprehensive random-triangle shape theories and the unavailable Eisenberg–Sullivan text.

## References
- Steven R. Finch, *Pins, Stakes, Anchors and Gaussian Triangles*, arXiv:1410.6742v1, 24 October 2014, page 8, https://arxiv.org/pdf/1410.6742.
- Alan Edelman and Gilbert Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053v1, 9 January 2015, especially Section 3.4, https://arxiv.org/pdf/1501.03053.
- Bennett Eisenberg and Rosemary Sullivan, *Random Triangles in n Dimensions*, *American Mathematical Monthly* **103** (1996), 308–318, https://doi.org/10.2307/2975187 (full text not inspected).
