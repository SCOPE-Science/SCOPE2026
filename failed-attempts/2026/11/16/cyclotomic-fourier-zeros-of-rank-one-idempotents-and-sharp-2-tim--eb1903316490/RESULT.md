# Cyclotomic Fourier zeros of rank-one idempotents and sharp \(2\times2\) endpoint norms

## Finding

Let \(q=p^r\) be a prime power, \(p\) its characteristic, and \(n\ge1\). On the additive group \(G=M_n(\mathbb F_q)\), use the nondegenerate pairing \(\langle X,P\rangle=\operatorname{tr}(XP)\) and the additive character
\[
\psi(a)=\exp\bigl(2\pi i\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(a)/p\bigr).
\]
Let \(\mathcal I_n\) be the set of matrices satisfying \(P^2=P\) and \(\operatorname{rank}P=1\), and write
\[
S_n(X)=\sum_{P\in\mathcal I_n}\psi(\operatorname{tr}(XP)).
\]
For \(\lambda\in\mathbb F_q\), put \(g_\lambda(X)=\dim_{\mathbb F_q}\ker(X-\lambda I)\), and for \(t\in\mathbb F_p\), let
\[
A_t(X)=\sum_{\substack{\lambda\in\mathbb F_q\\\operatorname{Tr}(\lambda)=t}}
 \frac{q^{g_\lambda(X)}-1}{q-1}.
\]
Each \(A_t(X)\) is a nonnegative integer: it counts eigenlines of \(X\) whose eigenvalue has absolute trace \(t\).

**Complete coefficient and zero criterion.** For every prime power \(q\), every \(n\ge1\), and every \(X\in G\),
\[
\boxed{S_n(X)=q^{n-1}\sum_{t\in\mathbb F_p}A_t(X)e^{2\pi it/p};\qquad
 S_n(X)=0\ \Longleftrightarrow\ A_0(X)=A_1(X)=\cdots=A_{p-1}(X).}
\]
In particular, the zeros depend on the geometric eigenspace dimensions, not merely the rank of \(X\). For every \(n\ge2\), the indicator of \(\mathcal I_n\) has a noninvertible additive convolution operator, since matrices with irreducible characteristic polynomial have no eigenlines over \(\mathbb F_q\).

**Exact two-dimensional Fourier zeros.** For \(n=2\), the zero coefficients are exactly those at matrices with irreducible characteristic polynomial; in characteristic two there is one further class: matrices with two distinct eigenvalues \(\lambda,\mu\in\mathbb F_q\) for which \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(\lambda-\mu)=1\). The precise number of zero Fourier frequencies is
\[
\boxed{Z(q)=\begin{cases}
\dfrac{q^2(q-1)^2}{2},&p\text{ odd},\\[2mm]
\dfrac{q^2(q-1)^2}{2}+\dfrac{q^3(q+1)}4,&p=2.
\end{cases}}
\]
Thus \(Z(q)/q^4\to1/2\) along odd-characteristic fields of increasing size, whereas \(Z(q)/q^4\to3/4\) along characteristic-two fields of increasing size.

**Sharp endpoint Fourier-projection norm.** Let \(P_{\mathcal I_2}\) be the Fourier projection retaining exactly the additive characters indexed by \(\mathcal I_2\). With counting \(\ell^1\) and \(\ell^\infty\) norms on \(G\),
\[
\boxed{\|P_{\mathcal I_2}\|_{\ell^1\to\ell^1}
=\|P_{\mathcal I_2}\|_{\ell^\infty\to\ell^\infty}
=\begin{cases}
(q+1)/2,&p=2,\\
\dfrac{q+1}{p}\csc\!\left(\dfrac\pi{2p}\right),&p\text{ odd}.
\end{cases}}
\]
Both norm identities are sharp equalities, not bounds. Although the field order is \(q\), the normalized factor depends specifically on its prime characteristic \(p\).

## Assumptions and scope

There are no restrictions beyond \(q=p^r\), \(r\ge1\), and \(n\ge1\) for the first formula and criterion. The zero counts and sharp projection norm concern \(n=2\). All matrices and eigenvectors are over \(\mathbb F_q\), not an algebraic closure. The group operation on \(G\) is matrix addition, even though the frequency set consists of multiplicative idempotents. The rank-one restriction is essential.

