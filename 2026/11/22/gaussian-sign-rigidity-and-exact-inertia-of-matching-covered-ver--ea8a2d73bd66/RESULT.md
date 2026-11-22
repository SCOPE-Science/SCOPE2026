# Gaussian sign rigidity and exact inertia of matching-covered vertex convolution

## Finding

Let \(n\ge 0\), let \(K_n\) be the labelled complete simple graph, and let \(\mu_n:\mathbb F_2^n\to\mathbb Z_{\ge0}\) count matchings by their *covered-vertex masks*. Thus \(\mu_n(x)\) is the number of matchings covering precisely the vertices with coordinate \(1\) in \(x\), and the empty matching is included. Consider unnormalized convolution
\[
(T_nf)(z)=\sum_{x\in\mathbb F_2^n}\mu_n(x)f(z+x).
\]
For a Walsh character \(\chi_\xi(x)=(-1)^{\langle\xi,x\rangle}\), write \(\lambda_n(\xi)=\sum_x\mu_n(x)\chi_\xi(x)\), and set \(k=|\xi|\) and \(q=\min(k,n-k)\).

**Theorem.** Every multiplier for \(n\ge4\) is nonzero, with the exact sign
\[
\operatorname{sgn}\lambda_n(\xi)=(-1)^q.
\]
The only zero multipliers at any dimension are the \(\binom21=2\) characters of weight one when \(n=2\) and the \(\binom31+\binom32=6\) characters of weights one and two when \(n=3\). Dimensions zero and one are invertible. Consequently \(T_n\) is invertible over \(\mathbb R\) or \(\mathbb C\) exactly when \(n\notin\{2,3\}\), with ranks \(\operatorname{rank}(T_2)=\operatorname{rank}(T_3)=2\).

For \(n\ge4\), let \(N_+(n)\) and \(N_-(n)\) count strictly positive and strictly negative eigenvalues, including multiplicity. For \(n=2m\ge4\),
\[
N_+(n)=N_-(n)=2^{n-1}.
\]
For \(n=2m+1\ge5\),
\[
N_+(n)=2^{n-1}+(-1)^m\binom{2m}{m},\qquad
N_-(n)=2^{n-1}-(-1)^m\binom{2m}{m}.
\]
In particular, the spectrum has a rigid alternating sign pattern indexed solely by the smaller of the positive and negative vertex-sign counts.

## Assumptions and scope

The ground field of the input to \(T_n\) has characteristic zero, and character values are \(\pm1\). The multiplicity \(\mu_n(x)\) counts distinct matchings with equal covered masks separately; it is not the Boolean indicator of perfectly matchable sets. More explicitly, \(\mu_n(x)=(|x|-1)!!\) for even \(|x|\), and \(\mu_n(x)=0\) for odd \(|x|\), where \((-1)!!=1\). Statements concern unnormalized Fourier coefficients and the standard real symmetric convolution matrix of dimension \(2^n\).

## Proof

1. **Matching masks and Gaussian moments.** Let \(Z\) be a real standard Gaussian. Since \(\mathbb E[Z^{2r}]=(2r-1)!!\) and odd moments vanish, for any signs \(s_i\in\{-1,1\}\),
\[
\sum_{M\text{ matching of }K_n}\prod_{v\in V(M)}s_v
=\mathbb E\prod_{i=1}^n(1+s_iZ).
\]
Choosing \(s_i=(-1)^{\xi_i}\) identifies the left side with \(\lambda_n(\xi)\). The right side depends only on the number \(k\) of negative signs, and is invariant under simultaneous sign reversal because it is a sum of even-degree monomials. Thus take \(q=\min(k,n-k)\), with \(p=n-q=q+d\), \(d\ge0\), to obtain
\[
\lambda_n(\xi)=\mathbb E[(1-Z^2)^q(1+Z)^d].
\]

2. **Positive centered moments.** Set \(X=Z^2-1\), \(a_j=\mathbb E[X^j]\). Its moment-generating function, for \(|t|<1/2\), is
\[
\mathbb E[e^{tX}]=e^{-t}(1-2t)^{-1/2}
=\exp\!\left(\sum_{r\ge2}\frac{2^{r-1}}r t^r\right).
\]
Every coefficient of the series in the exponential is nonnegative, and the coefficient of \(t^j\) in the exponent is strictly positive whenever \(j\ge2\). Hence \(a_0=1\), \(a_1=0\), and \(a_j>0\) for all \(j\ge2\). This argument establishes positivity of the *whole* moment and does not infer positivity from finite experiments.

