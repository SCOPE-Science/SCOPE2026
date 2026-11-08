# Exact centroids and logarithmic edge profiles of two-row Monge polytopes

## Finding

**Theorem (complete two-row centroid law).** For every integer \(q\ge1\), let \(\mathcal M_{2,q}\) be the polytope of all nonnegative real \(2\times q\) matrices \(C=(c_{ij})\) with total entry sum one and satisfying the Monge inequalities
\[
c_{1,j}+c_{2,k}\le c_{1,k}+c_{2,j}\qquad(1\le j<k\le q).
\]
Let \(\bar C\) denote its centroid with respect to uniform relative \((2q-1)\)-dimensional Lebesgue measure, and define the rational numbers
\[
R_{q,j}=\sum_{k=0}^{j-1}\binom qk\int_0^{1/2}u^{q-k-1}(1-u)^k\,du
\qquad(1\le j\le q).
\]
Every entry of the centroid is given explicitly by
\[
\boxed{\quad
\bar c_{1,j}=\frac{\frac12+R_{q,j}}{2q},\qquad
\bar c_{2,j}=\frac{\frac12+R_{q,q+1-j}}{2q}.
\quad}
\]
In particular all centroid coordinates are rational. The top row is strictly increasing from left to right for \(q\ge2\), the bottom row strictly decreasing, and the column totals \(s_j=\bar c_{1,j}+\bar c_{2,j}\) are mirror-symmetric and *strictly discretely convex* for \(q\ge3\):
\[
s_j=s_{q+1-j},\qquad s_j-2s_{j+1}+s_{j+2}>0\quad(1\le j\le q-2).
\]
Thus the least column total is attained at the central column when \(q\) is odd and at exactly the two central columns when \(q\) is even. The two row totals are exactly \(1/2\) each.

Write \(H_q=\sum_{r=1}^q 1/r\). The extreme-right entries have the closed forms
\[
\boxed{\quad
\bar c_{1,q}=\frac{\frac12+H_q-\sum_{r=1}^q 2^{-r}/r}{2q},\qquad
\bar c_{2,q}=\frac{\frac12+2^{-q}/q}{2q}.
\quad}
\]
Consequently
\[
2q\bar c_{1,q}=\log q+\gamma-\log 2+\tfrac12+O(q^{-1}),\quad
2q\bar c_{2,q}=\tfrac12+O(2^{-q}/q),
\]
where \(\gamma\) is Euler's constant. The rightmost top entry therefore carries a logarithmic edge enhancement, while the rightmost bottom entry remains asymptotic to \(1/(4q)\).

More precisely, if \(j_q/q\to u\in(0,1)\), put
\[
Q(u)=\begin{cases}\log(2u),&0<u\le\frac12,\\
-\log(2(1-u)),&\frac12\le u<1.
\end{cases}
\]
Then the full continuum centroid profile is
\[
2q\bar c_{1,j_q}\longrightarrow\frac12+\max\{Q(u),0\},\quad
2q\bar c_{2,j_q}\longrightarrow\frac12+\max\{-Q(u),0\},
\]
and hence \(2qs_{j_q}\to1+|Q(u)|\).

## Assumptions and scope

The matrix orientation is fixed as displayed: indices increase from left to right, and the Monge inequality has the \(\le\) convention. The ambient metric does not affect the centroid because the relative Lebesgue density is constant on the affine hyperplane \(\sum_{ij}c_{ij}=1\). All \(q\ge1\) are included; the strictness assertions only apply in the stated nonvacuous ranges. In the continuum statement, \(u\) is fixed strictly between zero and one, while the endpoint asymptotics are separate. No claim is made for three or more rows.

## Proof

**1. Uniform measure as normalized exponentials.** Take \(2q\) independent rate-one exponential random variables \(E_{ij}\), let \(T=\sum E_{ij}\), and set \(C_{ij}=E_{ij}/T\). Then \(C\) is uniform on the full matrix probability simplex, and \(T\) is independent of \(C\) with \(\mathbb ET=2q\). Put \(X_j=E_{1j}-E_{2j}\). The Monge inequalities are precisely \(X_1\le\cdots\le X_q\), an event depending only on \(C\) (positive scaling cancels). The \(X_j\)'s are independent, identically distributed, and continuous; thus this event has probability \(1/q!\), and conditioning the uniform simplex distribution on it is exactly uniform relative volume on \(\mathcal M_{2,q}\).

**2. Conditional exponential splitting.** Each \(X_j\) has centered Laplace density \(e^{-|x|}/2\). For a single independent exponential pair \((A,B)\), conditional on \(A-B=x\), the smaller exponential is rate two. Therefore
\[
\mathbb E[A\mid A-B=x]=\tfrac12+\max\{x,0\},\qquad
\mathbb E[B\mid A-B=x]=\tfrac12+\max\{-x,0\}.
\]
Under the ordered event, \(X_j\) has the law of the \(j\)-th order statistic \(X_{(j)}\) of \(q\) independent standard Laplace variables. Since \(T\) remains independent of \(C\) and of this conditioning event, \(\mathbb E[E_{ij}\mid\text{Monge}]=2q\,\bar c_{ij}\). Consequently
\[
2q\bar c_{1,j}=\tfrac12+\mathbb E(X_{(j)})_+,\qquad
2q\bar c_{2,j}=\tfrac12+\mathbb E(-X_{(j)})_+.
\]
The symmetry of the Laplace law identifies the second positive-part expectation with \(\mathbb E(X_{(q+1-j)})_+\).

