# Characteristic-two resonance in idempotent derivations of unipotent almost-abelian Lie algebras

## Finding

Let \(k\) be a field, \(N\ge 2\), \(R=k[x]/(x^N)\), and \(T:R\to R\) be multiplication by \(1+x\). Form the \((N+1)\)-dimensional almost-abelian Lie algebra
\[
L_N=kt\ltimes_T R,\qquad [t,v]=Tv,\quad [R,R]=0.
\]
A derivation is an ordinary \(k\)-linear Lie derivation, and *idempotent* means \(D^2=D\) as a linear operator, not a restricted-Lie identity.

**Classification.** All idempotent derivations fall into the following disjoint families:

1. The zero derivation.
2. For every \(u\in R\), the derivation \(D_u(t)=u\), \(D_u(v)=v\) for \(v\in R\). Each has rank \(N\).
3. Only if \(\operatorname{char}k=2\) and \(N=2m\), the derivations
   \[
   D_{c,u}(t)=t+u,\qquad D_{c,u}(v)=B_c(v),\qquad
   B_c=(1+x)\frac{d}{dx}+M_c,
   \]
   where \(M_c\) denotes multiplication by \(c\in R\), with the necessary and sufficient constraints
   \[
   c^2+c+(1+x)c'=0\text{ in }R,\qquad B_c(u)=0.
   \]
   Each has rank \(m+1\). These operators have \(m\)-dimensional kernel, and their image satisfies the striking bracket identity
   \[
   [\operatorname{im}D_{c,u},\operatorname{im}D_{c,u}]
   =\ker D_{c,u}.
   \]
   Here brackets of subspaces mean their linear span; the displayed equality shows that the image need not be a Lie subalgebra.

For every finite field \(k=\mathbb F_q\), the **complete labeled rank polynomial** is
\[
\boxed{\mathcal P_{N,q}(Z)=1+q^N Z^N+
\begin{cases}q^N Z^{N/2+1},&\operatorname{char}k=2\text{ and }2\mid N,\\ 0,&\text{otherwise.}\end{cases}}
\]
In particular, the number of idempotent derivations is \(1+q^N\) outside even characteristic-two module dimensions, and \(1+2q^N\) in the exceptional case. If \(N=2\), the two nonzero families have the same rank and their polynomial coefficients add. All formulas count distinct labeled operators, not conjugacy classes.

