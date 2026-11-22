# Signed three-tap convolution has seven exact rank strata on the icosahedral rotation group

## Finding

Let \(G=A_5\) be the group of 60 even permutations of five letters. For every ordered choice of pairwise distinct elements \(u,v,w\in G\), with the first two positive sites unordered, define
\[
 k=\delta_u+\delta_v-\delta_w,\qquad (T_k f)(x)=\sum_{s\in G}k(s)f(s^{-1}x).
\]
There are exactly \(\binom{60}{2}\cdot58=102{,}660\) distinct signed kernels of this form. The possible complex ranks of the 60-dimensional convolution operator, and the exact numbers of kernels realizing each, are:

| \(\operatorname{rank}_{\mathbb C}T_k\) | \(\dim\ker T_k\) | signed kernels |
|---:|---:|---:|
| 40 | 20 | 1,800 |
| 45 | 15 | 3,600 |
| 49 | 11 | 3,600 |
| 54 | 6 | 3,600 |
| 55 | 5 | 7,200 |
| 56 | 4 | 10,800 |
| 60 | 0 | 72,060 |
| **total** | | **102,660** |

There is an intrinsic rank test requiring only three group-element orders, a generated-subgroup order, and—on one exceptional stratum—a relative five-cycle conjugacy flag. Let
\[
 a=u^{-1}v,\quad b=u^{-1}w,\quad h=|\langle a,b\rangle|,\quad r=\operatorname{ord}(a),\quad (s,t)=\operatorname{sort}\{\operatorname{ord}(b),\operatorname{ord}(a^{-1}b)\}.
\]
The rank is 60 unless exactly one of the following mutually exclusive cases applies:

| \(r\) | \((s,t)\) | \(h\) | Additional condition | Rank |
|:---:|:---:|---:|---|---:|
| 3 | (2,2) | 6 | none | 40 |
| 3 | (3,3) | 12 | none | 45 |
| 3 | (5,5) | 60 | the two order-five quotients lie in the **same** \(A_5\)-conjugacy class | 49 |
| 2 | (5,5) | 60 | none | 54 |
| 5 | (2,5) | 60 | none | 55 |
| 5 | (2,3) | 60 | none | 56 |
| 5 | (3,3) | 60 | none | 56 |

The two conjugacy classes of order-five elements, each of size twelve, are closed under inversion. Thus the flag does not depend on how the two relevant quotients are oriented. In the (3,(5,5),60) geometry, *different* five-cycle classes instead give rank 60. The two positive sites may be exchanged without changing any prediction.

## Assumptions and scope

Coefficients are exactly \((+1,+1,-1)\), on three distinct group elements; the two positive sites are not labeled. Every signed kernel is included, not only generating supports or inverse-closed sets. The representation is the regular complex group algebra with **unnormalized** convolution, and the rank concerns complex-linear image dimension, not the spectrum of a self-adjoint graph adjacency matrix. The standard lexicographic order on even permutations of \((0,1,2,3,4)\) indexes the exact certificate tables; multiplication is function composition \((pq)(j)=p(q(j))\). No assumption of graph undirectedness, nonnegativity, or group commutativity is made.

## Proof

**Reduction.** Left translation of \(k\) by \(u^{-1}\) multiplies the convolution operator by an invertible regular translation and changes its support to \(\{e,a,b\}\), with coefficients \((1,1,-1)\). Interchanging the two positive sites replaces \((a,b)\) by \((a^{-1},a^{-1}b)\). Conjugating the pair by any element of \(S_5\) induces an automorphism of \(A_5\), hence a permutation similarity of the regular convolution matrix. These operations preserve rank. There are precisely \(59\cdot58=3422\) normalized ordered pairs \((a,b)\), and the actions partition them into 23 disjoint orbits. `orbit_table.csv` lists a representative, orbit size, signed-kernel multiplicity, exact rank, all three pairwise orders and generated-subgroup order. The first script generates the group and all 120 conjugations from permutation arithmetic, regenerates every orbit, checks that its lexicographically smallest pair is the listed representative, that the 23 orbits are disjoint and exhaustive, and that their sizes sum to 3422. This is a finite, specified algorithm rather than an appeal to an external enumeration.

**Exact rank verification.** For \(a,b\ne e\), \(a\ne b\), the 60-by-60 integer matrix is
\[
 M_{x,y}=\mathbf1_{x=y}+\mathbf1_{x=ay}-\mathbf1_{x=by},\qquad x,y\in A_5.
\]
Each row and column has exactly three nonzero entries, two \(+1\) and one \(-1\). Consequently every square minor of size at most 60 has absolute determinant at most \(3^{30}=205891132094649\) by Hadamard's inequality. The two distinct primes \(p_1=1000000007\), \(p_2=1000000009\) satisfy \(p_1p_2=1000000016000000063>2\cdot 3^{30}\). The exact modular checker computes the full row-echelon rank of **each of the 3422 normalized matrices** modulo both primes and checks agreement with the displayed 23-orbit table. If the common modular rank is \(d\), every \((d+1)\)-minor is divisible by both primes, and hence vanishes as an integer by the determinant bound, while a nonzero \(d\)-minor modulo either prime is nonzero over \(\mathbb C\). Therefore the true characteristic-zero rank is exactly \(d\), not merely bounded below by \(d\). All intermediate products fit within signed 64-bit arithmetic: residues are strictly below \(10^9+9\), so any residue product is less than \((10^9+9)^2<2^{63}\). Independently, `verify_rational.py` re-creates the 23 representative matrices with a different multiplication implementation and computes their ranks using exact rational sparse-matrix elimination.

