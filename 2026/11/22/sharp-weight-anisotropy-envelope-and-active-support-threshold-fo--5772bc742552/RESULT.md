# Sharp weight-anisotropy envelope and active-support threshold for squared weighted \(\ell_1\) proximal maps

## Finding
For an integer \(n\ge2\), \(\alpha>0\), and \(w=(w_1,\ldots,w_n)\in(0,\infty)^n\), define the nonlinear proximal map
\[
T_{\alpha,w}(x)=\mathop{\rm argmin}_{u\in\mathbb R^n}
\left\{\frac12\|u-x\|_2^2+
\frac\alpha2\left(\sum_{j=1}^nw_j|u_j|\right)^2\right\}.
\]
All Lipschitz coefficients below use the coordinate maximum norm on *both* input and output.

**Exact fixed-weight coefficient and support selection.** For each output coordinate \(i\), sort the \(n-1\) weights other than \(w_i\) in nondecreasing order \(b_{i,1}\le\cdots\le b_{i,n-1}\) and set \(B_{i,k}=\sum_{h=1}^{k}b_{i,h}\), \(C_{i,k}=\sum_{h=1}^{k}b_{i,h}^2\), with both sums zero for \(k=0\). Then
\[
\boxed{\operatorname{Lip}_\infty(T_{\alpha,w})=
1+\max_{1\le i\le n}\max_{0\le k\le n-1}
\frac{\alpha w_i(B_{i,k}-w_i)}
{1+\alpha(w_i^2+C_{i,k})}.}
\]
The maximum can be evaluated in \(O(n^2)\) arithmetic operations after one \(O(n\log n)\) weight sort; the underlying exponentially many active supports need not be enumerated. A pair of distinct finite inputs realizes the coefficient.

**Sharp normalized weight envelope.** Under \(\sum_{j=1}^nw_j^2=1\),
\[
\boxed{\max_{w\in(0,\infty)^n,\ \|w\|_2=1}
\operatorname{Lip}_\infty(T_{\alpha,w})
=1+\frac{\alpha}{1+\alpha}\frac{\sqrt n-1}{2}.}
\]
Equality holds **exactly**, up to coordinate permutation, when one distinguished weight is \(\sqrt n-1\) times each of the other \(n-1\) equal weights. Thus uniform weights maximize worst-case sensitivity among all normalized positive weights exactly at \(n=4\), and not at any other \(n\ge2\). Uniform weights themselves have coefficient \(1+\frac\alpha{1+\alpha}(1-2/n)\). The normalized worst-case sensitivity is of order \(\sqrt n\), versus less than \(2\) for uniform weights at fixed \(\alpha\).

The infimum of the coefficient over normalized positive weights is \(1\). For \(n=2\) it is attained exactly by equal weights; for \(n\ge3\) it is unattained. Accordingly, the map is coordinatewise nonexpansive exactly in the two-coordinate equal-weight case (within \(n\ge2\)).

## Assumptions and scope
All vectors and weights are real, all weights and \(\alpha\) strictly positive, and the coordinate maximum norm is \(\|x\|_\infty=\max_i|x_i|\). The equality and infimum statements compare weights subject to \(\sum_iw_i^2=1\), which fixes the effective regularization strength. A general nonnormalized weight vector has the exact first formula without rescaling. Only a *single weighted group* is considered; independent disjoint groups can be handled blockwise, but no claim concerns overlapping groups or non-Euclidean proximal objectives.

