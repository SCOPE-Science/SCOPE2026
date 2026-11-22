# Boolean classification of minimum-genus semigroups immediately beyond the one-third Frobenius threshold

## Finding

Let \(m\) be a positive integer and \(r\in\{1,2\}\), with \(m\ge2\) when \(r=1\) and \(m\ge3\) when \(r=2\). Put \(F=3m+r\). Among all numerical semigroups of multiplicity \(m\) and Frobenius number \(F\), the minimum genus equals \(\lceil(F+1)/2\rceil\). The exact number attaining this minimum is

\[
\boxed{I(m,3m+r)=2^{\lfloor(m-r-1)/2\rfloor}}.
\]

The attaining semigroups are exactly the irreducible semigroups with these two invariants. More strongly, their Kunz coordinates form a full Boolean cube of the displayed dimension, with explicit coordinate descriptions below. The two lines \(F=3m+1\) and \(F=3m+2\) are the first two admissible Frobenius lines beyond the established multiparameter-counting hypothesis \(m\ge(F+1)/3\); the intervening line \(F=3m\) admits no semigroups of multiplicity \(m\), since \(m\mid F\).

## Assumptions and scope

A numerical semigroup \(S\) is a cofinite additive submonoid of \(\mathbb N_0\). Its multiplicity \(m\) is its smallest positive element, Frobenius number \(F\) its largest omitted nonnegative integer, and genus \(g\) its number of omitted nonnegative integers. Its Apéry set with respect to \(m\) consists of \(0\) and \(w_i=mx_i+i\), for \(1\le i\le m-1\); the positive integers \(x_i\) are its Kunz coordinates. They obey

\[
x_i+x_j+\left\lfloor\frac{i+j}{m}\right\rfloor\ge x_{(i+j)\bmod m},\qquad 1\le i,j<m,
\]

with \(x_0=0\). Conversely every positive integral vector satisfying these inequalities defines a numerical semigroup of multiplicity \(m\), with \(g=\sum_{i=1}^{m-1}x_i\) and \(F=\max_i(mx_i+i)-m\).

The following gives all minimizers, including the smallest admissible values.

**First line \(F=3m+1\).** Set \(x_1=4\). Pair the indices \(2,\ldots,m-1\) under the involution \(i\mapsto m+1-i\). On each two-element orbit choose independently the ordered pair of coordinates \((1,2)\) or \((2,1)\). If there is a fixed index, assign its coordinate \(2\). These and only these vectors minimize genus. There are \(\lfloor(m-2)/2\rfloor\) independent choices.

**Second line \(F=3m+2\).** Set \(x_1=2\) and \(x_2=4\). Pair the indices \(3,\ldots,m-1\) under \(i\mapsto m+2-i\). Each two-element orbit independently gets \((1,2)\) or \((2,1)\); a fixed index, if any, gets \(2\). There are \(\lfloor(m-3)/2\rfloor\) independent choices.

## Proof

**The forced Apéry coordinate.** Suppose \(F=3m+r\). Since the largest Apéry element is \(F+m=4m+r\), it belongs to residue class \(r\), so \(x_r=4\). Every other \(x_i\) is at most \(3\), except that for \(r=2\) the coordinate \(x_1\) may be at most \(4\). All coordinates are at least one. The asserted constraints therefore apply to every semigroup in the given parameter class.

**Genus lower bound for \(r=1\).** The pairs \(i+j=m+1\), with \(2\le i,j<m\), have Kunz inequality \(x_i+x_j+1\ge x_1=4\), hence \(x_i+x_j\ge3\). A fixed point of the pairing must have coordinate at least \(2\). With \(x_1=4\), summing the disjoint orbits yields

\[
g\ge4+3\left\lfloor\frac{m-2}{2}\right\rfloor+2\big((m-2)\bmod2\big)=\left\lceil\frac{3m+2}{2}\right\rceil.
\]

Equality forces exactly the paired binary choices, because all other coordinates are positive and each pair's sum is exactly three. Such pairs can only be \((1,2)\) or \((2,1)\); the fixed coordinate equals two.

**Genus lower bound for \(r=2\).** The inequality at \(i=j=1\) gives \(2x_1\ge x_2=4\), so \(x_1\ge2\). For pairs \(i+j=m+2\), with \(3\le i,j<m\), the inequality gives \(x_i+x_j+1\ge x_2=4\), hence each pair has sum at least three and any fixed point has coordinate at least two. Thus

