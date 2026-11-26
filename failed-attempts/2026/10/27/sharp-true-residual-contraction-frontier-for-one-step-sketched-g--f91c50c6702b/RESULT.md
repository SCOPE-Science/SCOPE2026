# Sharp true-residual contraction frontier for one-step sketched GMRES on SPD systems

## Finding

For a real SPD linear system, one restarted sketched GMRES step seeks the scalar minimizing the sketched norm of the residual along its first Krylov direction. When the sketch is a squared-norm \(\varepsilon\)-embedding on the two vectors used by this step, the *exact* worst-case multiplicative factor for the **unsketched Euclidean residual** is

\[
q_\star(\kappa,\varepsilon)=\frac{\kappa-1}{(\kappa+1)\sqrt{1-\varepsilon^2}},\qquad 0\le\varepsilon<1.
\]

For \(\kappa>1\), all such steps contract the true residual uniformly if and only if

\[
\varepsilon<\frac{2\sqrt\kappa}{\kappa+1}.
\]

At the boundary, an admissible sketch can make the update vanish, so keeping that sketch in subsequent cycles makes the method stagnate at a nonzero residual. The factor and this obstruction are attained on a two-coordinate SPD system. In particular, the displayed strict condition permits a uniform geometric residual estimate even if admissible sketches are chosen adaptively between cycles.

## Assumptions and scope

Let \(d\ge1\), let \(A=A^{\mathsf T}\in\mathbb R^{d\times d}\) satisfy \(\mu I\preceq A\preceq LI\), with \(0<\mu\le L\), and write \(\kappa=L/\mu\). Given any nonzero current residual \(r=b-Ax\), choose any real linear sketch \(S\) of arbitrary output dimension obeying

\[
(1-\varepsilon)\|z\|_2^2\le\|Sz\|_2^2\le(1+\varepsilon)\|z\|_2^2
\quad\text{for all }z\in\operatorname{span}\{r,Ar\},
\]

with \(0\le\varepsilon<1\). Compute \(t=\arg\min_{t\in\mathbb R}\|S(r-tAr)\|_2\) and update \(x_+=x+tr\), so \(r_+=r-tAr\). The minimizer exists uniquely because \(SAr\ne0\). A new admissible sketch may be selected at every restart. The assertion is deterministic, uses the true residual norm, and assumes exact arithmetic; it makes no floating-point, sketch-randomness, or operation-count claim.

## Proof

**Step 1: exact worst distortion of a one-dimensional least-squares projection.** Normalize \(v=Ar/\|Ar\|_2\). Choose any unit \(w\perp v\) such that

\[
r/\|r\|_2=cv+sw,\quad c=\frac{\langle r,Ar\rangle}{\|r\|_2\|Ar\|_2}>0,\quad s=\sqrt{1-c^2}.
\]

The case \(s=0\) has \(r_+=0\). Otherwise restrict the symmetric sketch Gram operator \(S^{\mathsf T}S\) to the orthonormal pair \((v,w)\), with matrix \(\begin{psmallmatrix}a&d\\d&b\end{psmallmatrix}\). By assumption its eigenvalues lie in \([1-\varepsilon,1+\varepsilon]\) and \(a>0\). Direct substitution in the scalar normal equation yields

\[
\frac{r_+}{\|r\|_2}=s\left(w-\frac da v\right),\qquad
\frac{\|r_+\|_2^2}{\|r\|_2^2}=s^2\left(1+\frac{d^2}{a^2}\right).
\]

The bound \(\|M-I\|_2\le\varepsilon\) implies \((a-1)^2+d^2\le\varepsilon^2\). On \(1-\varepsilon\le a\le1+\varepsilon\), elementary completion of squares gives

\[
\frac{d^2}{a^2}\le\frac{\varepsilon^2-(a-1)^2}{a^2}
\le\frac{\varepsilon^2}{1-\varepsilon^2},
\]

because the difference after clearing the positive denominator is proportional to \((a-(1-\varepsilon^2))^2\). Both inequalities are sharp: for either sign take the Gram restriction

\[
M_\pm=\begin{pmatrix}
1-\varepsilon^2&\pm\varepsilon\sqrt{1-\varepsilon^2}\\
\pm\varepsilon\sqrt{1-\varepsilon^2}&1+\varepsilon^2
\end{pmatrix}.
\]

Its eigenvalues are exactly \(1\pm\varepsilon\), hence it is the Gram matrix of an admissible real sketch. The sharp factor for a *fixed* residual direction is therefore \(s/\sqrt{1-\varepsilon^2}\).

