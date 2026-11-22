# A sharp nearest-edge transition and mixed diameters in symmetric Monge simplices

## Finding
Let \(\mathcal S_n\) be the simplex of symmetric entrywise-nonnegative \(n\times n\) Monge matrices with sum of all entries equal to one, using full-matrix Frobenius distance, for each integer \(n\ge2\). Write \(\delta_n\) for the smallest edge length and \(D_n\) for its Euclidean diameter. All vertex pairs are edges, since \(\mathcal S_n\) is a simplex.

Its squared diameter is
\[
D_n^2=\begin{cases}\frac12,&n=2,\\[2pt]\frac12+\frac{n+1}{2n^2},&n\ge3.\end{cases}
\]
For \(n\ge3\), there are **exactly \(n-2\) diametral pairs**: the unique one-by-one corner-block vertex is paired with any one of the \(n-2\) interior additive-star vertices. For \(n=2\), the unique diametral pair is the pair of additive-star vertices.

The minimum squared edge length has a sharp change of geometric type at \(n=5\):
\[
\delta_n^2=\begin{cases}
\displaystyle \frac{2n-1}{2n^2(n-1)},&2\le n\le4,\\[4pt]
\displaystyle\frac1{2M_n},&n\ge5,
\end{cases}\qquad
M_n=\max_{1\le b\le n-2}(n-b-1)b(b+1).
\]
For \(2\le n\le4\), precisely two shortest edges join the two endpoint additive-star vertices to opposite longest corner blocks. For \(n\ge5\), the shortest edges lie **entirely inside the hollow symmetric Monge subsimplex**, joining the adjacent corner-block vertices
\[
H_{a,n-a-1}\longleftrightarrow H_{a,n-a},\qquad
H_{n-a-1,a}\longleftrightarrow H_{n-a,a},
\]
where \(a=n-b-1\) and \(b\) maximizes \(M_n\). There are exactly four such edges when \(n\equiv2\pmod3\), and exactly two otherwise. Consequently
\[
\delta_n^2\sim\frac{27}{8n^3},\qquad
\frac{D_n}{\delta_n}\sim\frac{2}{3\sqrt3}n^{3/2}.
\]
The sharp crossover refers to *the full symmetric simplex*; the hollow-only shortest-edge calculation is not claimed to be new.

## Assumptions and scope
For \(i<I\) and \(j<J\), the Monge inequality is \(c_{ij}+c_{IJ}\le c_{iJ}+c_{Ij}\). Distances are taken in all \(n^2\) real entries, so each symmetric off-diagonal entry is counted twice in the squared Frobenius norm. The ambient affine hyperplane is the sum-one hyperplane; no dimension-dependent rescaling or coordinate weighting is used.

For positive \(a,b\) with \(a+b\le n\), define \(H_{a,b}\) to equal \(1/(2ab)\) on the top-right \(a\times b\) rectangle and its transpose and zero elsewhere. For \(1\le i\le n\), define \(S_i=(e_i\mathbf1^\top+\mathbf1e_i^\top)/(2n)\); in particular its \((i,i)\) entry is \(1/n\). These are exactly the \(n(n+1)/2\) vertices of \(\mathcal S_n\), as established by Erickson and Kretschmann (2023), Proposition 4.1; Proposition 4.2 proves the simplex statement. Its hollow sub-simplex has precisely the \(H_{a,b}\) vertices.

## Proof
**1. Exact Gram data.** Directly counting the support coordinates gives
\[
\|H_{a,b}\|_F^2=\frac1{2ab},\qquad
\|S_i\|_F^2=\frac{n+1}{2n^2},\qquad
\langle H_{a,b},H_{c,d}\rangle_F=\frac{\min(a,c)\min(b,d)}{2abcd}.
\]
The two upper-right rectangles overlap in \(\min(a,c)\min(b,d)\) entries, with an identical transposed overlap; upper-right and lower-left rectangles from different admissible blocks never overlap because both block-size sums are at most \(n\). Also, for distinct \(i,j\), \(\|S_i-S_j\|_F^2=1/n\), and
\[
\|S_i-H_{a,b}\|_F^2=\frac{n+1}{2n^2}+\frac1{2ab}-\frac{\mathbf1_{i\le a}}{na}-\frac{\mathbf1_{i>n-b}}{nb}.\tag{1}
\]
The two indicator cases in (1) are disjoint.

**2. Diameter.** Every pair of distinct hollow vertices has squared distance strictly below \(1/2\): if neither is \(H_{1,1}\), each squared norm is at most \(1/4\) and their inner product is positive; if one is \(H_{1,1}\), the exact value for the other \(H_{a,b}\) is \(1/2-1/(2ab)\). Distinct stars are separated by squared distance \(1/n\). By (1), a mixed squared distance never exceeds \(1/2+(n+1)/(2n^2)\), with equality exactly when \(a=b=1\) and the star index \(i\) belongs to neither endpoint, i.e. \(2\le i\le n-1\). Such indices exist for \(n\ge3\). In dimension two, direct comparison of its three vertices gives star–star squared distance \(1/2\) and two mixed squared distances \(3/8\).

