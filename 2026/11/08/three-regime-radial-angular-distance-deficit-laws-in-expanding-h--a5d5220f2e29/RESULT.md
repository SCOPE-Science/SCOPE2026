# Three-regime radial–angular distance-deficit laws in expanding hyperbolic balls

## Finding

Fix an integer dimension \(d\ge3\), a parameter \(\alpha>0\), and curvature \(-1\). The hyperbolic distance \(D_R\) between two independent isotropic random points in a radius-\(R\) ball, with radial density
\[
q_{\alpha,R}(r)=\frac{\alpha\sinh(\alpha r)}{\cosh(\alpha R)-1}\mathbf1_{[0,R]}(r),
\]
has a nondegenerate distance deficit \(T_R=2R-D_R\). Put \(a=(d-1)/2\) and write \(\mathrm B\) for the Euler beta function. Then
\[
T_R\ \Longrightarrow\ W_{\alpha,d}=E_1+E_2-\log B,
\]
where the independent variables \(E_1,E_2\) have exponential law of rate \(\alpha\) and \(B\sim\mathrm{Beta}(a,a)\). For all \(s\ge0\),
\[
\mathbb E e^{-sW_{\alpha,d}}=\left(\frac{\alpha}{\alpha+s}\right)^2\frac{\mathrm B(a+s,a)}{\mathrm B(a,a)}.
\]
As \(t\to\infty\), three distinct, sharp upper-tail regimes occur:
\[
\Pr(W_{\alpha,d}>t)\sim
\begin{cases}
\displaystyle\frac{\alpha\mathrm B(a-\alpha,a)}{\mathrm B(a,a)}\,t e^{-\alpha t},&0<\alpha<a,\\[5pt]
\displaystyle\frac{a}{2\mathrm B(a,a)}\,t^2e^{-at},&\alpha=a,\\[5pt]
\displaystyle\frac1{a\mathrm B(a,a)}\left(\frac{\alpha}{\alpha-a}\right)^2e^{-at},&\alpha>a.
\end{cases}
\]
The radial model includes the usual isotropic hyperbolic graph sampling when \(d=2\); the higher-dimensional statement and its exact angular term are the focus here. If instead both points are uniform with respect to true hyperbolic volume in the ball, the same limit holds with \(\alpha=d-1\). Thus for all such volume-uniform samples the angular-dominated regime applies.

For odd hyperbolic dimension \(d=2k+1\), \(k\ge1\), the volume-uniform limiting law has the stronger phase-type identity
\[
W_{2k,2k+1}\ \stackrel{\mathrm{law}}=\ E'_{2k}+E''_{2k}+\sum_{j=k}^{2k-1}E_j,
\]
all displayed exponentials being independent, the subscript denoting their rate. Hence its mean equals \(1/k+\sum_{j=k}^{2k-1}1/j\), and its variance equals \(1/(2k^2)+\sum_{j=k}^{2k-1}1/j^2\). In dimension three,
\[
\Pr(W_{2,3}>t)=4e^{-t}-(3+2t)e^{-2t}\qquad(t\ge0).
\]

## Assumptions and scope

Let \(\mathbb H^d\) be real hyperbolic space of sectional curvature \(-1\), with fixed origin. Given radius \(R\), choose independently a direction uniform on \(S^{d-1}\) and a radius \(r\in[0,R]\) with the stated density, twice independently. Their intrinsic geodesic distance is \(D_R\), and the geometric triangle inequality yields \(0\le D_R\le2R\). The distribution of \(T_R\) is claimed in the successive limits first \(R\to\infty\) at fixed \(d,\alpha\), then \(t\to\infty\) for the limiting law. The actual-volume measure has radial density proportional to \(\sinh^{d-1}r\), **not** \(q_{d-1,R}\) at finite radius; only their limiting boundary defects coincide. All auxiliary variables in the stated distribution are mutually independent.

## Proof

