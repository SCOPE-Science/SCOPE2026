# A strongly Rayleigh retention law for marked cherries in homogeneous rooted tree types

## Finding

Fix an individually named finite induced base \(A\) in the countable homogeneous binary-branching \(C\)-relation, with \(n\ge2\) leaves. Its rooted binary tree has \(c\) cherries, namely pairs of leaves sharing a parent. For each \(r\ge0\), choose uniformly among the complete types of ordered injective \(r\)-tuples disjoint from \(A\). A cherry *survives* if its two old leaves are still siblings after adjoining the new leaves.

Write \(a=n-\tfrac32\) and define the falling factorial \(u_{\underline k}=\prod_{i=0}^{k-1}(u-i)\), with \(u_{\underline0}=1\). For every subset \(S\) of the \(c\) original cherries, the probability that **exactly** the cherries of \(S\) survive is

\[
\boxed{\Pr(\text{survivor set}=S)=\frac{a_{\underline{|S|}}\,r_{\underline{c-|S|}}}{(a+r)_{\underline c}}.}
\]

In particular, the entire joint law is independent of the old tree shape except for \(n\) and \(c\), and is exchangeable over the original cherries. The survival-count generating polynomial has only real nonpositive roots; more strongly, the full survivor-indicator law is **strongly Rayleigh** and therefore negatively associated. For distinct original cherries and \(r\ge1\), their indicators have strictly negative covariance

\[
\boxed{-\frac{4r(2n-3)}{(2n+2r-3)^2(2n+2r-5)}}.
\]

For example, if \(n=4\), \(c=2\), and \(r=2\), the probabilities of retaining respectively zero, one and two original cherries are \(8/63\), \(40/63\), and \(5/21\). When \(c\) is fixed and \(r\to\infty\), the probability that at least one original cherry remains is

\[
\frac{c(2n-3)}{2n+2r-3}+O_{n,c}(r^{-2}).
\]

## Assumptions and scope

The finite leaf structures are represented by rooted, non-plane, fully binary trees with distinctly labelled leaves. The ternary relation \(C(z,xy)\) is true exactly when the youngest common ancestor of \(x,y\) lies strictly below that of \(x,y,z\); see Bodirsky–Jonsson–Pham. A complete injective ordered tuple type over the individually named base is equivalent, by the homogeneity of this relational structure, to a uniquely determined labelled rooted binary extension tree on the old and new leaves whose restriction to the old leaves is the given tree. Distinct new coordinates are never identified with one another or with old leaves. No random selection of vertices of the infinite structure is used; the probability space is the finite set of logical types, with equal weights.

Every \(n\)-leaf rooted binary tree has \(2n-1\) possible insertion positions when its root stem is included. Its number \(c\) of cherries satisfies \(1\le c\le\lfloor n/2\rfloor\), so all displayed falling factorial denominators are positive. For \(r=0\), all original cherries survive deterministically.

## Proof

**1. Uniform extension by successive grafting.** Each new labelled leaf is inserted by subdividing one ordinary edge, or the root stem, and adjoining the leaf as a second child of the new subdivision node. Deleting the most recently added leaf and suppressing its parent uniquely recovers the preceding tree and its chosen insertion edge. Thus there is no overcounting: for \(r\) ordered new leaf labels the number of complete extension types is exactly

\[
N_{n,r}=\prod_{i=0}^{r-1}(2n+2i-1).
\]

Choosing uniformly among the available \(2n+2i-1\) edges at stage \(i\) consequently yields the uniform distribution on final types.

**2. An exchangeable pure-death process.** Each surviving original cherry has exactly two pendant edges, one incident to each of its two original leaves. Grafting onto either edge destroys that cherry; grafting anywhere else leaves it intact. Once destroyed it cannot reappear by further grafting. These two-edge sets are pairwise disjoint for distinct original cherries. Therefore, conditional on a survivor set of size \(s\), each of its members is destroyed at the next step with probability \(2/(2n+2i-1)\), and no more than one is destroyed in a step. This transition law does not use the remaining topology.

**3. Joint inclusion probabilities and exact law.** For any fixed set of \(j\) original cherries, the probability that all survive after \(r\) graftings is

\[
 p_j=\prod_{i=0}^{r-1}\left(1-\frac{2j}{2n+2i-1}\right)
     =\frac{a_{\underline j}}{(a+r)_{\underline j}}.
\]

The equality follows by cancelling the two-step-spaced factors. The survival law is exchangeable by the transition rule. The proposed probability for any exact survivor set \(S\) has the preceding joint inclusion probabilities: for fixed \(J\) of size \(j\), summing over supersets \(S\supseteq J\) gives

\[
\frac{a_{\underline j}}{(a+r)_{\underline c}}
\sum_{k=0}^{c-j}\binom{c-j}{k}
 (a-j)_{\underline k}\,r_{\underline{c-j-k}}
=\frac{a_{\underline j}}{(a+r)_{\underline j}},
\]

by the falling-factorial Vandermonde identity. Joint inclusion probabilities uniquely determine the distribution of a finite subset by inclusion–exclusion. This proves the formula. In particular the number \(R\) of survivors has

\[
\Pr(R=s)=\binom cs\frac{a_{\underline s}\,r_{\underline{c-s}}}{(a+r)_{\underline c}},
\qquad 0\le s\le c,
\]

