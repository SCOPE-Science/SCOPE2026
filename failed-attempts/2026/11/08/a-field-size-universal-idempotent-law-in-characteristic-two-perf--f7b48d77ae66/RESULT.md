# A field-size-universal idempotent law in characteristic-two perfect evolution algebras

## Finding

Fix an integer \(n\geq1\), a power \(q=2^s\) with \(s\geq1\), and a uniformly chosen matrix \(M\in\operatorname{GL}_n(\mathbb F_q)\). Construct the evolution algebra \(E_M\) with natural basis \(e_1,\ldots,e_n\), products \(e_ie_j=0\) for \(i\ne j\), and \(e_i^2=\sum_j M_{ij}e_j\). Let \(K_M\) be the number of its *nonzero* idempotents. Define \(D_M\) by \(K_M+1=2^{D_M}\).

**Theorem.** The number \(D_M\) is an integer in \(\{0,\ldots,n\}\). Its distribution is exactly that of the dimension of the ordinary fixed space of a uniform matrix \(B\in\operatorname{GL}_n(\mathbb F_2)\), independently of \(s\). Explicitly, for \(0\leq d\leq n\),
\[
\Pr\{K_M=2^d-1\}=\frac{1}{|\operatorname{GL}_d(\mathbb F_2)|}\sum_{j=0}^{n-d}\frac{(-1)^j2^{j(j-1)/2}}{2^{dj}|\operatorname{GL}_j(\mathbb F_2)|},
\]
where \(|\operatorname{GL}_0(\mathbb F_2)|=1\), and all other values of \(K_M\) have probability zero. The quantity on the right is the established finite-general-linear-group fixed-space probability, now identified with the entire idempotent law of this algebra family.

For each fixed \(d\geq0\), as \(n\to\infty\), the probability converges to
\[
\frac{\prod_{r=d+1}^{\infty}(1-2^{-r})}{|\operatorname{GL}_d(\mathbb F_2)|}
=\frac{\prod_{r=1}^{\infty}(1-2^{-r})}{2^{d^2}\prod_{r=1}^d(1-2^{-r})^2}.
\]
In particular, for every sequence of even prime powers \(q\) (including varying \(q\)), the probability of **no nonzero idempotent** tends to \(\prod_{r=1}^{\infty}(1-2^{-r})=0.2887880950866\ldots\) as \(n\to\infty\). At dimension three, the probabilities for \(K_M=0,1,3,7\) are respectively \(2/7,7/12,1/8,1/168\).

## Assumptions and scope

Every matrix entry is chosen through the uniform distribution on invertible \(n\)-by-\(n\) matrices, not through the distribution on isomorphism classes of evolution algebras. The coordinate convention is \(x^2=M^{\mathsf T}x^{[2]}\), where \(x^{[2]}\) squares each coordinate. The invertibility hypothesis is essential. The algebra is not presumed associative or unital. The coefficient field has characteristic exactly two, but need not equal the prime field. Nonzero idempotents exclude the zero vector. The theorem treats all positive dimensions and all finite fields of characteristic two, and makes no assertion for odd characteristic.

## Proof

**1. Semilinear fixed points.** Set \(T_M(x)=M^{\mathsf T}x^{[2]}\) on \(\mathbb F_q^n\). Since the characteristic is two, \(T_M(x+y)=T_M(x)+T_M(y)\) and \(T_M(cx)=c^2T_M(x)\). The idempotency equation is \(T_M(x)=x\). Thus its solution space \(V_M=\operatorname{Fix}(T_M)\) is an \(\mathbb F_2\)-vector space, and \(K_M=|V_M|-1\).

**2. Independence lemma.** Every \(\mathbb F_2\)-linearly independent collection of elements of \(V_M\) is linearly independent over \(\mathbb F_q\). Otherwise choose a minimal dependent subcollection \(v_1,\ldots,v_t\), and normalize the dependence relation to \(v_t=\sum_{i<t}c_i v_i\) with \(c_i\in\mathbb F_q\). Applying \(T_M\) and using that every \(v_i\) is fixed gives \(v_t=\sum_{i<t}c_i^2v_i\). Minimal dependence makes \(v_1,\ldots,v_{t-1}\) independent over \(\mathbb F_q\), so \(c_i^2=c_i\) for each \(i<t\). The only roots of \(z^2=z\) in \(\mathbb F_q\) are zero and one, yielding a forbidden \(\mathbb F_2\)-linear dependence. This proves the lemma and \(\dim_{\mathbb F_2}V_M\leq n\).

