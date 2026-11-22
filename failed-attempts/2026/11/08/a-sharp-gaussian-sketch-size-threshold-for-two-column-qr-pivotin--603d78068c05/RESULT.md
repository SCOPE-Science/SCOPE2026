# A sharp Gaussian sketch-size threshold for two-column QR pivoting

## Finding

Consider the first pivot of Gaussian-sketched QR with column pivoting, followed by exact projection onto the selected original column. For every full-column-rank real matrix \(A=[a\ b]\in\mathbb R^{m\times2}\) with \(\|b\|_2=t\|a\|_2\), \(t>1\), and \(\rho=\langle a,b\rangle/(\|a\|_2\|b\|_2)\in(-1,1)\), draw \(G\in\mathbb R^{k\times m}\) with independent standard-normal entries, for an arbitrary integer \(k\ge1\). Select whichever of the two columns of \(GA\) has larger Euclidean norm; project \(A\) onto the selected **original** column. Let \(E\) be the resulting squared Frobenius error divided by the minimum squared Frobenius error among the two one-column projections (not by the unconstrained best rank-one SVD error).

Define
\[
D=\sqrt{(t^2+1)^2-4t^2\rho^2},\qquad
\theta=\frac{D+1-t^2}{2D},\qquad
I_z(\alpha,\beta)=\frac{\int_0^z u^{\alpha-1}(1-u)^{\beta-1}\,du}{\int_0^1 u^{\alpha-1}(1-u)^{\beta-1}\,du}.
\]
Then the wrong-pivot probability and exact expected relative squared error are
\[
\boxed{\Pr\{E=t^2\}=I_{\theta}(k/2,k/2),\qquad
\mathbb E E=1+(t^2-1)I_{\theta}(k/2,k/2).}
\]
For fixed \(t>1\), both quantities are maximal among all correlations at \(\rho=0\); consequently
\[
\boxed{\sup_{|\rho|<1}\mathbb EE
=1+(t^2-1)I_{1/(1+t^2)}(k/2,k/2).}
\]
This gives a sharp **uniform-over-input sketch-size threshold**: with one Gaussian sketch row, \(\sup_{A}\mathbb EE=\infty\); with any \(k\ge2\), \(\mathbb EE<2\) for every full-rank two-column input. For two sketch rows, \(\sup_A\mathbb EE=2\), approached by orthogonal columns of diverging norm ratio. For four sketch rows, the sharper attained supremum is
\[
\boxed{\sup_A\mathbb EE=\frac{17+7\sqrt7}{27},\quad
\text{attained exactly when }\rho=0,\quad
 t^2=\frac{5+2\sqrt7}{3}.}
\]
For every fixed \(|\rho|<1\) and integer \(k\ge1\), the high-contrast asymptotic is
\[
\mathbb EE-1\sim
\frac{2\Gamma(k)}{k\Gamma(k/2)^2}(1-\rho^2)^{k/2}t^{2-k}
\quad(t\to\infty).
\]
Thus the expected excess grows linearly for one row, tends to \(1-\rho^2\) for two rows, and vanishes for three or more rows. These claims concern a single sketched pivot; subsequent verification, correction, or additional pivots can change the outcome.

## Assumptions and scope

All matrices and sketches are real; \(m\ge2\), \(k\ge1\), \(t>1\), \(\rho\in(-1,1)\), and the sketch entries are independent \(N(0,1)\). The column-projection approximation is \(\widehat A=cc^{\mathsf T}A/(c^{\mathsf T}c)\), where \(c\in\{a,b\}\) is selected by comparing \(\|Ga\|_2\) and \(\|Gb\|_2\). Equal sketched norms have probability zero under these assumptions. The all-input suprema allow arbitrary \(m\ge2\) and arbitrary nonzero independent column pairs. No assumption about a numerical tolerance, data distribution, or subsequent QR steps is made. Standard-normal scaling can be replaced by any common positive Gaussian variance without changing pivot decisions.

## Proof

