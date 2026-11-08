# Exact idempotent-count variance in random perfect evolution algebras over finite fields

## Finding

Let \(n\ge 2\), let \(q\) be any prime power, and choose \(M\) uniformly from \(\operatorname{GL}_n(\mathbb F_q)\). Use \(M\) as the coefficient operator of an \(n\)-dimensional perfect evolution algebra with a fixed natural basis: its idempotents have coordinate vectors \(x\in\mathbb F_q^n\) satisfying \(M x^{[2]}=x\), where \(x^{[2]}=(x_1^2,\ldots,x_n^2)^{\mathsf T}\). Denote by \(K_M\) the number of **nonzero** solutions.

Put \(Q=q^n\) and
\[
B_{n,q}=\begin{cases}
0,&\operatorname{char}\mathbb F_q=2,\\[2pt]
\displaystyle\frac{q-1}{2}\bigl((2q-1)^n-2q^n+1\bigr),&\operatorname{char}\mathbb F_q\ne2.
\end{cases}
\]
Then, **for every \(n\ge2\) and every prime power \(q\)**,
\[
\boxed{\mathbb E[K_M]=1,\qquad
\mathbb E[K_M(K_M-1)]=\operatorname{Var}(K_M)=
1-\frac{B_{n,q}}{(q^n-1)(q^n-q)}.}
\]
In particular, the variance equals exactly \(1\) in every even characteristic, but is strictly less than \(1\) in every odd characteristic. The odd-characteristic deficit has the asymptotics
\[
1-\operatorname{Var}(K_M)\sim
\frac{q-1}{2}\left(\frac{2q-1}{q^2}\right)^n
\quad(n\to\infty,\ q\text{ fixed and odd}),
\]
and, for each fixed \(n\ge2\),
\[
1-\operatorname{Var}(K_M)\sim(2^{n-1}-1)q^{1-n}
\quad(q\to\infty\text{ through odd prime powers}).
\]
The novelty claim is the dimension-uniform **second-moment** formula and the sharp characteristic dichotomy. The existing complete dimension-two idempotent distribution already implies the \(n=2\) specialization; it is not being claimed anew.

## Assumptions and scope

An evolution algebra over \(\mathbb F_q\) is a commutative, not necessarily associative, algebra with a natural basis \(e_1,\dots,e_n\) such that \(e_i e_j=0\) for distinct indices. Its multiplication is determined by the squares of basis vectors. A structure matrix is perfect exactly when invertible. We use the coordinate convention \(M x^{[2]}=x\), the transpose of a common row-wise structure-matrix convention; transposition is a bijection on invertible matrices, so the uniform distribution is unchanged.

The sample space is **labeled invertible structure matrices**, with all members equally likely. It is not the set of isomorphism classes with equal weights. The zero vector is not counted in \(K_M\). The lower bound \(n\ge2\) matters: in dimension one every invertible structure matrix has exactly one nonzero idempotent, so the variance is zero.

## Proof

**Step 1: the first moment.** Write \(V=\mathbb F_q^n\), \(Q=|V|\), and \(s(x)=x^{[2]}\). For every \(x\ne0\) one has \(s(x)\ne0\). The natural left action of \(\operatorname{GL}(V)\) is transitive on nonzero vectors, so
\[
\Pr_M\{M s(x)=x\}=\frac1{Q-1}.
\]
Summing over the \(Q-1\) nonzero vectors yields \(\mathbb E[K_M]=1\).

**Step 2: simultaneous fixed points.** Let \(x,y\) be distinct nonzero vectors. If \(y=cx\) with \(c\ne1\), then \(s(y)=c^2s(x)\). Were both \(M s(x)=x\) and \(M s(y)=y\) to hold, linearity would give \(c^2x=cx\), forcing \(c=1\), a contradiction. Thus a simultaneous pair must be linearly independent.

Suppose \(x,y\) are linearly independent. If \(s(x),s(y)\) are dependent, invertibility prevents \(M s(x)=x,\ M s(y)=y\). If both pairs are independent, a uniform invertible \(M\) sends the specified ordered independent source pair to the specified ordered independent target pair with probability exactly
\[
\frac1{(Q-1)(Q-q)},
\]
because \(\operatorname{GL}_n(\mathbb F_q)\) acts transitively on ordered independent pairs. Hence \(\mathbb E[K_M(K_M-1)]\) is \(1\) minus the fraction of ordered linearly independent pairs \((x,y)\) for which \(s(x),s(y)\) are dependent.

**Step 3: count the exceptional pairs.** There are \((Q-1)(Q-q)\) ordered independent nonzero pairs in total. In characteristic two, \(s\) is the coordinatewise Frobenius automorphism. It preserves and reflects linear dependence (with coefficients squared), so no independent pair has dependent squares; the exceptional count is zero.

