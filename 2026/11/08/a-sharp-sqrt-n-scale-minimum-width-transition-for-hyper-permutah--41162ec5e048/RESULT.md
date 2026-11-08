# A sharp \(\sqrt n\)-scale minimum-width transition for hyper-permutahedra

## Finding
For integers \(n\ge3\) and \(2\le k\le n\), define the (unscaled) hyper-permutahedron
\[
P_{n,k}=\sum_{\substack{S\subseteq[n]\\|S|=k}}\operatorname{conv}\{e_i:i\in S\}\subset\mathbb R^n.
\]
This is a polytope of intrinsic dimension \(n-1\), contained in the affine hyperplane \(\sum_i x_i=\binom nk\). Define
\[
C_{n,k}(s)=\binom nk-\binom sk-\binom{n-s}k,
\qquad1\le s\le n-1,
\]
with \(\binom ak=0\) for \(a<k\). Its intrinsic minimum **Euclidean** directional width is exactly
\[
\boxed{\operatorname{width}_{\min}(P_{n,k})
=\min_{1\le s\le\lfloor n/2\rfloor}
 C_{n,k}(s)\sqrt{\frac n{s(n-s)}}.}
\]
For each nonempty proper \(S\subset[n]\), let
\[
 v_S=\frac{\mathbf1_S-(|S|/n)\mathbf1}{\sqrt{|S|(n-|S|)/n}}.
\]
The **entire** set of minimizing oriented unit normals is precisely \(\{\pm v_S:\ |S|\text{ attains the displayed minimum}\}\), including all ties; no other normals minimize.

There is a sharp asymptotic transition. If integers \(k_n\) satisfy \(k_n/\sqrt n\to c\in(0,\infty)\), then
\[
\boxed{\lim_{n\to\infty}
\frac{\sqrt n\operatorname{width}_{\min}(P_{n,k_n})}{\binom n{k_n}}
=\min\{c,2\}.}
\]
If \(0<c<2\), then for all sufficiently large \(n\), the *only* minimizing normals are the signed singleton-cut normals \(\pm v_{\{i\}}\), \(i\in[n]\). If \(c>2\), then for all sufficiently large \(n\), the *only* minimizing normals are the signed balanced-cut normals \(\pm v_S\) with \(|S|=\lfloor n/2\rfloor\) or \(|S|=\lceil n/2\rceil\). At \(c=2\) only the limiting width formula is asserted; finite-dimensional equality and the eventual minimizing type are not claimed.

## Assumptions and scope
Widths and unit normals are measured using the ordinary Euclidean metric restricted to the linear hyperplane \(H=\{u:\sum_i u_i=0\}\). The sums defining \(P_{n,k}\) have one unweighted standard coordinate simplex for every distinct \(k\)-subset; there is no rescaling or volume normalization. In the asymptotic statement, \(c\) is fixed and positive and \(n\) tends through integers with \(2\le k_n\le n\). The exact finite formula also covers \(k=2\) (a complete-graphical zonotope) and \(k=n\) (a single simplex).

## Proof
**1. Width of a cut.** For \(u\in H\), additivity of support functions under Minkowski sums gives
\[
W_{P_{n,k}}(u)=\sum_{|T|=k}\big(\max_{i\in T}u_i-\min_{i\in T}u_i\big).
\]
For the unnormalized cut \(\mathbf1_S-(s/n)\mathbf1\), where \(s=|S|\), each term is one exactly when \(T\) meets both sides of the cut, and zero otherwise. Counting these mixed hyperedges gives \(C_{n,k}(s)\). The cut normal has norm \(\sqrt{s(n-s)/n}\), proving the stated candidate value.

