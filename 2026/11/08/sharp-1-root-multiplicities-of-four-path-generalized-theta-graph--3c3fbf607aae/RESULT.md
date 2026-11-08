# Sharp \(-1\)-root multiplicities of four-path generalized theta graphs

## Finding

Let \(G=\Theta(\ell_1,\ell_2,\ell_3,\ell_4)\) consist of four internally vertex-disjoint paths of integer edge lengths \(\ell_i\ge2\) between the same two nonadjacent vertices. Let \(P_G(x)=\sum_{S\subseteq V(G),\ S\text{ independent}}x^{|S|}\). The following is an exact classification of the multiplicity \(\mu_G\) of its root at \(x=-1\).

1. If the four path lengths do **not** represent all three residue classes modulo \(3\), then \(\mu_G=0\). If all three classes occur, then \(\mu_G\ge1\).
2. In the latter case, \(\mu_G\ge2\) precisely when, after reordering, the path lengths are \((3m,3n,3q+4,3q+2)\) with integers \(m,n\ge1\), \(q\ge0\). In every other root case, \(\mu_G=1\).
3. For this exceptional four-tuple, set
\[
Q(m,n,q)=q^2-(m+n)q-(m+n+2mn+1).
\]
Then \(\mu_G=2\) if \(Q\ne0\), and \(\mu_G=3\) if \(Q=0\). In particular, \(\mu_G\le3\) for **every** four-path generalized theta graph.

The smallest graph in this family having a double root has \(10\) vertices, attained by \(\Theta(2,3,3,4)\). The smallest graph having a triple root has \(61\) vertices, attained by \(\Theta(3,12,23,25)\). There are infinitely many triple-root examples:
\[
\Theta(3t,6t+6,12t+11,12t+13),\qquad t\ge1.
\]

## Assumptions and scope

The graph is finite, simple, undirected; each of its four paths has at least two edges, and they share only their two endpoints. Path lengths count **edges**, not internal vertices. The two branch vertices are nonadjacent. The independence polynomial counts the empty independent set and uses ordinary unit vertex weights. Multiplicity means order of vanishing in \(\mathbb Z[x]\) at \(-1\), not the multiplicity of a graph eigenvalue. All conclusions hold for every integer length tuple in the stated domain.

## Proof

**Endpoint decomposition.** Define the path independence polynomials by \(f_{-1}(x)=f_0(x)=1\), \(f_1(x)=1+x\), and \(f_j(x)=f_{j-1}(x)+x f_{j-2}(x)\) for \(j\ge2\). Given the selection status of the two branch vertices, the four path interiors contribute respectively \(f_{\ell_i-1}\), \(f_{\ell_i-2}\), or \(f_{\ell_i-3}\) as zero, one, or both endpoints are selected. Thus the exact identity is
\[
P_G(x)=\prod_{i=1}^{4}f_{\ell_i-1}(x)+2x\prod_{i=1}^{4}f_{\ell_i-2}(x)+x^2\prod_{i=1}^{4}f_{\ell_i-3}(x).
\tag{1}
\]
The convention \(f_{-1}=1\) accounts correctly for a path of length two when both endpoints are selected.

**Zero classification.** Put \(A_i=f_{\ell_i-1}(-1)\), \(B_i=f_{\ell_i-2}(-1)\), and \(C_i=f_{\ell_i-3}(-1)\). The recurrence gives \(f_j(-1)\) with period six: \(1,0,-1,-1,0,1\), starting at \(j=0\). Thus \(A_i=0\) precisely for \(\ell_i\equiv2\pmod3\), \(B_i=0\) for \(\ell_i\equiv0\pmod3\), and \(C_i=0\) for \(\ell_i\equiv1\pmod3\). If all three residues occur, every product in (1) vanishes at \(-1\). If exactly two residue classes occur, exactly one of the three products is nonzero. If only one residue class occurs, the surviving terms are \(2\varepsilon\) for class zero, \(-\varepsilon\) for class one, or \(-\varepsilon\) for class two, where \(\varepsilon\in\{-1,1\}\). In particular, none vanishes.

**Taylor calculation.** Write \(z=x+1\); for each length \(\ell\), set \(A=f_{\ell-1}(-1+z)\), \(B=f_{\ell-2}(-1+z)\), and \(C=f_{\ell-3}(-1+z)\). The following table lists coefficients \(c_0,c_1,c_2,c_3\) of \((-1)^k\) times each polynomial in \(z\), through degree three. Each row is an identity modulo \(z^4\). It follows directly by substituting \(x=-1+z\) into the stated path recurrence and inducting on \(k\). The allowed ranges are \(k\ge1\) for \(3k\) and \(3k+1\), and \(k\ge0\) for \(3k+2\).

| \(\ell\) | factor | \(c_0\) | \(c_1\) | \(c_2\) | \(c_3\) |
|---|---|---|---|---|---|
| \(3k\) | \(A\) | \(1\) | \(-2k\) | \(3k(k-1)/2\) | \(-k(k-1)(k-3)/2\) |
| \(3k\) | \(B\) | \(0\) | \(-k\) | \(3k(k-1)/2\) | \(-k(k-1)(k-2)\) |
| \(3k\) | \(C\) | \(-1\) | \(k-1\) | \(k-1\) | \(-(k-2)(k-1)(k+1)/2\) |
| \(3k+1\) | \(A\) | \(1\) | \(-k\) | \(-k\) | \(k(k-1)(k+2)/2\) |
| \(3k+1\) | \(B\) | \(1\) | \(-2k\) | \(3k(k-1)/2\) | \(-k(k-1)(k-3)/2\) |
| \(3k+1\) | \(C\) | \(0\) | \(-k\) | \(3k(k-1)/2\) | \(-k(k-1)(k-2)\) |
| \(3k+2\) | \(A\) | \(0\) | \(k+1\) | \(-3k(k+1)/2\) | \(k(k-1)(k+1)\) |
| \(3k+2\) | \(B\) | \(1\) | \(-k\) | \(-k\) | \(k(k-1)(k+2)/2\) |
| \(3k+2\) | \(C\) | \(1\) | \(-2k\) | \(3k(k-1)/2\) | \(-k(k-1)(k-3)/2\) |

