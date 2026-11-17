# Exactly one negative eigenvalue for third-order shifted Cesàro self-commutators

## Finding

For every \(-1<\alpha<0\), the compact self-adjoint self-commutator
\[
K_\alpha=M_{\alpha,3}^{*}M_{\alpha,3}-M_{\alpha,3}M_{\alpha,3}^{*}
\]
has **exactly one strictly negative eigenvalue**, counted with multiplicity. Here \(M_{\alpha,3}\) is the third-order generalized Cesàro matrix defined below. Thus its negative Morse index equals one throughout the entire negative-shift interval. No formula for the eigenvalue itself is asserted.

## Assumptions and scope

Work on the complex Hilbert space \(\ell^2(\mathbb N_0)\). Fix a real \(\alpha\) with \(-1<\alpha<0\), and define the bounded lower triangular operator
\[
(M_{\alpha,3})_{nj}=\begin{cases}
\displaystyle\frac{3(n-j+1)(n-j+2)}{(n+\alpha+1)(n+\alpha+2)(n+\alpha+3)},&0\le j\le n,\\
0,&j>n.
\end{cases}
\]
The boundedness, dense-range identity, and defect decomposition quoted below are from Ma [1], Sections 2.1–2.4. The conclusion concerns only integer order three and real shifts in \((-1,0)\), not arbitrary orders, nonreal shifts, or the values of positive eigenvalues.

## Proof

**1. A three-term bounded defect decomposition.** Define
\[
H(n)=(n+\alpha+1)(n+\alpha+2)(n+\alpha+3),\quad
D(n)=(n+\alpha+4)(n+\alpha+5)(n+\alpha+6),
\]
\(r_n=1-H(n)/D(n)>0\), and \(R=\operatorname{diag}(r_n)\). Specializing Ma's exact identity [1, Theorem 2.3] to order three yields a bounded \(B\) and vectors \(v_0,v_1,v_2\in\ell^2\) with
\[
K_\alpha=M_{\alpha,3}^{*}EM_{\alpha,3},\qquad
E=I-B^*B=R+9\alpha v_0v_0^*+48\alpha(\alpha^2-1)v_1v_1^*
 +5\alpha(\alpha^2-1)(\alpha^2-4)v_2v_2^*.
\]
Here \(v_j(n)=p_{3,j}(n;\alpha)/D(n)\), where the polynomials \(p_{3,j}\) are monic of degree \(2-j\); in particular \(v_2(n)=D(n)^{-1}\). The rank-one notation means \(vv^*x=\langle x,v\rangle v\). On \(-1<\alpha<0\), the first and last finite-rank coefficients are negative, while the middle coefficient is positive. Put \(a_2=-5\alpha(\alpha^2-1)(\alpha^2-4)>0\).

**2. The final negative rank-one term is absorbed by the diagonal.** For every integer \(n\ge0\),
\[
\frac{H(n)}{D(n)}
=\prod_{j=1}^{3}\frac{n+\alpha+j}{n+\alpha+j+3}
\le\frac{n+\alpha+1}{n+\alpha+4}
\le\frac{n+1}{n+4},
\]
so \(r_n\ge3/(n+4)\ge1/(n+2)\). Since \(\alpha>-1\), also \(D(n)\ge(n+3)^3\). With \(x=-\alpha\in(0,1)\),
\[
a_2=5x(1-x^2)(4-x^2)
\le \frac{40}{3\sqrt3}<8,
\]
using \(\max_{0\le x\le1}x(1-x^2)=2/(3\sqrt3)\). Hence
\[
\begin{aligned}
a_2\|R^{-1/2}v_2\|_2^2
&=a_2\sum_{n\ge0}\frac{1}{D(n)^2r_n}\\
&<8\sum_{n\ge0}\frac{n+2}{(n+3)^6}
\le8\sum_{j\ge3}j^{-5}
\le 8\int_2^\infty t^{-5}\,dt
=\frac18.
\end{aligned}
\]
The elementary weighted Cauchy–Schwarz inequality therefore gives, for every \(z\in\ell^2\),
\[
\langle(R-a_2v_2v_2^*)z,z\rangle
\ge\frac78\langle Rz,z\rangle\ge0.
\]
Because \(48\alpha(\alpha^2-1)>0\), the operator
\[
P=R+48\alpha(\alpha^2-1)v_1v_1^*-a_2v_2v_2^*
\]
is positive. Thus \(E=P+9\alpha v_0v_0^*\) is a positive operator plus **one negative rank-one operator**, and its negative quadratic-form index is at most one. The same is true of \(K_\alpha=M^*EM\).