**Step 2: worst Euclidean angle for SPD matrices.** Normalize \(\|r\|_2=1\), and put \(m=\langle r,Ar\rangle\). Positivity of \((A-\mu I)(LI-A)\) implies \(\|Ar\|_2^2\le(L+\mu)m-\mu L\). Minimizing the resulting lower bound \(m^2/[(L+\mu)m-\mu L]\) over \(m\in[\mu,L]\) gives

\[
c\ge\frac{2\sqrt{\mu L}}{\mu+L},\qquad s\le\frac{L-\mu}{L+\mu}=\frac{\kappa-1}{\kappa+1}.
\]

Equality is attained by \(A=\operatorname{diag}(\mu,L)\) and \(r=(\sqrt L,\sqrt\mu)^{\mathsf T}/\sqrt{L+\mu}\). Combining Step 1 and Step 2 gives the asserted *attained* exact worst factor. If \(\kappa=1\), then \(Ar=\mu r\) and the least-squares solve eliminates the residual exactly.

**Step 3: sharp uniform convergence frontier and boundary counterexample.** When \(\kappa>1\), the condition \(q_\star<1\) is algebraically equivalent to \(\varepsilon<2\sqrt\kappa/(\kappa+1)\). Iteration of the one-step estimate proves \(\|r_n\|_2\le q_\star^n\|r_0\|_2\) for arbitrary changing admissible sketches, provided every step satisfies the stated embedding assumption on its own two-vector subspace.

For necessity, choose the two-coordinate equality configuration above and write \(c=2\sqrt\kappa/(\kappa+1)\), \(s=(\kappa-1)/(\kappa+1)\). At the critical value \(\varepsilon=c\), use \(M_-\) from Step 1 with basis \((v,w)\). Then \(d/a=-c/s\), so the sketched normal-equation numerator is exactly zero and \(t=0\). This *same* sketch is admissible whenever the permitted distortion \(\varepsilon\ge c\); repeated one-vector restarts therefore preserve the nonzero residual forever. This proves necessity of the strict threshold. It also proves the sharpness statement at equality without confusing absence of a guarantee with divergence.

## Verification

The accompanying standard-library script `verify.py` uses exact rational arithmetic for a two-dimensional sharpness witness, including a critical-distortion stagnation case. It constructs the sketch Gram matrix independently, verifies its eigenvalues through trace/determinant, computes the scalar sketched minimizer from the original normal equation, and checks the squared true-residual identity. It also tests 2,500+ rational examples against the claimed global factor. Finite tests corroborate the derivation and cannot establish the universal assertions, which follow from the proof above. Run with `python verify.py`.

## Relationship to prior work

The definition and residual formulation of sketched GMRES are due to Nakatsukasa and Tropp (2021/2022), whose accessible manuscript, Section 3.2, gives the general relative quasi-optimality estimate for a sketched least-squares solve. Burke, Güttel, and Soodhalter (2023/2024), Section 4, analyze sketched residual projectors, sketched angles, and harmonic Ritz recycling. Güttel, Liu, and Nyman (2026) develop sketched harmonic Arnoldi restarting for matrix functions, motivating exact parameter-dependent stability benchmarks. These methods, and the classical SPD residual-angle/Kantorovich inequality, are not claimed as new.

The claim assessed here is specifically the **joint, necessary-and-sufficient, sharp deterministic frontier** for the *true one-cycle Euclidean residual*, with a common explicit two-dimensional extremizer and a fixed-sketch stagnation obstruction for one-step restarting. A generic multiplicative quasi-optimality bound does not provide this exact factor or its converse; an earlier spectral-sign threshold for sketched Ritz values does not bound the true GMRES residual norm. Both components of the proof use familiar inequalities, so earlier equivalently sharp specialized treatments cannot be ruled out exhaustively.

## Limitations

The result addresses real SPD matrices, one-dimensional Krylov cycles, exact sketch-based least squares and a deterministic subspace-embedding inequality. It neither proves analogous higher-restart-length sharp factors nor bounds practical floating-point effects, random sketch failure rates, or runtime savings. The example at the frontier is adversarial; it does not assert that common randomized sketches typically stagnate. No independent validation is asserted.

## References

1. S. Güttel, J. Liu, L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354v1 (first public July 11, 2026), https://arxiv.org/abs/2607.10354 .
2. Y. Nakatsukasa, J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113v2, https://arxiv.org/html/2111.00113v2 .
3. L. Burke, S. Güttel, K. M. Soodhalter, *GMRES with randomized sketching and deflated restarting*, arXiv:2311.14206v2, https://arxiv.org/html/2311.14206v2 .
