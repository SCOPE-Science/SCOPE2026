# Parity reversal of two-landmark anonymity in folded cubes

## Finding

For each integer \(n\ge4\), let \(F_n\) be the antipodal quotient of the binary cube \(Q_n\). A vertex is a class \([x]=\{x,\overline{x}\}\), and the graph distance is \(d([x],[y])=\min\{d_H(x,y),n-d_H(x,y)\}\). For a two-vertex landmark set \(S=\{a,b\}\), partition \(V(F_n)\setminus S\) by the ordered pair \((d(v,a),d(v,b))\), and denote the size of its smallest nonempty class by \(k(S)\). This is the exact \(k\) for which \(S\) is a \(k\)-antiresolving set.

Write \(h=d(a,b)\), where \(1\le h\le\lfloor n/2\rfloor\). Then

\[
k(S)=\begin{cases}
n-1,&h=1,\\
2,&(n,h)=(4,2),\\
n,&n\ge6\text{ even and }h=n/2,\\
h,&2\le h<n/2.
\end{cases}
\]

In particular, the largest anonymity class minimum obtainable by **exactly two** landmarks is \(n-1\) for odd \(n\ge5\) and for \(n=4\), attained exactly by adjacent landmarks; it is \(n\) for even \(n\ge6\), attained exactly by diametral landmarks. Thus the optimal two-landmark geometry reverses with dimension parity. The number of unordered optimal landmark pairs is \(n2^{n-2}\) for odd \(n\ge5\) and for \(n=4\), and \(2^{n-3}\binom{n}{n/2}\) for even \(n\ge6\).

More strongly, for every \(n\ge4\) and separation \(h\), the following explicit polynomial is the **complete** joint distance-profile enumerator of the unmarked vertices:

\[
\begin{aligned}
P_{n,h}(u,v)={}&\frac12\sum_{i=0}^{h}\sum_{j=0}^{n-h}\binom hi\binom{n-h}{j}
 u^{\min\{i+j,n-i-j\}}
 v^{\min\{h-i+j,n-h+i-j\}}\\
&-u^hv^0-u^0v^h.
\end{aligned}
\]

Its coefficient at \(u^rv^s\) is the number of vertices outside \(S\) with distances \((r,s)\). In particular, the polynomial is independent of the chosen pair once its graph distance \(h\) is fixed.

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted. The quotient identifies complementary binary words, **not** the separate model formed by merely marking antipodal edges of the original cube without identification; these standard models are graph-isomorphic after the usual dimension convention is fixed, but the vertex counts must agree. The two sensor vertices are distinct, fixed, and excluded from the signature classes. The \(k\) value is the minimum over **nonempty** classes; no class with an impossible signature is included in the minimum. Both sensors have separate ordered coordinates in each distance signature; swapping them only interchanges polynomial variables. The theorem does not assert the full \(k\)-metric antidimension over landmark sets of arbitrary sizes.

## Proof

**Distance enumerator.** Choose binary representatives of the two sensors so that \(a=[0^n]\) and \(b=[1^h0^{n-h}]\). For a test word \(x\), suppose \(i\) of the first \(h\) positions and \(j\) of the remaining \(n-h\) positions are equal to one. There are exactly \(\binom hi\binom{n-h}j\) such words. Their Hamming distances to the chosen sensor representatives are \(i+j\) and \(h-i+j\). Passage to the quotient replaces each by the smaller of that distance and its complement to \(n\). Each quotient vertex is represented twice in the complete word sum, including when its coordinate-count pattern is fixed by complement. Hence dividing the sum by two and deleting one copy of each of the two marked quotient vertices gives the stated polynomial. This proves every coefficient, without a finite-search assumption.

**Uniform lower bounds away from the middle layer.** Complementing a word transforms its count pair \((i,j)\) into \((h-i,n-h-j)\). Its coordinate-count orbit under the pointwise stabilizer of the sensor representatives therefore contributes \(\binom hi\binom{n-h}j\) quotient vertices to a signature class, except that a self-complementary count pair contributes half that amount. The self-complementary case can only arise for \(n\) even with \(h\) and \(n-h\) both even. The four corner pairs \((0,0),(h,n-h),(h,0),(0,n-h)\) represent the two sensors and have been deleted. Every other count pair has \(0<i<h\) or \(0<j<n-h\), and so has multiplicity at least \(\min\{h,n-h\}=h\), unless self-complementary. If \(2\le h<n/2\), the self-complementary multiplicity is \(\frac12\binom{h}{h/2}\binom{n-h}{(n-h)/2}\), where this case is possible only when both quantities below the binomial signs are even. Here \(h\ge2\) and \(n-h\ge h+2\), so the product is at least \(\frac12 h(n-h)\ge h\). Thus every nonempty class has at least \(h\) members.

For \(2\le h<n/2\), exactly \(h\) neighbours of \(a\) arise by toggling one of the \(h\) coordinates in which the representatives of \(a,b\) differ. These have signature \((1,h-1)\). Any other neighbour of \(a\) has second distance \(\min\{h+1,n-h-1\}\), strictly larger than \(h-1\) because \(n>2h\). Therefore this class has exactly \(h\) vertices and \(k(S)=h\).

