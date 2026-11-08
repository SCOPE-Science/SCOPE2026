# Matched spectral classes at every singular-gap level in the two-dimensional twisted baker map

## Finding
For the two-dimensional twisted baker map, every iterate length \(n\ge1\) has an **exact joint census** of (i) real versus nonreal derivative eigenvalues, (ii) singular-value anisotropy, and (iii) eigenvalue-modulus anisotropy. With the definitions below, let
\[
 m_n(g)=\begin{cases}
 \frac12\binom{n}{n/2},&g=0\text{ and }n\text{ even},\\
 \binom{n}{(n-g)/2},&g>0,\quad 0\le g\le n,\quad g\equiv n\pmod 2,\\
 0,&\text{otherwise}.
 \end{cases}
\]
For each admissible \(g\), exactly \(m_n(g)\) of the isolated fixed points of \(F^n\) have **nonreal** derivative spectrum and singular logarithmic gap \(g\log2\). Exactly \(m_n(g)-\mathbf{1}_{\{g=n\}}\) have **entirely real** spectrum and the same singular gap. On the nonreal class the logarithmic eigenvalue-modulus gap is identically zero, whereas on the real class it is exactly \(g\log2\).

In particular, the real and nonreal classes have **identical singular-anisotropy histograms at every level below the maximum**. There is precisely one excess nonreal point at the maximal gap, because the all-left symbolic word corresponds to a nonisolated fixed face and must be excluded.

Let \(x_n\) be chosen uniformly among the \(2^n-1\) isolated fixed points of \(F^n\), and set
\[
 D_n=\log_2\frac{\sigma_{\max}(DF^n(x_n))}{\sigma_{\min}(DF^n(x_n))},\qquad
 E_n=\log_2\frac{\max_{\lambda\in\operatorname{spec} DF^n(x_n)}|\lambda|}{\min_{\lambda\in\operatorname{spec} DF^n(x_n)}|\lambda|}.
\]
Then, as \(n\to\infty\),
\[
 \boxed{\left(\frac{E_n}{\sqrt n},\frac{D_n}{\sqrt n}\right)
 \Longrightarrow(B|Z|,|Z|),}
\]
where \(B\) is a fair Bernoulli random variable, \(Z\) is standard Gaussian, and they are independent. Thus half the asymptotic periodic-point ensemble has equal eigenvalue moduli even though its singular-value anisotropy has a nondegenerate half-normal fluctuation. The law concerns fixed points of an iterate (including smaller prime periods), not solely points of least period \(n\).

## Assumptions and scope
Fix \(X=[-1,1]\times[0,1]\), with the convention that \(x=0\) belongs to the right branch. The map is
\[
 F(x,y)=\begin{cases}(1+2x,y),&x<0,\\(1-2y,x),&x\ge0.\end{cases}
\]
Its derivative matrices are \(L=\operatorname{diag}(2,1)\) and \(R=\begin{pmatrix}0&-2\\1&0\end{pmatrix}\). The nonisolated fixed face is \(N=\{(-1,y):0\le y\le1\}\). For each positive integer \(n\), use only \(\operatorname{Fix}_n=\{z\in X\setminus N:F^n(z)=z\}\); this set contains exactly \(2^n-1\) points by the symbolic correspondence in Saiki--Takahasi--Yorke (2022/2023), Lemmas 2.4--2.6. There are no periodic points on the branching line \(x=0\). Every derivative at an isolated periodic point is therefore well-defined along its orbit.

The singular values \(\sigma_{\max}\ge\sigma_{\min}>0\) are Euclidean singular values of the full derivative matrix \(DF^n(z)\). Eigenvalue-modulus gap \(E_n\) uses the absolute values of all complex eigenvalues and vanishes for a conjugate pair. Both gaps are nonnegative and dimensionless after taking base-two logarithms. A point is called nonreal-class if at least one eigenvalue is nonreal.

