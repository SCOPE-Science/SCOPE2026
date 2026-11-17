# Quartic-Weibull eccentricity of the midpoint-smoothed random cyclic polygon

## Finding

Let \(n\ge3\), and independently sample \(n\) points uniformly by arclength on the unit Euclidean circle. List them counterclockwise in increasing polar angle as \(z_j=\exp(2\pi iU_{(j)})\), where \(U_{(1)}<\cdots<U_{(n)}\) are the order statistics of independent \(\operatorname{Unif}(0,1)\) variables. Put \(q_j=\exp(2\pi i j/n)\) and define the first pair of discrete Fourier coefficients
\[
 A_n=\frac1n\sum_{j=1}^n z_j\overline{q_j},\qquad
 B_n=\frac1n\sum_{j=1}^n z_jq_j.
\]
The *principal-harmonic envelope* of the iterated-midpoint polygon is the centered curve
\[
 \mathcal E_n=\{A_ne^{it}+B_ne^{-it}:0\le t<2\pi\}.
\]
Almost surely it is a noncircular, nondegenerate ellipse. Write its major and minor semiaxes as \(a_n\ge b_n>0\), its usual geometric eccentricity as \(e_n=(1-b_n^2/a_n^2)^{1/2}\), and its unoriented major-axis angle as \(\Theta_n\in[0,\pi)\). Then
\[
 a_n=|A_n|+|B_n|,\qquad b_n=\big||A_n|-|B_n|\big|,
\]
\[
 \sqrt n\left(1-\frac{b_n}{a_n}\right)\ \Longrightarrow\ H,
 \qquad \Pr(H\le x)=1-e^{-x^2}\quad(x\ge0),
\]
\[
 n^{1/4}e_n\ \Longrightarrow\ E,
 \qquad \Pr(E\le x)=1-e^{-x^4/4}\quad(x\ge0).
\]
For every finite \(n\ge3\), \(\Theta_n\) is exactly uniform on \([0,\pi)\) and independent of the two semiaxes; hence the two displayed limiting laws hold jointly with an independent uniform direction. In particular, the smoothed ellipse tends to a circle in semiaxis ratio, but its *geometric eccentricity* vanishes at the slower, sharp order \(n^{-1/4}\).

## Assumptions and scope

The sampling law is independent normalized arclength on a single Euclidean circle, with vertices arranged by cyclic order before iteration. The midpoint operator on complex polygon coordinates is \((Tz)_j=(z_j+z_{j+1})/2\), with cyclic indices. This theorem uses a *single global scale* after centering, not separate Euclidean normalizations of the horizontal and vertical coordinate vectors. For each fixed \(n\), the spectral envelope is defined by the dominant Fourier pair; the probability limits then take \(n\to\infty\). No simultaneous uniform assertion in iteration count and sample size is made. The principal-harmonic envelope is a continuum ellipse; the actual normalized polygon has \(n\) vertices near an affine-regular \(n\)-gon inscribed in that ellipse, not a Hausdorff limit to the full ellipse at fixed \(n\).

## Proof

**1. Deterministic envelope.** Set \(m_n=n^{-1}\sum_j z_j\). Every discrete Fourier mode \(q_j^r\) is an eigenvector of \(T\) with eigenvalue
\[
 \lambda_r=\tfrac12(1+e^{2\pi ir/n})=e^{\pi ir/n}\cos(\pi r/n).
\]
After removal of the constant mode, the two modes indexed \(r=1,-1\) have maximal modulus \(c_n=\cos(\pi/n)>0\), strictly larger than that of any remaining mode (there are no remaining modes when \(n=3\)). Their coefficients are exactly \(A_n,B_n\). Thus for every fixed \(n\), uniformly in vertex index \(j\),
\[
 c_n^{-k}\bigl(T^k(z-m_n)\bigr)_j
 =A_ne^{i(2\pi j/n+k\pi/n)}
 +B_ne^{-i(2\pi j/n+k\pi/n)}+o(1)
 \quad(k\to\infty).
\]
The error even decays geometrically when higher modes occur. Writing \(A_n=\alpha e^{iu}, B_n=\beta e^{iv}\) and shifting the ellipse parameter gives
\[
 A_ne^{it}+B_ne^{-it}
 =e^{i(u+v)/2}\big((\alpha+\beta)\cos s+i(\alpha-\beta)\sin s\big),
\]
which establishes the semiaxis formulas. Exceptional zero or degenerate Fourier coefficients are zero sets of nontrivial real-analytic functions on the sampling simplex and thus have probability zero: a regular polygon gives \(A_n=1,B_n=0\), while small non-regular perturbations give \(B_n\ne0\).

