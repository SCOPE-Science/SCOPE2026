# Sharp involution conditioning and a symmetry-breaking threshold for three-step nilpotents

## Finding

For \(c\in\mathbb C\), let \(N_c\) act on complex Euclidean \(\mathbb C^3\) by
\[
N_c=\begin{pmatrix}0&1&c\\0&0&1\\0&0&0\end{pmatrix},
\qquad \rho=|c|.
\]
An involution means a complex-linear operator \(J\) satisfying \(J^2=I\), with no self-adjointness assumption. Define its optimal negative-conjugation norm
\[
\mu(c)=\min\big\{\|J\|_{2\to2}:J^2=I,\ JN_c=-N_cJ\big\}.
\]
The minimum exists and has the exact value
\[
\boxed{\mu(c)=p(\rho)+\sqrt{p(\rho)^2-1}},\qquad
p(\rho)=\begin{cases}1+\rho^2/4,&0\le\rho\le2,\\\rho,&\rho\ge2.\end{cases}
\]
The optimal spectral-condition number among these involutions is \(\mu(c)^2\), since \(J^{-1}=J\).

All minimizing involutions are explicitly classified. When \(c=0\), they are exactly \(\pm\operatorname{diag}(1,-1,1)\). For \(c\ne0\), put \(\zeta=c/|c|\) and
\[
J_{r,s}=\begin{pmatrix}
1&-2\zeta r&-2\zeta^2rs\\
0&-1&-2\zeta s\\
0&0&1
\end{pmatrix}.
\]
Every minimizer is \(\pm J_{r,s}\), where \(r+s=\rho\) and
\[
(r,s)=\begin{cases}
(\rho/2,\rho/2),&0<\rho\le2,\\
((\rho+\sqrt{\rho^2-4})/2,(\rho-\sqrt{\rho^2-4})/2)
\text{ or the reversed ordered pair},&\rho>2.
\end{cases}
\]
Thus the symmetric optimizer is unique modulo sign up to the threshold \(\rho=2\); beyond it, exactly two nonsymmetric optimizers emerge. The minimal norm is continuously differentiable but not twice differentiable at \(\rho=2\).

## Assumptions and scope

All norms are the spectral operator norm induced by the standard Hermitian inner product on \(\mathbb C^3\). The two adjacent superdiagonal entries of \(N_c\) are normalized to \(1\); the shortcut entry \(c\) is arbitrary complex. Neither an extra invariant orthogonal decomposition nor a diagonal, self-adjoint, unitary, or real-valued condition on \(J\) is imposed. The extremizer classification is in the displayed fixed coordinate basis.

## Proof

**1. Exhaustion of all possible involutions.** We have \(N_c^3=0\) and \(N_c^2\ne0\). If \(JN_c=-N_cJ\), then \(J\) preserves both \(\ker N_c=\operatorname{span}\{e_1\}\) and \(\ker N_c^2=\operatorname{span}\{e_1,e_2\}\). Consequently \(J\) is upper triangular. The \((1,2)\) and \((2,3)\) entries of the anticommutation relation force the diagonal entries to be \((\varepsilon,-\varepsilon,\varepsilon)\). The diagonal entries of \(J^2=I\) imply \(\varepsilon\in\{1,-1\}\). Multiplying by \(\varepsilon\), which changes neither norm nor constraints, gives diagonal \((1,-1,1)\). With first and second superdiagonal parameters \(x,z\), the \((1,3)\) entries of \(JN_c+N_cJ=0\) and \(J^2=I\) then give, respectively, \(x+z=-2c\) and the remaining entry \(-xz/2\). Hence the complete solution set is
\[
J=\pm\begin{pmatrix}1&x&-xz/2\\0&-1&z\\0&0&1\end{pmatrix},
\qquad x,z\in\mathbb C,\quad x+z=-2c.
\tag{1}
\]
Direct multiplication verifies the converse.

**2. Reflection norm and rank-one geometry.** For the positive-diagonal-sign representative in (1), \(Q=(I-J)/2\) is the rank-one idempotent
\[
Q=vw^*,\qquad v=(-x/2,1,0)^\mathsf T,\qquad
w^*=(0,1,-z/2),\qquad w^*v=1.
\]
Thus
\[
p:=\|Q\|=\|v\|_2\|w\|_2
=\sqrt{(1+|x|^2/4)(1+|z|^2/4)}\ge1.
\]
A rank-one idempotent on a Hilbert space has an orthonormal two-dimensional reduction \(\left(\begin{smallmatrix}1&u\\0&0\end{smallmatrix}\right)\), where \(|u|=\sqrt{p^2-1}\); its complement is zero. Therefore the nontrivial block of \(I-2Q\) is \(\left(\begin{smallmatrix}-1&-2u\\0&1\end{smallmatrix}\right)\). Its larger singular value is \(p+\sqrt{p^2-1}\), while the remaining one-dimensional block has singular value \(1\). This includes \(p=1\) by direct inspection. Hence
\[
\|J\|=p+\sqrt{p^2-1}.
\tag{2}
\]
The right-hand side is strictly increasing in \(p\) for \(p\ge1\).