and \(\mathbb E[(R)_{\underline j}]=(c)_{\underline j}a_{\underline j}/(a+r)_{\underline j}\).

**4. All roots are real and nonpositive.** Let \(F_i(z)=\mathbb E[z^{R_i}]\) after \(i\) insertions. By the pure-death transition,

\[
F_0(z)=z^c,\qquad
F_{i+1}(z)=F_i(z)+\alpha_i(1-z)F_i'(z),
\qquad \alpha_i=\frac{2}{2n+2i-1}.
\]

Since \(c\le n/2\), we have \(0<\alpha_i c<1\). Suppose that \(f\) is a positive-leading degree-\(c\) polynomial with all roots real and nonpositive. If its roots \(x_1<\cdots<x_c\) are simple, the values of \(f+\alpha(1-z)f'\) at those roots alternate in sign, because \(1-x_i>0\). Its leading coefficient is positive when \(\alpha c<1\). Consequently one root lies to the left of \(x_1\), and one lies in each interval \((x_i,x_{i+1})\). Thus all \(c\) roots remain real and nonpositive. Multiple-root cases follow by continuity from a sequence of distinct negative roots. Induction from \(F_0=z^c\) proves the assertion.

The multiaffine generating polynomial of the survivor indicators is symmetric and has diagonal specialization \(F_r(z)\). It is exactly the polarization of \(F_r\). By the Grace–Walsh–Szegő polarization preservation theorem (as in Borcea–Brändén–Liggett, Corollary 4.7), it is real stable. Nonnegative coefficients and normalization make this a strongly Rayleigh probability measure. Its negative association is a standard consequence of that established theorem; no new general stability theorem is claimed.

**5. Covariance and large-extension limit.** With \(A_0=2n-3\) and \(B_0=2n+2r-3\), inclusion probabilities give \(p_1=A_0/B_0\) and \(p_2=A_0(A_0-2)/(B_0(B_0-2))\). Therefore, for two distinct original cherries,

\[
\operatorname{Cov}(I_1,I_2)=p_2-p_1^2
=-\frac{4rA_0}{B_0^2(B_0-2)}<0
\]

when \(r\ge1\). Finally \(p_j=O_{n,j}(r^{-j})\) for fixed \(n,j\), so inclusion–exclusion gives \(\Pr(R\ge1)=cp_1+O_{n,c}(r^{-2})\).

## Verification

The standalone `verify.py` uses only the Python standard library. It checks 980 exact fractional probability/Markov/moment cases for \(2\le n\le18\), \(0\le c\le\lfloor n/2\rfloor\), \(0\le r\le9\). Separately, it constructs and enumerates all labelled tree extensions by independent canonicalized edge grafting for 25 finite cases across balanced and caterpillar old trees, comparing the observed laws with the theorem. The command is `python verify.py`; expected final output is `ALL_MARKED_CHERRY_EXTENSION_CHECKS_OK`. These finite checks are corroboration, not a substitute for the proof for arbitrary \(n,r\).

## Relationship to prior work

Bodirsky, Jonsson and Pham describe the homogeneous binary-branching \(C\)-relation and its finite rooted leaf structures. McKenzie and Steel, and Wu and Choi, establish foundational PDA leaf-grafting and *global* cherry/pitchfork-count distributions. Their studied variables count all cherries in the evolving tree, rather than the survival vector of specifically marked original cherries over an individually named finite base. Borcea, Brändén and Liggett supply the general strongly Rayleigh and polarization theory used in Step 4. The new application is the exact finite conditional law, its topology independence, and the resulting multivariate negative-dependence structure. The known general results and counting identities are not claimed as new.

## Limitations

The model is uniform over complete types or, equivalently, over rooted PDA extensions with a fixed order of new labels; the result does not apply unchanged to the Yule–Harding model, plane trees, unresolved polytomies, arbitrary rooted relations, or random vertices of the countably infinite structure. The full probability law is conditional on a fixed old tree, not a distribution over random old trees. Historical coverage by an earlier equivalent tagged-cherry formula cannot be ruled out conclusively; independent review has not been performed.

## References

- M. Bodirsky, P. Jonsson, T. V. Pham, *The Reducts of the Homogeneous Binary Branching C-relation*, arXiv:1408.2554 (initial posting 2014-08-11), especially Section 3.2. https://arxiv.org/abs/1408.2554
- A. McKenzie, M. Steel, *Distributions of Cherries for Two Models of Trees*, Mathematical Biosciences 164 (2000), 81–92, especially Sections 2 and 4. https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/cherry.pdf
- T. Wu, K. P. Choi, *On Joint Subtree Distributions under Two Evolutionary Models*, arXiv:1508.03139 (initial posting 2015-08-13), especially Sections 2 and 4. https://arxiv.org/abs/1508.03139
- J. Borcea, P. Brändén, T. M. Liggett, *Negative Dependence and the Geometry of Polynomials*, arXiv:0707.2340 (initial posting 2007-07-16), especially Corollary 4.7 and Section 4.2. https://arxiv.org/abs/0707.2340
- K. P. Choi, G. Kaur, T. Wu, *On Asymptotic Joint Distributions of Cherries and Pitchforks for Random Phylogenetic Trees*, Journal of Mathematical Biology 83 (2021), Article 40, especially Section 5. https://doi.org/10.1007/s00285-021-01667-2
