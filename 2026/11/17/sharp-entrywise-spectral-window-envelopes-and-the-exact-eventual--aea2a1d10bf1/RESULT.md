# Sharp entrywise spectral-window envelopes and the exact eventual-positivity horizon

## Finding
Let \(n\geq3\), let \(u\in\mathbb R^n\) satisfy \(u_i>0\) for every coordinate and \(\|u\|_2=1\), and fix \(0<\delta<L\). Consider **all** real symmetric matrices \(A\) satisfying
\[
 Au=0,\qquad \sigma(A|_{u^\perp})\subseteq[-L,-\delta].
\]
For \(i\ne j\) set \(r_i=\sqrt{1-u_i^2}/u_i\), and for \(t>0\) write \(a=e^{-Lt}\), \(b=e^{-\delta t}\). Then the exact, attained envelope of the \((i,j)\) entry over this entire class is
\[
\boxed{\quad u_i u_j\left(1-\frac{a+b}{2}\right)-\frac{b-a}{2}\sqrt{(1-u_i^2)(1-u_j^2)}\ \leq\ (e^{tA})_{ij}\ \leq\ u_i u_j\left(1-\frac{a+b}{2}\right)+\frac{b-a}{2}\sqrt{(1-u_i^2)(1-u_j^2)}.\quad}
\]
Each endpoint is attained, simultaneously for **every** positive \(t\), by a suitable generator with spectrum exactly \(\{0,-\delta,-L\}\). The endpoint generators may depend on the chosen entry, but not on time.

Define the coordinate-imbalance invariant
\[
 R(u)=\max_{1\le i<j\le n}r_i r_j,
 \qquad H_{\delta,L}(t)=\frac{2-e^{-Lt}-e^{-\delta t}}{e^{-\delta t}-e^{-Lt}}\quad(t>0).
\]
The function \(H_{\delta,L}\) increases strictly from \((L+\delta)/(L-\delta)\) to \(+\infty\). Consequently the sharp universal positivity onset for the stated class is
\[
\boxed{\quad T(u,\delta,L)=
\begin{cases}
0,&R(u)\le (L+\delta)/(L-\delta),\\
\text{the unique }T>0\text{ with }H_{\delta,L}(T)=R(u),&R(u)>(L+\delta)/(L-\delta).
\end{cases}\quad}
\]
Every admissible \(e^{tA}\) is entrywise strictly positive for \(t>T\), and is entrywise nonnegative for \(t=T>0\). When \(T>0\), one fixed admissible three-level matrix has a negative entry at **each** \(0<t<T\). Thus no earlier uniform nonnegative time works. When \(T=0\), every admissible exponential has strictly positive entries at every positive time.

In the equally spaced case \(L=2\delta\), the onset becomes explicitly
\[
 T=\delta^{-1}\max\!\left\{0,\log\frac{R(u)-1}{2}\right\},
\]
where the maximum expression is used when \(R(u)>1\), and understood as zero otherwise. For instance, in dimension three \(u=(3,4,12)/13\) has \(R(u)=\sqrt{170}\), so the sharp onset is \(\delta^{-1}\log((\sqrt{170}-1)/2)\).

## Assumptions and scope
The order is the coordinatewise cone order on \(\mathbb R^n\). An entrywise nonnegative exponential means it maps the nonnegative cone into itself; strictly positive means every matrix entry is positive. The leading eigenvalue is normalized to zero, with strictly positive, fixed unit eigenvector \(u\). The remaining eigenvalues lie in a *closed* strictly negative interval; no irreducibility, Metzler condition, or prescribed remaining eigenvectors is assumed. The lower and upper envelope optimize over the whole stated symmetric matrix class, not just a fixed generator. The dimension restriction \(n\ge3\) ensures that the orthogonal projections of any two coordinate vectors onto \(u^\perp\) are independent.

