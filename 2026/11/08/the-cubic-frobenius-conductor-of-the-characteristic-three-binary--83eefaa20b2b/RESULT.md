# The cubic Frobenius conductor of the characteristic-three binary-cubic discriminant

## Finding

Let \(k\) be any field of characteristic \(3\), and write a binary cubic as
\[
f=aX^3+bX^2Y+cXY^2+dY^3.
\]
Its discriminant hypersurface \(D\subset\mathbb P^3_k\) has equation
\[
\Delta=b^2c^2-ac^3-b^3d=0.
\]
Let \(L=V(b,c)\). There are three simultaneous structural conclusions:

1. The complete scheme-theoretic Jacobian singular scheme is \(V((b,c)^3)\), the third infinitesimal neighborhood of \(L\). It has degree \(6\) and Hilbert polynomial \(6n-2\).
2. The normalization \(\nu:\mathbb P^1\times\mathbb P^1\rightarrow D\) given by the factorization \(f=(sX+tY)^2(uX+vY)\) is a finite universal homeomorphism. Over \(L\) its restriction to the diagonal is cubic Frobenius, of purely inseparable degree \(3\). Its *exact conductor ideal in the nonnormal surface* is \(\mathfrak c=\mathcal I_L^2\), and its extension to the normalization is the square of the diagonal ideal.
3. For every \(q=3^m\), the point count and Hasse–Weil zeta function are
\[
\#D(\mathbb F_q)=(q+1)^2,
\quad Z(D/\mathbb F_q,T)=\frac1{(1-T)(1-qT)^2(1-q^2T)}.
\]
Despite the universal-homeomorphism relationship with \(\mathbb P^1\times\mathbb P^1\), the quartic surface has \(H^2(D,\mathcal O_D)\cong k\) whereas the normalization has vanishing second coherent structure-sheaf cohomology.

## Assumptions and scope

All scheme equalities and the normalization/conductor statement hold over **any** characteristic-three field \(k\), without algebraic-closure or perfection hypotheses. The line \(L\) is defined scheme-theoretically by the homogeneous ideal \((b,c)\). The notation \(V((b,c)^3)\) denotes the subscheme of \(\mathbb P^3\) with its indicated homogeneous ideal, not its reduced support. The zeta formula requires a finite field \(\mathbb F_q\) with \(q\) a power of \(3\). Cohomology statements refer to the coherent structure sheaf over \(k\).

## Proof

**1. The actual Jacobian scheme.** The universal integral discriminant of \(aX^3+bX^2Y+cXY^2+dY^3\) is
\[
b^2c^2-4ac^3-4b^3d+18abcd-27a^2d^2.
\]
Reduction modulo \(3\) gives the displayed \(\Delta\). Its derivatives in the order \((a,b,c,d)\) are
\[
(-c^3,-bc^2,-b^2c,-b^3).
\]
Thus the Jacobian ideal is *exactly* \((b,c)^3\). Since \(\Delta\in(b,c)^3\), imposing the defining equation adds no condition. The associated graded sheaf of the third thickening of a line has pieces \(\mathcal O_L\), \(\mathcal O_L(-1)^{\oplus 2}\), and \(\mathcal O_L(-2)^{\oplus3}\). Therefore its Hilbert polynomial is
\[
(n+1)+2n+3(n-1)=6n-2.
\]
This also proves its degree is \(6\).

**2. An explicit finite normalization.** Multiplying two linear forms with one repeated gives the morphism
\[
\nu([s:t],[u:v])=[s^2u:s^2v-stu:t^2u-stv:t^2v].
\]
Set \(\lambda=sv-tu\). Then \(b=s\lambda\), \(c=-t\lambda\). Thus \(\nu^{-1}(L)\) is the diagonal Cartier divisor \(\lambda=0\), and on that diagonal
\[
\nu([s:t],[s:t])=[s^3:0:0:t^3].
\]
If \(b\) or \(c\) is nonzero, the unique repeated factor is recovered as \([s:t]=[b:-c]\), and the remaining factor is unique. If \(b=c=0\), after any algebraic closure a binary cubic is a cube of a linear form, so every geometric point of \(D\) is hit. This proves the morphism is surjective and geometrically injective. All its geometric fibers are finite; properness then implies it is finite. The inverse on \(D\setminus L\) proves birationality; the source is smooth and normal, so the finite birational morphism identifies it with the normalization. Geometric injectivity and surjectivity together show that it is radicial and a universal homeomorphism. On the diagonal it is the cubic Frobenius map, generically purely inseparable of degree \(3\). These facts do not assert that the normalization map itself is generically of degree three: its generic degree is one.

