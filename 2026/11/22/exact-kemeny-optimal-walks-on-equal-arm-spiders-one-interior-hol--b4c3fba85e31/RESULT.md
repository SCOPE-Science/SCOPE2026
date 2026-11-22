# Exact Kemeny-optimal walks on equal-arm spiders: one interior holding junction and a degree-dependent uniformity penalty

## Finding

For integers \(k\ge3\) and \(L\ge3\), let \(S_{k,L}\) be the tree made of \(k\) internally disjoint paths of length \(L\) meeting at one hub. Among **all** irreducible real symmetric, entrywise nonnegative row-stochastic transition matrices supported on its edges and diagonal, there is a unique minimizer of the non-return Kemeny spectral sum
\[
\mathcal K(P)=\sum_{i=2}^{kL+1}\frac{1}{1-\lambda_i(P)}.
\]
All edges at the same depth have the same transition probability. Set \(N=kL+1\), and for \(1\le j\le L\) define
\[
 c_j=(L-j+1)((k-1)L+j),\quad
 E=\sum_{\substack{2\le j\le L\\j\text{ even}}}c_j,\quad
 O=\sum_{\substack{3\le j\le L\\j\text{ odd}}}c_j,
 \qquad u=\frac{\sqrt E}{\sqrt E+\sqrt O}.
\]
For each arm, indexed by depth from the hub, the exact optimal edge probabilities are
\[
\boxed{w_1=\frac1k,\qquad w_{2h}=u,\qquad w_{2h+1}=1-u\quad(2h+1\ge3),}
\]
with indices in the stated range. In the unique optimum the hub and every nonterminal depth \(j\ge2\) have zero holding probability; each depth-one vertex has the *strictly positive* holding probability \(1-1/k-u\), and each terminal leaf has the positive holding probability \(1-w_L\). All tree edges are used. The exact minimum is
\[
\boxed{\mathcal K_* =\frac{k}{kL+1}\left[kL((k-1)L+1)+(\sqrt E+\sqrt O)^2\right].}
\]
For each fixed \(k\ge3\), as \(L\to\infty\),
\[
 u\to\frac12,\qquad 1-\frac1k-u\to\frac12-\frac1k,
 \qquad \mathcal K_*\sim \frac{3k-2}{3}L^2.
\]
The standard maximum-degree, equal-edge symmetric walk with edge probabilities \(1/k\) incurs the sharp asymptotic multiplicative penalty
\[
\boxed{\lim_{L\to\infty}\frac{\mathcal K(P_{\rm uniform})}{\mathcal K_*}=\frac{k}{2}.}
\]
For example, at \(k=L=3\), the exact optimal depth probabilities are \((1/3,4/7,3/7)\), the depth-one hold is \(2/21\), and \(\mathcal K_*=168/5\).

## Assumptions and scope

The graph contains one hub and \(kL\) other vertices, with \(k\) paths of exactly \(L\) edges. Each allowed nonloop entry \(P_{xy}=P_{yx}\ge0\), each diagonal entry \(P_{xx}\ge0\), and each row sums to one. No periodicity restriction is needed; disconnected transitions have infinite objective and are excluded. The uniform stationary distribution is automatic for a symmetric stochastic matrix. The spectral sum omits the trivial eigenvalue \(1\); a convention that counts positive first-return times instead adds a constant \(1\), without changing the optimizer. The claim does not concern nonsymmetric or nonuniform-stationary chains, unequal arms, or fastest-mixing spectral radius.

## Proof