**1. Exact loss from either pivot.** Rescale so \(\|a\|_2=1\). Set \(s=\sqrt{1-\rho^2}>0\), and select orthonormal vectors \(e_1,e_2\) with \(a=e_1\) and \(b=t(\rho e_1+s e_2)\). Projecting onto \(b\) leaves squared residual \(s^2\); projecting onto \(a\) leaves squared residual \(t^2s^2\). Since \(t>1\), selecting \(b\) is the optimal one-column projection and \(E\) is exactly \(1\) or \(t^2\).

**2. Gaussian reduction.** Rotational invariance gives two independent standard-normal \(k\)-vectors \(g=Ge_1\) and \(h=Ge_2\). The wrong-pivot event is
\[
\|g\|_2^2-t^2\|\rho g+s h\|_2^2>0.
\]
For each coordinate pair \((g_i,h_i)\), the quadratic-form matrix is
\[
M=\begin{pmatrix}1-t^2\rho^2&-t^2\rho s\\-t^2\rho s&-t^2s^2\end{pmatrix}.
\]
Its trace is \(1-t^2\), determinant is \(-t^2s^2\), and eigenvalues are \(\lambda_+=(D+1-t^2)/2>0\) and \(\lambda_-=(1-t^2-D)/2<0\). Applying the same orthogonal eigenbasis to each independent Gaussian coordinate pair transforms the event into \(\lambda_+X> -\lambda_-Y\), with independent \(X,Y\sim\chi_k^2\). The standard gamma-ratio identity gives \(X/(X+Y)\sim\operatorname{Beta}(k/2,k/2)\). Since this beta law is symmetric, the wrong-pivot probability is \(I_{\lambda_+/D}(k/2,k/2)=I_\theta(k/2,k/2)\). The two-point law for \(E\) proves the expectation formula.

**3. Sharp coherence comparison.** Write \(w=t^2>1\). Since \(D^2=(w-1)^2+4w(1-\rho^2)\) and \(\theta=\tfrac12-(w-1)/(2D)\), \(\theta\) is strictly increasing in \(1-\rho^2\). The beta distribution function is strictly increasing on \((0,1)\). Hence the largest wrong-pivot probability and largest expected error occur exactly at \(\rho=0\), where \(D=w+1\) and \(\theta=1/(1+w)\).

**4. Uniform sketch-size threshold.** For \(k=1\), \(I_z(1/2,1/2)=\frac2\pi\arcsin\sqrt z\); at \(\rho=0\), the excess relative error is asymptotic to \(2t/\pi\), so no finite input-uniform mean approximation ratio exists. For \(k\ge2\), set \(\alpha=k/2\ge1\). The symmetric-beta density is proportional to \([u(1-u)]^{\alpha-1}\), nondecreasing on \((0,1/2)\); it intersects the uniform density at most once there. Since its CDF agrees with the uniform CDF at both endpoints \(0\) and \(1/2\), this proves \(I_z(\alpha,\alpha)\le z\) for \(0\le z\le1/2\). Therefore
\[
\mathbb EE\le1+(w-1)I_{1/(1+w)}(\alpha,\alpha)
\le1+\frac{w-1}{w+1}<2.
\]
When \(k=2\), the beta distribution is uniform, so the worst-case expression equals \(2w/(1+w)\) and approaches \(2\) as \(w\to\infty\).

**5. Sharp four-row constant.** For \(k=4\), the beta law is \(\operatorname{Beta}(2,2)\), with \(I_z(2,2)=3z^2-2z^3\). At \(\rho=0\),
\[
R(w)=1+(w-1)\frac{3w+1}{(w+1)^3}
=\frac{w(w^2+6w+1)}{(w+1)^3},\quad w>1,
\]
and
\[
R'(w)=\frac{-3w^2+10w+1}{(w+1)^4}.
\]
The derivative changes from positive to negative exactly at \(w_*=(5+2\sqrt7)/3>1\), so the unique maximum is \(R(w_*)=(17+7\sqrt7)/27\). Step 3 gives the stated equality condition on the columns.

