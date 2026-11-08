# Sharp rare failure of uniform-edge greedy matching on crown graphs

## Finding

Let \(C_n=K_{n,n}\setminus\{(i,i):1\le i\le n\}\), with the two vertex classes separately labelled \(1,\ldots,n\). Beginning with \(C_n\), repeatedly choose one of the **remaining edges uniformly**, add it to a matching, and delete both endpoints and their incident edges. Denote by \(p_n\) the probability that the resulting maximal matching is not perfect. For every integer \(n\ge2\):

1. The output has either \(n\) or \(n-1\) edges. Its failure probability is given exactly by the finite recurrence in the Proof below.
2. \(p_2=0\), and for every \(n\ge3\), \(0<p_n<2/(n+1)\).
3. As \(n\to\infty\),
   \[
   p_n=\frac{2}{n+1}-\frac{4\log n}{n(n-1)}+O(n^{-2}).
   \]
   Equivalently, \(np_n\to2\) and
   \[
   \lim_{n\to\infty}\frac{n(n-1)}{\log n}
   \left(\frac{2}{n+1}-p_n\right)=4.
   \]

Here the implicit \(O\)-constant is absolute. In particular, the algorithm succeeds with probability \(1-2/n+O((\log n)/n^2)\), although a perfect matching is always available in \(C_n\).

## Assumptions and scope

The graph is fixed and simple, not an independently sampled graph. Randomness enters only through the successive uniform choices of **edges**, not vertices or endpoints. Labels on the two sides are matched in the deleted diagonal. No edge reappears after an endpoint is removed. Logarithms are natural. The asymptotic assertions concern integers \(n\to\infty\); the exact recurrence covers all integers \(n\ge2\).

## Proof

**State reduction and exact recurrence.** At a stage with \(m\) unmatched vertices on each side, write \(L,R\) for the two remaining sets of labels and \(r=|L\cap R|\). There are \(m^2-r\) permitted edges. Choosing an edge removes one left label \(i\) and one right label \(j\), necessarily \(i\ne j\). The number of permitted edges that remove respectively zero, one, or two labels from \(L\cap R\) is
\[
(m-r)^2,\qquad 2r(m-r),\qquad r(r-1).
\]
Thus, writing \(F_m(r)\) for failure probability from this state, set \(F_1(0)=0\), \(F_1(1)=1\), and for \(m\ge2\), \(0\le r\le m\),
\[
 F_m(r)=\frac{(m-r)^2F_{m-1}(r)+2r(m-r)F_{m-1}(r-1)+r(r-1)F_{m-1}(r-2)}{m^2-r},
\]
where terms of zero coefficient are omitted. Then \(p_n=F_n(n)\). If \(m\ge2\), the current graph has at least \(m(m-1)>0\) edges, so termination can occur only at \(m=1\); there it occurs exactly when \(r=1\). This also proves the two possible output sizes. Explicitly, \(p_2=0\), \(p_3=1/3\), \(p_4=p_5=4/21\).

**A telescoping tagged-label identity.** Let \(R_m\) be the random overlap when \(m\) vertices remain on each side, so \(R_n=n\) and \(p_n=\Pr(R_1=1)=\mathbb E R_1\). From the transition counts,
\[
 \mathbb E[R_{m-1}\mid R_m=r]
 =r\frac{m-1}{m+1}-\frac{2r(r-1)}{(m+1)(m^2-r)}.
\]
Dividing by \(m(m-1)\) and taking expectations gives the exact finite identity
\[
 \frac1{n+1}-\frac{p_n}{2}
 =\sum_{m=2}^n\frac{2}{m(m-1)(m+1)}
 \mathbb E\!\left[\frac{R_m(R_m-1)}{m^2-R_m}\right].\tag{1}
\]
Every summand is nonnegative. For \(n\ge3\), the initial term with \(m=n\) is positive. Thus \(p_n<2/(n+1)\). Positivity for \(n\ge3\) follows by choosing a sequence of non-diagonal edges leaving a common final label; such a sequence has strictly positive probability: choose a derangement matching on any \(n-1\ge2\) labels, selecting those edges one at a time and leaving the last label untouched.