**2. Random Fourier fluctuation.** Write \(D_{n,j}=U_{(j)}-j/n\). The standard functional central limit theorem for the uniform empirical quantile process gives, with stepwise interpolation,
\[
 \bigl(\sqrt nD_{n,\lceil nt\rceil}\bigr)_{0\le t\le1}
 \Longrightarrow (-\mathbb B(t))_{0\le t\le1}
\]
in the uniform topology, where \(\mathbb B\) is a standard real Brownian bridge. In particular \(\max_j|D_{n,j}|=O_{\mathsf P}(n^{-1/2})\). Uniform Taylor expansion gives
\[
 e^{2\pi iU_{(j)}}=q_j\bigl(1+2\pi iD_{n,j}+O(D_{n,j}^2)\bigr).
\]
Since \(n^{-1}\sum_jq_j^2=0\) for every \(n\ge3\), the quadratic remainder contributes \(o_{\mathsf P}(1)\) after multiplying \(B_n\) by \(\sqrt n\). Riemann-sum convergence and the continuous-mapping theorem yield
\[
 \sqrt nB_n\Longrightarrow
 -2\pi i\int_0^1e^{4\pi it}\mathbb B(t)\,dt
 =\frac12\int_0^1e^{4\pi it}\,dW(t)=:G,
\]
where \(W\) is standard real Brownian motion and \(\mathbb B(t)=W(t)-tW(1)\). The integration-by-parts identity uses the bridge's zero endpoints and \(\int_0^1e^{4\pi it}dt=0\). Its real and imaginary parts are independent centered normals with variance \(1/8\), since \(\int_0^1\cos^2(4\pi t)dt=\int_0^1\sin^2(4\pi t)dt=1/2\) and their cross integral vanishes. Consequently
\[
 \Pr(|G|>r)=e^{-4r^2}\quad(r\ge0).
\]
The same expansion with \(\overline{q_j}\) gives \(A_n=1+O_{\mathsf P}(n^{-1/2})\). In particular the event \(|A_n|>|B_n|\) has probability tending to one, and on that event
\[
 \sqrt n(1-b_n/a_n)=\frac{2\sqrt n|B_n|}{|A_n|+|B_n|}\Longrightarrow2|G|.
\]
Its distribution is \(\Pr(2|G|\le x)=1-e^{-x^2}\). Finally
\[
 e_n^2=1-\left(\frac{1-r_n}{1+r_n}\right)^2
 =\frac{4r_n}{(1+r_n)^2},\qquad r_n=|B_n|/|A_n|,
\]
on the same high-probability event. Therefore \(n^{1/4}e_n\Longrightarrow2\sqrt{|G|}\), with \(\Pr(2\sqrt{|G|}\le x)=1-e^{-x^4/4}\). These are full distributional limits, not conclusions from finite simulations.

**3. Exact direction independence.** Rotation of the original sample by \(\delta\) may cyclically relabel its sorted vertices, say by \(s\). The new coefficients are \(A'_n=e^{i\delta}e^{2\pi is/n}A_n\) and \(B'_n=e^{i\delta}e^{-2\pi is/n}B_n\), so \(\mathcal E'_n=e^{i\delta}\mathcal E_n\) as unparameterized sets. The semiaxes are unchanged, and \(\Theta'_n=\Theta_n+\delta\pmod\pi\). The input distribution is invariant under every \(\delta\), so conditional on any semiaxis-measurable event, the angle has a translation-invariant probability law on \(\mathbb R/\pi\mathbb Z\), necessarily uniform. This also proves the asserted joint independence and convergence.

## Verification

Run `python checker.py` with NumPy installed. The checker compares the complex Fourier ellipse against an independent real-matrix singular-value decomposition, verifies midpoint iteration against its dominant spectral approximation, and simulates independent cyclic samples for \(n=64,256,512\). The numerical CDFs approach \(1-e^{-x^2}\); an angular Fourier-moment diagnostic checks the exact rotation symmetry. All assertions passed in the recorded execution. The checker is corroborative and is not a proof of the infinite-sample statement.

## Relationship to prior work

Elmachtoub and Van Loan (2010) established the deterministic midpoint-to-ellipse mechanism for an independently normalized pair of Cartesian coordinate vectors. VandeBogert (2016) analyzed weighted barycentric versions and their deterministic Fourier spectra. Kostadinov (2016) independently described the principal harmonic pair for *globally* normalized complex polygonal coordinates and its deterministic elliptical envelope. These establish the spectral setting (not claimed as new); the present statement concerns a precisely specified probability model with counterclockwise-ordered circle-uniform vertices, an explicitly evaluated Gaussian fluctuation and the resulting quartic-Weibull geometric eccentricity. The uniform-angle conclusion follows from rotational equivariance, not a new deterministic spectral theorem. Standard weak convergence of the uniform quantile process supplies the stochastic ingredient. The claims are not equivalent to a statement about arbitrarily generated fixed polygons or separately renormalized Cartesian coordinates.

## Limitations

The result treats one global normalization of midpoint smoothing and uniform circular arclength sampling only. It makes no claim for general vertex distributions or higher dimensions, no total-variation convergence of the asymptotic eccentricity law, and no uniform exchange of the large-iteration and large-vertex limits. Full text of Kostadinov's 2016 article was not retrievable from the available open repository during comparison, so possible historical overlap remains a priority risk. No independent mathematical audit has been completed.

## References

1. A. N. Elmachtoub and C. F. Van Loan, *From Random Polygon to Ellipse: An Eigenanalysis*, SIAM Review **52** (2010), 151–170, DOI: 10.1137/090746707 (published February 5, 2010).
2. K. VandeBogert, *Random Polygon to Ellipse: A Generalization*, arXiv:1606.08888v1, June 26, 2016. Full HTML: https://arxiv.org/html/1606.08888v1.
3. B. Kostadinov, *Limiting Forms of Iterated Circular Convolutions of Planar Polygons*, first available in CUNY Academic Works August 12, 2016; DOI: 10.1007/s40819-016-0224-1; https://academicworks.cuny.edu/ny_pubs/84/.
4. M. Csörgő, *Quantile Processes with Statistical Applications*, CBMS-NSF Regional Conference Series, 1983, Chapter 3 (uniform quantile weak approximations), DOI: 10.1137/1.9781611970289.ch3.
