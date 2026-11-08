# Strict parity monotonicity and two distinct limits for binary Veronese Fourier projection norms

## Finding
Let \(q=2^s\), \(s\ge1\), and \(G_m=\operatorname{Sym}_m(\mathbb F_q)\) under addition. Let \(C_m=\{vv^{\mathsf T}:v\in\mathbb F_q^m\}\) and let \(L_m(q)\) be the sharp \(\ell^1\)- and \(\ell^\infty\)-operator norm of the Fourier projection onto \(C_m\). Put \(H_m(q)=q^{-\lfloor m/2\rfloor}L_m(q)\). Then, for every such \(q\),
\[
1=H_0(q)>H_2(q)>H_4(q)>\cdots>C_{\rm even}(q)>0,
\qquad
1=H_1(q)>H_3(q)>H_5(q)>\cdots>C_{\rm odd}(q)>C_{\rm even}(q).
\]
Writing \(D_k(q)=\prod_{i=1}^{k}(1-q^{-i})\), with \(D_0(q)=1\), and \(c_q=\prod_{i=1}^\infty(1-q^{-(2i-1)})\), the distinct limits are
\[
 C_{\rm even}(q)=c_q\sum_{d=0}^{\infty}\frac{q^{-2d^2}}{D_{2d}(q)},
 \qquad C_{\rm odd}(q)=c_q\sum_{d=0}^{\infty}\frac{q^{-2d(d+1)}}{D_{2d+1}(q)}.
\]
The exact unnormalized norm, valid for all \(m\ge0\), is
\[
 L_m(q)=q^{m-m(m+1)/2}\sum_{j=0}^{\lfloor m/2\rfloor}q^j{m\brack 2j}_q q^{j(j-1)}\prod_{i=1}^j(q^{2i-1}-1),
\]
where \({m\brack r}_q\) is the Gaussian binomial coefficient. Hence \(L_{2h}(q)\sim C_{\rm even}(q)q^h\) and \(L_{2h+1}(q)\sim C_{\rm odd}(q)q^h\), with genuinely different limiting constants.

## Assumptions and scope
The field \(\mathbb F_q\) must have characteristic two; \(m\) is any nonnegative integer (dimension zero is included as a harmless base case). Every character of \(G_m\) is counted once; the Fourier transform is \(\widehat f(\gamma)=|G_m|^{-1}\sum_{X\in G_m}f(X)\overline{\gamma(X)}\). The Fourier projection on the dual of \(G_m\) retaining frequencies \(C_m\) is convolution by \(\widehat {1_{C_m}}\) under the natural finite-dual identification. Its sharp \(\ell^1\) and \(\ell^\infty\) operator norm is the sum of absolute kernel values, equal to \(\|1_{C_m}\|_{A(G_m)}\). No assertion is made for odd characteristic or non-rank-one frequency loci.

## Proof
**Fourier reduction.** The map \(v\mapsto vv^{\mathsf T}\) is injective: its diagonal recovers \(v_i^2\), and squaring is a bijection in characteristic two. Parameterize characters by their coefficients \(t_{ij}\) for \(1\le i\le j\le m\), using any fixed nontrivial additive character \(\psi\) of \(\mathbb F_q\). The unnormalized cone transform is
\[
S_T=\sum_{v\in\mathbb F_q^m}\psi\!\left(\sum_{i\le j}t_{ij}v_iv_j\right).
\]
Its polar bilinear form has alternating matrix \(B_T\) with off-diagonal entries \(t_{ij}\) for \(i<j\). If \(\operatorname{rank}(B_T)=2j\), the quadratic phase is a linear additive phase on the \((m-2j)\)-dimensional radical; the radical character is either trivial, yielding \(|S_T|=q^{m-j}\), or nontrivial, yielding \(S_T=0\). For each fixed \(B_T\), exactly \(q^{2j}\) choices of the diagonal coefficients make the radical character trivial. Indeed, raising each diagonal coefficient to its unique square-root gives a bijection from diagonals to linear additive phases, and restriction to the radical is surjective. Therefore the total absolute sum over the diagonal, at fixed \(B_T\), equals \(q^{m+j}\).

The number of alternating \(m\)-matrices of rank \(2j\) is
\[
 A_{m,j}(q)={m\brack2j}_q\frac{|\operatorname{GL}_{2j}(q)|}{|\operatorname{Sp}_{2j}(q)|}
 ={m\brack2j}_q q^{j(j-1)}\prod_{i=1}^j(q^{2i-1}-1).
\]
To see this, choose the radical, then a nondegenerate alternating form on its quotient. Dividing the character absolute sum by \(|G_m|=q^{m(m+1)/2}\) proves the displayed exact norm formula. Since there are \(q^{m(m-1)/2}\) alternating matrices, if \(B_m\) is uniform alternating and \(K_m=(m-\operatorname{rank}B_m-(m\bmod2))/2\), then
\[
H_m(q)=\mathbb E\big[q^{-K_m}\big].
\]

