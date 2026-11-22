# An inhomogeneous marked Poisson law for simplicial vertices of uniform random interval graphs

## Finding

For a graph vertex, **simplicial** means that all of its neighbors are pairwise adjacent. In the independent-uniform-endpoint interval graph defined below, put
\[
\Xi_n=\sum_{i:\,i\text{ simplicial}}\delta_{(A_i,n(B_i-A_i))}.
\]
On \((0,1)\times[0,\infty)\), this point process converges vaguely in distribution to a Poisson point process with intensity \(2f_x(u)\,dx\,du\), where
\[
\begin{aligned}
\lambda_L(x)&=2(1-x),\qquad \lambda_R(x)=2x,\\
f_x(u)&=e^{-\lambda_L(x)u}+\lambda_L(x)\int_0^u
 e^{-\lambda_R(x)v-\lambda_L(x)(u-v)}\,dv.
\end{aligned}
\]
Consequently, for any fixed \(0<\alpha<\beta<1\), the count \(S_n[\alpha,\beta]\) of simplicial intervals with left endpoint in \([\alpha,\beta]\) obeys
\[
S_n[\alpha,\beta]\ \xrightarrow{d}\ \operatorname{Poisson}\!\left(
 \log\frac{\beta(1-\alpha)}{\alpha(1-\beta)}\right).
\]
Counts in finitely many disjoint interior spatial bands have independent Poisson limits. In particular the central half-band \([1/4,3/4]\) has limiting mean \(\log 9\). The interval lengths, multiplied by \(n\), retain a nontrivial position-dependent limiting mark distribution; the spatial rate is \(1/[x(1-x)]\), not a constant.

A companion exact finite-size formula holds. For \(n\ge2\) and \(0\le a<b\le1\), condition on a specified interval being \([a,b]\). Define
\[
\begin{aligned}
h(a,b)&=1-\big[(1-a)^2-(1-b)^2\big],\\
g(a,b,t)&=1-(t^2-a^2)-\big[(1-t)^2-(1-b)^2\big].
\end{aligned}
\]
Its exact probability of being simplicial is
\[
\boxed{p_n(a,b)=h(a,b)^{n-1}+(n-1)\int_a^b 2(1-t)g(a,b,t)^{n-2}\,dt.}
\]
The expected total number \(S_n\) of simplicial vertices also satisfies the explicit lower bound
\[
\mathbb E S_n\ge 2H_{2n}-H_n-1
=\log n+2\log2+\gamma-1+o(1).
\]
This is a lower bound, not an asserted equivalent for the unrestricted global count.

## Assumptions and scope

For every integer \(n\ge1\), sample \(2n\) independent uniformly distributed real values on \([0,1]\), pair them by their fixed labels, and sort within each pair to produce \(I_i=[A_i,B_i]\), with \(A_i<B_i\) almost surely. Join vertices \(i,j\) precisely when \(I_i\cap I_j\ne\varnothing\). All intervals are independent; the joint density of \((A_i,B_i)\) is \(2\) on \(0<a<b<1\). Degenerate equal endpoints have probability zero. The point process restricts to left endpoints strictly inside \((0,1)\); its limit is locally finite there. Spatial bands remain fixed strictly inside \((0,1)\). Convergence makes no claim about the total simplicial count on all of \([0,1]\).

## Proof

**1. Exact endpoint-order criterion.** Fix a tagged interval \([a,b]\). For all other intervals, consider their left endpoints and right endpoints strictly inside \((a,b)\). Every neighbor of the tagged interval either contains \(a\), contains \(b\), or has one or both endpoints inside \((a,b)\). The neighbors form a clique if and only if every interior left endpoint occurs before every interior right endpoint; an empty set of either type makes the condition automatic. Indeed, if a right endpoint \(r\) lies before a left endpoint \(\ell\), both in \((a,b)\), their owning intervals are distinct (an interval has left endpoint before right endpoint), intersect the tagged interval, but are disjoint from each other. Conversely, if two tagged neighbors are disjoint, the earlier neighbor must end at an interior right endpoint before the later neighbor's interior left endpoint. This proves the equivalence without assumptions about any other interval outside the tagged one.