Now assume odd characteristic. Fix a nonzero \(x\) with precisely \(r\) nonzero coordinates. If \(s(y)\) is a nonzero scalar multiple of \(s(x)\), then \(y\) has the same support as \(x\). Pick one support coordinate: its value \(y_j\) has \(q-1\) choices. Every other nonzero coordinate of \(y\) must have ratio \(y_i/x_i=\pm(y_j/x_j)\), giving \(2^{r-1}\) sign patterns. Exactly \(q-1\) of these \((q-1)2^{r-1}\) vectors are scalar multiples of \(x\). Therefore the number of exceptional, linearly independent vectors \(y\) is
\[
(q-1)(2^{r-1}-1).
\]
There are \(\binom nr(q-1)^r\) choices of \(x\) of support size \(r\), so the total exceptional ordered-pair count is
\[
\begin{aligned}
B_{n,q}&=\sum_{r=1}^n\binom nr(q-1)^r(q-1)(2^{r-1}-1)\\
&=\frac{q-1}{2}\bigl((2q-1)^n-2q^n+1\bigr).
\end{aligned}
\]
This establishes the formula for \(\mathbb E[K_M(K_M-1)]\).

**Step 4: variance and boundaries.** Since \(\mathbb E K_M=1\), the identity
\[
\operatorname{Var}(K_M)=\mathbb E[K_M(K_M-1)]+\mathbb E K_M-(\mathbb E K_M)^2
\]
reduces variance to the same factorial second moment. For odd characteristic and \(n\ge2\), support size two already contributes a positive number to \(B_{n,q}\), proving strict inequality. The two displayed asymptotics follow by retaining the leading exponential for fixed odd \(q\), respectively the leading powers of \(q\) for fixed \(n\). In both limits the denominator is asymptotic to \(q^{2n}\). This completes the proof.

## Verification

The standalone Python script `checks/variance_checker.py` enumerates all invertible matrices and independently counts their nonzero idempotents, over prime and extension fields. It does **not** use the variance formula to enumerate. It calculates exact rational empirical means and variances and compares them to the formula. It also directly counts exceptional ordered pairs of vectors (for the tested field-size bounds) and verifies their predicted number.

Exact exhaustive cases are \((q,n)=(2,2),(3,2),(5,2),(7,2),(4,2),(8,2),(9,2),(2,3),(3,3),(2,4)\). Notably, for \((q,n)=(3,3)\), the 11,232 matrices have histogram \(\{0:3600,1:5056,2:1800,3:600,4:120,5:48,7:8\}\), giving variance \(23/26\). The characteristic-two cases have variance exactly \(1\), as predicted. The script's complete output is in `checks/variance_verification_output.txt`, ending in `VERIFY_OK`. Numerical enumeration is corroboration, not a proof for untested fields or dimensions.

Reproduce using `python3 checks/variance_checker.py` from the directory containing this document. The program uses only Python's standard library; its field arithmetic for the extension fields is explicit and finite.

## Relationship to prior work

Kaygorodov, Martín González, and Viruel, *Evolution algebras: a survey of results and a list of open problems* (arXiv:2610.22248v1, first posted 2026-10-15), Remark 23, proves the exact **first moment** \(\mathbb E[K_M]=1\) for uniform invertible structure matrices. Its Question 22 asks about random evolution algebras, and Conjecture 2 predicts the limiting fixed-point distribution from full symmetric monodromy. Neither statement gives an exact finite-field second moment; the present formula proves the predicted factorial second moment asymptotically without asserting the full distribution or the Galois conjecture.

Wei and Zou, *Isomorphism Classes of Idempotent Evolution Algebras* (arXiv:2310.12368v1), enumerate **isomorphism classes of perfect algebras** via a monomial-group action. That is a different random experiment from uniformly sampling structure matrices and counting element-level idempotents. The name "idempotent evolution algebra" in that paper refers to \(E^2=E\), not to the count \(K_M\).

A separately established dimension-two idempotent-count distribution contains the \(n=2\) case as a special case. The new result starts with the dimension-uniform formula and characteristic dependence for all \(n\ge3\), including an explicit \(n=3\) check.

## Limitations

The formula gives only the first and second moments, not the complete distribution, Galois group, or higher factorial moments. It concerns uniformly labeled perfect algebras, not isomorphism-class-uniform sampling, singular structure matrices, or arbitrary distributions on structure matrices. The all-dimensional result is a direct symbolic counting proof; independent expert validation and historical-priority certification have not been performed.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (2026-10-15), https://arxiv.org/abs/2610.22248. Relevant passages: Remark 23 (p. 19), Question 22 (p. 23), and Conjecture 2 (p. 27).
2. Y. Wei, Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (2023-10-18), https://arxiv.org/abs/2310.12368. Relevant passages: Introduction and orbit-counting method, §§1–2, and the dimension-three/four class-counting theorems.
