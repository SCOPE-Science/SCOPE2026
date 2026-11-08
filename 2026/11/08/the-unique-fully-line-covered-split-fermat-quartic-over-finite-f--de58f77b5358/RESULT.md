# The unique fully line-covered split Fermat quartic over finite fields

## Finding

Let \(q\) be any prime power such that \(q\equiv1\pmod 8\) and \(\operatorname{char}\mathbb F_q\ne3\). Consider the smooth Fermat quartic K3 surface
\[
X_q:\ x_0^4+x_1^4+x_2^4+x_3^4=0\subset\mathbb P^3_{\mathbb F_q}.
\]
For each of the three partitions of \(\{0,1,2,3\}\) into two unordered pairs \(\{i,j\}\), \(\{k,l\}\), and each \(\alpha,\beta\in\mathbb F_q\) with \(\alpha^4=\beta^4=-1\), let \(L_{ij|kl}(\alpha,\beta)\) be the projective line \(x_i=\alpha x_j\), \(x_k=\beta x_l\). Write \(U_q\) for their reduced union, consisting of exactly \(48\) distinct \(\mathbb F_q\)-lines. For \(r\ge0\), let \(N_r(q)\) be the number of points of \(X_q(\mathbb F_q)\) incident with exactly \(r\) of these lines.

