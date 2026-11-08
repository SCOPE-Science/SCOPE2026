# An optimal rank-one coarse correction for equicorrelated sketched-block preconditioning

## Finding

A memory-efficient block preconditioner for Nyström kernel ridge regression can entirely fail to improve the condition number on a fully coherent, positive-definite kernel family. For this family, **one positive rank-one correction is sufficient and globally optimal among all positive semidefinite corrections of rank at most one**. The corrected condition number is independent of the number of blocks at fixed block size.

For integers \(q,s\ge2\) and \(m=qs\), let \(0<\rho<1\), \(\lambda>0\), and \(a=1-\rho\). Use the equicorrelation center Gram matrix

\[
K=aI_m+\rho\mathbf1_m\mathbf1_m^{\mathsf T}.
\]

Let the training set consist of \(t\ge2\) identical copies of every center, with \(n=tm\). The Nyström normal matrix and exact-block-sketch denominator are

\[
H=\frac nmK^2+\lambda nK,\qquad
B=\bigoplus_{j=1}^{q}nq\left(\frac1s K_s^2+\lambda K_s\right),
\quad K_s=aI_s+\rho\mathbf1_s\mathbf1_s^{\mathsf T}.
\]

Put \(b=a+m\rho\), \(c=a+s\rho\), and

\[
\begin{aligned}
h_a&=na(a/m+\lambda),&h_b&=nb(b/m+\lambda),\\
d_a&=nqa(a/s+\lambda),&d_c&=nqc(c/s+\lambda).
\end{aligned}
\]

The three exact generalized eigenvalues of \((H,B)\) are

\[
\underbrace{h_a/d_c}_{q-1},\qquad
\underbrace{h_a/d_a}_{m-q},\qquad
\underbrace{h_b/d_c}_{1},
\]

in strictly increasing order. Therefore

\[
\kappa(B^{-1/2}HB^{-1/2})=h_b/h_a=\kappa(H).
\]

For every \(W\succeq0\) with \(\operatorname{rank}(W)\le1\), the sharp optimum is

\[
\boxed{\inf_W\kappa((B+W)^{-1/2}H(B+W)^{-1/2})
=\frac{d_c}{d_a}=\frac{c(c+\lambda s)}{a(a+\lambda s)}.}
\]

Write \(P=\mathbf1_m\mathbf1_m^{\mathsf T}/m\). Equality is attained by \(W=\tau P\) **exactly** for

\[
\boxed{\tau\in[\tau_-,\tau_+]}
\qquad\text{where}\qquad
\tau_-=d_a\frac{h_b}{h_a}-d_c,
\quad \tau_+=d_c\left(\frac{h_b}{h_a}-1\right).
\]

This interval is nonempty and has strictly positive lower endpoint. At \(\tau=\tau_-\) or \(\tau=\tau_+\), the corrected matrix has exactly two distinct generalized eigenvalues, so preconditioned conjugate gradients terminates within two iterations in exact arithmetic. Its inverse uses the original block inverse and one global scalar projection:

\[
(B+\tau P)^{-1}=B^{-1}-\frac{\tau}{d_c(d_c+\tau)}P.
\]

## Assumptions and scope

The kernel is a positive-definite compound-symmetry Gram matrix on distinct centers. Repeating each training center \(t\) times is an admissible deterministic Nyström training configuration with \(m<n\). The same kernel and regularization are used in all blocks. Blocks partition all center indices into \(q\) equal sets of size \(s\). All calculations are real and in exact arithmetic. The preconditioner denominator \(B\) is the full within-block-sketch version of the stated sketched block-Jacobi construction, **not** the exact block diagonal of \(H\). A coarse update is applied to the positive denominator before inversion. The optimization ranges over all symmetric positive semidefinite \(m\)-by-\(m\) matrices of rank at most one, without a norm bound on the update. No optimization over indefinite rank-one updates is claimed.

## Proof

**1. Simultaneous invariant subspaces.** The training-by-center kernel is \(t\) vertical copies of \(K\), so \(K_{nm}^{\mathsf T}K_{nm}=tK^2=(n/m)K^2\), giving the displayed \(H\). The all-ones vector spans a one-dimensional invariant subspace \(G\). The subspace \(V\) of blockwise-constant vectors with global sum zero has dimension \(q-1\). The subspace \(U\) of vectors summing to zero within each block has dimension \(m-q=q(s-1)\). Their orthogonal direct sum is all of \(\mathbb R^m\). On \(G\), the eigenvalues of \(H,B\) are \(h_b,d_c\); on \(V\) they are \(h_a,d_c\); and on \(U\) they are \(h_a,d_a\). Hence the complete generalized eigenvalue list follows, with stated multiplicities.

**2. Strict ordering.** Since \(c>a\), the scalar function \(x\mapsto x(x/s+\lambda)\) is strictly increasing, hence \(d_c>d_a\), giving \(h_a/d_c<h_a/d_a\). To verify \(h_b/h_a>d_c/d_a\), write

\[
G(z)=\frac{(a+\rho z)(a+(\rho+\lambda)z)}{a(a+\lambda z)}
=1+\frac{\rho z(2a+(\rho+\lambda)z)}{a(a+\lambda z)}.
\]