**2. Finite conditional probability.** The probability that a fresh interval's left endpoint is in \((a,b)\) is \((1-a)^2-(1-b)^2\); thus the probability that none of the other \(n-1\) intervals has an interior left endpoint is \(h^{n-1}\). Otherwise there is a unique *latest* interior left endpoint, say \(t\). Its owner's density at \(t\) is \(2(1-t)\). Every other interval must avoid both (i) a right endpoint in \((a,t)\) and (ii) a left endpoint in \((t,b)\). For a single interval these two forbidden events are disjoint because its left endpoint must precede its right endpoint. Their probabilities are respectively \(t^2-a^2\) and \((1-t)^2-(1-b)^2\). The probability of avoiding both is \(g(a,b,t)\). Summing over the \(n-1\) possible owners of the unique latest left endpoint gives the displayed integral. This exhausts the disjoint alternatives and proves the exact formula.

**3. Joint rare-event scaling.** Fix a compact spatial band \([\alpha,\beta]\subset(0,1)\), a finite mark cutoff \(U\), and finitely many distinct macroscopic positions \(x_1,\ldots,x_k\). Condition on \(k\) labelled tagged intervals having \(A_i=x_i\) and \(B_i=x_i+u_i/n\), where \(0\le u_i\le U\). Their shrinking supports are disjoint for all large \(n\). For a fresh other interval, the probability of a left endpoint falling in a scaled subwindow \(n^{-1}J\) around \(x_i\) is \(2(1-x_i)|J|/n+O(n^{-2})\), while that for a right endpoint is \(2x_i|J|/n+O(n^{-2})\). A single fresh interval hits two distinct such small endpoint windows, or contributes both endpoints in one window, with probability \(O(n^{-2})\). Across \(n-k\) independent fresh intervals, the left and right endpoint processes inside the \(k\) disjoint windows therefore converge jointly to independent homogeneous Poisson processes of respective rates \(\lambda_L(x_i)\) and \(\lambda_R(x_i)\) in each scaled window. One may prove this directly by expanding the joint multinomial probability generating function; the aggregate multi-hit error is \(O(n^{-1})\). The other tagged intervals have no endpoints inside these windows.

The simplicial event in a window is the endpoint-order event from step 1. Poisson points are distinct almost surely, so this event is a continuity set. Its probability is \(f_x(u)\): either there is no left point, of probability \(e^{-\lambda_Lu}\), or the final left point is at \(v\in(0,u)\), no further left point occurs and no right point lies before \(v\), giving the integrated density \(\lambda_L e^{-\lambda_L(u-v)}e^{-\lambda_Rv}\). Accordingly, the joint conditional simplicial probabilities of any fixed number of tagged short intervals converge to the product of their respective \(f_{x_i}(u_i)\).

For bounded continuous test windows contained in \((0,1)\times[0,U]\), the \(k\)-th factorial moment measure of \(\Xi_n\) is an integral over \(k\) ordered distinct tagged intervals. Change variables \(b_i=a_i+u_i/n\). The joint endpoint density contributes \((2/n)^k\), while the count of labelled choices contributes \((n)_k\). Almost every configuration has distinct macroscopic \(a_i\); on those configurations step 3 applies. Since conditional probabilities are bounded by one and the test domain has finite Lebesgue volume, dominated convergence proves convergence of every factorial moment measure to that of the process with intensity \(2f_x(u)\,dx\,du\). Uniform first-moment bounds on compact sets ensure tightness. The standard factorial-moment characterization of locally finite Poisson point processes gives vague convergence.

**4. Removing the length cutoff in interior bands.** Fix \(0<\alpha<\beta<1\), and write \(\ell=b-a\). If some other interval ends in \((a,a+\ell/4)\) and another begins in \((a+\ell/2,a+3\ell/4)\), both meet \([a,b]\) but are disjoint from each other. The respective probabilities for one independent interval are at least \(\alpha\ell/2\) and \((1-\beta)\ell/8\); the second bound follows because \(a+3\ell/4\le 1-(1-a)/4\). Therefore, with \(c=\min\{\alpha/2,(1-\beta)/8\}>0\), the simplicial probability is at most \(2e^{-c(n-1)\ell}\), by a union bound on the absence of one of these two event types. The expected number of simplicial intervals with \(a\in[\alpha,\beta]\) and \(n\ell>T\) is consequently at most
\[
4n(\beta-\alpha)\int_{T/n}^\infty e^{-c(n-1)\ell}\,d\ell
\le \frac{8(\beta-\alpha)}c e^{-cT/2},\qquad n\ge2.
\]
This is uniform in \(n\), and tends to zero as \(T\to\infty\). Thus the compact-mark Poisson limit extends to full simplicial counts on any fixed interior band. Finally,
\[
\int_0^\infty f_x(u)\,du=\frac1{\lambda_L(x)}+\frac1{\lambda_R(x)}
=\frac1{2x(1-x)}.
\]
Integrating twice this quantity over \([\alpha,\beta]\) yields exactly the stated logarithmic Poisson mean. Disjoint bands become independent from the joint Poisson point-process limit.

