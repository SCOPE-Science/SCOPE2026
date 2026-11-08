# Sharp stage-specific scheduling reversals in a four-season population projection

## Finding
For two positive two-stage Leslie operators, each used twice in a four-season cycle, the difference between clustered and alternating four-season growth factors has exactly the sign of a single explicit polynomial (defined below). If the environments differ **only in early-stage fertility**, clustering strictly raises the growth factor; if they differ **only in mature-stage fertility** or **only in maturation survival**, alternating strictly raises it. Both directions can strictly reverse the population extinction-versus-growth verdict, with all maturation probabilities at most one. This is the first possible schedule-sensitive length among binary seasonal words with a fixed multiset.

## Assumptions and scope
Consider a nonnegative population vector of two stages evolving by \(x_{t+1}=L_t x_t\), with \(L_t\) chosen periodically from two matrices
\[
 A=\begin{pmatrix}a&u\\v&0\end{pmatrix},\qquad B=\begin{pmatrix}d&w\\z&0\end{pmatrix},
\]
where \(a,d,u,w>0\) are reproductive outputs and \(0<v,z\le1\) are maturation probabilities. No survival of the mature stage is assumed: the lower-right entries are zero. The words AABB and ABAB use exactly two copies of each environment, with four equal-length projection intervals. Their monodromies can be represented (up to cyclic rotation) by \(C=A^2B^2\) and \(T=(AB)^2\). The four-step geometric growth factors are \(\rho(C)^{1/4}\) and \(\rho(T)^{1/4}\). The words are not assumed to be random, and no nonlinear density dependence is included.

Define
\[
\Delta=a^2wz-aduz-advw+d^2uv-u^2z^2+2uv wz-v^2w^2.
\]
Then for every parameter choice in the stated domain,
\[
\operatorname{sgn}(\rho(C)-\rho(T))=\operatorname{sgn}(\Delta).
\]
In particular: (i) if \(u=w\), \(v=z\), then \(\Delta=uv(a-d)^2\); (ii) if \(a=d\), \(v=z\), then \(\Delta=-v^2(u-w)^2\); (iii) if \(a=d\), \(u=w\), then \(\Delta=-u^2(v-z)^2\). Strict signs hold precisely when the one changing vital rate actually differs. For arbitrary simultaneous variation there is **no universal sign**; the sign of \(\Delta\) is the exact decision criterion.

## Proof
**Trace formula.** For arbitrary \(2\times2\) matrices, \(\operatorname{tr}(A^2B^2)-\operatorname{tr}(ABAB)=\det(AB-BA)\). One direct verification uses \(\operatorname{tr}(X^2)=\operatorname{tr}(X)^2-2\det X\) and \(\operatorname{tr}(A^2B^2)=\operatorname{tr}((AB)^2)+\det(AB-BA)\); the commutator has the explicit form \[AB-BA=\begin{pmatrix}uz-vw&aw-du\\vd-az&vw-uz\end{pmatrix}.\] Hence \(\det(AB-BA)=-(uz-vw)^2-(aw-du)(vd-az)\), which expands to the displayed \(\Delta\). These are polynomial identities; they do not require invertibility.

**From trace to spectral radius.** Both \(C\) and \(T\) are entrywise strictly positive. Their determinants agree and are positive: \(\det C=\det T=(uv wz)^2\). A strictly positive \(2\times2\) matrix has real distinct eigenvalues, the Perron eigenvalue being \((t+\sqrt{t^2-4\delta})/2\), where \(t\) is trace and \(\delta\) is determinant. At fixed \(\delta>0\), this expression is strictly increasing with \(t>2\sqrt\delta\). Consequently the two Perron eigenvalues have exactly the sign comparison of their traces, which is \(\Delta\). Substituting the three respective one-vital-rate constraints factorizes \(\Delta\) into the displayed nonzero signed squares.

