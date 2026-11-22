# An asymptotically binomial Katětov spectrum loses log-concavity at eleven leaves

## Finding

Let \(\mathbb U_4\) be the countable universal homogeneous metric structure with positive distances \(\{1,2,3,4\}\). For each integer \(n\ge1\), individually name the center \(c\) and leaves \(v_1,\ldots,v_n\) of the finite star metric \(A_n\) satisfying \(d(c,v_i)=2\) and \(d(v_i,v_j)=4\) for distinct leaves. Define \(c_{n,j}\) as the number of complete nonalgebraic singleton types over these named parameters for which exactly \(j\) leaves are at distance at most two from the new point. Then

\[
\boxed{F_n(z):=\sum_{j=0}^{n}c_{n,j}z^j=(1+z)^n+3(2+z)^n+n(1+2^n)z.}
\]

**Sharp coefficient-shape theorem.** For every \(n\ge1\), the entire sequence \((c_{n,0},\ldots,c_{n,n})\) is unimodal. It is log-concave at every internal grade if and only if \(n\le10\). For every \(n\ge11\), its *only* log-concavity violation is at grade \(j=2\), namely \(c_{n,2}^2<c_{n,1}c_{n,3}\). The first failure therefore requires exactly eleven leaves, or twelve named old parameters.

The normalized grade law nevertheless becomes asymptotically binomial: if \(J_n\) is the number of distance-at-most-two leaves in a uniformly chosen nonalgebraic singleton type, then

\[
 d_{\mathrm{TV}}\bigl(\mathcal L(J_n),\operatorname{Bin}(n,1/3)\bigr)
 \le \frac{2^n+n(1+2^n)}{2^n+3^{n+1}+n(1+2^n)}
 =O\bigl(n(2/3)^n\bigr).
\]

Thus global binomial approximation, even in total variation, does not guarantee log-concavity of all local grade counts.

## Assumptions and scope

Distances are integer-valued in \(\{0,1,2,3,4\}\), with zero only on the diagonal, and all parameters are individually named. An added point must be different from every parameter, so its distance to every parameter is positive. The base is an isometric metric star: each center-to-leaf distance is two, while the distance between two leaves is four. The grading counts the leaves at new-point distance one or two; the center is not part of the grade.

A finite map \(f:A_n\to\{1,2,3,4\}\) specifies a realizable singleton type if and only if
\[
 |f(u)-f(v)|\le d(u,v)\le f(u)+f(v)
\]
for every pair of old parameters. The finite one-point extension property realizes each such map. Every one has infinitely many distinct realizations: arbitrarily many new points can be prescribed to have this same positive distance-vector, with pairwise mutual distance one. The relevant metric triangle inequalities still hold. Consequently no type counted here is algebraic.

## Proof

**1. Classification of metric one-point extensions.** Write \(x=f(c)\) and \(y_i=f(v_i)\). The center-leaf inequalities require \(|x-y_i|\le2\le x+y_i\). The leaf-leaf inequalities simplify to \(y_i+y_j\ge4\), since their distance is four and their values lie between one and four. Therefore at most one leaf can have value one; if one does, every other leaf has value three or four (but for \(x=1\), only three is allowed).

For \(x=1\), the assignments without a leaf of value one have \(y_i\in\{2,3\}\), contributing \((1+z)^n\), and the assignments with exactly one such leaf contribute \(nz\). For \(x=2\) and for \(x=3\), the assignments without value one have \(y_i\in\{2,3,4\}\), contributing \((2+z)^n\) each; those with one value-one leaf contribute \(n2^{n-1}z\) for each choice of \(x\). For \(x=4\), every \(y_i\) lies in \(\{2,3,4\}\), contributing a third \((2+z)^n\). The five disjoint contributions give the claimed polynomial, including \(n=1\).

**2. A log-concave reference tail.** Put \(Q=2^n\) and
\[
 b_j=\binom nj(1+3\cdot2^{n-j})\qquad(0\le j\le n).
\]
Then \(c_{n,j}=b_j\) except at \(j=1\), where \(c_{n,1}=b_1+n(1+Q)\). We prove that \((b_j)\) is strictly log-concave for every \(n\ge2\). For an internal index \(j\), put \(k=n-j\ge1\) and \(t=3\cdot2^k\). The inequality \(b_j^2>b_{j-1}b_{j+1}\) is equivalent, after cancelling positive binomial factors, to
\[
 2(n+1)(1+t)^2>jkt.
\]
Indeed \((1+2t)(1+t/2)=(1+t)^2+t/2\) and \(\binom nj^2/(\binom n{j-1}\binom n{j+1})=1+(n+1)/(jk)\). Because \(n+1>j\), it is enough that \(2(1+t)^2>kt\), which follows from \(2(t+2+t^{-1})>k\), since \(t=3\cdot2^k>k\). Therefore the only potentially failing log-concavity index of \((c_{n,j})\) is \(j=2\). The increase at \(j=1\) cannot harm the inequality centered at \(j=1\), and all inequalities centered at \(j\ge3\) are unchanged.

