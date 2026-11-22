# Piecewise height and exact distribution for binary words with isolated one-markers

## Finding
Let \(t\ge3\), let \(a_0,\ldots,a_t\) be positive integers, and write
\[
 w=0^{a_0}1\,0^{a_1}1\cdots 1\,0^{a_t}.
\]
Let \(h(w)\) be the least integer \(H\) such that no other binary word has exactly the same scattered subsequences of lengths at most \(H\). Then
\[
 \boxed{h(w)=t+1+\max_{0\le i\le t}a_i.}
\]
Thus the longest zero gap, together with the marker count, completely determines the distinguishing depth on this entire infinite family.

For \(n\ge 2t+1\), the exact number \(N_t(n,H)\) of these length-\(n\), weight-\(t\) words with \(h(w)\le H\), at any integer \(H\ge t+2\), is
\[
 \boxed{N_t(n,H)=\sum_{j=0}^{t+1}(-1)^j\binom{t+1}{j}
 \binom{n-t-1-j(H-t-1)}{t}.}
\]
Here a binomial coefficient with a top index smaller than its nonnegative bottom index is zero. At \(H<t+2\), the count is zero. Summing over all possible word lengths gives precisely \((H-t-1)^{t+1}\) words of this form with height at most \(H\).

For fixed \(t\ge3\), choose uniformly among these length-\(n\) words, and put \(S=n-t\), \(k=t+1\). As \(n\) increases, the normalized variable \((h(w)-t-1)/S\) converges in distribution to the maximum coordinate of a uniform \((k-1)\)-simplex point, with cumulative distribution function
\[
 F_t(x)=\sum_{j=0}^{k}(-1)^j\binom{k}{j}(1-jx)_+^{k-1},\quad 0\le x\le1,
\]
where \((y)_+=\max(y,0)\). Its exact limiting mean and variance are
\[
 \mathbb E X=\frac{H_k}{k},\qquad
 \operatorname{Var}(X)=\frac{H_k^2+H_k^{(2)}}{k(k+1)}-\frac{H_k^2}{k^2},
\]
with \(H_k=\sum_{i=1}^{k}1/i\) and \(H_k^{(2)}=\sum_{i=1}^{k}1/i^2\). These are familiar longest-spacing moments; the new identification is their occurrence as a scattered-subsequence distinguishing-depth law.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), and scattered subsequences may skip arbitrary positions. The comparison word in the definition of height is unrestricted: it need not have the same length, weight, endpoints, or forbidden-factor conditions. The words considered have exactly \(t\ge3\) ones, no adjacent ones, and at least one zero before the first and after the last one. Every one of the \(t+1\) zero gaps is strictly positive. The count does not apply without modification when an endpoint or internal zero gap is permitted to vanish. The probabilistic limit holds for fixed \(t\) with \(n\to\infty\), not uniformly for growing \(t\).

## Proof
**Upper bound.** Every word with the same subsequences through depth \(t+1+M\), with \(M=\max_i a_i\), has exactly \(t\) ones: \(1^t\) occurs and \(1^{t+1}\) does not. For every \(0\le i\le t\), the subsequence \(1^i0^{a_i}1^{t-i}\) occurs, while \(1^i0^{a_i+1}1^{t-i}\) does not. Each requires all \(t\) ones, fixing the respective zero gap uniquely to \(a_i\) in any comparison word. All distinguishing templates have length at most \(t+M+1\), so the word is uniquely determined at that depth.

**Lower bound.** We use the insertion characterization proved in Proposition 3.1 of Praveen–Schnoebelen–Veron–Vialard (2023):
\[
 h(w)=1+\max_{w=uv,\ b\in\{0,1\}}
 \bigl(r(u,b)+\ell(b,v)\bigr),
\]
where \(r(u,b)\) is the largest depth at which \(u\) and \(ub\) have identical scattered-subsequence sets, and \(\ell(b,v)=r(v^{\mathrm{rev}},b)\). Their Lemma 4.1 gives \(r(u0,0)=r(u,0)+1\).

Fix a gap index \(i\). Let \(P_i\) be the prefix ending just after the first \(i\) ones, and \(R_i\) the suffix beginning just before the remaining \(t-i\) ones, with the zero gap removed. For \(i=0\) the prefix is empty, and for \(i=t\) the suffix is empty. Because all zero gaps are positive, \(P_i\) contains the alternating subsequence \((01)^i\), which itself contains every binary word of length \(i\) as a subsequence. Thus appending a zero to \(P_i\) introduces no new subsequence of length at most \(i\). It does introduce the absent word \(1^i0\) of length \(i+1\), proving \(r(P_i,0)=i\). Symmetrically, \(r(R_i^{\mathrm{rev}},0)=t-i\).

