# Marked Gumbel extremes for products of two uniform involutions

## Finding

Let \(\sigma_n\) and \(\tau_n\) be independent, uniformly random involutions of \([n]\). Join each transposed pair in \(\sigma_n\) by a solid edge and each transposed pair in \(\tau_n\) by a dashed edge, allowing a double edge. A connected component of this two-coloured multigraph is an alternating path or an even alternating cycle; singleton vertices are paths.

For every alternating path \(P\) of length \(|P|\ge2\) vertices, write
\[
X(P)=\frac{|P|}{\sqrt n}-\log\sqrt n.
\]
Give \(P\) mark \(O\) if its two degree-one endpoints are fixed by *different* involutions (this happens for odd \(|P|\)); mark \(S\) if both are fixed by \(\sigma_n\), and \(T\) if both are fixed by \(\tau_n\) (these occur for even \(|P|\)). Define the marked point measure
\[
\Xi_n=\sum_{P:\,|P|\ge2}\delta_{(X(P),\,M(P))}.
\]
Then, in the vague topology of locally finite point measures on \(\mathbb R\times\{O,S,T\}\),
\[
\Xi_n\ \xrightarrow{d}\ \operatorname{PPP}\bigl(e^{-x}\,dx\otimes\nu\bigr),\qquad
\nu(O)=\tfrac12,\quad\nu(S)=\nu(T)=\tfrac14.
\]
The three limiting marked processes are independent. In particular, if \(L_n\) is the largest cycle length of the permutation \(\tau_n\circ\sigma_n\), then, for every \(x\in\mathbb R\),
\[
\lim_{n\to\infty}\Pr\left(\frac{L_n}{\sqrt n}-\log\sqrt n\le x\right)=\exp(-e^{-x}).
\]
With probability tending to one, the longest permutation cycle comes from a unique alternating path; its endpoint mark converges to \(\nu\) and is asymptotically independent of its centered length. In particular, the probability that the two endpoints of the extremal path are fixed by different involutions tends to \(1/2\).

## Assumptions and scope

Both involutions are sampled independently and uniformly from all \(T_n\) involutions on \([n]\), with no restriction on fixed-point count. A path's *length* is its number of vertices; an alternating cycle's length is also its number of vertices. Every graph edge retains its colour, including coincident solid/dashed edges, which form two-vertex cycles. Endpoint marks of the singleton path are not used. The convergence holds for fixed finite collections of bounded intervals of the centered length coordinate, and for their upper tails; no finite-\(n\) exact Poisson assertion is made. The theorem concerns the joint, marked extremal process, not merely a fixed-period marginal.

## Proof

**1. Component enumeration.** Write \(b_n=T_n^2/n!\), so that the probability space has size \(n!b_n=T_n^2\). By independent union of coloured path and even-cycle components, the exponential generating function is (Lugo, Section 4)
\[
B(z)=\sum_{n\ge0}b_nz^n
=\exp\!\left(\frac{z}{1-z}\right)(1-z^2)^{-1/2}.
\]
Every path size \(k\ge1\) has EGF weight \(z^k\). For \(k\ge2\), odd \(k\) gives mark \(O\) and weight \(1\); even \(k\) gives marks \(S,T\), each with weight \(1/2\). A graph-cycle size \(k\) contributes weight \(z^k/k\) if \(k\ge2\) is even, and zero otherwise.

Write \(w_{k,m}\) for these path weights. For any ordered list of \(r\) pairwise distinct paths with prescribed sizes \(k_1,\ldots,k_r\ge2\), and prescribed marks \(m_i\), the multivariate factorial enumeration gives the **exact** identity
\[
\mathbb E\!\sum_{(P_1,\ldots,P_r)\text{ distinct}}
\prod_{i=1}^r\mathbf1\{|P_i|=k_i,\ M(P_i)=m_i\}
=\left(\prod_{i=1}^r w_{k_i,m_i}\right)
\frac{b_{n-\sum_i k_i}}{b_n},
\]
with the quotient interpreted as zero when \(\sum_i k_i>n\). Removing the mark restrictions and taking \(r=1\) yields \(\mathbb E N_{n,k}=b_{n-k}/b_n=(n)_{\underline k}(T_{n-k}/T_n)^2\), for \(k\le n\).

