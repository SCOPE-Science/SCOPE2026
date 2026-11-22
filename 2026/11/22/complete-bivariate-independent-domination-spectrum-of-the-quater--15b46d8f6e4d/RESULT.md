# Complete bivariate independent-domination spectrum of the quaternary projective-plane incidence graph

## Finding

Let \(G\) be the 42-vertex bipartite point–line incidence graph of the Desarguesian plane \(\operatorname{PG}(2,4)\). Its two color classes \(P\) and \(L\) each contain 21 vertices. Write
\[
F_G(u,v)=\sum_{I\text{ maximal independent in }G}u^{|I\cap P|}v^{|I\cap L|}.
\]
An independent set is maximal precisely when it dominates every vertex outside it. The **complete bivariate polynomial** is
\[
\begin{aligned}
F_G(u,v)={}&u^{21}+v^{21}
+21(u^{16}v+uv^{16})\\
&+210(u^{12}v^2+u^2v^{12})
+1120(u^9v^3+u^3v^9)\\
&+210(u^8v^3+u^3v^8)
+2520(u^7v^4+u^4v^7)\\
&+3360(u^6v^4+u^4v^6)
+10080u^5v^5+168u^6v^6+105u^4v^4.
\end{aligned}
\]
Thus the independent-domination size polynomial is
\[
F_G(z,z)=105z^8+16800z^{10}+5460z^{11}+2408z^{12}
+420z^{14}+42z^{17}+2z^{21}.
\]
In particular, the plane has exactly 25,237 maximal independent sets, its independent domination number is 8, exactly 105 independent dominating sets attain this minimum, and the possible maximal-independent-set sizes are exactly \(8,10,11,12,14,17,21\). The minimum cardinality itself is a known consequence of earlier work, not a new claim here.

## Assumptions and scope

The underlying geometry is the Desarguesian projective plane over \(\mathbb F_4\), not an arbitrary projective plane of order four or an affine-plane incidence graph. In fact the order-four projective plane is unique up to isomorphism, but no classification theorem of planes is needed for the computation. A vertex of \(G\) is either a one-dimensional subspace of \(\mathbb F_4^3\) (a point) or the kernel of a nonzero covector (a line). A point and line are adjacent exactly when incident. There are 21 vertices of each kind, with degree 5.

The two variables retain point-side and line-side cardinalities, not arbitrary colors. The polynomial counts *labeled subsets of the 42 actual graph vertices*, not isomorphism classes or group orbits. The 17 displayed bidegrees list every nonzero coefficient; no omitted coefficient is presumed positive.

## Proof

**1. An exact one-shore parametrization.** For any finite bipartite incidence graph with point shore \(P\) and line shore \(L\), let \(S\subseteq P\), and put \(L_0(S)=\{\ell\in L:\ell\cap S=\varnothing\}\). Any maximal independent set \(I\) having point component \(S\) must contain **every** line vertex not adjacent to \(S\): otherwise such a line could be adjoined. It contains no other line. Therefore necessarily \(I=S\cup L_0(S)\). Conversely this is independent, and it is maximal if and only if every point outside \(S\) is adjacent to a line of \(L_0(S)\). Indeed, no further line can be adjoined by construction, and the condition excludes adding any further point. Hence the desired coefficients count the exact finite predicate
\[
\#\left\{S\subseteq P:\ |S|=a,\ |L_0(S)|=b,\ S\cup\bigcup_{\ell\in L_0(S)}\ell=P\right\}.
\]
No unlabeled or symmetry-class multiplicity is introduced.

**2. Explicit arithmetic model.** Represent the field as \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), with each element encoded by two bits. For the 63 nonzero vectors in \(\mathbb F_4^3\), normalize by multiplying by the inverse of the first nonzero coordinate and deduplicate. This gives exactly 21 representatives \(p_i\). Use the same 21 normalized vectors as nonzero covectors \(a_j\), defining \(\ell_j=\{p_i:a_j\cdot p_i=0\}\). In the supplied C++17 checker, finite-field multiplication is implemented directly by polynomial reduction modulo \(t^2+t+1\). The checker verifies \(|\ell_j|=5\) for every line, each point lies on 5 lines, and distinct lines meet in exactly one point; these checks also safeguard the model.

**3. Exhaustive finite identity.** Encode \(S\) as a 21-bit integer \(s\) ranging from 0 through \(2^{21}-1\). Encode each line as its five-one bitmask \(m_j\). Initialize the covered-point mask \(c=s\) and the eligible-line count \(b=0\). For each line mask \(m_j\), test \(s\mathbin{\&}m_j=0\); if yes, increment \(b\) and set \(c=c\mathbin{|}m_j\). Accept exactly when \(c=2^{21}-1\), incrementing the coefficient indexed by \((\operatorname{popcount}(s),b)\). By Step 1 this finite procedure enumerates *all and only* maximal independent sets, without missing any choice of line vertices. Exactly \(2^{21}=2{,}097{,}152\) distinct point masks are exhausted. The embedded program `checks/pg4_homogeneous.cpp` evaluates this deterministic finite sum with unsigned integer arithmetic and checks equality of every nonzero bidegree to the 17-term table below.