## Proof
**1. Exact reduction to an order interval.** Set \(P=uu^{\mathsf T}\), \(Q=I-P\). Symmetry and \(Au=0\) give \(AP=PA=0\) and \(e^{tA}=P+Qe^{tA}Q\). The spectral assumption yields
\[
 aQ\preccurlyeq Qe^{tA}Q\preccurlyeq bQ,
\]
so there is a self-adjoint operator \(K\) with \(0\preccurlyeq K\preccurlyeq Q\), acting trivially on \(\mathbb Ru\), such that
\[
 e^{tA}=P+aQ+(b-a)K. \tag{1}
\]
Conversely, every orthogonal projection \(K\preccurlyeq Q\) is realized simultaneously at every \(t\) by the fixed symmetric matrix
\[
 A_K=-\delta K-L(Q-K). \tag{2}
\]
Its eigenvalues are zero on \(\mathbb Ru\), \(-\delta\) on the range of \(K\), and \(-L\) on the complement inside \(u^\perp\).

**2. Optimizing a pair of coordinates.** For \(i\ne j\), set \(v_i=Qe_i\), \(v_j=Qe_j\), where \(e_i\) are coordinate unit vectors. Write \(\alpha=\|v_i\|=\sqrt{1-u_i^2}\), \(\beta=\|v_j\|=\sqrt{1-u_j^2}\), and \(c=\langle v_i,v_j\rangle=-u_i u_j\). Both \(\alpha,\beta\) are strictly positive. Because \(u\) has a nonzero coordinate distinct from \(i,j\), the vectors \(v_i,v_j\) are linearly independent; hence \(\alpha\beta>|c|\).

Define the symmetric rank-two matrix \(S=(v_i v_j^{\mathsf T}+v_j v_i^{\mathsf T})/2\) on \(u^\perp\). Its only two nonzero eigenvalues are
\[
 \lambda_+=\frac{c+\alpha\beta}{2}>0,
 \qquad \lambda_-=\frac{c-\alpha\beta}{2}<0. \tag{3}
\]
Indeed, the eigenvectors are \(z_+=v_i/\alpha+v_j/\beta\) and \(z_-=v_i/\alpha-v_j/\beta\), which are orthogonal; applying \(S\) directly gives (3). For every effect \(0\preccurlyeq K\preccurlyeq Q\),
\[
 \lambda_-\ \leq\ \operatorname{tr}(KS)=\langle Kv_i,v_j\rangle\ \leq\ \lambda_+. \tag{4}
\]
This follows by resolving the positive and negative eigenspaces: for each unit eigenvector \(z\), \(0\le\langle Kz,z\rangle\le1\), with zero contribution on the kernel. Equality in the lower (respectively upper) bound is attained by taking \(K\) to be the rank-one orthogonal projector onto the \(z_-\) (respectively \(z_+\)) ray. Both satisfy \(K\preccurlyeq Q\).

For \(i\ne j\), (1) now reads
\[
 (e^{tA})_{ij}=u_i u_j(1-a)+(b-a)\langle Kv_i,v_j\rangle.
\]
Substituting (3)–(4), together with \(c=-u_i u_j\), gives precisely both claimed envelope endpoints. The generators (2) built from the extremizing rank-one projectors attain equality for *all* \(t>0\), rather than merely at a single time.

**3. Exact simultaneous positivity onset.** A symmetric positive-definite matrix has strictly positive diagonal entries, so only off-diagonal entries need inspection. The attained lower envelope for \((i,j)\) is nonnegative if and only if
\[
 2-a-b\ge(b-a)r_i r_j,
 \quad\text{equivalently}\quad H_{\delta,L}(t)\ge r_i r_j. \tag{5}
\]
Thus *every* admissible exponential is entrywise nonnegative at time \(t>0\) if and only if \(H_{\delta,L}(t)\ge R(u)\). The same equivalence with strict inequalities characterizes universal strict positivity.

