# Thirteen-periodic maximal-component counts for square-zero sandwich representations

## Finding
For any field \(k\) and integer \(n\ge1\), let \(\mathcal X_n(k)\) consist of ordered pairs of \(n\)-by-\(n\) matrices satisfying
\[
P^2=P,\qquad N^2=0,\qquad PNP=0.
\]
For \((P,N)\in\mathcal X_n(k)\), set \(r=\operatorname{rank}P\), \(h=\operatorname{rank}N\), and \(t=\operatorname{rank}(NP)\). The reduced rank stratum \(\mathcal X_n(r,h,t)\) is nonempty, smooth, and geometrically irreducible precisely for the integer ranges
\[
0\le h\le\lfloor n/2\rfloor,\qquad 0\le r\le n-h,\qquad 0\le t\le\min(h,r).
\]
Its dimension is exactly
\[
d_n(r,h,t)=2h(n-h)+2r(n-r)-hr+ht-t^2.
\]
Over \(\mathbb F_q\), the number of **individual labeled pairs** in this stratum is
\[
\boxed{C_{n,q}(r,h,t)={n\brack h}_q{n-h\brack h}_q|\mathrm{GL}_h(\mathbb F_q)|{h\brack t}_q{n-h-t\brack r-t}_q\,q^{t(n-h)+r(n-r-t)}.}
\]
Here \({a\brack b}_q=0\) for \(b<0\) or \(b>a\), and \(|\mathrm{GL}_0(\mathbb F_q)|=1\). The formula counts the zero matrices and all boundary ranks. Summing the displayed expression over the permitted triples gives the complete finite-field count of the pair variety.

The reduced affine variety has sharp dimension
\[
\boxed{\dim\mathcal X_n=\left\lfloor\frac{11n^2}{13}\right\rfloor.}
\]
For every \(n\ge13\), the number of top-dimensional irreducible components depends only on \(n\bmod13\). In order of residue \(0,1,\ldots,12\), this number is
\[
\boxed{(1,4,2,3,2,1,2,2,1,2,3,2,4).}
\]
For \(1\le n<13\), the same table applies except that \(n=1\) has two rather than four top components and \(n=3\) has two rather than three. This counts only components of **maximal dimension**, not all irreducible components.

## Assumptions and scope
The equations are interpreted as ordinary matrix polynomial equations over \(k\), without assumptions on characteristic or algebraic closure. Smoothness, irreducibility, and dimension are assertions about the **reduced, locally closed geometric rank strata** after base extension to an algebraic closure. No claim is made that the original possibly nonreduced equation scheme is smooth. For the cardinality formulas \(q\) is an arbitrary prime power. The ranks refer to maps on the same \(n\)-dimensional space, not to simultaneous-conjugacy classes.

## Proof
**1. Square-zero rank data.** Let \(V=k^n\), \(U=\operatorname{im}N\), and \(K=\ker N\). If \(N^2=0\) and \(\operatorname{rank}N=h\), then \(U\subseteq K\), \(\dim U=h\), and \(\dim K=n-h\). Conversely, any flag \(U\subseteq K\subseteq V\) with these dimensions, together with an isomorphism \(V/K\longrightarrow U\), uniquely determines such an \(N\). The rank-\(h\) square-zero locus is a smooth geometrically irreducible homogeneous bundle of dimension \(2h(n-h)\), with exactly
\[
{n\brack h}_q{n-h\brack h}_q|\mathrm{GL}_h(\mathbb F_q)|
\]
points over \(\mathbb F_q\).

