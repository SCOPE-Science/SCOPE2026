# A sharp degree–Euler threshold for spinor varieties
## Finding
For each integer
\[
n\ge1,
\]
let
\[
S_n=\operatorname{OG}(n+1,2n+2)
\]
denote one connected component of the maximal orthogonal Grassmannian over \(\mathbb C\), embedded by its minimal half-spin line bundle. Put
\[
M=\frac{n(n+1)}2.
\]

Then
\[
\boxed{
\deg S_n
=
M!\,
\frac{\prod_{j=1}^{n-1}j!}
{\prod_{j=1}^{n}(2j-1)!}
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}(S_n)=2^n.
}
\]

There is no equality between these two invariants. Their complete ordering is
\[
\boxed{
\deg S_n<\chi_{\mathrm{top}}(S_n)
\iff
1\le n\le4,
}
\]
and
\[
\boxed{
\deg S_n>\chi_{\mathrm{top}}(S_n)
\iff
n\ge5.
}
\]

The transition is sharp:
\[
(\deg S_4,\chi_{\mathrm{top}}(S_4))=(12,16),
\]
whereas
\[
(\deg S_5,\chi_{\mathrm{top}}(S_5))=(286,32).
\]

More structurally,
\[
\boxed{
\frac{\deg S_{n+1}}{\deg S_n}
=
\frac{\binom{M+n+1}{n+1}}
{\binom{2n+1}{n+1}}.
}
\]
After division by the Euler growth factor \(2\), the normalized quotient
\[
\frac{\deg S_n}{2^n}
\]
is unchanged only from \(n=2\) to \(n=3\), and is strictly increasing for every subsequent step.

## Assumptions and scope
The base field is \(\mathbb C\). The variety is one of the two connected components of maximal isotropic \((n+1)\)-planes in a nondegenerate quadratic vector space of dimension \(2n+2\).

The polarization is the ample generator giving the minimal half-spin embedding. The projective degree is taken in this embedding.

The Euler characteristic is the ordinary topological Euler characteristic of the complex projective homogeneous variety.

## Proof
Kresch and Tamvakis identify
\[
S_n=\operatorname{OG}(n+1,2n+2)
\]
and give an integral Schubert basis indexed by strict partitions whose largest part is at most \(n\). Such a strict partition is uniquely determined by the subset of
\[
\{1,\ldots,n\}
\]
formed by its parts. Therefore the Schubert cell decomposition has exactly
\[
2^n
\]
cells. Every cell has even real dimension, so
\[
\chi_{\mathrm{top}}(S_n)=2^n.
\]

Let
\[
\rho_n=(n,n-1,\ldots,1).
\]
Its size is
\[
|\rho_n|=M.
\]
The codimension-one Schubert class is the hyperplane class of the minimal homogeneous embedding. The classical Pieri rule for multiplication by this class adds one box with coefficient one. Consequently the coefficient of the point class after \(M\) multiplications is the number of saturated chains from the empty strict partition to \(\rho_n\), equivalently the number of shifted standard tableaux of staircase shape \(\rho_n\).

The shifted hook-length formula therefore gives
\[
\deg S_n
=
M!\,
\frac{\prod_{1\le i<j\le n}(\rho_i-\rho_j)}
{\left(\prod_{i=1}^{n}\rho_i!\right)
 \left(\prod_{1\le i<j\le n}(\rho_i+\rho_j)\right)}.
\]
Substituting
\[
\rho_i=n-i+1
\]
and simplifying the products yields
\[
\deg S_n
=
M!\,
\frac{\prod_{j=1}^{n-1}j!}
{\prod_{j=1}^{n}(2j-1)!}.
\]

Now compare consecutive degrees. Since
\[
M_{n+1}=M+n+1,
\]
the factorial product gives
\[
\frac{\deg S_{n+1}}{\deg S_n}
=
\frac{(M+1)(M+2)\cdots(M+n+1)\,n!}{(2n+1)!}
=
\frac{\binom{M+n+1}{n+1}}
{\binom{2n+1}{n+1}}.
\]

Set
\[
\delta=M-n=\frac{n(n-1)}2.
\]
The last quotient may be written as
\[
\prod_{s=1}^{\delta}
\frac{2n+1+s}{n+s}.
\]
For \(n=2\), one has \(\delta=1\), so the ratio is exactly \(2\). For every \(n\ge3\), one has \(\delta>1\); the first factor is \(2\), and every subsequent factor is strictly greater than \(1\). Hence
\[
\frac{\deg S_{n+1}}{\deg S_n}>2
\qquad(n\ge3).
\]

Thus
\[
R_n=\frac{\deg S_n}{2^n}
\]
satisfies
\[
R_2=R_3=\frac14
\]
and is strictly increasing for \(n\ge3\). The explicit values
\[
R_4=\frac34
\qquad\text{and}\qquad
R_5=\frac{143}{16}>1
\]
give the unique crossover. The initial value
\[
R_1=\frac12
\]
completes the classification.

## Verification
The bundled checker evaluates the factorial degree formula with exact integer arithmetic for
\[
1\le n\le30.
\]
It independently evaluates the shifted-tableau product formula and verifies that it agrees with the factorial expression.

It checks the exact adjacent-degree ratio and the complete comparison with
\[
2^n
\]
through the same range.

These finite computations are regression evidence only. The infinite classification follows from the symbolic adjacent-ratio argument.

## Relationship to prior work
The Schubert calculus of maximal orthogonal Grassmannians gives both the strict-partition cell indexing and the Pieri rule needed to interpret projective degree as a staircase shifted-tableau count. The shifted hook-length formula then supplies the closed product for that count.

Existing arithmetic work on spinor degrees studies divisibility and relations with other homogeneous varieties. The comparison made here is different: it puts the minimal projective degree against the total Schubert-cell count, equivalently the Euler characteristic, and identifies a single sharp threshold between \(S_4\) and \(S_5\).

Targeted searches using spinor-variety, orthogonal-Grassmannian, degree, Euler characteristic, Schubert-cell count, and equality language did not locate this complete ordering.

## Limitations
The theorem concerns only the minimal half-spin polarization. Higher tensor powers multiply the degree by a power determined by the dimension and therefore have different thresholds.

The result is a comparison of two numerical invariants; it does not assert a direct geometric map between the corresponding enumerative and topological counts.

Both ingredient formulas are classical, so an older or unindexed source may contain the same inequality without emphasizing the threshold.

## References
Andrew Kresch and Harry Tamvakis, *Quantum cohomology of orthogonal Grassmannians*, arXiv:math/0306338, first submitted 24 June 2003; *Compositio Mathematica* 140 (2004), 482--500, DOI 10.1112/S0010437X03000204.

Ilse Fischer, *A bijective proof of the hook-length formula for shifted standard tableaux*, arXiv:math/0112261, first submitted 23 December 2001.
