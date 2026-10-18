# Sharp cubic-graph Fourier extension with nonconstant antipodal extremizers

## Finding
For every finite field \(\mathbb F_q\) of characteristic \(p>3\), the cubic graph
\[ C_q=\{(u,u^3):u\in\mathbb F_q\}\subseteq\mathbb F_q^2 \]
has sharp Fourier extension inequality
\[
\sum_{x,t\in\mathbb F_q}|\mathcal E_q f(x,t)|^4
\le\left(3-\frac6{2q+1}\right)
\left(\frac1q\sum_{u\in\mathbb F_q}|f(u)|^2\right)^2.
\]
Equivalently, its exact \(L^2\to L^4\) operator norm is \(\bigl(3-6/(2q+1)\bigr)^{1/4}\) under the measures below. Every nonzero extremizer is explicitly classified: there is a common \(\lambda\in\mathbb C\setminus\{0\}\) and, independently for each unordered antipodal pair, a phase \(\theta_u\in\mathbb R\), such that
\[
f(0)=\sqrt3\lambda,\quad
f(u)=\sqrt2\lambda e^{i\theta_u},\quad
f(-u)=\sqrt2\lambda e^{-i\theta_u}.
\]
In particular, constants do **not** maximize the cubic-graph inequality, unlike several quadratic-graph analogues. This conclusion covers prime fields and non-prime finite fields without a congruence restriction.

## Assumptions and scope
Let \(q=p^r\) for a prime \(p>3\) and integer \(r\ge1\). Fix any nontrivial additive character \(\chi\) of \(\mathbb F_q\). Define
\[
\mathcal E_q f(x,t)=q^{-1}\sum_{u\in\mathbb F_q}f(u)\chi(xu+tu^3),\qquad (x,t)\in\mathbb F_q^2.
\]
The physical \(L^4\) norm uses counting measure, \(\|h\|_4^4=\sum_{x,t}|h(x,t)|^4\). The input \(L^2\) norm uses normalized counting measure, \(\|f\|_{2,\sigma}^2=q^{-1}\sum_u|f(u)|^2\). The empty signal satisfies the inequality trivially but is not considered an extremizer. No assertions are made in characteristics \(2\) or \(3\).

## Proof
**1. The only nontrivial collision fiber is the antipodal one.** For \(u,v\in\mathbb F_q\), let \(\Phi(u,v)=(u+v,u^3+v^3)\). Write \(s=u+v\). The identity
\[
u^3+v^3=s^3-3suv
\]
shows that, when \(s\ne0\), the image \(\Phi(u,v)\) fixes the product \(uv\). The unordered pair \(\{u,v\}\) is then uniquely recovered as the roots (with multiplicity) of \(X^2-sX+uv\). This uses \(p\ne3\). When \(s=0\), all \(q\) ordered pairs \((u,-u)\) map to \((0,0)\). Thus every other fiber is either an ordered diagonal pair or a pair of swapped distinct points.

**2. Exact convolution identity.** Write \(S=\sum_u|f(u)|^2\), \(a=|f(0)|^2\), and
\[
H=\sum_{u\in\mathbb F_q}f(u)f(-u).
\]
Expanding the fourth power and using character orthogonality on \(\mathbb F_q^2\) gives
\[
q^2\|\mathcal E_q f\|_4^4
=\sum_{z\in\mathbb F_q^2}\left|\sum_{\Phi(u,v)=z}f(u)f(v)\right|^2
=2S^2-\sum_u|f(u)|^4-a^2
-2\sum_{u\ne0}|f(u)f(-u)|^2+|H|^2.
\tag{1}
\]
The separate subtraction of \(a^2\) is essential: the diagonal pair \((0,0)\) is already included in the zero-sum collision fiber and cannot be counted twice.

