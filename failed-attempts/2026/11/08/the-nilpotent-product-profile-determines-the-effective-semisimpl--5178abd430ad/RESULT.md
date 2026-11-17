# The nilpotent-product profile determines the effective semisimple blocks of a finite ring

## Finding

Let \(R\) be a finite, nonzero, associative ring with identity, and let \(J=J(R)\) be its Jacobson radical. Write its Artin–Wedderburn quotient, uniquely up to factor order, as
\[
 R/J\cong\prod_{i=1}^{t}M_{d_i}(\mathbb F_{q_i}),
 \qquad t\ge1,\quad d_i\ge1,
\]
where each \(q_i\) is a prime power. For each integer \(k\ge1\), draw independent uniform \(X_1,\ldots,X_k\in R\), and define
\[
 p_k(R)=\Pr\bigl(X_1X_2\cdots X_k\text{ is nilpotent}\bigr).
\]
Put \(Q_i=q_i^{d_i}\). Then the **entire nilpotent-product profile** is
\[
 \boxed{p_k(R)=\prod_{i=1}^{t}\left[1-\bigl(1-Q_i^{-1}\bigr)^k\right]\quad(k\ge1).}
\]
Moreover, for any two such rings \(R\) and \(S\),
\[
 \boxed{p_k(R)=p_k(S)\ \text{for every }k\ge1
 \quad\Longleftrightarrow\quad
 \{q_i^{d_i}:1\le i\le t\}\text{ and the corresponding multiset for }S\text{ coincide}.}
\]
These are multisets, so multiplicity is retained. The probabilities determine the effective block sizes \(Q_i\), but not the separate field orders and matrix dimensions. In particular, a matrix algebra \(M_d(\mathbb F_q)\) and the field \(\mathbb F_{q^d}\) have identical profiles.

For the two-factor statistic introduced by Sarma and Subedi,
\[
 \boxed{p_2(R)=\prod_{i=1}^{t}\frac{2Q_i-1}{Q_i^2}\le\frac34,}
\]
with equality if and only if \(R/J(R)\cong\mathbb F_2\). In the finite unital setting this is equivalent to having a unique maximal (two-sided) radical quotient that is the two-element field. The displayed formula is an explicit, ring-by-ring determination for arbitrary finite unital rings, including noncommutative ones; it is distinct from the earlier classification of the *set of possible numerical values*.

## Assumptions and scope

Rings are finite, associative, unital, and nonzero, with no commutativity hypothesis. All products are ordered in the displayed order, the factors are independent and uniform, and nilpotent means some positive power is zero. The semisimple quotient and the prime powers are taken in the ordinary finite-ring sense. The empty-product convention is not used. The theorem treats every integer \(k\ge1\) simultaneously. It does not attempt to reconstruct the individual \(q_i\) or \(d_i\), since that is impossible from these probabilities.

## Proof

**1. Reduction through the radical.** Since \(R\) is finite, its Jacobson radical \(J\) is nilpotent: \(J^h=0\) for some \(h\ge1\). For any \(a\in R\), a nilpotent \(a\) maps to a nilpotent in \(R/J\). Conversely, if the image of \(a\) has zero \(m\)-th power, then \(a^m\in J\), so \(a^{mh}=0\). Thus nilpotence is detected exactly by reduction modulo \(J\). Independent uniform elements of \(R\) reduce to independent uniform elements of \(R/J\) because all additive cosets have size \(|J|\). Therefore
\[
 p_k(R)=p_k(R/J)\qquad(k\ge1).
\]

**2. Direct products.** An element in a finite direct product of rings is nilpotent if and only if each coordinate is nilpotent. The uniform product measure is the product of uniform measures. Hence
\[
 p_k(A_1\times\cdots\times A_t)=\prod_{i=1}^{t}p_k(A_i).
\]
By the Artin–Wedderburn theorem and the fact that every finite division ring is a field, it remains to compute \(p_k(M_n(\mathbb F_q))\) for every prime power \(q\), integer \(n\ge1\), and \(k\ge1\).