3. **Exact sign and exceptional zeros.** Odd powers of \(Z\) average to zero against any polynomial in \(Z^2\). Expanding the preceding expectation, and using \(Z^{2r}=(1+X)^r\), gives the exact finite identity
\[
(-1)^q\lambda_n(\xi)
=\sum_{r=0}^{\lfloor d/2\rfloor}\binom d{2r}
\sum_{j=0}^r\binom rj a_{q+j}.
\tag{1}
\]
Every summand is nonnegative. If \(q=0\), the term \(r=j=0\) equals one. If \(q\ge2\), that term equals \(a_q>0\). If \(q=1\), the right side vanishes for \(d=0,1\); for \(d\ge2\), its \(r=j=1\) term is positive because \(a_2=2\). The exceptional pairs \((q,d)=(1,0),(1,1)\) give precisely \((n,k)=(2,1),(3,1),(3,2)\). Therefore the sign formula and all claimed ranks hold. For \(n=0,1\), the single empty matching has multiplier one at every character.

4. **Inertia.** For \(n\ge4\), all Walsh characters are eigenvectors and no eigenvalue vanishes. Each frequency of weight \(k\) has sign \((-1)^{\min(k,n-k)}\). The difference \(N_+(n)-N_-(n)\) therefore equals
\[
\sum_{k=0}^n\binom nk(-1)^{\min(k,n-k)}.
\]
For \(n=2m\), the sum is
\[
2\sum_{k=0}^{m-1}(-1)^k\binom{2m}k+(-1)^m\binom{2m}m=0.
\]
For \(n=2m+1\), it is
\[
2\sum_{k=0}^m(-1)^k\binom{2m+1}k
=2(-1)^m\binom{2m}m.
\]
Both evaluations use \(\sum_{k=0}^j(-1)^k\binom Nk=(-1)^j\binom{N-1}j\), a direct consequence of Pascal's identity. Combining with \(N_++N_-=2^n\) proves the stated inertia counts.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. The verifier explicitly enumerates matchings and performs full integer Walsh transforms for every \(0\le n\le12\); independently compares against a binomial signed-subset sum; computes centered-chi-square moments by an exact cumulant recurrence; checks identity (1), all signs, and inertia across \(0\le n\le50\). A completed run reports **11,014 exact assertions passed**. The all-size proof is mathematical; the finite checks are corroboration rather than a substitute for it. No external numerical package or corpus is required.

## Relationship to prior work

Wagner's preprint arXiv:math/0412059 (first posted 2004-12-02), and its 2008 extended rewrite arXiv:0803.1659, develop matching enumeration and the multivariate Heilmann–Lieb nonvanishing framework. The latter's positive-half-plane condition does not include arbitrary negative real vertex activities. Drake's arXiv:0909.1655 (first posted 2009-09-09), especially Section 5, relates complete-graph matching enumerators to Hermite polynomials and Gaussian moments; it does not present the covered-mask Walsh sign or inertia classification here. These works supply the natural objects and background, not an assertion of independent priority for the present specialization. Earlier signed-edge Fourier results distinguish *edge incidence* and do not directly imply the present *vertex coverage* spectrum.

## Limitations

The theorem does not give the smallest absolute nonzero eigenvalue, the optimal inverse norm, or analogous formulas for noncomplete graphs. A possible unindexed or implicit \(\pm1\)-specialization of older multivariate matching-polynomial identities remains a priority risk. A separate independent audit or external verification has not been performed.

## References

- D. G. Wagner, *Enumeration of spanning subgraphs with degree constraints*, arXiv:math/0412059 (2004), https://arxiv.org/abs/math/0412059.
- D. G. Wagner, *Weighted enumeration of spanning subgraphs with degree constraints*, arXiv:0803.1659 (2008), https://arxiv.org/abs/0803.1659.
- D. Drake, *Higher order matching polynomials and d-orthogonality*, arXiv:0909.1655 (2009), https://arxiv.org/abs/0909.1655.