For the Fourier projection, use
\[
(P_{\mathcal I_2}f)(Y)=q^{-4}\sum_{X\in G}S_2(X)f(Y-X).
\]
Choosing the conjugate sign in the Fourier convention only conjugates coefficients and leaves the zero set and endpoint norms unchanged. A different nontrivial additive character corresponds to a nonzero scalar change of the dual variable, and hence has the same counts and norm.

## Proof

**1. Rank-one factorization and its normalization.** Every rank-one idempotent is \(P=uv^{\mathsf T}\) with \(u\in\mathbb F_q^n\setminus\{0\}\), \(v\in\mathbb F_q^n\), and \(v^{\mathsf T}u=1\): indeed, \(P^2=(v^{\mathsf T}u)P\). Every such \(P\) has exactly \(q-1\) representations, obtained by \((u,v)\mapsto(cu,c^{-1}v)\) for \(c\in\mathbb F_q^\times\). In particular, \(|\mathcal I_n|=(q^n-1)q^{n-1}/(q-1)\).

For fixed nonzero \(u\), sum over the affine hyperplane \(H_u=\{v:v^{\mathsf T}u=1\}\). If \(Xu=\lambda u\), then \(v^{\mathsf T}Xu=\lambda\) for all \(v\in H_u\), and the inner sum equals \(q^{n-1}\psi(\lambda)\). Otherwise the linear form \(v\mapsto v^{\mathsf T}Xu\) is nonconstant on \(H_u\), and additive-character orthogonality makes its sum zero. Therefore
\[
S_n(X)=\frac{q^{n-1}}{q-1}\sum_{\lambda\in\mathbb F_q}(q^{g_\lambda(X)}-1)\psi(\lambda).
\]
Grouping by absolute trace proves the coefficient formula. Since \(1+z+\cdots+z^{p-1}\) is the minimal polynomial of a primitive \(p\)th root of unity over \(\mathbb Q\), a rational linear combination \(\sum_{t=0}^{p-1}a_t\exp(2\pi it/p)\) vanishes if and only if all its coefficients \(a_t\) agree. This proves the zero criterion without any equidistribution assumption.

**2. Four mutually exclusive matrix types in dimension two.** Every \(X\in M_2(\mathbb F_q)\) is of exactly one of the following forms up to similarity:

(a) \(X=\lambda I\) for some \(\lambda\in\mathbb F_q\), with \(q\) matrices in total. Its \(q+1\) eigenlines yield \(S_2(X)=q(q+1)\psi(\lambda)\).

(b) A single nontrivial Jordan block for \(\lambda\in\mathbb F_q\), with \(q(q^2-1)\) matrices in total. Its unique eigenline yields \(S_2(X)=q\psi(\lambda)\).

(c) Two distinct eigenvalues \(\lambda,\mu\in\mathbb F_q\), with \(\binom q2\,q(q+1)\) matrices in total. Its two eigenlines yield \(S_2(X)=q(\psi(\lambda)+\psi(\mu))\).

(d) An irreducible quadratic characteristic polynomial, with \(q^2(q-1)^2/2\) matrices in total, and \(S_2(X)=0\).

For completeness, these multiplicities follow from the \(\operatorname{GL}_2(\mathbb F_q)\) conjugacy-class sizes \(1\), \(q^2-1\), \(q(q+1)\), and \(q(q-1)\) respectively, using centralizers of orders \(|\operatorname{GL}_2|\), \(q(q-1)\), \((q-1)^2\), and \(q^2-1\); the number of monic irreducible quadratics is \((q^2-q)/2\). The displayed counts sum to \(q^4\).

The coefficients in (a) and (b) do not vanish. In (c), \(\psi(\lambda)+\psi(\mu)=0\) requires the ratio of two \(p\)th roots of unity to equal \(-1\); this is possible only when \(p=2\), in which case it holds exactly when \(\operatorname{Tr}(\lambda-\mu)=1\). There are \(q(q/2)/2=q^2/4\) unordered such pairs. Multiplying by the class size \(q(q+1)\) gives \(q^3(q+1)/4\) additional zero matrices. This establishes both zero counts and their two asymptotic zero proportions.

