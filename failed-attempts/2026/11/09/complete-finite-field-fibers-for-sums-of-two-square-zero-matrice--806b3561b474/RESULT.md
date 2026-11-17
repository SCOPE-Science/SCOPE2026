# Complete finite-field fibers for sums of two square-zero matrices of order three

## Finding

Let \(k=\mathbb F_q\) be any finite field, including fields of characteristic two. Put
\[
\mathcal S_q=\{A\in M_3(k):A^2=0\},\qquad
F_q(C)=\#\{(A,B)\in\mathcal S_q^2:A+B=C\},\qquad
s_q=q^4+q^3-q.
\]
All ordered pairs are counted, including zero summands. For a rank-two target \(C\), let \(W=\operatorname{im}C\) and \(M=C|_W\), considered as an endomorphism of the two-dimensional space \(W\). Write \(e(M)\) for its number of rational invariant lines, and \(z(M)\) for its number of lines in \(\ker M\). The **complete prescribed-target fiber law** is
\[
F_q(C)=
\begin{cases}
s_q,&C=0,\\
2q^2-q,&\operatorname{rank}C=1,\ \operatorname{tr}C=0,\\
q+1-e(M)+qz(M),&\operatorname{rank}C=2,\ \operatorname{tr}C=0,\\
0,&\text{otherwise.}
\end{cases}
\]
In particular, every positive fiber is determined by an elementary similarity invariant of its target. The following explicit strata include the number of targets of each type (all unlisted targets have fiber zero).

When \(q\) is odd:

| Target type | Number of targets | Fiber size |
|---|---:|---:|
| Zero | \(1\) | \(s_q\) |
| Nonzero square-zero | \(s_q-1\) | \(2q^2-q\) |
| Regular nilpotent, a single block of size three | \(q(q^2-1)(q^3-1)\) | \(2q\) |
| Rank-two, nonzero eigenvalues \(\lambda,-\lambda\in k\) | \(\frac12q^3(q+1)(q^3-1)\) | \(q-1\) |
| Rank-two, nonzero eigenvalues forming an irreducible quadratic pair | \(\frac12q^3(q-1)(q^3-1)\) | \(q+1\) |

When \(q\) is even:

| Target type | Number of targets | Fiber size |
|---|---:|---:|
| Zero | \(1\) | \(s_q\) |
| Nonzero square-zero | \(s_q-1\) | \(2q^2-q\) |
| Regular nilpotent, a single block of size three | \(q(q^2-1)(q^3-1)\) | \(2q\) |
| Rank-two, with one nonzero Jordan block of size two and one zero block | \(q^2(q^2-1)(q^3-1)\) | \(q\) |

The number of representable targets is exactly
\[
\#\{C:F_q(C)>0\}=\begin{cases}
q^3s_q,&q\text{ odd},\\
1+(q+1)(q^3-1)(q^3-q+1),&q\text{ even}.
\end{cases}
\]
For example, in characteristic two, \(\operatorname{diag}(\lambda,\lambda,0)\) with \(\lambda\ne0\) has no decomposition into two square-zero matrices, whereas a target with a nontrivial size-two Jordan block at the same eigenvalue has exactly \(q\) ordered decompositions. This support distinction was already characterized by prior existence theorems; the exact positive multiplicities and population formula are the finding assessed here.

## Assumptions and scope

The matrix algebra is the *full* \(3\)-by-\(3\) algebra over an arbitrary finite field. A square-zero matrix means precisely \(A^2=0\); there are no rank, invertibility, or nonzero-summand restrictions. Ordered pairs \((A,B)\) and \((B,A)\) are counted separately when distinct. The target-dependent counts have no analytic or asymptotic assumptions. The characteristic-two and odd-characteristic cases are both included. A rational eigenline is a one-dimensional invariant subspace defined over \(k\), not over an algebraic closure.

## Proof

