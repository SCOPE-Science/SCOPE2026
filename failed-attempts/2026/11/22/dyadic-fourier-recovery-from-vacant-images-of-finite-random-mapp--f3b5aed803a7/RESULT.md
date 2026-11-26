# Dyadic Fourier recovery from vacant images of finite random mappings

## Finding

For each integer \(n\ge1\), let \(G_n=\mathbb F_2^n\). Every mapping \(f:[n]\to[n]\) has a vacant-image set \(E(f)=[n]\setminus f([n])\). Define the integer-valued counting kernel
\[
q_n(x)=\#\{f:[n]\to[n]:\mathbf 1_{E(f)}=x\},\qquad x\in G_n,
\]
and let \(T_nh=q_n*h\), where convolution uses addition in \(G_n\) and counting measure. For a Walsh character indexed by \(S\subseteq[n]\), write \(k=|S|\) and \(\lambda_{n,k}=\sum_xq_n(x)(-1)^{\sum_{i\in S}x_i}\).

**Theorem.** For every \(n\ge1\) the multiplier depends only on \(k\), and
\[
\lambda_{n,k}=\sum_{j=0}^{k}\binom kj(-2)^j(n-j)^n.
\]
The complete dyadic valuation law, with \(\nu_2\) the exponent of two dividing a nonzero integer, is as follows:

1. When \(n\) is odd, every \(\lambda_{n,k}\) is odd.
2. When \(n\ge4\) is even, \(\nu_2(\lambda_{n,0})=n\nu_2(n)\), and for every \(1\le k\le n\),
\[
\boxed{\nu_2(\lambda_{n,k})=1+\nu_2(k).}
\]
3. At \(n=2\), the degree-zero, degree-one and degree-two multipliers are respectively \(4,2,0\).

Consequently, \(T_n\) is invertible over \(\mathbb R\) and \(\mathbb C\) exactly for \(n=1\) and all \(n\ge3\). Its only singular order is \(n=2\), with nullity one and rank three. For even \(n\ge4\), the multiplicity of valuation \(1+a\) among the nonconstant frequencies is exactly
\[
\sum_{\substack{1\le k\le n\\\nu_2(k)=a}}\binom nk,
\]
while the single constant frequency has valuation \(n\nu_2(n)\). The determinant therefore satisfies
\[
\nu_2(|\det T_n|)=n\nu_2(n)+\sum_{k=1}^n\binom nk(1+\nu_2(k))\qquad(n\ge4\text{ even}),
\]
and is odd for every odd \(n\).

## Assumptions and scope

All \(n^n\) mappings are counted once, with no restrictions on fixed points or indegrees. The vertex labels serve simultaneously as domain and target labels. The vacant-image profile is not the set of cyclic vertices: it is the set of vertices with indegree zero. The zero-degree Fourier character is the constant character. The conventions \(0^n=0\) for \(n\ge1\) and \(\nu_2(0)\) undefined are used. No conclusion about the signs or the magnitudes of the nonzero multipliers beyond their exact dyadic valuations is asserted.

The underlying occupancy kernel has the classical exact expression
\[
q_n(\mathbf 1_E)=(n-r)!\left\{\begin{matrix}n\\n-r\end{matrix}\right\},\qquad r=|E|,
\]
where braces denote a Stirling number of the second kind. This distribution and its usual occupancy interpretations are prior art; the theorem concerns the complete dyadic spectrum of its convolution transform.

## Proof

**1. Exact character sum.** Fix \(S\subseteq[n]\) of size \(k\). For any mapping \(f\), with \(I_i(f)=\mathbf1_{\{i\notin f([n])\}}\), its Walsh sign is
\[
(-1)^{\sum_{i\in S}I_i(f)}=\prod_{i\in S}(1-2I_i(f))
=\sum_{J\subseteq S}(-2)^{|J|}\mathbf1_{\{J\cap f([n])=\varnothing\}}.
\]
For a prescribed \(J\), all \(n\) images must lie in \([n]\setminus J\), giving exactly \((n-|J|)^n\) mappings. Summing and grouping by \(|J|\) proves the formula. Also, prescribing an exact vacant set \(E\) requires a surjection onto its complement; this gives the displayed Stirling expression.

**2. Odd orders.** If \(n\) is odd, the \(j=0\) term of the character sum is the odd integer \(n^n\); every term with \(j\ge1\) is even. Thus all multipliers are odd and nonzero, including \(n=1\).

**3. Even orders at least four.** Suppose \(n\ge4\) is even, \(1\le k\le n\), and put \(a=\nu_2(k)\). Separate the \(j=1\) summand:
\[
-2k(n-1)^n.
\]
As \(n-1\) is odd, this has valuation exactly \(a+1\). The \(j=0\) term has valuation \(n\nu_2(n)\ge n\ge a+2\), because \(a\le\lfloor\log_2 n\rfloor\) and \(n\ge\lfloor\log_2 n\rfloor+2\) for \(n\ge4\).

