# Exact rank transitions and sharp synchronization of random fixed-rank retractions

## Finding

Let \(n\ge3\) and \(2\le r<n\). On the labeled set \(X=[n]\), let \(\mathcal E_{n,r}\) be the set of all idempotent transformations \(e:X\to X\) of image rank \(r\). Put \(N=\binom nr r^{n-r}\). Independently choose \(E_1,E_2,\ldots\), each uniformly on \(\mathcal E_{n,r}\), and set \(P_k=E_k\circ\cdots\circ E_1\), \(R_k=|\operatorname{im}P_k|\).

For \(1\le t\le s\le r\), define the rational number
\[
Q_{s,t}=\frac{1}{\binom ns}\sum_{a=\max(0,s-n+r)}^{\min(s,r,t)}
\binom ra\binom{n-r}{s-a}\binom{r-a}{t-a}\frac{1}{r^{s-a}}
\sum_{j=0}^{t-a}(-1)^j\binom{t-a}{j}(t-j)^{s-a}.
\]
All inadmissible binomial coefficients are zero, and \(Q_{s,t}=0\) for \(t>s\). Then \(Q\) is a stochastic lower-triangular matrix, and for every \(k\ge1\)
\[
\boxed{\Pr(R_k=t)=(Q^{k-1})_{r,t}.}
\]
In particular, writing \(c_z:X\to X\) for the constant map with value \(z\in X\), the complete prescribed-constant factorization law is
\[
\boxed{\#\{(e_1,\ldots,e_k)\in\mathcal E_{n,r}^k:
 e_k\circ\cdots\circ e_1=c_z\}
 =\frac{N^k}{n}(Q^{k-1})_{r,1}.}
\]

Let \(\nu\) be uniform on the \(n\) constant transformations. Then **the total-variation distance on the full transformation monoid** is exactly
\[
\boxed{d_{\mathrm{TV}}(\mathcal L(P_k),\nu)=
\sum_{t=2}^{r}(Q^{k-1})_{r,t}.}
\]
The diagonal entries \(\lambda_s=Q_{s,s}\) satisfy
\(1=\lambda_1>\lambda_2>\cdots>\lambda_r>0\), with
\[
\boxed{\lambda_2=1-\frac{(n-r)(n+r-1)}{r n(n-1)}.}
\]
For \(r=2\), the total-variation distance is exactly \(\lambda_2^{k-1}\). For \(r\ge3\), define \(c_2=1\), and recursively for \(3\le s\le r\) define
\[
c_s=\frac{\sum_{t=2}^{s-1}Q_{s,t}c_t}{\lambda_2-\lambda_s}.
\]
Then all \(c_s>0\) and the sharp synchronization law is
\[
\boxed{d_{\mathrm{TV}}(\mathcal L(P_k),\nu)
=c_r\lambda_2^{k-1}+O_{n,r}(\lambda_3^{k-1})
\qquad(k\to\infty).}
\]
Thus the exact exponential decay base and its strictly positive amplitude are explicit for every \(n,r\).

For example, \(n=4,r=3\) gives \(\lambda_2=5/6\), \(\lambda_3=1/2\), \(c_3=3/2\), and the **exact** identity
\[
d_{\mathrm{TV}}(\mathcal L(P_k),\nu)
=\frac32\left(\frac56\right)^{k-1}
-\frac12\left(\frac12\right)^{k-1}.
\]

## Assumptions and scope

Every transformation is a **total** selfmap on the same labeled \(n\)-set. A transformation is idempotent if and only if it fixes each point of its image. For each \(r\)-subset \(B\subset X\), exactly \(r^{n-r}\) such maps have image and fixed set \(B\): all points of \(B\) are fixed, and each other point freely chooses one root in \(B\). Therefore \(N=\binom nr r^{n-r}\), with \(B\) uniform and assignments independent uniform when a factor is uniform. Composition is right-to-left, as indicated. \(k\ge1\) is an integer, no independence of images is assumed across intermediate products, and the error constant in the asymptotic may depend on fixed \(n,r\).

## Proof