**1. Radial boundary layer.** Write \(X_R=R-r\) for a sampled radius. For \(0\le u\le R\), its exact survival function is
\[
\Pr(X_R>u)=\frac{\cosh(\alpha(R-u))-1}{\cosh(\alpha R)-1}
=e^{-\alpha u}\left(\frac{1-e^{-\alpha(R-u)}}{1-e^{-\alpha R}}\right)^2.
\]
This converges to \(e^{-\alpha u}\), and is at most \(e^{-\alpha u}\). Thus \(X_R\) converges to an exponential of rate \(\alpha\), with a uniform exponential-tail domination. For the true hyperbolic volume density, \(X_R\) instead has survival ratio \(\int_0^{R-u}\sinh^{d-1}v\,dv/\int_0^R\sinh^{d-1}v\,dv\to e^{-(d-1)u}\), by the large-\(v\) asymptotic \(\sinh^{d-1}v\sim 2^{-(d-1)}e^{(d-1)v}\).

**2. Angular factor and distance.** For independent uniform directions \(U,V\in S^{d-1}\), the quantity \(B=(1-U\cdot V)/2\) has density \(b^{a-1}(1-b)^{a-1}/\mathrm B(a,a)\) on \((0,1)\). It is independent of the two radii. The exact hyperbolic cosine formula is
\[
\cosh D_R=(1-B)\cosh(r_1-r_2)+B\cosh(r_1+r_2).
\]
Joint convergence of \(X_{R,1},X_{R,2}\) and the fixed angular \(B\) implies \(r_1,r_2\to\infty\) in probability, while \(B>0\) almost surely. Therefore \(D_R-r_1-r_2-\log B\to0\) in probability: indeed divide the displayed identity by \(e^{r_1+r_2}/2\), use \(\cosh(r_1+r_2)\sim e^{r_1+r_2}/2\) and \(\cosh(r_1-r_2)/e^{r_1+r_2}\to0\), then use \(\operatorname{arcosh}u=\log(2u)+o(1)\). The continuous-mapping theorem proves the distributional limit. It also proves the stated version for true volume-uniform radii. Since \(e^{D_R}\ge\cosh D_R\ge Be^{r_1+r_2}/2\), one has
\[
0\le T_R\le X_{R,1}+X_{R,2}-\log B+\log2.
\]
The stochastic exponential domination therefore gives uniform integrability of \(e^{\beta T_R}\) for \(0\le\beta<\min(\alpha,a)\) in the prescribed radial model; convergence of each such exponential moment follows. This is not a uniform-in-radius claim at the boundary exponent.

**3. Transform and regime constants.** Set \(Y=E_1+E_2\) and \(Z=-\log B\). Independence gives the stated beta-ratio Laplace transform. The variable \(Y\) has Erlang(shape two, rate \(\alpha\)) survival \(e^{-\alpha t}(1+\alpha t)\). The density of \(Z\) is
\[
f_Z(z)=\frac{e^{-az}(1-e^{-z})^{a-1}}{\mathrm B(a,a)},\quad z>0,
\]
so \(\Pr(Z>t)\sim e^{-at}/(a\mathrm B(a,a))\). The exact decomposition
\[
\Pr(Y+Z>t)=\Pr(Z>t)+e^{-\alpha t}\int_0^t e^{\alpha z}(1+\alpha(t-z))f_Z(z)\,dz
\]
gives the cases. If \(\alpha<a\), the tilted integral's first term is \(\alpha t\mathbb E e^{\alpha Z}\) to leading order and \(\mathbb E e^{\alpha Z}=\mathrm B(a-\alpha,a)/\mathrm B(a,a)\). If \(\alpha=a\), then \(e^{az}f_Z(z)\to1/\mathrm B(a,a)\), yielding the leading integral \(at^2/(2\mathrm B(a,a))\). If \(\alpha>a\), condition on \(Y\) instead, use the tail of \(Z\), and obtain its coefficient times \(\mathbb E e^{aY}=(\alpha/(\alpha-a))^2\). In this last case, splitting \(Y\le (1-\delta)t\) and the complementary event, with small fixed \(\delta>0\), and exponential domination justifies passage through the expectation.

**4. Exact odd-dimensional phase-type factorization.** For \(d=2k+1\), the beta ratio telescopes:
\[
\frac{\mathrm B(k+s,k)}{\mathrm B(k,k)}=\prod_{j=k}^{2k-1}\frac{j}{j+s}.
\]
The Laplace transform of each independent rate-\(j\) exponential is \(j/(j+s)\); multiplication with two rate-\(2k\) radial factors proves the distributional factorization by uniqueness of Laplace transforms. Moment and dimension-three survival formulas follow by convolution or partial fractions.