**2. Idempotents as splittings.** Every idempotent \(P\) uniquely determines a direct sum \(V=S\oplus W\), with \(S=\operatorname{im}P\), \(\dim S=r\), and \(W=\ker P\); conversely each such splitting defines a unique \(P\). The condition \(PNP=0\) is equivalent to \(N(S)\subseteq W\). In particular \(S\cap N(S)=0\), and \(t=\dim N(S)\). If \(A\) denotes the image of \(S\) inside \(V/K\), then \(\dim A=t\), while \(B=S\cap K\) has dimension \(b=r-t\). The space \(T=N(S)\subseteq U\) is the image of \(A\) under the fixed isomorphism \(V/K\cong U\). Because \(T\subseteq K\), the condition \(S\cap T=0\) is equivalent to \(B\cap T=0\).

**3. Counting the admissible images.** First choose \(A\subseteq V/K\) of dimension \(t\): \({h\brack t}_q\) choices. For its fixed image \(T\subseteq K\), choose a \(b\)-subspace \(B\subseteq K\) disjoint from \(T\). Projection along \(T\) shows that there are
\[
{n-h-t\brack b}_q q^{tb}
\]
choices: choose a \(b\)-subspace of \(K/T\), then a linear graph over it with values in \(T\). For each fixed \((A,B)\), the subspaces \(S\) with projection \(A\) and intersection \(B\) form an affine space of dimension \(t(n-h-b)\). Thus the total number of choices of \(S\) is
\[
{h\brack t}_q{n-h-t\brack r-t}_q q^{t(n-h)}.
\]
The existence conditions are exactly \(0\le t\le\min(h,r)\) and \(r\le n-h\), together with \(2h\le n\). These are also sufficient.

**4. Counting the kernels.** With \(S\cap T=0\), the complements \(W\) to \(S\) that contain \(T\) are precisely the complements of \((S+T)/T\) in \(V/T\). They form an affine space of dimension \(r(n-r-t)\), hence number \(q^{r(n-r-t)}\) over \(\mathbb F_q\). Multiplying the counts from steps 1, 3, and 4 proves the displayed formula. Every construction is a bundle made from flag varieties, open disjointness conditions, and affine spaces. Consequently each nonempty **reduced rank stratum** is smooth and geometrically irreducible. The dimension, obtained by summing those of the factors, simplifies to
\[
2h(n-h)+t(h-t)+(r-t)(n-h-r)+t(n-h)+r(n-r-t)
=2h(n-h)+2r(n-r)-hr+ht-t^2.
\]

**5. The global sharp bound.** Put
\[
\alpha=r-5n/13,\quad \beta=h-6n/13,\quad\gamma=t-3n/13.
\]
An exact completion of squares gives
\[
\frac{11n^2}{13}-d_n(r,h,t)
=2(\alpha+\beta/4)^2+\frac{13}{8}\beta^2+(\gamma-\beta/2)^2\ge0.
\]
Since \(d_n(r,h,t)\) is an integer, the dimension is at most \(\lfloor11n^2/13\rfloor\). Equality is attained for every \(n\ge1\) by the integral triples given in step 6, so the bound is sharp.

**6. Exact thirteen-periodic maximizers.** Write \(n=13m+s\) with \(0\le s\le12\). All unconstrained integer triples attaining the floor bound are obtained by adding \((5m,6m,3m)\) to the following list of triples \((r,h,t)\) for the residue \(s\):

| \(s\) | Integral maximizers at \(m=0\) |
|---|---|
| 0 | (0,0,0) |
| 1 | (0,0,0), (0,1,0), (0,1,1), (1,0,0) |
| 2 | (1,1,0), (1,1,1) |
| 3 | (1,1,0), (1,1,1), (1,2,1) |
| 4 | (1,2,1), (2,2,1) |
| 5 | (2,2,1) |
| 6 | (2,3,1), (2,3,2) |
| 7 | (3,3,1), (3,3,2) |
| 8 | (3,4,2) |
| 9 | (3,4,2), (4,4,2) |
| 10 | (4,4,2), (4,5,2), (4,5,3) |
| 11 | (4,5,2), (4,5,3) |
| 12 | (4,6,3), (5,5,2), (5,5,3), (5,6,3) |

