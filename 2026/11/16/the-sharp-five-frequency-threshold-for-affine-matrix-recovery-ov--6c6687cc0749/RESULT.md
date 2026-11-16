# The sharp five-frequency threshold for affine matrix recovery over thirteen points

## Finding

Let \(\mathbb F_{13}\) be the field with thirteen elements, let \(U=\mathbb F_{13}^{\times}\), and let \(\rho\) be the standard twelve-dimensional irreducible unitary representation of the affine group \(G=\mathbb F_{13}\rtimes U\) on \(\mathbb C^U\), given by
\[
(\rho(k,\ell)\varphi)(t)=e^{-2\pi i kt/13}\varphi(\ell t),\qquad k\in\mathbb F_{13},\quad \ell,t\in U.
\]
The smallest possible support size of a vector \(\varphi\in\mathbb C^U\) whose orbit projectors \(\{\rho(g)\varphi\varphi^*\rho(g)^*:g\in G\}\) span all of \(M_{12}(\mathbb C)\) is **exactly five**. Thus every generator supported on four or fewer Fourier coordinates fails full matrix recovery, while the following five-frequency generator succeeds:
\[
\operatorname{supp}\varphi=\{1,2,3,4,11\},\qquad
(\varphi(1),\varphi(2),\varphi(3),\varphi(4),\varphi(11))=(1,2,4,8,16).
\]
This is a Fourier-coordinate sparsity theorem; it makes no sparsity claim about the inverse Fourier transform in the original thirteen-point coordinate system. The resulting affine orbit contains \(13\cdot12=156\) vectors and permits exact recovery of any complex \(12\)-by-\(12\) matrix by its \(156\) rank-one measurements (and therefore phaseless recovery of every signal up to global phase).

The obstruction at support size four is an incompatibility between covering the twelve nonzero **additive differences** and covering the eleven nonidentity **multiplicative quotients**. All four-element perfect additive difference sets in \(\mathbb F_{13}\), avoiding zero, realize at most nine distinct nonidentity multiplicative quotients.

## Assumptions and scope

The field is exactly \(\mathbb F_{13}\). The frequency set \(U\) excludes zero. Complex coefficients of \(\varphi\) are unrestricted, except for the declared exact support. The group action is indexed by \(G\) with the usual affine law \((k,\ell)(k',\ell')=(k+\ell k',\ell\ell')\). The sign convention in the exponential has no bearing on orbit-projector span. Matrix recovery means injectivity of the complex-linear measurement map \(A\mapsto(\operatorname{tr}(A\rho(g)\varphi\varphi^*\rho(g)^*))_{g\in G}\) on all of \(M_{12}(\mathbb C)\), not merely on rank-one positive matrices.

We use the proved affine-group recovery criterion of Bartusel–Führ–Oussa (2021, Theorem 6.5 and equation (6.5)): the orbit does matrix recovery if and only if (i) every multiplicative Fourier coefficient of \(|\varphi|^2\) on \(U\) is nonzero, and (ii) the \(12\)-by-\(11\) matrix \(C_\varphi\), obtained from the nontrivial columns of their transformed matrix \(C_\varphi\), has column rank eleven. Their equation (6.10) shows that the alternative matrix \(B_\varphi\) in the criterion differs only by row and column permutations. We construct the former explicitly below.

## Proof

**1. Convert the rank condition into additive and multiplicative support covers.** For each \(m\in U\) and \(n\in U\setminus\{1\}\), set
\[
C_\varphi(m,n)=\varphi\!\left(\frac{m}{1-n}\right)
\overline{\varphi\!\left(\frac{mn}{1-n}\right)},
\]
with all fractions interpreted in \(\mathbb F_{13}\). If \(S=\operatorname{supp}\varphi\), a column indexed by \(n\) is zero unless \(n=y/x\) for distinct \(x,y\in S\); a row indexed by \(m\) is zero unless \(m=x-y\) for distinct \(x,y\in S\). Consequently column rank eleven requires at least eleven distinct nonidentity multiplicative quotients and at least eleven nonzero additive differences.

For \(|S|\le3\), there are at most six ordered pairs of distinct elements, and hence at most six nonzero columns: recovery is impossible. Suppose \(|S|=4\). Since \(S-S\setminus\{0\}\) is symmetric under negation and thirteen is odd, it has even cardinality. At least eleven nonzero rows therefore forces all twelve nonzero differences to occur. Because four points have exactly twelve ordered distinct pairs, every nonzero difference must occur **exactly once**: \(S\) is a cyclic \((13,4,1)\) planar difference set.

