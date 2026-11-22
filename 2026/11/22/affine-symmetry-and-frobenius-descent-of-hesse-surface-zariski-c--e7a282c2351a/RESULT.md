# Affine symmetry and Frobenius descent of Hesse-surface Zariski chambers

## Finding
Consider the Hesse pencil of plane cubics over an algebraically closed field of characteristic different from three, and let \(X\) be the blowup of its nine distinct base points. The negative curves on \(X\) comprise the nine exceptional sections \(E_p\), indexed by points \(p\in\mathbb F_3^2\), and the twelve strict transforms \(L_\ell\) of the Hesse lines, indexed by affine lines \(\ell\subset\mathbb F_3^2\). The Zariski chambers of its big cone correspond to the empty support and all negative-definite subsets of these 21 curves.

**Theorem.** The full affine incidence group \(G=\operatorname{AGL}_2(\mathbb F_3)\) of order \(432\) acts on the \(50\,165\) Zariski chamber supports with precisely \(239\) orbits. Its determinant-one Hessian subgroup \(G^+=\mathbb F_3^2\rtimes\operatorname{SL}_2(\mathbb F_3)\), of order \(216\), has exactly \(299\) orbits. The fixed-support counts for the eleven conjugacy classes of \(G\) are the following. A representative is the affine map \((x,y)\mapsto(ax+by+u,cx+dy+v)\) over \(\mathbb F_3\).

| \(\det A\) | Order | Class size | Affine representative \((a,b,c,d;u,v)\) | Fixed chambers |
|---:|---:|---:|---|---:|
| 1 | 1 | 1 | \(1,0,0,1,0,0\) | 50,165 |
| 1 | 2 | 9 | \(2,0,0,2,0,0\) | 285 |
| 1 | 3 | 8 | \(1,0,0,1,0,1\) | 26 |
| 1 | 3 | 24 | \(0,1,2,2,0,0\) | 305 |
| 1 | 3 | 48 | \(0,1,2,2,0,1\) | 26 |
| 1 | 4 | 54 | \(0,1,2,0,0,0\) | 21 |
| 1 | 6 | 72 | \(0,1,2,1,0,0\) | 27 |
| 2 | 2 | 36 | \(0,1,1,0,0,0\) | 1,037 |
| 2 | 6 | 72 | \(0,1,1,0,0,1\) | 8 |
| 2 | 8 | 54 | \(0,1,1,1,0,0\) | 7 |
| 2 | 8 | 54 | \(0,1,1,2,0,0\) | 7 |

The complete fixed-support-size coefficient vectors, by sizes \(0\) through \(9\), and the specific representatives are supplied in `verification/fixed_table.json` and verified independently by `verification/verify.py`. In particular, the two distinct determinant-two order-eight classes each fix exactly seven chambers. Two distinct determinant-one order-three classes both fix 26 chambers but with different support-size distributions.

For the **standard Hesse pencil over** \(\mathbb F_q\), in characteristic at least five, the number of chambers descending to \(\mathbb F_q\) is exactly
\[
N_q=\begin{cases}50\,165,&q\equiv1\pmod 3,\\1\,037,&q\equiv2\pmod3.\end{cases}
\]
More generally, for a finite-field form whose geometric Frobenius acts on the 21 negative curves through a specified affine element of \(G\), the number of rational chambers is the fixed-support total in its row. This conditional formulation does not assert the realization of every abstract affine class over every finite field.

## Assumptions and scope
The geometric statements hold over an algebraically closed field of characteristic unequal to three with the ordinary four-fiber Hesse-pencil geometry. All 21 negative curves are included, and the nef chamber is counted. \(G\) is the full **combinatorial affine-incidence group** on the 9-point, 12-line configuration. Its determinant-one subgroup acts by classical projective Hesse symmetries; determinant-two elements are not claimed to be regular complex projective automorphisms, but can describe arithmetic Frobenius actions on the marked configuration.

For the arithmetic corollary \(q\) is a prime power of characteristic at least five, and \(X\) is the blowup of the nine geometric base points of \(x^3+y^3+z^3-\lambda xyz=0\) over \(\mathbb F_q\). A rational chamber means a Frobenius-stable geometric chamber support, equivalently the support of the negative part of an \(\mathbb F_q\)-rational big divisor. No assertion is made in characteristic three.

## Proof
**1. Geometric curve exhaustion.** The fiber class \(F=-K_X\) is nef. Adjunction gives \(C^2=2p_a(C)-2+F\cdot C\). A negative irreducible curve is therefore either a rational section of self-intersection \(-1\), or a \(-2\) component of a reducible fiber. The four singular fibers have Kodaira type \(I_3\), hence 12 components. Shioda–Tate gives Mordell–Weil rank \(10-2-4(3-1)=0\), and its torsion group has order nine (the root-fiber lattice has discriminant \(3^4\), the Néron–Severi lattice is unimodular). The nine exceptional sections exhaust the sections. These facts reproduce the original 21-curve configuration, rather than assuming its completeness from an experiment.

**2. Integral intersection rules.** For distinct points \(p,p'\), \(E_p\cdot E_{p'}=0\) and \(E_p^2=-1\); for a Hesse affine line \(\ell\), \(L_\ell^2=-2\), while \(E_p\cdot L_\ell=1\) precisely when \(p\in\ell\). Components from the same triangular fiber intersect pairwise once and components of different fibers are disjoint. These formulas specify every entry of the 21-by-21 integral intersection matrix.