Let the four residue-class counts be \((r_0,r_1,r_2)\). For a zero at \(-1\), these counts are a permutation of \((2,1,1)\). Up to an overall sign \(\varepsilon\), the coefficient of \(z\) in (1) is: \(q+1-p\) for \((r_0,r_1,r_2)=(2,1,1)\) with lengths \((3m,3n,3p+1,3q+2)\); \(q+1+2m\) for counts \((1,2,1)\); and \(2m+p\) for counts \((1,1,2)\). Here \(m,n,p\ge1\) and \(q\ge0\) designate the relevant lengths. The last two expressions are strictly positive; the first is zero precisely when \(p=q+1\), giving the exceptional tuple in the statement.

For that tuple put \(\varepsilon=(-1)^{m+n+1}\). Expanding (1) with the table gives the exact Taylor coefficients
\[
[z^0]P_G(-1+z)=[z^1]P_G(-1+z)=0,\quad [z^2]P_G(-1+z)=\varepsilon Q(m,n,q).
\tag{2}
\]
When \(Q(m,n,q)=0\), the cubic coefficient simplifies using this quadratic relation to
\[
[z^3]P_G(-1+z)=-2\varepsilon\bigl(mn+(m+n)q+m+n+q+1\bigr)\ne0.
\tag{3}
\]
Since all parameters are nonnegative with \(m,n\ge1\), the expression in parentheses is strictly positive. Equations (2)--(3) prove the precise double/triple classification and the universal upper bound three.

**First occurrences and an infinite series.** In the exceptional family the number of vertices is \(N=3(m+n+2q)+4\). It is at least \(10\), and at \((m,n,q)=(1,1,0)\) the quadratic coefficient is nonzero. For a triple root, \(Q=0\) implies \(q\ge m+n+2\): indeed, \(q(q-m-n)=m+n+2mn+1\), whose right side exceeds \(m+n+1\). If \(N<61\), then \(m+n+2q\le18\), hence \(m+n\le4\). For the four unordered pairs \((m,n)=(1,1),(1,2),(1,3),(2,2)\), the discriminants of the quadratic in \(q\) are respectively \(24,41,60,68\), none a square. At \((m,n,q)=(1,4,7)\), \(Q=0\) and \(N=61\). Finally, \((m,n,q)=(t,2t+2,4t+3)\) satisfies \(Q=0\) identically for every \(t\ge1\), yielding the asserted infinite family.

## Verification

The standalone Python 3 script `artifacts/verify.py` uses only the standard library and contains an independent graph construction plus a deletion-based independence-polynomial computation, rather than relying solely on (1). Run it with `python3 artifacts/verify.py` from the package root. It compares 63 complete small-graph polynomials, verifies the multiplicity classification for 5,985 sorted four-length tuples, checks the exceptional Taylor coefficients, tests the infinite family at fourteen values, and checks the finite sharpness range below 61 vertices. The observed final output was `VERIFY_OK`. These tests are corroboration; the unrestricted classification is proved by (1)--(3).

## Relationship to prior work

Bhardwaj, Chau, Ikram, Lather, Nanjangud and Venugopal (arXiv:2607.08480, originally released 9 July 2026) initiate systematic study of root multiplicity at \(-1\), including trees, pseudoforests, and line graphs of forests; those statements do not determine the order of vanishing on four-path generalized theta graphs. Levit and Mandrescu (arXiv:0904.4819) proved the general bound \(|P_G(-1)|\le2^{\nu(G)}\), where \(\nu\) is the cyclomatic number; an upper bound on **value** does not determine multiplicity. Przytycki and Silvero (2024, DOI below), Example 3.8, study homotopy types of independence complexes of **three-path** theta subdivisions; this does not determine derivatives of the independence polynomial for four-path theta graphs. All these stronger/different aspects are credited rather than treated as new. The source comparison does not constitute a proof of global priority.

## Limitations

The theorem applies to exactly four paths of lengths at least two sharing their endpoints, with unweighted independent sets. It does not determine multiplicities for arbitrary series-parallel graphs or more than four parallel paths. The numerical and symbolic checks are not external mathematical certification. Unindexed or inaccessible prior literature could contain an equivalent theorem; historical priority remains provisional.

## References

1. O. P. Bhardwaj, T. Chau, S. Ikram, G. Lather, V. Nanjangud and C. Venugopal, *Multiplicity of negative one of independence polynomials of graphs*, arXiv:2607.08480v1 (first posted 2026-07-09), https://arxiv.org/abs/2607.08480 .
2. V. E. Levit and E. Mandrescu, *The independence polynomial of a graph at -1*, arXiv:0904.4819 (2009), https://arxiv.org/abs/0904.4819 .
3. J. H. Przytycki and M. Silvero, *Khovanov homology, wedges of spheres and complexity*, Rev. R. Acad. Cienc. Exactas Fis. Nat. Ser. A Mat. 118, 102 (2024), https://doi.org/10.1007/s13398-024-01594-z , Example 3.8.