**1. Image rank is strongly lumpable.** Fix an arbitrary map \(f\) having image \(S\subseteq X\) of cardinality \(s\). For an independent uniform \(E\in\mathcal E_{n,r}\),
\(\operatorname{rank}(E\circ f)=|E(S)|\). Because the law of \(E\) is invariant under conjugation by the symmetric group, the distribution of \(|E(S)|\) depends only on \(s\), not on \(f\) or the specific subset \(S\). Thus the rank process is Markov, initialized at \(R_1=r\).

**2. Exact conditional image count.** Let \(B=\operatorname{im}(E)=\operatorname{Fix}(E)\), and put \(a=|S\cap B|\). There are \(\binom ra\binom{n-r}{s-a}\) subsets \(S\) of this intersection type for each fixed \(B\); equivalently, for each fixed \(S\) the same hypergeometric probability holds for a uniform \(B\). Of the \(s\) inputs, \(a\) are fixed roots of \(E\), and the other \(b=s-a\) independently choose uniformly among the \(r\) roots. To obtain total image cardinality \(t\), choose \(t-a\) additional roots out of the other \(r-a\), then require every chosen additional root to be hit at least once while allowing arbitrary use of the original \(a\) roots. Inclusion-exclusion gives
\[
\binom{r-a}{t-a}\sum_{j=0}^{t-a}(-1)^j\binom{t-a}{j}(t-j)^{s-a}
\]
assignments out of the \(r^{s-a}\) equally likely assignments. Multiplication by the hypergeometric weight, and summation over \(a\), yields \(Q_{s,t}\). These events partition all assignments, proving \(\sum_t Q_{s,t}=1\) and the power formula.

**3. Individual constant products and total variation.** Every permutation \(\sigma\in S_n\) conjugates the factor law to itself, and sends \(c_z\) to \(c_{\sigma(z)}\). Hence the probability of each particular constant product equals \(\Pr(R_k=1)/n\). Multiplying by the \(N^k\) equiprobable ordered words gives the stated exact fiber count. Since \(\nu\) is supported on constants and the product's conditional distribution on constants is uniform, the total-variation distance from \(\nu\) equals the probability that the product is not constant. This proves the exact mixing-distance identity, with no assumption that higher-rank targets have equal fibers.

**4. Strict eigenvalue order.** \(\lambda_s=Q_{s,s}\) is the probability that \(E\) is injective on an arbitrary fixed \(s\)-subset. Nested subsets imply \(\lambda_s\le\lambda_{s-1}\). The inequality is strict for \(2\le s\le r\): choose a root set \(B\) containing \(s-1\) specified points but omitting the extra point and map that extra point to any one of the \(s-1\) roots. This event has positive probability and is injective on the first \(s-1\) points but not all \(s\). Also \(\lambda_s>0\) because a root set can contain all \(s\) specified points. Finally \(\lambda_1=1\).

**5. The two-point eigenvalue.** For distinct inputs \(x,y\), the event \(E(x)=E(y)\) is impossible if both are roots; if exactly one is a root it has probability \(1/r\); if neither is a root it also has probability \(1/r\). The probability at least one point is not a root equals \(1-r(r-1)/(n(n-1))\). Dividing by \(r\) proves
\[
1-\lambda_2=\frac{1}{r}\left(1-\frac{r(r-1)}{n(n-1)}\right)
=\frac{(n-r)(n+r-1)}{r n(n-1)}.
\]

**6. Sharp convergence and coefficient.** Delete absorbing state \(1\) and take the substochastic lower-triangular matrix \(T=(Q_{s,t})_{2\le s,t\le r}\). Its strictly positive and pairwise distinct diagonal eigenvalues are \(\lambda_2>\cdots>\lambda_r>0\). Define the vector \(c\), indexed by \(2,\ldots,r\), by \(c_2=1\) and the displayed recursion. Then \(Tc=\lambda_2 c\). Every numerator is nonnegative and contains the strictly positive term \(Q_{s,s-1}c_{s-1}\), whose positivity follows by fixing \(s-1\) inputs as roots and identifying the remaining input with a previous root; hence \(c_s>0\). As \(T\) is triangular with distinct eigenvalues, it is diagonalizable. Its left \(\lambda_2\)-eigenvector is the row vector supported on state \(2\) and normalized to have coordinate \(1\), so the spectral projector is \(c\) times that row. Therefore
\[
\mathbf e_r^{\mathsf T}T^{k-1}\mathbf1
=c_r\lambda_2^{k-1}+O_{n,r}(\lambda_3^{k-1})
\]
for \(r\ge3\), and equals \(\lambda_2^{k-1}\) for \(r=2\). The left side is the probability of remaining at rank at least two. The illustrative exact formula follows by diagonalizing the two-state transient chain when \(n=4,r=3\).