**3. Exact conductor calculation.** We compute where \(a=1\), which covers one endpoint chart of \(L\). On the normalization this implies \(s=u=1\). Write \(t=t\) and \(v=t+b\). Then
\[
c=-bt,\qquad d=t^3+bt^2.
\]
Put \(A=k[b,d]\), \(S=k[b,t]\), and \(R=k[b,c,d]/(b^2c^2-c^3-b^3d)\). The relation \(t^3+bt^2=d\) makes \(S\) free of rank three over \(A\), with basis \(1,t,t^2\). The cubic equation for \(c\) is monic up to sign, so
\[
R=A\oplus A(bt)\oplus A(b^2t^2)\subset S=A\oplus At\oplus At^2.
\]
To compute the conductor \(\{r\in R:rS\subset R\}\), write \(r=\alpha+\beta bt+\gamma b^2t^2\) with \(\alpha,\beta,\gamma\in A\). Membership of \(rt\) in \(R\) forces \(\alpha\in bA\), \(\beta\in bA\); membership of \(rt^2\) additionally forces \(\alpha\in b^2A\). Conversely these conditions give \(r\in b^2S\), and \(b^2S\subset R\) is visibly an ideal of \(S\). Hence
\[
\mathfrak c|_{a\ne0}=b^2S=(b^2,bc,c^2)\subset R.
\]
The symmetric chart \(d=1\) follows by reversing the binary cubic variables, interchanging \(a,d\) and \(b,c\). These two charts cover \(L\), and away from \(L\) the normalization is an isomorphism. Thus globally \(\mathfrak c=\mathcal I_L^2\). Pulling back \(\mathcal I_L=(b,c)\) yields the diagonal ideal \((\lambda)\), so the extended conductor is \(\mathcal I_{\mathrm{diag}}^2\).

**4. Arithmetic and coherent cohomology.** Because finite fields are perfect, cubic Frobenius on each \(\mathbb F_q\)-rational line point is a bijection, and off \(L\) the normalization is an isomorphism. It follows that the normalization induces a bijection of \(\mathbb F_{q^r}\)-points for every positive integer \(r\), giving \((q^r+1)^2\) points and the stated zeta function. The exact sequence
\[
0\to\mathcal O_{\mathbb P^3}(-4)\to\mathcal O_{\mathbb P^3}\to\mathcal O_D\to0
\]
gives \(H^2(D,\mathcal O_D)\cong H^3(\mathbb P^3,\mathcal O(-4))\cong k\). Meanwhile \(H^2(\mathbb P^1\times\mathbb P^1,\mathcal O)=0\) by Künneth. The quartic is Gorenstein with \(\omega_D\cong\mathcal O_D\), even though it is nonnormal.

## Verification

Run `python3 verify.py` with the included standalone Python 3 source. The program checks the discriminant's symbolic partial derivatives modulo \(3\), the parametrization and diagonal identities, the affine conductor relations, and exhaustive projective point equality over \(\mathbb F_3\) and \(\mathbb F_9\). The captured exact output is `verification_output.txt` and terminates with `ALL_CHECKS_PASSED`. The finite-field tests are independent sanity checks; the all-fields and infinite-scheme assertions follow from the proof above, not from finite enumeration. The conductor lattice argument, proper quasi-finite criterion, and projective chart cover are mathematical proof steps rather than external computational claims.

## Relationship to prior work

Chipalkatti, *On equations defining coincident root loci* (2001), studies normalization defects of coincident-root loci and is the closest structural antecedent; its arguments and statements are formulated over characteristic zero. D'Andrea and Chipalkatti, *On the Jacobian ideal of the binary discriminant* (2006), determine characteristic-zero Jacobian geometry and explicitly analyze the degree-six thickening of the twisted cubic for binary cubics; their positive-characteristic specialization cannot simply be assumed. Kurmann, *Some remarks on equations defining coincident root loci* (2011), gives local fiber-product generators and normalization singularity criteria, again assuming algebraically closed characteristic-zero fields. Shakirov's higher-discriminant paper supplies further classical discriminant background. The present assertion is not that the repeated-root parametrization or the integral cubic discriminant is new. The characteristic-three identification of the *cube of the line ideal*, the exact *square conductor*, and the Frobenius normalization comparison is the specifically assessed combination. Literature searches did not locate an equivalent statement; absence from searched material is not a proof of priority.

## Limitations

No claim is made in other characteristics, for binary forms of higher degree, or about classification of all characteristic-three nonnormal discriminants. Geometric injectivity alone does not imply scheme isomorphism, which is why conductor and normalization are computed separately. The arithmetic formula does not imply equality of coherent cohomology. The published historical coverage may be broader than the accessible texts and database summaries; independent assessment of originality remains unperformed.

## References

1. J. Chipalkatti, *On equations defining coincident root loci*, 2001-10-19, arXiv:math/0110224v1, https://arxiv.org/abs/math/0110224 (sections on normalization defects and conductor, characteristic-zero base).
2. C. D'Andrea and J. Chipalkatti, *On the Jacobian ideal of the binary discriminant*, 2006-01-29, arXiv:math/0601705v1, https://arxiv.org/abs/math/0601705 (binary cubics, §4.1, explicit characteristic-zero scope).
3. B. Shakirov, *Higher discriminants of binary forms*, arXiv:math/0609524, https://arxiv.org/abs/math/0609524 (classical discriminant background).
4. S. Kurmann, *Some remarks on equations defining coincident root loci*, 2011-08-23, arXiv:1108.4532v1, https://arxiv.org/abs/1108.4532 (normalization fiber products and local generators over characteristic zero).