**3. A conditional rank lemma.** Let \(V=\mathbb F_q^n\). Fix a linear transformation \(A\in\operatorname{End}(V)\) of rank \(r\), write \(W=\operatorname{im}A\), and draw \(B\) uniformly from \(\operatorname{End}(V)\). The product \(AB\) is uniformly distributed among all linear maps \(V\to W\): each column of \(B\) is uniform in \(V\), and the surjective linear map \(A:V\to W\) sends it uniformly to \(W\), independently across columns.

Choose a complement \(U\) of \(W\). Every such map has block form, relative to \(V=W\oplus U\),
\[
 AB=\begin{pmatrix}C&D\\0&0\end{pmatrix},
\]
where \(C\) is uniform in \(\operatorname{End}(W)\), independent of \(D\). This block operator is nilpotent exactly when \(C\) is nilpotent (its image is in \(W\), and its restriction to \(W\) is \(C\)). The classical Fine–Herstein–Hall nilpotent count, with an accessible bijective proof given by Leinster, states that a uniform endomorphism of an \(r\)-dimensional vector space over \(\mathbb F_q\) is nilpotent with probability \(q^{-r}\). The convention at \(r=0\) is \(q^0=1\). It follows that
\[
 \boxed{\Pr(AB\text{ nilpotent}\mid A)=q^{-\operatorname{rank}A}.}
\]
The cited nilpotent count is established prior work, not asserted as a new lemma.

**4. All numbers of factors.** Let \(P_{k-1}=X_1\cdots X_{k-1}\), with \(P_0=I\). The conditional rank lemma gives
\[
 p_k(M_n(\mathbb F_q))
 =\mathbb E\,q^{-\operatorname{rank}P_{k-1}}
 =q^{-n}\mathbb E\,|\ker P_{k-1}|.
\]
For a fixed nonzero \(v\in V\), each independent uniform matrix takes a nonzero current vector to a uniformly random vector of \(V\). Hence the probability that the successive image of \(v\) remains nonzero after \(k-1\) matrices is \((1-q^{-n})^{k-1}\). Once zero, it remains zero. By linearity of expectation over the \(q^n\) possible kernel vectors,
\[
 \mathbb E|\ker P_{k-1}|
 =1+(q^n-1)\left[1-(1-q^{-n})^{k-1}\right].
\]
Substitution simplifies, for every \(k\ge1\), to
\[
 \boxed{p_k(M_n(\mathbb F_q))=1-(1-q^{-n})^k.}
\]
This matrix-product formula is already contained in Kovács's 1987 enumeration (for arbitrary \(k\)); the calculation here supplies a direct verification and prepares its use in the ring-by-ring statement. Applying Steps 1 and 2 now proves the first boxed formula.

**5. Recovering the effective block multiset.** Put \(a_i=1-Q_i^{-1}\), so \(0<a_i<1\) and \(p_k=\prod_i(1-a_i^k)\). Write \(a_*\) for the maximum \(a_i\), occurring \(m_*\) times. Expansion of the finite product gives
\[
 1-p_k=m_*a_*^k+o(a_*^k)\qquad(k\to\infty),
\]
because every other individual base is smaller than \(a_*\), while products of two or more bases are strictly smaller than \(a_*\). Therefore the sequence \((p_k)_{k\ge1}\) determines
\[
 a_*=\lim_{k\to\infty}(1-p_k)^{1/k},
 \qquad m_*=\lim_{k\to\infty}\frac{1-p_k}{a_*^k}.
\]
Divide each \(p_k\) by \((1-a_*^k)^{m_*}\). The remaining sequence is a product of the same form with all maximal factors removed. Repeating recovers every \(a_i\), with multiplicity, and therefore every \(Q_i=(1-a_i)^{-1}\). Conversely, equal multisets give identical product formulas. If one finite product has been fully stripped, its remaining sequence is identically one; a nonempty product of factors with \(0<a<1\) is never identically one. This proves the stated if-and-only-if.

**6. Maximum of the two-factor probability.** For every integer \(Q\ge2\), the factor \((2Q-1)/Q^2\) is at most \(3/4\), with equality only at \(Q=2\), and is always strictly below one. A nonempty product of these factors attains \(3/4\) precisely when it has one factor and \(Q=2\), which is equivalent to \(R/J(R)\cong\mathbb F_2\). This proves the final claim.

