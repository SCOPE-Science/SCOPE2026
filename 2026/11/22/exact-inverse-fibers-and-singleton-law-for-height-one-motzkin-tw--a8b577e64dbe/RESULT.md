# Exact inverse fibers and singleton law for height-one Motzkin two-gram observations

## Finding
Let \(\mathcal M_n^{(1)}\) be the set of step words \(w\in\{U,D,F\}^n\) which start at height zero, never visit a negative height or a height greater than one, and finish at height zero; \(U,D,F\) change height by \(+1,-1,0\), respectively. The observation consists of the multiplicities of all oriented contiguous factors of length one or two. For every \(n\geq0\), the theorem below classifies **every observation and the exact cardinality of its inverse fiber**.

For a source with at least one \(U\), let \(t\) be the number of \(U\)'s, \(f=n-2t\), \(h=t-N_{DU}\), \(q=N_{UF}\), \(\ell=N_{FU}-(h-1)\), and \(r=N_{DF}-(h-1)\), where \(N_{ab}\) is the observed count of the ordered factor \(ab\). Write \(g=h-1+\ell+r\) and \(s=q+g\). An observation is realizable exactly when
\[
1\le t\le\lfloor n/2\rfloor,\quad 1\le h\le t,\quad 0\le q\le t,\quad \ell,r\in\{0,1\},
\]
with \(f=0\) if \(s=0\), or \(f\ge s\) if \(s>0\), and its remaining factor counts obey
\[
N_{UD}=t-q,\quad N_{UF}=N_{FD}=q,\quad N_{DU}=t-h,
\]
\[
N_{FU}=h-1+\ell,\quad N_{DF}=h-1+r,\quad N_{FF}=f-s,\quad N_{UU}=N_{DD}=0.
\]
Its exact inverse-fiber size is
\[
B(t,h,q,f,\ell,r)=\binom{t-1}{h-1}\binom tq
\begin{cases}\binom{f-1}{s-1},&s>0,\\1,&s=0\ (f=0).\end{cases}
\]
The remaining observations are the single all-flat word \(F^n\), one at each length.

Writing \(u_n\) for the number of observations having **exactly one** source word, the exact ordinary generating function is
\[
\begin{aligned}
U(z)=\sum_{n\ge0}u_nz^n={}&\frac1{1-z}+z^2+\frac{3z^3}{1-z}+3z^4+z^5\\
&+\frac{z^4(1+z)^2}{1-z^2}+\frac{2z^6}{(1-z)(1-z^2)}\\
&+\frac{z^6(1+z)^2+z^5(1+z)^2}{1-z^3}+\frac{z^6}{1-z}+\frac{z^7(1+z)^2}{1-z^4}.
\end{aligned}
\]
In particular \(u_n=n+O(1)\). Since there are exactly \(2^{n-1}\) height-one Motzkin words of length \(n\ge1\), a uniformly chosen source is uniquely reconstructible with probability
\[
\frac{u_n}{2^{n-1}}=\frac{n+O(1)}{2^{n-1}}.
\]
The first non-singleton observation occurs at length five. The numbers \(u_n\) for \(n=0,\ldots,17\) are \(1,1,2,4,8,8,12,13,15,15,16,16,20,19,19,21,24,22\).

## Assumptions and scope
The observation uses **overlapping** contiguous factors; factor identities and their orientation are retained, and multiplicities count starting positions. There is no cyclic wraparound and no knowledge of step heights at read time. The empty word is permitted at length zero. The claim concerns paths of maximum height one; unrestricted Motzkin paths are not covered. All binomial coefficients are ordinary integer combinatorial coefficients on the stated nonnegative domain.

## Proof
Every height-one Motzkin path has a **unique** parsing as a concatenation of ground flat steps \(F\) and arches \(UF^aD\) with integer \(a\ge0\): an up-step must be followed by zero or more flats and its corresponding down-step, because a second up-step is forbidden at height one. Fix \(t\ge1\) arches. Decompose the list of arches into \(h\) maximal contiguous blocks, separated by nonempty ground-flat runs; in addition, a nonempty ground-flat run may lie before the first block (indicator \(\ell\)) or after the last block (indicator \(r\)). There are \(g=h-1+\ell+r\) such ground-flat runs. Let \(q\) arches have positive flat interiors, so there are \(s=q+g\) nonempty flat runs in total.

The ordered two-factor counts uniquely reveal these parameters. There is one \(DU\) factor precisely between consecutive arches within each block, hence \(N_{DU}=t-h\). A positive-interior arch contributes one \(UF\) and one \(FD\), whereas a zero-interior arch contributes one \(UD\), giving \(N_{UF}=N_{FD}=q\) and \(N_{UD}=t-q\). Every interior ground-flat run contributes \(DF\) and \(FU\), while leading and trailing runs contribute only their respective adjacent factors, yielding \(N_{FU}=h-1+\ell\) and \(N_{DF}=h-1+r\). Each flat run of length \(a\ge1\) contains exactly \(a-1\) occurrences of \(FF\), giving \(N_{FF}=f-s\). No \(UU\) or \(DD\) factors occur. These equations also reconstruct the boundary indicators and show that two different parameter tuples cannot describe the same observation.

