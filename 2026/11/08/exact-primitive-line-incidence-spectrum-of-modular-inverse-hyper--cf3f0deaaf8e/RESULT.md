# Exact primitive-line incidence spectrum of modular inverse hyperbolas over odd prime powers

## Finding
For every odd prime \(p\) and integer \(k\ge1\), let \(q=p^k\), \(R=\mathbb Z/q\mathbb Z\), and \(H=\{(x,x^{-1}):x\in R^\times\}\). A primitive affine line is a subset \(L(a,b,c)=\{(X,Y)\in R^2:aX+bY=c\}\), where at least one of \(a,b\) is a unit. Count lines as *subsets* of \(R^2\), not as coefficient triples. Let \(N_j\) be the number of lines \(L\) with \(|L\cap H|=j\).

Put \(S=p^{k-1}\), \(U=(p-1)S\), and \(T=q^2+qS\). There are exactly \(T\) primitive affine lines. When \(k=1\),
\[
N_1=3(p-1),\qquad N_2=\frac{(p-1)(p-2)}2,\qquad N_0=\frac{p^2-p+4}{2}.
\]
When \(k\ge2\), all positive entries of the incidence spectrum are **exactly**
\[
N_1=2(p-1)S^2,\qquad N_2=\frac{(p-1)(p-2)}2S^2,
\]
\[
N_{2p^h}=\frac{(p-1)U}{2}\,p^{k-2h-1}
\qquad(1\le h\le\lfloor(k-1)/2\rfloor),
\]
\[
N_{p^{\lfloor k/2\rfloor}}=U,
\qquad N_0=T-\sum_{j\ge1}N_j.
\]
All other \(N_j\) vanish. The positive incidence sizes displayed here are pairwise distinct for odd \(p\).

The **sharp maximum intersection size**, including the number of lines attaining it, is
\[
\begin{array}{c|c|c}
 k&\max_L|L\cap H|&\#\{L:|L\cap H|=\max\}\\ \hline
 1&2&(p-1)(p-2)/2\\
 k\ge2\text{ even}&p^{k/2}&U\\
 k\ge3\text{ odd}&2p^{(k-1)/2}&(p-1)U/2
\end{array}
\]
(where the last two rows apply to the indicated exponents).

In particular, for each fixed odd prime \(p\), the proportion of all primitive affine lines having no point on \(H\) tends, as \(k\to\infty\), to
\[
\frac{p^3+2p^2+2p+3}{2p(p+1)^2}.
\]
For each \(h\ge1\), the proportion having exactly \(2p^h\) points stabilizes at \((p-1)^2/[2p^{2h+1}(p+1)]\) once \(k\ge2h+1\).

## Assumptions and scope
The prime is odd, the modulus is the full prime power \(q=p^k\), and a line is the solution set of one **primitive** linear equation over the ring \(R\). These ring-affine lines are not Euclidean straight lines through the integer representatives of \(H\); the distinction is essential. All counts concern distinct subsets and include empty-intersection lines. No claims are made for the prime \(2\), non-prime-power moduli, or nonprimitive equations.

## Proof
**Step 1 (unique line normalization).** A primitive coefficient row defines a surjective homomorphism \(R^2\to R\) with a free rank-one kernel. Rows giving the same kernel differ by a unit, and equal line subsets have the same kernel and intercept after that rescaling. Therefore each primitive line appears in exactly one of the two canonical families
\[
 X+bY=c\ (b,c\in R),\qquad aX+Y=c\ (a\in pR,\ c\in R).
\]
There are \(q^2+qS=T\) such lines.

**Step 2 (the second family).** On \(H\), the equation \(aX+Y=c\) is \(ax^2-cx+1=0\). For \(a\in pR\), reducing modulo \(p\) shows that there is no root when \(p\mid c\), whereas if \(c\) is a unit there is exactly one root modulo \(p\), namely \(x=c^{-1}\). Its derivative \(2ax-c\) is a unit, so Hensel lifting gives exactly one root in \(R\). Thus this family contributes \(US=(p-1)S^2\) lines with one incidence, and no multiple incidences.

**Step 3 (the first family and unit roots).** On \(H\), \(X+bY=c\) is equivalent to \(x^2-cx+b=0\) with \(x\) a unit. As \(2\) is invertible, \(z=2x-c\) converts the equation into \(z^2=\Delta\), with \(\Delta=c^2-4b\). For each \(c\), the map \(b\mapsto\Delta\) bijects \(R\) with itself. If \(c\) is a unit and \(b\in pR\), there is exactly one unit root by Hensel lifting (the other reduction is zero); this accounts for \(US\) further single-incidence lines. If \(c\) is not a unit and \(b\) is not a unit, the polynomial has no unit root modulo \(p\). In all remaining cases producing solutions, \(b\) is a unit: unit discriminants that are nonzero squares modulo \(p\) give exactly two unit roots, whereas discriminants divisible by \(p\) require \(c\) a unit and are the exceptional cases of Step 4.

The two-root lines with \(c\in pR\) number \(S\cdot (p-1)S/2=(p-1)S^2/2\), because \(-4b\) must be a nonzero square modulo \(p\). Those with \(c\) a unit number \(U\cdot(p-3)S/2\), because the nonzero-square reductions of \(\Delta\) must exclude \(c^2\) (which would give \(b\equiv0\pmod p\)). Their sum is \((p-1)(p-2)S^2/2\).

