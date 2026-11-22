# Inhomogeneous Poisson onset of consecutive missing parts in random integer partitions

## Finding

For each fixed integer \(r\ge2\), let \(\lambda_n\) be a uniformly chosen integer partition of \(n\). Write \(\nu(j)\) for the number of occurrences of the part \(j\), and let
\[
A_{r,n}(k)=\mathbf1_{\{\nu(k)=\nu(k+1)=\cdots=\nu(k+r-1)=0\}}.
\]
Put \(c=\pi/\sqrt6\) and \(\alpha_r=r/[2(r+1)]\). Then the random locally finite counting measures
\[
\Xi_{r,n}=\sum_{k\ge1}A_{r,n}(k)\,\delta_{k/n^{\alpha_r}}
\]
converge vaguely in distribution on \([0,\infty)\) to a Poisson point process with intensity measure
\[
\mu_r(dx)=c^r x^r\,dx.
\]
In particular, the first starting point \(M_{r,n}=\min\{k\ge1:A_{r,n}(k)=1\}\), called the \(r\)-chain minimal excludant, obeys the exact limiting survival law
\[
\lim_{n\to\infty}\Pr\!\left(\frac{M_{r,n}}{n^{\alpha_r}}>y\right)=\exp\left(-\frac{c^ry^{r+1}}{r+1}\right),\qquad y\ge0.
\]
More generally, if \(M_{r,n}^{(h)}\) is the \(h\)-th smallest \(k\) with \(A_{r,n}(k)=1\), then for each fixed \(h\ge1\),
\[
\lim_{n\to\infty}\Pr\!\left(\frac{M_{r,n}^{(h)}}{n^{\alpha_r}}>y\right)
=e^{-\Lambda_r(y)}\sum_{j=0}^{h-1}\frac{\Lambda_r(y)^j}{j!},\qquad \Lambda_r(y)=\frac{c^r y^{r+1}}{r+1}.
\]
For example, with \(r=2\), the onset scale is \(n^{1/3}\) and the survival function is \(\exp(-\pi^2y^3/18)\). The classical first *single* absent part has the different \(n^{1/4}\) scale.

## Assumptions and scope

An integer partition of \(n\ge0\) is a finite multiset of positive integers summing to \(n\). Each partition has probability \(1/p(n)\), where \(p(n)\) counts partitions of \(n\). An absent part has multiplicity zero. The parameter \(r\) is fixed before \(n\to\infty\); the assertions are not uniform when \(r\) grows. The point process counts all starting locations of absent runs of length \(r\), whether or not a longer absent run contains more than one such location. Convergence of point processes means joint convergence to independent Poisson variables of counts on finitely many pairwise disjoint bounded intervals whose endpoints have zero intensity measure.

## Proof

**Step 1: independent geometric coordinates and exact conditioning.** Let \(q_n=e^{-c/\sqrt n}\) and let \((Z_j)_{j\ge1}\) be independent with
\[
\Pr(Z_j=a)=(1-q_n^j)q_n^{ja},\qquad a=0,1,2,\ldots.
\]
The random total weight \(S_n=\sum_{j\ge1}jZ_j\) is finite almost surely. The product of the geometric probabilities of any fixed multiplicity vector of total weight \(n\) depends only on \(n\), so the conditional distribution \((Z_j)_{j\ge1}\mid S_n=n\) is exactly the multiplicity-vector distribution of \(\lambda_n\). No approximation enters this identity.

**Step 2: deconditioning on all part sizes below the onset scale.** Fix \(B>0\), and let \(m_n=\lfloor Bn^{\alpha_r}\rfloor+r-1=o(\sqrt n)\). Set
\[
V_n=\sum_{j\le m_n}jZ_j,\qquad W_n=S_n-V_n.
\]
Standard summation of geometric moments, justified by Riemann sums, yields
\[
\mathbb ES_n=n+O(\sqrt n),\qquad
\operatorname{Var}(S_n)=\frac{\pi^2}{3c^3}n^{3/2}(1+o(1)).
\]
Since \(j^2\operatorname{Var}(Z_j)=j^2q_n^j/(1-q_n^j)^2\le n/c^2\), independence gives \(\operatorname{Var}(V_n)\le nm_n/c^2=o(n^{3/2})\). Hence \((V_n-\mathbb EV_n)/n^{3/4}\to0\) in probability, while \(\operatorname{Var}(W_n)\sim\operatorname{Var}(S_n)\).

