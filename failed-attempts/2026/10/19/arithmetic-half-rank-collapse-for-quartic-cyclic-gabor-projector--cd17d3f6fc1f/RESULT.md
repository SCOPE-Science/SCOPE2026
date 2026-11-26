# Arithmetic half-rank collapse for quartic cyclic Gabor projectors

## Finding

For every prime \(p\ge5\) and \(N\in\{p,p^2\}\), let
\[
g_N(t)=N^{-1/2}\exp(2\pi i t^4/N),\quad t\in\mathbb Z/N\mathbb Z,
\]
and let \(v_{a,b}=M_bT_a g_N\), with \((T_a g)(t)=g(t-a)\) and \((M_b g)(t)=\exp(2\pi i bt/N)g(t)\). Form the \(N^2\)-by-\(N^2\) Gram matrix of rank-one projectors
\[
K_{(a,b),(c,d)}=|\langle v_{a,b},v_{c,d}\rangle|^2.
\]
Write \(\zeta_N=\exp(2\pi i/N)\) and define the normalized self-ambiguity
\[
A_N(h,w)=\frac1N\sum_{t\bmod N}\zeta_N^{(t+h)^4-t^4-wt}.
\]
For all \((u,v)\in(\mathbb Z/N\mathbb Z)^2\), the Fourier characters diagonalize \(K\), with the **exact** eigenvalue at character \((u,v)\) given by
\[
\lambda_{u,v}=N|A_N(-v,u)|^2.
\]
In particular, the matrix rank equals the number of nonzero ambiguity values, and the kernel is the span of the associated vanishing Fourier-character directions. These assertions concern the *linear operator-valued intensity lifting*, not unconditional phase retrieval of all pure states.

**Prime order.** For \(N=p\), \(A_p(h,w)=0\) exactly when either \(h=0\) and \(w\ne0\), or \(p\equiv2\pmod3\), \(h\ne0\), and \(w=h^3\) in \(\mathbb F_p\). Consequently
\[
\operatorname{rank}K_p=p^2-(p-1)(1+\mathbf1_{p\equiv2\ (\mathrm{mod}\ 3)}).
\]

**Prime-square order.** For \(N=p^2\), the following mutually exclusive conditions describe *all* zeros:

1. \(h=0\) and \(w\ne0\pmod{p^2}\).
2. \(h=pH\) with \(H\in\mathbb F_p^\times\), and either \(p\nmid w\), or \(p\equiv2\pmod3\) and \(w=0\pmod{p^2}\).
3. \(p\nmid h\), and \(\chi_p((w-h^3)(12h)^{-1})=-1\). Here reduction to \(\mathbb F_p\) is implicit and \(\chi_p(0)=0\).

There are no additional zero cells. In particular, \(\operatorname{rank}K_{p^2}=R_p\), where
\[
R_p=1+(p-1)(p-\mathbf1_{p\equiv2\ (\mathrm{mod}\ 3)})
+\frac{p^2(p^2-1)}2
=\begin{cases}
(p^4+p^2-2p+2)/2,&p\equiv1\pmod3,\\
(p^4+p^2-4p+4)/2,&p\equiv2\pmod3.
\end{cases}
\]
The exact kernel dimension is \(p^4-R_p\). Thus
\[
\frac{\operatorname{rank}K_p}{p^2}\longrightarrow1,
\qquad
\frac{\operatorname{rank}K_{p^2}}{p^4}\longrightarrow\frac12
\quad (p\to\infty\text{ through primes}).
\]
The congruence class of \(p\) mod \(3\) controls a smaller correction at both orders.

## Assumptions and scope

Only odd primes \(p\ge5\) and cyclic rings of order \(p\) or \(p^2\) are considered. The normalized vector \(g_N\) has squared norm one. A matrix direction is **linearly identifiable** when it is outside the kernel of the map \(X\mapsto(\operatorname{tr}(Xv_{a,b}v_{a,b}^*))_{a,b}\) on complex matrices. The count \(R_p\) is the complex dimension of the identifiable operator span, equivalently the real dimension on Hermitian operators. Every congruence in the zero criterion is taken modulo the stated modulus. The Legendre symbol is \(-1\) exactly on nonzero quadratic nonresidues.