**2. No multilevel direction can improve a cut.** Fix a nonconstant \(u\in H\) and sort its coordinates \(u_{i_1}\le\cdots\le u_{i_n}\). Put \(d_j=u_{i_{j+1}}-u_{i_j}\ge0\) and \(S_j=\{i_{j+1},\ldots,i_n\}\). Write \(a_j=\mathbf1_{S_j}-(|S_j|/n)\mathbf1\). The telescoping identity gives \(u=\sum_{j=1}^{n-1}d_ja_j\). All these vectors lie in the same braid cone, so each hyperedge's range is additive along this decomposition, hence
\[
W(u)=\sum_j d_j C_{n,k}(|S_j|).
\]
Let \(m\) be the least normalized cut width. Then
\[
W(u)\ge m\sum_jd_j\|a_j\|_2\ge m\|u\|_2.
\]
If at least two different gaps \(d_j\) are positive, the last triangle inequality is strict because the corresponding centered proper-set indicators are not parallel and have positive coefficients. Thus equality for a unit \(u\) forces exactly one positive gap, making \(u=\pm v_S\) for a minimizing cut. This establishes the exact formula and all equality cases.

**3. Normalize the uniform-hypergraph cut count.** Let \(M=\binom n{k_n}\), \(r=\lfloor n/2\rfloor\), and
\[
p_n(s)=C_{n,k_n}(s)/M,
\qquad B_n(s)=\frac{n\,p_n(s)}{\sqrt{s(n-s)}}.
\]
Thus \(\sqrt n\operatorname{width}_{\min}(P_{n,k_n})/M=\min_{1\le s\le r}B_n(s)\).
For any fixed positive integer \(s\), the identity
\[
\frac{\binom{n-s}{k_n}}M
=\frac{(n-k_n)_{s}}{(n)_{s}}
\]
(with falling factorials) and \(k_n/\sqrt n\to c>0\) imply \(p_n(s)=s k_n/n+O_s(k_n^2/n^2)\). Thus \(B_n(s)\to c\sqrt s\).
If \(s_n/n\to\alpha\in(0,1/2]\), the bounds
\[
\frac{\binom{n-s_n}{k_n}}M\le(1-s_n/n)^{k_n},\qquad
\frac{\binom{s_n}{k_n}}M\le(s_n/n)^{k_n}
\]
show \(p_n(s_n)\to1\); hence \(B_n(s_n)\to[\alpha(1-\alpha)]^{-1/2}\ge2\), with equality only at \(\alpha=1/2\).

**4. Intermediate cuts cannot minimize in the limit.** If \(s_n\to\infty\) and \(s_n/n\to0\), the same probability bounds yield
\[
p_n(s_n)\ge1-e^{-k_ns_n/n}-2^{-k_n}.
\]
Since \(k_n\asymp\sqrt n\), \(2^{-k_n}=o(k_n/n)\), while \(k_ns_n/n\ge k_n/n\). The elementary inequality \(1-e^{-x}\ge(1-e^{-1})\min\{x,1\}\) therefore gives, for all sufficiently large \(n\), a fixed \(\eta>0\) with
\[
 B_n(s_n)\ge\eta\min\left\{
 k_n\sqrt{\frac{s_n}{n-s_n}},\ 
 \frac n{\sqrt{s_n(n-s_n)}}\right\}\longrightarrow\infty.
\]
Every minimizing sequence of cut cardinalities has a subsequence with either fixed size, positive limiting fraction, or this intermediate behavior. The first two cases have limiting lower bounds \(c\) and \(2\), respectively; the third diverges. Since singleton and balanced cuts attain limits \(c\) and \(2\), respectively, the normalized minimum converges to \(\min\{c,2\}\).

**5. Eventual strict minimizer types.** If \(c<2\), a hypothetical sequence of nonsingleton minimizers would, after passage to a subsequence, fall into the three cases just analyzed. A fixed size \(s\ge2\) has limit \(c\sqrt s>c\); positive limiting fraction has limit at least \(2>c\); intermediate size diverges. All contradict the singleton candidate. Therefore singleton cuts are the only minimizers for all sufficiently large \(n\).

