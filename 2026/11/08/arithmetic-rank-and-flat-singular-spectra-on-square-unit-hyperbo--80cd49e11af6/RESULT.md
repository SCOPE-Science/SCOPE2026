# Arithmetic rank and flat singular spectra on square-unit hyperbolas modulo prime squares

## Finding

For every odd prime \(p\), let \(R=\mathbb Z/p^2\mathbb Z\), \(Q=(R^\times)^2\) (unit squares), and
\[
S=\{(t,t^{-1}):t\in Q\}\subset R^2.
\]
For each \(c\in R^\times\), take the primitive additive character \(\psi_c(x)=\exp(2\pi i cx/p^2)\). On the hyperbola subset \(S\), the unnormalized square Fourier matrix is
\[
H_{p,c}(t,u)=\psi_c(tu+t^{-1}u^{-1}),\qquad t,u\in Q.
\]
It has \(p(p-1)/2\) rows and columns. Its **exact complex rank** is
\[
\operatorname{rank}H_{p,c}=
\begin{cases}
(p-1)(p+3)/8,&p\equiv1\pmod8,\\
(p-1)^2/8,&p\equiv5\pmod8,\\
(p-1)^2/4,&p\equiv3,7\pmod8.
\end{cases}
\]
In particular, the operator is never injective for odd \(p\). When \(p\equiv3\pmod4\), its complete singular-value multiset is
\[
\{p\text{ with multiplicity }(p-1)^2/4,\quad
0\text{ with multiplicity }p(p-1)/2-(p-1)^2/4\}.
\]
Thus \(H_{p,c}/p\) is a partial isometry in these congruence classes. The ranks do not depend on the choice of primitive additive character.

## Assumptions and scope

All vector spaces and ranks are over \(\mathbb C\). The pairing on \(R^2\) is \((x_1,x_2)\cdot(y_1,y_2)=x_1y_1+x_2y_2\). Here \(p\) is an odd prime, not an arbitrary odd modulus, and \(c\) must be a unit modulo \(p^2\): additive characters with conductor \(p\) are not covered. No normalization by the ambient group size or the cardinality of \(S\) is performed.

The subgroup \(Q\) has order \(p(p-1)/2\). Its reduction modulo \(p\) is the subgroup \(Q_0=(\mathbb F_p^\times)^2\), of order \(h=(p-1)/2\). Each residue in \(Q_0\) has a unique Teichmüller lift \(w\in R^\times\) satisfying \(w^{p-1}=1\) and reducing to that residue. The group \(Q\) splits as the product of these \(h\) lifts and \(1+pR\).

## Proof

**1. Convert Fourier sampling into abelian convolution.** Set \(K(v)=\psi_c(v+v^{-1})\) for \(v\in Q\). Since \(H_{p,c}(t,u)=K(tu)\), permuting columns by inversion yields \(C(t,u)=K(tu^{-1})\). Every character \(\chi\in\widehat Q\) is an eigenvector of this group convolution, with eigenvalue \(\lambda_\chi=\sum_{v\in Q}K(v)\overline{\chi(v)}\). The permutation is unitary, so the singular values of \(H_{p,c}\) are \(|\lambda_\chi|\), counting characters.

**2. Evaluate each multiplier by a complete stationary-phase sum.** Every character is uniquely indexed by a tame character \(\theta\in\widehat{Q_0}\) and a wild index \(a\in\mathbb F_p\), with
\[
\chi\big(w(1+ps)\big)=\theta(\bar w)\exp(2\pi i as/p),\qquad s\in\mathbb F_p,
\]
where \(w\) is a Teichmüller lift and \(\bar w\in Q_0\) its reduction. For \(s\in\mathbb F_p\),
\[
w(1+ps)+[w(1+ps)]^{-1}
\equiv w+w^{-1}+ps(w-w^{-1})\pmod{p^2}.
\]
Summation over \(s\) therefore gives the **exact identity**
\[
\lambda_{\theta,a}=
p\!\sum_{\substack{x\in Q_0\\c(x-x^{-1})=a}}
\overline{\theta(x)}\,
\exp\big(2\pi i c(w_x+w_x^{-1})/p^2\big),
\]
where \(w_x\) is the unique Teichmüller lift of \(x\), and the congruence in the subscript is modulo \(p\). Thus \(\lambda_{\theta,a}=0\) if the fiber of \(x\mapsto c(x-x^{-1})\) on \(Q_0\) is empty.

