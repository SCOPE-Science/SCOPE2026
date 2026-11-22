# Lagrangian incidence shattering: isotropic partial frames and exact finite topology

## Finding

Let \(V\) be a \(2n\)-dimensional vector space over \(\mathbb F_q\), with \(n\geq1\), \(q\) a prime power, and a nondegenerate alternating bilinear form \(\omega\). Let \(X=V\setminus\{0\}\), and let \(\mathcal L\) be the family of all maximal totally isotropic (Lagrangian) \(n\)-subspaces, regarded as Boolean point-incidence concepts on \(X\).

**Theorem.** A finite support \(S\subseteq X\) is shattered by \(\mathcal L\) if and only if its vectors are linearly independent and mutually orthogonal under \(\omega\). Thus its shattering complex is the complex of independent isotropic partial vector frames, and

\[
\Phi_{q,n}(z)=\sum_{k=0}^{n}\frac{z^k}{k!}\prod_{i=0}^{k-1}(q^{2n-i}-q^i),\qquad
\operatorname{VCdim}(\mathcal L)=\operatorname{Ldim}(\mathcal L)=n.
\]

Every maximal shattered support has size \(n\), so the complex is pure. For \(n\geq2\) it is neither a matroid independence complex nor a flag complex. For \(q=2\), in ranks \(n=1,2,3\), respectively, the complete polynomials are

\[
1+3z,\quad 1+15z+45z^2,\quad 1+63z+945z^2+3780z^3,
\]

and the only nonzero reduced mod-two Betti numbers are, respectively,
\[
\widetilde\beta_0=2,\qquad\widetilde\beta_1=31,\qquad\widetilde\beta_2=2897.
\]

## Assumptions and scope

The bilinear form is alternating and nondegenerate. Points are **nonzero vectors**, not projective one-spaces: distinct scalar multiples are distinct queries but cannot occur together in a shattered support. A concept contains a point exactly when the point lies in its Lagrangian subspace. Boolean shattering requires all \(2^{|S|}\) membership labels, including all-negative. All statements hold over arbitrary prime-power fields. The mod-two homology numbers are asserted **only** for binary fields and ranks at most three; they are not claims of integral homology or homotopy type.

## Proof

1. **Necessity.** The all-positive labeling of a shattered support \(S\) has a Lagrangian witness, so \(\omega(s,t)=0\) for every \(s,t\in S\). If \(S\) is dependent, choose a minimal dependent subfamily \(T\subseteq S\) and \(t\in T\) in the span of \(T\setminus\{t\}\). The labeling making the latter vectors positive and \(t\) negative is impossible for a vector subspace. Therefore \(S\) is independent and isotropic.

2. **Sufficiency.** An ordered independent isotropic support \(S=(s_1,\ldots,s_k)\) extends by the symplectic basis extension theorem to a symplectic basis \((e_1,\ldots,e_n,f_1,\ldots,f_n)\) with \(e_i=s_i\) for \(i\leq k\) and \(\omega(e_i,f_j)=\delta_{ij}\). For each requested positive-index set \(P\subseteq\{1,\ldots,k\}\), let \(L_P\) be the span of \(e_i\) for \(i\in P\), \(f_j\) for \(j\in\{1,\ldots,k\}\setminus P\), and \(e_l\) for \(k<l\leq n\). These \(n\) generators form a pairwise orthogonal independent family, so \(L_P\) is Lagrangian. It contains \(s_i\) exactly when \(i\in P\), by linear independence of the displayed symplectic basis. Hence every labeling occurs.

3. **Counting and purity.** After choosing an isotropic independent ordered \(i\)-tuple, its span \(W\) is isotropic of dimension \(i\); the next vector must lie in \(W^\perp\setminus W\), which has \(q^{2n-i}-q^i\) elements. Division by \(k!\) counts unordered supports. Such sets extend to an isotropic basis of a Lagrangian, giving purity and largest size \(n\).

4. **Exact online dimension.** The static dimension \(n\) gives the online lower bound. A nontrivial first query \(v\ne0\) in a shattered online tree splits the concepts into those containing \(v\) and those avoiding it. The containing family is naturally the Lagrangian incidence system of \(v^\perp/\langle v\rangle\), a symplectic space of rank \(n-1\): every remaining query either has constant value or descends to a nonzero quotient point (possibly duplicated). Therefore this positive branch has online dimension at most \(n-1\). Induction, starting with the rank-zero singleton family, excludes a tree of depth \(n+1\), establishing equality.