If \(c>2\), the same trichotomy forces every sequence of minimizing sizes to satisfy \(s_n/n\to1/2\). It remains to distinguish exact balance from nearby sizes. For every \(s\in[\lceil n/4\rceil,r-1]\),
\[
p_n(s)\ge1-2(3/4)^{k_n},\qquad p_n(r)\le1.
\]
Putting \(t_s=s(n-s)\), integer arithmetic gives \(t_r-t_s\ge1\), \(t_r\le n^2/4\), and therefore \(\sqrt{t_r/t_s}\ge1+1/n^2\) for sufficiently large \(n\). Because \(2(3/4)^{k_n}=o(n^{-2})\),
\[
\frac{B_n(s)}{B_n(r)}
=\frac{p_n(s)}{p_n(r)}\sqrt{\frac{t_r}{t_s}}
\ge\bigl(1-2(3/4)^{k_n}\bigr)\bigl(1+1/n^2\bigr)>1.
\]
Minimizers eventually belong to \(s\ge n/4\), so their only possible cardinality is \(r\). Taking complements gives both balanced cardinalities when \(n\) is odd; the equality classification from Step 2 concludes the proof.

## Verification
The accompanying standalone Python script `verify.py` checks mixed-hyperedge counts by direct enumeration for \(3\le n\le9\), compares each cut normal's width with direct simplex support-function evaluation, and tests randomly selected unit directions against the exact cut formula. It also performs exact-integer squared-width comparisons over 11,172 finite parameter profiles with \(4\le n\le150\) and tests 16 explicit off-critical asymptotic profiles. A finite test is not a proof of the asymptotic statements; all-dimensional validity follows from Steps 1–5 above. The checker has no nonstandard dependencies.

## Relationship to prior work
Agnarsson's 2017 hyper-permutahedra are precisely these fixed-uniformity simplex Minkowski sums; that paper gives their combinatorial face and flag structure. Benedetti, Bergeron, and Machacek (2017 preprint) study hypergraphic face/acyclic-orientation structure. Pešović and Stojadinović (2022) study graph-polytope interpolations by sums of simplices; Cardinal and Steiner (2023) study shortest paths on hypergraphic-polytope one-skeleta. None of these statements is an assertion about intrinsic Euclidean directional width. The present work concerns an exact width functional and a \(k\asymp\sqrt n\) transition, not a new construction of the polytopes or their face structures.

The \(k=2\) endpoint is a graphical zonotope, for which cut-based minimum-width arguments are related to familiar graph total-variation principles. This alone does not yield the uniform-hypergraph mixed-cut counts, the sharp asymptotic constant two, or the eventual singleton/balanced equality classification. As always, absence of a match in the inspected literature does not establish historical uniqueness.

## Limitations
The result makes no claim of an exact finite-parameter proof that the minimizer cardinality must always be either one or balanced; the exact finite formula retains a minimization over all \(1\le s\le\lfloor n/2\rfloor\). The exhaustive numerical profiles are not used to assert such a universal endpoint theorem. The critical scaling \(k_n/\sqrt n\to2\) is settled only at the level of the limiting normalized width, not the eventual contact orbit. The Euclidean metric is unweighted. Historical priority may be affected by earlier general results on widths of permutohedra under alternative terminology.

## References
1. G. Agnarsson, “On a Special Class of Hyper-Permutahedra,” *Electronic Journal of Combinatorics* **24** (2017), P3.46, published 2017-09-08. DOI: 10.37236/6652. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p46/pdf/ .
2. C. Benedetti, N. Bergeron, and J. Machacek, “Hypergraphic polytopes: combinatorial properties and antipode,” arXiv:1712.08848 (first public preprint 2017-12-23), later *Journal of Combinatorics* 10 (2019), 515–544. https://arxiv.org/abs/1712.08848 .
3. M. Pešović and T. Stojadinović, “Between graphical zonotope and graph-associahedron,” arXiv:2209.12053 (first public 2022-09-24). https://arxiv.org/html/2209.12053v1 .
4. J. Cardinal and R. Steiner, “Shortest paths on polymatroids and hypergraphic polytopes,” arXiv:2311.00779 (first public 2023-11-01). https://arxiv.org/abs/2311.00779 .