## Proof

**1. Weyl/Fourier diagonalization (standard component).** The unit-modulus commutation factor of \(M_bT_a\) gives \(K_{(a,b),(c,d)}=|A_N(a-c,b-d)|^2\). Expanding the squared absolute value in the discrete Fourier transform gives the exact identity
\[
\sum_{h,w\bmod N}|A_N(h,w)|^2\zeta_N^{-uh-vw}
=N|A_N(-v,u)|^2.
\]
Therefore Fourier characters diagonalize \(K\). Their labels are permuted bijectively by \((u,v)\mapsto(-v,u)\), and the number of nonzero eigenvalues equals the ambiguity support count. For the operator-valued analysis map, expand each matrix in the orthogonal Weyl-operator basis. The measured coefficient Fourier transform is the corresponding Weyl coefficient multiplied by the window's ambiguity value (up to a nonzero phase). Consequently the complex lifting kernel is precisely the span of Weyl operators indexed by ambiguity zeros. This diagonalization is standard in finite Gabor lifting; the new arithmetic task is the exact ambiguity-zero classification below.

**2. Cubic permutation criterion over a prime field.** For nonzero \(a\in\mathbb F_p\), consider \(F(x)=ax^3+bx\). Its additive character sum vanishes precisely when its \(p\) outputs are all distinct. Indeed, if \(c_j\) is the number of outputs equal to \(j\), the relation \(\sum_jc_j\zeta_p^j=0\) and irreducibility of \(1+X+\cdots+X^{p-1}\) force \(c_0=\cdots=c_{p-1}=1\). If \(b=0\), \(x\mapsto ax^3\) permutes the field exactly when \(\gcd(3,p-1)=1\), equivalently \(p\equiv2\pmod3\). If \(b\ne0\), a collision \(F(x)=F(y)\), \(x\ne y\), is equivalent to \(x^2+xy+y^2=-b/a\). With \(u=x-y\) and \(v=x+y\), this becomes \(u^2+3v^2=-4b/a\), where the right side is nonzero. The classical quadratic-character sum \(\sum_{v\in\mathbb F_p}\chi_p(C-3v^2)=-\chi_p(-3)\) for \(C\ne0\) shows that this conic has \(p-\chi_p(-3)\ge p-1\) solutions; at most two have \(u=0\). Since \(p\ge5\), a solution with \(u\ne0\) exists. Hence the character sum is nonzero for \(b\ne0\).

**3. Prime modulus.** Because \(2\) is invertible, substitute \(s=t+h/2\) to obtain
\[
(t+h)^4-t^4-wt
=4hs^3+(h^3-w)s+wh/2.
\]
For \(h=0\), the ambiguity is one at \(w=0\) and zero otherwise. For \(h\ne0\), the irrelevant constant phase disappears from zero testing and step 2 applies with \(a=4h\), \(b=h^3-w\). Thus \(A_p(h,w)=0\) precisely for \(p\equiv2\pmod3\) and \(w=h^3\). Counting gives the stated prime-order rank.

