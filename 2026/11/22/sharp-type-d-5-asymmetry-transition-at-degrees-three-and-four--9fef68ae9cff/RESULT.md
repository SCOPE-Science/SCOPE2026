# Sharp type-\(D_5\) asymmetry transition at degrees three and four

## Finding

Let \(W=W(D_5)\) be the Weyl group of type \(D_5\), represented by even signed permutations of \(1,2,3,4,5\). Write \(\ell\) for Coxeter length, \(\le\) for Bruhat order, and \(P_{x,w}(q)\) for the Kazhdan–Lusztig polynomials in their constant-term-one normalization. Put
\[
P_w(q)=\sum_{x\le w}q^{\ell(x)},\qquad
D_w(q)=q^{\ell(w)}P_w(q^{-1})-P_w(q).
\]
For every \(w\in W\) with \(P_{e,w}(1)=2\), the following sharp bounds hold:
\[
\begin{array}{ll}
[q^3]D_w(q)\le14,&\ell(w)>6,\\
[q^4]D_w(q)\le27,&\ell(w)>8.
\end{array}
\]
Equality in either bound occurs **if and only if**
\[
w=a:=(-1,-3,-4,2,-5)\quad\text{or}\quad
w=a^{-1}=(-1,4,-2,-3,-5).
\]
Both extremizers have \(\ell(w)=16\), \(P_{e,w}(q)=1+q\), and the same ordinary Poincaré polynomial, with coefficients in ascending degree:
\[
P_w(q):\quad (1,5,14,30,54,85,120,153,175,178,159,123,81,44,19,6,1).
\]
Their first eight asymmetry coefficients, indexed from degree zero, are \((0,1,5,14,27,38,39,25)\).

The general finite-Weyl-group coefficient bound, also recorded in the subsequent asymmetry literature, yields \([q^4]D_w(q)\le [q^3]P_{w_0}(q)=30\); the exact type-\(D_5\) value is therefore **strictly smaller by three**. At degree three the universal bound \([q^2]P_{w_0}(q)=14\) is attained, but by exactly the indicated inverse pair.

## Assumptions and scope

The base field is \(\mathbb C\) for the standard interpretation of these polynomials as invariants of Schubert varieties in the complete flag variety of a connected complex reductive group of type \(D_5\). The calculation is equally an exact statement about the finite Coxeter group. The simple reflections in the accompanying checker are \(s_0\), which swaps the first two entries and negates both, and \(s_i\), \(1\le i\le4\), which swaps positions \(i,i+1\); the Coxeter diagram has trivalent node \(s_2\) joined to \(s_0,s_1,s_3\), and \(s_3\) joined to \(s_4\). Signs in one-line notation act on negative positions in the usual way. All coefficient inequalities restrict to \(k<\ell(w)/2\) as stated. No claim is made for arbitrary Weyl ranks or for arbitrary singular Schubert varieties without \(P_{e,w}(1)=2\).

## Proof

**1. Finite and exhaustive domain.** Every element of \(W(D_5)\) is an even signed permutation, so \(|W|=2^4\cdot5!=1920\). Breadth-first traversal from the identity through the five specified involutive generators lists all 1920 elements and computes their shortest word lengths, with maximum 20. For each \(w\), the Bruhat subword criterion applied to a reduced word gives the *complete* lower interval \([e,w]\), hence the exact coefficient vector of \(P_w(q)\). The full-flag Poincaré polynomial begins \((1,5,14,30,54)\), also agreeing with the product of the \(q\)-integers of sizes \(2,4,5,6,8\).

**2. Necessary coefficient inequalities from intersection cohomology.** These inequalities can be deduced directly from the standard palindromic intersection-cohomology Poincaré polynomial and Kazhdan–Lusztig monotonicity, without assuming the claimed rank-five optimum. Since \(P_{e,w}(1)=2\), positivity implies \(P_{e,w}(q)=1+q^h\) for one \(h\ge1\). Coefficientwise monotonicity implies that \(P_{x,w}(q)\) is either \(1\) or \(1+q^h\) for each \(x\le w\). Let \(S_w(q)=\sum_{x\le w,\,P_{x,w}\ne1}q^{\ell(x)}\). The intersection-cohomology Poincaré polynomial is \(P_w(q)+q^hS_w(q)\), which is palindromic by intersection-cohomology Poincaré duality on projective Schubert varieties. Therefore
\[
D_w(q)=q^hS_w(q)-q^{\ell(w)-h}S_w(q^{-1}).
\]
Writing \(c_j=[q^j]S_w(q)\), with \(c_j=0\) for \(j<0\), gives \([q^k]D_w(q)=c_{k-h}-c_{\ell(w)-k-h}\le c_{k-h}\le[q^{k-h}]P_{w_0}(q)\le[q^{k-1}]P_{w_0}(q)\) for \(1\le k<\ell(w)/2\); the last step uses rank unimodality of the full flag Poincaré polynomial. These are standard consequences of the classical intersection-cohomology formalism, and also appear explicitly as Corollary 3.3 of Burrull–Li–Zeng–Zhang (2026). Thus a possible degree-three equality must satisfy \(([q]D_w,[q^2]D_w,[q^3]D_w)=(d_1,d_2,14)\) with \(d_1\le1,d_2\le5\). An exhaustive comparison of all 1920 lower intervals leaves exactly **nine** possibilities. The degree-four question requires \(d_1\le1,d_2\le5,d_3\le14\). Among all \(w\) with \(\ell(w)>8\), exactly **572** pass these three necessary inequalities, and their maximal fourth difference is **27**, attained at exactly seven elements. This establishes the degree-four upper bound without a Kazhdan–Lusztig computation for every element.