**Complete signed-kernel count.** Each signed kernel has two ordered descriptions of its positive sites. The normalization \((u,v,w)\mapsto(u,u^{-1}v,u^{-1}w)\) is bijective on such ordered descriptions, so an orbit containing \(c\) normalized pairs accounts for exactly \(60c/2=30c\) signed kernels. Summing the checked orbit counts by rank gives exactly the seven multiplicities in the first table. The intrinsic test is obtained by grouping the 23 checked orbits according to the orders of \(a,b,a^{-1}b\) and their generated subgroup. The only equal-invariant pair with different ranks has \(r=3\), \((s,t)=(5,5)\), \(h=60\): its two orbits are distinguished by the same/different \(A_5\) five-cycle-class flag. The flag is determined in the certificate by exact conjugation within \(A_5\). This proves every assertion for every valid signed kernel.

## Verification

From a directory containing `orbit_table.csv`, `verify_modular.py`, `verify_rational.py`, and `requirements.txt`, install the versions listed in `requirements.txt` and execute `python3 verify_modular.py` and `python3 verify_rational.py`. Both scripts contain assertions covering their entire checked domains and print an exact-rank histogram on success. The modular script checks all 3422 normalized pairs at two primes, recalculates all 23 orbit sizes and all 102660 signed-kernel multiplicities. The second script checks all 23 orbit representatives over the rationals. Prime moduli and Hadamard arithmetic are explicit above; no probabilistic rank test, floating point tolerance, unproved infinite extrapolation, or previously generated log is needed. The table in `orbit_table.csv` is evidence only in conjunction with both scripts and the orbit-completeness assertion.

## Relationship to prior work

General nonabelian Fourier-support uncertainty bounds [1] and group-convolution/block-factorization methods [2] establish the general framework; neither implies the seven exact signed-mask ranks and their counts. A published complete unsigned three-point classification on \(A_5\) [3] treats coefficients \((+1,+1,+1)\), with different attainable nullities \(0,4,5,10,20,40\), whereas here the nullity 11 occurs 3600 times and the unsigned spectrum does not determine it. This coefficient change is not generally removable by a character twist: \(A_5\) is perfect and has no nontrivial homomorphism to \(\{\pm1\}\). The particularly sharp same/different five-cycle-class transition at rank 49 is sign-sensitive. Siemons and Zalesski [4] study undirected Cayley graphs with conjugation-invariant connection sets, which does not cover arbitrary signed, nonnormal, non-inverse-closed three-point kernels. These comparisons concern hypotheses and implications, not title matches.

## Limitations

The classification concerns one fixed natural sign pattern on one finite simple group. It is not a theorem for arbitrary complex coefficients, other groups, or the singular values beyond their zero multiplicities. The computation-based finite proof requires verification of the transparent supplied scripts and is not an independent audit. Priority remains vulnerable to an unindexed equivalent signed-Cayley or group-ring enumeration. The 2004 A5 small-valency digraph symmetry papers were considered by abstracts/available excerpts only; they do not directly furnish a spectral-rank comparison from the material read. No quantitative conditioning estimate is claimed.

## References

[1] G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702, first posted 2006-08-28, especially Theorem 2 and the finite-group discussion. https://arxiv.org/html/math/0608702v2

[2] M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, Electronic Journal of Combinatorics 20(3) (2013), #P57, DOI 10.37236/3105. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v20i3p57

[3] *Exact three-tap convolution nullities on the icosahedral rotation group*, public mathematical research note (2026), full finding and proof. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-exact-three-tap-convolution-nullities-on-the-icosahedral-rotatio--49866d6f62a3/RESULT.md

[4] J. Siemons and A. Zalesski, *Remarks on singular Cayley graphs and vanishing elements of simple groups*, Journal of Algebraic Combinatorics 50 (2019), 379–401, DOI 10.1007/s10801-018-0860-0. https://link.springer.com/article/10.1007/s10801-018-0860-0

[5] X.-G. Fang, Z.-P. Lu, J. Wang and M.-Y. Xu, *Cayley Digraphs of Finite Simple Groups with Small Out-Valency*, Communications in Algebra 32 (2004), 1201–1211, DOI 10.1081/AGB-120027974. https://www.tandfonline.com/doi/abs/10.1081/AGB-120027974
