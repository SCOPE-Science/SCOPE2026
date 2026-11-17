# Rank-vector enumeration of mutually annihilating self-adjoint operators over finite orthogonal spaces

## Finding

Let \(k=\mathbb F_q\) with \(q\) an odd prime power, let \(V\) be a nondegenerate symmetric bilinear space of dimension \(n\ge 3\), and let \(r\ge 2\). For an ordered tuple \((X_1,\ldots,X_r)\) of endomorphisms, impose
\[
 X_i^\dagger=X_i,\qquad X_iX_j=0\quad\text{for every }1\le i,j\le r.
\]
The diagonal conditions \(X_i^2=0\) are included. Write \(U=\sum_i\operatorname{im}X_i\), \(d=\dim U\), and \(\rho_i=\operatorname{rank}X_i\). The following formula counts **labeled ordered tuples**, with zero operators allowed, for every fixed rank vector and joint-image dimension.

Define the Gaussian binomial coefficient \({a\brack b}_q\) by its usual subspace count, with value zero outside \(0\le b\le a\). Let
\[
 M_{e,t}(q)={e\brack t}_q q^{t(t+1)/2}
 \prod_{h=1}^{\lceil t/2\rceil}\left(1-q^{-(2h-1)}\right)
\]
for integers \(0\le t\le e\), and \(M_{e,t}(q)=0\) otherwise; empty products equal one. This is the number of symmetric \(e\times e\) matrices of rank \(t\) over \(k\).

Let \(w\) be the Witt index of \(V\). For \(0\le d\le w\), let \(I_V(d)\) be the number of totally isotropic \(d\)-dimensional subspaces, with \(I_V(0)=1\). The precise answer is
\[
 \boxed{\mathcal F_{V,r}(d;\rho_1,\ldots,\rho_r)
  =I_V(d)\sum_{j=0}^d(-1)^j q^{\binom j2}
    {d\brack j}_q\prod_{i=1}^r M_{d-j,\rho_i}(q).}
\]
The count is zero when \(d>w\). The formula applies to all nonnegative ranks, interpreted using the zero convention on \(M_{e,t}\). In particular, the pairwise products and all squares vanish automatically in every counted tuple.

The isotropic factor is explicitly determined by \(n,q\) and the orthogonal type. For odd \(n\), the Witt index is \((n-1)/2\). For even \(n\), it is \(n/2\) in split (hyperbolic) type and \(n/2-1\) in nonsplit (elliptic) type. Define \(s_V(m)\), for the residual form of dimension \(m=n-2i\), by
\[
 s_V(m)=\begin{cases}
 q^{m-1}-1,&n\text{ odd},\\
 q^{m-1}+(q-1)q^{m/2-1}-1,&n\text{ even and split},\\
 q^{m-1}-(q-1)q^{m/2-1}-1,&n\text{ even and nonsplit}.
 \end{cases}
\]
Then
\[
 \boxed{I_V(d)=\frac{\prod_{i=0}^{d-1}q^i s_V(n-2i)}{
 \prod_{i=0}^{d-1}(q^d-q^i)}}
\]
for \(1\le d\le w\). The numerator is a count of ordered isotropic frames; the denominator is \(|\mathrm{GL}_d(k)|\).

Summing over every individual rank yields the compact joint-image distribution
\[
 \boxed{\mathcal F_{V,r}(d)=I_V(d)
 \sum_{j=0}^d(-1)^j q^{\binom j2}{d\brack j}_q
 q^{r(d-j)(d-j+1)/2}.}
\]
The total count is \(\sum_{d=0}^{w}\mathcal F_{V,r}(d)\). These are exact formulas for all odd finite fields, dimensions, tuple lengths and orthogonal types in the stated scope.

A concrete discrimination occurs already for \(n=4\), \(q=3\), and \(r=2\): a split form admits \(1+128+5568=5697\) tuples in joint-image dimensions \(0,1,2\), whereas a nonsplit form admits only \(1+80=81\) tuples, in dimensions \(0,1\). Thus the point-count distribution detects Witt type.