**3. Exact singularity filtering.** For each of the nine degree-three possible equalizers, the attached checker computes \(P_{e,w}(q)\) using the standard exact \(R\)-polynomial recursion and the Kazhdan–Lusztig bar-invariance identity, with the usual degree cutoff. The resulting test \(P_{e,w}(1)=2\) holds for exactly the two signed permutations \(a,a^{-1}\). The seven fourth-degree possible equalizers are a subset of the same nine; exactly those two pass the test. Thus both equality classifications are exhaustive, not merely demonstrations of attainability.

For transparency, the seven degree-four possible equalizers and their identity Kazhdan–Lusztig polynomials are:

| Signed permutation | \(P_{e,w}(q)\) |
|---|---|
| \((-4,1,-2,-5,-3)\) | \(1+q+q^2\) |
| \((-2,-3,-5,1,-4)\) | \(1+q+q^2\) |
| \((-1,-3,-4,2,-5)\) | \(1+q\) |
| \((-1,2,-3,-4,-5)\) | \(1+q+q^2+q^3\) |
| \((-1,4,-2,-3,-5)\) | \(1+q\) |
| \((2,-3,-5,-1,-4)\) | \(1+q+q^2\) |
| \((4,-1,-2,-5,-3)\) | \(1+q+q^2\) |

**4. Verification of the witnesses.** Exact lower-interval enumeration yields \(\ell(a)=\ell(a^{-1})=16\), the displayed Poincaré vector, and \([q^3]D_a=14\), \([q^4]D_a=27\). Direct signed-permutation inversion gives \(a^{-1}\) as displayed. The exact recursion gives \(P_{e,a}=P_{e,a^{-1}}=1+q\). These prove attainability, completing the two sharp bounds and equality classifications.

The exact \(R\)-polynomial recursion has base cases \(R_{x,w}=0\) for \(x\not\le w\), \(R_{w,w}=1\). For a right descent \(s\) of \(w\), it uses \(R_{x,w}=R_{xs,ws}\) if \(xs<x\), and \(R_{x,w}=qR_{xs,ws}+(q-1)R_{x,ws}\) otherwise. The defining bar identity \(q^{\ell(w)-\ell(x)}P_{x,w}(q^{-1})-P_{x,w}(q)=\sum_{x<y\le w}R_{x,y}(q)P_{y,w}(q)\), together with \(\deg P_{x,w}<(\ell(w)-\ell(x))/2\), determines the coefficients recursively. This is the actual identity tested by the checker, not an unsupported appeal to numerical sampling.

## Verification

Run \(\texttt{python3 checker.py}\) with Python 3 and the standard library only. The checker reconstructs the complete Weyl group and its Bruhat intervals, checks the 572-element necessity-filter census and all nine possible degree-three equalizers, recomputes the seven degree-four Kazhdan–Lusztig polynomials, verifies the inverse relation and the full Poincaré vector, and checks the \(R\)-recursion against **every available right descent** for every interval pair among the seven degree-four candidates. It also calibrates the normalization against \(4231\in S_4\) and the published type-\(D_4\) short singularity table. Every arithmetic operation is exact. Execution passed on the supplied file; no random experiment or timeout is used as proof.

## Relationship to prior work

Li–Rietsch–Yang, *An anticanonical perspective on \(G/P\) Schubert varieties* (2025), proves that for simply-laced Schubert varieties the equality of degree-two and next-to-top Betti numbers characterizes factoriality. This provides a natural motivation to quantify *higher* opposite-degree Betti differences in the simply-laced \(D_5\) flag variety. The later paper of Burrull–Li–Zeng–Zhang, *On the asymmetry polynomial of Schubert varieties* (2026), proves a universal inequality for those higher differences and sharpness in types \(A\) and \(B\), but gives neither the degree-four optimal type-\(D_5\) value 27 nor its exact equality class. Goresky's indexed tables stop at type \(D_4\) among the type-\(D\) cases and therefore cannot simply be read to obtain this result. A general algorithm for Kazhdan–Lusztig polynomials establishes computability, not this particular optimum without the exhaustive comparison.

## Limitations

This is a complete finite classification for two coefficients in one Weyl rank, not an infinite-rank theorem. The proof uses standard intersection-cohomology duality and monotonicity, plus finite exact enumeration of 1920 elements. The 2026 general coefficient inequality is a subsequent supporting comparison, not a premise requiring its authors’ classification. The result does not classify all type-\(D_5\) elements with \(P_{e,w}(1)=2\), nor the singular loci of the two extremal Schubert varieties. Potential unindexed type-\(D_5\) tables or equivalent finite extremal calculations remain a literature-priority risk. Independent mathematical audit has not been performed.

## References

1. C. Li, K. Rietsch and M. Yang, *An anticanonical perspective on \(G/P\) Schubert varieties*, arXiv:2506.18388v1 (first public 2025-06-23), https://arxiv.org/html/2506.18388v1, Theorem A and Remarks 1.1–1.2.
2. G. Burrull, Z. A. Li, S. Zeng, X. Zhang, *On the asymmetry polynomial of Schubert varieties*, arXiv:2611.24751v1 (first public 2026-11-18), https://arxiv.org/html/2611.24751v1, especially Corollary 3.3 and Section 4 (subsequent related literature).
3. M. Goresky, *Tables of Kazhdan–Lusztig Polynomials* (1996), https://www.math.ias.edu/~goresky/tables.html; type \(D_4\) data at https://www.math.ias.edu/~goresky/D4.txt.
4. D. Kazhdan and G. Lusztig, *Representations of Coxeter groups and Hecke algebras*, Invent. Math. 53 (1979), 165–184, for the defining recursion.