**2. Coefficient ratio, uniformly in the extremal window.** The established coefficient asymptotic for this same generating function (Lugo, Section 7, using Wright's exp-pole estimate) is
\[
b_n\sim\frac{e^{2\sqrt n}}{\sqrt{8\pi e n}}.
\]
Thus, for every fixed \(A>0\), uniformly for integers \(0\le s\le A\sqrt n\log n\),
\[
\frac{b_{n-s}}{b_n}=e^{-s/\sqrt n}(1+o(1)).
\]
Indeed \(2(\sqrt{n-s}-\sqrt n)=-s/\sqrt n+O(s^2/n^{3/2})\), and the remainder is \(o(1)\) in that window. The same asymptotic and positivity give a constant \(C\) such that \(b_{n-s}/b_n\le C e^{-s/\sqrt n}\) for \(0\le s\le n/2\). For \(n/2<s\le n\), the entire ratio is at most \(C n^{1/2}e^{-c\sqrt n}\) for a fixed \(c>0\), using the uniformly valid finite-index coefficient bound \(b_m\le C(1+m)^{-1/2}e^{2\sqrt m}\). These bounds justify truncating all factorial-moment sums at a multiple of \(\sqrt n\log n\).

**3. Marked rare paths.** For \(u_n(x)=\sqrt n(\log\sqrt n+x)\), the geometric Riemann sum gives
\[
\sum_{k\ge\lceil u_n(x)\rceil}e^{-k/\sqrt n}\longrightarrow e^{-x}.
\]
Restricting to odd or even \(k\) gives half of that limit. Hence the sums of the weighted terms \(w_{k,m}e^{-k/\sqrt n}\) have limits \(\nu(m)e^{-x}\). The exact factorial enumeration in step 1 and uniform ratio control in step 2 imply that, for any fixed disjoint centered intervals and marks, *all mixed factorial moments* converge to those of independent Poisson counts with means \(\nu(m)\int_Ie^{-x}dx\). For upper tails \((x,\infty)\), truncate at a fixed upper cutoff \(M\) and use the uniform first-moment bound \(O(e^{-M})\). This proves convergence of the marked point process and of its upper-tail counts.

**4. Alternating graph cycles are negligible at the extreme scale.** Their expected number with size at least \(u_n(x)\) is exactly
\[
\sum_{\substack{k\ge\lceil u_n(x)\rceil\\k\ \mathrm{even}}}
\frac1k\frac{b_{n-k}}{b_n}
=O\left(\frac{1}{\sqrt n\log n}\right)\longrightarrow0.
\]
Each alternating path of size \(k\) contributes one \(k\)-cycle to \(\tau_n\circ\sigma_n\), whereas each alternating graph cycle of even size \(k\) contributes two permutation cycles of length \(k/2\). Thus, up to an event of probability tending to zero, the maximal permutation cycle is the largest marked path, and its centered length is the maximum atom of the limiting point process. A Poisson process with total upper-tail intensity \(e^{-x}\) has maximum CDF \(\exp(-e^{-x})\). Its highest atom has an independent mark of distribution \(\nu\). The limit is diffuse; moreover, at any fixed threshold \(u_n(x)\), the expected number of ordered pairs of distinct paths of the *same* size above that threshold is at most \(\sum_{k\ge u_n(x)}b_{n-2k}/b_n=O(n^{-1/2})\), which rules out exact ties at the top. This proves all assertions.

## Verification

The accompanying `verify_involutions.py` independently enumerates every pair of involutions for each \(1\le n\le7\). It reconstructs alternating graph components and the cycle decomposition of \(\tau\circ\sigma\), and checks the exact first- and second-factorial-moment coefficient identities. The execution passed 60,528 counted checks. This is finite corroboration; the infinite-volume conclusions follow from the coefficient asymptotic and factorial-moment proof above.

## Relationship to prior work

Roberts and Vivaldi (2009, arXiv:0905.4135) studied reversible random permutations with prescribed involution fixed-point counts, deriving their mean orbit-period profile and fixed-period Poisson results. Lugo (2009, arXiv:0911.3604) established the coloured path/cycle generating function, fixed-period distributions, and coefficient asymptotics used as inputs here. These are not new claims. The present result addresses the **largest** cycle in the unrestricted uniform-involution product, its complete extremal path point process, and the independent endpoint-fixation marks. The known fixed-length and mean-size formulas do not alone give this moving-window, joint extreme theorem. General exponential-formula and saddle-point machinery can be applied to related structures and may supply an alternative proof; no general claim of uniqueness or independent verification is made.

## Limitations

The law assumes independent *uniform* involutions. Fixed-point-conditioned models, nonuniform reversible dynamics, and deterministic maps over finite fields are not covered. The Gumbel and Poisson statements are asymptotic, not finite-sample approximations with an explicit rate. A stronger historical theorem on extremes of assemblies may imply some or all of the unmarked statement; the explicit three-mark conclusion is the principal additional distinction. 

## References

1. J. A. G. Roberts and F. Vivaldi, “A combinatorial model for reversible rational maps over finite fields,” first arXiv submission 26 May 2009. https://arxiv.org/abs/0905.4135
2. M. Lugo, “The cycle structure of compositions of random involutions,” first arXiv submission 18 November 2009. https://arxiv.org/abs/0911.3604
3. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), exponential formula and exp-pole coefficient methods. https://algo.inria.fr/flajolet/Publications/book.pdf