## Assumptions and scope

All vector spaces are finite-dimensional over an odd-characteristic finite field. The adjoint is taken **relative to the fixed nondegenerate symmetric bilinear form**, not to a positive-definite inner product. The matrices are endomorphisms of the **same** underlying space; the condition \(X_iX_j=0\) includes both orders and self-products. No restriction to invertible or nonzero tuple entries is imposed. Changing the matrix basis for the same form changes none of the counts.

## Proof

**1. Common image and isotropy.** Let \(U=\sum_i\operatorname{im} X_i\). For arbitrary \(x,y\in V\), self-adjointness gives
\[
 \langle X_i x,X_j y\rangle=\langle x,X_iX_j y\rangle=0.
\]
Hence \(U\) is totally isotropic and \(0\le d\le w\). Moreover \(X_i\) annihilates \(U^\perp\): for \(v\in U^\perp\) and all \(x\in V\), \(\langle X_i v,x\rangle=\langle v,X_i x\rangle=0\). Therefore each \(X_i\) factors as \(V\to V/U^\perp\to U\subseteq V\).

**2. Symmetric maps.** Nondegeneracy identifies \(V/U^\perp\cong U^*\). Under this identification the self-adjointness equation is precisely symmetry of the corresponding map \(B_i:U^*\to U=(U^*)^*\); equivalently, a symmetric bilinear form on \(U^*\). Conversely, any such symmetric map produces a self-adjoint \(X_i\) with image in \(U\) and kernel containing \(U^\perp\). Since \(U\subseteq U^\perp\), any pair of resulting endomorphisms has zero composition. Their ranks agree with \(\operatorname{rank} B_i\). Their combined images equal \(U\) exactly when the common radical \(\bigcap_i\ker B_i\) is zero.

**3. Symmetric-rank counts.** The radical of a symmetric \(e\)-dimensional bilinear form of rank \(t\) is an \((e-t)\)-space. There are \({e\brack t}_q\) choices for that radical and, on the quotient, the number of nonsingular symmetric \(t\times t\) matrices equals
\[
 q^{t(t+1)/2}\prod_{h=1}^{\lceil t/2\rceil}(1-q^{-(2h-1)}).
\]
The latter identity follows by summing the \(\mathrm{GL}_t(k)\)-congruence orbit sizes of the two discriminant classes using standard odd-field orthogonal-group orders. It also holds for \(t=0\), where there is exactly one zero-dimensional form. This proves the stated \(M_{e,t}\).

**4. Recovering full joint image.** Fix \(U\) of dimension \(d\) and ranks \((\rho_1,\ldots,\rho_r)\). On the lattice of subspaces \(K\subseteq U^*\), the Möbius coefficient of a subspace of dimension \(j\) is \((-1)^j q^{\binom j2}\). For a fixed \(K\), the number of rank-\(\rho_i\) symmetric forms whose radical contains \(K\) is \(M_{d-j,\rho_i}(q)\), because such a form descends uniquely to the quotient \(U^*/K\). Möbius inversion therefore counts exactly the tuples with common radical zero, giving the sum displayed in the finding. The unique common image \(U\) prevents double-counting between distinct \(d\)-spaces.

**5. Isotropic-subspace factor.** A nondegenerate symmetric form of odd dimension \(m\) has exactly \(q^{m-1}\) zero vectors, including zero. In even dimension \(m\), the number is \(q^{m-1}\pm(q-1)q^{m/2-1}\), with sign determined by its Witt type. These standard identities follow by counting zeros in a Witt decomposition into hyperbolic planes and an anisotropic summand of dimension at most two (the hyperbolic-plane zero count is \(2q-1\); the anisotropic two-space has only the zero vector). After choosing \(i\) mutually orthogonal independent isotropic vectors, the orthogonal quotient has dimension \(n-2i\) and the original orthogonal complement has a \(q^i\)-element radical. The next frame vector therefore has \(q^i s_V(n-2i)\) admissible choices. Division by the \(\prod_{i=0}^{d-1}(q^d-q^i)\) ordered bases of a fixed \(d\)-space gives \(I_V(d)\). This completes the rank-vector count.