## Proof
**Step 1: word-to-point correspondence.** By the cited symbolic coding and boundary lemmas, each length-\(n\) word in \(\{L,R\}^n\) containing an \(R\) represents one and only one isolated point of \(\operatorname{Fix}_n\), with that word repeating under forward dynamics. The omitted word \(L^n\) generates the nonisolated fixed face \(N\). No additional branch-boundary fixed points exist. This establishes the uniform counting measure over the \(2^n-1\) admissible words and takes care of the boundary convention.

**Step 2: exact label-stretch coding.** Temporarily include all \(2^n\) binary words. Encode \(R\) by \(b_i=1\) and \(L\) by \(b_i=0\), for \(0\le i<n\). Define cumulative right-branch parities
\[
 s_j=b_0+\cdots+b_{j-1}\pmod2,\qquad j=1,\ldots,n.
\]
The transformation \((b_0,\ldots,b_{n-1})\mapsto(s_1,\ldots,s_n)\) is a bijection of \(\mathbb F_2^n\): inversely \(b_0=s_1\) and \(b_i=s_i+s_{i+1}\pmod2\) for \(i\ge1\). Hence the \(s_j\) are independent fair bits under uniform word counting.

Follow the original first basis vector under the product of branch Jacobians. At an \(L\)-step its magnitude is multiplied by \(2\) if that label is in coordinate 1; at an \(R\)-step it is multiplied by \(2\) if that label is in coordinate 2. Both conditions are equivalent to the label being in coordinate 1 *after* that step, namely \(s_{i+1}=0\). Consequently its total stretch equals \(2^A\), with
\[
 A=\sum_{j=1}^n\mathbf{1}_{\{s_j=0\}}=Q+\mathbf{1}_{\{s_n=0\}},\qquad
 Q=\sum_{j=1}^{n-1}\mathbf{1}_{\{s_j=0\}}.
\]
The other basis vector is stretched by \(2^{n-A}\) because each one-step Jacobian has absolute determinant \(2\). The total derivative is monomial, so its singular values are **exactly** \(2^A\) and \(2^{n-A}\). Thus \(D=|2A-n|\). Since \(Q\sim\operatorname{Binomial}(n-1,1/2)\) and is independent of \(s_n\), all finite counts can now be computed without approximation.

**Step 3: spectral class and exact histogram matching.** If \(s_n=0\), the number of \(R\)-visits is even and the derivative is diagonal. Its two eigenvalue moduli are \(2^A\) and \(2^{n-A}\), so \(E=D\). If \(s_n=1\), the derivative is off-diagonal, with negative off-diagonal entry product; its characteristic polynomial is \(\lambda^2+2^n\), so its two eigenvalues are a nonreal conjugate pair of equal modulus \(2^{n/2}\). Thus \(E=0\) for this class.

