# Sharp four-jet phaseless reconstruction of two unequal-width isotropic Gaussian packets

## Finding

Let \(d\ge2\). The Fourier-intensity Taylor jet through order four of an equal-amplitude sum of two unit-mass, isotropic Gaussian densities of **arbitrary strictly positive and possibly unequal variances** determines their unordered variance pair and their two centers up to translation and global reflection. The result holds at all separations, including coincident centers. Orders zero and two are insufficient, so the fourth order is sharp. More strongly, the theorem below characterizes *every realizable pair of quadratic and quartic intensity jets* by an isotropic-plus-rank-one matrix condition and one scalar inequality. In dimension one, the fourth-order jet need not be identifying, even with strictly positive, unequal variances and distinct centers.

## Assumptions and scope

Write \(g_a(x)=(2\pi a)^{-d/2}\exp(-|x|^2/(2a))\) for a centered Gaussian of variance \(a>0\) per coordinate, and set
\[
f(x)=g_a(x-c_1)+g_b(x-c_2),\qquad c_1,c_2\in\mathbb R^d,\quad a,b>0.
\]
Our Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-i\xi\cdot x}\,dx\). The observed intensity is \(I(\xi)=|\widehat f(\xi)|^2\); no phase or first spatial moment is supplied. Unit component masses and isotropy are essential assumptions. Define \(s=(a+b)/2\), \(q=(a-b)/2\), \(h=c_1-c_2\), \(u=|\xi|^2\), and \(v=h\cdot\xi\). Then \(s>0\) and \(|q|<s\). Global translation and reflection \(x\mapsto -x\) are unavoidable ambiguities, and exchanging the two components is not a new mixture.

For a smooth intensity \(I\) near zero, define its quadratic and quartic Taylor data by
\[
Q=-\tfrac12 D^2 I(0),\qquad P_4(\xi)=\tfrac1{24}D^4I(0)[\xi,\xi,\xi,\xi].
\]
This is a quadratic-form matrix \(Q\) and a homogeneous quartic polynomial \(P_4\), with no coordinate normalization ambiguity.

**Exact realizability and reconstruction.** A pair \((Q,P_4)\) arises from the stated model in \(d\ge2\) if and only if the following conditions all hold. Set \(s=\lambda_{\min}(Q)/4\) and \(T=Q-4s\operatorname{Id}\). We require \(s>0\), \(T\succeq0\), \(\operatorname{rank}T\le1\), and a real number \(z\) satisfying \(0\le z<s^2\) such that identically in \(\xi\),
\[
P_4(\xi)=(2s^2+z)|\xi|^4+s|\xi|^2\langle T\xi,\xi\rangle+\tfrac1{12}\langle T\xi,\xi\rangle^2.\tag{1}
\]
Necessarily \(z\) is unique: for any unit \(e\in\ker T\), \(z=P_4(e)-2s^2\). The unordered variances are \(\{s+\sqrt z,s-\sqrt z\}\), while \(T=hh^T\) recovers the center displacement up to sign. The intensity's remaining derivatives through order three are necessarily \(I(0)=4\) and \(DI(0)=D^3I(0)=0\).

## Proof

By the Gaussian Fourier integral,
\[
\widehat f(\xi)=e^{-a|\xi|^2/2-i c_1\cdot\xi}+e^{-b|\xi|^2/2-i c_2\cdot\xi},
\qquad I(\xi)=2e^{-su}(\cosh(qu)+\cos v).\tag{2}
\]
Expanding each entire function to homogeneous degree four gives, with a remainder of order six locally,
\[
I(\xi)=4-4s|\xi|^2-(h\cdot\xi)^2
 +(2s^2+q^2)|\xi|^4+s|\xi|^2(h\cdot\xi)^2
 +\tfrac1{12}(h\cdot\xi)^4+O(|\xi|^6).\tag{3}
\]
Therefore \(Q=4s\operatorname{Id}+hh^T\) and (1) follows with \(z=q^2\). Since \(d\ge2\), \(hh^T\) always has a zero eigenvalue, even if \(h=0\). Thus \(s=\lambda_{\min}(Q)/4\) exactly, and the positive-semidefinite matrix \(T=hh^T\) is known. Any unit vector in its nontrivial kernel gives \(z\) by (1), so \(|q|\), and hence both variances, are determined. The vector \(h\) is determined up to sign by its outer product \(hh^T\), including the zero case. The sign of \(q\) corresponds, after possible exchange of labels, to reflecting the entire two-component mixture, so there is no further ambiguity.

