# Four-phase optimal coordinate sampling for two-community correlation systems

## Finding

Let \(p,q\ge 2\). Consider a unit-diagonal symmetric matrix \(C\) indexed by two communities of sizes \(p\) and \(q\), with every distinct within-first entry equal to \(a\), every distinct within-second entry equal to \(b\), and every cross-community entry equal to \(c\). Assume
\[
0<a<1,\quad 0<b<1,\quad c>0,\quad
\left(1+(p-1)a\right)\left(1+(q-1)b\right)>pq c^2.
\]
These assumptions are precisely sufficient for positive definiteness in the stated parameter range. Let \(D=\operatorname{diag}(\pi_1,\ldots,\pi_{p+q})\), where \(\pi_i\ge0\) and \(\sum_i\pi_i=1\). The sharp guaranteed one-step expected squared-energy decrease from exact randomly selected coordinate minimization of the quadratic with Hessian \(C\) is
\[
\rho(\pi)=\lambda_{\min}(D^{1/2}CD^{1/2}).
\]
We determine \(\rho_*=\max_{\pi}\rho(\pi)\) and an optimal sampler with no numerical optimization. Define
\[
 u=\frac{1-a}{p},\qquad v=\frac{1-b}{q},\qquad
 r=a+u,\qquad s=b+v,\qquad \Delta=rs-c^2>0,
\]
\[
 t_0=\frac{v}{u+v},\qquad
 t_Q=\frac{s+c}{r+s+2c},\qquad
 \rho_Q=\frac{\Delta}{r+s+2c}.
\]
Here \(t\) denotes total sampling mass assigned to the first community. The globally optimal block-uniform sampler has \(\pi_i=t_*/p\) on the first community and \(\pi_j=(1-t_*)/q\) on the second. The following mutually exclusive rules provide \(t_*\) and \(\rho_*\):

1. **Two contrast modes:** if \(c^2\le ab\), then \(t_*=t_0\) and \(\rho_*=uv/(u+v)\).
2. **Pure community-mean mode:** if \(c^2>ab\) and either \(t_Q=t_0\), or \(t_Q<t_0\) with \(\rho_Q\le u t_Q\), or \(t_Q>t_0\) with \(\rho_Q\le v(1-t_Q)\), then \(t_*=t_Q\) and \(\rho_*=\rho_Q\).
3. **First-community contrast meets the mean mode:** if \(c^2>ab\), \(t_Q<t_0\), and \(\rho_Q>u t_Q\), then
\[
 t_*=\frac{as-c^2}{as-c^2+au},\qquad \rho_*=u t_*.
\]
4. **Second-community contrast meets the mean mode:** if \(c^2>ab\), \(t_Q>t_0\), and \(\rho_Q>v(1-t_Q)\), then
\[
 t_*=\frac{bv}{br-c^2+bv},\qquad \rho_*=v(1-t_*).
\]

All denominators in the applicable regimes are positive. Each block-uniform optimizer has a unique value of \(t_*\); uniqueness of the full unrestricted probability vector is not asserted. The boundary \(c^2=ab\) is sharp for the change away from the two-contrast solution. All four regimes occur for rational, strictly positive-definite four-coordinate matrices. Moreover, the optimal sharp decrease factor can exceed the decrease under uniform coordinate sampling by an arbitrarily large multiplicative factor as the dimension varies.

## Assumptions and scope

The quadratic is \(f(x)=\frac12(x-x_*)^T C(x-x_*)\), or equivalently a translated SPD quadratic with this Hessian. At every iteration one coordinate \(i\) is chosen independently with its fixed probability \(\pi_i\), and is minimized exactly while all others stay fixed. The energy metric is \(\|x-x_*\|_C^2\), or twice the objective gap. The value \(1-\rho(\pi)\) is the exact worst-case conditional one-step expected energy contraction factor, not an asserted exact finite-horizon convergence rate or optimality over adaptive, block, accelerated, or time-varying policies.

The block condition is not a sparsity constraint: all cross-community entries are the same positive correlation. Permutations within each community are symmetries. At the boundary \(c^2=ab\), the specified two-contrast rule is used. At equalities involving \(\rho_Q\), the pure mean-mode rule is used; the formulas agree by continuity. Every displayed candidate probability is positive.

## Proof

**Exact one-step criterion.** Write \(e=x-x_*\). Since \(C_{ii}=1\), the coordinate update gives \(e^+=e-(Ce)_i e_i\). Its squared-energy decrease is exactly \((Ce)_i^2\). Therefore
\[
\mathbb E[\|e^+\|_C^2\mid e]
=\|e\|_C^2-e^TCDCe.
\]
The smallest possible decrement divided by \(e^TCe\) is \(\lambda_{\min}(C^{1/2}DC^{1/2})\), which has the same eigenvalues as \(D^{1/2}CD^{1/2}\). Thus the displayed criterion is exact for every fixed probability vector, including at equality via a minimizing eigenvector.

