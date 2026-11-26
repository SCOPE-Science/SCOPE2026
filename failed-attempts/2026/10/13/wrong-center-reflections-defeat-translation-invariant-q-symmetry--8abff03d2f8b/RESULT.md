# Wrong-center reflections defeat translation-invariant q-symmetry characterizations
## Finding

Let \(X\sim N(0,1)\) and define \(q(x)=1-x\). The map \(q:\mathbb R\to\mathbb R\) is a strictly decreasing differentiable bijection and an involution. It does **not** make \(X\) q-symmetric, because
\[
q(X)\sim N(1,1)\neq N(0,1).
\]

Even so, the entropy identities used as converses in the recent q-symmetry characterizations all hold for this wrong reflection center. For every fixed integer \(i\ge1\) and every \(n\ge i\),
\[
H(X_{i:n})=H\!\left(q(X_{n-i+1:n})\right).
\]
At the admissible choice \(\alpha=2\), the analogous equalities also hold for Tsallis entropy, Rényi entropy, the information generating function, and extropy. Consequently, the converse directions of Theorems 3.1--3.4 and 4.1 in Ahmadi and Balakrishnan fail as stated.

There is a structural reason. For an absolutely continuous law with positive density on \(\mathbb R\), define its intrinsic quantile reflection
\[
p(x)=F^{-1}(1-F(x)).
\]
Condition (ii) of the source's Lemma 3.1 implies
\[
q'(x)=p'(x),
\]
and hence
\[
q(x)=p(x)+C
\]
for a constant \(C\). The differential condition therefore loses exactly one additive degree of freedom. An extra anchor, such as agreement of \(q\) and \(p\) at the median, is needed to recover the prescribed map.

## Assumptions and scope

The concrete counterexample uses the standard normal law, so the support is the connected interval \(\mathbb R\), the density is strictly positive and smooth, and all order-statistic Shannon, Rényi, Tsallis, information-generating, and extropy quantities used below are finite at \(\alpha=2\).

The claim concerns the converse characterization of a **prescribed** decreasing map \(q\). It does not dispute the classical center-free statement that equality of suitable upper- and lower-order-statistic information measures can characterize symmetry about *some* location.

The structural calculation \(q=p+C\) is asserted here for full support \(\mathbb R\) under the differentiability and positive-density hypotheses needed by the source's quantile-density identity. No claim is made that the same one-parameter freedom survives unchanged on every bounded or half-line support.

## Proof

For the standard normal law, symmetry gives
\[
X_{i:n}\overset{d}{=}-X_{n-i+1:n}.
\]
Therefore
\[
q(X_{n-i+1:n})
=
1-X_{n-i+1:n}
\overset{d}{=}
1+X_{i:n}.
\]
Differential Shannon entropy is invariant under translation, so
\[
H\!\left(q(X_{n-i+1:n})\right)
=
H(1+X_{i:n})
=
H(X_{i:n}).
\]
This proves that the hypothesis in the converse direction of Theorem 3.1 is satisfied for every \(i\) and every \(n\ge i\), although \(X\not\overset{d}{=}q(X)\).

The same argument applies to every density functional that is invariant under translation. If a random variable has density \(f\), then a translate by a constant has density \(f(\,\cdot-c)\), and hence
\[
\int_{\mathbb R} f(x-c)^2\,dx
=
\int_{\mathbb R} f(x)^2\,dx.
\]
Thus at \(\alpha=2\), the Tsallis entropy, Rényi entropy, information generating function, and extropy of \(1+X_{i:n}\) equal those of \(X_{i:n}\). This gives the same counterexample to the converse directions of Theorems 3.2, 3.3, 3.4, and 4.1.

For the structural statement, let
\[
p(x)=F^{-1}(1-F(x)).
\]
The source's Lemma 3.1(ii) is
\[
\delta(u)
=
-q'\!\left(F^{-1}(1-u)\right)\delta(1-u).
\]
Put \(u=1-F(x)\). Since
\[
\delta(1-F(x))=\frac{1}{f(p(x))}
\quad\text{and}\quad
\delta(F(x))=\frac{1}{f(x)},
\]
the displayed condition becomes
\[
\frac{1}{f(p(x))}
=
-\frac{q'(x)}{f(x)}.
\]
Hence
\[
q'(x)=-\frac{f(x)}{f(p(x))}.
\]
Differentiating the definition of \(p\) gives exactly
\[
p'(x)=-\frac{f(x)}{f(p(x))}.
\]
Therefore \(q'(x)=p'(x)\) on \(\mathbb R\), so connectedness yields \(q(x)=p(x)+C\).

For the standard normal law, \(p(x)=-x\). Taking \(C=1\) gives the explicit wrong-center involution \(q(x)=1-x\), completing both the counterexample and the diagnosis.

## Verification

The proof is symbolic. The counterexample satisfies the source's stated support, monotonicity, differentiability, and finiteness requirements. No finite enumeration or numerical approximation is used.

The source's own location-symmetry subsection is consistent with the diagnosis: the earlier quantile-density symmetry condition is described there as implying the existence of a location center, rather than identifying a preassigned center. The new q-symmetry converse tries to recover a prescribed transformation from a derivative relation that does not retain its additive constant.

## Relationship to prior work

Ahmadi and Balakrishnan introduce q-symmetry and state the fixed-\(q\) entropy/extropy characterizations in their 2026 article. Their primary classification is 62E10, and the article was published online on 27 May 2026.

Earlier work by Fashandi and Ahmadi (2012) characterizes ordinary symmetry through equality of Rényi entropies of upper and lower order statistics. Ahmadi and Fashandi (2019) extends this theme to several information measures. Those results concern symmetry about some center and therefore do not imply a characterization of a preassigned reflection \(q(x)=c-x\). The distinction between existence of a center and identification of a specified center is exactly what the counterexample exposes.

Targeted searches for the exact 2026 article, its DOI, q-symmetric order-statistic entropy characterizations, wrong-center reflections, translation invariance, and correction/corrigendum language did not locate a published correction or an equivalent counterexample.

## Limitations

The result does not address weighted extropy in Theorem 4.2, which is not translation invariant because its weight depends on the absolute observation value.

The additive-constant diagnosis is proved here for full support \(\mathbb R\). Boundary conditions can remove translation freedom on other supports, so any corrected theorem should be formulated with support geometry and an explicit anchor in view.

A very recent corrigendum, author note, or non-indexed observation could reduce originality. None was located in the searches performed.

## References

1. J. Ahmadi and N. Balakrishnan, “Characterizations of q-symmetric continuous distributions based on properties of order statistics of entropy-types,” *Statistics*, published online 27 May 2026, DOI 10.1080/02331888.2026.2679014.
2. M. Fashandi and J. Ahmadi, “Characterizations of symmetric distributions based on Rényi entropy,” *Statistics & Probability Letters* 82 (2012), 798--804, DOI 10.1016/j.spl.2012.01.004.
3. J. Ahmadi and M. Fashandi, “Characterization of symmetric distributions based on some information measures properties of order statistics,” *Physica A* 517 (2019), 141--152, DOI 10.1016/j.physa.2018.11.009.