**3. Global constrained minimization.** Put \(r=|x|/2\), \(s=|z|/2\), and \(\rho=|c|\). Equation (1) implies \(r+s\ge\rho\). When \(\rho>0\) and \(r+s>\rho\), scaling both nonnegative radii by \(\rho/(r+s)\) strictly decreases \((1+r^2)(1+s^2)\) and produces a feasible pair with radii summing to \(\rho\), realized by \(x=-2\zeta r\), \(z=-2\zeta s\). Thus every minimizer has \(r+s=\rho\), and equality in the complex triangle inequality forces \(x,z\) to have the same direction as \(-c\). For \(\rho=0\), the minimum occurs only at \(x=z=0\).

On the boundary \(r+s=\rho\), the key exact identity is
\[
p^2=(1+r^2)(1+s^2)=\rho^2+(rs-1)^2,
\qquad 0\le rs\le\rho^2/4.
\tag{3}
\]
If \(0<\rho\le2\), the allowable product is at most \(1\), so the unique optimum is \(rs=\rho^2/4\), forcing \(r=s=\rho/2\). Substitution into (3) gives \(p=1+\rho^2/4\). If \(\rho>2\), the attainable product \(rs=1\) uniquely minimizes (3) in product space. The two solutions of \(r+s=\rho\), \(rs=1\) are the ordered pairs stated above, with \(p=\rho\). Equations (2)–(3) prove the exact formula and all equality cases.

**4. Threshold regularity and comparison to a canonical construction.** The two branches of \(p(\rho)\) agree with identical first derivative at \(\rho=2\), but their second derivatives are \(1/2\) and \(0\). Since \(u\mapsto u+\sqrt{u^2-1}\) is smooth with positive derivative at \(u=2\), the same second-derivative mismatch holds for \(\mu\). A convenient nonoptimal involution is obtained by \(x=0\), \(z=-2c\); its norm is \(\rho+\sqrt{1+\rho^2}\). Formula (3) shows the optimal value is strictly smaller for every finite \(\rho>0\), including above the threshold.

## Verification

The accompanying `CHECK.py` runs independent matrix-multiplication and spectral-norm checks for real and complex shortcut parameters, tests the explicit optimizers, compares thousands of feasible complex perturbations to the sharp lower bound, and checks the structural identities symbolically. The program prints `THREE_STEP_INVOLUTION_NORM_DIAGNOSTIC_OK 22463`. The continuum-wide conclusion, including all equality cases, follows from the preceding proof rather than numerical sampling. Reproduction: `python CHECK.py`, requiring Python, NumPy, and SymPy.

## Relationship to prior work

Aouichaoui, *Optimal lengths of commutators of idempotents and similarity of nilpotent operators to their negatives* (arXiv:2611.01316v1, first posted 31 October 2026), Section 4, considers three-block nilpotents with identical adjacent blocks and a variable long-range block. It establishes existence/nonexistence criteria for bounded anticommuting involutions in infinite-dimensional families and gives an explicit one-sided upper triangular involution. The present finite-dimensional theorem instead finds the minimum possible spectral norm, its equality cases, and its symmetry-breaking transition on the scalar three-step specialization. The norm optimum does not follow from the existence criterion alone; notably, the displayed one-sided construction has the strictly larger norm computed above.

Marcoux, Radjavi and Zhang, *Around the closure of the set of commutators of idempotents in B(H): Biquasitriangularity and factorisation* (J. Funct. Anal. 284 (2023), 109854), study operator factorization and similarity questions. The available abstract and the precise questions cited in Aouichaoui's full text concern qualitative factorization/similarity, not the quantitative optimization proved here. The complete 2023 paper could not be compared, so equivalent quantitative material there is an acknowledged residual bibliographic risk.

## Limitations

The theorem concerns precisely the normalized complex three-dimensional nilpotent family above and the spectral operator norm of involutions; it does not determine costs for general weighted nilpotent chains, non-involutive similarities, block-operator extensions, or other operator norms. The supplemental diagnostics are finite tests, not proofs. The originality assessment is limited by incomplete access to the 2023 full text and by the possibility of unindexed equivalents. Independent verification has not been performed.

## References

1. Mohamed Amine Aouichaoui, *Optimal lengths of commutators of idempotents and similarity of nilpotent operators to their negatives*, arXiv:2611.01316v1 (2026-10-31), Section 4. https://arxiv.org/html/2611.01316v1
2. Laurent W. Marcoux, Heydar Radjavi and Yuanhang Zhang, *Around the closure of the set of commutators of idempotents in B(H): Biquasitriangularity and factorisation*, Journal of Functional Analysis 284 (2023), 109854. https://doi.org/10.1016/j.jfa.2023.109854
3. Bernard Mutuku Nzimbi et al., *On Some n-Involution and k-Potent Operators on Hilbert Spaces* (2017), Section 4 (involution–idempotent correspondence). https://doi.org/10.11648/j.mcs.20170206.11
