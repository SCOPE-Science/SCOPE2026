# A sharp eigenvector mode-switching threshold for Nyström extraction

## Finding

**Theorem (exact mode switch despite improved leading eigenvalue).** Fix \(a,u\in(0,1)\) and \(0<\delta<1-a\). Let
\[
A=\operatorname{diag}(1,a,1-\delta,0),\qquad
q_1=\sqrt{1-u}\,e_1+\sqrt u\,e_2,\qquad
q_2=\sqrt{1-u}\,e_3+\sqrt u\,e_4,
\]
and \(Q=[q_1,q_2]\). Define the ordinary Rayleigh--Ritz matrix \(B=Q^{\mathsf T}AQ\) and the Nyström approximation
\[
N=AQ(Q^{\mathsf T}AQ)^{-1}Q^{\mathsf T}A.
\]
The leading eigenvalue of \(A\) is simple, with eigenvector \(e_1\), and its leading two-dimensional invariant subspace is \(U=\operatorname{span}(e_1,e_3)\). The maximal principal-angle sine between \(\operatorname{ran}Q\) and \(U\) equals \(\sqrt u\).

Put
\[
\delta_c(a,u)=\frac{a(1-a)u}{1-(1-a)u}.
\]
The unique leading Rayleigh--Ritz vector is \(q_1\) for every admissible \(\delta\), with squared sine error \(u\). The unique leading Nyström vector is \(e_3\), **orthogonal** to \(e_1\), exactly when \(0<\delta<\delta_c(a,u)\); when \(\delta_c(a,u)<\delta<1-a\), it is
\[
\frac{\sqrt{1-u}\,e_1+a\sqrt u\,e_2}{\sqrt{1-u+a^2u}},
\]
with squared sine error \(a^2u/(1-u+a^2u)<u\). At \(\delta=\delta_c(a,u)\) the largest Nyström eigenvalue is double, so the leading vector is not uniquely defined.

Throughout the mode-swapped regime, Nyström's leading eigenvalue is \(1-\delta\), strictly closer to the true leading eigenvalue \(1\) than the Rayleigh--Ritz value \(1-(1-a)u\), even though its corresponding eigenvector is orthogonal to the true leading eigenvector. For \(a=1/2\) and \(\delta=u/8\), this eigenvalue error improves by exactly a factor of four for every \(0<u<1\); nevertheless, as \(u\downarrow0\), both the trial subspace and its leading Ritz vector converge to the correct objects while the leading Nyström vector remains \(e_3\).

## Assumptions and scope

All calculations are in real exact arithmetic. The matrix is positive semidefinite; \(Q\in\mathbb R^{4\times2}\) has orthonormal columns. The condition \(0<\delta<1-a\) orders the four true eigenvalues as \(1>1-\delta>a>0=\lambda_4\). The Nyström core \(B\) is positive definite, so its ordinary inverse and pseudoinverse agree. Eigenvector errors mean \(\sin\angle(v,e_1)=\sqrt{1-|v^{\mathsf T}e_1|^2}\) for unit vectors, with signs irrelevant. The result classifies the particular two-leakage-mode family above, not arbitrary PSD matrices or individual eigenvectors in every search subspace.

## Proof

The two columns of \(Q\) have disjoint supports and unit length, so \(Q^{\mathsf T}Q=I_2\). Direct evaluation gives
\[
B=\operatorname{diag}(b_1,b_2),\quad
b_1=1-(1-a)u,\quad b_2=(1-\delta)(1-u).
\]
Both diagonal entries are positive, and
\[
b_1-b_2=a u+\delta(1-u)>0.
\]
Hence the unique leading Ritz vector is \(q_1\), with largest Ritz value \(b_1\) and squared sine error \(u\).

As \(Aq_1\perp Aq_2\), the Nyström matrix is the sum of two orthogonal rank-one operators
\[
N=\frac{(Aq_1)(Aq_1)^{\mathsf T}}{b_1}
 +\frac{(Aq_2)(Aq_2)^{\mathsf T}}{b_2}.
\]
Its two strictly positive eigenvalues are
\[
\nu_1=\frac{1-(1-a^2)u}{b_1}
       =1-\frac{a(1-a)u}{b_1}=1-\delta_c(a,u),
\qquad \nu_2=1-\delta.
\]
The eigenvectors associated with \(\nu_1\) and \(\nu_2\) are respectively \(Aq_1/\|Aq_1\|\) and \(e_3\). Thus \(\nu_2>\nu_1\) if and only if \(\delta<\delta_c\). This proves the exact mode-switching classification, including the double leading eigenvalue at equality. Since \(\operatorname{span}(e_1,e_3)\) has cross-Gram matrix \(\sqrt{1-u}\,I_2\) against \(Q\), both principal angles have sine \(\sqrt u\).

