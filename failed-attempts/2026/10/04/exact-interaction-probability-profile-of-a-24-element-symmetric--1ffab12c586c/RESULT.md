# Exact interaction-probability profile of a 24-element symmetric skew brace
## Finding
Let \(V=\mathbb F_2^2\), let \(H=\operatorname{GL}_2(\mathbb F_2)\cong S_3\), and let \(B=V\times H\) carry the symmetric skew-brace operations
\[
(u,h)+(v,g)=(u+v,hg),\qquad
(u,h)\circ(v,g)=(u+h^{-1}v,hg).
\]
This is the symmetric skew brace of Example 6.12 in arXiv:2609.16269. Its exact global interaction-probability profile is
\[
\operatorname{Pb}(B)=\frac16,\qquad
P_{\lambda}(B)=\frac7{24},\qquad
P_t(B)=\frac5{48}.
\]
The two underlying group commuting probabilities are
\[
\operatorname{Pr}(B,+)=\frac12,\qquad
\operatorname{Pr}(B,\circ)=\frac5{24},
\]
so the five quantities are strictly ordered by
\[
P_t(B)<\operatorname{Pb}(B)<\operatorname{Pr}(B,\circ)<P_{\lambda}(B)<\operatorname{Pr}(B,+).
\]
The same published example uses Sylow sub-skew braces \(P\) and \(Q\) with \(\operatorname{Pb}(P,Q)=5/12\). Hence
\[
\operatorname{Pb}(P,Q)=\frac52\operatorname{Pb}(B),
\]
which gives an exact local-to-global separation inside the paper's counterexample.

## Assumptions and scope
For a skew brace, write \(a*b=\lambda_a(b)-b\). Here \(P_{\lambda}(B)\) is the probability that \(a*b=1\), and \(P_t(B)\) is the probability that two sampled elements generate a trivial sub-skew brace. The source's Lemma 5.1 characterizes the latter by
\[
a*a=a*b=b*a=b*b=1.
\]
The brace commuting probability \(\operatorname{Pb}(B)\) is the probability that the sampled pair brace-commutes. The claim concerns only the explicit order-\(24\) symmetric skew brace above; it is not a classification of symmetric skew braces or a new threshold theorem.

## Proof
For \(h\in H\), put \(F(h)=|\operatorname{Fix}_V(h)|\). The six elements of \(H\cong S_3\) split into the identity, three involutions, and two elements of order \(3\). Their fixed-space sizes on \(V\) are respectively
\[
4,\quad 2,\quad 1,
\]
and their centralizer sizes in \(H\) are respectively
\[
6,\quad 2,\quad 3.
\]

Take \(a=(u,h)\) and \(b=(v,g)\). From the displayed operations and the source's formula
\[
\lambda_{(u,h)}(v,g)=(h^{-1}v,h^{-1}gh),
\]
one obtains the following exact conditions.

First, \(a\) and \(b\) brace-commute exactly when \(hg=gh\), \(h(v)=v\), and \(g(u)=u\). Therefore the number of ordered brace-commuting pairs is
\[
\sum_{hg=gh}F(h)F(g).
\]
For \(h=1\), the contribution is \(4(4+3\cdot2+2\cdot1)=48\). For the three involutions the total contribution is \(3\cdot2(4+2)=36\). For the two elements of order \(3\) it is \(2\cdot1(4+1+1)=12\). Thus there are \(96\) brace-commuting ordered pairs, and
\[
\operatorname{Pb}(B)=\frac{96}{24^2}=\frac16.
\]

Second, \(a*b=1\) exactly when \(hg=gh\) and \(h(v)=v\), with \(u\) arbitrary. Hence the number of ordered pairs counted by \(P_{\lambda}(B)\) is
\[
4\sum_{h\in H}F(h)|C_H(h)|
=4(4\cdot6+3\cdot2\cdot2+2\cdot1\cdot3)=168,
\]
so
\[
P_{\lambda}(B)=\frac{168}{24^2}=\frac7{24}.
\]

Third, by Lemma 5.1, the pair is counted by \(P_t(B)\) exactly when \(hg=gh\) and both \(u\) and \(v\) are fixed by both \(h\) and \(g\). Thus the count is
\[
\sum_{hg=gh}|\operatorname{Fix}_V(h)\cap\operatorname{Fix}_V(g)|^2.
\]
The identity row contributes \(4^2+3\cdot2^2+2\cdot1^2=30\). Each involution commutes only with the identity and itself, contributing \(2^2+2^2=8\), for a total of \(24\). Each order-\(3\) element commutes with the identity and the two order-\(3\) elements, and the common fixed space has size \(1\), giving \(3\) each and \(6\) total. Therefore the count is \(60\), and
\[
P_t(B)=\frac{60}{24^2}=\frac5{48}.
\]

Finally, \((B,+)\cong C_2^2\times S_3\), so its commuting probability is \(3/6=1/2\). The source identifies \((B,\circ)\cong V\rtimes H\cong S_4\), whose five conjugacy classes give commuting probability \(5/24\). The source itself computes \(\operatorname{Pb}(P,Q)=5/12\) for the Sylow pair in Example 6.12, so the ratio to the newly computed global value is \(5/2\).

## Verification
A standalone exhaustive checker reconstructs all six matrices in \(\operatorname{GL}_2(\mathbb F_2)\), all \(24\) brace elements, and all \(576\) ordered pairs directly from the two operations. It obtains counts
\[
96,\ 168,\ 60,\ 288,\ 120
\]
for brace commuting, the \(P_{\lambda}\) condition, the \(P_t\) condition, additive commuting, and multiplicative commuting, respectively. These reduce to the five probabilities stated above. The checker ends with `CHECK_OK`.

## Relationship to prior work
Mondal, Shumyatsky, Trombetti, and Yadav introduce the relative and auxiliary probabilities used here and, in Example 6.12, construct this exact symmetric skew brace to show that an additive derived subgroup need not be an ideal even when the Sylow-local commuting probability exceeds \(2/5\). Their full-text calculation gives \(\operatorname{Pb}(P,Q)=5/12\) for a Sylow pair but does not state the three global values \(1/6\), \(7/24\), and \(5/48\).

The earlier paper of Mondal and Yadav develops the global brace commuting probability and its general bounds. It does not contain this later order-\(24\) symmetric example or the probability profile above. Targeted searches for the exact fractions together with skew-brace terminology, for the \(V=\mathbb F_2^2\), \(H=\operatorname{GL}_2(\mathbb F_2)\) construction, and for equivalent interaction-probability formulations did not locate a prior statement of the profile.

## Limitations
The result is an exact invariant calculation for one structurally motivated example. It does not determine the possible triples \((P_t,P_{\lambda},\operatorname{Pb})\) for all finite skew braces, and it does not imply a general relation between Sylow-local and global brace commuting probabilities beyond this example. Older computational brace tables could encode the same values without presenting them as a theorem; no such statement was located in the inspected sources.

## References
1. S. Mondal, P. Shumyatsky, M. Trombetti, M. K. Yadav, *Relative commuting probability and BFC-type results for finite skew braces*, arXiv:2609.16269v1, 2026.
2. S. Mondal, M. K. Yadav, *Commuting probability of skew left braces*, arXiv:2603.16771v1, 2026.