## Verification

The accompanying standalone program `verify_nil_product.py` uses direct finite ring multiplication, tests nilpotency by matrix powers, and counts products by a dynamic histogram; it does not use the theorem to count. Its `verification_output.txt` records 31 exact product-length tests across nine small matrix and triangular-matrix rings and four tests of a semisimple direct product. All 35 comparisons agree with the formula. These finite checks do not establish the universal theorem; Steps 1–6 do.

Examples from the exact calculations include \(p_2(M_2(\mathbb F_2))=7/16\), \(p_2(M_3(\mathbb F_2))=15/64\), \(p_2(\mathrm{UT}_2(\mathbb F_2))=9/16\), and \(p_2(\mathbb F_2\times M_2(\mathbb F_2))=21/64\). The first equals \(p_2(\mathbb F_4)\), but the theorem says more: the entire profiles agree.

To reproduce: save both supplied verification artifacts in one directory and run `python verify_nil_product.py` using Python 3. No additional packages or input datasets are required.

## Relationship to prior work

Sarma and Subedi (2026), *Nilpotent Product Probability of Finite Rings*, introduce the two-factor nilpotent-product probability. Their full accessible text treats general bounds, commutative ring decompositions (including a statement of the set of achievable numerical values in Corollary 2.18), and upper-triangular matrix rings (Theorem 2.24). The statement about the **set** of achievable values is credited and is not treated as new here. Their article does not supply the explicit radical/Wedderburn **ring-by-ring** profile formula nor the multiset reconstruction theorem for all finite noncommutative unital rings.

Kovács (1987), *Some enumeration problems for matrices over a finite field*, already gives the probability that a product of any fixed positive number of independent uniform square matrices over a finite field is nilpotent. This matrix-factor law is an input and is not claimed as new. Leinster (2020 preprint, 2021 publication) supplies a full accessible proof of the classical nilpotent endomorphism count. Chen and collaborators (2025) treat pairs of linear maps and include the two-factor square-matrix case. None of these sources, as inspected, states the classification of the **full profile for arbitrary finite unital rings** by the multiset of effective semisimple block sizes. Blackburn (2022) supplies background finite-ring structure, but studies enumeration of rings rather than this probability profile.

The added claim is specifically the complete profile of arbitrary finite unital rings and its exact equality criterion. It combines established matrix counting with nilpotent-ideal lifting and a recoverability argument. The combination may have occurred earlier in unpublished or differently indexed work; the lack of a search hit is not proof of priority.

## Limitations

The theorem assumes a finite nonzero unital associative ring. Infinite rings, nonassociative structures, nonunital rings, nonuniform factors, and dependent samples are not covered. The profile cannot separate \(q_i\) from \(d_i\) when their product exponent \(q_i^{d_i}\) is fixed; no stronger reconstruction is asserted. All results are exact, but external independent mathematical review is not supplied. The full 1987 Kovács article was not available during comparison; its reported matrix-factor theorem is expressly credited, and a possible older extension to radical quotients remains a priority risk.

## References

1. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1, first publicly submitted 2026-10-06, full HTML: https://arxiv.org/html/2610.07892v1.
2. A. Kovács, *Some enumeration problems for matrices over a finite field*, Linear Algebra and its Applications **94** (1987), 223–236. The accessible abstract records the all-factor matrix nilpotency formula.
3. T. Leinster, *The probability that an operator is nilpotent*, arXiv:1912.12562v2, https://arxiv.org/html/1912.12562v2 (theorem and proof); American Mathematical Monthly **128** (2021), 371–375.
4. W. Chen, M. S. Im, M. Khovanov, C. Lillja and N. Rugo, *Pairs of eventually constant maps and nilpotent pairs*, arXiv:2512.03367, https://arxiv.org/abs/2512.03367.
5. S. Blackburn, *The enumeration of finite rings*, Journal of the London Mathematical Society **106** (2022), 3240–3262, https://doi.org/10.1112/jlms.12661.
6. D. Dolžan, *The probability of zero multiplication in finite rings*, Bulletin of the Australian Mathematical Society **106** (2022), 83–88; this is a different probability (zero rather than nilpotent products).