**Unrestricted global symmetry reduction.** The map \(D\mapsto \lambda_{\min}(C^{1/2}DC^{1/2})\) is concave in the diagonal probabilities. Permuting probabilities within either community preserves the objective, since the corresponding permutation commutes with \(C\) and its positive square root. Jensen's inequality applied to the product of the two permutation groups shows that the group-average probability vector is at least as good as the original. Hence an unrestricted optimum can be chosen uniform within each community. Zero-probability distributions have zero minimum eigenvalue, while positive probabilities give a positive eigenvalue; an optimum exists in the interior.

**Exact spectrum.** Put total first-community mass \(t\in(0,1)\). The within-first zero-sum subspace has eigenvalue \(u t\), multiplicity \(p-1\); the within-second zero-sum subspace has eigenvalue \(v(1-t)\), multiplicity \(q-1\). The subspace of community-constant vectors has the symmetric matrix
\[
Q(t)=\begin{pmatrix}
rt & c\sqrt{t(1-t)}\\
c\sqrt{t(1-t)} & s(1-t)
\end{pmatrix}.
\]
Consequently, with \(g(t)=\lambda_{\min}(Q(t))\), the sharp rate is
\[
R(t)=\min\{ut,\ v(1-t),\ g(t)\},
\qquad
g(t)=\frac{rt+s(1-t)-\sqrt{(rt-s(1-t))^2+4c^2t(1-t)}}2.
\]
The positive-definiteness assumptions imply \(r,s>0\), \(\Delta=rs-c^2>0\), and \(g(t)>0\) for \(0<t<1\).

**Shape and maximum of the mean-mode eigenvalue.** The polynomial under the square root has the form \(At^2+Bt+E\) with \(4AE-B^2=16c^2\Delta>0\). Its square root is strictly convex on \((0,1)\); hence \(g\) is strictly concave, vanishes at the endpoints, and has a unique maximum. Indeed, for an arbitrary tentative rate \(z\),
\[
\det(Q(t)-zI)=\Delta t(1-t)-z\bigl(rt+s(1-t)\bigr)+z^2.
\]
At \(z=\rho_Q\), this concave quadratic in \(t\) has maximum zero, attained only at \(t_Q\). It follows that \(g(t)\le\rho_Q=g(t_Q)\), with strict inequality away from \(t_Q\). In particular \(g\) increases strictly up to \(t_Q\) and decreases strictly afterward.

**The threshold and remaining branches.** Let \(h(t)=\min\{ut,v(1-t)\}\). It increases linearly up to its unique maximum \(h(t_0)=uv/(u+v)\), and decreases afterward. At \(t_0\), the matrix \(Q(t_0)-h(t_0)I\) has diagonal entries \(a t_0\), \(b(1-t_0)\) and determinant \((ab-c^2)t_0(1-t_0)\). Thus \(g(t_0)\ge h(t_0)\) exactly when \(c^2\le ab\). This proves rule 1 globally (the universal bound \(R(t)\le h(t)\) is then attained). If \(c^2>ab\), we have \(R(t_0)=g(t_0)<h(t_0)\).

If \(t_Q=t_0\), the unique maximum of \(g\) is also optimal for \(R\). If \(t_Q<t_0\), on the interval left of \(t_Q\) both \(g\) and \(h=ut\) increase, while right of \(t_0\) both decrease. On \([t_Q,t_0]\), \(g\) decreases and \(ut\) increases. The optimum is therefore \(t_Q\) when \(g(t_Q)\le ut_Q\), otherwise the unique crossing \(g(t)=ut\). Substitution of \(z=ut\) in the preceding determinant gives
\[
\det(Q(t)-utI)=t\bigl((as-c^2)(1-t)-au t\bigr),
\]
so the crossing is exactly the value in rule 3. The analogous argument when \(t_Q>t_0\) compares \(g\) with \(v(1-t)\) on \([t_0,t_Q]\), and
\[
\det(Q(t)-v(1-t)I)=(1-t)\bigl((br-c^2)t-bv(1-t)\bigr)
\]
yields rule 4. If the mean-mode maximum lies below the corresponding contrast line, the optimum is \(t_Q\), proving rule 2. These monotonicities also establish uniqueness among block-uniform samplers.

