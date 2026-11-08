# A rank census of square-zero derivations on characteristic-two evolution algebras

## Finding
For every even prime power \(q\) and integer \(r\ge2\), define the \((r+1)\)-dimensional algebra \(E_{r,q}\) over \(\mathbb F_q\) by a basis \(e_1,\ldots,e_r,z\) and products \(e_i^2=z\), with all other basis products zero. We determine the complete distribution by rank of **labeled derivations** \(D\) satisfying \(D^2=0\). This also determines the homology-dimension distribution of the differential algebra \((E_{r,q},D)\).

Put \(V=\langle e_1,\ldots,e_r\rangle\), with dot-product form \(B(v,w)=\sum_i v_iw_i\). A derivation has a unique decomposition
\[D(v+az)=Tv+f(v)z,\qquad T=T^{\mathsf T}\in\operatorname{End}(V),\quad f\in V^*.\]
It is square-zero if and only if \(T^2=0\) and \(fT=0\).

For \(0\le s\le\lfloor r/2\rfloor\), define \(C_r(s,q)=I_r(s,q)S_s(q)\). The exact enumerator is
\[\boxed{F_{r,q}(u)=\sum_{s=0}^{\lfloor r/2\rfloor} C_r(s,q)\left(q^s u^s+(q^{r-s}-q^s)u^{s+1}\right).}\]
The coefficient of \(u^d\) is precisely the number of such derivations of rank \(d\). The value \(F_{r,q}(1)\) counts all of them. Their homology has dimension \(r+1-2d\).

The factors are explicit. Write
\[J_a(s,q)={a\brack s}_q\prod_{j=0}^{s-1}(q^{a-j}+1),\qquad J_a(s,q)=0\ \text{when }s<0\text{ or }s>a.\]
Then
\[I_{2a+1}(s,q)=J_a(s,q),\qquad I_{2a}(s,q)=q^sJ_{a-1}(s,q)+J_{a-1}(s-1,q).\]
Here \({a\brack s}_q\) is the Gaussian binomial coefficient. Furthermore \(S_0(q)=1\), and for \(a\ge0\) or \(a\ge1\), respectively,
\[S_{2a+1}(q)=\frac{|\mathrm{GL}_{2a+1}(q)|}{|\mathrm{Sp}_{2a}(q)|},\quad S_{2a}(q)=\frac{|\mathrm{GL}_{2a}(q)|}{q^{2a-1}|\mathrm{Sp}_{2a-2}(q)|}+\frac{|\mathrm{GL}_{2a}(q)|}{|\mathrm{Sp}_{2a}(q)|}.\]
As usual \(|\mathrm{GL}_m(q)|=\prod_{j=0}^{m-1}(q^m-q^j)\), \(|\mathrm{Sp}_{2a}(q)|=q^{a^2}\prod_{j=1}^a(q^{2j}-1)\), and the empty products equal one.

In particular, a square-zero derivation has rank at most \(\lfloor(r+1)/2\rfloor\). For odd \(r=2a+1\) this bound is attained by exactly
\[I_r(a,q)S_a(q)q^a(q-1)\]
derivations, all with zero homology. For even \(r\), no acyclic square-zero derivation exists.

## Assumptions and scope
All fields in the counting theorem have \(q=2^b\) elements, \(b\ge1\); the integer \(r\) is arbitrary, \(r\ge2\). The algebra is a fixed, labeled, finite-dimensional, commutative associative nilpotent evolution algebra, with \(E^2=\mathbb F_qz\), \(E^3=0\). “Rank” means rank of the underlying linear map on \(E\); two conjugate derivations are counted separately. No restriction to invertible or inner derivations is made. The structural reduction \(D\leftrightarrow(T,f)\) holds over any characteristic-two field; the population formulas use a finite field.

## Proof
**1. All derivations.** Since \(z=e_i^2\) and the characteristic is two, every derivation satisfies \(D(z)=2e_iD(e_i)=0\). Thus write \(D(e_i)=\sum_jT_{ji}e_j+f_i z\). Applying the Leibniz identity to \(e_ie_j=0\) for distinct \(i,j\) gives \(T_{ij}+T_{ji}=0\), i.e. \(T=T^{\mathsf T}\). The diagonal equations impose no further condition. Conversely these conditions suffice on all basis products, so determine all derivations. Multiplication of their block matrices gives \(D^2|_V=(T^2,fT)\), proving the square-zero criterion.

