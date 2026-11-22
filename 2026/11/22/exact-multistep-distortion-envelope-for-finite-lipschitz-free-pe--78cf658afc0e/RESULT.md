# Exact multistep distortion envelope for finite Lipschitz-free permutation operators

## Finding

For every integer \(n\ge3\), set
\[
\mathcal P_n=\{2,3,\ldots,n\}\cup
\{\operatorname{lcm}(a,b): a,b\ge1,\ a+b\le n\},
\qquad
B_n(k)=\max_{\ell\in\mathcal P_n}((-k)\bmod\ell),
\]
where \(k\) is a nonnegative integer and the remainder lies in \(\{0,\ldots,\ell-1\}\). Let \(\mathcal F(M)\) be the real Lipschitz-free Banach space of a finite metric space \(M\); any permutation \(f\) induces its canonical linear operator \(U_f\) on \(\mathcal F(M)\). Write
\[
\operatorname{def}_-(f)=\max_{x\ne y}\bigl(d(x,y)-d(fx,fy)\bigr)_+.
\]
Among **all** metrics on \(n\) labeled points with every off-diagonal distance in \([1,2]\), and all permutations with \(\operatorname{def}_-(f)\le\varepsilon\), the sharp norm of the \(k\)-th iterate is
\[
\boxed{\quad
H_{n,k}(\varepsilon):=\max\|U_f^k\|
=1+\min\{1,\varepsilon B_n(k)\}\quad}
\qquad(k\ge0,\ \varepsilon\ge0).
\]
Every maximum is attained by an explicit metric and permutation. For \(n=2\), \(H_{2,k}(\varepsilon)=1\) for all \(k\) and \(\varepsilon\).

For each \(n\ge3\) and every \(\varepsilon>0\), the sequence \(k\mapsto H_{n,k}(\varepsilon)\) has **least positive period**
\[
\boxed{K_n=\operatorname{lcm}(1,2,\ldots,n).}
\]
Moreover, writing \(L_n=\max\mathcal P_n\), the initial time range has the exact linear law
\[
B_n(k)=L_n-k\qquad
\bigl(1\le k\le\lfloor(L_n+1)/2\rfloor\bigr).
\]
The one-step constant \(L_n-1\) is known from the sharp uniform-plasticity estimate of Kadets and Zavarzina (2023); the new assertion is the complete multistep envelope and its least-period law.

## Assumptions and scope

The metric is real, symmetric and defined on precisely \(n\) distinct points, with \(1\le d(x,y)\le2\) when \(x\ne y\). No graph metric, ultrametric or Euclidean embedding is assumed. \(f\) ranges over all bijections of those points, not arbitrary noninjective maps. The defect uses *additive* distance decrease in one application of \(f\), not the defect of \(f^k\). The operator \(U_f\) acts on mass-zero molecules by
\[
U_f\Bigl(\sum_{x\in M}a_x\delta_x\Bigr)
=\sum_{x\in M}a_x\delta_{f(x)},\qquad\sum_{x\in M}a_x=0,
\]
so its definition is independent of the chosen base point. \(\|U_f^k\|=\operatorname{Lip}(f^k)\) by the elementary molecule norm and the universal property of \(\mathcal F(M)\).

The restriction to distances in \([1,2]\) is natural and essential to the simple extremal construction: **every** symmetric assignment of off-diagonal distances in that interval satisfies the triangle inequality. Without a lower-distance bound, an additive defect cannot give the same universal relative operator-norm bound.

## Proof

**1. Exact pair-orbit periods.** A permutation acts on the unordered pairs \(\{x,y\}\). If the two points lie in distinct cycles of lengths \(a\) and \(b\), their pair has period \(\operatorname{lcm}(a,b)\) with \(a+b\le n\). If they lie in one cycle of length \(a\), their unordered-pair period divides \(a\) and hence is no greater than \(a\le n\). Conversely, every period \(3\le\ell\le n\) occurs from adjacent points of an \(\ell\)-cycle, period \(2\) occurs from a transposition and a fixed point, and period \(\operatorname{lcm}(a,b)\) occurs from points in disjoint cycles of those lengths. Thus, for \(n\ge3\), the attainable periods are exactly \(\mathcal P_n\); the only pair period for \(n=2\) is \(1\).

**2. Upper bound.** Fix a pair \(P_0\) in an orbit of length \(\ell\). Write \(P_j=f^j(P_0)\) for indices modulo \(\ell\), and let \(r=k\bmod\ell\). If \(r=0\), the \(k\)-th iterate preserves the distance of this pair. Otherwise, the remaining \(\ell-r\) forward steps from \(P_r\) back to \(P_0\) each decrease distance by at most \(\varepsilon\). Telescoping yields
\[
d(P_r)-d(P_0)\le(\ell-r)\varepsilon.
\]
Since \(d(P_0)\ge1\) and every image distance is at most \(2\),
\[
\frac{d(f^kx,f^ky)}{d(x,y)}
\le1+\min\{1,\varepsilon((-k)\bmod\ell)\}.
\]
Taking the maximum over unordered pairs and using \(\|U_f^k\|=\operatorname{Lip}(f^k)\) proves \(H_{n,k}\le1+\min\{1,\varepsilon B_n(k)\}\).

