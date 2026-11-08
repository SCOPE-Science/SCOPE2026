# Random sweep-order mixing strictly slows two-row Kaczmarz in mean square

## Finding

Consider two distinct nonorthogonal lines through the origin in \(\mathbb R^2\). Let \(P_u=uu^{\mathsf T}\) and \(P_v=vv^{\mathsf T}\) be orthogonal projections onto those lines, where \(u,v\) are unit vectors oriented so that \(c=u^{\mathsf T}v\in(0,1)\). One complete two-row Kaczmarz sweep has error map \(F=P_vP_u\) or \(R=P_uP_v\). Independently at each sweep, use \(F\) with probability \(p\) and \(R\) with probability \(1-p\).

For any nonzero deterministic initial error and any \(0<p<1\), the exact asymptotic expected **squared Euclidean error factor per complete sweep** is

\[
\rho(c,p)=\frac{c^4+\sqrt{c^8+4p(1-p)c^4(1-c^4)}}{2}.
\]

This is strictly larger than the factor \(c^4\) of either repeated fixed order. Among all \(p\in[0,1]\), the slowdown factor is uniquely largest at \(p=1/2\), where \(\rho(c,1/2)=c^2(1+c^2)/2\). Thus genuinely mixing two equally costly convergent sweep orders always worsens their asymptotic mean-square contraction in this natural two-row model.

For fair order mixing, the *complete finite-horizon law* for every integer \(n\ge1\) is

\[
\mathbb E\|e_n\|_2^2=
\frac{c^2}{2}\bigl((u^{\mathsf T}e_0)^2+(v^{\mathsf T}e_0)^2\bigr)
\left(\frac{c^2+c^4}{2}\right)^{n-1}.
\]

The asymptotic rate ratio between fair randomization and a fixed order is \((1+c^2)/(2c^2)\), which diverges as \(c\downarrow0\). At \(c=1/2\), the respective mean-square factors are \(5/32\) and \(1/16\), a ratio of \(5/2\).

## Assumptions and scope

Take a nonsingular two-equation, two-unknown consistent real linear system and normalize its rows. The error update after projection onto either row's solution hyperplane is an orthogonal rank-one projector onto a line; denote these projectors by \(P_u,P_v\). Reversing the sign of one line's unit vector if necessary makes \(c=u^{\mathsf T}v\) positive. The theorem assumes \(0<c<1\), so the rows are linearly independent and not orthogonal. At every **complete** two-projection sweep, choose the forward or reverse order independently with the same fixed probability \(p\). Expectation is over all sweep orders, while \(e_0\ne0\) is deterministic. The endpoints \(p=0,1\) are deterministic cyclic sweeps. For \(c=0\), one complete sweep solves the error exactly, while \(c=1\) corresponds to dependent lines and is excluded.

## Proof

Since \(P_u=uu^{\mathsf T}\) and \(P_v=vv^{\mathsf T}\),

\[
F=cvu^{\mathsf T},\qquad R=cuv^{\mathsf T}.
\]

Both maps have rank one. After any sweep, the error lies along either \(v\) (last map \(F\)) or \(u\) (last map \(R\)). Define \(w_n=(w_{n,F},w_{n,R})^{\mathsf T}\), where the components are expected squared error contributed by paths whose last sweep was \(F\) and \(R\), respectively. Direct application gives

\[
w_1=c^2\begin{pmatrix}p(u^{\mathsf T}e_0)^2\\(1-p)(v^{\mathsf T}e_0)^2\end{pmatrix},
\qquad
w_{n+1}=K(c,p)w_n,
\]

\[
K(c,p)=\begin{pmatrix}pc^4&pc^2\\(1-p)c^2&(1-p)c^4\end{pmatrix},
\qquad \mathbb E\|e_n\|_2^2=(1,1)w_n.
\]

To see the four entries, repeating the same sweep from its previous output line multiplies squared norm by \(c^4\), whereas switching sweep orders multiplies squared norm by \(c^2\). The transfer matrix has trace \(c^4\) and determinant \(-p(1-p)c^4(1-c^4)\). Its two eigenvalues are