**6. Total distribution.** Summing \(M_{e,t}(q)\) over \(t\) gives the total number \(q^{e(e+1)/2}\) of symmetric \(e\times e\) matrices. Substituting into step 4 produces the joint-image distribution and its sum over \(d\).

## Verification

Run `python check_orthogonal_annihilating.py` for independent literal matrix enumeration, and `python check_orthogonal_formula.py` for independent integer evaluation of rank-vector and unrefined formulas. Python 3 and NumPy are required only for the first program. Outputs are supplied as `orthogonal_check_output.txt` and `orthogonal_formula_check_output.txt`. The first program enumerates all self-adjoint square-zero operators and all mutually annihilating pairs over \(\mathbb F_3\) in dimension four for both Witt types; it also enumerates dimension-three examples over \(\mathbb F_3\) and \(\mathbb F_5\). The second program verifies every rank-vector coefficient in the dimension-four tests and compares rank-vector sums with direct joint-image expressions for several larger dimensions, fields and tuple lengths. Finite checks are corroboration; the above proof handles unrestricted parameters.

## Relationship to prior work

Schröer (2002, arXiv:math/0211293) classifies geometric irreducible components of varieties of unrestricted mutually annihilating nilpotent pairs; this is not a finite-field point count for the fixed self-adjoint locus. Bondarenko, Gerasimova and Sergeichuk (2008, arXiv:0812.2155), with earlier cited classifications, give canonical forms for unrestricted mutually annihilating pairs under simultaneous similarity. This does not count labeled tuples satisfying a fixed self-adjointness constraint or distinguish orthogonal Witt types. Oblak (2006, arXiv:math/0612300) determines possible Jordan-form pairs rather than such counts. Brouwer, Gow and Sheekey (2014) count individual nilpotent operators self-adjoint for a symmetric form; they do not impose mutual annihilation on an ordered family and do not provide its joint-image/rank-vector enumerator. Huang (2021, arXiv:2110.15566) counts unrestricted mutually annihilating matrix pairs by a generating function, without the fixed quadratic-space condition. The present result combines the self-adjoint and mutually annihilating conditions through the isotropic common image, retaining individual ranks and arbitrary tuple length. A general unpublished or unidentified incidence-count formula could imply this result; priority is not certified.

## Limitations

The hypotheses require odd field characteristic and a nondegenerate symmetric bilinear form. The theorem enumerates labeled matrix tuples, not their isometry-conjugacy orbits, nonreduced scheme structures, or endomorphisms of higher nilpotence index. It does not count merely commuting operators whose products are nonzero. It is a mathematical proof accompanied by finite computations; it has not undergone independent external validation or exhaustive historical-priority certification.

## References

1. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293v1 (2002-11-19), https://arxiv.org/abs/math/0211293 .
2. V. M. Bondarenko, T. G. Gerasimova and V. V. Sergeichuk, *Pairs of mutually annihilating operators*, arXiv:0812.2155v1 (2008-12-11), https://arxiv.org/abs/0812.2155 .
3. A. E. Brouwer, R. Gow and J. Sheekey, *Counting symmetric nilpotent matrices*, Electronic Journal of Combinatorics 21(2) (2014), P2.4, https://doi.org/10.37236/3810 .
4. P. Oblak, *Jordan forms for mutually annihilating nilpotent pairs*, arXiv:math/0612300 (2006-12-12), https://arxiv.org/abs/math/0612300 .
5. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (2021), https://arxiv.org/abs/2110.15566 .