Conversely, suppose the explicit feasibility conditions hold. Choose any \(h\) with \(T=hh^T\), choose \(q=\sqrt z\), take \(a=s+q\), \(b=s-q\), and set \(c_1=h/2\), \(c_2=-h/2\). Strict inequality \(z<s^2\) makes both variances positive. Formula (3) realizes exactly the prescribed \(Q\) and \(P_4\). This also proves the sufficiency of *all* stated conditions, including coincident means and coincident widths.

Sharpness in \(d\ge2\) follows by keeping \(s\) and \(h\) fixed while varying \(q\) with \(|q|<s\): all the zeroth-, first-, second-, and third-order derivatives agree but the fourth-order jet changes by \(q^2|\xi|^4\). Thus no lower derivative order identifies every mixture.

To prove the **one-dimensional boundary** by exact numbers, put \(r=h^2\). The quadratic jet is \(Q=4s+r\), and the quartic coefficient is \(2s^2+q^2+sr+r^2/12\). The two strictly admissible parameter triples
\[
(s,q^2,r)=(2,1/4,1),\qquad (s,q^2,r)=(41/20,47/200,4/5)
\]
both give \(Q=9\) and quartic coefficient \(31/3\), but have different center separations and variance pairs. Both have \(s>0\), \(q^2<s^2\), and \(r>0\); therefore neither is a translated or reflected copy of the other. This establishes failure of fourth-jet injectivity on the line.

## Verification

The standalone `CHECK.py` uses only the Python standard library and exact rational arithmetic. It independently expands the Gaussian amplitude products and trigonometric factors through fourth order along several rational directions, verifies (3) and the reconstruction identities, and checks the two one-dimensional ambiguity triples exactly. Run `python CHECK.py` in the same directory. The proof is symbolic for every dimension and every positive variance; finite checks are supplementary, not infinite proofs.

## Relationship to prior work

Kalavasis, Kothari, Li and Zampetakis (first public January 8, 2026) analyze recovery of high-dimensional mixture parameters using complex Fourier information and sparse Fourier methods. Their main method explicitly excludes Gaussian components; their Gaussian appendix treats local convergence with access to ordinary mixture samples, not intensity-only fourth jets. Xia and Xu (June 18, 2026) study Fourier-magnitude recovery of interval indicators, a distinct structured family. Classical Gaussian-mixture moment identification, including Fukunaga–Flick (1983) and Agostini–Améndola–Ranestad (2020), uses the *original mixture's* moments; a Fourier-intensity jet instead supplies only even moments of the *autocorrelation*, so the stated data and its sign ambiguities differ. No listed theorem entails the explicit full feasible-jet criterion (1) under these assumptions. This literature comparison is not a priority or uniqueness certificate.

## Limitations

The theorem uses two equally weighted Gaussian components of unit mass and scalar positive covariance matrices. It does not address unknown component weights, anisotropic covariances, more components, robust estimation from noisy derivative data, or absolute translation. It proves only that fourth-order intensity data fail to identify *all* one-dimensional mixtures, not that every one-dimensional configuration is ambiguous. The same Gaussian moment equations may have equivalent formulations in older inverse-scattering, autocorrelation or mixture-identifiability literature. The cited 1983 paper was available in abstract form only, and the June 2026 interval preprint's complete manuscript was not inspected.

## References

- A. Kalavasis, P. Kothari, S. Li, M. Zampetakis, *Learning Mixture Models via Efficient High-dimensional Sparse Fourier Transforms*, arXiv:2601.05157, v1 January 8, 2026, https://arxiv.org/abs/2601.05157 . Full HTML v2 was inspected.
- Y. Xia, Z. Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, v1 June 18, 2026, https://arxiv.org/abs/2606.19855 . Abstract inspected.
- K. Fukunaga, T. Flick, *Estimation of the Parameters of a Gaussian Mixture Using the Method of Moments*, IEEE Trans. PAMI 5 (1983), 410–416, DOI:10.1109/TPAMI.1983.4767410 . Abstract inspected.
- D. Agostini, C. Améndola, K. Ranestad, *Moment Identifiability of Homoscedastic Gaussian Mixtures*, Found. Comput. Math. 21 (2021), 695–724, DOI:10.1007/s10208-020-09469-6 . Public article text inspected.