**Four realized regimes.** Take \(p=q=2\). The tuples \((a,b,c;t_*,\rho_*)\) equal
\[
\begin{array}{c|c|c}
(a,b,c)&t_*&\rho_*\\\hline
(1/5,1/5,1/5)&1/2&1/5\\
(1/5,1/5,1/4)&1/2&7/40\\
(2/5,1/5,1/3)&29/56&87/560\\
(1/5,2/5,1/3)&27/56&87/560
\end{array}
\]
respectively representing two contrasts, pure means, first contrast/means, and second contrast/means. Each meets the strict SPD assumptions, and each identity follows by substitution into the formulas.

**Unbounded advantage over uniform sampling.** For integer \(q\ge2\), set \(p=2\), \(a=1-q^{-2}\), \(b=1/2\), and \(c=1/4\). Because \(c^2\le ab\), the optimal guaranteed decrease is \(\rho_*=1/(2q(q+1))\). Moreover, \(C\succeq q^{-2}I\), since it decomposes into the diagonal \(\operatorname{diag}(q^{-2}I_2,(1/2)I_q)\) plus the positive semidefinite matrices \((a-c)J_2\oplus0\), \(0\oplus(b-c)J_q\), and \(cJ_{q+2}\). The first-community contrast eigenvalue is exactly \(q^{-2}\), so uniform sampling has sharp rate \(\rho_{\mathrm{unif}}=1/(q^2(q+2))\). Therefore
\[
\frac{\rho_*}{\rho_{\mathrm{unif}}}
=\frac{q(q+2)}{2(q+1)}\longrightarrow\infty.
\]
This compares worst-case one-step rates within the same exact-coordinate-update model; no wall-clock or other algorithmic claim is made.

## Verification

The standalone standard-library script `artifacts/verify.py` performs exact rational computations. It verifies attainment by a full-matrix positive-semidefinite test on 13,070 positive-definite examples for community sizes from two to six, checks 91,843 distinct non-improvement inequalities for block-uniform and nonsymmetric probability choices, exercises every phase, checks four exact rational witnesses, and tests the unbounded-gain construction for \(2\le q\le24\). Each inequality uses rational Schur-complement elimination, rather than floating-point eigensolvers. Run `python3 artifacts/verify.py` from the extracted package root. These finitely many computations do not replace the proof for infinitely many parameters or dimensions.

## Relationship to prior work

Gower and Richtárik (2015), *Randomized Iterative Methods for Linear Systems*, derive the general exact smallest-eigenvalue sampling objective and the optimal-distribution semidefinite program (their Section 5.1, especially equations (5.3)–(5.4)); they do not evaluate this particular two-community family or its phase thresholds in the inspected text. Richtárik and Takáč (2013), *On Optimal Probabilities in Stochastic Coordinate Descent Methods*, optimize a different worst-case complexity bound rather than the exact one-step quadratic-energy eigenvalue. Qu and Richtárik (2014), *Coordinate Descent with Arbitrary Sampling I*, cover arbitrary sampling in a broad algorithmic framework without an explicit two-community probability classification.

Pukelsheim and Torsney (1991), *Optimal Weights for Experimental Designs on Linearly Independent Support Points*, provide the corresponding general E-optimal-design viewpoint and a fixed-point characterization; their closed-form formula is for A-optimality, and their inspected E-optimal statements do not contain the four-phase formulas here. The published *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* establishes a formula under \(C^{-1}\ge0\); that hypothesis cannot hold for this strictly positive, nondiagonal matrix \(C\), since an invertible nonnegative matrix with nonnegative inverse must be monomial.

## Limitations

The optimizer's explicit formula is a symmetry-classification result, not a claim that the general semidefinite sampling problem is new. Older E-optimal-design, diagonal-scaling, and structured-covariance literature could contain equivalent expressions under different terminology; publication priority requires further independent literature confirmation. Only the sharp conditional one-step expected energy decrease is optimized. No claim is made for adaptive coordinate rules, independent finite-horizon optimality, simultaneous updates, or execution-time advantage. The stated positive-correlation and SPD hypotheses exclude signed correlations and singular boundary matrices. Independent audit has not been performed.

## References

1. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (first posted 2015-06-10); Section 5.1. https://arxiv.org/abs/1506.03296
2. P. Richtárik and M. Takáč, *On Optimal Probabilities in Stochastic Coordinate Descent Methods*, arXiv:1310.3438 (first posted 2013-10-13). https://arxiv.org/abs/1310.3438
3. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling I: Algorithms and Complexity*, arXiv:1412.8060 (first posted 2014-12-27). https://arxiv.org/abs/1412.8060
4. F. Pukelsheim and B. Torsney, *Optimal Weights for Experimental Designs on Linearly Independent Support Points*, Annals of Statistics 19(3) (1991), 1614–1625. https://doi.org/10.1214/aos/1176348265 ; lawful full text https://www.math.uni-augsburg.de/htdocs/emeriti/pukelsheim/1991d.pdf
5. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* (published mathematical result), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995