**2. Self-adjoint square-zero endomorphisms.** Fix \(T=T^{\mathsf T}\) with \(T^2=0\) and \(\operatorname{rank}T=s\). Its image \(W=\operatorname{im}T\) is totally \(B\)-isotropic: \(B(Tu,Tv)=B(u,T^2v)=0\). Also \(\ker T=W^\perp\) by nondegeneracy and self-adjointness. Conversely, fixing any totally isotropic \(s\)-space \(W\), a self-adjoint square-zero \(T\) with image exactly \(W\) is equivalent to an isomorphism \(V/W^\perp\longrightarrow W\) which is symmetric under \(V/W^\perp\simeq W^*\). Such isomorphisms are in bijection with nondegenerate symmetric bilinear forms on \(W^*\), of which there are \(S_s(q)\). This proves \(C_r(s,q)=I_r(s,q)S_s(q)\) without any appeal to a small-dimensional computation.

**3. Isotropic subspace counts.** Let \(c=(1,\ldots,1)\). In characteristic two, \(B(v,v)=\bigl(B(v,c)\bigr)^2\), so any totally isotropic subspace lies in \(H=c^\perp\). If \(r=2a+1\), then \(B(c,c)=1\); the restriction to \(H\) is symplectic and nondegenerate, of dimension \(2a\). If \(r=2a\), then \(B(c,c)=0\) and \(H\) has radical \(\langle c\rangle\), with symplectic quotient of dimension \(2a-2\). Every isotropic \(s\)-plane containing \(c\) is the inverse image of an isotropic \((s-1)\)-plane in the quotient. Every isotropic \(s\)-plane avoiding \(c\) is a graph over an isotropic \(s\)-plane in the quotient, with \(q^s\) choices of graph. The standard symplectic flag count is \(J_a(s,q)\); this proves the displayed formulas for \(I_r\).

**4. Nonsingular symmetric forms.** Over a finite field of even order, there is one congruence class of nonsingular *nonalternating* symmetric forms in each positive dimension. In odd dimension \(2a+1\), its isometry group has order \(|\mathrm{Sp}_{2a}(q)|\). In even dimension \(2a\), that group has order \(q^{2a-1}|\mathrm{Sp}_{2a-2}(q)|\). An additional *alternating* congruence class exists in even dimension, with isometry group \(\mathrm{Sp}_{2a}(q)\). Orbit–stabilizer under \(\mathrm{GL}_s(q)\) yields exactly the formulas for \(S_s(q)\), including \(S_0(q)=1\). These are standard bilinear-form counts, not a novelty claim.

**5. The added functional and actual rank.** For fixed \(T\) of rank \(s\), the condition \(fT=0\) means \(f\) annihilates \(W=\operatorname{im}T\), leaving \(q^{r-s}\) choices. The rank of the block map \(D(v)=(Tv,f(v))\) is \(s\) precisely when \(f\) also vanishes on \(\ker T\); there are \(q^s\) such functionals because \(\dim V/\ker T=s\). The remaining \(q^{r-s}-q^s\) yield rank \(s+1\). Multiplying by \(C_r(s,q)\) and summing proves \(F_{r,q}(u)\).

**6. Homology and acyclicity.** For \(D^2=0\), \(\dim\ker D/\operatorname{im}D=(r+1)-2\operatorname{rank}D\). If \(r=2a\), the largest rank is \(a\): at \(s=a\) the extra rank term vanishes, and smaller \(s\) give rank at most \(a\). If \(r=2a+1\), the only rank-\((a+1)\) maps arise at \(s=a\), contributing \(C_r(a,q)(q^{a+1}-q^a)=I_r(a,q)S_a(q)q^a(q-1)\). This proves the exact acyclic count.