Conditionally on \(s_n=1\), \(D=|2Q-n|\). Conditionally on \(s_n=0\), \(D=|2(Q+1)-n|\). Because \(Q\) is binomial with size \(n-1\), replacing \(Q\) by \(n-1-Q\) leaves its distribution unchanged and transforms the latter absolute value into \(|n-2Q|\). Therefore in the full word ensemble \(D\) is independent of the spectral-class indicator \(B=\mathbf{1}_{\{s_n=0\}}\), which is fair. Moreover its common conditional distribution is that of \(|S_n|\), for a sum \(S_n\) of \(n\) independent fair signs: direct Pascal identities give
\[
 \#\{\text{words}:s_n=b,\ D=g\}=m_n(g),\qquad b\in\{0,1\}.
\]
For \(g>0\), this is \(\binom{n}{(n-g)/2}\); for \(g=0\), it is half the central binomial coefficient. Finally exclude \(L^n\), which has \(s_n=0\), \(A=n\), and \(D=E=n\). It removes exactly one real-class point at \(g=n\) and nothing elsewhere, proving the joint census and the sum \(\#\operatorname{Fix}_n=2^n-1\).

**Step 4: joint limit.** In the full word ensemble, the entire joint law is exactly \((E,D)=(B|S_n|,|S_n|)\), with \(B\) fair and independent of \(|S_n|\). The classical central limit theorem gives \(S_n/\sqrt n\Rightarrow Z\). Excluding the single word \(L^n\) changes the sampling law in total variation by exactly \(2^{-n}\), so it does not affect the joint weak limit. This proves the displayed formula and all stated asymptotic interpretations.

## Verification
The included self-contained program `check_twisted_joint.py` uses exact integer Jacobian products for every non-all-left binary word of lengths \(1\) through \(11\). For lengths up to \(8\), it additionally solves the affine fixed-point equations in rational arithmetic, verifies the point's true itinerary and return, and checks that its coordinates remain in \(X\). It compares every observed pair of singular and eigenvalue-modulus gaps with the stated closed counting formula. Run `python check_twisted_joint.py` using Python 3; no third-party dependencies are needed. The program reports `CHECK_OK 4083 finite word/periodic geometry/spectrum identities across n=1..11`. Finite computations check examples and identities, while the proof's bijection and binomial calculations cover all \(n\).

## Relationship to prior work
Saiki, Takahasi and Yorke, *The twisted baker map* (arXiv:2202.04304), introduce the geometric system, give the exact symbolic correspondence and show density/equidistribution of real- and nonreal-spectrum periodic points. Their Sections 2.1--2.3 give the Jacobian structure and total fixed-point counts, but do not compute the joint distribution of Euclidean singular anisotropy and eigenvalue-modulus anisotropy.

The subsequent publicly available research note *Exact real-spectrum residue law for the twisted baker map* (2026) gives exact residue-class real/nonreal counts and characteristic-polynomial factors. These results supply the **spectral-class marginal**, not the joint histogram indexed by singular anisotropy. Existing exact periodic eigenvalue minimum-modulus counts on the same map determine certain eigenvalue marginal statistics, while central limit results for tangent-vector stretches under stationary Lebesgue sampling establish a **singular-value marginal in a different ensemble**. Neither comparison implies the finite-period equality of the two class-conditional singular histograms, the one-word extreme defect, or the stated coupled joint limiting law. We do not claim novelty for their independent marginal calculations or the general binomial/central-limit tools.

Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps* (arXiv:2409.01261), studies unstable-dimension classes and equilibrium states of **different** baker maps; it does not give a joint singular/eigen gap census for this twisted map.

## Limitations
The theorem is specific to the two-dimensional twisted baker map and iterate-fixed-point counting, including points whose least period divides \(n\). It does not extend automatically to higher dimensions or to individual least-period-\(n\) orbit statistics. The formal all-word independence is exact; among actual isolated periodic points the sole missing word creates the precisely stated extreme-gap defect. The theorem does not assert independence of eigenvalue and singular-value gaps (which are related by construction), only of the **spectral class** and singular gap in the augmented uniform word ensemble and the exact matching for realizable levels below the extreme. The result uses published symbolic coding, not an independent reconstruction for arbitrary \(n\). Although searches found no explicit prior joint law, a short derivation from existing monomial-cocycle techniques could occur in unindexed literature; this is a priority risk. The normal limit is a weak distributional statement, not a deterministic trajectory-by-trajectory bound.

## References
1. Y. Saiki, H. Takahasi, J. A. Yorke, *The twisted baker map*, arXiv:2202.04304 (first public version 9 February 2022), particularly Sections 2.1--2.3, Lemmas 2.4--2.6, and Theorems A--D. https://arxiv.org/abs/2202.04304
2. *Exact real-spectrum residue law for the twisted baker map*, publicly available research note (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261 (2 September 2024), particularly Theorem 1.1. https://arxiv.org/abs/2409.01261