**Theorem.** For every such \(q\), the complete positive-incidence spectrum is
\[
N_4(q)=24,\qquad N_2(q)=192,\qquad N_1(q)=48(q-9),
\]
and \(N_r(q)=0\) for all other positive integers \(r\). In particular,
\[
\#U_q(\mathbb F_q)=48q-216,\qquad
N_0(q)=\#X_q(\mathbb F_q)-48q+216.
\]
The complete rational-point covering classification is
\[
\boxed{X_q(\mathbb F_q)=U_q(\mathbb F_q)\quad\Longleftrightarrow\quad q=17.}
\]
For the only other admissible prime powers below \(73\), the exact pairs \((\#X_q(\mathbb F_q),N_0(q))\) are \((1112,128)\) at \(q=25\), \((2520,768)\) at \(q=41\), and \((3480,1344)\) at \(q=49\). At \(q=17\) they are \((600,0)\).

## Assumptions and scope

The characteristic restriction excludes the exceptional characteristic-three line geometry; no statement is made for characteristic three. Because \(q\equiv1\pmod8\), the four fourth roots of \(-1\) lie in \(\mathbb F_q\), so all \(48\) specified lines are rational. These are the ordinary coordinate-pairing lines of the quartic; the theorem concerns their union and does not require an independent geometric classification of every possible line in other characteristics. A point lying on a line is counted once as a point of the union, regardless of incidence multiplicity. A point on several lines contributes to exactly one \(N_r\).

## Proof

**1. The incidence spectrum of the forty-eight lines.** Fix one of the three pairings. It yields \(4\cdot4=16\) distinct lines. Two different lines in this family meet precisely when they have a common first ratio or a common second ratio; in either case the intersection is supported on only one coordinate pair. For each of the six choices of supported coordinate pair, there are four choices of fourth-root ratio. Thus there are \(6\cdot4=24\) points at which four lines from one pairing family meet. They are rational, and there are no intersections involving a line from a different pairing family at such a point.

For intersections between two different pairing families, choose representatives
\[
L_{01|23}(\alpha,\beta):\ x_0=\alpha x_1,\ x_2=\beta x_3,
\]
\[
L_{02|13}(\gamma,\delta):\ x_0=\gamma x_2,\ x_1=\delta x_3.
\]
These lines meet exactly when \(\alpha\delta=\gamma\beta\), and the resulting point has all four coordinates nonzero. For each of the \(16\) choices of \((\alpha,\beta)\), four values of \(\delta\) determine exactly four values of \(\gamma\), so there are \(64\) distinct intersections for this ordered pair of families. (Distinct choices of the first line have distinct intersection points because a point with all coordinates nonzero lies on a unique line of each fixed pairing family.) There are three unordered pairs of families, producing \(192\) pairwise intersections.

None of these points lies on a line of the third family. Indeed, the equations for two pairings imply \(x_0^4=x_2^4=-x_1^4=-x_3^4\), whereas the third pairing would require \(x_0^4=-x_3^4\), forcing \(2x_0^4=0\), impossible in the stated odd characteristic with nonzero coordinates. Therefore the \(192\) intersections have multiplicity exactly two. There are no intersections other than the \(24\) fourfold and \(192\) twofold points.

Each line contains two of the fourfold points (one on each of its coordinate pairs). Each line intersects the other two pairing families in four points per family, hence eight distinct twofold points. Consequently each line has \((q+1)-2-8=q-9\) points of multiplicity one. Summing these disjoint strata gives the asserted \(N_4,N_2,N_1\), and
\[
\#U_q(\mathbb F_q)=24+192+48(q-9)=48q-216.
\]

**2. Complete covering over \(\mathbb F_{17}\).** The fourth-power set in \(\mathbb F_{17}\), written with balanced integer representatives, is \(\{0,1,-1,4,-4\}\). Suppose four such values sum to zero modulo \(17\). Their integer sum has absolute value at most \(16\), so it is zero as an integer. In a sum of at most four elements from \(\{0,\pm1,\pm4\}\), the number of \(+4\) terms equals the number of \(-4\) terms: otherwise the unmatched multiple of \(4\) cannot be canceled by at most three summands of magnitude \(1\), nor by a remaining multiple of \(4\) without balancing. The remaining \(+1\) and \(-1\) counts likewise agree. Thus the four fourth-power values split into two additive-opposite pairs (with zeros paired together). If \(x_i^4+x_j^4=0\), then \(x_i=\alpha x_j\) for some \(\alpha^4=-1\), including the case both coordinates vanish. Therefore every point of \(X_{17}(\mathbb F_{17})\) belongs to one of the \(48\) lines. The line-incidence count then gives \(\#X_{17}(\mathbb F_{17})=600\).

**3. Explicit obstructions for the other small fields.** In every admissible field, membership of \(U_q\) is equivalent to being able to partition the four fourth powers into two pairs each summing to zero. In \(\mathbb F_{41}\), the point \([1:2:7:1]\) has fourth powers \((1,16,23,1)\). Their sum is \(0\), but they admit no opposite-pair partition, giving an off-line point. In \(\mathbb F_{25}=\mathbb F_5(\theta)\) with \(\theta^2=2\), the point \([0:1+\theta:4+\theta:1]\) has fourth powers \((0,2+2\theta,2+3\theta,1)\), also a sum of zero with no opposite-pair partition. In \(\mathbb F_{49}=\mathbb F_7(\theta)\), \(\theta^2=3\), the point \([0:1:3+2\theta:1]\) has fourth powers \((0,1,5,1)\) and is likewise outside \(U_q\).

The exact point counts claimed in the theorem are obtained by exhaustive, independent finite-field arithmetic: `verify_point_counts.py` evaluates the fourth-power multiplicity convolution and exhausts all standard projective charts; `verify_incidence.py` independently enumerates all rational projective points and checks incidence with each of the \(48\) explicitly constructed lines. Both scripts use the standard library and all tables are formed from exact arithmetic, not floating-point approximations.

**4. All larger fields.** A smooth quartic surface in \(\mathbb P^3\) is a K3 surface; its first and third \(\ell\)-adic Betti numbers vanish and its second Betti number is \(22\). The Weil conjectures give
\[
\#X_q(\mathbb F_q)\ge q^2+1-22q.
\]
Subtracting the exact line-union count yields
\[
N_0(q)\ge q^2-70q+217.
\]
This is strictly positive for every \(q\ge73\). The only prime powers \(q\equiv1\pmod8\) below \(73\) are \(9,17,25,41,49\); the characteristic-three value \(9\) is outside the hypotheses. Steps 2 and 3 therefore prove the covering classification for every admissible prime power.

## Verification

Run the two included standalone files using a Python 3 interpreter:

```text
python3 verify_point_counts.py
python3 verify_incidence.py
```

The first prints exact tuples \((q,\#X_q,N_0)\): \((17,600,0)\), \((25,1112,128)\), \((41,2520,768)\), \((49,3480,1344)\) and concludes `VERIFY_POINT_COUNTS_OK`. The second explicitly enumerates all points in each finite field and all \(48\) lines, reproduces every incidence multiplicity, and concludes `VERIFY_INCIDENCE_OK`. The case of infinitely many fields is proved by the incidence argument and K3 Weil bound, not extrapolated from finite enumeration.

## Relationship to prior work

The geometric \(48\)-line coordinate-pairing configuration of the Fermat quartic is classical. Degtyarev and Rams, *Lines on K3-quartics via triangular sets*, arXiv:2301.04127 (first public January 10, 2023), describe the line-configuration context and classify configurations with more than \(48\) lines on smooth complex quartics; they do not give the stated arithmetic point-incidence spectrum or the uniform covering classification. Schütt, Shioda, and van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377, give broader geometric and arithmetic context for Fermat lines.

Voloch and Zieve, *Rational points on some Fermat curves and surfaces over finite fields*, arXiv:1310.1772, Theorem 1.5 and Corollary 1.7, already characterize \(\mathbb F_{25}\)-points on the quartic written as the \(q-1\) Fermat surface for \(q=5\), including points off the lines. In particular, the \(q=25\) noncoverage and its associated count are **not claimed to be independently new**. Salberger, *Counting rational points on projective varieties*, doi:10.1112/plms.12508, considers rational points outside lines in a different (number-field height) setting. The contribution asserted here is the joint exact incidence spectrum and the complete uniqueness classification over the indicated infinite class of finite fields, including the \(\mathbb F_{17}\) extremum.

## Limitations

This theorem is confined to \(q\equiv1\pmod8\) outside characteristic three; it does not classify line coverage in other congruence classes or the exceptional characteristic. The geometric line configuration is previously known. The formula for \(N_0\) is expressed through \(\#X_q\) for general \(q\), rather than a closed Jacobi-sum formula for every extension. The uniqueness claim is relative to the specified \(48\) lines and the stated class of fields. Historical priority of this arithmetic classification has not been independently certified; a specialized earlier point-count or code-derived equivalent may exist.

## References

- A. Degtyarev and S. Rams, *Lines on K3-quartics via triangular sets*, arXiv:2301.04127 (v1, January 10, 2023), https://arxiv.org/html/2301.04127v1 .
- M. Schütt, T. Shioda, R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377, https://arxiv.org/abs/0812.2377 .
- J. F. Voloch and M. E. Zieve, *Rational points on some Fermat curves and surfaces over finite fields*, arXiv:1310.1772, Theorem 1.5 and Corollary 1.7, https://arxiv.org/html/1310.1772v1 .
- P. Salberger, *Counting rational points on projective varieties*, Proc. London Math. Soc. (2023), doi:10.1112/plms.12508, https://doi.org/10.1112/plms.12508 .
- P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974); the weight bound used is the standard consequence for smooth projective K3 surfaces.
