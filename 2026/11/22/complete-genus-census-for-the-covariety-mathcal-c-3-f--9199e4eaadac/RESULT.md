# Complete genus census for the covariety \(\mathcal C(\{3,F\})\)

## Finding

For each integer \(F\ge4\), write
\[
\mathcal C_3(F)=\{S\subseteq\mathbb N_0:\ S\text{ is a numerical semigroup},\ F(S)=F,\ 3\in\operatorname{PF}(S)\}.
\]
This is the prescribed-pseudo-Frobenius covariety \(\mathcal C(\{3,F\})\) of Hernández-Yanes and Rosales. The following is an exact, genus-refined classification **of the entire family**, with no fixed-multiplicity restriction.

Every member is uniquely
\[
S_{a,b,c}=\{0\}\cup\{3j+1:j\ge a\}\cup\{3j+2:j\ge b\}\cup\{3j:j\ge c\},
\]
where \(a,b\ge1\), \(c\ge2\), and
\[
b\le2a,\qquad a\le2b+1,\qquad c\le a+b+1,\qquad
F=\max(3a-2,3b-1,3c-3).
\]
Its genus is \(g(S_{a,b,c})=a+b+c-1\).

Let \(G_F(z)=\sum_{S\in\mathcal C_3(F)}z^{g(S)}\). For \(k\ge2\),
\[
G_{3k}(z)=z^k\sum_{\substack{1\le a,b\le k\\a+b\ge k,\ b\le2a,\ a\le2b+1}}z^{a+b}.
\]
For \(k\ge1\),
\[
G_{3k+1}(z)=z^k\left(\sum_{b=\lceil k/2\rceil}^kz^b\right)
\left(\sum_{c=2}^{k+1}z^c\right),
\]
\[
G_{3k+2}(z)=z^k\left(\sum_{a=\lceil(k+1)/2\rceil}^{k+1}z^a\right)
\left(\sum_{c=2}^{k+1}z^c\right).
\]
An explicit coefficient law in the remaining case is available: for \(k\ge2\) and \(k\le t\le2k\), the coefficient of \(z^{k+t}\) in \(G_{3k}(z)\) equals
\[
\min\!\left(k,\left\lfloor\frac{2t+1}{3}\right\rfloor\right)
-\max\!\left(t-k,\left\lceil\frac t3\right\rceil\right)+1,
\]
and all other coefficients vanish.

In particular, the **exact total counts** are
\[
|\mathcal C_3(3k)|=\left\lceil\frac{(k+1)(k+2)}3\right\rceil \quad(k\ge2),
\]
\[
|\mathcal C_3(3k+1)|=k\left(\left\lfloor\frac k2\right\rfloor+1\right),\qquad
|\mathcal C_3(3k+2)|=k\left(\left\lfloor\frac{k+1}2\right\rfloor+1\right)\quad(k\ge1).
\]
The cardinality is a quadratic quasipolynomial with period dividing \(18\). Along the Frobenius residue class divisible by three it is \(F^2/27+O(F)\), while on the other two classes it is \(F^2/18+O(F)\). Thus the leading coefficient differs by a factor \(3/2\) according to \(F\bmod3\).

## Assumptions and scope

Here \(\mathbb N_0=\{0,1,2,\ldots\}\). A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\); \(F(S)\) is its largest gap and \(g(S)\) its number of positive gaps. A pseudo-Frobenius number \(p\) is a gap with \(p+s\in S\) for every nonzero \(s\in S\). The requirement is **containment** \(3\in\operatorname{PF}(S)\), not equality \(\operatorname{PF}(S)=\{3,F\}\). For \(F=3\), the two-generator semigroup \(\langle2,5\rangle\) is an exceptional member not described by the displayed parameter domain; consequently all the claims above intentionally require \(F\ge4\).

## Proof

**Residue tails.** If \(3\in\operatorname{PF}(S)\), then \(3\notin S\) and \(S\setminus\{0\}+3\subseteq S\). Every nonzero residue class modulo three is therefore an upward tail in steps of three. Because \(1\in S\) would imply \(S=\mathbb N_0\), we have \(1\notin S\). If \(2\in S\), then closure forces all even integers at least two to lie in \(S\), while the pseudo-Frobenius condition forces \(5\in S\). Hence every integer at least four is in \(S\) and \(F(S)=3\), excluded by \(F\ge4\). Thus \(2,3\) are gaps, the three tails start at \(3a+1\), \(3b+2\), \(3c\) with \(a,b\ge1\), \(c\ge2\), and uniqueness of the thresholds is immediate.

**Closure.** The sum of two positive tail elements lies above the first element of its target residue tail precisely when the minimal sums do. Same-residue-zero products and products with a positive residue-zero element are automatically in the required tails. The remaining three products impose exactly
\[
2(3a+1)\ge3b+2,\quad 2(3b+2)\ge3a+1,\quad
(3a+1)+(3b+2)\ge3c,
\]
which reduce to the three stated inequalities. Conversely, they ensure additive closure; co-finiteness is automatic, and adding three to a positive member stays in the same tail. The last omitted elements of the three residue classes are \(3a-2\), \(3b-1\), \(3c-3\). Taking their maximum proves the exact Frobenius formula. Counting omissions in the three classes gives \(g=a+b+c-1\).

