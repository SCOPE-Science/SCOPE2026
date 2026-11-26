# Frobenius orbit spectra of sixers and double-sixes on six-point blowup cubic surfaces

## Finding
Let \(k=\mathbb F_q\) be any finite field and \(Z\subset\mathbb P^2_k\) a reduced finite étale subscheme of degree six whose six geometric points are in general position: no three are collinear and no conic passes through all six. Let \(S=\operatorname{Bl}_Z\mathbb P^2\), a smooth cubic del Pezzo surface, and let \(\sigma\in S_6\) denote geometric Frobenius's permutation of the six geometric points (either Frobenius convention gives the same orbit profile).

A **sixer** is an unordered set of six mutually disjoint geometric exceptional lines of \(S\), and a **double-six** is an unordered pair of complementary sixers with the Schläfli incidence pattern. These define finite étale marking schemes \(\mathcal S\) and \(\mathcal D\) of degrees 72 and 36. A marking is rational when its underlying set is Frobenius-invariant, even if its individual curves or its sixer halves are not rational.

**Classification.** The entire Frobenius orbit profiles of \(\mathcal S\) and \(\mathcal D\), including all eleven possible cycle partitions of \(\sigma\), are:

| Cycle type on six points | Sixer Frobenius orbits | Double-six Frobenius orbits | Rational sixers | Rational double-sixes | Double-sixes with exchanged halves |
|---|---|---|---:|---:|---:|
| \((1,1,1,1,1,1)\) | \(1^{72}\) | \(1^{36}\) | 72 | 36 | 0 |
| \((2,1,1,1,1)\) | \(1^{30}2^{21}\) | \(1^{16}2^{10}\) | 30 | 16 | 1 |
| \((2,2,1,1)\) | \(1^{12}2^{30}\) | \(1^{8}2^{14}\) | 12 | 8 | 2 |
| \((2,2,2)\) | \(1^{2}2^{35}\) | \(1^{4}2^{16}\) | 2 | 4 | 3 |
| \((3,1,1,1)\) | \(1^{12}3^{20}\) | \(1^{6}3^{10}\) | 12 | 6 | 0 |
| \((3,2,1)\) | \(1^{6}2^{3}3^{8}6^{6}\) | \(1^{4}2^{1}3^{4}6^{3}\) | 6 | 4 | 1 |
| \((3,3)\) | \(1^{6}3^{22}\) | \(1^{3}3^{11}\) | 6 | 3 | 0 |
| \((4,1,1)\) | \(1^{4}2^{4}4^{15}\) | \(1^{2}2^{3}4^{7}\) | 4 | 2 | 0 |
| \((4,2)\) | \(1^{2}2^{5}4^{15}\) | \(1^{2}2^{3}4^{7}\) | 2 | 2 | 1 |
| \((5,1)\) | \(1^{2}5^{14}\) | \(1^{1}5^{7}\) | 2 | 1 | 0 |
| \((6)\) | \(1^{2}2^{2}6^{11}\) | \(1^{1}2^{1}3^{1}6^{5}\) | 2 | 1 | 0 |

Here \(d^m\) denotes \(m\) orbits of length \(d\), *not* exponentiation of the group or a number of rational points. In particular every such cubic has at least two distinct \(k\)-defined blowdown structures to \(\mathbb P^2_k\) modulo target projective automorphisms, even when none of its 27 geometric lines is individually \(k\)-rational (e.g. \(\sigma\) is a six-cycle). For cycle type \((2,2,2)\), four double-sixes descend, but three have their two halves exchanged by Frobenius and thus provide no individually rational sixer half.

