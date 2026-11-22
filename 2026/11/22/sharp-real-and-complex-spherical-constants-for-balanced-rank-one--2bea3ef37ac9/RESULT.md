# Sharp real and complex spherical constants for balanced rank-one multiplier norms

## Finding
Let \(\mathbb K\in\{\mathbb R,\mathbb C\}\), let \(d\ge1\), and let \((x_j,f_j)_{j=1}^N\) be a finite family in \(\mathbb K^d\times\mathbb K^d\), not identically zero, such that \(\|x_j\|_2=\|f_j\|_2\) for each \(j\). Define the unconditional rank-one multiplier norm and the two optimal Bessel bounds by
\[
U(x,f)=\max_{|\varepsilon_j|=1}\left\|\sum_{j=1}^N\varepsilon_j\,x_jf_j^*\right\|_{2\to2},\qquad
B_x=\left\|\sum_{j=1}^Nx_jx_j^*\right\|_{2\to2},\quad
B_f=\left\|\sum_{j=1}^Nf_jf_j^*\right\|_{2\to2}.
\]
Here the coefficients \(\varepsilon_j\) range over signs in the real case and unimodular complex numbers in the complex case, and \(x_jf_j^*\) is the rank-one operator \(v\mapsto\langle v,f_j\rangle x_j\). Then the **best possible dimension-dependent constant** in \(\max(B_x,B_f)\le\kappa_{\mathbb K,d}U(x,f)\) is
\[
\boxed{\displaystyle
\kappa_{\mathbb R,d}=\frac{\sqrt\pi\,\Gamma((d+1)/2)}{\Gamma(d/2)},\qquad
\kappa_{\mathbb C,d}=\frac{\Gamma(d+1/2)}{\Gamma(3/2)\Gamma(d)}.}
\]
The inequalities remain sharp when **both** vector families span \(\mathbb K^d\) (so both are frames). For \(d\ge2\), however, the inequality is **strict for every nonzero finite family**. When \(d=1\) equality always holds. The constants grow at different sharp rates:
\[
\kappa_{\mathbb R,d}\sim\sqrt{\frac{\pi d}{2}},\qquad
\kappa_{\mathbb C,d}\sim\frac{2}{\sqrt\pi}\sqrt d.
\]
An explicit real planar extremizing sequence takes \(f_j=e_1\) and
\(x_j=(\cos(\pi j/N),\sin(\pi j/N))\), \(0\le j<N\). For every \(N\ge2\), it has \(B_f=N\) and
\[
U(x,f)=\csc\!\left(\frac{\pi}{2N}\right),\qquad
\frac{B_f}{U(x,f)}=N\sin\!\left(\frac{\pi}{2N}\right)\nearrow\frac\pi2.
\]

## Assumptions and scope
All spaces are the standard Euclidean real or complex Hilbert spaces, and all norms above are operator norms induced by their Hilbert norms. Zero pairs may occur, but at least one pair is nonzero. The pairwise equality of lengths is essential; there is no assumption of equal lengths across distinct indices, no condition-number restriction, no reconstruction identity, and no assumption that either family is tight. The claim compares the original, *unrescaled* Bessel bounds to the unconditional norm, not optimal bounds after coefficient reweighting. Its primary classification is MSC2020 47A30, concerning inequalities for operator norms. The motivating preprint was first made public on 2 December 2022.

## Proof
**1. Phases and a spherical moment.** Taking the operator norm, dualizing by unit vectors, and then optimizing the phases gives the exact identity
\[
U(x,f)=\max_{\|u\|=\|v\|=1}\sum_{j=1}^N
|\langle u,x_j\rangle|\,|\langle v,f_j\rangle|.
\tag{1}
\]
Let \(W\) be uniformly distributed on the unit sphere of \(\mathbb K^d\). Rotational invariance gives \(\mathbb E|\langle W,z\rangle|=\mu_{\mathbb K,d}\|z\|\). The squared first coordinate is beta distributed, with parameters \((1/2,(d-1)/2)\) over \(\mathbb R\) and \((1,d-1)\) over \(\mathbb C\), for \(d\ge2\). Direct beta integration and the trivial \(d=1\) case yield
\[
\mu_{\mathbb R,d}=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\qquad
\mu_{\mathbb C,d}=\frac{\Gamma(3/2)\Gamma(d)}{\Gamma(d+1/2)}.
\tag{2}
\]
Fix a unit vector \(v\) and average (1) with respect to \(u=W\). Using \(\|x_j\|=\|f_j\|\),
\[
U(x,f)\ge\mu_{\mathbb K,d}\sum_j\|f_j\|\,|\langle v,f_j\rangle|
\ge\mu_{\mathbb K,d}\sum_j|\langle v,f_j\rangle|^2.
\]
Taking the supremum over \(v\) yields \(U\ge\mu B_f\). Interchanging the two vector families yields \(U\ge\mu B_x\), establishing both inequalities.

**2. Sharpness, including spanning families.** Fix \(d\) and the scalar field. Let \(x_1,\ldots,x_N\) be unit vectors whose equal-mass empirical measures converge weakly to spherical Haar probability. Such finite sets exist by approximating the Haar integral on successive finite partitions of a compact sphere; alternatively an independent spherical sample supplies them almost surely. For every unit \(u\),
\[
\frac1N\sum_{j=1}^N|\langle u,x_j\rangle|\longrightarrow\mu_{\mathbb K,d}.
\]
The convergence is uniform in \(u\): the functions of \(u\) are uniformly 1-Lipschitz, so a fixed finite net upgrades pointwise convergence to uniform convergence. Put \(f_j=e_1\) for every \(j\). Formula (1) then gives \(U/N\to\mu_{\mathbb K,d}\), while \(B_f=N\). Hence no smaller universal constant than \(1/\mu_{\mathbb K,d}\) works. We may choose the empirical sets to span \(\mathbb K^d\). Replace the last \(d-1\) members of the \(f\)-family by \(e_2,\ldots,e_d\). Both families then span and all pairwise lengths still match. The rank-one multiplier changes, uniformly in the phases, by operator norm at most \(2(d-1)\), while the new \(B_f\) equals \(N-d+1\). The same ratio therefore still tends to \(1/\mu_{\mathbb K,d}\). The construction works for both fields and every dimension.

