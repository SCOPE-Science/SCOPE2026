# Divisor-stratified lattice volumes of one-defect directed-cycle simplices

## Finding
For integers \(n\ge 3\), \(w\ge 2\), and \(u\ge 1\), put
\[
P_{n,w,u}=\operatorname{conv}\bigl\{e_i+w e_{i+1}\ (1\le i<n),\ e_n+u e_1\bigr\}\subset\mathbb R^n,
\qquad T_n(w)=\left|\sum_{k=0}^{n-1}(-w)^k\right|.
\]
Let \(\operatorname{Vol}_{\mathbb Z}(P)\) mean the normalized \((n-1)\)-dimensional volume in the intrinsic affine lattice \(\operatorname{aff}(P)\cap\mathbb Z^n\). Then
\[
\boxed{\operatorname{Vol}_{\mathbb Z}(P_{n,w,u})=\gcd\bigl(T_n(w),|u-w|\bigr).}
\]
In particular, the uniform-weight case has normalized volume \(T_n(w)\), while changing **one** vertex weight by one, to \(u=w+1\), gives a unimodular simplex in every dimension. As \(u\) runs through positive integers, the distinct normalized volumes are precisely the positive divisors of \(T_n(w)\); the volume is periodic in \(u\) with **least** positive period \(T_n(w)\), and the proportion of unimodular weights in any complete period is \(\varphi(T_n(w))/T_n(w)\). In every unimodular case the full Ehrhart counting polynomial is \(\binom{m+n-1}{n-1}\) for each nonnegative integer dilation \(m\), and the simplex has the integer decomposition property.

## Assumptions and scope
The vectors \(e_i\) are the standard basis of \(\mathbb R^n\). These are positive-exponent weighted directed-cycle edge vectors, not the signed root vectors of an oriented cycle. All vertex weights are positive integers, with the first \(n-1\) arrivals weighted \(w\) and exactly one exceptional arrival weighted \(u\). The lattice used to normalize volume is **intrinsic to each varying affine hyperplane**, not one fixed Euclidean measure. The Euler totient \(\varphi(t)\) counts residue classes coprime to \(t\). We adopt \(\gcd(t,0)=|t|\) for nonzero integers. For the stated parameters \(T_n(w)>1\), and every polytope is an \((n-1)\)-simplex.

## Proof
**1. A full-rank cyclic column matrix.** Let \(C\) be the integer \(n\times n\) matrix whose columns are the displayed vertices in order. Its diagonal entries are one, its entries immediately below the diagonal are \(w\), and its upper-right entry is \(u\). The only two nonzero permutation products in its determinant give
\[
D:=\det C=1+u(-w)^{n-1}.
\]
When \(n\) is odd, \(D>0\); when \(n\) is even, \(u w^{n-1}\ge8\), so \(D<0\). Thus \(D\ne0\), and the \(n\) columns are affinely independent.

**2. Primitive integral normal and volume.** Set \(z=\operatorname{adj}(C^T)\mathbf1\in\mathbb Z^n\), so \(C^T z=D\mathbf1\). Let \(g=\gcd(|z_1|,\ldots,|z_n|)\), and write \(a=z/g\), which is primitive integral. The affine hull of the simplex has equation \(a\cdot x=D/g\). The kernel lattice \(\Lambda=\{b\in\mathbb Z^n:a\cdot b=0\}\) is primitive of rank \(n-1\). Subtracting the last column of \(C\) from the first \(n-1\) columns does not change its determinant; computing the resulting determinant after a unimodular integer coordinate change taking \(a\) to a coordinate covector yields
\[
|D|=|D/g|\,\operatorname{Vol}_{\mathbb Z}(P_{n,w,u}).
\]
Consequently \(\operatorname{Vol}_{\mathbb Z}(P_{n,w,u})=g\). This is an integer lattice-index identity, not an inference from ambient Euclidean volume.