\[
g\ge6+3\left\lfloor\frac{m-3}{2}\right\rfloor+2\big((m-3)\bmod2\big)=\left\lceil\frac{3m+3}{2}\right\rceil.
\]

Equality forces \(x_1=2\), all indicated binary pairs, and the possible fixed coordinate two.

**Existence and absence of hidden constraints.** Every vector described above satisfies all Kunz inequalities. Indeed, every coordinate except the special \(x_r=4\) lies in \(\{1,2\}\), and any inequality whose right-hand coordinate is not \(x_r\) is automatic because its right-hand side is at most two and its left-hand side is at least two. For \(r=1\), the right-hand coordinate is \(x_1\) only when \(i+j=m+1\), where the constructed pair has \(x_i+x_j+1=4\). For \(r=2\), the right-hand coordinate \(x_2\) occurs only when \(i=j=1\), where \(2x_1=4\), or when \(i+j=m+2\), where the constructed pair has \(x_i+x_j+1=4\). Thus every constructed positive integral vector defines a numerical semigroup. Its largest Apéry member is \(4m+r\), because each other member is at most \(3m+i<4m+r\) (or \(2m+1\) at coordinate one in the second case). Its multiplicity and Frobenius number are exactly the stipulated values.

**Exact count and irreducibility.** Every orbit of size two makes one unconstrained binary choice, and the number of such orbits is \(\lfloor(m-r-1)/2\rfloor\). Hence precisely the displayed power of two arises. The standard genus bound \(g\ge\lceil(F+1)/2\rceil\) follows by pairing each gap with its reflection under \(z\mapsto F-z\); equality is equivalent to a symmetric semigroup when \(F\) is odd and a pseudo-symmetric semigroup when \(F\) is even. In either parity these are precisely the irreducible numerical semigroups. The constructions attain equality and thus classify every irreducible in both specified classes.

## Verification

Run the self-contained Python 3 script `verify.py`. It exhaustively enumerates every Kunz vector compatible with each \((m,F)\) for \(m\le11\) on the first line and \(3\le m\le11\) on the second, checks the full Kunz inequality system, filters by the least genus, and compares the entire set—not just its cardinality—to the predicted Boolean family. All nineteen cases pass. The script also independently constructs membership sets and verifies closure, Frobenius number, and genus for the predicted vectors. Its terminal success string is `TWO_LINE_KUNZ_VERIFY_OK`.

The computation checks bounded cases only; the preceding symbolic proof covers all admissible \(m\).

## Relationship to prior work

Bras-Amorós and Torra's November 2026 theorem gives an explicit multiparameter counting formula under \(m\ge(F+1)/3\), while the July 2026 paper develops enumeration algorithms and tabulates finite ranges. Neither stated theorem applies to \(F=3m+1\) or \(F=3m+2\), since in both cases \(m<(F+1)/3\). The two lines here provide closed, complete irreducible subfamilies immediately beyond that boundary, but they do not replace the earlier three-parameter census for other genus values.

Branco, Ojeda and Rosales (2019) give a general algorithm for enumerating semigroups and irreducibles with fixed \(m\) and \(F\) via Kunz-coordinate constraints. That algorithm can generate each finite instance here; the claimed contribution is the uniform power-of-two count and explicit independent-choice classification across unbounded multiplicity, not the Kunz-coordinate method. Related covariety and irreducible-tree algorithms are likewise acknowledged.

## Limitations

Only the minimum-genus (irreducible) layer and only the two displayed first-outside-boundary Frobenius lines are classified. No formula is claimed for larger genus or for \(F\ge3m+3\). General algorithms may reproduce any fixed instance; the discovery is the infinite symbolic enumeration. Historical originality remains provisional with respect to unindexed specialist literature; no independent audit has been performed.

## References

1. M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups by Frobenius number, genus, and multiplicity*, 2026-11-08, https://arxiv.org/abs/2611.11559 .
2. M. Bras-Amorós and V. Torra, *Algorithms and results on multiparameter counting of numerical semigroups*, 2026-07-25, https://arxiv.org/abs/2607.23111 .
3. M. B. Branco, I. Ojeda and J. C. Rosales, *The set of numerical semigroups of a given multiplicity and Frobenius number*, 2019-04-11, https://arxiv.org/abs/1904.05551 .
4. M. A. Moreno-Frías and J. C. Rosales, *The covariety of numerical semigroups with fixed Frobenius number*, 2024, https://doi.org/10.1007/s10801-024-01342-x .
