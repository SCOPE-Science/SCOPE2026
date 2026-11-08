# Gaussian-angle limits and irrational readout probabilities for colored perfect matchings

## Finding

Consider a uniformly random perfect matching on \(2n\) labeled vertices, and independently mark each vertex with one fair unary predicate \(P\). Let \(R\) denote the undirected matching relation. At each vertex \(x\), observe the pair of bits consisting of \(P(x)\) and the value of \(P\) at its unique \(R\)-neighbor. For \(i,j\in\{0,1\}\), let \(T_{ij}\) count vertices with observed pair \((i,j)\).

Let \(\mathcal F\) be the fragment of two-variable local-global counting sentences formed by finite Boolean combinations of comparisons
\[
\sum_{i,j\in\{0,1\}}c_{ij}T_{ij}\ge b,
\qquad c_{ij},b\in\mathbb Z,
\]
with coefficients and threshold independent of \(n\). Every sentence of \(\mathcal F\) has a limiting probability as \(n\to\infty\). The complete set of limiting probabilities is precisely the set of standard planar Gaussian angular measures of finite Boolean combinations of half-planes
\[
dX+\frac{e}{\sqrt2}Y\ge0,
\qquad d,e\in\mathbb Z,
\]
where \(X,Y\) are independent standard Gaussians. Equivalently, this is the set of normalized angular measures of finite unions of sectors whose bounding lines have normals in the displayed countable dense set. This spectrum is **countable and dense** in \([0,1]\).

In particular, the conjunction
\[
-T_{00}+2T_{01}-T_{11}\ge0,
\qquad -5T_{00}+2T_{01}+3T_{11}\ge0
\]
has the **irrational** limiting probability
\[
\boxed{\frac14+\frac{\arcsin(1/3)}{2\pi}}
=0.3040867239846964\ldots.
\]
By contrast, if the global comparisons may use only the original unary color counts (no neighbor-color observations), the complete limiting-probability spectrum is exactly \(\{0,1/2,1\}\). Thus permitting one local one-step observation before global linear aggregation already changes a three-value spectrum into a dense spectrum containing irrational values.

## Assumptions and scope

The language contains a symmetric irreflexive binary symbol \(R\) interpreted as a perfect matching and one unary symbol \(P\). The sample size is \(2n\), with integer \(n\ge1\). Conditional on the matching, all vertex colors are independent unbiased bits. The sentence is fixed as \(n\) varies. Only Boolean combinations of constant-coefficient linear comparisons between counts of the four local types are claimed; this theorem **does not claim** convergence for the full unrestricted two-variable local-global Presburger language or for arbitrary graph distributions.

