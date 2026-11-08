# Sharp two-phase optimal coordinate sampling on positive-correlation friendship matrices

## Finding

There is an exact two-phase formula for the globally optimal fixed iid coordinate sampling of a natural sparse positive-definite family whose off-diagonal correlations form triangles sharing a hub. Fix an integer \(m\ge2\), put \(q=2m\), and fix real parameters \(0<s<1\) and \(t>0\) satisfying \(qt^2<1+s\). Form the \((q+1)\)-by-\((q+1)\) symmetric matrix \(C\) with diagonal \(1\), hub-to-leaf entries \(t\), within-pair leaf entries \(s\), and all other entries zero. More explicitly, label the hub by \(0\), pair leaves \(2j-1,2j\) for \(1\le j\le m\), and let \(C_{0i}=t\) for all leaves and \(C_{2j-1,2j}=s\). The assumptions make \(C\) strictly positive definite.

For the strictly convex quadratic \(f(z)=\tfrac12 z^TCz-b^Tz\), an exact coordinate-descent step samples \(i\) with fixed probability \(p_i\), independently of earlier steps, and sets \(z^+=z-(Cz-b)_i e_i\). Its sharp worst-case one-step expected squared \(C\)-energy contraction decrement is
\[
\rho(p)=\lambda_{\min}\bigl(C^{1/2}\operatorname{Diag}(p)C^{1/2}\bigr).
\]
Define \(c=1+s\), \(r=qt^2\), and the phase boundary
\[
s_0=\frac{t+qt^2}{2+t}=\frac{t+r}{2+t}.
\]
Every parameter choice in the stated domain has an optimal sampler assigning a probability \(x_*\) to the hub and the same probability \(y_*\) to each leaf. The optimal decrement, including optimization over **all**, not necessarily symmetric, sampling distributions, is
\[
\boxed{\begin{aligned}
\text{if }s\le s_0:\quad
D_R&=c+q+2qt,\\
x_*&=\frac{c+qt}{D_R},\qquad
 y_*=\frac{1+t}{D_R},\qquad
\rho_* =\frac{c-r}{D_R};\\
\text{if }s>s_0:\quad
D_P&=2s(1-s)+q(2s-r),\\
x_*&=\frac{2s(1-s)}{D_P},\qquad
 y_*=\frac{2s-r}{D_P},\qquad
\rho_* =\frac{(1-s)(2s-r)}{D_P}.
\end{aligned}}
\]
All denominators and displayed optimal probabilities are strictly positive. Both formulas agree at equality \(s=s_0\). The class-symmetric optimal sampler is unique. At \(s<s_0\), the radial two-dimensional eigenspace determines the sharp decrement; at \(s>s_0\), the leaf-pair antisymmetric modes and the radial mode meet at the optimum. The theorem does not assert uniqueness of all nonsymmetric optimizers.

For instance, \(m=2\), \(s=1/2\), \(t=1/5\) gives \(x_*=25/193\), \(y_*=42/193\), and \(\rho_*=21/193\); uniform sampling gives only \(1/10\). The active-mode switch is an exact optimization phase transition rather than a numerical observation.

## Assumptions and scope

All entries, parameters, and optimization variables are real. There are \(q+1=2m+1\) coordinates. The probability simplex includes its boundary. The update is exact, unaccelerated coordinate minimization on an SPD quadratic, with one index sampled iid from a fixed distribution. The objective is the sharp one-step conditional expectation bound for squared \(C\)-energy, equivalently twice the objective gap; it is not a statement about implementation time, finite-horizon adaptive scheduling, or other norms. The vector \(b\in\mathbb R^{q+1}\) is arbitrary and affects neither the optimum probabilities nor the decrement.

## Proof