## Proof
**1. KKT structure and realizable cells.** The objective is strongly convex, so \(T_{\alpha,w}\) exists uniquely. Fix an open input cell where the nonzero coordinates of its output have support \(S\ne\varnothing\) and fixed signs \(s_i\in\{-1,1\}\), \(i\in S\). Let \(q=\sum_{i\in S}w_i|u_i|\) and \(v_i=s_iw_i\) on \(S\), zero otherwise. The KKT conditions give \(u_i=x_i-\alpha s_iw_iq\) for \(i\in S\), \(u_i=0\) otherwise, and \(|x_j|<\alpha w_jq\) for strictly inactive \(j\). Hence
\[
q=\frac{\sum_{i\in S}s_iw_ix_i}{1+\alpha\sum_{i\in S}w_i^2},
\qquad
J_S=\operatorname{diag}(\mathbf1_S)-\frac{\alpha vv^{\mathsf T}}{1+\alpha\|v\|_2^2}.
\]
This Jacobian is constant on the cell. Every nonempty support is strictly realizable: take any \(u_i>0\) for \(i\in S\), \(u_j=0\) off \(S\), let \(q=\sum_{i\in S}w_iu_i>0\), and choose \(x_i=u_i+\alpha w_iq\) on \(S\) and \(x_j=0\) off \(S\). The KKT inequalities are strict. Thus every support Jacobian is a genuine local derivative, not merely a formal candidate.

The map is continuous and piecewise affine with finitely many sign/support cells. Integrating along line segments through these cells bounds its global Lipschitz coefficient by the largest induced matrix norm; perturbing a point inside a maximizing open cell in a row-sign direction gives equality with two finite inputs. For an active row \(i\in S\), the diagonal entry of \(J_S\) is positive and the absolute row sum is
\[
1+\frac{\alpha w_i(\sum_{j\in S\setminus\{i\}}w_j-w_i)}{1+\alpha\sum_{j\in S}w_j^2}.
\]
Inactive rows are zero. Since \(n\ge2\), this maximum is at least one: if \(n=2\), use the smaller weight in the full support (equality only for equal weights); if \(n\ge3\), use the smallest weight in the full support, whose other weights have larger sum. This proves the full-subset exact formula and nonexpansivity classification.

**2. Sorted-prefix law.** Fix \(i\), put \(D=\alpha^{-1}+w_i^2+\sum_{j\in S\setminus\{i\}}w_j^2\) and \(N=w_i(\sum_{j\in S\setminus\{i\}}w_j-w_i)\), and maximize \(r=N/D\) over supports \(S\) containing \(i\). If \(r>0\), adding a currently excluded index \(j\) increases the ratio exactly when \(w_j<w_i/r\); removing an included other index increases it exactly when \(w_j>w_i/r\). Consequently an optimal support can include all weights below the same cutoff and omit all weights above it, assigning ties either way. The selected other weights therefore form a sorted prefix; inserting their prefix sums into the row expression proves the first boxed formula. Since the global maximum has a nonnegative excess and every strict expansive case has a positive one, no unsupported assumption about a negative maximizing ratio is used. The \(n=2\), equal-weight boundary also satisfies the prefix formula directly.

**3. Sharp weight envelope.** Assume \(\|w\|_2=1\). In an active support \(S\) of cardinality \(k\), let \(a=w_i\), \(b=(\sum_{j\in S\setminus\{i\}}w_j^2)^{1/2}\), and \(q=a^2+b^2\le1\). Cauchy--Schwarz gives
\[
w_i\left(\sum_{j\in S\setminus\{i\}}w_j-w_i\right)
\le\sqrt{k-1}\,ab-a^2
\le q\,\frac{\sqrt{k}-1}{2}.
\]
For the second inequality, the symmetric quadratic form \(-a^2+\sqrt{k-1}\,ab\) has largest eigenvalue \((\sqrt{k}-1)/2\) on the \((a,b)\) plane (the other eigenvalue is negative). Since \(q\mapsto\alpha q/(1+\alpha q)\) and \(k\mapsto\sqrt{k}\) are increasing, every row norm is at most the second boxed expression. For equality, take the *full support*, choose one \(a>0\) and \(n-1\) equal positive weights \(b_0\), with \(a=(\sqrt n-1)b_0\) and \(a^2+(n-1)b_0^2=1\). Cauchy--Schwarz and the eigenvalue bound are then both equalities. Conversely equality in the two inequalities forces full support, equal remaining weights, and exactly that positive top-eigenvector ratio. A strictly realizable full-support cell therefore provides finite input pairs achieving the sharp global envelope.

