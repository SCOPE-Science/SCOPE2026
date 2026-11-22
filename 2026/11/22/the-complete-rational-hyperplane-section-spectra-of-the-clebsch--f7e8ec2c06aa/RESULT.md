# The complete rational hyperplane-section spectra of the Clebsch cubic over \(\mathbb F_7\) and \(\mathbb F_{11}\)

## Finding
Let \(X_q\subset\mathbb P^4_{\mathbb F_q}\), for \(q\in\{7,11\}\), be the smooth cubic surface
\[
\sum_{i=0}^{4}X_i=0,\qquad \sum_{i=0}^{4}X_i^3=0.
\]
A rational hyperplane means a hyperplane of the ambient three-dimensional linear subspace \(\sum X_i=0\), so two proportional nonzero linear forms give the same hyperplane. Define
\[
n_q(z)=\#\{H\in(\mathbb P^3)^\vee(\mathbb F_q):\#(X_q\cap H)(\mathbb F_q)=z\}.
\]
Every nonzero value of \(n_q(z)\) is as follows; all unlisted values are zero.

| \(q\) | Section sizes \(z\) | Corresponding multiplicities \(n_q(z)\) |
|:---:|:---|:---|
| 7 | 6, 9, 10, 11, 12, 13, 14, 16, 21, 22 | 10, 40, 60, 60, 120, 20, 30, 45, 5, 10 |
| 11 | 12, 14, 15, 16, 17, 18, 22, 23, 24, 33, 34 | 30, 60, 100, 300, 300, 440, 30, 24, 135, 35, 10 |

There are respectively 400 and 1464 rational hyperplanes. Of these, exactly 15 and 45 contain three rational surface-lines: the 10 coordinate-pair Eckardt planes in each field have respectively 22 and 34 rational points, while the remaining 5 and 35 tritangent planes have respectively 21 and 33 points. Exactly 75 and 189 other planes contain one rational surface-line, and all remaining planes contain none. The 10 maximizers are, in both cases, precisely \(H_{ij}:X_i+X_j=0\), for \(0\le i<j\le4\).

For the linear evaluation code of the anticanonical system on all rational points of \(X_q\), we obtain the full Hamming weight enumerator
\[
W_q(T)=1+(q-1)\sum_z n_q(z)T^{N_q-z},\qquad (N_7,N_{11})=(85,199).
\]
Thus the code parameters are \([85,4,63]_7\) and \([199,4,165]_{11}\), respectively. The new object of study is the complete distribution, not simply the minimum-distance consequence.

## Assumptions and scope
The ground field is exactly \(\mathbb F_7\) or \(\mathbb F_{11}\). The surface is the displayed five-coordinate Clebsch model, not a twist. Rational point counts refer to the underlying reduced finite sets of the section, not scheme-theoretic intersection multiplicity. A rational line means an \(\mathbb F_q\)-linear projective line contained in the surface. The weight enumerator uses one representative per rational projective point, chosen by setting its first nonzero coordinate to one; any other such choice produces a monomially equivalent code with the same Hamming distribution.

Both surfaces are nonsingular: a singular point in \(\sum X_i=0\) would have all five squared coordinates equal. Nonzero coordinates must therefore be the signs of one scalar, and the sum of five signs belongs to \(\{\pm1,\pm3,\pm5\}\), none zero in characteristics seven or eleven. If the common square were zero, the point itself would be zero. Hence the gradient criterion excludes singularities over the algebraic closure.

## Proof
**1. Exact projective enumeration.** Eliminate \(X_4\) and use the four homogeneous coordinates \(v=(v_0,v_1,v_2,v_3)\). The defining equation becomes
\[
F(v)=\sum_{i=0}^{3}v_i^3-\left(\sum_{i=0}^{3}v_i\right)^3=0.
\]
Every rational projective point has exactly one normalized coordinate vector of the form \((0,\ldots,0,1,t_1,\ldots,t_r)\) with each trailing coordinate in \(\mathbb F_q\). For \(r=0,1,2,3\), these disjoint charts contain respectively \(1,q,q^2,q^3\) vectors, totalling \(q^3+q^2+q+1\). Apply this same complete list both to the rational surface points satisfying \(F=0\), and to nonzero dual coefficient vectors \(h\). The section count is the finite integer
\[
z_q(h)=\sum_{\substack{v\text{ normalized}\\F(v)=0}}[h_0v_0+h_1v_1+h_2v_2+h_3v_3=0].
\]
These mutually exclusive and exhaustive loops, implemented in the accompanying independent integer verifier, give exactly the two tables in the Finding. The loop bounds are at most \(11^3\) points per normalized chart and 1464 dual vectors; there is no probabilistic sampling or extrapolation. Since every hyperplane has strictly fewer than \(N_q\) surface points, the four-dimensional space of linear forms evaluates injectively. Every nonzero codeword is a nonzero scalar multiple of one projective hyperplane word, proving the stated complete weight enumerator.

**2. Independent point generator.** A separate enumeration writes the first three coordinates as a normalized nonzero triple \((a,b,c)\), lets \(s=a+b+c\), \(t=a^3+b^3+c^3\), and solves, for each fourth coordinate \(d\),
\[
t-s^3-3s^2d-3sd^2=0\pmod q.
\]
It adds the one exceptional point \((0,0,0,1)\). This independent quadratic formula produces exactly the same 85 and 199 normalized surface-point sets as the four-variable cubic evaluation. An independent double-count validates
\[
\sum_z n_q(z)=q^3+q^2+q+1,\quad
\sum_z z n_q(z)=N_q(q^2+q+1),\quad
\sum_z\binom z2n_q(z)=(q+1)\binom{N_q}2.
\]
The second identity counts point–hyperplane flags; the third counts unordered distinct point-pairs and the hyperplanes through their joining line.