**1. Square-zero locus.** Since \(\operatorname{im}A\subseteq\ker A\), every nonzero square-zero matrix of size three has rank one. It is expressible as \(A=uv^{\mathsf T}\) with \(u,v\ne0\) and \(v^{\mathsf T}u=0\). For each \(u\ne0\), there are \(q^2-1\) choices of nonzero \(v\) satisfying this equation, and each nonzero rank-one matrix has exactly \(q-1\) such factorizations. Consequently
\[
\#\mathcal S_q=1+\frac{(q^3-1)(q^2-1)}{q-1}=q^4+q^3-q=s_q.
\]
For \(C=0\), any \(A\in\mathcal S_q\) has the unique partner \(B=-A\), proving \(F_q(0)=s_q\).

**2. Rank-one targets.** Every sum of two square-zero matrices has trace zero and rank at most two. A nonzero rank-one, trace-zero target is automatically square-zero. Write it as \(C=uv^{\mathsf T}\) with \(v^{\mathsf T}u=0\). If \(A+B=C\) with both summands of rank at most one, then either their column lines coincide or their row lines coincide; otherwise the sum would have rank two. The common-column decompositions are
\[
A=u\alpha^{\mathsf T},\qquad B=u(v-\alpha)^{\mathsf T},\qquad \alpha^{\mathsf T}u=0,
\]
with \(q^2\) choices; the common-row decompositions have another \(q^2\) choices. Both descriptions overlap exactly for \(A=tC,\ B=(1-t)C\), with \(q\) values of \(t\). Therefore \(F_q(C)=2q^2-q\). The zero summands are already included.

**3. Rank-two targets.** Fix a rank factorization \(C=UV\), with \(U:k^2\hookrightarrow k^3\) injective and \(V:k^3\twoheadrightarrow k^2\) surjective. Put \(M=VU\); this represents \(C|_{\operatorname{im}C}\), and \(\operatorname{tr}M=\operatorname{tr}C\). If \(A+B=C\) with \(A^2=B^2=0\), both summands must have rank one. Their column spaces span \(\operatorname{im}C\), and their row spaces span \(\operatorname{row}C\). Hence there is a unique rank-one idempotent \(P\in M_2(k)\) such that
\[
A=UPV,\qquad B=U(I-P)V.
\]
Conversely each rank-one idempotent produces rank-one summands adding to \(C\). Because \(PMP=\operatorname{tr}(PM)P\) and \((I-P)M(I-P)=\operatorname{tr}((I-P)M)(I-P)\), these summands are square-zero precisely when both traces vanish. For \(\operatorname{tr}M=0\), this is the single condition \(\operatorname{tr}(PM)=0\).

Every rank-one projector has the form \(P=x\varphi\), where \(kx\) is its image line and \(\varphi(x)=1\). Fix the line \(\ell=kx\). If \(Mx=0\), all \(q\) choices of \(\varphi\) work; if \(Mx=\lambda x\) with \(\lambda\ne0\), no choice works; if \(x,Mx\) are independent, exactly one choice works. The number of good projectors is therefore
\[
(q+1-e(M))+qz(M),
\]
proving the stated formula. This proof requires neither characteristic restrictions nor Jordan normal forms.

**4. Explicit rank-two strata.** Rank-two \(C\) has a nonzero restricted operator \(M\), since \(C^2=0\) would force \(\operatorname{rank}C\le1\). If \(M\) is singular with trace zero, it is a nonzero nilpotent map on \(k^2\), with \(e(M)=z(M)=1\), hence \(2q\) decompositions; such \(C\) is regular nilpotent. When \(M\) is invertible and \(q\) is odd, its zero trace forces either two distinct nonzero rational eigenvalues (\(e=2,z=0\), count \(q-1\)) or an irreducible quadratic (\(e=z=0\), count \(q+1\)). In characteristic two an invertible zero-trace \(M\) has a repeated nonzero eigenvalue in \(k\). If scalar, \(e=q+1,z=0\) and the count vanishes; otherwise \(e=1,z=0\) and the count equals \(q\).

