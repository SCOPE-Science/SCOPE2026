# The full-matrix idempotent law for binary-characteristic evolution algebras

## Finding

For every integer \(n\geq1\) and every finite field \(K=\mathbb F_q\), where \(q=2^f\) with \(f\geq1\), choose the structure matrix \(M\) uniformly from **all** \(n\times n\) matrices over \(K\), including singular matrices. Give \(K^n\) its evolution-algebra product with natural basis \(e_1,\ldots,e_n\), \(e_i e_j=0\) for \(i\ne j\), and \(e_i^2=\sum_j M_{ij}e_j\). Let \(N(M)\) be its number of nonzero idempotents.

**Theorem (unrestricted exact law and singular universality).** Almost surely \(N(M)=2^D-1\) for a unique integer \(0\le D\le n\), and every such value occurs with positive probability. Define
\[
G_k=\prod_{i=0}^{k-1}(2^k-2^i),\quad G_0=1,\qquad
B_{k,d}={k\brack d}_2=\frac{\prod_{i=0}^{d-1}(2^k-2^i)}{G_d},
\]
where \(0\le d\le k\), and let
\[
H_{n,q}(k)=\prod_{i=0}^{k-1}(1-q^{i-n}),\qquad H_{n,q}(0)=1.
\]
Then, exactly for every \(0\le d\le n\),
\[
\boxed{\mathbb P\{N(M)=2^d-1\}=
\sum_{k=d}^{n}(-1)^{k-d}2^{\binom{k-d}{2}}\,{k\brack d}_2\,
\frac{H_{n,q}(k)}{G_k}.}
\]
In particular,
\[
\mathbb E[N(M)]=1-q^{-n},\qquad
\operatorname{Var}(N(M))=(1-q^{-n})(1-(q-1)q^{-n}).
\]
For every fixed nonnegative integer \(d\), there is a finite constant \(C_d\), independent of \(n\) and \(q\), such that
\[
\left|\mathbb P\{N(M)=2^d-1\}-
\frac{\prod_{r=1}^{\infty}(1-2^{-r})}{2^{d^2}\prod_{r=1}^{d}(1-2^{-r})^2}\right|\le C_d 2^{-n}
\]
whenever \(n\ge d\). Therefore the limiting idempotent-count distribution is **independent of field size even if that size changes with dimension**, despite finite-dimensional dependence on \(q\).

Furthermore, for every **fixed** \(q=2^f\), the same limiting distribution holds when \(M\) is sampled uniformly **conditional on being singular**. Its finite-dimensional conditional law is obtained explicitly by subtracting the known invertible-matrix law:
\[
\boxed{\mathbb P(D=d\mid\det M=0)
=\frac{P_{n,q}(d)-c_{n,q}Q_n(d)}{1-c_{n,q}},\qquad
c_{n,q}=\prod_{j=1}^n(1-q^{-j}),}
\]
where \(P_{n,q}(d)\) is the boxed unrestricted probability and \(Q_n(d)\) is the previously established perfect-algebra law, equivalently the probability that a uniform matrix in \(\mathrm{GL}_n(\mathbb F_2)\) has a \(d\)-dimensional fixed space. In particular the conditional singular law never has \(D=n\). These laws count labeled matrices, not algebra isomorphism classes.

## Assumptions and scope

The base field is a finite field of characteristic two. Both \(n\) and \(f\) are arbitrary positive integers. Sampling is uniform over all \(q^{n^2}\) structure matrices, with no nondegeneracy, perfection, associativity or unit assumption. The coordinate squaring equation is \(x=M^{\mathsf T}x^{[2]}\), where \(x^{[2]}\) denotes coordinatewise Frobenius squaring; this fixes all orientation conventions. The zero idempotent is not included in \(N(M)\). Conditional singular asymptotics are asserted for each fixed field size, whereas the unconditioned bound is uniform over all even prime-power field sizes.

## Proof

**Step 1: Fixed-space and independence.** The map \(T_M(x)=M^{\mathsf T}x^{[2]}\) is additive and satisfies \(T_M(ax)=a^2T_M(x)\). Its fixed set \(V_M\) is an \(\mathbb F_2\)-linear subspace, hence contains \(2^D\) elements for some \(D\). Every \(\mathbb F_2\)-independent family of fixed vectors is also independent over \(K\). To prove this, take a minimal \(K\)-dependent family \(v_1,\ldots,v_t\) of fixed vectors and write \(v_t=\sum_{i<t}a_iv_i\). Applying \(T_M\) gives \(v_t=\sum_{i<t}a_i^2v_i\), and independence of the first \(t-1\) vectors over \(K\) forces \(a_i^2=a_i\). Consequently each \(a_i\in\mathbb F_2\), contradicting \(\mathbb F_2\)-independence. This argument works also for singular \(M\), proving \(0\le D\le n\).