\[
\lambda_\pm=\frac{c^4\pm\sqrt{c^8+4p(1-p)c^4(1-c^4)}}2.
\]

For \(0<p<1\) every entry of \(K\) is positive. Therefore its positive Perron eigenvalue \(\lambda_+=\rho(c,p)\) strictly dominates the modulus of the negative eigenvalue. As \(e_0\ne0\) and \(u,v\) span the plane, at least one component of \(w_1\) is positive; positive left/right Perron eigenvectors give a strictly positive leading coefficient. Hence

\[
\lim_{n\to\infty}(\mathbb E\|e_n\|_2^2)^{1/n}=\rho(c,p).
\]

Because \(c^4(1-c^4)>0\), \(\rho(c,p)>c^4\) whenever \(0<p<1\), and it is strictly increasing in \(p(1-p)\). Its maximum is unique at \(p=1/2\), where \(\sqrt{c^8+c^4(1-c^4)}=c^2\). At either deterministic endpoint \(p\in\{0,1\}\), repeating \(F\) or \(R\) yields \(F^n=c^{2n-1}vu^{\mathsf T}\) or \(R^n=c^{2n-1}uv^{\mathsf T}\), with sharp asymptotic squared rate \(c^4\). For fair mixing, \((1,1)K=\rho(c,1/2)(1,1)\), which proves the displayed finite-horizon formula by induction. The slowdown ratio and its \(c\downarrow0\) behavior follow algebraically. All statements apply to complete sweeps, not individual projection steps.

## Verification

The supplied standalone `verifier.py` performs exact rational matrix arithmetic on three Pythagorean unit-vector pairs, five nontrivial order biases and three distinct initial errors. For every sweep count from one through eight, it independently enumerates all \(2^n\) order histories, compares their exact probability-weighted squared errors with the transfer-matrix recurrence, and checks the fair-mixing formula. It also verifies transfer trace, determinant, negative determinant and analytic spectral-rate inequalities. Execution output is included as `verification_output.txt`. These finite checks support the proof; they do not establish the infinite-horizon Perron assertion without the analytic argument above.

## Relationship to prior work

The underlying rank-one orthogonal projections and cyclic Kaczmarz iteration are classical. Necoara's randomized block Kaczmarz analysis [1] samples blocks and gives expected convergence bounds; its principal block-averaging model is not independently reshuffled two-projection compositions, and its inspected statements do not give the all-bias two-row transfer law above. Steinerberger's weighted randomized Kaczmarz [2] chooses individual equations according to their current residuals, rather than using each equation exactly once per independently ordered epoch. Earlier work by Bai and Wu [3] analyzes exact mean-square errors for independently sampled randomized Kaczmarz, a different sampling mechanism. Literature on row reordering in tomography [4] discusses one-time/random shuffles and does not, in accessible material, supply the exact independent-per-sweep classification here. The distinction is a comparison of sampling models and implications, not evidence of exhaustive novelty.

## Limitations

This is an exact-arithmetic, two-dimensional, two-row theorem for consistent full-rank systems with orthogonal projections and independent complete-sweep orientation choices. It does **not** state that fixed cyclic order is superior for larger systems or arbitrary sampling models, nor that almost-sure Lyapunov exponents equal the mean-square factor. No result on floating-point rounding or noisy/inconsistent equations is claimed. Prior specialist work on two-projection random products and independently reshuffled Kaczmarz may contain an equivalent formula; an inaccessible full comparison remains a precedence risk. The computed finite checks are not independent certification.

## References

[1] I. Necoara, *Faster randomized block Kaczmarz algorithms* (first public 26 February 2019), https://arxiv.org/abs/1902.09946.

[2] S. Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems* (first public 6 July 2020), https://arxiv.org/abs/2007.02910.

[3] Z.-Z. Bai and W.-T. Wu, *On convergence rate of the randomized Kaczmarz method*, Linear Algebra and its Applications 553 (2018), 252–269, https://doi.org/10.1016/j.laa.2018.05.009.

[4] *Kaczmarz Anomaly in Tomography Problems* (2022), https://www.mdpi.com/2673-9909/2/2/12.