**3. Prove that no nonempty stationary fiber cancels.** If \(x-x^{-1}=y-y^{-1}\), then \((x-y)(xy+1)=0\), so the fiber contains at most \(x\) and \(y=-x^{-1}\). A singleton contributes a nonzero term of modulus \(p\). For two distinct points, \(w_y=-w_x^{-1}\), and hence the two exponential phases differ by \(\exp(4\pi i c(w_x+w_x^{-1})/p^2)\). The residue \(x+x^{-1}\) is nonzero: otherwise \(x^2=-1\), giving \(y=x\). Thus this exponential is a primitive \(p^2\)-th root. The ratio of the tame-character factors is a root of unity of order dividing \(h\), which is prime to \(p\). The two terms cannot have ratio \(-1\). It follows that
\[
\lambda_{\theta,a}\ne0\iff a\in c\,\{x-x^{-1}:x\in Q_0\}.
\]

**4. Count the fibers and spectral multiplicities.** Put \(\phi(x)=x-x^{-1}\) and \(J(x)=-x^{-1}\). All nontrivial fibers are exactly the two-element orbits of \(J\). If \(p\equiv3\pmod4\), \(-1\) is a nonsquare, so \(J\) exchanges squares and nonsquares: \(\phi\) is injective on \(Q_0\), and its image has size \(h\). Since there are \(h\) tame characters, the rank is \(h^2=(p-1)^2/4\), and every nonzero multiplier is a single term of modulus \(p\). If \(p\equiv1\pmod4\), \(J\) is an involution of \(Q_0\). Its fixed points are the roots of \(x^2=-1\); both lie in \(Q_0\) exactly when \(p\equiv1\pmod8\). Writing \(f=2\) in that case and \(f=0\) for \(p\equiv5\pmod8\), the number of orbits (and hence the size of the image of \(\phi\)) is \((h+f)/2\). Multiplying by \(h\) yields precisely the two remaining rank formulas. Multiplication by the unit \(c\) does not alter image cardinality, completing the proof.

## Verification

The independent-to-the-algebra numerical script `checker.py` constructs \(H_{p,c}\) directly and computes its singular values for \(p\in\{3,5,7,11,13\}\) and \(c\in\{1,2\}\), retaining only units \(c\). It compares numerical ranks to the three exact arithmetic formulas, and for \(p\equiv3\pmod4\) checks that all positive singular values equal \(p\). It also enumerates the stationary-image sizes exactly for \(p\in\{17,19,23,29,31,37,41\}\). Invoke `python checker.py` after installing `requirements.txt`; the script prints `SQUARE_UNIT_HYPERBOLA_RANK_PASS` on success. This is finite corroboration only; the proof above establishes all odd primes.

## Relationship to prior work

D. Kelmer's 2008 preprint (Section 2, Proposition 2.1) gives an exact stationary-phase formula for multiplicatively twisted Kloosterman sums on the **full group of units** modulo an even prime power. This proof uses the same elementary stationary-phase mechanism but concerns the **index-two square subgroup** and deduces its Fourier sampling rank, a modulo-eight orbit dichotomy, and flat positive singular values in the \(p\equiv3\pmod4\) classes. No new claim is made for Kelmer's full-unit sum evaluations or their distribution theory.

J. Hickman and J. Wright study norm inequalities and restriction over the full rings \(\mathbb Z/N\mathbb Z\). Their 2018 results motivate ring-based restriction analysis but are not an exact self-sampling rank statement for the square-unit hyperbola. The classical finite-field hyperbola and finite-field torus sampling problems have different ambient additive groups and cannot transfer the prime-square stationary fibers merely by reducing modulo \(p\).

## Limitations

The theorem is for the specific index-two subgroup of unit squares modulo an odd prime **square**. It does not classify other subgroup indices, higher prime powers, imprimitive additive characters, or sharp nonzero singular values in the classes \(p\equiv1\pmod4\). The elementary stationary-phase computation closely resembles classical twisted Kloosterman techniques, and potential equivalent historical presentations remain a priority risk. No independent mathematical audit has been performed.

## References

1. D. Kelmer, *Distribution of twisted Kloosterman sums modulo prime powers*, arXiv:0801.4162, first version posted 2008-01-27, Section 2. https://arxiv.org/abs/0801.4162
2. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176, first version posted 2018-01-09, especially Sections 1–2 and 6. https://arxiv.org/abs/1801.03176