**3. Exact sharp threshold.** For \(n\ge3\), expand the only unsettled Turán difference:
\[
 \begin{aligned}
 c_{n,2}^2-c_{n,1}c_{n,3}
 =\frac{n^2(n-1)}{192}\bigl(& (33-3n)Q^2\\
 &+(136-32n)Q+(80-16n)\bigr),\qquad Q=2^n.
 \end{aligned}
\]
For \(n\ge11\) all three coefficients inside the parentheses are nonpositive and the linear and constant coefficients are strictly negative, so the difference is negative. For \(3\le n\le4\), all three coefficients are positive; for \(n=5\) the expression is \(18Q^2-24Q>0\). For \(6\le n\le10\), the parenthetical expression is at least \(3Q^2-184Q-80>0\), because \(Q\ge64\). The cases \(n=1,2\) have no internal index two, and strict log-concavity elsewhere is already established. At the threshold \(n=11\),
\[
 (c_{11,0},c_{11,1},c_{11,2},c_{11,3},c_{11,4})
 =(6145,56342,84535,126885,127050)
\]
and \(c_{11,2}^2-c_{11,1}c_{11,3}=-2788445\). This proves sharpness and the uniqueness of the violating index at each larger order.

**4. Unimodality.** The reference tail starting at \(j=2\) is strictly log-concave and hence unimodal. Direct subtraction gives
\[
 c_{n,2}-c_{n,1}=\frac n8\bigl((4n-20)+(3n-23)2^n\bigr).
\]
It is negative for \(1\le n\le7\) and positive for \(n\ge8\). Also \(c_{n,0}\le c_{n,1}\) for every \(n\ge1\). For \(n\le7\), \(c_{n,2}\ge c_{n,3}\) (trivial for \(n\le2\); for \(3\le n\le7\) use \(c_{n,3}/c_{n,2}=\frac{n-2}{3}\frac{1+3\cdot2^{n-3}}{1+3\cdot2^{n-2}}<1\)). Thus the mode is at grade one for \(n\le7\). For \(n\ge8\), the initial three grades increase, after which the log-concave tail can change from increasing to decreasing at most once. Every full sequence is unimodal.

**5. Binomial proximity.** The summand \(3(2+z)^n\), normalized by its total \(3^{n+1}\), is exactly the probability generating function of \(\operatorname{Bin}(n,1/3)\). The other two summands have nonnegative coefficients and combined total \(R_n=2^n+n(1+2^n)\). The full normalized law is therefore a convex mixture with binomial weight \(3^{n+1}/(3^{n+1}+R_n)\), implying the stated total-variation bound. Finally \(R_n/3^{n+1}=O(n(2/3)^n)\). All assertions follow.

## Verification

The standalone Python script `artifacts/check_star_types.py` independently enumerates every possible center/leaf distance vector, directly checks every old/new triangle, and constructs the entire grading histogram for all \(1\le n\le7\); these match the closed polynomial coefficient-by-coefficient. It also checks exact symbolic coefficient identities, log-concavity failure locations and unimodality for all \(1\le n\le300\), and reports `VERIFY_OK`. The analytic all-order arguments in the preceding proof, not the finite checks, establish the assertions for unbounded \(n\).

## Relationship to prior work

The Katětov inequalities and realization of finite types in universal homogeneous finite-distance metric spaces are standard; Sauer's 2010 treatment supplies them explicitly. Those results do not state a near-leaf grade polynomial or a sharp coefficient-shape boundary. A published representation of diameter-three singleton types as Widom–Rowlinson partition functions treats only the distance palette \(\{1,2,3\}\) and a different class of parameter metrics. Earlier diameter-four results on equilateral parameter sets address type-compatibility matrices and two-point type channels, not the present center-plus-equilateral-leaves grading. The binomial-sum polynomial is a new specialization and its full coefficient-shape classification and total-variation contrast are the retained claims. Published and indexed comparisons did not identify a stronger covering statement; this is a best-knowledge novelty assessment rather than a guarantee of historical priority.

## Limitations

The formula and sharp transition are specific to the isometric \(2/4\)-star base, the four-valued unrestricted metric Fraïssé limit, and a leaf-only distance-at-most-two grading. They do not classify arbitrary metric parameter spaces, other distance palettes, or higher-arity types. Finite checker coverage stops at seven leaves for complete diagram enumeration and at 300 leaves for exact coefficient checks. Full historical priority and independent mathematical validation remain unperformed.

## References

1. Norbert Sauer, *Vertex partitions of metric spaces with finite distance sets* (preprint first public on arXiv, 2010-10-20), https://arxiv.org/abs/1010.4212 ; see Section 2 for Katětov maps, their metric inequalities and one-point extension realization.
2. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* (public mathematical note), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989 ; compare the different palette and graph-metric parameter class.
3. R. P. Stanley, *Log-Concave and Unimodal Sequences in Algebra, Combinatorics, and Geometry*, Ann. N.Y. Acad. Sci. 576 (1989), 500–535, for classical coefficient-shape terminology.