5. **Not matroidal or flag for \(n\geq2\).** Choose symplectic basis vectors \(e_1,e_2,f_1,f_2\). The support \(\{e_1,e_2\}\) is shattered, whereas \(\{f_1+f_2,e_i\}\) is not, for either \(i=1\) or \(i=2\), violating the matroid exchange axiom. The three distinct vectors \(e_1,e_2,e_1+e_2\) have pairwise shattered supports but their triple is dependent, so the complex is not flag.

6. **Exact binary finite homology.** At rank one the complex consists of three isolated vertices. At rank two it has fifteen vertices and 45 edges, with augmented boundary ranks \((1,14)\), yielding \(\widetilde\beta_1=45-14=31\). At rank three the face numbers in cardinalities \(0,1,2,3\) are \((1,63,945,3780)\). The augmented binary boundary ranks in cardinalities \(1,2,3\) are \((1,62,883)\), giving \(\widetilde\beta_0=63-1-62=0\), \(\widetilde\beta_1=945-62-883=0\), and \(\widetilde\beta_2=3780-883=2897\). These are exact finite-matrix computations, not deductions from Euler characteristic alone.

## Verification

Three standalone checkers are included. The first constructs all binary Lagrangians recursively from isotropic bases, independently tests all supports of cardinalities at most \(n\) against the actual Boolean trace family, and performs Gaussian elimination over \(\mathbb F_2\). The second, in C++17, enumerates independent isotropic generating tuples and deduplicates their spans, checks all Boolean traces and separately computes binary boundary ranks. Both reproduce 3, 15 and 135 Lagrangians for binary ranks one to three, together with all displayed face counts and boundary ranks. A separate ternary-field checker finds 40 Lagrangians in rank two and confirms all 80 singleton supports and 960 shattered two-point supports by exhaustive traces.

Reproduce using only a Python 3 interpreter and C++17 compiler:

```sh
python3 checks/lagrangian_check.py
python3 checks/lagrangian_q3.py
c++ -std=c++17 -O2 checks/lagrangian_independent.cpp -o lagrangian_check
./lagrangian_check
```

## Relationship to prior work

The geometric terminology, extension of isotropic bases and Lagrangian incidence families are standard; they are not claimed as discoveries. Bhaskar (2017) develops online/thicket shattering as a model-theoretic concept but does not calculate the finite Lagrangian membership system. Yao, Lv and Wang (2020) study maximal intersecting subfamilies of symplectic polar-space subspaces, not the full Boolean projection traces on point supports. Piterman (2023) studies a different frame complex whose vertices are **nondegenerate two-dimensional subspaces**, not nonzero isotropic vectors; its homology and spectral calculations do not give this complex's homology. The published fixed-rank affine-flat shattering characterization concerns all affine flats without symplectic isotropy constraints and does not determine this formula or complex. A published complete-flag shattering result concerns nested subspace queries, not point-incidence of Lagrangian generators.

## Limitations

The polynomial and online-dimensional statements are proved for all prime powers and ranks. The mod-two ranks are finite exact calculations for three small binary ranks; no integral torsion, shellability, general-rank homology or homotopy-type theorem is claimed. Literature indexing is incomplete, and an equivalent earlier classification of independent isotropic partial frames or their topology may exist under different terminology. No independent external mathematical audit has been performed.

## References

- Siddharth Bhaskar, *Thicket Density*, arXiv:1702.03956, first public 2017-02-13. https://arxiv.org/html/1702.03956v4
- Tian Yao, Benjian Lv, Kaishun Wang, *Non-trivial \(t\)-intersecting families for symplectic polar spaces*, arXiv:2010.05030, first public 2020-10-10. https://arxiv.org/abs/2010.05030
- Kevin I. Piterman, *On the frame complex of symplectic spaces*, arXiv:2305.02940, first public 2023-05-04. https://arxiv.org/html/2305.02940v1
- Related published computational results: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fixed-rank-affine-flat-shattering-complexes-over-finite-fields--6e9f3ce9d85a and https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-flag-shattering-gaussian-multinomial-supports-and-exact--e221fe2ce784
