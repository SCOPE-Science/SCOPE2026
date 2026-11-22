# A parity transition from unique weights to a regular polygon of Schur-cycle normers

## Finding

For every integer \(n\ge3\), let \(B_n=I_n+P_n\), where \((P_n x)_j=x_{j-1}\) with indices modulo \(n\). Define \(F_n(u,v)=\|D_{\sqrt u}B_nD_{\sqrt v}\|_{S_1}\) for two probability vectors \(u,v\in[0,1]^n\). Its maximum is \(2/(n\sin(\pi/(2n)))\) for odd \(n\), and \(2/(n\tan(\pi/(2n)))\) for even \(n\). For odd \(n\), the unique maximizing pair is \(u_j=v_j=1/n\). For even \(n\), every maximizing pair, and no other pair, is parameterized by real \(a,b\) as \[u_j=\frac{1+a\cos(2\pi j/n)+b\sin(2\pi j/n)}n,\qquad v_j=\frac{1+a\cos(2\pi(j-1/2)/n)+b\sin(2\pi(j-1/2)/n)}n,\] with all displayed coordinates nonnegative. The feasible parameter set is the regular \(2n\)-gon of inradius one. This is a complete norming-probability classification for the complex Schur multiplier with cyclic two-neighbor mask.

The underlying multiplier preserves positions \((j,j)\) and \((j,j-1)\) in complex \(n\times n\) matrices. For even \(n\), all norming probability pairs form a two-dimensional regular polygon, including boundary pairs with zero coordinates; for odd \(n\), there is exactly one pair. The multiplier norms themselves are classical; the equality classifications are the result.

## Assumptions and scope

Let \(n\ge3\) be an integer. All matrices act on complex Euclidean space. Indices \(j\) run through \(0,\ldots,n-1\), modulo \(n\). The positive diagonal \(D_{\sqrt u}\) is defined even if some coordinates vanish. The trace/nuclear norm is \(\|T\|_{S_1}=\operatorname{tr}|T|\). A norming probability pair maximizes \(F_n\) over the product of two probability simplices; it is not an assertion that every norming operator has rank one.

## Proof

**1. Sharp uniform upper bound and equality.** Write \(B=HW\), with \(W=|B|\ge0\) and \(H\) any unitary extension of its polar partial isometry, so \(HW=B\). As \(B\) is circulant, \(W\) has constant diagonal \(c=\operatorname{tr}W/n\); the same is true of \(HWH^*\). Put \(X=D_{\sqrt u}HW^{1/2}\) and \(Y=D_{\sqrt v}W^{1/2}\), so \(XY^*=D_{\sqrt u}BD_{\sqrt v}\) and \(\|X\|_F^2=\|Y\|_F^2=c\). The trace-class Cauchy–Schwarz inequality gives \(F_n(u,v)\le c\); uniform weights attain \(c\). Its equality condition (including singular \(W\)) is \(X^*X=Y^*Y\): this follows from \(\|XY^*\|_1=\operatorname{tr}\sqrt{(X^*X)^{1/2}(Y^*Y)(X^*X)^{1/2}}\) and equality in matrix fidelity Cauchy–Schwarz for equal-trace positive matrices. As \(W\) is invertible on its support \(Q\), equality is equivalent to
\[Q(H^*D_uH-D_v)Q=0.\tag{1}\]

**2. Fourier reduction.** In the Fourier basis \(\phi_r(j)=n^{-1/2}e^{2\pi irj/n}\), the eigenvalue of \(B\) is \(1+e^{-2\pi ir/n}\). Put \(h_r=e^{-\pi ir/n}\operatorname{sgn}\cos(\pi r/n)\) for each nonzero eigenvalue. When \(n\) is even, the single missing frequency is \(r=n/2\). Taking the \((r,r+k)\) matrix coefficient in (1) yields, for every \(k\) modulo \(n\),
\[\widehat v(k)=\overline{h_r}h_{r+k}\widehat u(k),\qquad r,r+k\ne n/2,\tag{2}\]
where Fourier coefficients use the convention \(\widehat u(k)=n^{-1}\sum_j u_j e^{2\pi ikj/n}\); indices on \(h\) are interpreted modulo \(n\). The multiplier \(\overline{h_r}h_{r+k}\) is constant in the admissible \(r\) exactly for \(k=0\) (every \(n\)), and also \(k=1,-1\) when \(n\) is even. Indeed, between successive nonzero modes the polar phases advance by \(e^{-\pi i/n}\); the single sign change passes directly through the omitted zero mode in even dimension, while for every other nonzero frequency there exist admissible pairs with opposite sign factors. On crossing the periodic endpoint the same phase increment appears. For odd \(n\), the sign change necessarily has two nonzero endpoints and every nonzero frequency sees both signs. Thus (2) kills every nonconstant Fourier mode for odd \(n\), forcing uniform \(u,v\).

For even \(n\), (2) allows only the constant and first harmonics, and the phase \(e^{-\pi i/n}\) corresponds in physical coordinates to shifting the first-harmonic weight from \(j\) to \(j-1/2\). Normalization fixes the constant coefficient at \(1/n\), yielding precisely the displayed two-parameter family. Conversely, substituting these Fourier coefficients in (2) proves (1) and hence equality in the Schur bound, including on the boundary where some weights vanish. The \(2n\) nonnegativity conditions have outward normals at all the equally spaced angles \(k\pi/n\); their intersection is a regular \(2n\)-gon with inradius one.

**3. Value of the maximum.** The singular values of \(I+P\) are \(2|\cos(\pi r/n)|\). The finite trigonometric sums give \(\frac2n\sum_{r=0}^{n-1}|\cos(\pi r/n)|=2/[n\sin(\pi/(2n))]\) for odd \(n\), and \(2/[n\tan(\pi/(2n))]\) for even \(n\). This equals \(c\), completing the proof.

## Verification

`verify.py` recomputes singular values of the cycle mask, evaluates nonuniform even-dimensional polygon points, and checks the Fourier equality equations for a bounded range of dimensions. The analytic Fourier argument, not the finite numerical checks, establishes the theorem for all \(n\). Reproduction: `python3 verify.py` (Python 3 with NumPy). The bounded diagnostic is not an exhaustive search over all probabilities.

## Relationship to prior work

Mathias (1993) proves the circulant Schur norm formula and the uniform-optimality condition. Levene (2026) presents the trace-norm probability variational characterization and cites Mathias. These results give the value of the maximum but do not, in the accessible inspected statements, classify its entire equality set. The present theorem identifies all probability maximizers and the odd/even change of its dimension, rather than recalculating the known norm. Related published classifications for projective-plane/design incidence masks have different incidence objects; the cycle has degree two and is not a nontrivial symmetric two-design for \(n\ge4\).

## Limitations

The theorem concerns complex Schur multipliers and norming **probability weights**, not a classification of all norming matrices. The older Mathias article was available through an abstract rather than complete primary text; an implicit equality classification in that work is a residual originality risk. Finite diagnostics do not prove the infinite-family Fourier statement.

## References

1. R. H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419 (first public 2026-11-05), https://arxiv.org/abs/2611.08419 (Section 2, Lemma 2.3; Section 3, reference to Mathias).
2. R. Mathias, *The Hadamard operator norm of a circulant and applications*, SIAM J. Matrix Anal. Appl. 14 (1993), 1152–1167, https://doi.org/10.1137/0614080 (accessible abstract and norm statement).