**3. Sharp construction.** Suppose \(B_n(k)>0\), and select an attainable pair period \(\ell\) at which its maximum occurs. Choose a permutation with an orbit \(P_0,P_1,\ldots,P_{\ell-1}\) of that length. Let \(r=k\bmod\ell\), so \(1\le r<\ell\), and put \(h=\min\{\varepsilon,1/(\ell-r)\}\). On this orbit prescribe
\[
d(P_j)=\begin{cases}
1,&0\le j<r,\\
1+(\ell-j)h,&r\le j<\ell.
\end{cases}
\]
Give every other unordered pair distance \(1\). All prescribed distances lie in \([1,2]\), so the triangle inequality holds. The only strictly decreasing successive steps in the chosen orbit have decrement exactly \(h\); all other pair orbits retain constant distance. Thus \(\operatorname{def}_-(f)\le h\le\varepsilon\), while \(P_0\) has distance \(1\) and its image after \(k\) steps, \(P_r\), has distance \(1+(\ell-r)h\). Consequently
\[
\|U_f^k\|\ge1+\min\{1,\varepsilon B_n(k)\},
\]
which proves equality. When \(B_n(k)=0\), all pair distances are fixed by \(f^k\), so every admissible induced operator has norm \(1\). An equilateral metric supplies an attainer. The \(n=2\) assertion follows because the only unordered pair is fixed by every permutation.

**4. Exact temporal period.** Every \(\ell\in\mathcal P_n\) divides \(K_n\), since \(\ell\) is a least common multiple of cycle lengths no greater than \(n\). Thus \(B_n(k+K_n)=B_n(k)\). Because \(2,3,\ldots,n\) all occur as pair periods, \(B_n(k)=0\) holds **if and only if** \(K_n\) divides \(k\). In particular, any period of this nonnegative sequence must take its zero at \(k=0\) to a zero and hence be divisible by \(K_n\). The least positive period is therefore \(K_n\); the same conclusion holds for \(H_{n,k}(\varepsilon)\) whenever \(\varepsilon>0\).

**5. Initial transient.** For \(1\le k\le\lfloor(L_n+1)/2\rfloor\), the orbit \(\ell=L_n\) gives \(B_n(k)\ge L_n-k\). If \(\ell>k\), its residue is \(\ell-k\le L_n-k\); if \(\ell\le k\), its residue is at most \(\ell-1\le k-1\le L_n-k\). This proves the stated initial linear profile.

## Verification

Run `python3 POWER_CHECK.py` using the Python standard library. The included finite diagnostic exhaustively enumerates permutations through eight points and checks the exact attainable pair periods; for up to fifteen points it checks explicit extremizing metrics, every triangle inequality, sharp iteration norms for a range of time indices and noncontraction tolerances, and the initial linear law. Its successful output was `MULTISTEP_FREE_PERMUTATION_DIAGNOSTIC_OK 5536379`. Those finite checks corroborate, but do not prove, the infinite family of assertions; the proof above is independent of numerical enumeration.

## Relationship to prior work

Kadets and Zavarzina, *Plastic pairs of metric spaces* (2023), Theorems 2.6–2.7 and Lemma 2.5, already prove the sharp one-step bound for finite spaces using exactly the maximum pair-orbit period \(L_n\); this case is credited and not claimed as original. Their theorems do not give the sharp profile of \(\|U_f^k\|\) under an *original one-step defect budget* for each \(k\), nor its least temporal period. Applying their one-step theorem to \(f^k\) provides only a bound through the defect of \(f^k\), which can be strictly weaker. For example, for a pair orbit of length six and \(k=4\), bounding the defect of \(f^4\) by \(4\varepsilon\) and applying an orbit-three inequality allows \(8\varepsilon\) expansion, whereas the direct four-step complementary-path argument gives the sharp \(2\varepsilon\) for that pair orbit.

Duzer, *Compact Quasi-Metric Spaces Are Expand-Contract Plastic* (2026), gives qualitative rigidity for compact spaces, including the zero-defect limit, rather than the nonzero-defect multistep norm envelope. Cúth, Doucha and Titkos (2024) study isometry groups of Lipschitz-free spaces; their classification of *isometric* operators does not imply the sharp norms of these generally non-isometric permutation linearizations. Aliaga, Cúth and Vico (2026) study the strongly unique predual of Lipschitz spaces rather than quantitative norms of permutation iterates. The elementary identity between induced operator norm and Lipschitz constant is classical and is not claimed as new.

## Limitations

The exact result is specific to finite **symmetric** metric spaces with the normalized interval of off-diagonal distances \([1,2]\), and to bijective point maps. No claim is made for quasi-metrics, unbounded aspect ratios, arbitrary nonbijective maps, or norm bounds for general operators on Lipschitz-free spaces. The single-step theorem and maximal pair-period formula are previously known. Unindexed priority and possible reformulations of the multistep envelope are residual bibliographic risks.

## References

1. V. Kadets and O. Zavarzina, *Plastic pairs of metric spaces*, arXiv:2301.06589 (first posted 16 January 2023), especially Section 2.2, Lemma 2.5 and Theorems 2.6–2.7. https://arxiv.org/abs/2301.06589
2. T. Duzer, *Compact Quasi-Metric Spaces Are Expand-Contract Plastic*, arXiv:2610.14301 (first posted 9 October 2026), Theorem 1.1. https://arxiv.org/abs/2610.14301
3. M. Cúth, M. Doucha and T. Titkos, *Isometries of Lipschitz-free Banach spaces*, J. London Math. Soc. 110 (2024), e70000. https://doi.org/10.1112/jlms.70000
4. R. J. Aliaga, M. Cúth and F. Vico, *Lipschitz-free spaces are strongly unique preduals*, arXiv:2609.24392 (first posted 21 September 2026). https://arxiv.org/abs/2609.24392
5. C. Cobollo and A. Peris, *On Disjoint Dynamical Properties and Lipschitz-Free Spaces*, Results Math. 80 (2025), article 16, especially Theorem 4.1 on linearization norms. https://doi.org/10.1007/s00025-024-02319-9