**Step 2: Exact frame moments over unrestricted matrices.** Set \(F_k(d)=\prod_{i=0}^{k-1}(2^d-2^i)\) for \(0\le k\le n\), with \(F_0=1\). It counts ordered independent \(k\)-tuples in the fixed \(\mathbb F_2\)-space. By Step 1 these tuples are ordered \(K\)-frames; their Frobenius squares are \(K\)-frames as well. There are \(\prod_{i=0}^{k-1}(q^n-q^i)\) possible \(K\)-frames. For a prescribed frame \((v_i)\), requiring \(M^{\mathsf T}v_i^{[2]}=v_i\) for all \(i\) supplies \(nk\) independent uniform linear constraints on the \(n^2\) entries of the unrestricted matrix \(M\), and therefore has probability \(q^{-nk}\). Counting fixed frames by linearity of expectation gives
\[
\boxed{\mathbb E[F_k(D)]=q^{-nk}\prod_{i=0}^{k-1}(q^n-q^i)=H_{n,q}(k).}
\]
This is the essential difference from uniform **invertible** matrices, where frame transitivity instead gives moments identically one.

**Step 3: Gaussian-binomial inversion.** Put \(P_{n,q}(d)=\Pr(D=d)\) and \({d\brack k}_2=F_k(d)/G_k\). Step 2 yields
\[
\sum_{d=k}^n{d\brack k}_2 P_{n,q}(d)=H_{n,q}(k)/G_k.
\]
The finite triangular Gaussian-binomial inversion formula states that if \(b_k=\sum_{d\ge k}{d\brack k}_2 p_d\), then \(p_d=\sum_{k\ge d}(-1)^{k-d}2^{\binom{k-d}{2}}{k\brack d}_2 b_k\). This follows by substituting and applying \(\sum_{j=0}^h(-1)^j2^{\binom j2}{h\brack j}_2=0\) for \(h>0\). Substitution produces the stated exact law. For each \(d\le n\), a diagonal matrix with exactly \(d\) unit diagonal entries and otherwise zero entries has exactly \(2^d\) fixed vectors; hence every predicted support value is attained.

**Step 4: Two moments.** The first frame polynomial is \(F_1(D)=2^D-1=N(M)\), and the second is \(F_2(D)=N(M)(N(M)-1)\). Thus \(\mathbb E[N]=H(1)=1-q^{-n}\) and \(\mathbb E[N(N-1)]=H(2)=(1-q^{-n})(1-q^{1-n})\) (with the same expression equal to zero at \(n=1\)). Rearranging \(\mathbb E[N^2]-\mathbb E[N]^2\) gives the variance formula.

**Step 5: Uniform limiting law and quantitative bound.** Write
\[
a_{k,d}=\frac{2^{\binom{k-d}{2}}{k\brack d}_2}{G_k}\quad(k\ge d).
\]
For fixed \(d\), \(a_{k,d}=O_d(2^{-k^2/2+O_d(k)})\), so \(S_d=\sum_{k=d}^{\infty}2^k a_{k,d}\) is finite. For all \(q\ge2\) and \(k\le n\), the elementary product bound gives
\[
0\le 1-H_{n,q}(k)\le\sum_{i=0}^{k-1}q^{i-n}\le2^{k-n}.
\]
The finite inversion formula hence differs from the infinite series \(\sum_{k=d}^\infty(-1)^{k-d}a_{k,d}\) by at most \(2^{-n}\sum_{k=d}^n 2^k a_{k,d}+\sum_{k>n}a_{k,d}\le2^{1-n}S_d\). The infinite series is the classical fixed-space probability for a uniform element of \(\mathrm{GL}_n(\mathbb F_2)\) as \(n\to\infty\), evaluated by the Euler product identity; it equals the stated product, with the claimed uniform bound by taking \(C_d=2S_d\).