**3. Exact negative-definite-support criterion.** A curve subset has negative definite intersection form if and only if (i) it chooses at most two lines from each parallel class, (ii) no chosen section meets two chosen components, (iii) no chosen component meets two chosen sections, and (iv) if two components of one fiber are chosen, at most one chosen section meets their union. Necessity comes from the affine \(I_3\) cycle and the singular principal submatrices with three- or four-vertex chains of weights \(-1,-2\). Sufficiency follows because the remaining incidence graph decomposes into isolated vertices and the finite chains \(E-L\), \(L-L\), or \(E-L-L\), whose negative intersection matrices have strictly positive leading principal minors. These are precisely the four conditions appearing in the earlier geometric Hesse-chamber calculation, and they are not claimed as new here.

For a second exact check, choose a subset of zero, one, or two line components in each of four fibers, yielding \(7^4=2401\) line selections. The negative line intersection matrix \(F_B\) is block diagonal. If \(B\) is the section-line incidence matrix, the Schur complement of \(F_B\) in the negative intersection form is \(I-B^T F_B^{-1}B\), which is positive definite exactly for valid section subsets. Multiplying by six makes its entries integral, since the one- and two-line inverses have denominators two and three. Sylvester's criterion and fraction-free exact integer determinants enumerate all eligible section sets. This gives the known polynomial \(1+21t+210t^2+1236t^3+4497t^4+10308t^5+14772t^6+12612t^7+5634t^8+874t^9\) and its sum \(50\,165\). The independent four-condition enumeration produces exactly the same support masks.

**4. Affine action and conjugacy classes.** Enumerate all 48 invertible \(2\times2\) matrices over \(\mathbb F_3\), combined with all nine translations, acting on the nine affine points and the twelve three-point affine lines. The resulting 432 distinct permutations preserve the integral intersection matrix and hence the set of negative supports. Direct conjugation in this explicit finite permutation group gives 11 conjugacy classes, with class sizes \(1,9,8,24,48,54,72,36,72,54,54\) in displayed order, totaling 432. Applying one representative of each class to every one of the independently certified support masks yields the fixed counts in the table and full size vectors in the standalone data file. Both order-eight classes are represented separately and checked separately.

**5. Orbit and rational-descent checks.** The sums of class size times fixed-support number are \(103\,248=432\cdot239\) for \(G\), and \(64\,584=216\cdot299\) for \(G^+\). Burnside's lemma proves the two orbit counts. Independently, breadth-first orbit traversal under four generators of \(G^+\), and then one additional determinant-two generator of \(G\), produces precisely 299 and 239 orbits respectively.

For the standard rational Hesse pencil, a rational base point serves as origin of the nine-point \(\mathbb F_3^2\)-torsor. If \(q\equiv1\pmod3\), all cube roots of unity are rational and Frobenius fixes all 21 negative curves. If \(q\equiv2\pmod3\), Frobenius on the nine points is conjugate to \((x,y)\mapsto(-x,y)\): it fixes three points and swaps the other six in three pairs, inducing the determinant-two order-two class of size 36. That row fixes exactly 1,037 supports. Every stable support is realized by a rational big divisor by averaging an ample divisor and the reduced support over Frobenius, so fixed supports are exactly rational Zariski chambers.

## Verification
The standalone Python 3 program `verification/verify.py` uses only standard-library exact integer operations. It enumerates the \(50\,165\) geometric supports with integer Schur complements and Bareiss determinants; a second implementation independently applies the four forbidden-support conditions and confirms equality of the full support sets. It constructs all 432 affine permutations, checks the 11 conjugacy classes, matches the entire published table-data file, and independently counts 239 and 299 orbits by generator traversal. It also directly checks the standard nonsplit Frobenius involution fixes 1,037 supports. The output in `verification/output.txt` terminates in `HESSE_AFFINE_CHAMBER_11_CLASSES_OK` and was reproduced directly from the embedded package.

## Relationship to prior work
Artebani–Dolgachev (arXiv:math/0611590) provide the nine-point/twelve-line geometry, four \(I_3\) fibers, and projective Hessian group of order 216. Bauer–Funke–Neumann (arXiv:0912.0958) prove the chamber/negative-support correspondence, and Bauer–Schmitz (arXiv:1204.4373) develop general exact counting methods. The previous published Hesse-chamber computation already proves the four support restrictions and the exact 50,165 geometric count; these are expressly prior results. Its complete `RESULT.md` contains no affine conjugacy-class fixed-support table, 239/299 orbit count, or 1,037 rational nonsplit count. The new contribution is the **equivariant classification and finite-field descent**, not a repeated geometric chamber census. A general negative-support algorithm does not itself state this eleven-class arithmetic enumeration. Searches did not identify an earlier equivalent fixed-class table, but historical priority remains provisional.

## Limitations
The classification is for this Hesse 21-curve configuration and its affine incidence symmetries. The 432-element abstract combinatorial group must not be conflated with the 216-element complex projective Hessian automorphism group. For arbitrary arithmetic forms, fixed-support counts are conditional on the Frobenius affine type; no existence claim for every such type is made. Characteristics three and other changes in the negative-curve configuration are excluded. The calculations are exact but have not received independent expert validation. Unindexed prior computations may contain related orbit data.

## References
1. M. Artebani and I. Dolgachev, *The Hesse pencil of plane cubic curves*, arXiv:math/0611590, first public 2006-11-19, §§1–2 and 5; https://arxiv.org/abs/math/0611590.
2. T. Bauer, M. Funke and S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958, first public 2009-12-04, Proposition 1.1; https://arxiv.org/abs/0912.0958.
3. T. Bauer and D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373, first public 2012-04-19, §1; https://arxiv.org/abs/1204.4373.
4. *The Zariski-chamber polynomial of the Hesse rational elliptic surface*, published published-finding corpus finding, 2026-11-08, full RESULT.md inspected; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-zariski-chamber-polynomial-of-the-hesse-rational-elliptic-su--ad77c7e792a1.
