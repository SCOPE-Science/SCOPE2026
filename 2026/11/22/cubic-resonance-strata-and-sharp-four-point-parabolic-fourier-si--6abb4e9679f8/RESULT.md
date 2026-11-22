# Cubic-resonance strata and sharp four-point parabolic Fourier sixth moments

## Finding
Let \(F=\mathbb F_q\) be a finite field of characteristic \(p\ge7\), and let \(T\subset F\) consist of four distinct elements. Write \(P_t=(t,t^2)\). For \(c=(c_t)_{t\in T}\in\mathbb C^T\), define
\[
\widehat f(u,v)=q^{-1}\sum_{t\in T}c_t\psi(-ut-vt^2),\qquad (u,v)\in F^2,
\]
where \(\psi\) is any nontrivial additive character and the transform is unitary on \(\ell^2(F^2)\). Define the sixth-power synthesis quotient
\[
\mathcal K_6(T)^6=\sup_{c\ne0}\frac{q^4\sum_{(u,v)\in F^2}|\widehat f(u,v)|^6}{(\sum_{t\in T}|c_t|^2)^3}.
\]
The twenty unordered triple sums of the four parabolic points have either zero or exactly one nontrivial collision, and the possible collisions have two disjoint geometric forms:

**Unbalanced cubic centroid stratum:** \(3P_a=P_b+P_c+P_d\), where \(T=\{a,b,c,d\}\). Such a stratum exists exactly when \(3\mid(q-1)\), and its sets are precisely
\[
T=\{a,a+u,a+u\omega,a+u\omega^2\},\qquad a\in F,\ u\in F^\times,
\]
where \(\omega\) is a fixed primitive cube root of unity. There are exactly \(q(q-1)/3\) distinct sets. On **each** one,
\[
\boxed{\mathcal K_6(T)^6=\frac{r_*^6+27r_*^4+12r_*^3+135r_*^2+93}{(r_*^2+3)^3}=4.203233399468414\ldots},
\]
where \(r_*=1.112646984532186\ldots\) is the unique positive root of
\[
r^4+r^3+6r^2-3r-7=0.
\]
All nonzero extremizers have the unique center-to-arm modulus ratio \(|c_a|:|c_b|:|c_c|:|c_d|=r_*:1:1:1\) and the single phase relation \(3\arg c_a-\arg c_b-\arg c_c-\arg c_d\equiv0\pmod{2\pi}\). These conditions are sufficient.

**Balanced stratum:** \(2P_a+P_b=2P_c+P_d\), with four distinct points. These sets are exactly the affine copies \(a+u\{0,1,3,4\}\), and there are precisely \(q(q-1)/2\). Their sharp sixth-moment constant for the corresponding isolated balanced relation is already known [3] and is not asserted as a new formula here.

Every remaining four-point subset has distinct unordered triple sums and has \(\mathcal K_6(T)^6=4\), with equality exactly when all four coefficient magnitudes are equal, with arbitrary phases. The number of these collision-free sets is
\[
\binom q4-\frac{q(q-1)}2-\mathbf1_{3\mid(q-1)}\frac{q(q-1)}3.
\]
Thus four-site parabolic supports have a complete cubic-collision incidence classification and an explicitly sharp **new unbalanced** sixth-moment threshold.

## Assumptions and scope
All arithmetic defining \(P_t\) and the collision geometry occurs inside \(F\). The coefficient field is \(\mathbb C\). The assertion holds for every odd prime power of characteristic at least seven, including extension fields, and does not require that the additive character be primitive over the prime field beyond nontriviality. There are no constraints on coefficient phases except at equality. The Fourier \(\ell^6\) norm is with counting measure on all \(q^2\) frequencies, while the coefficient \(\ell^2\) norm is also counting measure. The factor \(q^4\) makes the quotient independent of the Fourier normalization. An unordered triple sum is a size-three multiset, allowing repeated sites.