**4. Prime-square stationary-phase identity.** For an integral polynomial \(F\) and \(N=p^2\), writing \(t=x+py\) yields
\[
\sum_{t\bmod p^2}\zeta_{p^2}^{F(t)}
=p\sum_{\substack{x\bmod p\\F'(x)\equiv0\ (\mathrm{mod}\ p)}}\zeta_{p^2}^{F(x)}.
\]
This is exact because \(F(x+py)\equiv F(x)+pyF'(x)\pmod{p^2}\), and the inner sum over \(y\) is either \(p\) or zero. For \(p\nmid h\), use the centered cubic from step 3. Its derivative is \(12hs^2+h^3-w\). The stationary congruence has zero, one, or two solutions according as \((w-h^3)(12h)^{-1}\) is a nonresidue, zero, or nonzero square in \(\mathbb F_p\). With no stationary points the sum is zero; with one it is a single nonzero root of unity; with two it is the sum of *two odd-order roots of unity*, which cannot cancel because \(-1\) is not a \(p^2\)-th root of unity. This proves zero criterion 3, including the discriminant boundary.

**5. Prime-divisible shifts.** For \(h=pH\ne0\pmod{p^2}\), the phase reduces to \(4pHt^3-wt\pmod{p^2}\). If \(p\nmid w\), summing lifts \(t=x+py\) yields zero. If \(w=pW\), then
\[
A_{p^2}(pH,pW)=\frac1p\sum_{x\bmod p}\zeta_p^{4Hx^3-Wx},
\]
which vanishes by step 2 precisely when \(p\equiv2\pmod3\) and \(W=0\). For \(h=0\), Fourier orthogonality gives criterion 1. These are all cases.

**6. Counting.** The \(h=0\) row contributes one survivor. The \(p-1\) shifts with \(p\mid h\), \(h\ne0\), each have \(p\) surviving frequencies when \(p\equiv1\pmod3\) and \(p-1\) when \(p\equiv2\pmod3\). There are \(p^2-p\) unit shifts; for each one, the set \(\{0\}\cup(\mathbb F_p^\times)^2\) contains \((p+1)/2\) allowed derivative right-hand sides, each with \(p\) frequency lifts, hence \(p(p+1)/2\) survivors. Adding gives \(R_p\), the nullity, and the limits. \(\square\)

## Verification

The standalone checker `verify_quartic.py` evaluates every ambiguity-zero condition **exactly** for primes \(5,7,11,13\), at both modulus exponents \(1\) and \(2\). It reduces the exponent-count polynomial modulo the corresponding cyclotomic polynomial, rather than treating small floating sums as zero. This checks \(46{,}592\) total ambiguity cells: \(25+625+49+2401+121+14641+169+28561=46{,}592\). The measured ranks at square order are \(317,1219,7361,14353\); all match the formulas. Separate numerical Fourier-Gram comparisons at the first two primes check the eigenvalue normalization and Fourier labeling. The recorded maximum discrepancy is below \(1.5\cdot10^{-14}\). Run `python verify_quartic.py` with Python 3 and NumPy as specified in `requirements.txt`; compare with `verify_output.txt`.

The symbolic argument proves the infinite two-exponent family; finite tests do not establish a theorem for arbitrary primes or higher prime powers.

## Relationship to prior work

Bojarovska and Flinth, *Phase Retrieval from Gabor Measurements* (arXiv:1503.05800v2, 2015), prove general finite-Gabor phase-retrieval conditions and develop the Weyl-coordinate lifting framework. The present Weyl diagonalization is not asserted to be original. Alaifari and Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements* (arXiv:1901.05296, first posted 2019-01-12), give discrete ambiguity-factor identities and stability analysis. Their results do not state the congruence-by-congruence quartic prime-square zeros or the exact rank count here. The combined new statement is the explicit arithmetic support and rank classification for the unmodified quartic phase window at prime and prime-square orders. Prior work on cubic phase windows and on indicator windows supported on polynomial graphs concerns different finite Gabor generators and does not imply these quartic cyclic prime-square zero sets. Classical stationary-phase and cyclotomic identities are used and not claimed as new.

## Limitations

The conclusions cover \(p\ge5\) and exponents \(1,2\) only. The exact **rank** and **zero set** are determined; the positive eigenvalues are specified by finite exponential sums, not gathered into a minimal list of distinct magnitudes. Noninjectivity of a linear operator-valued lift alone does not establish failure of nonlinear pure-state phase retrieval for a particular signal class. No noise stability or condition-number theorem is asserted. An equivalent older description in polynomial-phase radar or character-sum literature cannot be ruled out by bibliographic searches alone.

## References

1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (initial public version 2015-03-19), https://arxiv.org/html/1503.05800v2 . See Section 2.2 and the Weyl expansion in its proof.
2. R. Alaifari and M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296 (first public 2019-01-12), https://ar5iv.labs.arxiv.org/html/1901.05296 . See Section 2, especially Lemma 2.2.