**Step 1: positive definiteness and reduction of the contraction objective.** The leaf space splits orthogonally into antisymmetric vectors on each pair, of dimension \(m\), with eigenvalue \(\alpha=1-s\), and vectors constant on each pair with total leaf sum zero, of dimension \(m-1\), with eigenvalue \(c=1+s\). The remaining radial space, spanned by the hub unit vector and normalized all-leaf vector, has matrix
\[
\begin{pmatrix}1&\sqrt q\,t\\\sqrt q\,t&c\end{pmatrix}.
\]
Its determinant is \(c-r>0\). Thus \(C\succ0\) exactly under the declared strict conditions. If \(e=z-C^{-1}b\), one coordinate step decreases \(\|e\|_C^2\) by \((Ce)_i^2\). Therefore its expectation is \(\|e\|_C^2-e^TC\operatorname{Diag}(p)Ce\). The sharp Rayleigh quotient gives precisely \(\rho(p)=\lambda_{\min}(C^{1/2}\operatorname{Diag}(p)C^{1/2})\).

**Step 2: symmetry is globally lossless.** As a function of \(p\), the matrix inside the smallest eigenvalue is affine, hence \(\rho\) is concave. Permuting the \(m\) pairs and interchanging the two members of any pair preserves \(C\) and \(\rho\). Averaging any sampling vector over this finite automorphism group leaves the hub probability unchanged, makes every leaf probability identical, and by concavity cannot decrease \(\rho\). Thus the supremum over the full simplex is attained by a class-symmetric vector \((x,y,\ldots,y)\) with \(x+qy=1\); no unexamined asymmetry can yield a larger value.

**Step 3: exact class-symmetric spectrum.** The smallest eigenvalue of \(C^{1/2}\operatorname{Diag}(p)C^{1/2}\) equals that of \(\operatorname{Diag}(\sqrt p)C\operatorname{Diag}(\sqrt p)\). For the symmetrical design its spectrum comprises \(\alpha y\) with multiplicity \(m\), \(cy\) with multiplicity \(m-1\), and two eigenvalues of
\[
R(x,y)=\begin{pmatrix}x&\sqrt{qrxy}\\\sqrt{qrxy}&cy\end{pmatrix}
=\begin{pmatrix}x&qt\sqrt{xy}\\qt\sqrt{xy}&cy\end{pmatrix}.
\]
Because \(\alpha<c\), the sharp decrement is \(\min\{\alpha y,\lambda_-(R)\}\). The entry \(\sqrt{qrxy}=qt\sqrt{xy}\) follows from \(r=qt^2\). All identities hold continuously at simplex endpoints.

**Step 4: solve the radial-only maximization.** For a positive candidate rate \(\lambda\), rescale \(X=x/\lambda\), \(Y=y/\lambda\). The condition \(\lambda_-(R)\ge\lambda\) is
\[
X\ge1,\quad cY\ge1,\quad (X-1)(cY-1)\ge rXY.
\]
Equivalently, for \(X>c/(c-r)\), one needs \(Y\ge (X-1)/((c-r)X-c)\). Since \(x+qy=1\), maximizing the radial eigenvalue amounts to minimizing the sharp total \(X+qY\). The derivative of its lower-bound curve is \(-r/((c-r)X-c)^2\), so the unique minimizer satisfies \((c-r)X-c=qt\). Hence
\[
X_R=\frac{c+qt}{c-r},\quad Y_R=\frac{1+t}{c-r},\quad
\lambda_R=\frac{c-r}{c+q+2qt}.
\]
The unique radial-only optimizer is \((x_R,y_R)=(\lambda_RX_R,\lambda_RY_R)\). Its leaf-pair eigenvalue is no smaller than \(\lambda_R\) exactly when
\[
(1-s)(1+t)\ge c-r\iff s\le\frac{t+r}{2+t}=s_0.
\]
This proves the first regime and its uniqueness among class-symmetric designs.

**Step 5: solve the pair-limited phase.** Suppose \(s>s_0\), so at the radial optimizer \(\alpha y_R<\lambda_R\). Since \(s>s_0\) and \(r<c<2\), we have \(2s>r\). At \(x=0\) the radial minimum is zero, whereas \(\alpha y>0\). The radial least eigenvalue, viewed as \(\lambda_{\min}(C_{\mathrm{rad}}^{1/2}\operatorname{Diag}(x,y)C_{\mathrm{rad}}^{1/2})\), is a concave function of \(x\). The unique radial maximizer is \(x_R\); consequently the radial value is strictly increasing from zero to its maximum on \([0,x_R]\). Meanwhile \(\alpha y=\alpha(1-x)/q\) strictly decreases. They therefore cross exactly once in \((0,x_R)\), and the minimum of the two increases before the crossing and decreases after it. At the crossing \(\lambda_-(R)=\alpha y\), and the determinant condition is
\[
(x-\alpha y)(cy-\alpha y)=rxy,
\quad\text{equivalently}\quad
\frac{x}{y}=\frac{2s(1-s)}{2s-r}.
\]
Combining this ratio with \(x+qy=1\) yields \(x_P,y_P\) and \(\rho_P=\alpha y_P\) as displayed. This is the unique class-symmetric optimum in the second regime; continuity identifies equality at the boundary. Automorphism averaging from Step 2 makes the two formulas globally optimal.