Here is a local central limit estimate sufficient for the transfer. Both \(S_n\) and \(W_n\) have lattice probabilities, uniformly in integers \(a\), of the form
\[
\Pr(U_n=a)=\frac{1}{\sqrt{2\pi}\,s_{U,n}}
\exp\!\left(-\frac{(a-\mathbb EU_n)^2}{2s_{U,n}^2}\right)
+o(n^{-3/4}),\qquad s_{U,n}^2=\operatorname{Var}(U_n),
\]
where \(U_n\) is either sum. To verify this estimate rather than assume it, write the centered characteristic function as a product of geometric characteristic functions. For every \(j\),
\[
\left|\mathbb E e^{itjZ_j}\right|^2=
\left(1+\frac{2q_n^j(1-\cos(jt))}{(1-q_n^j)^2}\right)^{-1}.
\]
For integers \(j\) in a fixed interval \([a\sqrt n,b\sqrt n]\), above \(m_n\), their parameters \(q_n^j\) are bounded away from zero and one. Summation of cosines gives, for \(|t|\le\pi\), a lower bound of the form
\[
\sum_{j=\lceil a\sqrt n\rceil}^{\lfloor b\sqrt n\rfloor}(1-\cos(jt))
\ge d\sqrt n\,\min\{1,nt^2\}
\]
with some \(d>0\); this follows from the geometric-sum formula for \(|t|\gg n^{-1/2}\) and a compact-parameter Riemann-sum bound for \(|t|=O(n^{-1/2})\). Thus the characteristic function outside the central window is bounded by \(\exp[-d'\min(n^{3/2}t^2,\sqrt n)]\). The sum of absolute centered third moments of the summands is \(O(n^2)=o((n^{3/4})^3)\), so Taylor expansion on the central Fourier window and Fourier inversion prove the stated uniform local estimate for both sums. All estimates apply to \(W_n\) because \(m_n=o(\sqrt n)\).

It follows that
\[
R_n(V_n):=\frac{\Pr(W_n=n-V_n)}{\Pr(S_n=n)}\longrightarrow1
\quad\text{in probability under the independent-coordinate law.}
\]
Indeed, \(n-\mathbb ES_n=O(\sqrt n)\), the fluctuations of \(V_n\) are \(o_{\Pr}(n^{3/4})\), and the two local Gaussian densities share the same asymptotic variance. Moreover \(R_n(V_n)\ge0\) and, by convolution, \(\mathbb ER_n(V_n)=1\). Therefore \(R_n(V_n)\to1\) in \(L^1\) (for example by the elementary positive-density version of Scheffé's lemma). Consequently, the total-variation distance between the laws of \((Z_1,\ldots,Z_{m_n})\) with and without conditioning on \(S_n=n\) tends to zero.

**Step 3: a rare-run Poisson limit in the independent model.** Now work before conditioning. The absence events \(I_j=\mathbf1_{\{Z_j=0\}}\) are independent Bernoulli variables with \(p_{j,n}=1-e^{-cj/\sqrt n}\). Let \(A_k=\prod_{a=0}^{r-1}I_{k+a}\). For each bounded interval \((u,v]\subset[0,\infty)\),
\[
\sum_{un^{\alpha_r}<k\le vn^{\alpha_r}}\mathbb EA_k
\longrightarrow c^r\int_u^v x^r\,dx.
\]
This follows directly from \(p_{k,n}=ck/\sqrt n+O(k^2/n)\), Riemann summation, and the identity \((r+1)\alpha_r=r/2\).

For all \(k\le Bn^{\alpha_r}\) and the finitely many neighboring indices, put \(p_{*,n}=\max p_{j,n}=O(n^{-1/[2(r+1)]})\); hence \(n^{\alpha_r}p_{*,n}^r=O(1)\). In each fixed joint factorial moment of the run-start counts, group the distinct selected start locations into connected components, joining starts whose distance is less than \(r\). If there are \(t\) starts in \(s\) components, their union requires the absence of at least \(rs+t-s\) distinct part sizes. For fixed \(r,t\), there are \(O(n^{\alpha_rs})\) such configurations, and the contribution of all configurations with an overlap (\(t>s\)) is at most
\[
O\!\left((n^{\alpha_r}p_{*,n}^{r})^s p_{*,n}^{t-s}\right)=o(1).
\]
Configurations with no overlaps factor by independence, and their factorial moments converge to those of independent Poisson variables with means \(c^r\int_u^v x^r\,dx\) in disjoint intervals. The first-moment bounds supply tightness, so the counts converge jointly and the full point process converges vaguely to the asserted inhomogeneous Poisson process.

**Step 4: transfer and order statistics.** Every run-start event in \([0,B]\) depends only on parts of sizes at most \(\lfloor Bn^{\alpha_r}\rfloor+r-1\). The total-variation estimate from Step 2 transfers the independent-model point-process limit to uniform partitions. A Poisson process has no points in \([0,y]\) with probability \(e^{-\Lambda_r(y)}\), and its count there is \(\operatorname{Poisson}(\Lambda_r(y))\). Applying this fact to the first and the \(h\)-th start proves the survival formulas. Endpoints cause no problem because the limiting intensity is continuous.

## Verification

The accompanying standalone Python program `verify.py` uses two independent exact enumerations of finite partition events: (i) a dynamic program tracking forbidden missing runs and (ii) direct enumeration of partitions. It checks their agreement for all \(0\le n\le24\), \(1\le r\le4\), and \(1\le m\le6\), totaling 600 assertions. It also prints exact finite-\(n\) survival probabilities for three larger weights and three fixed run lengths alongside the asymptotic approximation; these finite comparisons are illustrations and are not used to infer the limiting theorem. Reproduction: `python verify.py` using only the Python standard library.

## Relationship to prior work

Bhoria, Eyyunni and Maji introduced the \(r\)-chain minimal excludant, supplied identities for its sum over partitions, and asked in their Section 5, Problem 6, for asymptotic information about that sum. Bhoria, Eyyunni and Li subsequently studied bijective identities for the chain minimal and maximal excludants. Those exact identities neither state nor directly supply the location point-process limit, and the present result does not claim to solve the earlier problem about the full first moment. Arratia and Tavaré's independent-process approach provides the general conditioning framework; the total-variation transfer on the relevant growing window and the rare overlapping-run analysis are supplied here. A *least \(r\)-gap* defined by part multiplicity below \(r\) is a different statistic from \(r\) consecutive wholly absent part sizes.

## Limitations

The proof establishes weak distributional/point-process convergence for each fixed \(r\ge2\) only. No rate of convergence, uniformity in \(r\), asymptotic of the unconditional mean or higher unbounded moments, or full-series result is asserted. The standalone finite checks do not certify an infinite asymptotic claim. The scientific literature comparison is limited to inspected works and discoverable records; an unindexed equivalent statement is possible.

## References

1. S. C. Bhoria, P. Eyyunni, and B. Maji, *A new generalization of the minimal excludant arising from an analogue of Franklin's identity*, 2022 preprint, arXiv:2208.03658v1, first posted 2022-08-07, https://arxiv.org/abs/2208.03658 (especially Definition 1, Theorem 2.6, and Section 5, Problem 6).
2. S. C. Bhoria, P. Eyyunni, and R. Li, *On the combinatorics of r-chain minimal and maximal excludants*, 2023 preprint, arXiv:2312.02620v1, first posted 2023-12-05, https://arxiv.org/abs/2312.02620 (especially Theorems 1.5–1.10).
3. R. Arratia and S. Tavaré, *Independent process approximations for random combinatorial structures*, Advances in Mathematics 104 (1994), 90–154, https://www.columbia.edu/cu/simontavare/STpapers-pdf/AT94.pdf (independent geometric component laws and conditioning for integer partitions).
