# Cartier-rank rigidity in prime-linked dihedral hyperelliptic pencils

## Finding
For every prime \(p\ge11\), put \(g=(p-1)/2\) and \(k=\overline{\mathbb F}_p\). On the smooth family
\[
C_a:\quad y^2=x^{p+1}+a x^{(p+1)/2}+1,\qquad a\in k,\quad a^2\ne4,
\]
define the coefficient polynomials
\[
b_j(A)=[T^j](T^2+AT+1)^g\in\mathbb F_p[A],\qquad0\le j\le2g.
\]
Its entire geometric \(p\)-rank and Cartier \(a\)-number stratification is determined by the finite list of coefficient polynomials:
\[
 f_p(C_a)=\sum_{i=1}^g\mathbf1_{b_{2i-1}(a)\ne0},\qquad
 a(C_a)=g-f_p(C_a).
\]
In particular \(a=0\) is the **unique** smooth coefficient parameter of \(p\)-rank zero, its Jacobian is superspecial, and every other smooth parameter has \(p\)-rank at least two. The generic member is ordinary. When \(p\equiv1\pmod4\), every member has even \(p\)-rank. The statements concern marked coefficient parameters and do not count geometric isomorphism classes.

## Assumptions and scope
The base field is algebraically closed of prime characteristic \(p\ge11\); no assertion for characteristic two or all primes at a fixed genus is intended. The polynomial on the right has degree \(p+1=2g+2\). Its derivative is
\[
 g+1\,\cdot x^g(2x^{g+1}+a).
\]
Because \(p\nmid g+1\), a multiple finite root exists precisely when \(a^2=4\). Hence the indicated parameter locus comprises smooth hyperelliptic curves of genus \(g\).

The \(p\)-rank \(f_p(C_a)\) means the dimension of \(\operatorname{Jac}(C_a)[p](k)\) over \(\mathbb F_p\); the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_p,\operatorname{Jac}(C_a)[p])\). The latter is the dimension of the Cartier kernel on global regular differentials.

## Proof
**Coefficient support.** Put \(n=g+1=(p+1)/2\) and write
\[
 F_a(x)^g=(x^{2n}+a x^n+1)^g=(T^2+aT+1)^g\big|_{T=x^n}
             =\sum_{j=0}^{2g}b_j(a)x^{nj}.
\]
For the standard differential basis \(x^{i-1}dx/y\), the Cartier/Hasse–Witt coefficient array (up to coefficientwise \(p\)-th roots and, depending on convention, transposition) is
\[
 M_{ij}= [x^{pi-j}]F_a(x)^g,\qquad 1\le i,j\le g.
\]
As \(p=2n-1\), the congruence \(pi-j\equiv0\pmod n\) is equivalent to \(j=n-i\). Thus all off-antidiagonal entries are zero, while
\[
 M_{i,n-i}=b_{2i-1}(a).
\]

**Frobenius stability.** The polynomial \((T^2+aT+1)^g\) is reciprocal, so \(b_j=b_{2g-j}\). In particular the two entries corresponding to the transposition \(i\mapsto n-i\) are equal. In the semilinear Frobenius iteration \(M\,M^{(p)}\), the resulting matrix is diagonal, and its \(i\)-th diagonal entry is \(b_{2i-1}(a)b_{2i-1}(a)^p\). The indices of nonzero entries therefore remain exactly the same under every further Frobenius iterate. (For the Cartier-semilinear convention, take coefficientwise \(p\)-th roots; nonvanishing and stable dimensions are unchanged.) Hence the stable Frobenius rank equals \(\#\{i:b_{2i-1}(a)\ne0\}\); this is the geometric \(p\)-rank. The ordinary rank of the Cartier matrix is the same number, so its nullity, the Cartier \(a\)-number, is \(g-f_p(C_a)\).

**Extreme and generic strata.** At \(a=0\), the polynomial \((T^2+1)^g\) has no odd-degree coefficients: \(M=0\). This means \(a(C_0)=g\), which is the superspecial Jacobian criterion. Conversely
\[
 b_1(a)=ga\ne0\quad\text{for }a\ne0,
 \qquad b_{2g-1}(a)=ga,
\]
and the associated two distinct antidiagonal positions show \(f_p(C_a)\ge2\). Thus no \(p\)-rank-one fiber occurs and the zero-rank parameter is unique. To prove generic ordinarity, for each odd \(j\le g\), the coefficient of the highest power \(A^j\) in \(b_j(A)\) is \(\binom gj\), nonzero modulo \(p\) since \(g<p\). Every odd \(j>g\) is handled by reciprocity. Hence none of the finitely many \(b_{2i-1}\) is the zero polynomial, and their common nonvanishing defines a nonempty Zariski open subset of the parameter line (also avoiding \(a^2=4\)). Finally the index involution has no fixed point when \(g\) is even; each nonzero coefficient then contributes in pairs, proving even \(p\)-rank when \(p\equiv1\pmod4\).

## Verification
The accompanying standalone standard-Python script `verify.py` expands both sides of the coefficient identity exactly in characteristic \(p\), compares every entry of the resulting Cartier arrays, and checks the ranks of both the array and its \(g\)-fold product for all smooth prime-field parameters at the ten primes from \(11\) to \(43\). It also checks reciprocal symmetry, the leading parameter coefficients, and the unique zero-rank parameter. Run `python3 verify.py`. Successful output begins with `VERIFY_PRIME_RIGIDITY_OK`.

At \(p=11\), the five antidiagonal entries are \(5a\), \(9a+10a^3\), \(8a+9a^3+a^5\), \(9a+10a^3\), \(5a\). The script checks them directly. The proof above is symbolic and applies to all primes in scope and all geometric parameters; the finite computations are supporting verification rather than extrapolation.

## Relationship to prior work
Borges and Gonçalves study \(p\)-ranks of Fermat-type curves \(y^m=x^n+1\) and establish formulas for the undeformed two-term curves; they motivate comparison with the corresponding three-term deformation. The superspecial undeformed member \(a=0\) is therefore not claimed as a new construction. Kudo, Nakagawa, and Takagi study superspecial genus-four hyperelliptic curves with a different three-term-plus-one family and describe standard Cartier coefficient methods. Their explicit genus-four calculations do not, by themselves, imply the stated all-prime family formula and its Frobenius-stability property. Related low-genus dihedral pencils and classical Hasse–Witt coefficient identities are also acknowledged as context. The present claim is only the uniform complete prime-linked marked-family stratification for \(p\ge11\).

## Limitations
No Newton polygons, moduli-isomorphism counts, or exact cardinalities of the intermediate geometric parameter strata are determined. The explicit coefficient equations give a finite test for each stratum but are not a closed root-count formula. Historical priority remains uncertain because older treatments of dihedral hyperelliptic Hasse–Witt matrices could contain an equivalent general statement. No independent mathematical audit is claimed.

## References
1. M. Kudo, T. Nakagawa and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing Z6*, arXiv:2210.14822, first posted 2022-10-26. https://arxiv.org/abs/2210.14822
2. H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987, first posted 2022-12-07. https://arxiv.org/abs/2212.03987
3. R. Pries, *Pries Project: hyperelliptic curves, Hasse–Witt matrices and p-rank* (mathematical notes). https://wiki.sagemath.org/days26/Pries%20Project