On the \(\nu_1\)-leading branch, \(Aq_1=\sqrt{1-u}\,e_1+a\sqrt u\,e_2\), giving squared sine error \(a^2u/(1-u+a^2u)<u\). On the \(\nu_2\)-leading branch the vector is exactly \(e_3\), so its squared sine error equals \(1\). Finally, since \(b_1>a\) when \(0<u<1\),
\[
0<\delta_c(a,u)=\frac{a}{b_1}(1-a)u<(1-a)u.
\]
For \(\delta<\delta_c\), Nyström's largest eigenvalue error equals \(\delta\), while the Ritz error is \((1-a)u\). Substituting \(a=1/2\) and \(\delta=u/8\) gives \(\delta_c=u/(4-2u)>u/8\), a Nyström error of \(u/8\), and a Ritz error of \(u/2\). Letting \(u\) decrease to zero completes the assertion about arbitrarily accurate trial subspaces. Every displayed inequality is strict away from the stated switching surface. \(\square\)

## Verification

The companion file `verify.py` checks the rational spectral identities and both strict ordering regimes using Python's exact rational arithmetic. Execute `python verify.py` in the directory containing that file. The verifier tests the equality surface, the explicit fourfold error example, and a finite collection of parameter triples; the proof above, rather than those samples, establishes the quantified theorem for all admissible real parameters.

## Relationship to prior work

Nakatsukasa and Tang (arXiv:2605.05043, initially public 6 May 2026) prove an ordered improvement in leading *eigenvalue* approximations for Nyström versus Rayleigh--Ritz. Their Section 2 explicitly observes that an ordering of the quality of extraction subspaces does not imply an ordering for individual extracted eigenvectors; their Section 4 reports numerical eigenvector comparisons. The present theorem complements those results with a closed-form, discontinuous individual-eigenvector mode switch and the exact separating eigengap \(\delta_c\), under arbitrarily accurate two-dimensional trial subspaces. It does not contradict their eigenvalue ordering or their numerical observations.

Haas and Nakatsukasa (arXiv:2506.01207) give refined eigenvalue error bounds for Rayleigh--Ritz and projected singular values, not this Nyström-versus-Ritz individual eigenvector mode switch. Classical spectral-gap perturbation bounds explain why near-equal leading eigenvalues permit unstable individual eigenvectors, but do not give this method-specific switching surface or simultaneous fourfold eigenvalue-error improvement. Literature and published mathematical finding searches identified related Nyström sketch orientation and Ritz error phenomena but not this exact statement; the literature comparison is not a proof of absolute historical priority.

## Limitations

The gap \(\delta\) shrinks at order \(u\) in the arbitrarily accurate-subspace construction; no failure with a fixed positive leading eigengap as \(u\downarrow0\) is claimed. The counterexample concerns individual *ordered* leading eigenvectors and does not show that Nyström's leading two-dimensional extraction subspace is worse than the Ritz trial subspace. The matrix has a zero eigenvalue, though the Nyström core is nonsingular. Finite tests are not exhaustive. The claim does not classify all PSD inputs or numerical floating-point rounding effects.

## References

1. Y. Nakatsukasa and Z. Tang, *Finding accurate eigenvalues and eigenvectors of positive semi-definite matrices given a subspace*, arXiv:2605.05043v1 (6 May 2026); also consulted v2 (13 Nov 2026). https://arxiv.org/abs/2605.05043
2. I.-B. Haas and Y. Nakatsukasa, *Sharp error bounds for approximate eigenvalues and singular values from subspace methods*, arXiv:2506.01207v2 (2025). https://arxiv.org/abs/2506.01207
3. Y. Nakatsukasa, *Sharp error bounds for Ritz vectors and approximate singular vectors*, arXiv:1810.02532 (2018). https://arxiv.org/abs/1810.02532