**3. Strict nonattainment for finite nonzero families.** Suppose \(d\ge2\). Take a unit vector \(v\) attaining \(B_f=\sum_j|\langle v,f_j\rangle|^2>0\), and let \(a_j=|\langle v,f_j\rangle|\). The continuous function
\[
F(u)=\sum_j a_j|\langle u,x_j\rangle|,\qquad \|u\|=1,
\]
is not constant. To prove this, choose \(j_0\) with \(a_{j_0}>0\), and a unit \(u_0\perp x_{j_0}\) not perpendicular to any \(x_j\) with \(a_j>0\) unless \(x_j\) is parallel to \(x_{j_0}\). Such a choice exists because a finite union of proper subspaces cannot cover the orthogonal complement of \(x_{j_0}\) (and in dimension two any nonparallel vector has nonzero projection onto that complement). Along the real great-circle path \(u(t)=\cos(t)u_0+\sin(t)x_{j_0}/\|x_{j_0}\|\), every positive-weight term parallel to \(x_{j_0}\) contributes a positive multiple of \(|\sin t|\), while each other term is differentiable near zero. The resulting derivative jump is strictly positive, so \(F\) cannot be constant. A continuous nonconstant function on the sphere has maximum strictly above its Haar average. Thus, applying (1) with this \(v\),
\[
U(x,f)>\mu_{\mathbb K,d}\sum_ja_j\|x_j\|
\ge\mu_{\mathbb K,d}B_f.
\]
The same reasoning with the roles interchanged gives \(U>\mu B_x\). Hence both bounds are strict for \(d\ge2\). In dimension one, all terms have identical absolute projection for the unique unit direction, so \(U=\sum_j\|x_j\|^2=B_f=B_x\).

**4. An exact planar family.** In the real plane with the explicit vectors in the finding, \(U=\max_\theta\sum_j|\cos(\theta-\pi j/N)|\). Optimizing signs first shows this is the maximum modulus of \(\sum_j\varepsilon_j e^{i\pi j/N}\). At a maximizing direction, signs select precisely \(N\) consecutive roots of unity among the \(2N\)-th roots, one from each antipodal pair. Their geometric sum has modulus \(2/|1-e^{i\pi/N}|=\csc(\pi/(2N))\). Taking \(N\to\infty\) yields the exact planar sharpness limit. Finally Stirling's ratio formula applied to (2) gives the two displayed high-dimensional asymptotics.

## Verification
The accompanying standalone `verify.py` checks the gamma-function constants in low dimensions, the exact planar multiplier formula against complete finite sign enumeration for \(2\le N\le13\), and convergence of the explicit planar sharpness ratios. It uses only the Python standard library. These checks are finite diagnostics and do not establish the arbitrary-dimensional statement; the proof is the spherical average, uniform approximation and nonattainment argument above.

## Relationship to prior work
Balazs, Freeman, Popescu and Speckbacher (first public 2022) study equal-length pairs and prove a bound involving \(27\beta^2\) under a frame-operator conditioning hypothesis; their preprint's Theorem 4.6 and Example 3.2 explicitly concern this unconditional multiplier framework. They do not give the present **unconditional, condition-number-free, exact dimension-dependent constants for unrescaled Bessel bounds**, strict finite nonattainment, or both scalar fields' sharp rates. The earlier results on unconditional constants for ordinary frame expansions by Bemrose, Casazza, Kaftal and Lynch (2014) address reconstruction frame expansions rather than this unrestricted pairwise matched rank-one operator family. The present claim neither resolves the unrestricted rescaling conjecture nor improves the conditioned bound uniformly in dimension; the respective hypotheses and quantities differ.

## Limitations
The constant grows as \(\sqrt d\), hence no finite dimension-free comparison is asserted for unrescaled Bessel bounds. Sharpness is a supremum over finite systems of arbitrarily increasing length, not an attained finite extremum when \(d\ge2\). The result assumes pairwise matched vector lengths, and makes no claim for unequal lengths without renormalization. The precise real and complex constants are supported by a full argument; an unindexed equivalent formula in earlier frame multiplier or absolutely summing operator literature cannot be excluded by searches alone.

## References
1. P. Balazs, D. Freeman, R. Popescu, M. Speckbacher, *Quantitative bounds for unconditional pairs of frames*, arXiv:2212.00947v1, first public 2022-12-02, https://arxiv.org/abs/2212.00947. Later published in *J. Math. Anal. Appl.* 531 (2024), article 127874, https://doi.org/10.1016/j.jmaa.2023.127874.
2. T. Bemrose, P. G. Casazza, V. Kaftal, R. G. Lynch, *The Unconditional Constants for Hilbert Space Frame Expansions*, arXiv:1405.6656, https://arxiv.org/abs/1405.6656 (supporting background).
3. *Mathematics Subject Classification 2020*, code 47A30: norms of linear operators, https://mathscinet.ams.org/msc/msc2020.html?t=47A16.