**A monotone nullity chain.** Grow a uniform alternating matrix by one row and its matching column with independent uniform entries. Conditional on its nullity \(d\), the augmented matrix has nullity \(d+1\) with probability \(q^{-d}\) (new column lies in the image) and nullity \(d-1\) otherwise. The latter event increases the rank by two. Observing only every second dimension gives a time-homogeneous birth–death chain for \(K\). From state \(k\), its birth and death probabilities are, respectively,
\[
 b_{\mathrm e}(k)=q^{-(4k+1)},\quad
 d_{\mathrm e}(k)=(1-q^{-2k})(1-q^{-(2k-1)})
\]
for even dimensions, and
\[
 b_{\mathrm o}(k)=q^{-(4k+3)},\quad
 d_{\mathrm o}(k)=(1-q^{-(2k+1)})(1-q^{-2k})
\]
for odd dimensions. In both cases \(d(0)=0\); all remaining probability is for holding at \(k\). The kernels are stochastically monotone because \(b(k)+d(k+1)\le1\): after writing \(t=q^{-1}\in(0,1/2]\), the even inequality is
\[
t^{4k+1}+(1-t^{2k+2})(1-t^{2k+1})\le1,
\]
whose difference from one equals \(t^{2k+1}(1+t-t^{2k+2}-t^{2k})\ge0\). The odd inequality follows similarly from
\[
t^{4k+3}+(1-t^{2k+3})(1-t^{2k+2})\le1.
\]
[Both identities can alternatively be verified directly by grouping powers of \(t\).] As the initial state at dimensions zero and one is \(K=0\), stochastic monotonicity of the kernels gives \(K_{m+2}\) stochastically dominating \(K_m\) within each parity. Strictness follows since after \(h+1\) two-step updates the state \(h+1\) has positive probability, whereas after \(h\) updates it is impossible. Because \(q^{-k}\) decreases strictly in \(k\), the expectations \(H_m\) strictly decrease separately on even and odd dimensions.

**Limiting constants and their separation.** For \(m=2h\), the exact probability of nullity \(2d\), for \(0\le d\le h\), obtained by dividing the preceding rank count by \(q^{\binom m2}\), is
\[
 \Pr(\operatorname{nullity} B_{2h}=2d)
 =q^{-d(2d-1)}\frac{\prod_{i=2h-2d+1}^{2h}(1-q^{-i})}{D_{2d}(q)}
 \prod_{i=1}^{h-d}(1-q^{-(2i-1)}).
\]
For \(m=2h+1\), nullity \(2d+1\) has probability
\[
 \Pr(\operatorname{nullity} B_{2h+1}=2d+1)
 =q^{-d(2d+1)}\frac{\prod_{i=2h-2d+1}^{2h+1}(1-q^{-i})}{D_{2d+1}(q)}
 \prod_{i=1}^{h-d}(1-q^{-(2i-1)}).
\]
The denominators \(D_k(q)\) are uniformly bounded below by the positive product \(\prod_{i\ge1}(1-q^{-i})\). The quadratic exponents in \(d\) give a summable uniform majorant. Dominated convergence yields precisely the two stated \(q\)-series limits. In particular the even limiting law assigns positive mass to state \(K=1\).

For a single even-to-odd augmentation, conditional on \(K_{2h}=k\), the next odd state is \(k\) with probability \(q^{-2k}\) and \(k-1\) otherwise. Consequently
\[
 H_{2h+1}-H_{2h}=(q-1)\mathbb E\left[q^{-K_{2h}}(1-q^{-2K_{2h}})\right].
\]
Passing to the limit and retaining the positive probability at \(K=1\) gives \(C_{\rm odd}>C_{\rm even}\). Both are positive because the limiting probability of \(K=0\) is positive. And \(C_{\rm odd}<H_3<1\) by strict odd-parity decrease. This completes the proof.

## Verification
The accompanying Python checker directly enumerates all quadratic Veronese frequencies and all dual coefficients for \((q,m)=(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(8,2)\), checking each Fourier amplitude, complete multiplicities, normalization and sharp norm against the rank formula. A separate exact-rational checker reconstructs both nullity birth–death kernels and compares their norms with direct rank counts for \(q=2,4,8\), dimensions through \(29\), also checking strict parity monotonicity. Run `python3 verify.py` from the extracted package. The checks are finite corroboration, not an all-dimension proof.

## Relationship to prior work
Finite-field Fourier extension on quadratic varieties is classical; Iosevich–Koh (2008) deals with odd characteristic and does not yield this binary Veronese parity law. The symmetric-bilinear/quadric association-scheme character tables in Schmidt (2018), following earlier MacWilliams and Wang–Wang–Ma–Ma work, are stronger than a bare claim to new finite-field character sums or rank multiplicities. Those **are not claimed as new**. Rather, the result is the normalized sharp Fourier-algebra endpoint norm, its strict dimension-by-two monotonicity and two unequal convergent parity profiles, proved here through a stochastic rank-nullity coupling. Earlier geometric classifications of the even-field Veronese surface study intersection orbits rather than endpoint projection norms. Exhaustive priority is not established; a pre-existing result combining association-scheme character tables with rank-nullity Markov monotonicity may imply the statement.

## Limitations
Characteristic two and the full rank-one cone including zero are essential to the stated formula. The result supplies neither analogous odd-characteristic constants nor a classification of extremizers. The Fourier eigenvalue calculation alone is classical in a more general association-scheme framework; the proposed distinct contribution is the sharp normalized monotonicity and limiting parity behavior. Independent review and exhaustive historical-priority determination have not been carried out.

## References
- A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1 (public 2008-04-28), https://arxiv.org/html/0804.4505v1.
- K.-U. Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, arXiv:1803.04274v1 (2018), https://arxiv.org/html/1803.04274v1, especially Sections 2–4.
- N. Alnajjarine and M. Lavrauw, *A classification of planes intersecting the Veronese surface over finite fields of even order*, arXiv:2209.08354v1 (2022), https://arxiv.org/html/2209.08354v1.