## Verification

The accompanying self-contained checker `checker.py` uses numerical integration and direct hyperbolic-cosine geometry to test the transform, the odd-dimensional factorization, the complete dimension-three survival law, and tail constants. With fixed seed it tested 85,000 independent geometrically generated point pairs in each of five parameter settings (425,000 total), including both sides and the critical point of the phase threshold. It additionally checked analytic Laplace-product equalities in dimensions 3, 5, 7, 9, and asymptotic coefficients in dimensions 3 and 5. The observed marker was `HYPERBOLIC_RADIAL_ANGULAR_TAIL_PHASES_OK 85000 5`. The proof above, not the simulations, establishes the infinite-dimensional parameter statements and successive limits.

## Relationship to prior work

Krioukov et al. (arXiv:1006.5169v1, June 2010) introduced the two-dimensional hyperbolic network setting and a large-radius metric approximation. Gugelmann, Panagiotou, and Peter (arXiv:1205.1470v1, May 2012) rigorously studied its radial law and graph degree/clustering. Alanis-Lobato and Andrade-Navarro (2016, DOI below), especially their Sections 2–4 and equations (6)–(10), derived an **approximate two-dimensional pair-distance density** and already treated the \(\alpha=1/2\) critical case. Their paper explicitly identifies extension to arbitrary hyperbolic dimension as future work. Consequently no priority is asserted for the two-dimensional radial convolution or the existence of a critical threshold itself. The present mathematical statement retains the exact sine-based angle law, proves the limiting distribution from the exact hyperbolic distance, works in every fixed higher dimension, obtains sharp three-regime constants, and identifies finite independent-exponential decompositions for odd-dimensional volume-uniform balls.

Budel et al. (arXiv:2010.12303v1, October 2020; published 2024), Sections II–V, study random hyperbolic graphs of arbitrary dimension and their degree and clustering regimes. Their general radial/angular formulas are compatible with the setup; their analyzed outcomes are network observables rather than this exact distance-deficit limit, its three tail coefficients, or the odd-dimensional independent-exponential law. These general setup formulas alone do not assert the present limit theorem. Related results on hyperbolic network graph distance (shortest paths through graph edges) concern a different metric observable than the ambient hyperbolic geodesic distance here.

## Limitations

This is an unvalidated mathematical research claim: independent audit is not performed and the literature comparison does not establish absolute historical priority. The primary new higher-dimensional phenomenon can be derived using a relatively short combination of known radial boundary asymptotics, spherical beta laws, and classical convolution; a yet-unidentified general theorem may already imply it. The \(d=2\) approximation and qualitative critical behavior belong to existing literature. The claimed tail regimes concern the limiting \(W_{\alpha,d}\) only, and must not be applied uniformly to finite-radius \(T_R\). In particular \(\alpha=d-1\) applies to volume-uniform sampling *asymptotically*, not to its exact finite-radius radial density. The computation is a numerical consistency check, not an independent proof.

## References

1. D. Krioukov, F. Papadopoulos, M. Kitsak, A. Vahdat, and M. Boguñá, *Hyperbolic Geometry of Complex Networks*, arXiv:1006.5169v1 (public 2010-06-26); https://arxiv.org/abs/1006.5169 .
2. L. Gugelmann, K. Panagiotou, and U. Peter, *Random Hyperbolic Graphs: Degree Sequence and Clustering*, arXiv:1205.1470v1 (public 2012-05-07); https://arxiv.org/abs/1205.1470 .
3. G. Alanis-Lobato and M. A. Andrade-Navarro, *Distance Distribution between Complex Network Nodes in Hyperbolic Space*, Complex Systems 25 (2016), 223–236, DOI:10.25088/ComplexSystems.25.3.223 ; https://content.wolfram.com/sites/13/2018/02/25-3-3.pdf .
4. G. Budel, M. Kitsak, R. Aldecoa, K. Zuev, and D. Krioukov, *Random hyperbolic graphs in \(d+1\) dimensions*, arXiv:2010.12303v1 (public 2020-10-23), Physical Review E 109 (2024) 054131; https://arxiv.org/abs/2010.12303 .