**Two exact persistence switches.** With changing early-stage fertility alone take
\[
 A=\begin{pmatrix}8/5&4/5\\2/5&0\end{pmatrix},\qquad B=\begin{pmatrix}4/25&4/5\\2/5&0\end{pmatrix}.
\]
Here \(\det C=\det T=4096/390625<1\), while
\[
\det(I-C)=-98079/390625<0,\qquad \det(I-T)=161121/390625>0.
\]
Hence \(\rho(C)>1>\rho(T)\). With changing maturation survival alone, take
\[
 A=\begin{pmatrix}33/50&11/10\\11/20&0\end{pmatrix},\qquad B=\begin{pmatrix}33/50&11/10\\11/100&0\end{pmatrix}.
\]
Now \(\det C=\det T=214358881/40000000000<1\), and
\[
\det(I-C)=1468416481/40000000000>0,\quad \det(I-T)=-7901823519/40000000000<0.
\]
Hence \(\rho(C)<1<\rho(T)\). These implications follow since both Perron roots are positive and, with determinant below one, \(\det(I-M)=(1-\lambda_1)(1-\lambda_2)\) is negative exactly when the larger eigenvalue exceeds one.

**Sharp period bound.** Every binary word of length one, two or three with a specified multiset of A and B is a cyclic rotation of any other such word. Cyclic permutations of square-matrix products have the same characteristic polynomial (by \(\det(I-XY)=\det(I-YX)\)); hence no schedule comparison at a shorter period can change growth. At period four with two A and two B, exactly two cyclic word classes occur: AABB and ABAB. The exhibited matrices distinguish them. Thus four is the least possible schedule-sensitive period among fixed-multiset binary two-stage schedules.

## Verification
Run `python checker.py` with SymPy (listed in `requirements.txt`). The checker independently expands both traces, compares the commutator determinant, verifies the three signed-square reductions, enumerates all binary schedules through four slots, and recomputes all exact rational threshold witnesses. All checks passed on the included files. The finite word enumeration is not used as a substitute for the general spectral sign proof.

## Relationship to prior work
The ordered-product framework and sensitivity to seasonal vital rates are classical (Caswell and Trevisan, 1994; Caswell, 2019). In a closely relevant structured weed model, Mertens, van den Bosch and Heesterbeek (2002) explicitly compared the same seasonal words AABB and ABAB and found a regime where ABAB is superior. Thus **neither schedule dependence nor AABB-versus-ABAB comparison is claimed as new**. The separate result here is a universal exact sign trichotomy by the sole changing biological stage, its explicit general parameter criterion for the two-stage zero-adult-stasis Leslie family, and exact opposing persistence witnesses. Cushing and Ackleh (2011) treat periodic net reproduction and persistence thresholds, including a period-two Leslie application, rather than this parameter-specific period-four comparison. General two-by-two matrix identities are mathematical predecessors; the polynomial criterion follows by specialization and is not presented as independent from them.

## Limitations
This is a deterministic linear two-stage projection result and does not assert stochastic survival probability, finite-population persistence, empirical relevance to any one species, or robustness to adult stasis. The ranking comparison is already part of a broader published research direction. Historical priority for the specialized universal trichotomy remains provisional: the full text of the highly relevant 2002 weed-rotation article and the 1994 paper was not obtained, and their accessible abstracts alone cannot exclude prior appearance of this specialization. The result has not undergone independent scientific audit.

## References
1. Caswell, H. and Trevisan, M. C. (1994). *Sensitivity Analysis of Periodic Matrix Models*, *Ecology* 75, 1299–1303. https://doi.org/10.2307/1937455 (first online 1994-07-01).
2. Mertens, S. K., van den Bosch, F. and Heesterbeek, J. A. P. (2002). *Weed populations and crop rotations: exploring dynamics of a structured periodic system*, *Ecological Applications* 12, 1125–1141. https://doi.org/10.1890/1051-0761(2002)012%5B1125:WPACRE%5D2.0.CO;2 .
3. Cushing, J. M. and Ackleh, A. S. (2011). *A net reproductive number for periodic matrix models*, *Journal of Biological Dynamics*. https://doi.org/10.1080/17513758.2010.544410 (online 2011-02-18).
4. Caswell, H. (2019). *Periodic Models*, in *Sensitivity Analysis: Matrix Methods in Demography and Ecology*, chapter 8. https://doi.org/10.1007/978-3-030-10534-1_8 .
