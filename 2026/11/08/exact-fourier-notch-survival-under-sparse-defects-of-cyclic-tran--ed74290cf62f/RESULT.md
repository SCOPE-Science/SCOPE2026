# Exact Fourier-notch survival under sparse defects of cyclic transversals

## Finding

Fix an odd prime \(p\), integers \(k>b\ge1\), and put \(N=p^k\), \(s=p^b\), and \(a=N/s\). Let \(T\subset\mathbb Z_N\) contain exactly one point in each residue class modulo \(s\). Choose disjoint sets \(A,B\subset\mathbb Z_s\) of equal size \(r\), where \(1\le r<p\) and \(2r<s\). Remove from \(T\) the representatives over \(A\), and insert one new, distinct point over each residue in \(B\), different from the representative already present there. Denote the resulting \(s\)-point set by \(T'\).

For \(0\le v\le b\), let \([A]_v\) and \([B]_v\) be the multisets of their reductions modulo \(p^v\), and define
\[
V=\max\{v\in\{0,1,\ldots,b\}:[A]_v=[B]_v\}.
\]
As \(A\cap B=\varnothing\), one has \(0\le V\le b-1\). With the unnormalized Fourier transform
\[
\widehat{1_{T'}}(j)=\sum_{x\in T'}\exp(-2\pi i jx/N),\qquad j\in\mathbb Z_N,
\]
**every nontrivial Fourier zero is classified exactly**:
\[
\boxed{\{j\ne0:\widehat{1_{T'}}(j)=0\}
=\{a h\pmod N:0<h<s,\ p^{b-V}\mid h\}.}
\]
In particular the number of such zeros is \(p^V-1\), independent of the original transversal and of all chosen lifts of the inserted points. Equivalently, \(V\) is the optimal bottleneck \(p\)-adic matching depth of \(A\) and \(B\):
\[
V=\max_{\sigma\in S_r}\min_{1\le i\le r}\min\{b,\nu_p(u_i-v_{\sigma(i)})\},
\]
where \(u_i\) and \(v_i\) enumerate \(A\) and \(B\); valuations of nonzero differences of chosen integer representatives are used, with the inner truncation making the formula independent of representatives.

The original transversal has precisely \(s-1\) nontrivial Fourier zeros. Hence any allowed nonempty defect destroys at least \((p-1)p^{b-1}\) of those zeros. This loss bound is attained already by a single relocation, and, for each \(v\in\{0,\ldots,b-1\}\), one relocation attains exactly \(p^v-1\) surviving zeros.

The cutoff \(r<p\) is sharp for the matching conclusion. For any odd prime, take \(k=3\), \(b=2\), \(T=\{0,1,\ldots,p^2-1\}\), remove the \(p\) points \(A=\{0,p,\ldots,(p-1)p\}\), and insert \(B+p^2\) for \(B=\{1,1+p,\ldots,1+(p-1)p\}\). The two residue multisets differ even modulo \(p\), but the modified set still has a zero at index \(p\).

## Assumptions and scope

The sets are unweighted \(0\)-\(1\) subsets of the cyclic group \(\mathbb Z_{p^k}\). Every residue modulo \(p^b\) is initially represented exactly once. Each of the \(r\) deleted residues is different from each of the \(r\) receiving residues; receiving residues acquire one additional point. The inequality \(2r<s\) guarantees at least one untouched singly occupied residue, while \(r<p\) forbids a complete prime cycle among the signed changes. The theorem does not describe arbitrary perturbations that preserve residue counts or allow larger fault sets.

## Proof

**Prime-power cyclotomic coefficient lemma.** Let \(t\ge1\) and \(c_0,\ldots,c_{p^t-1}\in\mathbb Z\). For a primitive \(p^t\)-th root \(\zeta\),
\[
\sum_{j=0}^{p^t-1}c_j\zeta^j=0
\quad\Longleftrightarrow\quad
c_{u}=c_{u+p^{t-1}}=\cdots=c_{u+(p-1)p^{t-1}}
\quad(0\le u<p^{t-1}).
\]
Indeed \(\Phi_{p^t}(X)=\sum_{h=0}^{p-1}X^{h p^{t-1}}\) is the minimal polynomial of \(\zeta\). A polynomial of degree less than \(p^t\) divisible by \(\Phi_{p^t}\) is precisely \(\Phi_{p^t}(X)Q(X)\) with \(\deg Q<p^{t-1}\). Comparing coefficients proves both directions. For a polynomial with larger exponents, first sum coefficients in the same residue class modulo \(p^t\).

**Exclusion of higher-order roots.** A nontrivial Fourier index \(j\) has character order \(p^t\), with \(t=k-\nu_p(j)\). Suppose \(t>b\). Choose a residue class \(u\pmod s\) outside \(A\cup B\), possible by \(2r<s\). The modified set contains exactly one point over \(u\). Since \(t-1\ge b\), every coefficient position in one prime-power cyclotomic fiber
\(w,w+p^{t-1},\ldots,w+(p-1)p^{t-1}\) lies in the same residue class modulo \(s\). The fiber containing that unique point has one coefficient equal to one and the other \(p-1\) coefficients zero. The lemma rules out a Fourier zero of order \(p^t\). Thus any nontrivial zero has order at most \(p^b\), or equivalently \(a\mid j\).

**Cancellation at the remaining indices.** Write \(j=ah\), where \(0<h<s\). The original transversal has one element in each residue modulo \(s\), so its Fourier coefficient is a complete nontrivial character sum on \(\mathbb Z_s\) and equals zero. The changed coefficient is therefore
\[
\widehat{1_{T'}}(ah)
=\sum_{v\in B}e^{-2\pi ihv/s}-\sum_{u\in A}e^{-2\pi ihu/s}.
\]
If the character has order \(p^t\), the coefficient lemma says that the differences between the multiplicities of \(B\) and \(A\) in each of the \(p\) positions of every cyclotomic fiber must be equal. If the common difference in a fiber were positive, each of the \(p\) positions would contain at least one point of \(B\), contradicting \(|B|=r<p\). If negative, the same argument contradicts \(|A|<p\). Hence every such difference is zero: the multisets of \(A\) and \(B\) agree modulo \(p^t\). The converse follows immediately by character periodicity.

The equal-multiset property holds for exactly the depths \(0\le t\le V\), since equality modulo a higher power implies equality modulo every lower power. For \(j=ah\), character order at most \(p^V\) is equivalent to \(p^{b-V}\mid h\). There are \(p^V-1\) nonzero such indices. The standard finite multiset-matching principle shows that equal multiplicities in every residue class modulo \(p^v\) are equivalent to the existence of a bijection pairing \(A\) with \(B\) modulo \(p^v\); maximizing \(v\) yields the bottleneck formula.

**Sharpness and boundary.** The same singleton-residue argument gives no Fourier zeros of order above \(p^b\) for the original transversal, while all \(s-1\) nontrivial characters of order at most \(p^b\) vanish. Because \(V\le b-1\), at most \(p^{b-1}-1\) remain after a nonempty defect, yielding the asserted loss. For each \(0\le v<b\), take \(r=1\), \(A=\{0\}\), \(B=\{p^v\}\), and choose any permitted new lift; then \(V=v\), establishing all levels and the sharp bound.

For the announced boundary at \(r=p\), the sums of primitive \(p^2\)-th roots over each of \(A\) and \(B\) vanish separately (each is a complete \(p\)-cycle), while the two sets have different reductions modulo \(p\). The original transversal sum also vanishes at order \(p^2\). Hence the modified set retains a Fourier zero at index \(p\) despite matching depth zero, proving the strict threshold is essential.

## Verification

Run `python CHECK.py` with the Python standard library. It performs independent exact cyclotomic tests and compares the predicted and observed zero sets over hundreds of randomly generated cyclic transversals and relocations, including multi-defect cases, plus independent direct numerical Fourier-sum checks and the sharp failure example at \(r=p\). The packaged run reported `CHECK_OK checks=33317`. These computations are finite supplementary checks; the unrestricted statement is proved by the preceding argument.

For a concrete case, \(p=3\), \(k=3\), \(b=2\), \(T=\{0,1,\ldots,8\}\), removal of \(0\) and insertion of \(12\) produces exactly the nontrivial Fourier zeros \(\{9,18\}\). Insertion of \(10\) instead produces none.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez introduce block equivalence for finite Gabor frames and connect cyclotomic divisibility of indicator polynomials to vanishing frame-matrix diagonals. Their cyclotomic criterion is a motivating setting, not a claim of novelty for prime-power root theory. De Carli and Laporta give a general cyclotomic divisibility test; Lam and Leung and the preceding Rédei–de Bruijn–Schoenberg theorem describe the group-ring kernel of evaluations at roots of unity. Those broad ingredients imply the coefficient lemma used here. The statement isolated here is the exact, lift-independent classification of **all** Fourier zeros after fewer than \(p\) displaced representatives, its optimal \(p\)-adic matching invariant, and a sharp defect threshold with a counterexample at \(r=p\). A specialized earlier derivation may exist; no blanket priority claim is made.

## Limitations

The result is confined to odd prime-power cyclic groups, complete-residue transversals, and the specified collision-form perturbations with \(r<p\) and \(2r<p^b\). The corresponding zero patterns are not claimed for general mixed-prime moduli, weighted data, arbitrary missing/extra points, or an arbitrary Fourier-band concentration operator. It does not compute full Gabor frame operators. The cyclotomic coefficient lemma is classical rather than new, and the originality of the combined special-family classification remains conditional on prior-art coverage.

## References

1. O. Asipchuk, L. De Carli, and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, first submitted 15 May 2026, Sections 1–5, https://arxiv.org/abs/2605.16139.
2. L. De Carli and M. Laporta, *Divisibility criteria and coefficient formulas for cyclotomic polynomials*, arXiv:2508.02722, first submitted 1 August 2025, Sections 1–3, https://arxiv.org/abs/2508.02722.
3. T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, arXiv:math/9511209, 13 November 1995, Theorem 2.2 and Main Theorem, https://arxiv.org/abs/math/9511209; journal version, *J. Algebra* 224 (2000), 91–109.