If \(h=1\), the only count pairs with a binomial factor equal to one are the sensor corners. Every other quotient count orbit contributes at least \(\binom{n-1}{1}=n-1\). Exactly \(n-1\) neighbours of \(a\) other than \(b\) have second distance two (for \(n\ge4\)), and there is no further neighbour with that signature. Hence \(k(S)=n-1\).

**The even middle layer.** Set \(n=2m\) and \(h=m\), with \(m\ge3\). The distance signature of a count pair is
\[
\bigl(\min\{i+j,2m-i-j\},\ m-|i-j|\bigr).
\]
It is invariant under exchanging \(i\) and \(j\), in addition to simultaneous complementation \((i,j)\mapsto(m-i,m-j)\). If both \(i,j\) are interior, \(1\le i,j\le m-1\), the associated quotient count orbit has at least \(m^2\ge2m\) vertices. The only exception in the counting formula is the self-complementary pair \(i=j=m/2\) when \(m\) is even: its size is \(\frac12\binom m{m/2}^2\), at least \(2m\) for all even \(m\ge4\). If exactly one of \(i,j\) is an endpoint, the orbit contributes at least \(m\) vertices, and its distinct partner obtained by swapping \(i,j\) contributes another at least \(m\) to the same distance class. If both are endpoints, the associated vertices are the deleted sensors. Thus every nonempty distance class has size at least \(2m\). All \(2m\) neighbours of \(a\) have second distance \(m-1\) and therefore give a class of exactly \(2m\). Hence \(k(S)=2m=n\).

When \(n=4\) and \(h=2\), the complete profile is \(P_{4,2}(u,v)=4uv+2u^2v^2\), so \(k(S)=2\); the central self-complementary count pair is the small-dimension exception. For \(n=4,h=1\), the profile is \(3uv^2+3u^2v\), so \(k(S)=3\).

**Sharp placement and its count.** For odd \(n\), every nonadjacent pair has \(k(S)=h\le\lfloor n/2\rfloor<n-1\). For even \(n\ge6\), a diametral pair has \(k(S)=n\), exceeding the adjacent value \(n-1\) and all shorter nonadjacent values \(h\le n/2-1\). The \(n=4\) exception was checked above. Since \(F_n\) has \(2^{n-1}\) vertices and degree \(n\), it has \(n2^{n-2}\) unordered adjacent pairs. For even \(n\), each vertex has \(\frac12\binom{n}{n/2}\) diametral neighbours in the quotient, yielding \(2^{n-3}\binom{n}{n/2}\) unordered diametral pairs. This completes all claims.

## Verification

The standalone `folded_formula_check.py` evaluates the exact double-binomial formula for every \(n=4,\ldots,80\) and every possible separation, checking coefficient nonnegativity, total count and the claimed minima. The independent `folded_direct_check.py` constructs quotient vertices as binary words with a fixed first bit, calculates quotient distances directly, checks every unordered landmark pair for \(4\le n\le8\), and checks representatives of all separation classes for \(9\le n\le14\). These calculations agree with the proof, including the exceptional \(n=4\) case. Both programs use only the Python standard library. Run them with `python3 folded_formula_check.py` and `python3 folded_direct_check.py`. Finite computational checks support but are not substituted for the all-dimension argument.

## Relationship to prior work

Fernández, Kuziak, Muñoz Márquez and González Yero (2023, arXiv:2304.00849), Definitions 1–2 and Section 3, study metric antidimension and anonymity for cylinders, tori and **two-dimensional Hamming graphs**. Their formula does not cover antipodal quotients, nor does it determine the separation-dependent profiles or parity reversal here. Background descriptions of folded cubes establish their quotient construction, distance transitivity and elementary graph parameters, but not this landmark-fibre theorem. Work on two individually marked ordinary binary hypercubes concerns the **unquotiented** graph and has a different distance-vector partition; the unquotiented distance partition alone does not state the folded two-landmark optimum; proving the parity reversal requires analyzing collisions after antipodal identification. Research on the ordinary metric dimension, spectral properties and distance matrices of folded cubes likewise does not provide the claimed minimum size of every joint two-landmark class. The claim is provisional with respect to unpublished or poorly indexed historical calculations.

## Limitations

The statement is about **exactly two distinct landmarks**; it is not a formula for \(\operatorname{adim}_k(F_n)\) when arbitrary numbers of landmarks may be chosen. It assumes the antipodal quotient, not an arbitrary covering or folded grid, and \(n\ge4\). The term "anonymity" here denotes exact graph-theoretic equality of distance signatures, not a guarantee about practical privacy attacks in networks with additional identifying data. The argument is mathematical and the checks are reproducible, but independent audit and exhaustive historical-priority certification have not occurred.

## References

- E. Fernández, D. Kuziak, M. Muñoz Márquez, I. G. Yero, *On the (k,ℓ)-anonymity of networks via their k-metric antidimension*, arXiv:2304.00849v1, first public 2023-04-03; https://arxiv.org/abs/2304.00849.
- E. W. Weisstein, *Folded Cube Graph*, MathWorld; https://mathworld.wolfram.com/FoldedCubeGraph.html (reference date not asserted).
- L. Hou, B. Hou, S. Gao, W.-H. Yu, *New code upper bounds for the folded n-cube*, arXiv:1801.06971v1, 2018-01-22; https://arxiv.org/abs/1801.06971 (coding-theoretic background, not an antidimension result).
