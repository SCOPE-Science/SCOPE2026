# Exact two-rail entropy and closed-island counts for the odd-component shift

## Finding

The natural two-row restriction of the odd-component subshift has an **exact algebraic entropy**. With the convention of entropy per whole two-cell column,
\[
h_{\mathrm{top}}(X_2)=\log\lambda,
\qquad
\lambda^5-4\lambda^4+3\lambda^3-5\lambda^2+2\lambda+1=0,
\qquad
\lambda\approx3.49756499717934,
\]
where \(\lambda\) is the unique real root larger than \(3\). Thus entropy per occupied-or-empty cell is \(\frac12\log\lambda\approx0.62603350564085\).

For every integer \(n\ge0\), let \(a_n\) be the number of assignments of zeros and ones to the vertices of the open ladder \(P_n\square K_2\), such that every connected component induced by vertices assigned one has *odd* cardinality. The empty ladder has \(a_0=1\). Then
\[
\sum_{n\ge0}a_nz^n
=\frac{1-z+2z^2-3z^3-z^4}{1-4z+3z^2-5z^3+2z^4+z^5}.
\]
In particular, \((a_n)_{n=0}^{8}=(1,3,11,37,127,445,1559,5451,19061)\). The generating function yields a homogeneous order-five recurrence for \(n\ge5\) and a Perron asymptotic \(a_n\sim C\lambda^n\) for a constant \(C>0\).

## Assumptions and scope

Let \(L=\mathbb Z\times\{0,1\}\), with nearest-neighbor adjacency: vertical neighbors in each column and horizontal neighbors in the same row of consecutive columns. A configuration \(x\in\{0,1\}^L\) is **admissible** if every *finite* connected component of the induced subgraph on vertices with \(x=1\) has odd cardinality. Infinite components are unrestricted by this oddness rule. Let \(X_2\) be the resulting closed, horizontally translation-invariant space, and let \(\sigma\) shift each column left. All logarithms are natural, and one entropy step means one two-vertex column, not one cell.

The finite-ladder count \(a_n\) imposes oddness also on components touching either finite end. It is **not** defined as the number of all length-\(n\) blocks in \(X_2\); the proof shows those two sequences have the same exponential growth rate. Edges outside \(P_n\square K_2\) are absent, so no periodic wraparound is imposed.

## Proof

**1. Finite-state boundary rule.** Encode a column by the occupied-row mask \(m\in\{0,1,2,3\}\), where the two low bits correspond to the two rows. An occupied column has one connected component meeting the current boundary, because mask \(3\) contains a vertical edge; masks \(1\) and \(2\) contain one vertex. Hence at any cut **at most one** occupied component can meet the boundary. It suffices to record its accumulated size modulo two.

Use seven states, in the order
\[
Z,\ U_0,\ U_1,\ D_0,\ D_1,\ B_0,\ B_1,
\]
where \(Z\) is the empty column and \(U,D,B\) denote respectively upper-only, lower-only, and both occupied; the subscript is the running parity (zero for even, one for odd). If the next column mask intersects the current mask, the active component persists and its parity changes by the number of occupied sites of the new column modulo two. If the masks are disjoint, the old component is closed and the transition is permitted **exactly when** its parity is odd; the new component, if any, starts with parity equal to the size of the new mask modulo two. The same closure rule applies to a following zero column.

The resulting adjacency matrix, with rows and columns in the state order above, is
\[
M=\begin{pmatrix}
1&0&1&0&1&1&0\\
0&0&1&0&0&1&0\\
1&1&0&0&1&0&1\\
0&0&0&0&1&1&0\\
1&0&1&1&0&0&1\\
0&0&0&0&1&1&0\\
1&1&0&1&0&0&1
\end{pmatrix}.
\]
A finite mask word of length \(n\) has all occupied components odd if and only if its unique state path beginning at \(Z\) can end by a permitted transition back to \(Z\). Therefore
\[
a_n=(M^{n+1})_{ZZ}.
\]
Uniqueness of the path follows because the starting state and next mask determine the next parity whenever an arrow exists. Equivalence follows from the absence of distinct frontier components in a width-two ladder.

**2. Symmetry reduction and exact generating function.** Interchanging the two rows swaps \(U_0\leftrightarrow D_0\) and \(U_1\leftrightarrow D_1\), fixing the other three states. The induced nonnegative matrix on symmetric vectors, in order \(Z,O_0,O_1,B_0,B_1\), is
\[
B=\begin{pmatrix}
1&0&2&1&0\\
0&0&1&1&0\\
1&1&1&0&1\\
0&0&2&1&0\\
1&2&0&0&1
\end{pmatrix}.
\]
The same boundary counts satisfy \(a_n=(B^{n+1})_{ZZ}\). Direct exact determinant and cofactor computation gives
\[
\det(tI-B)=t^5-4t^4+3t^3-5t^2+2t+1
\]
and
\[
\sum_{n\ge0}(B^{n+1})_{ZZ}z^n
=\big[B(I-zB)^{-1}\big]_{ZZ}
=\frac{1-z+2z^2-3z^3-z^4}{1-4z+3z^2-5z^3+2z^4+z^5}.
\]
Every entry of \(B^2\) is positive, so \(B\) is primitive. Perron–Frobenius theory thus supplies a simple positive spectral radius \(\lambda\) and \(a_n\sim C\lambda^n\) with \(C>0\). The polynomial is negative at \(3\) and positive at \(4\); its first derivative is strictly positive on \([3,\infty)\), as follows from its second and third derivatives there. This verifies that its unique real root above \(3\) equals the spectral radius: any root above \(3\) cannot exceed the spectral radius, and the latter is a positive root.