**5. Harmonic finite-size lower bound.** Let \(\mathcal L_n\) and \(\mathcal R_n\) be the sets of tagged intervals that contain no left, respectively no right, endpoint of any *other* interval. Membership in either set guarantees simpliciality. Directly from step 2,
\[
\begin{aligned}
\mathbb E|\mathcal L_n|&=2n\int_{0<a<b<1}h(a,b)^{n-1}\,da\,db\\
&=\int_0^1\frac{1-s^{2n}}{1-s^2}\,ds
=\sum_{j=0}^{n-1}\frac1{2j+1}
=H_{2n}-\frac12H_n.
\end{aligned}
\]
The identical expression holds for \(\mathbb E|\mathcal R_n|\) by reflection. The overlap \(\mathcal L_n\cap\mathcal R_n\) comprises intervals with no other endpoint strictly between their endpoints; equivalently, matched adjacent endpoints among the sorted \(2n\) endpoints. In a uniform random perfect matching each fixed consecutive pair is paired with probability \(1/(2n-1)\), so the expected overlap count is exactly one. Inclusion-exclusion proves \(\mathbb E S_n\ge\mathbb E|\mathcal L_n\cup\mathcal R_n|=2H_{2n}-H_n-1\). Harmonic-number asymptotics give the displayed growth lower bound.

## Verification

The accompanying dependency-free `check.py` enumerates every perfect matching of \(2n\) distinct ranked endpoints for \(1\le n\le6\); for every vertex it checks the original graph-theoretic simplicial condition against the endpoint-order criterion. The program also checks the exact conditional polynomial-integral formula against exhaustive endpoint orderings at nine rational parameter choices. The executed result was **PASS: 67,598 exact structural/order checks**. Run `python3 check.py` from the extracted package directory. Finite enumeration verifies only finite instances and supporting identities; the Poisson limit is proved analytically in steps 3–4.

## Relationship to prior work

The independent paired-endpoint model is classical (Scheinerman, 1988; Boucheron and Fernandez de la Vega, 2001). Previous investigations establish independence-number fluctuations, interval-graph properties and dense graph limits, rather than the present marked point process of vertices whose entire neighbor set forms a clique. The full accessible Iliopoulos treatment and the interval-graph-limit text were inspected for same-model results; neither of the inspected relevant sections establishes this law. A 2026 database result concerning simplicial vertices in *near-complete independent-edge graphs* concerns a different model, and one concerning covariance of component count and covered length in paired intervals concerns a different statistic. The new statement is neither a consequence of those stated findings nor a relabelled global graph limit. Bibliographic access to Scheinerman's original complete text remained unavailable, so definitive historical priority is not certified.

## Limitations

The Poisson convergence is vague on the interior position space, not on a compactified boundary including positions zero and one. The count law requires a fixed band bounded away from both endpoints; the unrestricted expected simplicial count is only lower-bounded here. No convergence rate, full global count law or coupling to graph-elimination dynamics is established. The independent scientific validation and comprehensive historical-priority certification have not been performed. An inaccessible older original paper leaves a residual risk of overlooked related assertions.

## References

1. E. R. Scheinerman, “Random interval graphs,” *Combinatorica* 8 (1988), 357–371. DOI: `10.1007/BF02189092`. Full text not obtained.
2. S. Boucheron and W. Fernandez de la Vega, “On the Independence Number of Random Interval Graphs,” *Combinatorics, Probability and Computing* 10 (2001), 385–396. DOI: `10.1017/S0963548301004813`; published online 2001-12-10. Model and independence-number study; abstract and publication metadata checked.
3. P. Diaconis, S. Holmes and S. Janson, “Interval graph limits,” arXiv:`1102.2841`, first posted 2011-02-14. Accessible full text studied at relevant model and graph-limit sections.
4. V. Iliopoulos, “Random Interval Graphs,” University of Essex M.Sc. thesis (2005); open full text `https://repository.essex.ac.uk/14414/1/M.Sc.%20thesis.pdf` and arXiv:`1507.06275`. Accessible full text and relevant chapter structure inspected.