**3. Exact moment integral.** For \(t\ge0\), the Laplace cumulative distribution function is \(F(t)=1-e^{-t}/2\). The event \(X_{(j)}>t\) means at most \(j-1\) observations are at most \(t\). By the tail-integral formula and the substitution \(u=e^{-t}/2\),
\[
\mathbb E(X_{(j)})_+
=\int_0^\infty\sum_{k=0}^{j-1}\binom qk F(t)^k(1-F(t))^{q-k}dt
=R_{q,j}.
\]
Each integrand is polynomial on the rational interval \([0,1/2]\), proving rationality; an explicit rational sum is
\[
R_{q,j}=\sum_{k=0}^{j-1}\sum_{\ell=0}^{k}
\frac{(-1)^\ell\binom qk\binom k\ell}{(q-k+\ell)2^{q-k+\ell}}.
\]
Summing positive parts before taking expectation gives \(\sum_{j=1}^qR_{q,j}=q\,\mathbb E(X_1)_+=q/2\), which proves both row totals.

**4. Strict shape.** Let \(U_{(1)},\ldots,U_{(q)}\) be uniform order statistics and define \(\phi(v)=[F^{-1}(v)]_+\). Thus \(\phi(v)=0\) for \(v\le1/2\), and \(\phi(v)=-\log(2(1-v))\) for \(v>1/2\). We have \(R_{q,j}=\mathbb E\phi(U_{(j)})\). Integrating the order-statistic density once gives, for \(1\le j<q\),
\[
R_{q,j+1}-R_{q,j}=\binom qj\int_0^1\phi'(v)v^j(1-v)^{q-j}dv>0.
\]
The distributional second derivative of \(\phi\) is the positive measure
\[
d\phi''=2\delta_{1/2}+(1-v)^{-2}\mathbf1_{(1/2,1)}(v)\,dv.
\]
Subtracting two successive differences and integrating by parts yields, for \(1\le j\le q-2\),
\[
R_{q,j+2}-2R_{q,j+1}+R_{q,j}
=\frac{\binom qj}{j+1}\int_0^1v^{j+1}(1-v)^{q-j}\,d\phi''(v)>0.
\]
All endpoints vanish: the powers absorb the logarithmic singularity at \(v=1\). Because \(s_j=(1+R_{q,j}+R_{q,q+1-j})/(2q)\), the reversed sum of two strictly convex sequences is strictly convex and symmetric, proving the asserted minimum and strictness.

**5. Edge and bulk asymptotics.** Directly, \(R_{q,1}=2^{-q}/q\), whereas
\[
R_{q,q}=\int_0^{1/2}\frac{1-(1-v)^q}{v}dv
=\sum_{r=1}^q\frac{1-2^{-r}}r.
\]
Since \(H_q=\log q+\gamma+O(q^{-1})\), and \(\sum_{r=1}^\infty2^{-r}/r=\log 2\) with tail \(O(2^{-q}/q)\), the endpoint statements follow.

For \(j_q/q\to u\in(0,1)\), the beta-distributed uniform order statistic \(U_{(j_q)}\) converges to \(u\) in probability. Its logarithmic tails are uniformly square-integrable: for example \(\mathbb E[-\log U_{(j_q)}]=H_q-H_{j_q-1}\) and \(\operatorname{Var}(-\log U_{(j_q)})=\sum_{r=j_q}^q r^{-2}\); the corresponding formulas for \(-\log(1-U_{(j_q)})\) use \(q-j_q+1\) in place of \(j_q\). Both are bounded for an interior limiting rank. As \(|\phi(v)|\) is bounded by a constant plus these logarithmic functions, convergence holds in \(L^1\), so \(R_{q,j_q}\to\phi(u)\). Apply the same argument to the reflected rank to obtain the second row. This proves the continuum profile.

## Verification

The standalone file `verify_centroid.py` uses exact rational arithmetic and the displayed polynomial-integral formula. It independently constructs \(R_{q,j}\) from the adjacent-spacing recurrence, checks both endpoint identities, positivity/normalization, symmetry, strict row monotonicity, and strict convexity of column totals for every \(1\le q\le36\). It also verifies the exact \(q=2\) conditional-Beta centroid and the \(q=3\) matrix. Execute `python3 verify_centroid.py` from the directory containing this file. The recorded execution reported **4036 passing exact-rational assertions**. These bounded calculations are consistency checks; all general assertions rest on the proof above.

## Relationship to prior work

Erickson and Kretschmann (2023), *The structure and normalized volume of Monge polytopes*, establish the face structure and the \(1/q!\) relative-volume formula for two-row Monge polytopes. Erickson and Jones (2026), *A lattice path model for the volume of the Monge polytope*, extend normalized volume and Ehrhart-series computations to arbitrary matrix sizes. Neither of the inspected relevant treatments presents the full coordinate centroid, its strict discrete convexity, or its logarithmic endpoint/continuum profiles. Those centroid statements are not consequences of volume values alone. Searches for ``Monge polytope centroid'', ``barycenter'', ``mean entries'', and equivalents did not identify a covering result. The underlying probability tools (Dirichlet normalization, exponential splitting, order statistics) are standard; the new content is their exact geometric evaluation and the boundary-layer classification for the normalized Monge family. A negative literature search is not a proof of historical uniqueness.

## Limitations

The result is for two-row matrices, with the stated inequality orientation and uniform affine-volume measure. The qualitative centroid profile is not a concentration theorem for a random matrix and says nothing about covariances or arbitrary higher-row Monge polytopes. The continuum limit fixes an interior rank fraction; extreme ranks are covered separately. The available literature comparison does not establish definitive historical priority.

## References

1. William Q. Erickson and Nicholas B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508v1, first submitted September 8, 2026, https://arxiv.org/abs/2609.09508 .
2. William Q. Erickson and Jan Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522v2, first submitted November 13, 2023, https://arxiv.org/abs/2311.07522 .