**3. Reduction to two masses.** Homogeneity permits \(S=1\). Let \(m=(q-1)/2\). For each of the \(m\) unordered nonzero antipodal pairs indexed by \(j\), write
\[
t_j=|f(u_j)|^2+|f(-u_j)|^2,\qquad b_j=2|f(u_j)f(-u_j)|\le t_j,
\]
\[
B=\sum_{j=1}^m b_j,\qquad \sum_{j=1}^m t_j=1-a,\qquad 0\le B\le1-a.
\]
For each pair \(\lvert f(u_j)\rvert^4+\lvert f(-u_j)\rvert^4=t_j^2-b_j^2/2\). Using (1), the triangle inequality \(|H|\le a+B\), and Cauchy–Schwarz for both pair sums yields
\[
\frac{\|\mathcal E_q f\|_4^4}{\|f\|_{2,\sigma}^4}
\le F(a,B)
:=2-2a^2-\frac{(1-a)^2}{m}-\frac{B^2}{2m}+(a+B)^2.
\tag{2}
\]
For fixed \(a\), \(F(a,B)\) is strictly convex in \(B\) (its \(B^2\) coefficient is \(1-1/(2m)>0\)), so its maximum for \(0\le B\le1-a\) occurs at \(B=0\) or \(B=1-a\). At the first endpoint,
\[
F(a,0)=2-a^2-\frac{(1-a)^2}{m}\le2-\frac1{m+1}.
\tag{3}
\]
At the second endpoint,
\[
F(a,1-a)=3-2a^2-\frac{3(1-a)^2}{2m}
\le3-\frac6{4m+3}=3-\frac6{2q+1},
\tag{4}
\]
with unique equality at \(a=3/(4m+3)=3/(2q+1)\). Since \(m\ge2\), the bound (4) is strictly larger than (3). This proves the inequality.

**4. Every equality case.** Strict superiority of (4) forces \(B=1-a>0\); thus \(b_j=t_j\) for every pair, so each pair has equal coordinate magnitudes. Equality in both Cauchy–Schwarz inequalities forces \(t_j=(1-a)/m\) and \(b_j=(1-a)/m\) for every \(j\). Therefore the normalized masses are
\[
|f(0)|^2=\frac3{2q+1},\qquad |f(u)|^2=\frac2{2q+1}\quad (u\ne0).
\]
Equality in the phase triangle inequality requires each product \(f(u)f(-u)\) to have the same argument as \(f(0)^2\). Taking \(\lambda=f(0)/\sqrt3\), this is precisely the parameterization in the finding. Conversely, these magnitudes and phase relations make every inequality in steps 2–3 an equality, proving both sharpness and the complete extremizer classification.

## Verification
The supplied standalone standard-library `verify.py` checks unordered-pair fiber uniqueness for every nonzero sum, compares the exact collision expression with a direct enumeration of all ordered pairs, tests forty deterministic pseudorandom complex vectors per field, and independently realizes equality with nontrivial phase choices. Tested fields are \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_{11}\), \(\mathbb F_{13}\), and \(\mathbb F_{25}\), the last represented with an explicit irreducible quadratic extension. All \(200\) random comparisons and five equality tests passed to floating-point tolerance \(5\times10^{-12}\). The proof above, not these tests, covers infinitely many field sizes.

As an additional analytic check, the constant input has fourth-power ratio \(3-3/q+1/q^2\), below the sharp ratio by exactly \((q-1)/(q^2(2q+1))>0\). Hence this result cannot be a mere constant-function energy calculation.

## Relationship to prior work
Koh and Shen [1] proved the \(L^2\to L^4\) finite-field extension *exponent range* for all plane algebraic curves with no linear component. This covers boundedness for the cubic graph but does not supply this numerical best constant or equality classification. González-Riquelme and Oliveira e Silva [2] established best constants on quadratic paraboloids, hyperbolic paraboloids, and cones, with distinct collision fibers; their covered surfaces do not include \((u,u^3)\). Biswas and collaborators [3] investigated the full moment curve \((u,u^2,\ldots,u^d)\) at its endpoint; this is not the sparse cubic graph in dimension two. Existing sharp quadratic-curve proofs therefore cannot be substituted for the antipodal fiber computation above.

## Limitations
The result requires characteristic greater than three and the stated counting-measure normalization. It makes no claim of independent auditing, prior publication, or priority over any unindexed mathematically equivalent theorem. The closest published analyses prove general curve boundedness or sharp estimates for different algebraic surfaces; an unnoticed treatment of this special cubic graph remains an originality risk. Numerical tests cover only the listed finite fields and do not certify the universal theorem independently.

## References
[1] D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240 (2010), Theorem 1.1 and Section 3. https://arxiv.org/html/1003.4240v3

[2] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (first submitted 2024-05-26), Theorems 1.1–1.6 and Sections 1–3. https://arxiv.org/html/2405.16647v2

[3] C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377 (2025), Introduction and main theorems. https://arxiv.org/html/2508.08377v1