**4. Extremal comparisons.** At uniform weights \(w_i=n^{-1/2}\), all-support row sums give \(1+\frac\alpha{1+\alpha}(1-2/n)\), and a proper support of size \(k\) has no larger row sum (this also follows by monotonicity in \(k\) of \((k-2)/(n+\alpha k)\) for \(k\ge2\)). Equality with the normalized envelope requires \(\sqrt n-1=1\), i.e. \(n=4\). For \(n\ge3\), the full support and a smallest weight give a strictly positive excess, hence no positive weight vector attains coefficient one. If one weight tends to one and all other weights tend to zero while \(\|w\|_2=1\), the exact row formula shows that all positive row excesses tend to zero, proving infimum one. For \(n=2\), equal weights attain it and unequal weights do not.

## Verification
A standalone standard-library Python checker, `verify.py`, independently evaluates rational active-set Jacobians, compares the exponential subset maximum with the sorted-prefix formula, and constructs exact finite KKT-consistent input pairs realizing each sample sharp coefficient. It also checks the radical normalized envelope by enumerating small dimensions. Run `python3 verify.py`; expected output: `PASS: 464 finite exact-rational/analytic-envelope assertions`. These finite checks supplement, but do not certify, the all-parameter analytic proof.

## Relationship to prior work
The **proximal formula and the rank-one generalized Jacobian are not new**. Lin, Sun, Toh and Yuan (arXiv:1902.00151, Sections 4.1–4.3, especially Proposition 7) establish them for arbitrary positive weights; Lin, Yuan, Sun and Toh (arXiv:2009.08719, Sections 4.1–4.3, and arXiv:2306.14196, Section 3) revisit and extend their algorithmic use. The new statement is the global induced maximum-norm optimization over *all realizable supports*, its sorted-prefix reduction, the exact fixed-energy weight envelope, equality and infimum classifications, and the dimensional anisotropy effect. The familiar weighted cross-polytope projection has a different constraint and active Jacobian, with normalization by active weight energy rather than its regularized denominator; its sharp norm claims do not imply the stated squared-penalty envelope. An earlier general sharp rank-one contraction norm identity could supply the eigenvalue optimization in Step 3, but would not by itself identify the proximal support law or the finite-input sharpness.

## Limitations
The envelope is normalized by the *Euclidean energy of the penalty weights*, and thus does not compare regularization schemes with other normalizations. The result applies to fixed finite \(n\), a strictly positive regularization parameter and positive weights; it does not classify arbitrary overlapping group penalties. The proof is self-contained but has not received independent audit. Historical priority of the joint sharp active-support and anisotropy statements cannot be certified exhaustively from bibliographic search.

## References
1. M. Lin, D. Sun, K.-C. Toh, Y. Yuan, *A dual Newton based preconditioned proximal point algorithm for exclusive lasso models*, arXiv:1902.00151v1, first public February 1, 2019, https://arxiv.org/abs/1902.00151 .
2. M. Lin, Y. Yuan, D. Sun, K.-C. Toh, *A Highly Efficient Algorithm for Solving Exclusive Lasso Problems*, arXiv:2306.14196v1, first public June 25, 2023, https://arxiv.org/abs/2306.14196 .
3. M. Weylandt, *Introduction to the ExclusiveLasso Package*, technical vignette dated October 23, 2018, https://dataslingers.github.io/ExclusiveLasso/articles/ExclusiveLasso.html .
4. M. Lin, Y. Yuan, D. Sun, K.-C. Toh, *Adaptive Sieving with PPDNA: Generating Solution Paths of Exclusive Lasso Models*, arXiv:2009.08719v1, first public September 18, 2020, https://arxiv.org/abs/2009.08719 .
5. *Exact Lipschitz stability and contractivity threshold for weighted cross-polytope projections*, published-finding corpus public record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-lipschitz-stability-and-contractivity-threshold-for-weight--c92b6dad1bd0 .
