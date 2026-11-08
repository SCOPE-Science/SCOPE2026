# The lattice-window law for concentration after adding a decisive pair

## Finding

Let \(G_n\) be an Erdős–Rényi graph on \(n\) labeled voters, in which every edge is a minimal winning coalition of size two, and let \(\mu(G_n)\) be the squared Deegan–Packel concentration of the associated monotonic voting game. Choose a fixed pair of distinct voters, condition it to be a nonedge, and add that pair as a new minimal winning coalition. For fixed \(c>0\) and \(\beta\in\mathbb R\), independently include each other possible edge with probability
\[
p_n=\frac{c}{n}+\frac{\beta}{n^{3/2}},
\]
for all sufficiently large \(n\) for which \(0<p_n<1\). Let \(I_n\) indicate that adding the pair **strictly increases** \(\mu\). When the initial graph is edgeless, define \(I_n=0\); this exceptional event has vanishing probability.

If \(2c\notin\mathbb Z\), then
\[
\lim_{n\to\infty}\Pr(I_n=1)=\Pr\{\Pi_{2c}>2c+1\},
\]
where \(\Pi_\lambda\) has the Poisson law of mean \(\lambda\). If \(k=2c\) is a positive integer, then
\[
\boxed{\lim_{n\to\infty}\Pr(I_n=1)
=\Pr\{\Pi_k\ge k+2\}
+\Phi\!\left(-\frac{\beta}{\sqrt{2(1+c)}}\right)
\Pr\{\Pi_k=k+1\}.}
\]
Here \(\Phi\) is the standard normal distribution function. At \(\beta=0\), the limit at each half-integer \(c\) is precisely the midpoint of its left and right limits. For instance, at mean degree \(c=1\), the limit is \(1-17e^{-2}/3\), with limiting left and right values \(1-5e^{-2}\) and \(1-19e^{-2}/3\), respectively.

This gives a discrete, infinitely repeating phase diagram for the probability that adding one newly decisive partnership **concentrates** rather than disperses voting power, including the Gaussian transition inside every critical parameter window.

## Assumptions and scope

All graphs are simple, undirected, labeled, and finite. The voting game for a nonempty graph \(G=(V,E)\) declares a nonempty coalition winning exactly if it contains both endpoints of some edge. Its minimal winning coalitions are therefore exactly \(E\). The Deegan–Packel power of voter \(i\) equals
\[
DP_i(G)=\frac{\deg_G(i)}{2|E|},\qquad
\mu(G)=\sum_{i\in V}DP_i(G)^2.
\]
This is the normalization \(a=1\) of the concentration measure characterized by Abe; multiplying by any fixed positive constant does not change the comparison event. The random pair can be taken as \(\{1,2\}\) without loss of generality. Conditioning it to be absent leaves all other edges independently Bernoulli with the displayed probability. There is no assumption of connectedness, weightedness, properness, or symmetry of the realized voting game. The first public motivating source is Abe's arXiv posting on 2026-06-04; that is not the date of the subsequent PDF revision.

## Proof

**1. Deterministic edge-insertion criterion.** Let \(m=|E|\ge1\), \(d_i=\deg_G(i)\), and define the unordered two-star (wedge) count
\[
W=\sum_i\binom{d_i}{2},\qquad S=\sum_i d_i^2=2m+2W.
\]
For a missing pair \(\{u,v\}\), put \(D=d_u+d_v\). Inserting the pair changes \(m\) to \(m+1\) and \(S\) to \(S+2D+2\). Consequently
\[
\mu(G+uv)>\mu(G)
\iff 2m^2(D+1)>(2m+1)S
\iff D>1+\frac{2W}{m}+\frac1m+\frac{W}{m^2}.
\tag{1}
\]
No approximation is involved. The criterion exposes the local/global competition: the new pair's endpoint-degree sum must exceed a threshold determined by the global wedge-to-edge ratio.