**Step 6: Singular conditioning.** Precisely a fraction \(c_{n,q}=\prod_{j=1}^n(1-q^{-j})\) of full matrices are invertible. On that event the established perfect-algebra idempotent distribution is \(Q_n(d)\), independent of \(q\), and \(Q_n(d)\to p_{\infty}(d)\). Total probability gives the conditional-law formula. At each fixed \(q\), \(c_{n,q}\to c_q=\prod_{j\ge1}(1-q^{-j})\), which lies strictly between zero and one. Since both \(P_{n,q}(d)\) and \(Q_n(d)\) tend to the same limit, so does their conditional singular combination. Finally, \(D=n\) forces an entire \(K\)-basis of fixed vectors by Step 1, so \(M\) must be invertible, establishing the forbidden singular top stratum.

## Verification

The standalone Python 3 program `verify.py` uses exact rational inversion and direct exhaustive evaluation of the idempotent equation over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\). It checks dimensions \(n=1\) for two fields, \(n=2\) for three fields, and \(n=3,4\) over \(\mathbb F_2\); the maximum check exhausts all \(65{,}536\) four-dimensional binary matrices. The complete output is `verification_output.txt` and terminates in `VERIFY_OK`. In dimension two, the nonzero-idempotent count histograms for \(q=2,4,8\) are respectively \((6,9,1)\), \((76,150,30)\), and \((1240,2268,588)\) at counts \((0,1,3)\). These finite exhaustions corroborate, but do not replace, the all-dimensional proof.

To reproduce: run `python3 verify.py` from the directory containing the standalone verification program. Only the Python standard library is used.

## Relationship to prior work

Kaygorodov, Martín González and Viruel (2026) pose random-evolution-algebra statistics questions and derive the expected number of nonzero idempotents for uniformly **invertible** structure matrices. The existing exact field-size-universal law for invertible matrices identifies its whole distribution with the \(\mathrm{GL}_n(\mathbb F_2)\) fixed-space law. The **distribution for invertible matrices, its Gaussian inversion method, and its limiting constant are prior work**. They are not claimed here. The present computation samples **all** matrices, has the distinct finite-dimensional moments \(H_{n,q}(k)\), gives the exact field-dependent full-matrix census, and additionally yields the conditional **singular** law and its shared limit. The perfect-algebra formula by itself does not determine the singular mass, because the latter has positive asymptotic probability at every fixed \(q\).

The normal-form theorem of Dempwolff, Fisher and Herman (2000) concerns semilinear transformations and their conjugacy over algebraic closures, not probability distributions for uniformly sampled singular finite matrices. Classical uniform square-matrix rank counts recover the present \(q=2\) specialization, when coordinate squaring is the identity, and are likewise not claimed as new. The familiar fixed-space probability for uniform binary general linear groups (Fulman and Stanton, drawing on Rudvalis and Shinoda) supplies the already-known limiting product.

## Limitations

The finite-dimensional all-matrix law depends on \(q\); exact field-size independence is asserted only for the previously known invertible model and for the **limit** of the present model. The conditional singular limit requires a fixed field size, not a growing one. No assertion concerns odd characteristic, uniform sampling of isomorphism classes, scheme multiplicity of solutions, or independent historical priority. A full-text copy of the motivating 2026 survey could not be retrieved in this review, though its arXiv record and the relevant claims quoted by subsequent work were checked. Older or unindexed general random-semilinear-map literature may contain equivalent derivations; the originality comparison is bounded rather than exhaustive.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public 2026-10-15), Question 22 and Remark 23. https://arxiv.org/abs/2610.22248
2. *A field-size-universal idempotent law in characteristic-two perfect evolution algebras* (2026), full result and proof, including the invertible-matrix law. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-field-size-universal-idempotent-law-in-characteristic-two-perf--f7b48d77ae66/RESULT.md
3. *Field-independent idempotent-count law for characteristic-two perfect evolution algebras* (2026), invertible-model count. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-field-independent-idempotent-count-law-for-characteristic-two-pe--3591a9c3116b/RESULT.md
4. U. Dempwolff, J. C. Fisher and A. Herman, *Semilinear transformations over finite fields are Frobenius maps*, Glasgow Math. J. 42 (2000), 289–295. https://doi.org/10.1017/S0017089500020164
5. J. Fulman and D. Stanton, *On the distribution of the number of fixed vectors for the finite classical groups* (2015), Theorem 2.1, recalling Rudvalis–Shinoda. https://dornsife.usc.edu/jason-fulman/wp-content/uploads/sites/224/2023/06/fulman-stantonfinal.pdf