For completeness, this is a finite exact arithmetic certificate, not a numerical optimization conjecture. If a triple attains the floor bound, the nonnegative sum in step 5 is strictly less than one. It follows that \(|\beta|<1\), \(|\alpha|<1\), and \(|\gamma|<3/2\). Hence at each residue only the two integers nearest to \(6s/13\) for \(h\), the two nearest to \(5s/13\) for \(r\), and integers from \(\lfloor3s/13\rfloor-1\) to \(\lceil3s/13\rceil+1\) for \(t\) need be checked. Direct substitution in the exact integer quadratic gives precisely the table. Adding \((5m,6m,3m)\) preserves the quantity in step 5 and gives every solution. For \(m\ge1\), all displayed triples satisfy the required rank inequalities. At \(m=0\), the only inadmissible top triples for positive \(s\) occur at \(s=1\) (the two with \(h=1\)) and at \(s=3\) (the one with \(h=2\)). Thus the table yields the stated exceptional counts. Finally, distinct nonempty rank strata of the same maximal dimension have distinct irreducible closures: each stratum is locally closed and dense open in its closure, and two such dense opens cannot have different generic ranks. Every top-dimensional component contains the closure of one such stratum. Therefore the number of top-dimensional components equals the number of admissible maximizing triples.

## Verification
The dependency-free program `verify.py` enumerates every idempotent and every square-zero matrix in the original matrix algebra, checks \(PNP=0\) by direct multiplication, and compares all \((r,h,t)\)-cell populations against the independent Gaussian-binomial formula. Exhaustive cells match over \(\mathbb F_2\) in dimensions one through three and over \(\mathbb F_3\) and \(\mathbb F_5\) in dimensions one/two as applicable. The exact dimension formula and component counts are additionally checked by integer enumeration through dimension 59. See `checks.txt` for exact outputs. These finite computations corroborate the proof but do not establish its infinite quantifiers by themselves.

## Relationship to prior work
Richmond's stratification of module varieties (2001) gives general smooth irreducible strata and an abstract dimension-maximization principle for subfinite algebras, but its examined theorems and examples do not give the specific \(PNP=0\) rank-cell count or the thirteen-periodic maximizer table. Schröer's work on mutually annihilating nilpotent matrix pairs (initial arXiv posting 2002) solves a different set of equations, with two nilpotent factors and both mixed products zero. The sharper relation \(PN=0\) is a **proper** special case of the present relation and, after transposition, is exactly the \(t=0\) slice. It cannot determine the new \(t>0\) cells; for example over \(\mathbb F_2\) in dimension three, the full relation admits 667 pairs whereas the \(t=0\) slice has only 415. Similarly, the two-dimensional published counts of idempotent–nilpotent *factorizations* concern fibers of a product, not pairs constrained by a sandwich zero relation. General representation-variety methods may still yield the present formula as a corollary after nontrivial calculations; no global historical-priority certification is claimed.

## Limitations
The theorem classifies the reduced rank strata and counts *top-dimensional* components, not all components or the nilpotent structure of the defining equation scheme. It does not classify similarity orbits, indecomposable modules, or deformations. General characteristic is included, and the finite-field count is exact, but the historical novelty comparison is necessarily bounded by accessible literature. No independent mathematical audit has been conducted.

## References
1. N. J. Richmond, *A Stratification for Varieties of Modules*, Bulletin of the London Mathematical Society 33 (2001), 565–577; DOI: 10.1112/S0024609301008189; publicly posted online 2001-10-23 at Cambridge Core, https://www.cambridge.org/core/journals/bulletin-of-the-london-mathematical-society/article/abs/stratification-for-varieties-of-modules/356511CE449511B57F1F1C79A2F5FAC7. Author-posted full text accessible at https://www.researchgate.net/publication/2607433_A_Stratification_For_Varieties_Of_Modules.
2. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (initial version 2002-11-19), https://arxiv.org/abs/math/0211293; Commentarii Mathematici Helvetici 79 (2004), 396–426.