**3. Equivalence of entropy growth.** Let \(L_n\) be the number of length-\(n\) column words appearing in a bi-infinite admissible configuration. Every finite-ladder pattern counted by \(a_n\) extends to an admissible configuration by zero columns, so \(a_n\le L_n\).

Conversely, a word appearing in \(X_2\) cannot contain an even-sized occupied component entirely separated from both ends of that word, since such a component could never connect to anything outside. At most one occupied component can touch each of its two boundary columns. If one such component has even size in the finite word, extend it by an occupied vertex in one adjacent new end column, chosen to share a row; if it is already odd, use zeros at that end. If the same component touches both ends, correct it at only one end. Thus every appearing word can be embedded in a *unique, canonically chosen* legal finite pattern of length \(n+2\) by adding one column on each side; different middle words give different padded patterns. Hence \(L_n\le a_{n+2}\).

The sandwich \(a_n\le L_n\le a_{n+2}\), together with the preceding Perron asymptotic, proves
\[
 h_{\mathrm{top}}(X_2)=\lim_{n\to\infty}n^{-1}\log L_n=\log\lambda.
\]

## Verification

The accompanying `checker.py` constructs \(M\) from the four exact parity rules rather than from the displayed matrix, confirms the row-symmetric intertwining identity and characteristic polynomial over the integers, checks the exact rational resolvent, and proves primitivity by testing positivity of \(M^3\). An independent component-flood-fill enumerates **all** \(4^n\) finite-ladder patterns for each \(0\le n\le8\), and matches \((M^{n+1})_{ZZ}\) and \((B^{n+1})_{ZZ}\) at each length. Those finite checks support the explicit formulas; the proof of the statements for all \(n\) and the entropy limit is mathematical, not based on finite enumeration.

Run `python checker.py` with Python 3 and SymPy. The script prints the verified initial counts and a success assertion.

## Relationship to prior work

The connected-component parity constraint, the distinction between one- and higher-dimensional sofic shifts, and the qualitative planar odd-shift example appear in A. Callard's public 2025 thesis, Chapter 7. That work describes soficity but does not give the two-rail exact generating function or the fifth-degree entropy constant in its odd-shift discussion. The present calculation concerns the first nontrivial transverse width: it makes the parity-frontier mechanism quantitative rather than re-proving planar soficity.

The 2026 theorem of Wu and Zhang concerns finiteness and Bernoulli structure of maximal-entropy measures from forbidden-word entropy gaps, rather than these particular cylinder counts. The subsequent study by Gladkov and Mitrofanov treats nonsoficity in dimensions at least three and a qualified planar obstruction, but no two-rail entropy formula is stated in its accessible text. The older unpublished odd-shift work of Cassaigne is a remaining priority risk, rather than evidence of an exact entropy calculation.

## Limitations

The result is **only** for a two-row ladder with open vertical boundary and nearest-neighbor connectivity. The two-row entropy is per column; divide by two for an entropy per cell. It does not determine the full \(\mathbb Z^2\) entropy, planar soficity, any three-or-more-row strip, or periodic-wraparound word counts. The source thesis is publicly dated by its June 24, 2025 defense, while the accessible manuscript carries an August 16, 2025 version date; the defense date is used as the earliest publicly evidenced event, not as the manuscript's revision date. Novelty is assessed against inspected material only and has not undergone independent validation. Cassaigne's unpublished original source could contain previously unlocated related enumerations.

## References

1. Antonin Callard, *Soficity of multidimensional subshifts*, PhD thesis, Université de Caen Normandie (public defense June 24, 2025), Chapter 7, especially page 54. https://www.acallard.net/publications/thesis.pdf ; institutional record: https://doi.org/10.70675/2f62f620z4bccz465dzb2c1z6a3cc5634f2a .
2. Xinxing Wu and Xu Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts*, arXiv:2611.03758 (first submitted November 2, 2026), https://arxiv.org/abs/2611.03758 .
3. Nikita Gladkov and Ivan Mitrofanov, *The Odd Shift is not sofic in dimensions \(d\ge3\)*, arXiv:2611.21008 (first submitted November 16, 2026), https://arxiv.org/html/2611.21008v1 . This later supporting source is **not** the date anchor of the present result.
4. Julien Cassaigne, *Odd shift* (2010), unpublished result cited in Callard's thesis, reference [Cas10]; its full derivation was unavailable for comparison.