**2. Classify the four-point difference sets and prove quotient obstruction.** Any four-point perfect difference set can be affinely normalized to contain \(0,1\). Write it as \(\{0,1,a,b\}\), with \(2\le a<b\le12\). Checking the fifty-five possible pairs \((a,b)\) against the twelve differences yields precisely
\[
(a,b)\in\{(3,9),(4,6),(5,11),(8,10)\}.
\]
These four normal forms are affine images of \(D=\{0,1,3,9\}\); hence every perfect difference set is \(uD+v\), with \(u\in U\), \(v\in\mathbb F_{13}\). Scaling by \(u\) preserves quotient-set size. Put \(t=v/u\); because the support must avoid zero, the only possible \(t\) values are \(1,2,3,5,6,7,8,9,11\). The numbers of distinct nonidentity quotients for \(D+t\) in this order are
\[
8,9,8,9,9,7,7,8,7.
\]
All are at most nine, so \(C_\varphi\) has at least two identically zero columns for every four-supported candidate satisfying the additive condition. Thus no four-supported vector can generate full matrix recovery, for any complex amplitudes. Both short finite classifications are fully reproduced by the standalone exact checker, which also independently exhausts all \(\binom{12}{4}=495\) candidate supports.

**3. Exhibit a five-supported recovery vector.** Set the five coefficients as in the finding. A multiplicative character \(\chi\) on \(U\) has modulus one, and the single largest coefficient gives
\[
\left|\sum_{t\in U}|\varphi(t)|^2\chi(t)\right|
\ge 16^2-(1^2+2^2+4^2+8^2)=171>0.
\]
Thus condition (i) holds for every one of the twelve characters. Form the integer matrix \(C_\varphi\) using the displayed formula and columns \(n=2,\ldots,12\). Delete its row \(m=4\); the resulting \(11\)-by-\(11\) integer determinant is exactly
\[
\det C_\varphi[U\setminus\{4\},\,\{2,\ldots,12\}]=-2^{43}\ne0.
\]
Hence the rank is eleven, condition (ii) holds, and the cited affine-group criterion yields full matrix recovery. In addition, an independent *exact modular certificate* avoids reliance on the sufficiency direction of that criterion: set \(q=53\), map the primitive complex thirteenth root of unity \(\zeta_{13}\) to \(10\in\mathbb F_{53}\), and form the full \(156\)-by-\(144\) orbit-projector coefficient matrix. Since \(10^{13}=1\) and \(10\ne1\) in \(\mathbb F_{53}\), this defines a homomorphism from the cyclotomic integer ring. Exact Gaussian elimination gives rank \(144\) modulo \(53\), so a maximal minor is nonzero already over the cyclotomic integers and consequently over \(\mathbb C\). Combining the lower and upper bounds proves the exact support threshold five.

## Verification

Run `python3 verify_affine13.py` with Python 3, using only its standard library. It checks all fifty-five normalized four-sets, enumerates all \(\binom{13}{4}=715\) four-sets to independently compare the fifty-two perfect sets with the affine orbit of \(D\), checks all nine possible translations for quotient counts, independently rules out the simultaneous support-cover condition on all 495 four-subsets of \(U\), and evaluates the displayed rank minor by an exact integer Bareiss elimination. The script checks the exact modular rank of the full \(156\)-by-\(144\) orbit-projector matrix over \(\mathbb F_{53}\), as a second proof of the witness sufficiency. It prints `AFFINE13_SPARSE_RECOVERY_PASS` and `AFFINE13_DIRECT_ORBIT_SPAN_PASS` only after all assertions succeed. The reduction is mathematically sound because evaluating a primitive thirteenth root at \(10\in\mathbb F_{53}\) respects the cyclotomic polynomial, and a determinant nonzero after reduction cannot have been zero in characteristic zero. Exact finite enumeration here proves a finite claim because all subsets and normalized configurations are exhausted; no assertion is extrapolated to larger fields.

## Relationship to prior work

Bartusel, Führ, and Oussa establish the general matrix-recovery criterion and construct working affine-group generators. Their theorem is used as a starting point; the new result identifies the minimum *Fourier support* for the specific prime thirteen, including an exact obstruction to the nominal four-frequency pair-counting bound. Mészáros, Rónyai, and Szabó describe planar Singer difference sets and their relationship to projective geometry; their work does not address affine rank-one matrix recovery or simultaneous additive-difference/multiplicative-quotient support coverage. Other affine-group retrieval and finite short-time Fourier phase-retrieval results concern different group actions or measurement families and do not give this exact cutoff.

## Limitations

The exact threshold is proved only at thirteen and concerns **full matrix recovery**, not the potentially weaker minimum support for phase retrieval alone. It is not a universal lower bound for arbitrary prime sizes or arbitrary frame families. The field-size-thirteen result is self-contained modulo the cited, independently published affine recovery criterion; no independent external mathematical validation has yet been performed. Historical priority under alternative finite-wavelet or difference-basis terminology remains provisional.

## References

1. D. Bartusel, H. Führ, V. Oussa, *Phase retrieval for affine groups over prime fields*, arXiv:2109.07123, first posted 2021-09-15. Theorem 6.5, equation (6.5), equation (6.10), Theorem 6.6 and its proof. https://arxiv.org/abs/2109.07123
2. T. Mészáros, L. Rónyai, T. Szabó, *Singer difference sets and the projective norm graph*, arXiv:1908.05591, first posted 2019-08-15, Section 1.2 on planar Singer difference sets. https://arxiv.org/abs/1908.05591
