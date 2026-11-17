# Degree-parity universality and three sign reversals for induced motifs in independent-edge random graphs

## Finding
Let \(G\sim G(n,p)\), with integer \(n\ge k\ge2\) and real \(0<p<1\). For any fixed unlabelled simple graph \(H\) on \(k\) vertices, let \(T_H\) be the number of \(k\)-element vertex subsets inducing a graph isomorphic to \(H\), and let \(O\) be the total number of vertices of odd degree in \(G\). Denote by \(o(H)\) the number of odd-degree vertices of \(H\), by \(e(H)\) its number of edges, and set \(q=1-2p\). Then

\[
\boxed{\operatorname{Cov}(T_H,O)=-\frac{\mathbb E T_H}{2}q^{n-k}\bigl[k-2o(H)-kq^{k-1}\bigr],}
\]

where

\[
\mathbb E T_H=\binom nk\frac{k!}{|\operatorname{Aut}(H)|}p^{e(H)}(1-p)^{\binom{k}{2}-e(H)}.
\]

Consequently the normalized covariance \(\operatorname{Cov}(T_H,O)/\mathbb E T_H\) depends on \(H\) only through its order \(k\) and its odd-degree count \(o(H)\), not through its edge count or isomorphism type otherwise. This remains exact for disconnected and connected motifs alike.

**A sharp three-reversal family.** Let \(H=P_5\), the path on five vertices, and let \(n\ge6\) be even. The covariance has precisely three zeros in \(0<p<1\), all of which are strict sign changes:

\[
p_{-}=\frac{1-5^{-1/4}}{2},\qquad \frac12,\qquad p_{+}=\frac{1+5^{-1/4}}{2}.
\]

Its successive signs, as \(p\) increases from zero to one, are \(+,-,+,-\). All three crossings persist for every even \(n\ge6\). More generally, when \(k\) is odd, \(0<o(H)<k/2\), and \(n-k\) is odd, the same three-crossing pattern follows with \(5^{-1/4}\) replaced by \((1-2o(H)/k)^{1/(k-1)}\).

## Assumptions and scope
The underlying graph is an undirected, simple labelled Erdős–Rényi graph: every unordered pair is an edge independently with common probability \(p\in(0,1)\). The motif \(H\) is deterministic, has \(k\ge2\) vertices, and need not be connected. Counts are over *unlabelled vertex subsets*, rather than embeddings. \(O\) uses full-graph degrees, not degrees internal to the induced subset. All parameters \(n,k,p\) are finite. At \(n=k\) the factor \(q^{n-k}\) is defined to be \(1\), including when \(q=0\).

For the general formula, the parity factor has no ambiguity because \(o(H)\) is even by the handshaking lemma. The precise three-reversal corollary requires \(n-k\) odd (in particular, \(n\) even when \(k=5\)); for the opposite parity the central zero can be tangential instead.

## Proof
For a fixed \(k\)-subset \(S\) of vertices, write \(A_S\) for the event that \(G[S]\) is isomorphic to \(H\). For each vertex \(v\), introduce its degree-parity character \(Z_v=(-1)^{\deg_G(v)}\), so the odd-degree indicator is \((1-Z_v)/2\). Each incident edge contributes an independent sign whose expectation is \(q=1-2p\), hence \(\mathbb E Z_v=q^{n-1}\) and \(\mathbb E O=n(1-q^{n-1})/2\).

Conditional on \(A_S\), the \(k(n-k)\) edges between \(S\) and its complement, together with all other edges not internal to \(S\), retain their original independent Bernoulli laws. For \(v\in S\), the induced degree \(\deg_{G[S]}(v)\) depends on the particular copy of \(H\), but the *sum* of its parity signs over \(S\) is always

\[
\sum_{v\in S}(-1)^{\deg_{G[S]}(v)}=k-2o(H).
\]

The \(n-k\) independent exterior incident edges multiply the conditional expectation of each internal sign by \(q^{n-k}\). For each \(v\notin S\), all its incident edges are independent of \(A_S\), so \(\mathbb E[Z_v\mid A_S]=q^{n-1}\). Therefore

\[
\mathbb E[O\mid A_S]-\mathbb E O=-\frac12\bigl[q^{n-k}(k-2o(H))-kq^{n-1}\bigr].
\]