**Fixing the Frobenius number.** The three candidate largest gaps have distinct residues modulo three. Thus \(F=3k\) forces \(c=k+1\), with \(a,b\le k\), and the closure inequalities reduce to \(a+b\ge k\), \(b\le2a\), \(a\le2b+1\). Similarly \(F=3k+1\) forces \(a=k+1\), \(\lceil k/2\rceil\le b\le k\), \(2\le c\le k+1\), with no other restriction. Finally \(F=3k+2\) forces \(b=k+1\), \(\lceil(k+1)/2\rceil\le a\le k+1\), \(2\le c\le k+1\). Substitution into the genus formula gives all three polynomial identities, without sampling or extrapolation.

**Coefficients and total.** For \(F=3k\), fixing \(t=a+b\) makes the inequalities equivalent to
\[
\max\!\left(t-k,\left\lceil\frac t3\right\rceil\right)
\le a\le\min\!\left(k,\left\lfloor\frac{2t+1}3\right\rfloor\right).
\]
This proves the coefficient expression. To count all pairs, begin with the \(T=k^2-(k-1)(k-2)/2\) pairs in the square \(1\le a,b\le k\) for which \(a+b\ge k\). Subtract the disjoint violations \(b>2a\) and \(a>2b+1\). Set \(h_1=\lfloor(k-1)/2\rfloor\), \(d_1=\lfloor(k-1)/3\rfloor\), \(h_2=\lfloor(k-2)/2\rfloor\), \(d_2=\lfloor(k-2)/3\rfloor\). The two forbidden counts are exactly
\[
R_1=\sum_{j=1}^{d_1}(j+1)+\sum_{j=d_1+1}^{h_1}(k-2j),\qquad
R_2=\sum_{j=1}^{d_2}(j+1)+\sum_{j=d_2+1}^{h_2}(k-2j-1).
\]
Evaluating these arithmetic sums in the six cases \(k\bmod6\) yields
\(T-R_1-R_2=\lceil(k+1)(k+2)/3\rceil\) for every \(k\ge2\). For the other Frobenius residues, multiplying the two independent interval lengths immediately produces the remaining total-count formulas. The quasipolynomial and leading-term assertions follow from the explicit counts.

## Verification

Run `python3 verify.py` using only the Python standard library. It independently enumerates *every* subset of positive integers below each Frobenius number \(4\le F\le18\), tests additive closure and the pseudo-Frobenius condition directly, and matches its complete genus histogram against the parameter classification. For \(19\le F\le750\), it separately recomputes all allowed parameter triples and compares every genus coefficient and each total to the formulas above. The recorded result from the embedded checker is `VERIFY_OK 747 parameter values; exhaustive F=4..18; formulas F=4..750`. Finite verification supports but does not replace the universal proof above.

## Relationship to prior work

Hernández-Yanes and Rosales (arXiv:2611.09425v1, 2026) introduced the general prescribed-pseudo-Frobenius covariety \(\mathcal C(\mathcal P)\), its tree, and algorithms for fixed type or genus. Their stated algorithms apply to this input, but the inspected results do not state the all-\(F\) residue-tail classification, exact genus polynomial, or quadratic quasipolynomial. Moreno-Frías and Rosales (2024) established the fixed-Frobenius covariety without the additional prescribed gap. Delgado, García-Sánchez, and Robles-Pérez (arXiv:1505.08111, 2015) provide algorithms for **exactly specified** pseudo-Frobenius sets, a distinct constraint. The result here is an explicit uniform enumeration of the containment-defined family, not a claim to invent the covariety framework or algorithms.

## Limitations

The result does not enumerate \(\mathcal C(\mathcal P)\) for general prescribed sets, nor does it determine full pseudo-Frobenius sets of every parameter triple. It proves an available period \(18\), without claiming it is the least quasiperiod. Earlier equivalent classifications in other terminology cannot be categorically ruled out from the accessible literature.

## References

1. W. G. Hernández-Yanes and J. C. Rosales, *The covariety of numerical semigroups with some prescribed pseudo-Frobenius numbers*, arXiv:2611.09425v1 (first posted November 6, 2026), https://arxiv.org/abs/2611.09425.
2. M. A. Moreno-Frías and J. C. Rosales, *The covariety of numerical semigroups with fixed Frobenius number*, Journal of Algebraic Combinatorics 60 (2024), 555–568, https://doi.org/10.1007/s10801-024-01342-x.
3. M. Delgado, P. A. García-Sánchez, and A. M. Robles-Pérez, *Numerical semigroups with a given set of pseudo-Frobenius numbers*, LMS J. Comput. Math. 19 (2016), 186–205; arXiv:1505.08111, https://arxiv.org/abs/1505.08111.