**1. Tree resistance identity and unrestricted uniqueness.** Write \(P=I-L_w\), with \(w_e\) the nonnegative edge transition probability and each vertex constraint \(\sum_{e\ni v}w_e\le1\). For positive edge probabilities, Kirchhoff's identity gives
\[
\mathcal K(P)=\operatorname{tr}(L_w^+)=\frac1N\sum_{\{x,y\}}R_w(x,y)=\frac1N\sum_{e\in E(S_{k,L})}\frac{s_e(N-s_e)}{w_e},
\]
where \(s_e\) is either component size after deleting the tree edge \(e\). The last equality follows because tree effective resistance is the sum of reciprocal edge conductances along the unique path, and an edge separates exactly \(s_e(N-s_e)\) unordered pairs. Each coefficient is positive, so the objective is **strictly convex** in the individual positive edge weights. A disconnected edge configuration has infinite cost; a positive feasible configuration exists. Thus the unrestricted optimum exists and is unique. Every permutation of the arms fixes the unique optimum, so it has depth probabilities \(w_j\). The exact reduced program, after deleting the positive factor \(k/N\), is
\[
\min\sum_{j=1}^{L}\frac{c_j}{w_j}
\quad\text{subject to}\quad
 k w_1\le1,\quad w_j+w_{j+1}\le1\ (1\le j<L),\quad 0<w_j\le1.
\]
Here the depth-\(j\) edge separates \(L-j+1\) vertices from the remaining \((k-1)L+j\) vertices.

**2. Candidate feasibility.** For \(2\le j\le L\), the coefficients \(c_j=(L-j+1)((k-1)L+j)\) strictly decrease with \(j\) and have constant negative second difference \(-2\). When \(L\) is odd, pairing \(c_{2i}\) with \(c_{2i+1}\) shows \(c_{2i}<2c_{2i+1}\), so \(E<2O\). For even \(L\ge4\), strict concavity gives \(c_2+c_4<2c_3\), while every subsequent even term \(c_{2i}\), \(i\ge3\), is smaller than the preceding odd term \(c_{2i-1}\); hence again \(E<2O\). Therefore
\[
 0<u<\frac{\sqrt2}{1+\sqrt2}<\frac23,
 \qquad \frac1k+u<1\quad(k\ge3).
\]
The root constraint is tight, the constraint at the first interior junction is strictly slack, and the consecutive constraints at depths \(j\ge2\) are tight. All edge weights lie strictly between zero and one.

**3. Exact KKT multiplier certificate.** Denote \(T=(\sqrt E+\sqrt O)^2\). For \(2\le j<L\), define
\[
 E_j=\sum_{\substack{2\le t\le j\\t\text{ even}}}c_t,
 \qquad O_j=\sum_{\substack{3\le t\le j\\t\text{ odd}}}c_t,
\]
and assign the nonnegative multipliers of \(w_j+w_{j+1}\le1\) as
\[
 \eta_j=\begin{cases}
 T(E_j/E-O_j/O),&j\text{ even},\\
 T(O_j/O-E_j/E),&j\text{ odd}.
 \end{cases}
\]
Set \(\eta_1=0\). The root multiplier for \(kw_1\le1\) is \(kc_1>0\). To show every displayed \(\eta_j\) is strictly positive, write \(e_i=c_{2i}\), \(o_i=c_{2i+1}\). For even \(j=2h<L\), the coefficient sequence is strictly decreasing: \(\sum_{i\le h}e_i>\sum_{i<h}o_i\) while \(\sum_{i>h}e_i<\sum_{i\ge h}o_i\). Cross-multiplication gives \(E_j/E>O_j/O\). For odd \(j=2h+1<L\), the pair ratios
\[
\frac{e_i}{o_i}=\frac{L-2i+1}{L-2i}\frac{(k-1)L+2i}{(k-1)L+2i+1}
\]
are strictly increasing with \(i\). Thus the ratio of the first \(h\) even/odd pair sums is strictly less than the full ratio \(E/O\); for even \(L\), the additional final even term only strengthens this inequality. Hence \(O_j/O>E_j/E\). The multipliers are strictly positive.

Because \(E/u^2=O/(1-u)^2=T\), these multipliers satisfy the full stationarity recurrence
\[
 \frac{c_j}{w_j^2}=\eta_{j-1}+\eta_j\quad(2\le j<L),
 \qquad \frac{c_L}{w_L^2}=\eta_{L-1},
\]
where the last identity follows from the equality of the total even and odd scaled sums. At \(j=1\), stationarity is \(c_1/w_1^2=k(kc_1)\). Every complementary-slackness condition holds; unused individual positivity and leaf-cap constraints have zero multipliers. The convex KKT theorem therefore proves global optimality. Strict convexity from step 1 proves uniqueness among fully asymmetric walks, not just the reduced symmetric class.