\[
\begin{array}{c|c|r}
|I\cap P|&|I\cap L|&\text{count}\\\hline
0&21&1\\1&16&21\\2&12&210\\3&8&210\\3&9&1120\\
4&4&105\\4&6&3360\\4&7&2520\\5&5&10080\\
6&4&3360\\6&6&168\\7&4&2520\\8&3&210\\
9&3&1120\\12&2&210\\16&1&21\\21&0&1
\end{array}
\]

These exact integer coefficients imply the stated bivariate polynomial, univariate specialization, total and set-size spectrum. In particular, there are no size-nine maximal independent sets and no sizes 13, 15, 16 or 18 through 20. This is a finite exhaustive proof of the specified 42-vertex case; it is not presented as an infinite-family enumeration.

## Verification

Both standalone verifiers are included and have been executed against their actual source files. The first constructs homogeneous point/covector coordinates in C++17 and exhaustively enumerates every point mask. The second, `checks/pg4_affine_numpy.py`, constructs an independent coordinate model using sixteen affine points, five points at infinity, twenty affine lines and the line at infinity. It evaluates the same all-subsets predicate using NumPy arrays, checks projective-plane incidence axioms, and independently produces the identical 17-term table. The TSV artifact `data/bivariate_spectrum.tsv` records the complete numerical certificate in the form `point_count<TAB>line_count<TAB>coefficient`, in ascending order of bidegree.

To reproduce from the package directory:

```bash
g++ -std=c++17 -O2 -Wall -Wextra checks/pg4_homogeneous.cpp -o pg4_check
./pg4_check
python3 checks/pg4_affine_numpy.py
```

The Python check requires NumPy; the C++ check needs only a conforming C++17 compiler and standard library. Both checkers verify the full polynomial, not a random or bounded sample of solutions.

## Relationship to prior work

Goldberg, Rajendraprasad and Mathew [1] introduced domination questions for designs and proved \(\gamma(G)=2q\) for projective-plane incidence graphs. Their Section 6 relates minimum dominating sets to independent domination and discusses an exhaustive Fano-plane check. Since \(q=4\), the minimum independent-domination cardinality 8 is part of the established foundation, not the novelty claim. They do not give the complete 17-bidegree spectrum for the quaternary plane.

Héger and Nagy [2] give structural restrictions on small minimal dominating sets, especially asymptotic restrictions at larger orders. Their explicit Problem 4.3 asks for the scale of the number of dominating, independent dominating and minimal dominating sets in projective planes. The exact finite polynomial here is a natural order-four benchmark, not a solution to that asymptotic problem. Hauschild, Ortiz and Vega [3], Lemma 1, exhibit general families of maximal independent sets in Levi graphs to establish a well-covered-dimension theorem. Their construction supplies examples and a lower bound but not this complete coefficient enumeration.

An exact classification of projective-plane point sets by parity-code *ghost* conditions in [4] also includes \(\operatorname{PG}(2,4)\), but the condition of meeting every line in fixed parity is distinct from coverage of all omitted points by lines disjoint from the selected set. Other indexed graph-family studies of maximal-independent-set polynomials and finite-plane studies of resolving, packing, matching and different domination variants have different objects or admissibility constraints; their results do not imply these 17 exact bidegrees as stated. The possibility of a previously unindexed exact census is a residual priority risk.

## Limitations

The result is deliberately finite and exact for \(\operatorname{PG}(2,4)\): it does not establish a general \(q\)-formula, counts for arbitrary non-Desarguesian planes, or a formula for minimal *non-independent* dominating sets. Exhaustive finite computation is justified here by a bijective reduction and full enumeration, not by treating a partial search as a proof. The originality assessment is based on inspected accessible primary literature and indexed-result searches, not on a mathematical proof of priority. Independent scholarly validation has not yet been performed.

## References

1. F. Goldberg, D. Rajendraprasad and R. Mathew, *Domination in Designs*, arXiv:1405.3436v1 (14 May 2014), especially Theorem 5.2, Proposition 6.3, Example 6.4. https://arxiv.org/pdf/1405.3436
2. T. Héger and Z. L. Nagy, *Dominating sets in projective planes* (2016 preprint), especially Theorem 1.5 and Problem 4.3. https://arxiv.org/abs/1603.02933 and https://nagyzoli.web.elte.hu/projdom-FIN-jav.pdf
3. J. Hauschild, J. Ortiz and O. Vega, *On the Levi Graph of Point-Line Configurations*, arXiv:1408.2879 (2014), especially Lemma 1 and Theorem 1. https://arxiv.org/pdf/1408.2879
4. M. L. Della Vedova, S. M. C. Pagani and S. Pianta, *Power sum polynomials and the ghosts behind them*, Journal of Geometry (2022/2023), especially Section 5.3. https://doi.org/10.1007/s00022-022-00662-2