Moreover, when \(N=2m\) and \(\operatorname{char}k=2\), the parameter locus \(\{c\in R:c^2+c+(1+x)c'=0\}\) is algebraically isomorphic to affine \(m\)-space over \(k\); consequently it has exactly \(q^m\) rational points. The condition on \(u\) gives exactly \(q^m\) choices per \(c\), without assuming algebraic closure.

## Assumptions and scope

The description of operators and the rank and bracket assertions hold for arbitrary fields, with the indicated characteristic and parity conditions. The numerical formulas and rank polynomial require \(k=\mathbb F_q\). The family uses one invertible unipotent Jordan block; it does not assert a classification for arbitrary almost-abelian Lie algebras or arbitrary action matrices. No claim is made about independent publication priority or automorphism-conjugacy classes.

## Proof

**1. Derivation reduction.** The operator \(T=I+M_x\) is invertible in \(R\), so \([L_N,L_N]=R\). Every derivation preserves the derived ideal. Write it uniquely as
\[
D(t)=at+u,\qquad D|_R=B,
\]
with \(a\in k\), \(u\in R\), \(B\in\operatorname{End}_k(R)\). Applying the derivation identity to \([t,v]=Tv\), while \([R,R]=0\), yields the complete and sufficient system
\[
[B,T]=aT.
\]
The extra identity \(D^2=D\) is equivalent to
\[
a^2=a,\qquad B^2=B,\qquad B(u)=(1-a)u.
\]
Thus \(a=0\) or \(a=1\) over every field.

**2. The \(a=0\) branch.** Since \(T=I+M_x\) is a single cyclic Jordan block, its full commutant is \(k[T]=\{M_c:c\in R\}\). A multiplication operator is idempotent exactly when \(c^2=c\). The local ring \(R\) has only the idempotents \(c=0,1\): modulo its maximal ideal the residue is \(0\) or \(1\), and a nilpotent idempotent (or its complement) must be zero. For \(B=0\), the condition \(B(u)=u\) forces \(u=0\); for \(B=I\), \(u\) is arbitrary. This gives exactly the first two families.

**3. Excluding the \(a=1\) branch outside characteristic two and in odd dimension.** Suppose \(B^2=B\) and \(BT-TB=T\). Decompose \(R=E_0\oplus E_1\) into the zero- and one-eigenspaces of \(B\). For \(v\in E_1\), the commutator equation gives \(B(Tv)=2Tv\). Outside characteristic two, the only eigenvalues of an idempotent are \(0,1\), so \(Tv=0\). Invertibility of \(T\) implies \(E_1=0\), hence \(B=0\), a contradiction. In characteristic two the same equation says that \(T\) exchanges \(E_0\) and \(E_1\): it maps each one isomorphically onto the other. Consequently \(\dim R\) must be even. This also proves \(\dim E_0=\dim E_1=m\) in the exceptional branch.

**4. All exceptional operators.** Suppose \(\operatorname{char}k=2\) and \(N=2m\). The derivation \(B_0=(1+x)d/dx\) is well defined on \(R\) since \((x^{2m})'=0\), and satisfies \([B_0,T]=T\). Also \(B_0^2=B_0\): in the coordinate \(y=1+x\), it is \(y\,d/dy\), acting by the parity of the exponent on a spanning set. Every solution of \([B,T]=T\) is therefore uniquely \(B=B_0+M_c\). Expanding the square in characteristic two gives
\[
B^2=B_0+M_{B_0(c)+c^2};
\]
hence \(B^2=B\) if and only if \(c^2+c+(1+x)c'=0\). The remaining condition on \(u\) is precisely \(B(u)=0\). By Step 3, \(\operatorname{rank}B=m\), so each \(c\) permits a \(m\)-dimensional choice of \(u\), and \(\operatorname{rank}D=m+1\). Since \(D(t)=t+u\) and \(D|_R=B\), its kernel is \(E_0\) and its image is \(k(t+u)\oplus E_1\). Moreover \(T(E_1)=E_0\), so the brackets of image elements span precisely \(E_0=\ker D\).

**5. Exact polynomial parameter count.** Set \(y=1+x\) and \(z=x^2=y^2+1\). Let \(S=k[z]/(z^m)\). As an \(S\)-module, \(R=S\oplus yS\); write uniquely \(c=A(z)+yC(z)\) with \(A,C\in S\). Since \(B_0\) vanishes on \(S\) and sends \(yC\) to \(yC\), the Riccati equation becomes
\[
A^2+A+(1+z)C^2=0\quad\text{in }S.
\]
Write \(A=\sum_{j=0}^{m-1}a_jz^j\), \(C=\sum_{j=0}^{m-1}b_jz^j\). Its constant coefficient is \(a_0^2+a_0+b_0^2=0\). With \(\theta=a_0+b_0\), this is equivalent to \(a_0=\theta^2\), \(b_0=\theta+\theta^2\). Successive coefficient equations uniquely prescribe
\[
a_{2i+1}=b_i^2\quad(2i+1<m),\qquad
a_{2i}=a_i^2+b_i^2\quad(0<2i<m).
\]
Thus the genuinely free parameters are \(\theta,b_1,\ldots,b_{m-1}\). These equations give mutually inverse polynomial coordinate maps between the solution locus and \(\mathbb A^m_k\), not merely a finite-field bijection. Over \(\mathbb F_q\), there are exactly \(q^m\) choices of \(c\), and Step 4 supplies exactly \(q^m\) vectors \(u\) per \(c\). This proves the full polynomial and all rank and bracket assertions. \(\square\)

## Verification

The included standalone program `verify_unipotent_toral.py` evaluates the original Lie bracket, derivation identity, and composition-idempotence on basis vectors; its matrices are constructed independently from their acting formulas. It exhaustively enumerates every raw linear map for \((q,N)=(2,2),(3,2),(2,3)\), finding respectively the rank multiplicities \((1,8)\), \((1,9)\), and \((1,8)\) at ranks \(0,N\). It also enumerates all permitted exceptional coefficients and compatible vectors for \((q,N)=(2,2),(2,4),(2,6),(4,2),(4,4)\) and the nonexceptional scalar branch for \((3,2),(3,4),(5,2)\). All match the theorem. These finite checks corroborate but do not replace Steps 1–5, which establish the assertions for all dimensions and fields stated.

## Relationship to prior work

Burde and Moens (2020; later published 2022) investigate Lie derivations satisfying polynomial identities, especially structural nilpotency implications. Their Theorem 3.10 and Remark 3.11 treat such identities in general but do not enumerate the idempotent derivations, ranks or characteristic-two Riccati fibers for the present unipotent family. Avetisyan (initial arXiv publication 2016, revised 2023) gives the general derivation block equations for almost-abelian Lie algebras in Proposition 13; Step 1 is the special case of that established foundation, and is not claimed as original. The new contribution is the complete nonlinear idempotent classification, sharp characteristic-and-parity switch, exact all-dimensional finite-field rank polynomial, affine exceptional parameterization, and bracket-span statement. Relevant published derivation censuses for free two-step Lie and filiform Leibniz algebras and idempotent Nijenhuis operators on almost-abelian Lie algebras concern different operator equations or algebra families and do not imply these formulas by specialization.

## Limitations

The theorem concerns a single invertible unipotent Jordan block and composition-idempotent **ordinary** derivations. It does not assert a formula for all rational canonical forms, higher polynomial identities, or orbit counts. The source comparison establishes originality relative to inspected published work only; it is not a proof of global priority. Some earlier records and all possible unpublished work are outside the checked evidence. Numerical tests cannot certify unbounded cases independently of the proof.

## References

1. D. Burde and W. A. Moens, *The structure of Lie algebras with a derivation satisfying a polynomial identity*, arXiv:2009.05434, first submitted 2020-09-11; see Theorem 3.10, Remark 3.11. https://arxiv.org/abs/2009.05434
2. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365, first submitted 2016-10-17, Proposition 13. https://arxiv.org/abs/1610.05365
3. D. Burde, K. Dekimpe, and B. Verbeke, *Almost inner derivations of Lie algebras II*, arXiv:1905.08145, first submitted 2019-05-20; background on almost-abelian derivations. https://arxiv.org/abs/1905.08145