For \(2\le j\le k\), use the exact integer identity
\[
j\binom kj=k\binom{k-1}{j-1}
\]
to get
\[
\nu_2\!\left(2^j\binom kj\right)\ge a+j-\nu_2(j).
\]
If \(j\) is odd, then \(j\ge3\) and this lower bound is at least \(a+3\). If \(j\) is even, then \(n-j\) is even. If \(n-j=0\), the summand vanishes; otherwise its additional factor \((n-j)^n\) has valuation at least \(n\), and since \(j-\nu_2(j)\ge1\), the whole term has valuation at least \(a+n+1\). Hence all summands other than \(j=1\) are divisible by \(2^{a+2}\), whereas the \(j=1\) term is divisible by exactly \(2^{a+1}\). Cancellation at that valuation is impossible. Therefore \(\nu_2(\lambda_{n,k})=a+1\). At \(k=0\), the only term is \(n^n\), with valuation \(n\nu_2(n)\).

**4. Exceptional order and consequences.** Direct substitution at \(n=2\) yields \((\lambda_{2,0},\lambda_{2,1},\lambda_{2,2})=(4,2,0)\). Each degree-\(k\) multiplier has multiplicity \(\binom nk\) because the characters of \(G_n\) form an orthogonal basis. Nonzero multipliers therefore give the stated rank and invertibility results. For even \(n\ge4\), the constant frequency has valuation strictly larger than all nonconstant frequency valuations, so the dyadic multiplicities are disjoint. Multiplying the eigenvalues, or adding their valuations, gives the determinant statement.

## Verification

The standalone Python program `verify.py` is independent of the proof's valuation estimates. It enumerates all \(n^n\) maps for each \(1\le n\le6\), constructs the vacancy-count kernel directly from image sets, performs a full fast Walsh transform, and checks every multiplier against the inclusion-exclusion formula. Separately, it checks the exact surjection/Stirling counts. Exact integer arithmetic tests all degree multipliers through \(n=120\), including the parity classes, exceptional order and valuations. It passes 15,137 assertions with no floating-point arithmetic. These finite checks corroborate, but do not replace, the all-order proof.

To reproduce: run `python3 verify.py` from the directory containing this document and the script; no third-party libraries or data files are required.

## Relationship to prior work

Classical occupancy and random-mapping research already describes empty-image sets, image sizes, and their exact counting measures. In particular, Soria's 1996 seminar discusses image/preimage parameters, Hwang and Janson's 2006 study treats finite-urn occupancy distributions, and Bogachev, Gnedin and Yakubovich's 2006 work gives occupancy moments. None of these is claimed as a new enumeration.

Published work on the joint distribution of cyclic and terminal vertices gives exact factorial moments of zero-indegree counts and a binomial inversion formula. Its complete marginal law implies the present *unsigned counting kernel*, and by an additional Walsh transform it also yields the displayed character-sum formula. The added mathematical assertion here is the exact, all-degree **dyadic valuation and nonvanishing law**, including exceptional rank and determinant valuation; the checked published statements do not state that law. Related results on cyclic-vertex Fourier transforms concern a different vertex statistic. The existence of an earlier equivalent arithmetic evaluation remains an explicit priority risk.

## Limitations

The theorem is specific to \(n\) independent uniform images in an \(n\)-element target. It does not classify nonuniform target weights, a different number of draws, or all prime-adic valuations. The multipliers may be negative, and no positive-definiteness classification is asserted. The literature comparison is bounded: earlier books, unindexed arithmetic identities, or uninspected portions of papers may contain the same valuation law. No independent external validation has been performed.

## References

1. M. Soria, *Distribution of Image Points in Random Mappings*, Algorithms Seminar, November 10, 1996, https://algo.inria.fr/seminars/sem96-97/soria.html .
2. H.-K. Hwang and S. Janson, *Local limit theorems for finite and infinite urn models*, first preprint April 18, 2006, https://arxiv.org/abs/math/0604397 .
3. L. V. Bogachev, A. V. Gnedin and Yu. V. Yakubovich, *On the variance of the number of occupied boxes*, first preprint September 18, 2006, https://arxiv.org/abs/math/0609498 .
4. *Exact joint law of cyclic and terminal vertices in uniform random mappings* (2026), publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-joint-law-of-cyclic-and-terminal-vertices-in-uniform-rando--0c1fa0e07cad .
5. *Pruning invariance and sharp terminal-component anticorrelation in random mappings* (2026), publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-pruning-invariance-and-sharp-terminal-component-anticorrelation--e4cf3e3e51f2 .
