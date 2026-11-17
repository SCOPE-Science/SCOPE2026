# Sharp path-variation instability of centered Euclidean group soft thresholding

## Finding

For an integer \(n\ge2\), let \(\bar x=n^{-1}\sum_{i=1}^n x_i\), let \(\mathbf1\) be the constant vector, and write \(Qx=x-\bar x\mathbf1\). For \(\lambda\ge0\), define the centered group-shrinkage operator
\[
T_\lambda(x)=\bar x\mathbf1+\left(1-\frac{\lambda}{\|Qx\|_2}\right)_+Qx,
\]
where the second term is zero if \(Qx=0\). Let \(V(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|\). Its exact two-input Lipschitz coefficient on the quotient by constants is
\[
\boxed{\sup_{V(x-y)>0}\frac{V(T_\lambda(x)-T_\lambda(y))}{V(x-y)}=
\begin{cases}
1,&\lambda=0\text{ or }n=2,\\[3pt]
\dfrac{1+\sqrt{(4n-6)\lfloor n^2/4\rfloor/n}}{2},&\lambda>0,\ n\ge3.
\end{cases}}
\]
For \(\lambda>0\) and \(n\ge3\), the displayed supremum is **not attained** by any distinct finite inputs with nonzero difference variation; an explicit family approaches it. For \(n=2\) the coefficient is attained. At \(\lambda=0\) the operator is the identity and the coefficient is attained. Thus the coefficient jumps at zero penalty for every \(n\ge3\), and for fixed positive penalty its dimension dependence is \(n/2+1/8+O(1/n)\).

## Assumptions and scope

All coordinates and inputs are real. The underlying graph is the unweighted, nonperiodic path of length \(n\), with its \(n-1\) adjacent edges. The Euclidean norm has no factor \(1/n\) in its normalization, and the common scalar threshold is any \(\lambda\ge0\). The map is equivalently the unique minimizer of
\[
\frac12\|z-x\|_2^2+\lambda\|Qz\|_2
\]
with respect to \(z\in\mathbb R^n\). It preserves means and constant translations, and is nonexpansive in Euclidean norm. The theorem concerns **differences between two filtered signals** in path total variation, not the one-input inequality \(V(T_\lambda x)\le V(x)\), which also holds.

## Proof

**1. Proximal formula and derivative.** Orthogonally splitting \(z\) into its mean and centered component reduces the objective to scalar least squares in the mean and the Euclidean-norm proximal problem in \(\mathbf1^\perp\). The optimal mean equals \(\bar x\), and radial minimization gives the stated formula. Set \(r=\|Qx\|_2\) and, for \(r>\lambda>0\), \(u=Qx/r\), \(a=1-\lambda/r\). Then \(\|u\|_2=1\), \(u\perp\mathbf1\), and
\[
DT_\lambda(x)=P_{\mathbf1}+aQ+(1-a)uu^{\mathsf T},
\]
where \(P_{\mathbf1}x=\bar x\mathbf1\). Since \(V\) ignores constants, for all perturbations \(h\),
\[
V(DT_\lambda(x)h)\le aV(h)+(1-a)V(uu^{\mathsf T}h).
\]
For \(r<\lambda\), the map is locally constant modulo constants. The map is Lipschitz and hence absolutely continuous on line segments; threshold crossings have measure zero unless the centered segment is constant, which gives zero difference variation. Therefore its two-input variation modulus is bounded by the larger of one and the supremum of the rank-one variation norms over unit centered vectors. Conversely, derivatives as \(r\downarrow\lambda\) approach \(uu^{\mathsf T}\) modulo constants, so the rank-one supremum is a lower bound for the nonlinear coefficient for every \(\lambda>0\).

**2. Exactly evaluating the rank-one supremum.** Write \((Dh)_j=h_{j+1}-h_j\), so \(V(h)=\|Dh\|_1\). For any mean-zero \(u\) and any \(j\in\{1,\ldots,n-1\}\), let \(h^{(j)}\) be zero on the first \(j\) positions and one thereafter, and put \(b_j=Qh^{(j)}\). Since the path differences freely parameterize the quotient by constants,
\[
\sup_{V(h)\le1}|u^{\mathsf T}h|=\max_j|u^{\mathsf T}b_j|.
\]
Also \(V(u)=\max_{\varepsilon\in\{-1,1\}^{n-1}}\varepsilon^{\mathsf T}Du\). Hence the rank-one supremum equals
\[
\max_{\substack{j,\ \varepsilon\in\{-1,1\}^{n-1}}}
\max_{\substack{\|u\|_2=1\\u\perp\mathbf1}}
\left|\langle D^{\mathsf T}\varepsilon,u\rangle\langle b_j,u\rangle\right|.
\]
For arbitrary real Hilbert-space vectors \(a,b\), the exact maximum over unit \(u\) of \(|\langle a,u\rangle\langle b,u\rangle|\) is
\[
\frac{\|a\|_2\|b\|_2+|\langle a,b\rangle|}{2}.
\]
Indeed this is the spectral radius of \((ab^{\mathsf T}+ba^{\mathsf T})/2\), whose two possibly nonzero eigenvalues are \((\langle a,b\rangle\pm\|a\|_2\|b\|_2)/2\). In the present setting both vectors lie in \(\mathbf1^\perp\). Directly,
\[
\langle D^{\mathsf T}\varepsilon,b_j\rangle=\varepsilon_j,
\qquad \|b_j\|_2^2=\frac{j(n-j)}{n},
\]
and
\[
\|D^{\mathsf T}\varepsilon\|_2^2
=2+\sum_{i=1}^{n-2}(\varepsilon_i-\varepsilon_{i+1})^2\le4n-6.
\]
The last bound is an equality for alternating signs. All \(j\) permit the same alternating maximizing signs and satisfy \(|\varepsilon_j|=1\), and \(j(n-j)\) is maximal for a central cut. Consequently the rank-one supremum is exactly
\[
C_n=\frac{1+\sqrt{(4n-6)\lfloor n^2/4\rfloor/n}}2.
\]
It equals one at \(n=2\) and strictly exceeds one for every \(n\ge3\). The derivative bound and line integration now give the sharp upper bound; boundary derivatives establish the matching lower bound.

**3. Constructive sharpness and nonattainment.** Choose \(j=\lfloor n/2\rfloor\), an alternating sign vector \(\varepsilon\) with \(\varepsilon_j=1\), set \(a=D^{\mathsf T}\varepsilon\), \(b=b_j\), and define
\[
u=\frac{a/\|a\|_2+b/\|b\|_2}{\|a/\|a\|_2+b/\|b\|_2\|_2}.
\]
The rank-one norm \(V(u)|\langle u,h^{(j)}\rangle|\) is exactly \(C_n\). For a positive threshold \(\lambda\), take \(x=\lambda u\) and \(y=x+\delta h^{(j)}\). As \(\delta\downarrow0\), the right directional derivative of the centered radial shrinker at \(x\), in the chosen direction, is \(u\langle u,h^{(j)}\rangle\) modulo constants. The variation quotient therefore tends to \(C_n\). This is a limit of finite data and is not an equality assertion at any positive \(\delta\).

For \(n\ge3\), \(C_n>1\). At every differentiability point with \(r>\lambda\), the preceding upper bound is at most \(a+(1-a)C_n<C_n\); at points with \(r<\lambda\), the quotient derivative is zero. Integrating along any nonconstant centered input segment gives **strictly** less than \(C_n V(x-y)\), since the sphere \(\|Qx\|_2=\lambda\) meets a nonconstant straight line at no more than two points. Thus no finite pair attains \(C_n\). For \(n=2\), two inputs of the same centered sign, each beyond the threshold, have identical centered increments before and after shrinkage and attain coefficient one. For \(\lambda=0\), the map is identity. The asymptotic expansion follows by substituting \(\lfloor n^2/4\rfloor\) for each parity into the formula.

## Verification

Run the complete, standard-library-only `VERIFY.py` using `python VERIFY.py`. The script independently enumerates every sign chamber at dimensions \(2\) through \(10\), checks the explicit rank-one norming vectors for dimensions \(2\) through \(100\), performs \(7{,}540\) seeded two-input tests, and checks boundary-direction limits in the same dimensions for three positive thresholds. All checks passed in the packaged run. The finite checks test the arithmetic and geometry but do not replace the all-dimension proof above.

## Relationship to prior work

Yuan and Lin (first public publication 21 December 2005) introduced grouped-variable regularization. Friedman, Hastie and Tibshirani (arXiv:1001.0736, 5 January 2010), section 2, derive the standard orthonormal-group shrinkage expression. Argyriou, Micchelli, Pontil, Shen and Xu (arXiv:1104.1436, 7 April 2011), section 2, equation (2.4), give the Euclidean proximal shrinker in full generality. Chambolle and Pock (*Acta Numerica*, first published online 23 May 2016), sections 2 and 3, distinguish group sparsity, image variation and Hilbertian nonexpansivity. These sources support the operator and analytic context; none of the materially inspected discussions supplies the exact path-variation coefficient, the nonattainment classification or the penalty-zero discontinuity. The first source was accessible as publication metadata and abstract, not an inspected entire paper, so no whole-document noncoverage claim is made for it. The present computation concerns a different norm and a precise mean-preserving proximal choice, rather than reproducing the known Euclidean nonexpansivity theorem.

## Limitations

The statement applies only to a single global centered Euclidean group, equally weighted observations, ordinary nonperiodic adjacent path variation, and one proximal step. A change to cyclic variation, vertex masses, multiple blocks, other convex penalties or a different contrast normalization requires a separate analysis. The exact coefficient need not be attained when it is sharp, and finite tests alone do not establish historical priority. Although the relevant source comparison was specific, priority against inaccessible or unindexed earlier work cannot be certified from the examined material.

## References

1. M. Yuan and Y. Lin, *Model selection and estimation in regression with grouped variables*, Journal of the Royal Statistical Society Series B 68 (2006), 49–67; first published 21 December 2005. https://doi.org/10.1111/j.1467-9868.2005.00532.x
2. J. Friedman, T. Hastie and R. Tibshirani, *A note on the group lasso and a sparse group lasso*, arXiv:1001.0736, submitted 5 January 2010. https://arxiv.org/abs/1001.0736
3. A. Argyriou, C. A. Micchelli, M. Pontil, L. Shen and Y. Xu, *Efficient First Order Methods for Linear Composite Regularizers*, arXiv:1104.1436, submitted 7 April 2011. https://arxiv.org/abs/1104.1436
4. A. Chambolle and T. Pock, *An introduction to continuous optimization for imaging*, Acta Numerica 25 (2016), 161–319, first published online 23 May 2016. https://doi.org/10.1017/S096249291600009X