**4. Strict monotonicity.** Put \(m=(L+\delta)/2\) and \(d=(L-\delta)/2>0\), so \(m>d\). Algebra gives
\[
 H_{\delta,L}(t)=\frac{e^{mt}-\cosh(dt)}{\sinh(dt)}.
\]
The derivative has the sign of
\[
 F(t)=e^{mt}\bigl(m\sinh(dt)-d\cosh(dt)\bigr)+d.
\]
Here \(F(0)=0\) and
\[
 F'(t)=(m^2-d^2)e^{mt}\sinh(dt)>0\qquad(t>0),
\]
so \(H'_{\delta,L}(t)>0\). Its limit at the origin is \(m/d=(L+\delta)/(L-\delta)\); as \(t\to\infty\), it diverges. Equation (5) therefore determines the stated \(T\). When \(T>0\), choose a pair realizing \(R(u)\) and its lower-extremizing projection \(K\) from step 2. The associated *single* matrix \(A_K\) has that off-diagonal entry strictly negative at every \(0<t<T\), zero at \(T\), and positive thereafter. For all other admissible matrices, every off-diagonal entry is strictly positive when \(t>T\); diagonal positivity follows from positive definiteness. When \(T=0\), strict increase above the origin limit makes all off-diagonal entries strictly positive for every \(t>0\).

**5. Explicit three-level example.** When \(L=2\delta\), set \(x=e^{-\delta t}\). Direct cancellation gives \(H(t)=(2-x-x^2)/(x-x^2)=1+2e^{\delta t}\), proving the displayed onset formula. For \(u=(3,4,12)/13\) one calculates \(r_1r_2=\sqrt{170}\), larger than the other two products. The rank-one projection onto \(Qe_1/\|Qe_1\|-Qe_2/\|Qe_2\|\) gives the asserted negative-entry witness for every earlier positive time.

## Verification
The proof above is independent of computation. The accompanying `verify.py` checks exact rational projector identities, a three-dimensional balanced spectral-window example, and the predicted sign transition using Python's standard library; it also verifies the analytic two-dimensional eigenvalue formula symbolically for rational test data. These are finite diagnostics, not a proof for all dimensions, vectors, time parameters, or spectral fillings. The projector/effect argument, strict derivative sign, and explicit endpoint generator establish the universal quantifiers.

## Relationship to prior work
Dobrick's 2026 paper establishes a striking failure of uniform eventual positivity for certain infinite-dimensional self-adjoint semigroups with a positive leading eigenvector. Its motivating issue is the relation between individual and uniform eventual positivity, not a finite-dimensional sharp minimax time. Daners and Glück develop qualitative uniform eventual positivity criteria. The present result fixes the leading eigenvector and the entire complementary spectral window, then optimizes every off-diagonal entry over all real symmetric generators in finite dimensions. It therefore neither contradicts the infinite-dimensional counterexamples nor follows from their statements: the positivity onset necessarily depends on the smallest coordinates of \(u\), which need not be uniformly bounded below in infinite dimension.

The order-interval optimization uses elementary spectral calculus and rank-two matrix geometry, classical ingredients not claimed as new. The claimed contribution is the combination of attained all-time spectral-window entry envelopes, the exact worst-case positivity onset, and a persistent sharp three-level witness.

## Limitations
The result concerns real symmetric matrices, a prescribed strictly positive normalized dominant eigenvector, a *fixed closed interval* containing the remaining spectrum, and finite dimension at least three. It makes no claim for arbitrary nonnormal generators, coordinate systems in which the positive cone changes, infinite-dimensional lattices, or individual-generator optimal times. The claim of originality is a comparison with inspected accessible works, not a claim of exhaustive literature coverage or independent certification.

## References
- A. Dobrick, *Individual and Uniform Eventual Positivity of Self-Adjoint Semigroups*, arXiv:2609.00425v1 (first public 2026-08-31), https://arxiv.org/abs/2609.00425.
- D. Daners and J. Glück, *A criterion for the uniform eventual positivity of operator semigroups*, arXiv:1801.05179v1 (2018), https://arxiv.org/abs/1801.05179.
- D. Daners, J. Glück and J. B. Kennedy, *Eventually positive semigroups of linear operators*, arXiv:1511.09020 (2015), https://arxiv.org/abs/1511.09020.
