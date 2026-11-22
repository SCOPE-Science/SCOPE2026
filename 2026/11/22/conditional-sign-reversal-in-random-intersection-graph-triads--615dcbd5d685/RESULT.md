# Conditional sign reversal in random intersection graph triads

## Finding

Let \(n\ge3\), \(m\ge1\), and \(0<p_j<1\) for \(1\le j\le m\). Independently for each vertex and each attribute \(j\), include that attribute at the vertex with probability \(p_j\). Join two vertices when they share at least one attribute. For three distinct labelled vertices, let \(X\), \(Y\), and \(Z\) indicate the edges on the three respective pairs, with \(X\) being the edge between the endpoints of \(Y\) and \(Z\) that are not shared by those two edges.

Then the *same* two adjacent-edge indicators have three rigorously different dependence signs:

\[
\operatorname{Cov}(Y,Z)>0,\qquad
\operatorname{Cov}(Y,Z\mid X=0)<0,\qquad
\operatorname{Cov}(Y,Z\mid X=1)>0.
\]

The inequalities hold for every finite \(m\) and every choice of attribute-specific probabilities. They are strict without asymptotic qualifications. The entire graph-edge measure is positively associated, but it is not multivariate totally positive of order two (MTP2) for any \(n\ge3\). The two strict conditional signs persist after an arbitrary positive edge-activity tilt of the three-edge marginal law. No equivalent assertion about conditional signs after tilting *all* edges of a larger graph is made.

In particular, for one attribute of membership probability \(1/2\), the unconditional covariance is \(1/16\), while the conditional covariances given absence and presence of the third edge are \(-1/36\) and \(1/4\), respectively.

## Assumptions and scope

All membership indicators for different vertex–attribute pairs are mutually independent. The probabilities may depend on the attribute index but are identical across vertices for a fixed attribute. The graph is simple and labelled. For a selected triple define

\[
\begin{aligned}
a_j&=1-3p_j^2+2p_j^3,\\
u_j&=1-2p_j^2+p_j^3,\\
v_j&=1-p_j^2,\\
A&=\prod_{j=1}^{m}a_j,\qquad
B=\prod_{j=1}^{m}u_j,\qquad
C=\prod_{j=1}^{m}v_j.
\end{aligned}
\]

For a specified labelled three-vertex edge configuration with exactly \(k\) present edges, the probability equals the corresponding entry of

\[
(P_0,P_1,P_2,P_3)
=(A,\ B-A,\ C-2B+A,\ 1-3C+3B-A).
\]

Each \(P_k\) is the probability of *one specified* edge set of size \(k\), not the probability of having any \(k\) edges; the latter is \(\binom3kP_k\). In particular, \(P_2\) can equal zero when \(m=1\).

## Proof

For one attribute, the induced three-edge configuration is empty with probability \(a_j\), is any one specified single edge with probability \(b_j=p_j^2(1-p_j)\), and is the whole triangle with probability \(p_j^3\); a two-edge configuration cannot arise from one attribute. The final graph is the union over attributes. The probabilities that respectively none of three specified edges, none of two specified edges, and none of one specified edge occurs are \(A\), \(B\), and \(C\). Inclusion–exclusion therefore gives the complete four-value mass function above.

For two Bernoulli edge indicators, covariance is the difference between their joint zero probability and the product of their zero probabilities. Substituting the mass function gives the exact identities

\[
\begin{aligned}
\operatorname{Cov}(Y,Z)&=B-C^2,\\
\operatorname{Cov}(Y,Z\mid X=0)&=\frac{AC-B^2}{C^2},\\
\operatorname{Cov}(Y,Z\mid X=1)&=
\frac{(B-A)(1-C)-(C-B)^2}{(1-C)^2}.
\end{aligned}
\]

Both conditioning events have strictly positive probability because \(0<C<1\). Two elementary strict identities valid for every \(0<p_j<1\) are

\[
u_j^2-a_jv_j=p_j^4(1-p_j)^2>0,
\qquad u_j-v_j^2=p_j^3(1-p_j)>0.
\]