**5. Populations and consistency.** The order of \(\mathrm{GL}_3(k)\) is \((q^3-1)(q^3-q)(q^3-q^2)\). Similarity-class sizes obtained from centralizers are as follows. The regular nilpotent class has size \(q(q^2-1)(q^3-1)\). For odd \(q\), the \((q-1)/2\) split pairs \(\{\lambda,-\lambda\}\) each have torus centralizer \((q-1)^3\), while the \((q-1)/2\) nonsplit quadratic classes each have centralizer \((q^2-1)(q-1)\). In characteristic two, each of the \(q-1\) nonzero size-two Jordan eigenvalue classes has centralizer of size \(q(q-1)^2\). These yield the target counts in the tables. Adding the positive-fiber target populations proves the representable-target formulas. Weighting every population by its corresponding fiber size gives exactly
\[
\sum_{C\in M_3(k)}F_q(C)=s_q^2,
\]
as required because both summands range independently over \(\mathcal S_q\). This identity is a consistency check, not a substitute for Steps 1--4.

## Verification

The package contains two standalone programs under `artifacts/`. `check_fibers.py` independently constructs the square-zero locus as actual rank-one matrices and evaluates its self-convolution, comparing every target over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) against a target-class formula derived using matrix products and ranks. It also checks all supported targets and 1,200 additional reproducible targets over \(\mathbb F_5\). The \(\mathbb F_4\) arithmetic is implemented via the irreducible polynomial \(t^2+t+1\). `check_direct.py` independently enumerates **all** \(3\)-by-\(3\) matrices over \(\mathbb F_2\) and \(\mathbb F_3\), detects square-zero matrices by literal multiplication, and then counts all ordered sums.

The first program checks 512, 19,683, and 262,144 complete target spaces for field orders 2, 3, and 4, and 94,325 tested targets at field order 5. The second program independently checks 484 and 11,025 ordered square-zero pairs at field orders 2 and 3. All comparisons passed. The output is in `artifacts/check_results.txt`; no external packages or input files are required.

For \(q=2\), exactly \(148\) of \(512\) matrices are representable, with \(22\) square-zero inputs and \(484\) ordered input pairs. For \(q=3\), exactly \(2,835\) of \(19,683\) targets are representable, with \(105\) square-zero inputs and \(11,025\) ordered pairs. The results are consistent with both population formulas. This finite verification corroborates, but does not replace, the unrestricted proof.

## Relationship to prior work

Botha (2012) characterized **which** matrices over arbitrary fields can be expressed as sums of two square-zero matrices. De Seguins Pazzis (arXiv:1605.05131v1, 2016) explicitly restates that characterization as Theorem 2.6 and Corollaries 2.7--2.8, and studies sums of three and four square-zero matrices. Song, Zheng and Cao (2013) supply an alternative existence characterization in terms of idempotents. These results establish the existence boundary, including the characteristic-two scalar obstruction, **before** the present counting calculation; they do not, in the material inspected, give the ordered finite-field representation multiplicities. The claim of additional content is solely the complete exact target-fiber law and population distribution in size three.

The proof requires only rank-one factorization, the incidence of projective eigenlines with the kernel, and finite-field similarity-class counts. The existence criterion is not claimed as original. Published related matrix-decomposition results and search records have been compared by statement and implication rather than title; no dominating explicit fiber census was identified, but exhaustive historical priority is not established.

## Limitations

Only three-by-three matrices are treated, not arbitrary dimension or more than two summands. There are no claims about similarity *orbits of pairs* rather than labeled ordered decompositions. Full texts of some historically relevant papers were unavailable; a broader theorem on additive convolution of rank-one nilpotent matrices might subsume the counting result. Independent external mathematical validation has not been performed. All formulas are exact, but the historical originality assessment is provisional.

## References

1. Clément de Seguins Pazzis, *A note on sums of three square-zero matrices*, arXiv:1605.05131v1 (first public version 2016-05-17), especially §2.4, Theorem 2.6, and Appendix A. https://arxiv.org/abs/1605.05131
2. J. D. Botha, *Sums of two square-zero matrices over an arbitrary field*, Linear Algebra and its Applications **436** (2012), 516--524. DOI:10.1016/j.laa.2011.07.011.
3. Xiaofei Song, Baodong Zheng and Chongguang Cao, *A Note on Decomposing a Square Matrix as Sum of Two Square Nilpotent Matrices over an Arbitrary Field*, The Scientific World Journal (2013), article 640350. DOI:10.1155/2013/640350.
4. A. Mohammadian, *Sums and Products of Square-Zero Matrices*, Communications in Algebra **40** (2012), 4568--4574. DOI:10.1080/00927872.2011.613423.