**3. All mixed-edge minima.** Set \(s_n=(2n-1)/(2n^2(n-1))\). If a star index lies in neither support endpoint block, equation (1) is greater than \(s_n\), since \((n+1)/(2n^2)\ge s_n\) for \(n\ge2\). For \(i\le a\), the expression in (1) strictly decreases as \(b\) increases, so its minimum at fixed \(a\) occurs at \(b=n-a\), where it equals
\[
\frac{n+1}{2n^2}+\frac1{2n}\left(\frac1{n-a}-\frac1a\right).
\]
This expression strictly increases with \(a\in\{1,\ldots,n-1\}\), hence its unique minimum has \(a=1,b=n-1,i=1\). Transposition gives the only other minimizer \(a=n-1,b=1,i=n\). The common minimum is \(s_n\), for every \(n\ge2\).

**4. All hollow-edge minima.** For nested indices \(a\le c,b\le d\), distinct hollow vertices have squared distance \(1/(2ab)-1/(2cd)\). Increasing at least one integer index by one while respecting \(c+d\le n\) gives a lower bound by one of the one-step increments \(1/[2ab(b+1)]\) or \(1/[2a(a+1)b]\). Their global minimum is \(1/(2M_n)\), attained by the adjacent block pairs in the finding.

For crossing indices \(a<c,b>d\), the top-right support of the first matrix has \(a(b-d)\) entries absent from the second, and the second has \((c-a)d\) entries absent from the first. Including transposes, these disjoint exclusive entries give
\[
\|H_{a,b}-H_{c,d}\|_F^2
\ge\frac{b-d}{2ab^2}+\frac{c-a}{2c^2d}
\ge\frac1{2ab^2}+\frac1{2c^2d}\ge\frac1{2M_n}.
\]
Indeed \(b\ge2,c\ge2\), and the feasible one-step blocks imply \(ab^2\le2a(b-1)b\le2M_n\) and \(c^2d\le2(c-1)cd\le2M_n\). Equality cannot occur: it would require \(b=c=2\), hence \(a=d=1\), but then \(M_n\ge (n-2)(n-1)>2\) for \(n\ge4\). Thus only nested one-step pairs minimize for \(n\ge4\).

The one-step cubic \(g_n(b)=(n-b-1)b(b+1)\) obeys
\[
g_n(b+1)-g_n(b)=(b+1)(2n-4-3b).
\]
It has one maximizing \(b\) except when \(n\equiv2\pmod3\), where two consecutive values tie. These give precisely the claimed two or four unordered edges. At \(n=3\), all three hollow edges have squared distance \(1/4\).

**5. Exact crossover and asymptotics.** For \(n=3,4\), \(s_n=5/36,7/96\) is strictly below the hollow minimum \(1/4,1/12\), respectively. For \(n\ge5\), the feasible choice \(a=2,b=n-3\) proves \(M_n\ge2(n-3)(n-2)\), so
\[
\frac1{2M_n}\le\frac1{4(n-3)(n-2)}<s_n,
\]
where the strict comparison reduces, upon writing \(n=t+5\), to positivity of \(3t^3+24t^2+49t+8\) for integers \(t\ge0\). For \(n=2\) there is only one hollow vertex, and the two mixed edges are shortest. The cubic maximum satisfies \(M_n\sim4n^3/27\), while \(D_n^2\to1/2\), yielding the asymptotic ratio.

## Verification
Run `python verify.py` using Python 3's standard library. The checker constructs all vertex matrices *from their coordinate definitions*, independently forms their exact rational pairwise Frobenius distances, compares them with the Gram formulas, and checks both extremal values and **complete sets of extremizing vertex pairs** for every integer \(2\le n\le12\). It also verifies sum-one normalization and every adjacent Monge inequality for every constructed vertex. The recorded terminal marker is `SYMMETRIC_MONGE_EUCLIDEAN_EXTREMA_EXACT_PASS`. These finite checks are supplementary; the preceding proof handles every integer dimension.

## Relationship to prior work
Erickson and Kretschmann (2023) proved the symmetric and hollow symmetric Monge polytopes are simplices, supplied the vertex matrices, and computed normalized volume. The present claim does not reassert those results as novel. A previous hollow-only exact shortest-edge classification gives the \(1/(2M_n)\) term, but does not determine the full symmetric simplex's star–block distances, its sharp dimension-five switch in shortest-edge type, or its exclusively mixed diametral pairs. Related existing work on the hollow simplex's incenter concerns a different invariant. The contribution is the **mixed-family extremal metric geometry and transition** in the standard Frobenius realization, not the hollow-only calculation.

## Limitations
The statements concern the specified normalized full symmetric Monge simplex and its **vertex-pair** Euclidean distances. They do not give the minimum Euclidean separation of arbitrary distinct points (which is zero), the minimum width, the inradius, or a claim about arbitrary nonsymmetric Monge polytopes. The full spectral distribution of all edge lengths is not collapsed into a single closed histogram; the Gram formulas determine it algorithmically. Historical priority remains subject to unindexed equivalent results or older cone studies not exhaustively searched.

## References
1. W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522 (first posted 2023-11-13), especially Sections 3–4 and Propositions 4.1–4.2. https://arxiv.org/abs/2311.07522
2. R. Rudolf and G. J. Woeginger, foundational extremal-ray description of nonnegative Monge cones (1995), as referenced in Erickson–Kretschmann, Section 3. The present proof uses the later explicit normalized vertex formulation.