**2. Local Poisson limit and global first order.** Write \(N=\binom n2\) and \(K=n\binom{n-1}{2}=N(n-2)\). Under the stated conditioned Bernoulli model, the new pair's original degree sum is exactly \(D_n\sim\operatorname{Binomial}(2n-4,p_n)\). Hence \(D_n\Rightarrow\Pi_{2c}\). Apart from forcing one edge absent, the global edge and wedge statistics satisfy
\[
\frac{m_n}{n}\xrightarrow{\Pr}\frac c2,
\qquad\frac{W_n}{n}\xrightarrow{\Pr}\frac{c^2}{2},
\qquad\frac{W_n}{m_n}\xrightarrow{\Pr}c.
\]
Indeed the unconditioned expectations are \(Np_n\) and \(Kp_n^2\); both variances are \(O(n)\), as shown below. Removing the forced pair alters the statistics by \(O_{\Pr}(1)\). Thus the right-hand side of (1) tends in probability to \(2c+1\). If \(2c\) is not an integer, the Poisson variable has no atom at the limiting strict threshold, giving the first formula.

**3. Gaussian fluctuation of the global threshold.** Initially work without the forced missing pair. Write \(X_e\) for the Bernoulli indicator of edge \(e\), and \(Y_e=X_e-p_n\). Summing over unordered pairs of adjacent edges gives the exact orthogonal decomposition
\[
W_n-cm_n=Kp_n^2-cNp_n
+\bigl(2(n-2)p_n-c\bigr)\sum_eY_e
+\sum_{\{e,f\}:e\sim f}Y_eY_f.
\tag{2}
\]
The last two sums are uncorrelated, and distinct quadratic summands are mutually uncorrelated. Therefore
\[
\operatorname{Var}(W_n-cm_n)=
\bigl(2(n-2)p_n-c\bigr)^2Np_n(1-p_n)
+Kp_n^2(1-p_n)^2,
\tag{3}
\]
while
\[
\frac{Kp_n^2-cNp_n}{\sqrt n}\longrightarrow\frac{c\beta}{2},
\qquad\frac{\operatorname{Var}(W_n-cm_n)}n
\longrightarrow\sigma_c^2:=\frac{c^2(1+c)}2>0.
\tag{4}
\]
For completeness, asymptotic normality follows directly by the cumulant method. For any fixed order \(r\ge3\), expand the \(r\)-th cumulant of the edge-and-wedge polynomial \(W_n-cm_n\). Each summand is an edge or a two-star indicator. Joint cumulants vanish when the corresponding edge sets split into two groups with no common edge. A remaining connected overlap diagram has an underlying connected graph with \(v\) vertices and \(e\) distinct edges, so \(e\ge v-1\). Its cumulant has magnitude \(O(p_n^e)\), while it has \(O(n^v)\) embeddings. With \(p_n=O(1/n)\), each diagram type contributes \(O(n)\). Only finitely many diagram types occur at fixed \(r\), so every such cumulant is \(O(n)\). After division by \(n^{r/2}\) it vanishes. The second cumulant tends to (4), and the moment-determinate Gaussian moment sequence proves
\[
\frac{W_n-cm_n}{\sqrt n}\Rightarrow
\mathcal N\!\left(\frac{c\beta}{2},\frac{c^2(1+c)}2\right).
\tag{5}
\]
Conditioning edge \(12\) absent does not change (5): the edge itself and all wedges touching it contribute only \(O_{\Pr}(1)\). Moreover, the limit in (5) is asymptotically independent of \(D_n\). To see this, delete the edges incident to vertices 1 and 2, leaving an independent \(G(n-2,p_n)\) background. The deleted edges number \(O_{\Pr}(1)\) and affect only \(O_{\Pr}(1)\) wedges (their expected count is bounded). The scaled global statistic differs from that of the independent background by \(o_{\Pr}(1)\). This establishes the claimed joint limit without assuming independence at finite \(n\).