**Step 4 (higher tangencies).** Suppose \(c\) is a unit and \(p\mid\Delta\). Then every square root \(z\) reduces to zero modulo \(p\), so \(x=(c+z)/2\) is automatically a unit. For \(1\le h\le\lfloor(k-1)/2\rfloor\), a discriminant of exact valuation \(2h\) has \(2p^h\) square roots precisely when its unit factor is a quadratic residue. The number of such discriminants modulo \(p^k\) is \((p-1)p^{k-2h-1}/2\). Multiplying by the \(U\) choices of unit \(c\) yields the formula for \(N_{2p^h}\). If \(\Delta=0\) modulo \(p^k\), there are precisely \(p^{\lfloor k/2\rfloor}\) square roots, and one such discriminant for every unit \(c\): this yields \(N_{p^{\lfloor k/2\rfloor}}=U\). The quadratic-root assertions follow by factoring off \(p^{2h}\), applying Hensel lifting to each of the two square roots of the reduced unit, and allowing \(p^h\) free high digits; zero roots are exactly the multiples of \(p^{\lceil k/2\rceil}\). An odd-valuation discriminant has no square root.

**Step 5 (the field case, maxima, and limits).** For \(k=1\), each of the \(U=p-1\) zero-discriminant lines in Step 4 has one point rather than a multiple incidence, hence \(N_1=2U+U=3U\); the two-point count remains the Step 3 count. Subtraction from \(T=p^2+p\) gives \(N_0\). For \(k\ge2\), subtract the positive counts of Steps 2–4 from \(T\); no further sizes occur. Among positive sizes, \(p^{k/2}\) is greatest for even \(k\), and \(2p^{(k-1)/2}\) is greatest for odd \(k\ge3\), using \(p\ge3\); the counts follow from their rows. Divide each count by \(T=p^{2k}(1+1/p)\). The ratios for one and two intersections are respectively \(2(p-1)/[p(p+1)]\) and \((p-1)(p-2)/[2p(p+1)]\). The ratio for fixed \(2p^h\) is \((p-1)^2/[2p^{2h+1}(p+1)]\), and the remaining exceptional tangency mass tends to zero. Summing the geometric series gives the stated limit for empty lines.

## Verification
A standalone script, `verify.py`, independently enumerates **all** distinct primitive affine lines by the two canonical forms and counts their intersections with \(H\). It checks the predicted full multiplicity dictionary, the total line count, the first-incidence moment, and the claimed sharp maxima for 15 prime-power cases; its observed output is:

```
VERIFY_OK cases=15 all_primitive_lines=292402 first_moment=PASS sharp_maxima=PASS
```

The checked prime powers include \(3,9,27,81,243\), \(5,25,125\), \(7,49,343\), \(11,121\), and \(13,169\). These finite checks support but do not replace the proof for arbitrary \(p,k\).

## Relationship to prior work
Khan, Magner, Senger, and Winterhof (arXiv:1304.6943, §1, particularly Proposition 7) study **Euclidean straight lines** through points in the integer-coordinate lift of a modular hyperbola. They explicitly reduce the intersection bound to square-root counts of a quadratic discriminant, including the same \(2p^h\) and \(p^{\lfloor k/2\rfloor}\) local root multiplicities. The square-root lemma is established antecedent mathematics and is **not** claimed new here. That work does not count primitive ring-affine line subsets, enumerate their entire point-intersection spectrum, or prove its stabilized incidence proportions. The present counting argument adds the canonical ring-line classification, the necessary unit-root exclusions, and the exact discriminant census.

Ford, Khan, and Shparlinski (2010) study other geometric statistics of modular hyperbolas, especially Euclidean width and convex hull. Shparlinski (arXiv:1103.2879) surveys their distribution and Euclidean geometry. Neither inspected account gives the primitive ring-line incidence census.

## Limitations
This is a self-contained arithmetic derivation, not an assertion of independent certification or historical priority. The 2013 paper's discriminant calculation is a substantial known ingredient, so the novelty lies solely in the complete **ring-affine incidence census**, exact maximum-line counts, and stabilized proportions. A previously unlocated equivalent census in finite-chain-ring geometry remains possible. The 2010 publisher PDF was not accessible in full; its bibliographic record, abstract, and published subject classification were checked. Even though no equivalent result was identified in the inspected literature, the literature comparison is not exhaustive.

## References
1. M. R. Khan, R. Magner, S. Senger, and A. Winterhof, *Two Combinatorial Geometric Problems Involving Modular Hyperbolas*, arXiv:1304.6943 (first posted 2013-04-25), especially Lemma 6 and Proposition 7. https://arxiv.org/abs/1304.6943
2. K. Ford, M. R. Khan, and I. E. Shparlinski, *Geometric properties of points on modular hyperbolas*, Proc. Amer. Math. Soc. 138 (2010), 4177–4185, DOI:10.1090/S0002-9939-2010-10561-0 (public record 2010-07-09). https://doi.org/10.1090/S0002-9939-2010-10561-0
3. I. E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879 (first posted 2011-03-15). https://arxiv.org/abs/1103.2879