## Verification

The standalone Python standard-library script `verify.py` directly constructs every fixed-rank idempotent map for \(3\le n\le5\), \(2\le r<n\) and computes actual compositions of every ordered word of lengths \(1,2,3\). It separately derives the formula \(Q_{s,t}\) by rational combinatorial arithmetic, compares every row against direct image-rank observations, compares every product rank against powers of the independently calculated \(Q\), and checks every prescribed constant-target fiber. All six parameter pairs pass. The captured output is in `verification_output.txt`. Run `python3 verify.py` with the Python standard library. This is a finite cross-check; the proof above establishes the universal quantifiers.

## Relationship to prior work

The classical generation results of Howie and of Howie–McFadden concern whether transformations can be written as products of idempotents and how many generators or factors suffice, not the numbers and probabilities of uniform prescribed-length products. Dolinka–East–Mitchell (arXiv:1504.02520, first publicly posted 2015-04-09) give idempotent-generation and minimal-generating-set counts for partition-preserving transformation monoids, including foundational full-transformation results in their introduction. Their inspected complete text does not supply the displayed rank transition kernel or sharp stochastic synchronization amplitude. Barnes–Cerrito–Levi (1998) study random walks on finite semigroups and transition-block structure at a broader level; the accessible abstract does not resolve whether their complete paper gives a specialized implication. Budzban–Feinsilver (2011) study finite transformation semigroups and probabilistic limiting kernels; the inspected full text contains no fixed-rank uniform-retraction transition or exact spectral amplitude. The closest published product-rank census available for two idempotents requires their product to be idempotent; these random products are unrestricted and have arbitrary length. Published convergence laws for order-decreasing chain contractions and for symmetric inverse monoids have different underlying maps and different transition kernels. When \(r=n-1\), factors collapse exactly one chosen point onto another; elementary coalescence is classical and is not itself claimed new. The asserted complete kernel and leading amplitude cover all fixed ranks \(2\le r<n\), including the more complicated simultaneous-merger regime.

## Limitations

This is a complete **image-rank distribution** and **constant-target fiber** result, not a prescribed-target fiber formula for nonconstant transformations. It requires uniform independent idempotents all of the same fixed image rank; neither dependence nor arbitrary nonuniform factor laws is addressed. The sharp convergence statement fixes \(n,r\) and takes \(k\to\infty\), rather than giving a simultaneous \(n,k\) cutoff. Historical-priority verification is limited to the listed inspected full texts and accessible abstracts; the 1998 random-walk paper and some older generation articles were not read in full, so unindexed equivalences remain a risk. Independent mathematical audit has not been performed.

## References

1. I. Dolinka, J. East, and J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition*, arXiv:1504.02520v1, first posted 2015-04-09, https://arxiv.org/abs/1504.02520; published Bulletin of the Australian Mathematical Society 93 (2016), DOI:10.1017/S0004972715000751.
2. J. M. Howie, *Products of idempotents in finite full transformation semigroups*, Proceedings of the Royal Society of Edinburgh Section A 86 (1980), 243–254, DOI:10.1017/S0308210500012154.
3. J. M. Howie and R. B. McFadden, *Idempotent rank in finite full transformation semigroups*, Proceedings of the Royal Society of Edinburgh Section A 114 (1990), 161–167, DOI:10.1017/S0308210500024355.
4. G. R. Barnes, P. B. Cerrito, and I. Levi, *Random walks on finite semigroups*, Journal of Applied Probability 35 (1998), 824–832, DOI:10.1239/jap/1032438378.
5. G. Budzban and P. Feinsilver, *A hierarchical structure of transformation semigroups with applications to probability limit measures*, arXiv:1103.0235v1 (2011-03-01), https://arxiv.org/abs/1103.0235.