**3. Exact frame moments.** For \(0\leq k\leq n\), define \(F_k(d)=\prod_{i=0}^{k-1}(2^d-2^i)\), with the empty product \(F_0(d)=1\). This is the number of ordered, linearly independent \(k\)-tuples in a \(d\)-dimensional \(\mathbb F_2\)-space. By Step 2, every such tuple of fixed points is also an ordered \(\mathbb F_q\)-frame. There are \(N_{n,k}(q)=\prod_{i=0}^{k-1}(q^n-q^i)\) ordered \(\mathbb F_q\)-frames in the ambient space. Squaring coordinates preserves their \(\mathbb F_q\)-independence, because Frobenius is a field automorphism. For any chosen frame \((v_1,\ldots,v_k)\), the matrix \(M^{\mathsf T}\) carries \((v_1^{[2]},\ldots,v_k^{[2]})\) to \((v_1,\ldots,v_k)\) with probability exactly \(1/N_{n,k}(q)\), by transitivity of the uniform general linear group on frames. Summing indicators for all frames shows
\[
\mathbb E[F_k(D_M)]=1\qquad(0\leq k\leq n).
\]

**4. Identify the fixed-space law.** For a uniform \(B\in\operatorname{GL}_n(\mathbb F_2)\), put \(C_B=\dim_{\mathbb F_2}\ker(B-I)\). The same frame-transitivity argument gives \(\mathbb E[F_k(C_B)]=1\) for all \(0\leq k\leq n\). The matrix \((F_k(d))_{0\leq k,d\leq n}\) is triangular, with zero entries if \(k>d\) and nonzero diagonal \(F_d(d)=|\operatorname{GL}_d(\mathbb F_2)|\). Consequently, the vector of \(n+1\) frame moments uniquely determines a probability law supported on \(\{0,\ldots,n\}\). Hence \(D_M\) and \(C_B\) have the same law. This equality of distributions is the new bridge between the algebraic idempotent problem and the classical fixed-space problem.

**5. Explicit inversion.** Write \({d\brack k}_2=F_k(d)/|\operatorname{GL}_k(\mathbb F_2)|\) for the Gaussian binomial coefficient, and define \(p_d=\Pr\{D_M=d\}\). Step 3 gives \(\sum_{d=k}^{n}{d\brack k}_2 p_d=1/|\operatorname{GL}_k(\mathbb F_2)|\). Gaussian-binomial inversion, using \(\sum_{j=0}^h(-1)^j2^{j(j-1)/2}{h\brack j}_2=0\) for every positive \(h\), yields
\[
p_d=\sum_{k=d}^{n}\frac{(-1)^{k-d}2^{(k-d)(k-d-1)/2}{k\brack d}_2}{|\operatorname{GL}_k(\mathbb F_2)|}.
\]
The elementary identity \({d+j\brack d}_2/|\operatorname{GL}_{d+j}(\mathbb F_2)|=1/(2^{dj}|\operatorname{GL}_d(\mathbb F_2)||\operatorname{GL}_j(\mathbb F_2)|)\) converts this into the stated formula. It agrees with the previously known fixed-space enumeration for ordinary finite general linear groups (Fulman–Stanton, Theorem 2.1, recalling Rudvalis–Shinoda).