For \(f=\#\{i:\sigma(i)=i\}\), let \(u_r(\sigma)\) be the number of \(\sigma\)-stable \(r\)-element subsets of the six labels, equivalently the number of ways to choose a union of cycle supports of total length \(r\). The rational marking counts satisfy the uniform formulas
\[
\#\mathcal S(k)=2+f(f-1)+2u_3(\sigma),\qquad
\#\mathcal D(k)=1+u_2(\sigma)+u_3(\sigma).
\]
The number of rational double-sixes with Frobenius-exchanged halves is exactly the number of transpositions occurring as cycles in \(\sigma\). For every \(m\ge1\), replace \(\sigma\) with \(\sigma^m\) to count markings over \(\mathbb F_{q^m}\). If \(b_d\) and \(c_d\) are the two orbit multiplicities in the corresponding row, the finite étale zeta functions are, respectively,
\[
Z(\mathcal S,T)=\prod_d(1-T^d)^{-b_d},\qquad Z(\mathcal D,T)=\prod_d(1-T^d)^{-c_d}.
\]
This is a conditional classification for surfaces given by a six-point blowup as above; it is not a claim that every finite-field cubic surface admits such a blowup or that every cycle pattern occurs over every finite field.

## Assumptions and scope
All curves and disjointness conditions are geometric, over an algebraic closure of \(k\). The six points are assumed distinct and in general position, which guarantees precisely the standard 27 exceptional curves and an ample anticanonical class in any characteristic. The finite étale marking schemes refer to the discrete reduced configurations with their actual Galois action, not to the surface's own Hasse–Weil zeta function. For an unordered sixer, a rational blowdown means a morphism defined over \(k\) and considered up to a \(k\)-automorphism of its target projective plane.

## Proof
**1. All 27 curves and their intersections.** On the six-point blowup let \(H\) be the pullback of a line and \(E_i\) the geometric exceptional curves, with \(H^2=1\), \(E_i^2=-1\), \(H E_i=0\), and \(E_iE_j=0\) for distinct indices. The 27 exceptional lines are exactly
\[
E_i\ (1\le i\le6),\quad L_{ij}=H-E_i-E_j\ (1\le i<j\le6),\quad Q_i=2H-\sum_{j\ne i}E_j\ (1\le i\le6).
\]
These divisor classes are all effective unique negative curves, and Frobenius permutes their indices by \(\sigma\). Thus the intersection graph, the full set of sixers, and its arithmetic action are independent of the coordinates of \(Z\).

**2. A complete, disjoint classification of sixers.** Write \(A^c\) for the complement of a three-subset \(A\) of the six labels. All sixers are precisely the following four nonoverlapping types:
\[
\begin{aligned}
&\{E_1,\ldots,E_6\},\quad \{Q_1,\ldots,Q_6\};\\
&S_{ij}=\{E_i,Q_i\}\cup\{L_{jk}:k\notin\{i,j\}\}\quad(i\ne j);\\
&U_A=\{E_a:a\in A\}\cup\{L_{bc}:b,c\in A^c\};\\
&V_A=\{Q_a:a\in A\}\cup\{L_{bc}:b,c\in A^c\}.
\end{aligned}
\]
There are \(2+6\cdot5+\binom63+\binom63=72\) distinct sixers in this list. Directly from the intersection form every listed set consists of six disjoint \((-1)\)-curves. Completeness follows from the classical 72-sixer theorem for smooth cubic surfaces (Buckley–Košir, as cited), or independently from the exhaustive 27-choose-6 intersection enumeration in the accompanying verifier, which obtains *exactly* these 72 sets. No heuristic sampling is used.

**3. Complementary sixers.** The complementary-half operation, defined intrinsically by the unique sixer in which every line meets exactly five of the given six lines, is
\[
\begin{aligned}
&\{E_i:1\le i\le6\}\longleftrightarrow \{Q_i:1\le i\le6\};\\
&S_{ij}\longleftrightarrow S_{ji};\\
&U_A\longleftrightarrow V_{A^c}.
\end{aligned}
\]
Each relation follows by checking disjointness within both halves and the five-versus-zero cross-incidence using \(H^2=1\), \(E_i^2=-1\). The exhaustive code also checks the unique complementary half independently for every one of the 72 sixers. Consequently the 36 unordered double-sixes split as \(S_6\)-sets into one singleton, fifteen unordered label pairs, and twenty three-subsets, with no additional pairs.

**4. Frobenius action and fixed-point formulas.** The 72 sixers form the explicit \(S_6\)-set
\[
\{\ast,\ast\}\ \sqcup\ \{(i,j):i\ne j\}\ \sqcup\ (\tbinom{[6]}3)_U\ \sqcup\ (\tbinom{[6]}3)_V.
\]
The 36 double-sixes form the \(S_6\)-set \(\{\ast\}\sqcup\tbinom{[6]}2\sqcup\tbinom{[6]}3\). The first is fixed on its two distinguished elements, with \(f(f-1)\) fixed ordered pairs and \(u_3\) fixed points in each triple-subset copy; the second has \(1+u_2+u_3\) fixed points. Only the double-six indexed by an unordered pair \(\{i,j\}\) can have its two halves interchanged: that happens precisely when \(\sigma(i)=j\) and \(\sigma(j)=i\), yielding one exchanged pair for every length-two cycle of \(\sigma\). In contrast, the other double-six halves lie in the distinct \(U\) and \(V\) classes, which are preserved separately under \(S_6\).

The complete orbit spectra follow by applying these index permutations to the finite sets for the eleven conjugacy classes. To check analytically, for every extension degree \(m\), compute fixed counts using \(\sigma^m\), then recover orbit multiplicities from the identity \(F_m=\sum_{d\mid m}d b_d\) and similarly for \(c_d\). The separate exhaustive computation iterates all \(720\) permutations and confirms each row, including profiles of both marking schemes.

**5. Rational plane contractions.** A Galois-stable sixer consists of disjoint \((-1)\)-curves and contracts over \(k\) to a degree-nine del Pezzo surface. This is a Severi–Brauer form of \(\mathbb P^2\), and its Brauer class vanishes over the finite field \(k\), so the target is \(\mathbb P^2_k\). Conversely a plane blowdown determines its six exceptional lines; two targets differing by projective automorphism give the same sixer. Hence the number of rational blowdowns modulo target automorphisms equals \(\#\mathcal S(k)\). For a six-cycle, the only rational sixers are the two distinguished configurations \(\{E_i\}\) and \(\{Q_i\}\), while no individual exceptional line is fixed under the six-cycle.

## Verification
The supplied `verify.py` uses only Python standard-library integer arithmetic. It computes the 27 class vectors and all pairwise intersection products; tests all \(\binom{27}{6}=296010\) candidate six-subsets; independently constructs the four-family enumeration and compares the two; computes the unique partner sixer by five-cross-incidence for each of 72 sixers; checks involutivity; iterates every permutation of the six labels; verifies eleven orbit profiles for both 72 sixers and 36 double-sixes; and compares fixed and exchanged-half counts with the independent cycle-union formula. All checks succeeded, ending with `CUBIC_SIXER_S6_FROBENIUS_EXHAUSTIVE_OK`. `check_output.txt` records the complete eleven-row sixer profile output. The finite enumeration is exhaustive because the standard exceptional-curve classification proves the universe has exactly 27 elements. The proof of contraction descent uses the separate standard finite-field Brauer theorem, not computation.

## Relationship to prior work
Buckley and Košir's 2006 paper supplies the known 72 geometric sixers, their correspondence with determinantal representations, and the 36 double-sixes. Elsenhans–Jahnel investigate Galois-invariant double-sixes, and Das (2020) provides a general Galois/Weyl-group statistics framework from which special marking counts can in principle be computed; these general results and the geometric cardinalities are not claimed as new. A published arithmetic result on *the Fermat cubic* already treats the split case and an involutory nonsplit Frobenius case, numerically overlapping the identity and the \((2,2,2)\) patterns in this classification. Its surface, Galois action and conclusions are narrower than the eleven-type classification for arbitrary Frobenius-stable six-point configurations, and those two numerical special cases are expressly excluded from any novelty claim. The proposed contribution here is the full explicitly proved \(S_6\)-set decomposition of all sixers and double-sixes together with the eleven-row arithmetic orbit and exchanged-half classifications for this natural family of blowups, including the six-cycle and mixed-cycle cases. Historical priority for an equivalent Weyl-group permutation-character computation remains provisional.

## Limitations
The theorem is conditional on the existence of the specified blowup model and on geometric general position. It neither classifies arbitrary cubic surfaces nor proves that every permutation type is geometrically realizable for every small finite field. The classification does not identify the finite étale marking-scheme zeta functions with the zeta function of \(S\). The material inspected did not rule out an earlier implicit derivation of the full table from a general Weyl-group character table. No independent scientific audit has been performed.

## References
1. Anita Buckley and Tomaž Košir, *Determinantal representations of smooth cubic surfaces*, arXiv:math/0606098, first posted 2006-06-05, https://arxiv.org/abs/math/0606098.
2. Andreas-Stephan Elsenhans and Jörg Jahnel, *Cubic surfaces with a Galois invariant double-six*, Central European Journal of Mathematics 2010, DOI:10.2478/s11533-010-0036-1, https://doi.org/10.2478/s11533-010-0036-1.
3. Andreas-Stephan Elsenhans and Jörg Jahnel, *On the Brauer–Manin obstruction for cubic surfaces*, arXiv:1011.1430, first posted 2010-11-05, https://arxiv.org/abs/1011.1430.
4. Ronno Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183, first posted 2020-02-25, https://arxiv.org/abs/2002.11183.
5. *Frobenius descent of sixers and double-sixes on the Fermat cubic surface*, published mathematical record 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-frobenius-descent-of-sixers-and-double-sixes-on-the-fermat-cubic--49ca8401e2ad.