For each \(i,j\), the local type formula is \(\eta_{ij}(x):=(P(x)\leftrightarrow i=1)\wedge\exists y\,[R(x,y)\wedge(P(y)\leftrightarrow j=1)]\), with the notation interpreted by choosing \(P\) or \(\neg P\) as appropriate. The inner neighbor test can equivalently be expressed using the permitted local counting comparison \(\#_y[R(x,y)\wedge P(y)]\ge1\), or its Boolean complement. The global term \(T_{ij}=\#_x[\eta_{ij}(x)]\) is therefore a legal global count of a locally defined unary property. No global cardinality enters a local comparison.

## Proof

**Step 1 (exact finite count law).** Let \(U,V,W\) be the numbers of matching edges with respectively zero, one, and two marked endpoints. Conditioned on any matching, its edges receive independent pairs of fair bits. Consequently,
\[
(U,V,W)\sim\operatorname{Multinomial}\bigl(n;1/4,1/2,1/4\bigr),
\qquad (T_{00},T_{01},T_{10},T_{11})=(2U,V,V,2W).
\]
For all nonnegative integers \(u+v+w=n\),
\[
\Pr(U=u,V=v,W=w)=\frac{n!}{u!v!w!\,4^{u+w}2^v}.
\]
This law remains exact after averaging over the random matching.

**Step 2 (independent Gaussian coordinates).** Define
\[
X_n=\frac{2V-n}{\sqrt n},\qquad Y_n=\sqrt{\frac2n}(W-U).
\]
For each edge the centered summands contributing to \(X_n\) and \(Y_n\) have variance one and covariance zero. Their two-dimensional covariance matrix is the identity. The ordinary multivariate central limit theorem therefore yields \((X_n,Y_n)\Rightarrow(X,Y)\), two independent standard normals.

**Step 3 (every comparison has a determinate Gaussian limit).** Given coefficients \(c_{ij}\), put \(d=c_{01}+c_{10}\) and \(s=c_{00}+c_{01}+c_{10}+c_{11}\). A direct substitution from Step 1 gives the exact identity
\[
\sum c_{ij}T_{ij}=
\frac{s}{2}n
+\sqrt n\left(\frac{d-c_{00}-c_{11}}2 X_n+\frac{c_{11}-c_{00}}{\sqrt2}Y_n\right).
\]
If \(s\ne0\), the comparison is asymptotically deterministically true or false according to the sign of \(s\). If \(s=0\), its Gaussian normal is \(dX+(c_{11}-c_{00})Y/\sqrt2\). When this normal vanishes identically, the count expression itself equals zero for every \(n\), so the test is simply \(0\ge b\). For every other critical test its limiting boundary line has Gaussian probability zero. Hence the portmanteau theorem, applied jointly to the finitely many tests in any Boolean combination, yields a limit equal to the planar Gaussian probability of the corresponding Boolean combination of homogeneous half-planes. Fixed finite thresholds \(b\) disappear in nondegenerate critical tests.

Conversely, every integer normal \((d,e/\sqrt2)\) occurs. Choose integer \(c_{00}=-(d+e)\), \(c_{11}=e-d\), \(c_{01}=2d\), and \(c_{10}=0\): then \(s=0\), and the resulting Gaussian normal is \(2dX+\sqrt2 eY\), a positive scalar multiple of \(dX+eY/\sqrt2\). Thus the angular characterization is exact in both directions. Integer normal directions form a countable dense set on the circle; the Gaussian angle of a sector varies continuously with its endpoints. These facts prove that the spectrum is countable and dense in \([0,1]\).

**Step 4 (explicit irrational limit).** For the two displayed comparisons, Step 3 produces the limit events \(X\ge0\) and \(2X+4\sqrt2Y\ge0\). The two standardized normal linear forms have correlation
\[
\rho=\frac{2}{\sqrt{2^2+(4\sqrt2)^2}}=\frac13.
\]
The elementary bivariate centered normal quadrant formula therefore gives \(1/4+\arcsin(1/3)/(2\pi)\). This number is irrational. Indeed, if \(\arcsin(1/3)/\pi\) were rational, then \(\zeta=\exp(i\arcsin(1/3))\) would be a root of unity. The number \(2\sin(\arcsin(1/3))=(\zeta-\zeta^{-1})/i=2/3\) would then be a rational algebraic integer, hence an integer, contradiction.

**Step 5 (boundary without local observations).** Without local observations, all available nonconstant global count comparisons reduce to fixed integer-affine comparisons involving the single total \(Z_n=\#\{x:P(x)\}\sim\operatorname{Binomial}(2n,1/2)\). For a fixed comparison, the mean drift either dominates or cancels. In the latter case the centered sign converges to a fair Gaussian sign. Any Boolean combination then depends asymptotically only on whether this one sign is positive or negative, giving one of \(0,1/2,1\). All three are attained by constant truths, falsehoods and \(Z_n\ge n\) (the last formulated as \(\#P\ge\#\neg P\)).

## Verification

The standalone `checker.py` enumerates all \(2^{2n}\) fair endpoint colorings for each \(1\le n\le7\), checking the exact multinomial law coefficient by coefficient and confirming the four local type counts. It separately computes exact rational joint probabilities of the displayed inequalities for \(1\le n\le16\) using multinomial sums and checks the Gaussian covariance calculation. Running the embedded checker prints `ALL_CHECKS_OK`. This finite test is not a substitute for Steps 2–5, which establish the infinite claims.

## Relationship to prior work

Benedikt, Lu, Perry and Tan (2026), arXiv:2610.39108v1, define separated local/global Presburger quantifiers and prove decidability of finite satisfiability. Their Definition 3 explicitly admits the local and global comparisons used here, but their main result is not a probability limit law or angular spectrum. Kopczyński and Tan (2013/2014), arXiv:1304.0829v4, characterize possible **finite model cardinalities** for two-variable logic with counting, a different meaning of “spectrum.” Larrauri and Perarnau (2024), arXiv:2405.14836v1, study first-order limiting probabilities for graphs with prescribed degree sequences; their first-order framework does not include the growing global count comparisons in the present fragment.

The exact multinomial law, multivariate CLT, normal quadrant identity and algebraic-integer argument are classical mathematical ingredients. The claim of a distinct contribution is limited to the complete local-global **logical readout** classification on this minimal fixed-degree graph model and the precise shift from a three-value to an irrational dense spectrum. General Gaussian-cone principles imply the probability calculation once the readout has been reduced to independent edge types; priority of equivalent logical formulations is not independently established.

## Limitations

The matching is a simple undirected perfect matching, the unary coloring is fair and independent, and coefficients are fixed integers. The classification concerns a stated syntactic fragment, not arbitrary nested counting formulas, arbitrary variable-dependent arithmetic, modulo quantifiers or arbitrary random graphs. The source is used for expressibility and motivation, not to claim any of its decision-theoretic results. No independent audit or exhaustive historical-priority certification has been performed. The result is an application of classical central-limit theory; its specific logical invariant, rather than a new probability limit theorem, is the claimed value.

## References

1. M. Benedikt, C.-H. Lu, A. Perry and T. Tan, *Deciding two-variable logic with global and local Presburger quantification*, arXiv:2610.39108v1 (first posted 2026-10-29), https://arxiv.org/html/2610.39108v1.
2. E. Kopczyński and T. Tan, *Regular graphs and the spectra of two-variable logic with counting*, arXiv:1304.0829v4 (first posted 2013-04-03), https://arxiv.org/html/1304.0829v4.
3. A. Larrauri and G. Perarnau, *First Order Logic of Sparse Graphs with Given Degree Sequences*, arXiv:2405.14836v1 (2024), https://arxiv.org/abs/2405.14836.
4. The multinomial central limit theorem and the centered bivariate Gaussian quadrant formula are used in their standard classical forms.