Conversely, any stated feasible tuple produces a path: choose a composition of \(t\) arches into \(h\) positive block sizes, select which \(q\) of the \(t\) ordered arches have a positive number of interior flats, and assign positive flat-run lengths totaling \(f\) to the \(s\) marked runs (or use no flats when \(s=f=0\)). Concatenate the prescribed blocks with intervening ground flats and the selected boundary runs. The resulting path is legal and has exactly the stated readout. All choices are unique and independent. There are \(\binom{t-1}{h-1}\) arch-block compositions, \(\binom tq\) choices of positive arches and, for \(s>0\), \(\binom{f-1}{s-1}\) positive compositions of the flat count. Multiplication proves the exact fiber formula, including both boundary cases.

For the singleton formula, each of the three binomial factors must equal one. For \(t\ge2\) this forces \(h\in\{1,t\}\) and \(q\in\{0,t\}\); for \(t=1\), \(h=1\) and both \(q\) values remain. The flat allocation has multiplicity one exactly when \(s=0=f\), or \(s=1\) with any \(f\ge1\), or \(s\ge2\) with \(f=s\). For \(t=1\) these cases contribute \(z^2+3z^3/(1-z)+3z^4+z^5\). For \(t\ge2\), the four ordered pairs \((h,q)=(1,0),(1,t),(t,0),(t,t)\) respectively contribute
\[
\frac{z^4(1+z)^2}{1-z^2}+\frac{2z^6}{(1-z)(1-z^2)},\quad
\frac{z^6(1+z)^2}{1-z^3},\quad
\frac{z^5(1+z)^2}{1-z^3}+\frac{z^6}{1-z},\quad
\frac{z^7(1+z)^2}{1-z^4}.
\]
The extra \(z^6/(1-z)\) in the third case accounts for \(t=2,h=2,q=0,\ell=r=0\), where exactly one ground-flat run may have arbitrary positive length. Adding the all-flat contribution \(1/(1-z)\) proves the displayed rational generating function.

Only the singularity at \(z=1\) has order two; the coefficient of \((1-z)^{-2}\) is exactly one, while every other root-of-unity pole has order at most one. Thus \(u_n=n+O(1)\). Finally, arbitrary concatenations of the primitive tokens \(F,UF^aD\) have generating function \((1-z)/(1-2z)\), so the source count is \(2^{n-1}\) for \(n\ge1\). Direct comparison of the first five profile totals, or the factor formula at length five, shows that the first collision is at \(n=5\), completing the proof.

## Verification
Run `python3 verify.py` using Python's standard library. It independently generates all valid paths and directly computes complete length-one and length-two factor multiplicity vectors through length 16, compares the entire dictionary of observed inverse-fiber cardinalities with the binomial formula, and checks source counts. A separate integer power-series calculation checks the singleton rational generating function against the exact parameter-count formula through length 65. These computations check finite instances; the argument above is the all-length proof.

## Relationship to prior work
Karhumäki, Saarela and Zamboni introduced and analyzed the general \(k\)-Abelian observation concept and gave Eulerian-multigraph realizability criteria. Baril and Petrossian studied Motzkin-path equivalence by the **positions** of occurrences of one specified pattern, not by the **joint multiplicity vector** of every one- and two-letter factor. Manes, Sapounakis, Tasoulas and Tsikouras likewise study occurrence positions for individual patterns of ballot and Dyck paths. The contribution here is the simultaneous observation's exact inverse-list cardinality and complete singleton law for a bounded-height Motzkin source, rather than the general definitions or counts attached to one fixed pattern.

## Limitations
This result is not a theorem about arbitrary-height Motzkin paths, factor lengths above two, unordered substring compositions or noisy reads. It makes no claim of independent external validation or of unconditional priority over inaccessible or unindexed literature. The explicit factorization is particular to the height-one arch decomposition.

## References
- J. Karhumäki, A. Saarela and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1, January 22, 2013, https://arxiv.org/abs/1301.5104.
- J.-L. Baril and A. Petrossian, *Equivalence Classes of Motzkin Paths Modulo a Pattern of Length at Most Two*, Journal of Integer Sequences 18 (2015), Article 15.7.1, https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Baril/baril3.pdf.
- K. Manes, A. Sapounakis, I. Tasoulas and P. Tsikouras, *Equivalence classes of ballot paths modulo strings of length 2 and 3*, arXiv:1510.01952v1, October 7, 2015, https://arxiv.org/abs/1510.01952.