For \(z>0\), its derivative is positive: each of \(z/(a+\lambda z)\) and \(z^2/(a+\lambda z)\) is strictly increasing. The two ratios equal \(G(m)\) and \(G(s)\), respectively, and \(m>s\). Thus \(h_b/d_c>h_a/d_a\). The largest-to-smallest ratio is therefore \((h_b/d_c)/(h_a/d_c)=h_b/h_a\), exactly the condition number of \(H\).

**3. Sharp lower bound for every rank-one positive correction.** Fix an arbitrary \(W\succeq0\), \(\operatorname{rank}(W)\le1\). Since \(\dim U=q(s-1)\ge2\), a nonzero \(u\in U\cap\ker W\) exists. The generalized Rayleigh quotient of \((H,B+W)\) at \(u\) is \(h_a/d_a\). Consequently its largest eigenvalue is at least this value. On the nonzero subspace \(V\), for every \(v\ne0\),

\[
\frac{v^{\mathsf T}Hv}{v^{\mathsf T}(B+W)v}
\le\frac{h_a}{d_c},
\]

because \(v^{\mathsf T}Wv\ge0\). The smallest generalized eigenvalue is thus at most \(h_a/d_c\). Dividing yields the uniform lower bound \(\kappa\ge d_c/d_a\). This does not presume the correction commutes with \(B\) or is aligned with the global mode.

**4. Attainment and exact tuning interval.** Since \(BP=d_cP\), the update \(B+\tau P\) leaves the eigenvalues on \(U\) and \(V\) unchanged and replaces the global eigenvalue by \(h_b/(d_c+\tau)\). The total condition number attains \(d_c/d_a\) exactly when this third eigenvalue lies between \(h_a/d_c\) and \(h_a/d_a\), equivalent by cross-multiplication to \(\tau_-\le\tau\le\tau_+\). Monotonicity from Step 2 implies \(\tau_->0\), and

\[
\tau_+-\tau_-=(d_c-d_a)h_b/h_a>0.
\]

At either endpoint the global eigenvalue coincides with a preexisting one. Finally, splitting into the \(P\) and \(I-P\) eigenspaces of \(B\) gives the inverse formula directly (equivalently, by the Sherman–Morrison identity).

**5. Dimension dependence.** The original condition number diverges at fixed \(s,\rho,\lambda\) as \(q\to\infty\):

\[
\frac{\kappa(H)}m\longrightarrow
\frac{\rho(\rho+\lambda)}{(1-\rho)\lambda}.
\]

The corrected sharp ratio \(d_c/d_a\) does not depend on \(q\) or on the replication factor \(t\). The proof is complete.

## Verification

The included `verify_coarse_rankone.py` runs exact-rational checks over varied block counts, block widths, correlation and regularization values, then independently constructs the full kernel, Nyström normal matrix and block denominator for direct matrix eigenvalue tests. Two small cases are checked in exact symbolic linear algebra. It also tests positive semidefinite rank-one competitors and the inverse update identity. It passed 4,216 assertions; these finite tests corroborate rather than replace the proof.

For the illustrative choice \(q=s=t=2\), \(\rho=1/2\), \(\lambda=1/10\), the generalized eigenvalues are \(3/68\), \(9/28\) (multiplicity two), and \(145/204\). The uncorrected condition number is \(145/9\), while the globally rank-one optimal value is \(51/7\). The optimal projector interval is \([1112/45,4624/15]\).

## Relationship to prior work

Vitale and collaborators introduced sketched block-Jacobi preconditioning for Nyström kernel ridge regression and explicitly suggested future coarse corrections for inter-block coupling. Their original comparisons of block-preconditioning strategies do not calculate the present sharp positive rank-one minimax correction on equicorrelated duplicated-center data. General two-level multigrid theory, including Xu–Zikatanov, motivates coarse spaces but treats different abstract correction and convergence formulations, rather than the explicit constrained positive-denominator perturbation with the scalar sharp tuning interval here. Prior block-Jacobi scaling results address scaling rather than this fixed-denominator, rank-constrained coarse update. The existence of a broader older spectral interlacing lemma that could subsume the lower-bound step is acknowledged.

## Limitations

This is a structured exact-arithmetic theorem for strictly positive equicorrelation, equal-size blocks, replicated training centers and full within-block sketches. It does not show a comparable rank-one remedy for general kernels, heterogeneous blocks, independently randomized sketch realizations, finite-precision implementation or noisy data. The derived condition number is a spectral worst-case quantity, not measured wall-clock convergence or predictive accuracy. Generic low-rank interlacing is classical and is not claimed new; the assessed contribution is its complete, sharp specialization to this recently proposed block preconditioner, including explicit achievable tuning and dimension dependence.

## References

1. Giordano Vitale, Giacomo Meanti, Marco Rando, Blanca Ayuso de Dios and Lorenzo Rosasco, *BLOKS: Scaling Kernel Solvers with Sketched Block Preconditioning*, arXiv:2610.13382, first posted 2026-10-09, https://arxiv.org/abs/2610.13382.
2. Jinchao Xu and Ludmil T. Zikatanov, *Algebraic Multigrid Methods*, arXiv:1611.01917, https://arxiv.org/abs/1611.01917.
3. James Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, DOI:10.1137/22M1504901, https://doi.org/10.1137/22M1504901.