**3. Geometry of the large fibers.** The ten displayed planes \(X_i+X_j=0\) meet the surface in the three coordinate lines obtained by making one of the other three coordinates zero: after \(X_i+X_j=0\), the other coordinates satisfy \(A+B+C=0\) and \(A^3+B^3+C^3=3ABC\). These three rational lines are concurrent at the rational Eckardt point with coordinates \([\ldots:1:\ldots:-1:\ldots:0]\), so each such plane has exactly \(3(q+1)-2=3q+1\) rational points. The exhaustive census proves that no other plane attains the same point count.

Independently, enumerate every rational line as the span of two distinct rational surface points, retaining it precisely when all \(q+1\) rational points of the span satisfy \(F=0\). This generates exactly 15 rational surface-lines at seven and 27 at eleven. Testing containment in each of the already enumerated rational hyperplanes shows the section-line profile: at seven, 310 sections contain no rational surface-line, 75 contain one, 5 contain three nonconcurrent lines, and 10 contain three concurrent lines; at eleven the corresponding counts are 1230, 189, 35, 10. Over either field, the union of three lines in any tritangent plane consists of the whole plane cubic because a cubic polynomial vanishing on three distinct lines in a plane is proportional to their product. The nonconcurrent configurations are triangles, whose union has \(3(q+1)-3=3q\) rational points. There is no section containing exactly two surface-lines because any plane section containing two must contain their residual third line.

**4. Symmetry certificate.** The coordinate-permutation group \(S_5\) acts on the five-coordinate model. A hyperplane in these coordinates is represented by a five-vector of coefficients up to addition of a constant vector and nonzero scaling; subtract the fifth coefficient and normalize the first four. Direct enumeration of all 120 coordinate permutations partitions the 400 and 1464 rational hyperplanes into respectively 13 and 30 orbits. Every orbit has a constant section size. The attached orbit table gives one normalized four-vector, orbit cardinality and section size for every orbit, and recovers both multiplicity tables by summation. This is an additional exact finite certificate.

## Verification
Run the accompanying standalone program with `python3 verification/clebsch_section_census.py`. It uses only the Python standard library and performs both independent point generators, every hyperplane count, the two moment identities, the 10 exact maximizer equations, all rational contained-line tests, the full codeword histogram and the full \(S_5\) orbit decomposition. The execution must end with `CLEBSCH_SECTION_CENSUS_OK`. The compact orbit table is in `data/clebsch_section_orbits.json`. No saved logs from another computation are assumed or needed.

## Relationship to prior work
The geometric 27-line, 45-tritangent and Eckardt configurations of smooth cubic surfaces are classical. Brundu–Logar–Polli (2022) classify symmetric cubics and give explicit line/tritangent geometry over characteristic zero; Bergvall–Gounelas (2019, first preprint) examine geometric types of anticanonical sections, not the rational section-size distribution of this fixed finite-field model. Boguslavskii (1998), discussed in Little's 2008 survey, determines generalized Hamming weights and maximal section sizes for split Del Pezzo surface codes; these do not determine the *complete* number of hyperplanes of each section size. In particular, the Eckardt maximum and the split-case minimum-distance principle are not claimed as novel.

Hirschfeld (1981) studies when the rational points of a cubic surface all lie on its 27 lines. A later arithmetic incidence calculation of the same Clebsch surface determines the multiplicities of rational points lying on geometric lines and establishes that the rational line complement is empty precisely in the two fields treated here. Neither statement determines the distribution across all rational hyperplanes, which is the content of this finite exact census. The latter known empty-complement characterization motivates treating this pair of exceptional fields together; the present finding does not re-claim it.

## Limitations
The theorem is finite, restricted to two named prime fields and to the untwisted displayed model. Its proof is exhaustive exact arithmetic, not a general formula for all finite fields. The full weight enumerators have not been asserted to improve best-known code parameters. The original 1981 Hirschfeld chapter was available as a detailed publisher summary but the full three-page article could not be inspected; the general Hamming-weight literature could still contain an unindexed equivalent numerical table. Historical priority is therefore subject to this explicit risk.

## References
- O. Bergvall and F. Gounelas, *Cohomology of moduli spaces of Del Pezzo surfaces*, arXiv:1904.10249 (first public 2019-04-23), https://arxiv.org/abs/1904.10249, Section 4.
- M. Brundu, A. Logar and F. Polli, *Construction of Symmetric Cubic Surfaces*, arXiv:2207.04493 (first public 2022-07-10), https://arxiv.org/html/2207.04493v2, Sections 2–3.
- M. I. Boguslavskii, *Sections of the Del Pezzo Surfaces and Generalized Weights*, Problemy Peredachi Informatsii **34** (1998), 18–29, https://www.mathnet.ru/eng/ppi392.
- J. B. Little, *Algebraic Geometry Codes from Higher Dimensional Varieties*, arXiv:0802.2349 (2008), https://arxiv.org/abs/0802.2349, Section 4.4.
- J. W. P. Hirschfeld, *Cubic surfaces whose points all lie on their 27 lines*, *Finite Geometries and Designs* (1981), 169–171, doi:10.1017/CBO9781107325579.020.
- *Arithmetic incidence and zeta function of the Clebsch cubic's line complement*, publicly accessible result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-incidence-and-zeta-function-of-the-clebsch-cubic-s-li--9b45ce52c311.