**3. A genuinely negative direction.** The monicity of the polynomials from [1, Eq. (2.13)] gives
\[
v_0(n)\sim n^{-1},\quad v_1(n)=O(n^{-2}),\quad v_2(n)=O(n^{-3}),\quad r_n\sim9n^{-1}.
\]
For each \(N\), take the finitely supported vector \(z_N(n)=v_0(n)/r_n\) when \(0\le n\le N\) and zero otherwise. Then
\[
E_N=\langle Rz_N,z_N\rangle
=\langle z_N,v_0\rangle
=\sum_{n=0}^{N}\frac{|v_0(n)|^2}{r_n}\sim\frac19\log N\longrightarrow\infty.
\]
In contrast, \(\langle z_N,v_1\rangle=O(1)\), because \(v_0(n)v_1(n)/r_n=O(n^{-2})\); the \(v_2\)-term is nonpositive. Consequently
\[
\langle Ez_N,z_N\rangle
\le E_N+48\alpha(\alpha^2-1)O(1)+9\alpha E_N^2<0
\]
for all sufficiently large \(N\), since \(\alpha<0\). Therefore \(E\) has at least one negative direction. Ma's finite-support right inverse [1, Eq. (2.2)] shows that the range of \(M_{\alpha,3}\) contains \(c_{00}\) and is dense. By continuity, a negative direction for \(E\) is approximable by an element of the range of \(M\), so \(K_\alpha\) also has a negative direction. Its negative index is exactly one.

**4. From index to eigenvalue.** Since \(r_n\to0\), \(R\) is compact, and \(E\) is a compact diagonal operator plus three rank-one operators. Therefore \(K_\alpha=M^*EM\) is compact and self-adjoint. The spectral theorem identifies its negative Morse index with the number of strictly negative eigenvalues counted with multiplicity. This number is precisely one. \(\square\)

## Verification

The proof above is analytical and does not infer infinite-dimensional spectral inertia from finite truncations. Its decisive numerical constants can be checked exactly: \(a_2<8\) follows from one one-variable cubic maximum, and \(8\sum_{n\ge0}(n+3)^{-5}\le1/8\) follows by integral comparison. Every denominating factor remains strictly positive for \(-1<\alpha<0\). The trace-class status is not needed; compactness follows directly from the exhibited diagonal-plus-finite-rank decomposition.

## Relationship to prior work

Ma [1] established the bounded defect identity and proved hyponormality precisely for nonnegative real shifts, obtaining one negative quadratic-form witness for every negative real shift. The present argument determines the **full negative index** at order three: two rank-one coefficients have negative signs, but one is uniformly dominated by the positive diagonal. Rhaly's earlier order-three study [2] provided supraposinormality and hyponormality results for certain nonnegative parameters, without this negative-inertia classification. An order-one negative-index result and a general trace formula were separately found in relevant research records [3,4]; neither implies the order-three assertion.

## Limitations

No classification is proved for orders four and higher or for complex shift parameters. The positive spectrum, eigenvalue magnitude, and eigenvector are not computed. The rank-one decomposition is taken from [1], and bibliographic priority remains subject to deeper older-literature comparison. A separate independent verification has not been performed.

## References

[1] Y. Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1 (first public 18 September 2026), Sections 2 and 7, https://arxiv.org/html/2610.00193v1.

[2] H. C. Rhaly Jr., *The generalized Cesàro matrices of order three are supraposinormal on \(\ell^2\)*, arXiv:1903.07896 (2019), https://arxiv.org/abs/1903.07896.

[3] *Infinite negative inertia under nonreal shifts of the Cesàro matrix*, research record 2026/11/8/SCOPE-infinite-negative-inertia-under-nonreal-shifts-of-the-ces-ro-mat--f33d5c640367 (order one only).

[4] *A shift-invariant harmonic trace for generalized Cesàro self-commutators*, research record 2026/10/11/SCOPE-a-shift-invariant-harmonic-trace-for-generalized-ces-ro-self-com--b9745d36b9d7 (trace, not inertia).