**A two-label survival estimate.** Fix two distinct labels \(u,v\). Condition on both labels remaining on both sides at size \(m\), necessarily with \(R_m=r\ge2\). They both remain common after one step with probability
\[
 Q_m(r)=\frac{(m-2)^2-(r-2)}{m^2-r}.
\]
This expression decreases with \(r\). For every \(m\ge4\),
\[
 \left(\frac{m-2}{m}\right)^2
 \left(1-\frac{2}{(m-1)(m-2)}\right)
 \le Q_m(r)\le
 \left(\frac{m-2}{m}\right)^2\left(1-\frac2{m^2}\right)^{-1}.
\]
The first correction factors telescope:
\[
 \prod_{j=m+1}^n\left(1-\frac2{(j-1)(j-2)}\right)
 =\frac{n(m-2)}{m(n-2)}.
\]
The product of the second correction factors is at most
\(\exp(16/(7m))\) for \(m\ge3\), using \(-\log(1-x)\le x/(1-x)\) and comparison of \(\sum_{j>m}j^{-2}\) with an integral. Since
\[
 \prod_{j=m+1}^n\left(\frac{j-2}{j}\right)^2
 =\left(\frac{m(m-1)}{n(n-1)}\right)^2,
\]
exchangeability over ordered label pairs implies, uniformly for \(3\le m\le n\),
\[
 \mathbb E[R_m(R_m-1)]
 =\frac{m^2(m-1)^2}{n(n-1)}\left(1+O(m^{-1})\right).\tag{2}
\]
For \(m=2\), the same upper comparison including the step \(j=3\) gives \(\mathbb E[R_2(R_2-1)]=O(n^{-2})\), because the infinite product \(\prod_{j\ge3}(1-2/j^2)^{-1}\) converges. All constants are uniform in \(m,n\).

**The logarithmic correction.** Since \(0\le R_m\le m\), the reciprocal \(1/(m^2-R_m)\) equals \(m^{-2}(1+O(m^{-1}))\), uniformly for \(m\ge3\). Combining this with (2), the summand on the right side of (1) is
\[
 \frac{2}{n(n-1)}\frac{m-1}{m(m+1)}\left(1+O(m^{-1})\right).
\]
The \(m=2\) summand is \(O(n^{-2})\), while
\[
 \sum_{m=3}^n\frac{m-1}{m(m+1)}=\log n+O(1),
 \qquad
 \sum_{m=3}^\infty\frac{m-1}{m^2(m+1)}<\infty.
\]
Consequently (1) becomes
\[
 \frac1{n+1}-\frac{p_n}{2}
 =\frac{2\log n}{n(n-1)}+O(n^{-2}),
\]
which is the stated expansion.

## Verification

The companion `check.py` independently evaluates the state recurrence and a labelled-subset recursion selecting actual available edges. They agree by exact rational arithmetic for \(2\le n\le6\). An independent forward-state computation reproduces the martingale telescoping identity at these sizes. Additional exact recurrence values at larger orders are reported as numerical illustrations of the asymptotic ratio; finite calculations are not used to prove the limit. Execute `python3 check.py` in the directory containing this file.

## Relationship to prior work

Dyer and Frieze introduced the edge-uniform randomized greedy matching problem for fixed graphs (1991). Gamarnik and Goldberg, arXiv:0807.1277 (first posted 2008-07-08), derive bounds for greedy matchings in regular graphs subject to girth constraints; their Theorem 5 bounds expected matching size rather than the exact rare failure probability of this high-degree crown-graph sequence. Mastin and Jaillet, arXiv:1307.2536 (2013), study online vertex-arrival matching in random bipartite graphs rather than sequential uniform-edge selection on a fixed graph; their Theorems 3–4 concern expected relative size in that online model. The claims here concern the exact two-state overlap transition and the coefficient of its logarithmic rare-failure correction. There may be implicit coverage in early randomized-greedy-matching literature, including sources whose complete texts were inaccessible; no priority claim beyond the comparisons actually made is asserted.

## Limitations

The result is specific to the perfect-matching deletion \(K_{n,n}\setminus M_n\) and uniform edge selection; it does not address other greedy variants, random input graphs, or nonuniform edge weights. The expansion controls the first logarithmic correction but does not identify the constant in the remaining order-\(n^{-2}\) term. Earlier general studies may implicitly subsume the finding; independent literature review has not been performed.

## References

1. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45, DOI: 10.1002/rsa.3240020104. [Original model; publisher abstract accessible, complete text not inspected.]
2. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277, first version 2008-07-08, https://arxiv.org/abs/0807.1277. [Theorem 5 and accompanying hypotheses inspected in the full paper.]
3. A. Mastin and P. Jaillet, *Greedy Online Bipartite Matching on Random Graphs*, arXiv:1307.2536, first version 2013-07-09, https://arxiv.org/abs/1307.2536. [Model definition and main theorem statements inspected in the full paper.]