## Proof
**1. At most one collision and its multiplicity pattern.** Any three distinct points \(P_t\) are affinely independent: the determinant of their columns \((1,t,t^2)\) is the nonzero Vandermonde product. If two distinct size-three multisets have equal parabolic sums, their multiplicity difference is a nonzero vector \(d=(d_i)_{i=0}^3\in\mathbb Z^4\), with \(\sum d_i=\sum d_i t_i=\sum d_i t_i^2=0\) in \(F\). Since any three columns are independent, all four coordinates of \(d\) are nonzero. If the two multisets share an element then cancellation would give a nontrivial equality of two unordered pair sums. This is impossible on a parabola in odd characteristic: the equal first and second power sums determine both the sum and product of the two parameters, hence their unordered pair. Therefore the multisets are disjoint. As each has mass three and every one of the four sites occurs, their multiplicity difference is, up to permutation and sign, either \((3,-1,-1,-1)\) or \((2,1,-2,-1)\). The kernel of the three-by-four evaluation matrix is one-dimensional over \(F\). For \(p\ge7\), no two distinct vectors of these two types, apart from negatives, are scalar multiples: the first has a repeated triple entry, while the second has four distinct entries; in the second type the only scalar preserving the multiset \(\{1,2,-1,-2\}\) is \(\pm1\). Therefore two different nontrivial collisions are impossible.

**2. Geometric classification.** For an unbalanced collision translate \(a\) to zero. The three nonzero offsets \(x,y,z\) satisfy \(x+y+z=x^2+y^2+z^2=0\). Since \(p\ne2\), also \(xy+yz+zx=0\), so \(x,y,z\) are the roots of \(X^3-xyz\). They are distinct and nonzero, forcing a nontrivial cubic root of unity \(\omega\) and \(\{x,y,z\}=\{u,u\omega,u\omega^2\}\). Conversely these offsets obey both moment conditions. The center is intrinsic, and the three choices of \(u\) within one orbit give the same set, hence the count \(q(q-1)/3\).

For the balanced collision translate \(c\) to zero and put \(a=x\ne0\). The first moment gives \(d=2x+b\), and the second gives \(2x^2+b^2=(2x+b)^2\). Therefore \(b=-x/2\) and \(d=3x/2\); up to an affine map, the set is \(\{0,1,3,4\}\). The two affine self-maps of this set are the identity and reflection \(t\mapsto4-t\): uniqueness of the signed relation requires any stabilizer to preserve or reverse the four distinct coefficient roles \(\{2,1,-2,-1\}\). Thus the orbit has \(q(q-1)/2\) members. The two strata cannot coincide by Step 1. Subtracting from \(\binom q4\) gives the generic count.

**3. Exact sixth moment.** Write \(s=\sum|c_i|^2\), \(e_2=\sum_{i<j}|c_i|^2|c_j|^2\), and \(e_3=\sum_{i<j<k}|c_i|^2|c_j|^2|c_k|^2\). Character orthogonality identifies \(q^4\sum|\widehat f|^6\) with the squared \(\ell^2\) norm of the triple convolution of \(f\). When all twenty size-three multiset sums are distinct, counting multinomial multiplicities gives the exact baseline \(H=s^3+6se_2+12e_3\). The single unbalanced collision pairs a pure cube coefficient (multinomial weight one) with a three-distinct coefficient (weight six), contributing
\[
q^4\sum|\widehat f|^6=H+12\operatorname{Re}(c_a^3\overline{c_bc_cc_d}).
\]
In the balanced case the sole additional contribution is \(18\operatorname{Re}(c_a^2c_b\overline{c_c^2c_d})\). These identities hold for every \(c\) and do not rely on finite enumeration.