Multiplication over attributes yields \(B^2>AC\) and \(B>C^2\). These establish respectively the negative conditional sign when \(X=0\) and the positive unconditional sign. To prove the remaining strict sign, observe \(0<A<B<C<1\) and set \(r=B/C\). From \(B^2>AC\) and \(B>C^2\) it follows that \(A/B<r\) and \(C<r\). Hence

\[
(B-A)(1-C) > B(1-r)^2,
\qquad (C-B)^2=C^2(1-r)^2,
\]

so the difference in the last conditional covariance numerator is strictly larger than \((B-C^2)(1-r)^2>0\). This completes the sign classification.

The edge vector is a coordinatewise increasing function of the independent membership bits. Harris's product-measure inequality therefore gives nonnegative covariance for every two increasing functions of the complete edge vector: positive association. On the other hand, in the three-edge law, the FKG lattice determinant for the two distinct singleton-edge configurations is

\[
P_0P_2-P_1^2=AC-B^2<0.
\]

Thus this three-edge law is not MTP2. Since MTP2 is preserved under marginalization (Karlin–Rinott), the complete edge vector for any \(n\ge3\) cannot be MTP2 either. For a positive tilt assigning weight \(w_e>0\) to each present edge of the selected triple, both conditional two-by-two determinants are multiplied by strictly positive factors; their signs therefore remain unchanged. This tilt statement concerns exactly the three-edge marginal distribution.

## Verification

The standalone `verify.py` independently enumerates all eight membership patterns for each attribute, convolves their labelled edge-set laws under graph union, and compares every one of the eight final edge-set probabilities with the formula. Fractions are exact. It checks all heterogeneous sequences of lengths one to four from the five distinct probabilities \(1/5,1/3,1/2,2/3,4/5\), totaling 780 sequences; it verifies normalization, all three covariance signs, and the displayed one-attribute example. Run `python3 verify.py` in a directory containing the embedded file. The enumeration checks only these finite cases; the universal quantified theorem is established by the preceding algebra.

## Relationship to prior work

Deijfen and Kets study degree distributions and clustering of attribute-intersection graphs; their Section 3 analyzes triangle events and asymptotic conditional edge probabilities in a related weighted model. Bloznelis studies local clustering versus degree in sparse intersection graphs. Zhao, Yağan and Gligor analyze connectivity and minimum degree in binomial and uniform intersection graphs. These works motivate the finite three-edge law but do not in their inspected theorem statements establish the stated universal *finite-size* sign reversal, especially for distinct attribute-specific probabilities. The association and MTP2-marginalization principles themselves are classical and are not claimed as new.

## Limitations

The membership probabilities must be the same across vertices for each attribute; allowing arbitrary vertex-dependent probabilities is not proved. A random number of attributes, fixed-size item sets at each vertex, thresholds requiring several shared attributes, or conditioning on additional edges may have different dependence signs. The result concerns conditional pairwise covariance and MTP2, not a complete classification of higher-order conditional association. Literature priority is qualified by the possibility of earlier equivalent formulations of the three-vertex graph law. No independent mathematical audit has been performed.

## References

- M. Deijfen and W. Kets, *Random intersection graphs with tunable degree distribution and clustering*, Probability in the Engineering and Informational Sciences (first available online 14 July 2009), DOI: 10.1017/S0269964809990064; full text available at https://arxiv.org/abs/1509.07019 .
- M. Bloznelis, *Degree and clustering coefficient in sparse random intersection graphs*, arXiv:1303.3388 (first posted 14 March 2013), DOI: 10.1214/12-AAP874.
- J. Zhao, O. Yağan and V. Gligor, *On k-connectivity and minimum vertex degree in random s-intersection graphs*, arXiv:1409.6021 (first posted 21 September 2014).
- S. Karlin and Y. Rinott, *Classes of orderings of measures and related correlation inequalities. I. Multivariate totally positive distributions*, Journal of Multivariate Analysis 10 (1980), 467–498, DOI: 10.1016/0047-259X(80)90065-2.