As \(T_H=\sum_{|S|=k}\mathbf1_{A_S}\), multiply this conditional difference by \(\Pr(A_S)\) and sum over \(S\) to obtain the boxed covariance formula. To compute \(\mathbb ET_H\), note that the number of distinct labelled graphs on \(S\) isomorphic to \(H\) is \(k!/|\operatorname{Aut}(H)|\). Each such graph has \(e(H)\) edges, giving the stated expression. Positivity of \(\mathbb ET_H\) for \(0<p<1\) permits sign analysis without further conditions.

For \(H=P_5\), the degree sequence is \((1,2,2,2,1)\), so \(k=5\), \(o(H)=2\), and \(k-2o(H)=1\). Therefore

\[
\operatorname{Cov}(T_{P_5},O)=-\frac{\mathbb E T_{P_5}}{2}q^{n-5}(1-5q^4).
\]

For every even \(n\ge6\), the exponent \(n-5\) is odd, so the zeros in the open interval occur exactly at \(q=5^{-1/4},0,-5^{-1/4}\). All are distinct and simple sign crossings of the displayed product. As \(p\) runs from zero to one, \(q\) decreases strictly from \(1\) to \(-1\), giving signs \(+,-,+,-\). The broader odd-\(k\) corollary follows identically by writing \(k-2o(H)-kq^{k-1}=k[s-q^{k-1}]\) with \(s=1-2o(H)/k\in(0,1)\).

## Verification
The accompanying standalone Python program \(`verify_covariance.py`\) independently enumerates each labelled ambient graph on \(n\le5\) vertices under five exactly rational edge probabilities; every induced motif class on \(2\le k\le\min(4,n)\) is canonicalized under all vertex permutations. It compares exact rational means and covariances against the formula for every class, yielding 420 exact equalities. Additional exact evaluations for \(P_5\), \(n=6\) at \(p=1/10,2/5,3/5,9/10\), have alternating signs \(+,-,+,-\). These finite tests provide reproducibility, but the proof for all \(n\) and all motifs is the conditional-parity argument above.

To replay: \(`python3 verify_covariance.py`\). The verifier uses only the Python standard library. It exhausts all ambient graphs only in the stated finite ranges; no unproved inference from these tests is made.

## Relationship to prior work
Grimmett and Janson, *Random even graphs*, [1], study even-degree constraints and their random-cluster connections, not the joint covariance of an unrestricted induced-motif count with the number of odd-degree vertices. Lin and Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model*, [2], study multivariate degree-count fluctuations under independent edges; this is a different pair of observables from the motif-versus-total-parity covariance. Matias et al., *Network motifs: mean and variance for the count*, [3], derive motif-count means and variances (using a non-induced motif convention and degree-based graph models), without this mixed covariance or a parity-sign phase diagram. Picard et al., [4], similarly analyze motif-count moments and approximations, not the mixed statistic.

The standard degree-parity character identity and the independence of external incident edges are classical; neither is claimed new. The claim here is the all-motif shape-free mixed covariance formula and its sharp three-reversal consequence. The result is not asserted to settle historical priority; broader implicit coverage in general generating-function or joint-moment work remains possible.

## Limitations
This is a finite-sample theorem for homogeneous independent-edge graphs, not a claim for general random graphs with dependent edges or for graph models conditioned on degrees. The normalized identity is undefined when \(p=0\) or \(p=1\) makes \(\mathbb ET_H=0\); these endpoints are excluded. The three-reversal statement applies only to the specified parity and motif classes. Reproducibility tests at small finite orders are supporting checks, not a replacement for the general proof. No independent audit or literature-priority certification has been performed.

## References
[1] G. Grimmett and S. Janson, *Random even graphs*, preprint first posted 19 September 2007, arXiv:0709.3039, https://arxiv.org/abs/0709.3039.

[2] K. Lin and G. Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model*, preprint first posted 24 December 2009, arXiv:0912.4812, https://arxiv.org/abs/0912.4812.

[3] C. Matias, S. Schbath, E. Birmelé, J.-J. Daudin, and S. Robin, *Network motifs: mean and variance for the count*, REVSTAT 4 (2006), 31–51, https://doi.org/10.57805/revstat.v4i1.25.

[4] F. Picard, J.-J. Daudin, S. Schbath, and S. Robin, *Assessing the exceptionality of network motifs*, research report dated 10 November 2006, https://genome.jouy.inra.fr/ssb/preprint/SSB-RR-1.netmotifs.pdf.