**4. Evaluation and large-arm-length limit.** Substituting the weights into the tree-resistance identity gives the stated minimum. The total nonroot coefficient sum is exactly
\[
 E+O=\sum_{j=2}^L c_j=\frac{L(L-1)((3k-2)L+4)}6.
\]
The alternating difference \(E-O\) is \(O_k(L^2)\), whereas \(E+O\) is asymptotic to \((3k-2)L^3/6\). Therefore \(u\to1/2\), \((\sqrt E+\sqrt O)^2=2(E+O)+O_k(L)\), and the asserted limit for \(\mathcal K_*\) follows. For the equal-edge walk, every allowed tree edge has probability \(1/k\), so
\[
\mathcal K(P_{\rm uniform})=\frac{k^2}{kL+1}\sum_{j=1}^L c_j
=\frac{k^2L(L+1)((3k-2)L+2)}{6(kL+1)}
\sim\frac{k(3k-2)}6L^2.
\]
The ratio of the leading coefficients is \(k/2\).

## Verification

Run `python3 verify.py` from a directory containing the packaged checker. It tests \(5{,}684\) exact-integer parameter pairs, including all candidate multiplier signs and the first-junction feasibility bound, and compares graph-eigenvalue spectral sums against the closed formula in \(60\) small instances (NumPy required for the spectral part). Recorded execution: `PASS: 5684 exact-inequality parameter pairs; 60 spectral comparator cases.` These tests are finite diagnostics; the all-size proof is the convexity and KKT argument above.

## Relationship to prior work

The Kemeny optimization problem for a prescribed graph and stationary distribution is developed by Agharkar, Patel and Bullo (2014) and Patel, Agharkar and Bullo (2015), with a general convex/semidefinite formulation. Their formulation does not itself identify the depth-one slack junction, exact alternating probabilities or large-degree penalty on the entire equal-arm-spider family. Hunter (2012) provides background on Kemeny's constant. Kirkland and Zeng (2016) develop tree formulas and investigate adding edges under ordinary random walks, rather than optimizing every symmetric transition probability under vertex stochasticity constraints. Zeng (2021; revised in 2026) studies weight-multiset-constrained tree rearrangements for degree-normalized walks; its fixed-weight-multiset and varying-stationary-law setting is different. Fixed-length spider fastest-mixing results concern spectral radius, not this inverse spectral sum.

## Limitations

The result assumes uniform stationary mass, arm symmetry only as an *output* of unrestricted uniqueness, exact equal arm length, and the non-return Kemeny convention. No claim is made for variable-stationary or directed chains, cost-weighted travel times, arbitrary arm-length mixtures, or the Kemeny constant of the naturally degree-normalized walk. The exact formulas do not imply universal optimality of this design for spectral mixing speed. The available literature comparison is not a proof of publication priority, and an unindexed equivalent special-case treatment could exist.

## References

1. J. J. Hunter, *The Role of Kemeny's Constant in Properties of Markov Chains*, arXiv:1208.4716, first submitted 2012-08-23. https://arxiv.org/abs/1208.4716
2. P. Agharkar, R. Patel and F. Bullo, *Robotic surveillance and Markov chains with minimal first passage time*, IEEE Conference on Decision and Control (2014). https://motion.me.ucsb.edu/pdf/2014b-apb-conference.pdf
3. R. Patel, P. Agharkar and F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control 60 (2015), 3156–3167. https://motion.me.ucsb.edu/pdf/2014b-pab.pdf
4. S. Kirkland and Z. Zeng, *Kemeny's Constant and an Analogue of Braess' Paradox for Trees*, Electronic Journal of Linear Algebra 31 (2016), 444–464. https://doi.org/10.13001/1081-3810.3222
5. J. Zeng, *On average hitting time and Kemeny's constant for weighted trees*, originally arXiv:2109.09249 (2021), revised in 2026. https://arxiv.org/abs/2109.09249
