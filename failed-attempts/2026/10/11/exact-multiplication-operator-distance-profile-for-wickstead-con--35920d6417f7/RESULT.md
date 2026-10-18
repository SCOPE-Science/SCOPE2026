# Exact multiplication-operator distance profile for Wickstead constant-diagonal projections
## Finding
Let \(K\) be a nonempty compact Hausdorff space and let \(P:C(K,\mathbb R)\to C(K,\mathbb R)\) be a positive projection with \(P\mathbf 1=\mathbf 1\). Assume there is \(\alpha>0\) such that \(\alpha I\le P\), and whenever \(0\le M_g\le P\) for a positive multiplication operator \(M_g\), one has \(\|g\|_\infty\le\alpha\). Define
\[
d(t)=P^*\delta_t(\{t\}),\qquad t\in K.
\]
Then, for every \(f\in C(K,\mathbb R)\),
\[
\boxed{\ \|P-M_f\|=\sup_{t\in K}\bigl(1-d(t)+|d(t)-f(t)|\bigr)\ }.
\]
The focal theorem and its proof imply \(d(t)\ge\alpha\) for all \(t\), that \(d(t_0)=\alpha\) for at least one \(t_0\), and that \(\alpha=1/n\) for some \(n\in\mathbb N\). Therefore
\[
\operatorname{dist}\bigl(P,\{M_f:f\in C(K,\mathbb R)\}\bigr)=1-\alpha.
\]
Moreover, \(M_f\) is a best multiplication-operator approximant exactly when
\[
\alpha\le f(t)\le 2d(t)-\alpha\qquad\text{for every }t\in K.
\]
In particular \(\alpha I\) is always best. Restricting to scalar multiples gives the exact V-shaped profile
\[
\|P-cI\|=1-\alpha+|c-\alpha|\qquad(c\in\mathbb R),
\]
so \(\alpha I\) is the unique best scalar multiple and
\[
\|I-P\|=2(1-\alpha)=2\left(1-\frac1n\right).
\]

## Assumptions and scope
The scalar field is real, as in the \(C(K,\mathbb R)\) formulation of the focal result. The hypotheses are exactly the positive, unital, constant-diagonal assumptions appearing in Theorem 2.1 of the focal source, with the nonzero case \(\alpha>0\). The function \(d\) is only used pointwise; no continuity of \(d\) is assumed or needed. The statement concerns approximation by multiplication operators in the ordinary operator norm on \(C(K,\mathbb R)\).

## Proof
For each \(t\in K\), set \(\mu_t=P^*\delta_t\). Positivity of \(P\) and \(P\mathbf1=\mathbf1\) imply that \(\mu_t\) is a positive probability measure. Write
\[
\mu_t=d(t)\delta_t+\rho_t,
\]
where \(\rho_t\ge0\) and \(\rho_t(\{t\})=0\). Hence \(\|\rho_t\|=1-d(t)\). The order inequality \(\alpha I\le P\) gives \(d(t)\ge\alpha\) for every \(t\). Lemma 2.11 in the proof of the focal theorem produces a point \(t_0\) whose entire finite atomic block has coefficient \(\alpha\); in particular \(d(t_0)=\alpha\).

For \(f\in C(K,\mathbb R)\),
\[
(P-M_f)^*\delta_t=(d(t)-f(t))\delta_t+\rho_t.
\]
The two measures on the right are mutually singular, so their total variation norms add:
\[
\|(P-M_f)^*\delta_t\|=|d(t)-f(t)|+1-d(t).
\]
For any bounded operator \(T:C(K)\to C(K)\),
\[
\|T\|=\sup_{t\in K}\|T^*\delta_t\|,
\]
because the left side is \(\sup_{\|h\|_\infty\le1}\sup_t|(Th)(t)|\). Applying this identity to \(P-M_f\) proves the boxed norm formula.

Choosing the constant function \(f=\alpha\) gives, using \(d(t)\ge\alpha\),
\[
1-d(t)+|d(t)-\alpha|=1-\alpha
\]
for every \(t\), so the distance to multiplication operators is at most \(1-\alpha\). Conversely, at \(t_0\), every \(f\) satisfies
\[
1-d(t_0)+|d(t_0)-f(t_0)|=1-\alpha+|\alpha-f(t_0)|\ge1-\alpha.
\]
Thus the distance is exactly \(1-\alpha\).

The norm formula is at most \(1-\alpha\) precisely when
\[
|d(t)-f(t)|\le d(t)-\alpha
\]
for every \(t\), which is equivalent to
\[
\alpha\le f(t)\le2d(t)-\alpha
\]
pointwise. This proves the characterization of all best multiplication-operator approximants. For \(f\equiv c\), if \(c\le\alpha\), every point contributes \(1-c\); if \(c>\alpha\), every contribution is at most \(1+c-2\alpha\), and equality occurs at \(t_0\). Hence
\[
\|P-cI\|=1-\alpha+|c-\alpha|.
\]
Its unique minimizer is \(c=\alpha\). Finally, the focal theorem gives \(\alpha=1/n\), and substituting \(c=1\) gives the formula for \(\|I-P\|\).

## Verification
The proof is symbolic. The only non-elementary input is the focal source's constant-diagonal theorem together with the proof-level fact that some point has diagonal atom exactly \(\alpha\). The total-variation step uses mutually singular measures \(\delta_t\) and \(\rho_t\). No finite sampling, numerical tolerance, asymptotic argument, or external certificate is used.

The boundary case \(\alpha=1\) is included: the formula gives \(\|P-I\|=0\), hence \(P=I\). The result does not assert an analogous formula for \(\alpha=0\), where the focal proof need not produce a point attaining a zero diagonal atom.

## Relationship to prior work
Muñoz-Lahoz proves that the constant-diagonal parameter is either \(0\) or a reciprocal integer. In the \(C(K)\) proof, the representing measures \(\mu_t=P^*\delta_t\) are reduced to finite atomic probability measures with diagonal mass at least \(\alpha\), and Lemma 2.11 produces an atomic block whose coefficients are all exactly \(\alpha\). The present result uses that structure to identify the complete operator-norm profile against every multiplication operator, the exact distance to the multiplication-operator subspace, and the full set of best approximants.

Wickstead's earlier work formulates the order-theoretic diagonal problem and studies representation and norm questions for two-dimensional Riesz algebras. The inspected material does not state the multiplication-operator metric projection formula above. Targeted searches for constant-diagonal positive projections, scalar perturbation norms, complementary projection norms, and best multiplication-operator approximants found no statement implying this exact profile.

## Limitations
The claim is restricted to the positive nonzero constant-diagonal case on real \(C(K)\). It does not classify best approximants by larger operator algebras, does not claim uniqueness among multiplication operators, and does not treat the \(\alpha=0\) case. Absolute novelty cannot be certified by search; an older equivalent formula could exist under Markov-kernel or positive-projection terminology.

## References
1. D. Muñoz-Lahoz, *Wickstead's conjecture on positive projections and non-representable Banach lattice algebras*, arXiv:2604.14697v1, first posted 2026-04-16; current full text inspected through the revised arXiv version.
2. A. W. Wickstead, *Two dimensional unital Riesz algebras, their representations and norms*, Positivity 21 (2017), 787–801, DOI:10.1007/s11117-015-0349-1.