## Verification
The included `checker.py` enumerates **the original derivation and square-zero equations** over \(\mathbb F_2\) in dimensions \(r+1=3,4\), without using the structural classification. It independently enumerates all symmetric square-zero \(T\), all permitted \(f\), and their actual ranks for \(r=2,3,4\) over \(\mathbb F_2\) and \(r=2,3\) over \(\mathbb F_4\). Finite-field multiplication for \(\mathbb F_4\) is implemented from \(\mathbb F_2[u]/(u^2+u+1)\), not by a floating-point approximation. It recomputes the finite orthogonal/symplectic formulas and compares all rank cells. The exact output, recorded in `checker_output.txt`, ends with `EVOLUTION_SQUAREZERO_RANK_CENSUS_PASS`.

Examples of the rank distributions, ordered from rank zero upward, are \((1,5)\) for \((r,q)=(2,2)\), \((1,13,6)\) for \((3,2)\), \((1,29,90)\) for \((4,2)\), \((1,27)\) for \((2,4)\), and \((1,123,180)\) for \((3,4)\). These finite experiments are consistency checks, **not a proof** of the formulas for unbounded \(r\) or arbitrary finite fields.

Reproduction: with Python 3, in the directory containing the two files, run `python checker.py` and compare the resulting UTF-8 output to `checker_output.txt`. The proof does not depend on installation of third-party packages.

## Relationship to prior work
Camacho, Gómez, Omirov and Turdibaev [1] studied derivations of **complex** evolution algebras, especially evolution matrices of full rank or rank one below full; those hypotheses do not cover the characteristic-two algebra above (its evolution-matrix rank is one for \(r\ge2\)). The arithmetic characteristic-two identity \(2e_iD(e_i)=0\) creates a larger derivation algebra.

Brouwer, Gow and Sheekey [2] gave a deep **prior enumeration of nilpotent self-adjoint matrices**, including shape-by-shape counts that cover the symmetric square-zero \(T\) subproblem. The existence and counts of these \(T\) are **not independently claimed as new**. The finding here concerns derivations of the specified algebra, the additional functional condition \(fT=0\), and the distribution of their **full** ranks and differential homology. Those are not stated or implied by a calculation of symmetric matrices alone without the algebraic derivation correspondence and fiber-rank argument. The overlap risk of an unlocated broader derivation census remains.

Mukhamedov, Khakimov, Omirov and Qaralleh [3] study evolution algebras of maximal nilindex over characteristic-zero fields, rather than our nilindex-three, characteristic-two family. A later structural work on commutative algebras with one-dimensional square [4] describes the underlying algebra class; no exact square-zero derivation rank census was identified in the accessible material. A 2026 survey of evolution-algebra derivations [5], including its section 1.6.2, records the complex full-rank results and graph-based derivation theorems but states no analogous finite-field square-zero differential census. Historical priority is not certified.

## Limitations
Only **square-zero** derivations, not arbitrary higher nilpotence indices, are counted; the result is not a conjugacy classification or a classification of differential algebra isomorphism classes. The derivation scheme's nilpotent structure is not studied. Nonperfect characteristic-two fields satisfy the structural reduction, but the formulas for \(S_s(q)\) and enumeration here assert only finite fields. The comparison with [4] is restricted by full-text access. The possible existence of an unlocated broader classification is a residual originality risk. Independent validation has not been performed.

## References
[1] L. M. Camacho, J. R. Gómez, B. A. Omirov, R. M. Turdibaev, “The derivations of some evolution algebras,” arXiv:1004.1936v1, first publicly posted 2010-04-12. https://arxiv.org/abs/1004.1936

[2] A. E. Brouwer, R. Gow, J. Sheekey, “Counting symmetric nilpotent matrices,” *Electronic Journal of Combinatorics* 21(2), P2.4 (2014). https://doi.org/10.37236/3810 ; public full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p4/pdf/

[3] F. Mukhamedov, O. Khakimov, B. Omirov, I. Qaralleh, “Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex,” arXiv:1805.10285v1, first posted 2018-05-25. https://arxiv.org/abs/1805.10285

[4] “Commutative Algebras with One-Dimensional Square,” *Mediterranean Journal of Mathematics*, DOI:10.1007/s00009-025-02812-7 (2025). https://doi.org/10.1007/s00009-025-02812-7

[5] I. Kaygorodov, C. Martín González, A. Viruel, “Evolution algebras: a survey of results and a list of open problems,” arXiv:2610.22248v1, first posted 2026-10-15. https://arxiv.org/html/2610.22248v1