**6. Limit.** For fixed \(d\), the summands in Step 5 are absolutely summable as \(j\to\infty\) because \(|\operatorname{GL}_j(\mathbb F_2)|\) grows on the order of \(2^{j^2}\). Euler's \(q\)-binomial product identity with base \(1/2\) gives
\[
\sum_{j\geq0}\frac{(-1)^j2^{j(j-1)/2}}{2^{dj}|\operatorname{GL}_j(\mathbb F_2)|}=\prod_{r=d+1}^{\infty}(1-2^{-r}).
\]
Dividing by \(|\operatorname{GL}_d(\mathbb F_2)|\) proves the limiting mass. Taking \(d=0\) proves the idempotent-free limit. Uniformity in \(q\) is exact at each finite dimension by Step 4, rather than an asymptotic approximation.

## Verification

An independent finite-field enumerator is supplied as `verify.cpp`. It constructs \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), enumerates all invertible matrices in six dimension–field combinations, directly enumerates vectors satisfying \(x=M^{\mathsf T}x^{[2]}\), and checks each resulting histogram. The most demanding check examines all \(181440\) matrices in \(\operatorname{GL}_3(\mathbb F_4)\); another examines all \(20160\) matrices in \(\operatorname{GL}_4(\mathbb F_2)\). In total \(205482\) matrices were checked and all histograms matched the theorem. The recorded output concludes `VERIFY_OK cases=6 matrices=205482`.

Reproduce with a C++17 compiler using `g++ -std=c++17 -O3 verify.cpp -o verify` and `./verify`. The full original output is included as `verification_output.txt`. This computation checks selected finite instances only; the proof above establishes the general theorem.

## Relationship to prior work

Kaygorodov, Martín González, and Viruel (2026), Remark 23, established that the expected number of nonzero idempotents is exactly one for uniform invertible structure matrices over every finite field. Their Question 22 asks for further statistics of random evolution algebras. That first-moment result does not determine the present complete distribution. The same survey discusses conjectural generic Galois behavior in characteristic zero; the present theorem addresses a different fixed-characteristic regime.

Fulman and Stanton (2015), Theorem 2.1, record the complete fixed-space distribution for ordinary uniform \(\operatorname{GL}_n(\mathbb F_2)\) matrices, building on Rudvalis and Shinoda. That **classical distribution is not claimed as new**. The contribution here is the all-dimension identification with random characteristic-two evolution-algebra idempotents and the resulting exact independence from the extension degree of the field.

Wei and Zou (2023) enumerate isomorphism classes of idempotent evolution algebras, rather than this labeled-matrix idempotent-count distribution. Dempwolff, Fisher, and Herman (2000), Sections 1–5, establish semilinear normal forms, a fixed-point statement over an algebraic closure, and applications to classical groups and projective geometry. Their inspected text does not establish the uniform finite-matrix idempotent distribution here. Their older related normal-form literature remains a priority-check risk.

The dimension-two specialization of the present theorem and the first two moments are already accessible by more limited enumerations; the specific new assertion is the **complete distribution in arbitrary dimension, with exact field-size invariance and the limiting probabilities**. No assertion of independently certified historical priority is made.

## Limitations

The random model is uniform on invertible labeled structure matrices; uniform isomorphism-class sampling is different. The proof uses characteristic two and does not transfer without modification to odd characteristic, where coordinatewise squaring is not additive. The result determines the number of rational idempotents, not their scheme multiplicities or automorphism groups. A complete literature search cannot establish absolute novelty; semilinear fixed-subspace literature beyond the inspected primary articles may contain equivalent probabilistic arguments. Independent external mathematical audit has not been performed.

## References

1. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15), Remark 23, Question 22, and Conjecture 2. https://arxiv.org/abs/2610.22248
2. J. Fulman and D. Stanton, *On the distribution of the number of fixed vectors for the finite classical groups* (2015), Theorem 2.1 (recalling Rudvalis and Shinoda). https://dornsife.usc.edu/jason-fulman/wp-content/uploads/sites/224/2023/06/fulman-stantonfinal.pdf
3. Y. Wei and Y. M. Zou, *Isomorphism classes of idempotent evolution algebras* (2023), arXiv:2310.12368. https://arxiv.org/abs/2310.12368
4. U. Dempwolff, J. C. Fisher, and A. Herman, *Semilinear transformations over finite fields are Frobenius maps*, Glasgow Mathematical Journal 42 (2000), 289–295. DOI:10.1017/S0017089500020164.