**3. Compute the normal's coordinate gcd.** Define the signed sums
\[
s=\sum_{k=0}^{n-1}(-w)^k,\qquad s'=\sum_{k=0}^{n-2}(-w)^k.
\]
Writing the equations \(C^Tz=D\mathbf1\) explicitly gives
\[
z_i+wz_{i+1}=D\quad(1\le i<n),\qquad z_n+uz_1=D.
\]
Iterating the first equations backward gives \(z_1=D s'+(-w)^{n-1}z_n\). Substituting \(z_n=D-uz_1\) and \(D=1+u(-w)^{n-1}\) yields \(D z_1=D(s'+(-w)^{n-1})=Ds\), hence
\[
z_1=s,\qquad z_2-s=-(u-w)(-w)^{n-2},\qquad z_n-s=-(u-w)s'.
\]
(The latter two identities use \(D\vert_{u=w}=(w+1)s\).) Since \(D\) is affine in \(u\), and the displayed recurrence gives \(z_n=D-us\) followed by \(z_i=D-wz_{i+1}\), every \(z_i\) is congruent to \(s\) modulo \(u-w\). Therefore \(\gcd(s,u-w)\) divides all entries of \(z\). Conversely, their gcd divides \(s=z_1\) and both \((u-w)(-w)^{n-2}\) and \((u-w)s'\). The geometric sum satisfies \(s'\equiv1\pmod w\), hence \(\gcd(s',w^{n-2})=1\); Bézout's identity now forces the gcd of all entries of \(z\) to divide \(u-w\). It follows that
\[
g=\gcd(|s|,|u-w|)=\gcd(T_n(w),|u-w|).
\]
The argument also includes \(u=w\), because all the normal coordinates then equal \(s\).

**4. Exact arithmetic spectrum and Ehrhart consequence.** The right side depends only on \(u-w\bmod T_n(w)\), so \(T_n(w)\) is a period. Conversely, any positive period \(p\) must preserve the maximal value at \(u=w\); therefore \(\gcd(T_n(w),p)=T_n(w)\), forcing \(T_n(w)\mid p\). For every divisor \(d\mid T_n(w)\), the positive weight \(u=w+d\) gives volume \(d\); these are all possible values. Exactly \(\varphi(T_n(w))\) residues have gcd one. In a unimodular simplex, an affine unimodular change of lattice coordinates sends the vertices to a standard lattice simplex. Its lattice-point count at dilation \(m\) is \(\binom{m+n-1}{n-1}\), and its lattice points decompose into sums of its degree-one vertices, establishing the stated Ehrhart and integer-decomposition conclusions. In particular, \(u=w+1\) is always unimodular, while \(u=w\) has volume \(T_n(w)\), whose magnitude grows exponentially with \(n\) for each fixed \(w\ge2\).

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The checker independently constructs each column matrix, computes its determinant by exact-integer Bareiss elimination, then computes the gcd of all maximal minors of the edge-difference matrix without using the normal-vector formula. It checks all \(264\) parameter triples \(3\le n\le8\), \(2\le w\le5\), \(1\le u\le11\), including \(181\) unimodular cases. The exact theorem is proved above; no finite enumeration is substituted for an infinite proof.

## Relationship to prior work
Biermann, Lin, and O'Keefe (arXiv:2611.17047, first posted 12 November 2026) define these weighted oriented graph edge polytopes, give the naturally oriented cycle incidence matrix in Definition 2.5, and study their integer decomposition property. Their Lemma 2.6 treats the equal-weight cyclic determinant; Theorem 4.5 gives a non-IDP obstruction for naturally oriented cycles with equal weight \(w>1\) and \(n\ge4\). The present result treats a different question—the normalized lattice volume and the *single unequal weight's* complete arithmetic spectrum—and strengthens the positive \(u=w+1\) instance to unimodularity. Nanduri and Roy (arXiv:2504.15200) study the corresponding toric ideals, rather than this lattice-volume classification. A public weighted-cycle Ehrhart computation (published-finding corpus, 17 November 2026, identifier `b7680edb541b`) establishes a shifted \(h^*\)-symmetry for arbitrary weights and a complete numerator only for equal-weight five-cycles. Its equal-weight volume is consistent with the specialization above, but neither that symmetry nor its specialized numerator yields the variable-weight gcd/divisor classification. A prior root-polytope calculation for arbitrarily oriented cycles (published-finding corpus, 4 October 2026, identifier `e32575b66377`) uses signed differences \(e_i-e_j\), not these positive-exponent vertices.

## Limitations
This theorem is confined to one exceptional positive integer vertex weight on an otherwise uniform **naturally oriented** cycle. It does not classify general unequal-weight cycles, Euclidean volumes under a fixed metric, or the integer decomposition property when the normalized volume is larger than one. Unimodularity is a sufficient, not necessary, condition for the integer decomposition property. Because the intrinsic affine lattice changes with \(u\), the sharp volume drop is an arithmetic index phenomenon; it must not be interpreted as a uniform Euclidean-volume drop. Earlier unindexed computations of exceptional-weight directed cycles may exist, so historical priority remains open to external scrutiny. No independent mathematical audit has been performed.

## References
- J. Biermann, K.-N. Lin, and A. O'Keefe, *Integer Decomposition Property of Edge Polytopes of Weighted Oriented Graphs*, arXiv:2611.17047 (first posted 2026-11-12), https://arxiv.org/abs/2611.17047.
- R. Nanduri and T. K. Roy, *On robust toric ideals of weighted oriented graphs*, arXiv:2504.15200 (first posted 2025-04-21), https://arxiv.org/abs/2504.15200.
- *Shifted Ehrhart symmetry and a sharp log-concavity threshold for weighted directed-cycle simplices*, published-finding corpus (2026-11-17), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-shifted-ehrhart-symmetry-and-a-sharp-log-concavity-threshold-for--b7680edb541b.
- *Exact Ehrhart polynomials of oriented cycle root polytopes*, published-finding corpus (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ehrhart-polynomials-of-oriented-cycle-root-polytopes--e32575b66377.