**6. High-contrast limit.** For fixed \(s>0\), as \(t\to\infty\), \(D=t^2+2s^2-1+O(t^{-2})\), and hence \(\theta=s^2/t^2+O(t^{-4})\). As \(z\downarrow0\), \(I_z(\alpha,\alpha)\sim z^\alpha/[\alpha B(\alpha,\alpha)]\). Inserting \(\alpha=k/2\) and \(B(\alpha,\alpha)=\Gamma(\alpha)^2/\Gamma(k)\) proves the asymptotic formula and all three limits. The coherence maximum in step 3 also makes the \(k\ge3\) convergence to \(1\) uniform over column correlations.

## Verification

The standalone \(verify.py\) checks the quadratic-form eigenvalues, exact rational beta specializations for two and four sketch rows, the four-row derivative and optimizer, uniform domination on finite grids, beta-integral numerical consistency, and seeded simulations of actual Gaussian pivot events for several correlations and sketch sizes. Run it with `python verify.py` using Python 3.10 or later and its standard library. The finite tests supplement, and do not replace, the complete proof above.

## Relationship to prior work

Gaussian sketches and norm-based pivoting are used in randomized QR with column pivoting (Martinsson, 2015; Martinsson and coauthors, 2015; Duersch and Gu, first preprint 2015 and revised discussion 2020), the reliability analysis by Xiao, Gu, and Langou (2018), and the randomized CholeskyQR-with-pivoting work of Melnichenko and coauthors (2023). The early Martinsson works develop Gaussian-sampled block-pivot algorithms and oversampling experiments; the 2020 analysis develops a single-column Gaussian sketch-norm/posterior description; the 2018 analysis provides Johnson–Lindenstrauss-based, high-probability pivot guarantees; the 2023 work develops full-algorithm rank-revealing and stability bounds. The present theorem is different: it characterizes the **joint**, correlation-dependent two-column pivot event exactly, its induced one-column projection loss, the smallest sketch-row count guaranteeing an input-uniform expected ratio, and an exact global four-row constant. It makes no assertion that later pivots or error-checking corrections inherit this loss. The simple underlying beta ratio is classical; novelty, if any, is the sharp first-pivot risk classification in this numerical-algorithm setting, not a new probability distribution. Historical derivations outside the inspected sources remain a precedence risk.

## Limitations

Only two original columns and one Gaussian-sketched maximum-norm pivot are treated. The approximation is the least-squares projection onto the selected original column, not the full QR approximation after additional pivots, not a best rank-one SVD approximation, and not a guarantee for non-Gaussian sketches. Expected squared Frobenius loss is used; an expectation bound is not a tail guarantee. The high-contrast expansion fixes \(|\rho|<1\), while the sharp finite-parameter formulas remain valid as columns approach parallelism without attaining it. 

## References

1. M. Melnichenko, O. Balabanov, R. Murray, J. Demmel, M. W. Mahoney and P. Luszczek, *CholeskyQR with Randomization and Pivoting for Tall Matrices (CQRRPT)*, arXiv:2311.08316, first public version 2023-11-14, https://arxiv.org/abs/2311.08316.
2. J. A. Duersch and M. Gu, *Randomized Projection for Rank-Revealing Matrix Factorizations and Low-Rank Approximations*, arXiv:2008.04447, 2020 (revised from earlier randomized QRCP work), https://arxiv.org/abs/2008.04447.
3. J. Xiao, M. Gu and J. Langou, *Fast Parallel Randomized QR with Column Pivoting Algorithms for Reliable Low-rank Matrix Approximations*, arXiv:1804.05138, https://arxiv.org/abs/1804.05138.
4. J. A. Duersch and M. Gu, *Randomized QR with Column Pivoting*, arXiv:1509.06820, https://arxiv.org/abs/1509.06820.
5. P. G. Martinsson, *Blocked rank-revealing QR factorizations: How randomized sampling can be used to avoid single-vector pivoting*, arXiv:1505.08115, https://arxiv.org/abs/1505.08115.
6. P.-G. Martinsson, G. Quintana-Orti, N. Heavner and R. van de Geijn, *Householder QR Factorization With Randomization for Column Pivoting (HQRRP)*, arXiv:1512.02671, https://arxiv.org/abs/1512.02671.