**4. Sharp unbalanced optimization and rigidity.** For a fixed center squared modulus \(x=|c_a|^2\) and fixed total outer squared mass \(y=\sum_{i\ne a}|c_i|^2\), the quadratic elementary symmetric function of the three outer squared moduli is at most \(y^2/3\), and their product is at most \((y/3)^3\), with simultaneous equality precisely for equal outer magnitudes. Every coefficient multiplying these quantities in \(H\), and the magnitude bound on the resonant cross term, is nonnegative. Therefore all maxima have equal outer moduli; the resonant real part must be positive and maximal. Put each outer modulus equal to one and the center modulus equal to \(r\ge0\). The normalized sixth power is
\[
\Phi(r)=\frac{r^6+27r^4+12r^3+135r^2+93}{(r^2+3)^3}.
\]
A direct differentiation gives
\[
\Phi'(r)=-\frac{36r(r^4+r^3+6r^2-3r-7)}{(r^2+3)^4}.
\]
The quartic has exactly one positive zero: its coefficient sign sequence has one change, and its values at zero and infinity have opposite signs. Thus \(\Phi\) increases before \(r_*\) and decreases thereafter, including the boundary \(r=0\), so \(r_*\) is the unique global maximizing ratio. The strict equality conditions in the symmetric-polynomial inequalities and the real-part bound give all stated complex extremizers.

**5. Collision-free optimum.** With \(s\) fixed, \(e_2\le3s^2/8\) and \(e_3\le s^3/16\) by the equal-variable inequalities, with equality simultaneously precisely when the four squared magnitudes are equal. Hence \(H/s^3\le1+6(3/8)+12(1/16)=4\).

## Verification
Run `python3 checker.py` with a standard Python interpreter. The checker enumerates all four-parameter sets over prime fields of orders \(7,11,13,17\), verifies the collision classification and exact counts, checks weighted threefold convolution against both the symbolic moment formula and the full finite Fourier sum for 28 cases, isolates the positive quartic root by bisection, and performs supplementary bound checks. All checks passed. These finite computations are diagnostics, not substitutes for the all-prime-power algebraic proof above.

## Relationship to prior work
Iosevich–Li–Yu [1] motivate exact spectral synthesis constants on finite groups and give a general even-moment convolution framework; their inspected paraboloid and affine-transitive results do not classify sharp four-point parabolic support by isolated triple-sum resonance. González-Riquelme–Oliveira e Silva [2] address sharp extension for the complete finite parabola rather than the four-site restricted problem. The closely related published result [3] determines the **balanced** four-character cubic defect constant under the isolated \(2+1=1+2\) relation; its full theorem explicitly excludes the unbalanced \(3=1+1+1\) defect. Its balanced constant is deliberately treated here as prior work, not a new result. Other indexed results on three-site parabolic sixth moments [4] and four-site parabolic Fourier zero sets [5] address different objects or norms.

## Limitations
The characteristic bound \(p\ge7\) is essential to the collision-pattern uniqueness argument as written; characteristics two, three, and five are not classified here. An older equivalent theorem on isolated unbalanced \(\Lambda(6)\) sets could subsume the sharp constant, and a finite-field additive-combinatorics classification under different terminology could subsume some geometry; neither possibility can be excluded solely from a finite search. This is a self-review, not independent validation. No claim is made about optimizing over all support cardinalities or about physical inverse Fourier recovery.

## References
[1] A. Iosevich, Z. Li and K. Yu, *Spectral synthesis with the complexity parameter in Z_N^d*, arXiv:2609.25404, first public 2026-09-21, https://arxiv.org/pdf/2609.25404.

[2] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first public 2024-05-26, https://arxiv.org/pdf/2405.16647.

[3] *Sharp sixth-moment norm for one balanced triple-sum defect*, published full result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-sixth-moment-norm-for-one-balanced-triple-sum-defect--927de11a37e9/RESULT.md.

[4] *Sharp sixth Fourier moments for three parabolic modes in every odd characteristic*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-fourier-moments-for-three-parabolic-modes-in-every-o--52302cf3414e.

[5] *Flat four-point finite parabola Fourier zeros: a prime-field symmetry*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-flat-four-point-finite-parabola-fourier-zeros-a-prime-field-symm--c2e3015b14a6.
