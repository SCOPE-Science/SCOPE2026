# Square-zero random matrix products: an exact rank census and a sharp three-sevenths exponent

## Finding
For every prime power \(q\) and integer \(n\ge1\), independently sample \(A,B\) uniformly from \(M_n(\mathbb F_q)\). Define \(R=\operatorname{rank}A\) and \(S=\operatorname{rank}(ABA)\). Write \({a\brack b}_q\) for the Gaussian binomial coefficient, and \(G_j(q)=|\operatorname{GL}_j(\mathbb F_q)|\), with \(G_0(q)=1\). For \(0\le s\le\lfloor r/2\rfloor\) let
\[
K_{n,q}(r,s)={n\brack r}_q^2G_r(q)q^{n(n-r)}{r\brack s}_q{r-s\brack s}_qG_s(q)q^{(r-s)(n-r)}.
\]
The **exact joint count** of ordered pairs satisfying \((AB)^2=0\), \(R=r\), \(S=s\), is \(K_{n,q}(r,s)\); all other strata are empty. In particular,
\[
\boxed{\Pr((AB)^2=0)=q^{-2n^2}\sum_{r=0}^{n}\sum_{s=0}^{\lfloor r/2\rfloor}K_{n,q}(r,s).}
\]
For each fixed \(q\), constants \(0<c_q<C_q<\infty\) independent of \(n\) satisfy
\[
\boxed{c_q q^{-3n^2/7}\le \Pr((AB)^2=0)\le C_q q^{-3n^2/7}.}
\]
Conditioned on \((AB)^2=0\), the two ranks concentrate at \(R=5n/7+O_q(1)\) and \(S=2n/7+O_q(1)\): for \(t\ge0\),
\[
\Pr\!\left(\left.\sqrt{(R-5n/7)^2+(S-2n/7)^2}\ge t\,\right|(AB)^2=0\right)
\le C'_q q^{-t^2/4}
\]
for some constant \(C'_q\) independent of \(n,t\). The comparison single uniform matrix \(X\) obeys \(\Pr(X^2=0)=\Theta_q(q^{-n^2/2})\); hence
\[
\boxed{\frac{\Pr((AB)^2=0)}{\Pr(X^2=0)}=\Theta_q(q^{n^2/14}).}
\]
Thus a product is exponentially (in \(n^2\)) more likely to be square-zero than a single uniform matrix, while square-zero products become extremely rare even among all nilpotent products.

## Assumptions and scope
Here \((AB)^2=0\) means the product is nilpotent of **index at most two**, including zero. Neither factor is assumed square-zero, nilpotent, invertible, or commuting. All matrices are square and sampled independently, each with probability \(q^{-n^2}\). For a chosen \(A\), the induced endomorphism on \(U=\operatorname{im}A\) is the restriction \(C=(AB)|_U\), and \(\operatorname{rank}C=\operatorname{rank}(ABA)\), because \(A:\mathbb F_q^n\to U\) is surjective. The notation \(\Theta_q\) means two positive multiplicative constants depending only on the fixed field order \(q\). The Gaussian factors are zero outside their usual feasible ranges. The conditional concentration applies for any real \(t\ge0\) and all \(n\ge1\).

## Proof
**1. Rank of the first factor.** A rank-\(r\) matrix \(A:\mathbb F_q^n\to\mathbb F_q^n\) is specified by its \(r\)-dimensional image and kernel and an isomorphism between the quotient by the kernel and the image. Therefore the number of such matrices is
\[
N_{n,r}={n\brack r}_q^2G_r(q).
\]
Fix one such \(A\), write \(V=\mathbb F_q^n=U\oplus W\), where \(U=\operatorname{im}A\) has dimension \(r\) and \(W\) has dimension \(n-r\). As \(B\) varies, \(AB\) varies uniformly over every linear map \(V\to U\), each with \(q^{n(n-r)}\) preimages \(B\), because \(\dim\ker(A\circ -)=n(n-r)\). In adapted coordinates,
\[
AB=\begin{pmatrix}C&D\\0&0\end{pmatrix},\quad C\in M_r(\mathbb F_q),\quad D\in M_{r,n-r}(\mathbb F_q).
\]
The square is \(\bigl(\begin{smallmatrix}C^2&CD\\0&0\end{smallmatrix}\bigr)\). Hence \((AB)^2=0\) exactly when \(C^2=0\) and every column of \(D\) lies in \(\ker C\).

**2. Rank-refined square-zero blocks.** Suppose \(\operatorname{rank}C=s\), so \(0\le s\le\lfloor r/2\rfloor\). Choose \(I=\operatorname{im}C\), an \(s\)-subspace of \(U\). Choose \(H=\ker C\), an \((r-s)\)-subspace containing \(I\). Choose the induced isomorphism \(U/H\to I\). There are respectively \({r\brack s}_q\), \({r-s\brack s}_q\), and \(G_s(q)\) choices. Each yields a unique square-zero \(C\). For each, \(\dim\ker C=r-s\), so all admissible \(D\) number \(q^{(r-s)(n-r)}\). Combining with the rank-\(r\) first factors and the uniform fiber of \(B\mapsto AB\) proves precisely \(K_{n,q}(r,s)\), with no missing or repeated pairs.

**3. Exact quadratic exponent.** Let \(\gamma_q=\prod_{j\ge1}(1-q^{-j})>0\). The standard product formulas give, uniformly over all integers \(0\le b\le a\),
\[
\gamma_q q^{b(a-b)}\le {a\brack b}_q\le \gamma_q^{-1}q^{b(a-b)},\quad
\gamma_q q^{a^2}\le G_a(q)\le q^{a^2}.
\]
It follows that every nonempty stratum's probability contribution \(q^{-2n^2}K_{n,q}(r,s)\) lies between positive \(q\)-dependent constants times \(q^{E_n(r,s)}\), where
\[
E_n(r,s)=-n^2+2nr-ns-2r^2+3rs-2s^2.
\]
Completing squares gives the **exact identity**
\[
E_n(r,s)=-\frac{3n^2}{7}
-\frac{(r-5n/7)^2+(s-2n/7)^2}{2}
-\frac{3\bigl((r-5n/7)-(s-2n/7)\bigr)^2}{2}.
\]
The integral feasible set \(0\le s\le r/2\le n/2\) contains an integer lattice point at bounded Euclidean distance from \((5n/7,2n/7)\), uniformly in \(n\): use the nearest integers when \(n\) is sufficiently large, since the optimum lies a positive linear distance from all nontrivial bounding lines; the finitely many smaller \(n\) admit a uniform bound. That stratum gives the lower bound. The sum of all other strata is bounded above by a translate of the full two-dimensional convergent theta sum \(\sum_{(i,j)\in\mathbb Z^2}q^{-((i-a)^2+(j-b)^2)/2}\), uniformly in fractional shifts \(a,b\in[0,1]\), giving the upper bound. Hence the entire probability is \(\Theta_q(q^{-3n^2/7})\), with no hidden polynomial factor.

**4. Concentration.** On the complement of the radius-\(t\) disk centered at the continuous optimum, split the quadratic penalty \(\frac12(x^2+y^2)\) into \(\frac14(x^2+y^2)+\frac14(x^2+y^2)\). The first factor is at most \(q^{-t^2/4}\), and summing the second over the lattice gives a uniform constant. Divide by the lower bound from step 3. This yields the stated all-\(n,t\) conditional Gaussian tail.

**5. Single-matrix comparison.** The number of square-zero matrices of rank \(s\) in \(M_n(\mathbb F_q)\) is exactly \({n\brack s}_q{n-s\brack s}_qG_s(q)\), by step 2. Dividing by \(q^{n^2}\), the \(s\)-th term is within constants of \(q^{-n^2+2s(n-s)}=q^{-n^2/2-2(s-n/2)^2}\). A bounded-distance rank and the convergent one-dimensional theta sum give \(\Theta_q(q^{-n^2/2})\). Divide by the product's already-proved probability to obtain \(\Theta_q(q^{n^2/14})\). This completes all claims.

## Verification
Run `python3 verify_squarezero_product.py` from the package and compare output to `verification_output.txt`. Independent direct multiplication, squaring, and rank elimination exhaust **all** \(n\)-square ordered pairs over the prime fields at \((q,n)=(2,1),(2,2),(3,2),(2,3)\), and test **every joint stratum** \((\operatorname{rank}A,\operatorname{rank}ABA)\). The largest case checks all \(262{,}144\) ordered pairs, not a sample. Integer-arithmetic formula evaluations at four larger dimensions give supplementary asymptotic numerical checks. All computations are finite corroboration; the all-prime-power result follows from the preceding proof and bounds.

## Relationship to prior work
Sarma and Subedi (2026) introduce the nilpotent-product probability for finite rings and study that **unrestricted nilpotency** event. Kovács (1987) gives an earlier formula for unrestricted nilpotent matrix products, including lengths greater than two. The published exact full-matrix law \(\Pr(AB\text{ nilpotent})=2q^{-n}-q^{-2n}\) is **prior work**, not part of the originality claim. An earlier published calculation counts the opposite extreme, products with one *regular* nilpotent Jordan block, rather than products with all Jordan blocks of size at most two. This result isolates the latter event with an exact two-rank fiber law and derives a sharp three-sevenths exponent and conditional concentration; those assertions are not logical consequences of an aggregate nilpotency count or the regular-nilpotent stratum alone. Standard Gaussian-binomial and square-zero-matrix enumeration identities are used openly as known ingredients. Dolžan (2025, Theorem 3.2) already gives an exact formula for the factorization count of each prescribed target matrix depending only on its rank. Therefore the **unconditional square-zero-product probability** can in principle be summed from that result and known square-zero target counts; it is not claimed as an independently new universal product-distribution theorem. The distinct contribution here is the exact two-factor joint spectrum \(\bigl(\operatorname{rank}A,\operatorname{rank}(ABA)\bigr)\) and its sharp two-dimensional conditioned rank concentration, together with an explicit asymptotic exponent for the index-two event. The published prescribed-target theorem does not state those conditioned internal ranks or their concentration.

## Limitations
No exact prefactor or periodic theta constant is asserted in the asymptotic formula; it is a sharp exponent with uniform-in-\(n\) multiplicative bounds for fixed \(q\). The joint rank \(S\) is the rank of \(ABA\), not necessarily the rank of \(AB\). Factors are uniform, independent, and square with the same field; no result is claimed for nonuniform factors, local rings, or arbitrary nilpotency indices. The historical full text of Kovács (1987, 1988) was not obtained. Dolžan (2025) Theorem 3.2 was inspected in full and already subsumes the *marginal* product probability through a prescribed-target formula. Only the rank-resolved two-factor census, its conditioned concentration, and the explicitly computed sharp asymptotic are assessed as potentially new; priority for all three remains provisional pending broader checking. Independent mathematical audit has not been performed.

## References
1. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1 (first public October 6, 2026), https://arxiv.org/abs/2610.07892.
2. A. Kovács, *Some enumeration problems for matrices over a finite field*, Linear Algebra and its Applications **94** (1987), 223–236.
3. A. Kovács, *Products of matrices over a finite field*, Illinois Journal of Mathematics (1988).
4. T. Leinster, *The probability that an operator is nilpotent*, arXiv:1912.12562, https://arxiv.org/abs/1912.12562.
5. D. Dolžan, *The multiplication probability of a finite ring*, arXiv:2504.12886, https://arxiv.org/abs/2504.12886.