Cut the \(i\)-th zero gap after \(x\) of its \(a_i\) zeros, with \(0\le x\le a_i\). The repeated-zero lemma gives
\[
 r(P_i0^x,0)=i+x,\qquad
 \ell(0,0^{a_i-x}R_i)=t-i+a_i-x.
\]
The insertion characterization therefore gives \(h(w)\ge t+a_i+1\) for each \(i\), hence \(h(w)\ge t+M+1\). This matches the upper bound, including the end-gap cases.

**Exact enumeration.** Set \(S=n-t\) and \(B=H-t-1\). Each eligible word corresponds bijectively to a positive integer composition \(a_0+\cdots+a_t=S\). By the height formula, the desired compositions have all parts at most \(B\); their ordinary generating function by zero count is \((z+z^2+\cdots+z^B)^{t+1}\). Writing this as \(z^{t+1}(1-z^B)^{t+1}/(1-z)^{t+1}\) and extracting the coefficient of \(z^S\) proves the stated alternating binomial sum. Summing over \(S\) gives exactly \(B^{t+1}\).

**Limiting distribution and moments.** For uniformly chosen positive compositions of \(S\) into \(k=t+1\) parts, there are \(\binom{S-1}{k-1}\) choices. Inclusion-exclusion gives
\[
 \Pr\left(\frac{\max_i a_i}{S}\le x\right)=
 \sum_{j=0}^{k}(-1)^j\binom{k}{j}
 \frac{\binom{S-1-j\lfloor Sx\rfloor}{k-1}}{\binom{S-1}{k-1}}.
\]
Each fixed \(j\) term converges to \((1-jx)_+^{k-1}\), giving the stated distribution. Uniform boundedness in \([0,1]\) allows convergence of moments. Integrating the tail \(1-F_t\) gives \(\mathbb E X=k^{-1}\sum_{j=1}^{k}(-1)^{j+1}\binom{k}{j}/j=H_k/k\), and integrating \(2x(1-F_t(x))\) gives \(\mathbb E X^2=(H_k^2+H_k^{(2)})/[k(k+1)]\). Subtraction proves the variance.

## Verification
Run `python3 verify.py` (standard library only). It separately implements the source's side-distance recursion and exact insertion/subsequence-set comparison, not the closed-form height as a computation of height. The finite test passes 3,240 dynamic-height cases for marker counts three through six, 324 direct insertion/subsequence cases for marker counts three and four, and 261 inclusion-exclusion coefficient cases. These tests are corroboration, not a proof of the infinite claims. The argument above, including the cited insertion proposition, is the proof.

## Relationship to prior work
Praveen, Schnoebelen, Veron, and Vialard (2023) define wordwise piecewise height and prove the insertion characterization and a general algorithm. Schnoebelen and Vialard (2024) give a general compressed-run algorithm for all binary words and special formulas for other block configurations. Those algorithms imply computability of every individual height, but the inspected statements do not give the present isolated-one, arbitrary-marker-count closed form, its exact bounded-height composition enumerator, or its limiting height law. Earlier work independently treats the full two-one-marker case, which is excluded here by \(t\ge3\). A separate four-run height enumerator addresses a structurally different family. The longest-spacing distribution and harmonic moments are classical as probability facts; their appearance here follows from the new structural identification.

## Limitations
The result requires positive zero gaps and fixed binary alphabet. It does not classify words with adjacent ones or missing endpoint zero runs, or the regime of a marker count growing with word length. The mathematical review is same-model only, not an independent audit. Searches and comparisons do not rule out unindexed or differently phrased earlier statements; priority remains subject to external literature review. Finite computations alone cannot certify the all-parameter claims.

## References
1. M. Praveen, Ph. Schnoebelen, J. Veron, I. Vialard, *On the piecewise complexity of words and periodic words*, arXiv:2311.15431v1, 26 November 2023, particularly Proposition 3.1 and Lemma 4.1. https://arxiv.org/abs/2311.15431
2. Ph. Schnoebelen and I. Vialard, *On the piecewise complexity of words*, arXiv:2412.16560v1, 21 December 2024, particularly Section 5. https://arxiv.org/abs/2412.16560
3. P. Karandikar and Ph. Schnoebelen, *The height of piecewise-testable languages and the complexity of the logic of subwords*, Logical Methods in Computer Science 15(2), 2019; first available arXiv:1511.01807, 5 November 2015. https://arxiv.org/abs/1511.01807