**Step 6: nontriviality beyond the inverse-positive formula.** In the worked instance, the inverse of the leaf Schur complement \(B=sI\)-paired block plus hub update has negative within-pair off-diagonal entries and positive cross-pair entries. The triangle pattern of sign constraints prevents diagonal sign-flipping into an entrywise-nonnegative inverse: two leaves in the same pair have opposite required signs, while leaves in distinct pairs require equal signs. With at least two pairs, those conditions contradict one another. Thus the general inverse-positive result is inapplicable to this natural all-positive interaction family, even though a generic semidefinite-program formulation applies.

## Verification

Run `python artifacts/verify_friendship_sampling.py` from a directory containing the provided `artifacts` folder. Only Python's standard-library `fractions` module is needed. `artifacts/verification_output.txt` records the expected deterministic output. The program checks the explicit probabilities, rational determinant and active-eigenvalue identities, positive definiteness assumptions, both phase inequalities, a rational grid of alternative symmetric designs, and the expected quadratic-energy loss identity. It verifies 343 admissible rational designs, 34,643 rational-grid comparison cases, and 46 exact energy identities, plus the explicit five-coordinate witness. These are finite checks; Steps 1–5 above prove the complete parameter range and global optimization.

## Relationship to prior work

Qu and Richtárik's 2014 original preprint develops arbitrary sampling for randomized coordinate descent using general complexity methods. Gower and Richtárik's 2015 account formulates optimal randomized linear-system sampling via semidefinite optimization. Pukelsheim and Torsney's 1991 optimal-design paper supplies general E-optimal-design machinery on linearly independent supports, but the inspected text does not evaluate the present correlated friendship family or identify its sharp eigenmode transition. Agaskar, Wang and Lu study optimal row sampling and exact mean-square error in randomized Kaczmarz algorithms, a related but distinct algorithmic objective.

An accessible previously published inverse-positive coordinate-sampling theorem proves an explicit formula when the normalized Hessian has entrywise nonnegative inverse. Our strictly positive triangle family does not generally satisfy that hypothesis, so the prior closed form does not imply this result. The novelty assessment is limited to the explicitly inspected texts and mathematical implications. The general SDP framework contains the present optimization as an instance but does not itself supply the explicit two-phase solution. A prior equivalent specialized calculation in E-optimal-design or structured matrix-scaling literature cannot be excluded without broader independent specialist review.

## Limitations

The optimum is for fixed iid exact coordinate updates, worst-case conditional expected squared energy, and the stated SPD family only. It is not a convergence-time lower bound against other algorithms, nor an assertion of unique nonsymmetric optimal sampling. Positivity of all triangle correlations is required, and boundary values making \(C\) singular are excluded. The formula is an exact explicit solution to a structured E-optimal design problem; generic SDP duality, by itself, does not certify publication novelty. The symbolic argument proves an infinite family, whereas the attached arithmetic tests check finitely many rational parameters. Independent mathematical validation and publication-priority review remain outstanding.

## References

1. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling I: Algorithms and Complexity*, initial arXiv posting December 27, 2014, https://arxiv.org/abs/1412.8060.
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296, first posted June 10, 2015, https://arxiv.org/abs/1506.03296.
3. F. Pukelsheim and B. Torsney, *Optimal weights for experimental designs on linearly independent support points*, Annals of Statistics 19 (1991), 1614–1625, https://doi.org/10.1214/aos/1176348265.
4. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities* (2014), publicly accessible manuscript at https://dash.harvard.edu/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/download.
5. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* (published research record, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995.