**3. Exact endpoint norm.** On a finite abelian group, convolution by a kernel \(K\) has sharp \(\ell^1\) and \(\ell^\infty\) norms \(\sum_X|K(X)|\): for \(\ell^1\), apply the operator to a point mass; for \(\ell^\infty\), choose phases at one output point to align every summand. The Fourier projector kernel is \(q^{-4}S_2\). Inserting the four similarity types above gives
\[
\begin{aligned}
\|P_{\mathcal I_2}\|
&=\frac{q^2(q+1)+q^2(q^2-1)+q^2(q+1)\displaystyle\sum_{\{\lambda,\mu\},\lambda\ne\mu}|\psi(\lambda)+\psi(\mu)|}{q^4}\\
&=\frac{q+1}{2q}\sum_{\delta\in\mathbb F_q}|1+\psi(\delta)|.
\end{aligned}
\]
For the second equality, translate each unordered distinct pair into its nonzero difference: each nonzero difference occurs \(q\) times in ordered pairs and the unordered sum is half of that.

The absolute trace maps \(\mathbb F_q\) onto \(\mathbb F_p\) with exactly \(q/p\) elements in every fiber. Hence
\[
\|P_{\mathcal I_2}\|=\frac{q+1}{2p}\sum_{t=0}^{p-1}|1+e^{2\pi it/p}|.
\]
For \(p=2\), the last sum is \(2\). For any odd prime \(p\), it is \(2\sum_{t=0}^{p-1}|\cos(\pi t/p)|=2\csc(\pi/(2p))\); the last identity follows from the standard finite cosine sum, split at \((p-1)/2\). This gives the exact sharp formula.

## Verification

The standalone `checker.py` independently enumerates the entire rank-one-idempotent orbit (without using a conjugacy-class table), every ambient frequency matrix, and the trace-exponent histogram of each character sum. It verifies the predicted eigenspace formula modulo the sole cyclotomic relation, tests zeros exactly by histogram balancing, and checks the norm and zero-count formulas. Cases run are \((q,n)=(2,2),(3,2),(4,2),(5,2),(7,2),(2,3)\); the \(q=4\) implementation uses the irreducible polynomial \(z^2+z+1\). The exact check covers \(16+81+256+625+2401+512=3891\) ambient frequencies. Its output ends with `RANK_ONE_IDEMPOTENT_ORBIT_FOURIER_EXACT_CHECKS_PASS`.

These computations are corroboration, not proof for untested field sizes or dimensions. The unrestricted assertions are established by the algebraic steps above.

## Relationship to prior work

De Seguins Pazzis (2009) studies representations of matrices as sums of idempotents, including their rank and trace algebra, but not additive Fourier coefficient zeros or endpoint projection norms. Li and Hu (2011) evaluate additive character sums over the multiplicative groups \(\operatorname{GL}_n\) and \(\operatorname{SL}_n\), where left-right group invariance reduces the dual parameter to its rank; the rank-one-idempotent conjugacy orbit has a different invariance and its coefficients depend on the eigenline data. A published result on coordinate-Fourier restriction to the *entire rank-one matrix shell* gives a Gram spectrum but does not apply the idempotence condition \(v^{\mathsf T}u=1\) or evaluate this orbital Fourier projection. These distinctions concern the mathematical implications of the results, not just their terminology. The general matrix character-orthogonality identities used here are classical and not claimed as new.

## Limitations

The exact operator norm and zero multiplicity are fully evaluated for \(2\times2\) matrices; for higher dimensions the theorem gives an explicit necessary-and-sufficient criterion, not a closed formula for the total number of balanced-eigenline matrices or for the endpoint norm. This theorem does not claim a classification of sums of rank-one idempotents, which is a separate additive combinatorics problem. Exhaustive historical priority and independent mathematical review have not been established. The finite code does not constitute certification of infinite assertions.

## References

1. C. de Seguins Pazzis, *On sums of idempotent matrices over a field of positive characteristic*, arXiv:0907.5360, first publicly submitted 2009-07-30, https://arxiv.org/abs/0907.5360.
2. Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513, first publicly submitted 2011-05-23, https://arxiv.org/html/1105.4513v1.
3. *Complete first-coordinate Fourier spectrum on finite-field rank-one matrices*, publicly posted research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-complete-first-coordinate-fourier-spectrum-on-finite-field-rank--3ad73e3126a7/RESULT.md. (Only its published mathematical statements are used in the comparison.)