**4. Arithmetic tie and its transition.** Suppose \(2c=k\in\mathbb Z_{>0}\). For \(D_n\le k\) condition (1) fails with probability tending to one, and for \(D_n\ge k+2\) it holds with probability tending to one. At the sole boundary value \(D_n=k+1\), the exact criterion from (1) reduces to
\[
2m_n(c m_n-W_n)>m_n+W_n.
\tag{6}
\]
The right-hand side divided by \(2m_n\) is \(O_{\Pr}(1)\), so (5), its asymptotic independence from \(D_n\), and \(\sigma_c>0\) yield
\[
\Pr(I_n=1\mid D_n=k+1)
\longrightarrow\Phi\!\left(-\frac{c\beta/2}{\sigma_c}\right)
=\Phi\!\left(-\frac{\beta}{\sqrt{2(1+c)}}\right).
\]
Combining with \(D_n\Rightarrow\Pi_k\) proves the asserted formula. Letting \(c\) approach \(k/2\) from below and above gives the respective limits \(\Pr(\Pi_k\ge k+1)\) and \(\Pr(\Pi_k\ge k+2)\), whose midpoint is the \(\beta=0\) case. This proves every assertion.

## Verification

The bundled standalone standard-library `checker.py` computes concentration directly from the squared Deegan–Packel vector and independently from \(S/(4m^2)\); exhaustively checks both sides of (1) for every nonempty labeled simple graph on three through five vertices and each missing pair (5,305 cases); and verifies the exact mean and variance in (3) against enumerated Bernoulli graph distributions for three through five vertices at three rational densities (3,288 graph weights). It also runs fixed-seed independent-edge simulations, including both signs of the critical-window perturbation, as limited numerical spot checks. The analytical cumulant argument, not the finite tests or Monte Carlo, establishes (5) and the all-order asymptotic law. Run with `python3 checker.py` using Python 3.9 or later; no dependencies beyond the standard library.

## Relationship to prior work

Abe (2026) proves the fundamental quadratic Deegan–Packel representation and overlap identity and studies voting thresholds in two-group councils. This finding accepts those formulas and addresses a different operation and distribution: adding one minimal winning pair to a random sparse **graphic** voting game. Hof, Kern, Kurz and Paulusma (2018) formally develop graphic simple voting games in the context of the critical-threshold distance to weighted majority games; their objective is distinct from concentration. Classical sparse random-graph two-star fluctuation methods inform the probability calculation, but do not themselves specify a voting-power insertion event, its integer-atom discontinuities, or its Gaussian boundary window. The exact implication comparisons and accessible-source limitations are recorded separately in the review.

## Limitations

The result applies to edge-generated monotone voting games with the independent sparse \(G(n,p_n)\) model and a proposed absent pair, not to arbitrary weighted voting rules, correlated coalitions, or different concentration indices. The limit is not uniform over \(c\) near its half-integer thresholds without using the stated \(n^{-1/2}\) parameter window. A possible equivalent treatment in unindexed literature cannot be excluded; no publication priority or independently certified status is claimed. Empirical finite checks cannot prove the central-limit theorem.

## References

1. Takaaki Abe, *Measuring Concentration of Power in Approval Voting Games*, arXiv:2606.05655, first submitted 2026-06-04, revision 2026-06-26, especially Proposition 4.1 and Sections 5–6. https://arxiv.org/pdf/2606.05655
2. Frits Hof, Walter Kern, Sascha Kurz, and Daniël Paulusma, *Simple Games versus Weighted Voting Games*, arXiv:1805.02192, 2018, especially Sections 1–2 on graphic simple voting games. https://arxiv.org/html/1805.02192v1
3. John Deegan Jr. and Edward W. Packel, *A New Index of Power for Simple \(n\)-Person Games*, International Journal of Game Theory 7 (1978), 113–123. The primary index definition used here is also reproduced in Abe (2026), Proposition 4.1.
