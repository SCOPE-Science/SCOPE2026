# The octahedral high-adhesion mixing law for four-card cut-first riffles

## Finding

Consider the card-weighted, block-weighted, and midpoint-interpolation cut-first adhesive riffle shuffles of Jiang [1] on a labelled deck of four cards. Write their contact-survival probability as \(p=1-q\), where \(q\downarrow0\), and start from any fixed deck order. Let \(d_{F,q}(m)\) denote total-variation distance after \(m\) shuffles from the uniform distribution on the 24 deck orders, for \(F\in\{C,B,I\}\).

**Theorem.** For every fixed real \(t>0\),
\[
\lim_{q\downarrow0}d_{F,q}(\lfloor t/q\rfloor)
=\frac12 e^{-4a_Ft}+\frac13 e^{-6a_Ft},
\qquad
(a_C,a_B,a_I)=\left(\frac9{64},\frac7{48},\frac7{16}\right).
\]
The convergence of the full 24-state probability law is in total variation, to the lift of a six-state continuous-time Markov law that is uniform within each cyclic-rotation class. The six-state generator is \(Q_F=a_F(A_{\mathrm{oct}}-4I)\), where \(A_{\mathrm{oct}}\) is the adjacency matrix of the octahedron (a complete graph on six vertices with three disjoint opposite pairs removed).

For every \(0<\varepsilon<5/6\), letting \(m_{F,q}(\varepsilon)\) be the least integer with \(d_{F,q}(m)\le\varepsilon\),
\[
\lim_{q\downarrow0}q\,m_{F,q}(\varepsilon)
=\frac{s_\varepsilon}{a_F},
\]
where \(s_\varepsilon>0\) is the unique solution to \(\frac12e^{-4s}+\frac13e^{-6s}=\varepsilon\). In particular the block-weighted rule's high-adhesion time constant divided by the midpoint rule's is exactly \(3\); the card-weighted to midpoint time-constant ratio is \(28/9\).

## Assumptions and scope

Each round independently chooses a cut of size \(K\sim\mathrm{Bin}(4,1/2)\). An empty cut does nothing. Each of the two internal packet gaps is independently broken with probability \(q\), producing contiguous, internally ordered blocks. The next block is selected from the two packet heads by one of the following rules: \(C\), proportional to remaining **card** counts, updating after an entire block is released; \(B\), proportional to remaining **block** counts; \(I\), increasing block midpoint key \((a+b-1)/(2m)\) for a block occupying positions \(a,\ldots,b\) of a packet of length \(m\), with independent fair tie-breaking. The full description and physical interpretation are in [1, Section 2.1]. All new random choices are independent across rounds. The theorem addresses fixed deck size four, \(q\to0\), and fixed positive rescaled time; it does not treat the correlated-label inverse-riffle family.

A **cyclic class** consists of the four cyclic rotations of a deck order. There are six such classes, corresponding to the six oriented circular orders of the four labels; two classes are called opposite if their orientations are reversed. Every class has one opposite class and four other classes.

## Proof

**1. Fast rotation and rare perturbations.** Let \(P_F(q)\) be the stochastic matrix on the 24 orders. Conditional on a nonempty cut there are exactly two potentially broken gaps, so every matrix entry is a polynomial in \(q\) of degree at most two. Write \(P_F(q)=P_F(0)+qR_F+O(q^2)\) entrywise. At \(q=0\), a round releases two intact packets in either order: the resulting deck is always a cyclic rotation. All four rotations have positive transition probability (empty cuts give a positive holding probability). Thus \(P_F(0)\) is aperiodic and irreducible within every four-element cyclic class. Because the rule is label-independent, every \(P_F(q)\) is doubly stochastic. Consequently the unique equilibrium of each \(P_F(0)\)-class is uniform over its four orders, and every other eigenmode of \(P_F(0)\) has modulus strictly below one.

**2. First-order escape mass.** Exactly one broken bond contributes at order \(q\) to changes of cyclic class; events with two broken bonds are \(O(q^2)\). For \(K=1\) or \(K=3\), the large packet has three cards, and its bond break can occur in either of two places. The small packet's singleton is placed between the two resulting blocks with conditional probabilities \((1/4,3/8)\) for \(C\), \((1/3,1/3)\) for \(B\), and \((1,1)\) for \(I\). The binomial cut weight is \(4/16\) for either such cut. For \(K=2\), one of the two size-two packets breaks into singletons, and the other intact packet lies between them with conditional probabilities \(1/3\) for \(C\), \(1/3\) for \(B\), and \(1\) for \(I\). The cut weight is \(6/16\). Therefore the coefficients of \(q\) in total departure probability from the initial cyclic class, grouped by cut \(K=1,2,3\), are respectively
\[
C:\ (5/32,1/4,5/32),\qquad
B:\ (1/6,1/4,1/6),\qquad
I:\ (1/2,3/4,1/2).
\]
Their sums are \(r_C=9/16\), \(r_B=7/12\), and \(r_I=7/4\). These quantities are coefficients, not probabilities at positive \(q\), so a coefficient greater than one is unobjectionable.

The first-order three-block interleavings preserve the internal order of an intact packet containing at least two cards; inspecting the two patterns \((1,3)\) and \((2,2)\) of packet sizes shows that their non-rotational output is never the reverse circular orientation. Thus no one-break event moves a cyclic class to its opposite class. Relabelling the four distinct card names maps every possible starting cyclic class and shuffle transition equivariantly to another. Under this \(S_4\)-action, all twelve unordered pairs of distinct, nonopposite cyclic classes form one orbit. The averaged first-order rate to each of the four accessible other classes must therefore be \(r_F/4\). This yields \(a_C=9/64\), \(a_B=7/48\), \(a_I=7/16\), and the asserted octahedral generator.

**3. Singular-time Markov limit.** Let \(\Pi\) be the projection averaging a probability measure uniformly within each cyclic class. Then \(\Pi P_F(0)=P_F(0)\Pi=\Pi\). On the complementary finite-dimensional subspace, \(P_F(0)\) has spectral radius \(\rho_F<1\). For row-vector probabilities, write \(\mu_k=x_k+y_k\), where \(x_k=\mu_k\Pi\) and \(y_k=\mu_k(I-\Pi)\). Since \(P_F(q)=P_F(0)+O(q)\) in any fixed matrix norm, the recurrences give uniformly for \(k\le T/q\)
\[
\|y_k\|=O_F(\rho_1^k+q),\qquad
x_{k+1}=x_k+q\,x_k\Pi R_F\Pi+O_F(q^2+q\|y_k\|)
\]
for some \(\rho_F<\rho_1<1\), after replacing the norm by an equivalent contraction norm on the complementary invariant subspace. Summing the error in the second recurrence up to \(T/q\) gives \(O_F(q)\). Euler convergence therefore yields, for each \(t>0\),
\[
\mu_{\lfloor t/q\rfloor}\ \longrightarrow\
(\mu_0\Pi)e^{t\Pi R_F\Pi},
\]
where the exponential acts on the class-constant subspace; the convergence is uniform for \(t\) in compact subsets of \((0,\infty)\). Identifying the six class masses gives \(e^{tQ_F}\). The uniform distribution on 24 states projects to uniform mass \(1/6\) per class, and taking total variation is unchanged by lifting a six-class distribution uniformly to the 24 states.

**4. Exact profile.** Let \(A=e^{-4a_Ft}\) and \(B=e^{-6a_Ft}\). The octahedral generator has eigenvalues \(0\) (multiplicity one), \(-4a_F\) (multiplicity three), and \(-6a_F\) (multiplicity two), as follows by splitting vectors into opposite-pair antisymmetric modes and opposite-pair symmetric, total-zero modes. Starting at one class, the six probabilities at time \(t\) are
\[
\begin{array}{ll}
1/6+A/2+B/3,&\text{initial class};\\
1/6-A/2+B/3,&\text{opposite class};\\
1/6-B/6,&\text{each of the other four classes}.
\end{array}
\]
Since \(A\ge B>0\), their total-variation distance from \(1/6\) is exactly \(A/2+B/3\). The function is continuous and strictly decreases from \(5/6\) (as \(t\downarrow0\)) to zero. Finite-state Markov contraction makes \(d_{F,q}(m)\) nonincreasing in \(m\). Pointwise limits on both sides of the unique threshold \(s_\varepsilon/a_F\) imply the claimed mixing-time asymptotic for \(0<\varepsilon<5/6\). The rate ratios follow by dividing the exact constants.

## Verification

The standalone standard-library file `verification/check_four_card.py` constructs the exact one-round kernels on all 24 permutations by enumerating five cuts, every internal-gap bond mask, and every permitted weighted or midpoint block merge. It independently constructs the first-order one-break quotient and checks all 36 entries of each six-state generator against the octahedron formula. It further checks exact rational stochasticity and nonnegativity at three adhesion values per shuffle family, and full state-level rotational support at \(q=0\). Running `python3 verification/check_four_card.py` gives 7,471 exact-rational assertions and 18 finite-\(q\) total-variation comparisons for \(q\in\{1/50,1/100\}\) and rescaled times \(t\in\{1/2,2,4\}\). These experiments are finite diagnostics; the infinite limiting statement is proved in Steps 1–4, not inferred from experiments.

## Relationship to prior work

Jiang [1, Definitions 2.1–2.3 and Theorem 10.1] specifies the three precise models and establishes a fixed-deck \(\Theta((1-p)^{-1})\) mixing-time divergence, using one-break insertions and rotations to derive a bound. Its Section 12 presents numerical mixing times at selected finite adhesion values; it does not derive the six-class limiting generator, three distinct exact rates, the two-exponential total-variation profile, or the sharp threshold constant. Those statements require the model-specific exhaustive one-break accounting and the singular perturbation limit above. Jonasson and Morris [2] study a *different* Markovian binary-label/clumpy shuffle, for which the cut law is not the fixed binomial cut used here, and establish a large-deck mixing upper bound. Sellke, Shi, and Wang [3] study non-adhesive GSR riffles with general pile-size laws, retaining conditionally uniform individual-card interleaving; their cutoff theorem is not an exact strong-adhesion profile for these three cut-first models.

## Limitations

This is a fixed-four-card, \(p\uparrow1\) theorem, not a claim about growing decks, a sharp finite-\(p\) cutoff, or the correlated-label family. The formula holds at strictly positive rescaled times; at exactly zero shuffles, the full-deck distance is \(23/24\), whereas the limiting fast-rotation boundary value at \(t\downarrow0\) is \(5/6\). The mixing-time limit is stated only for \(0<\varepsilon<5/6\); larger tolerance thresholds may occur during the initial fast-rotation layer. The computational checker does not certify the asymptotic perturbation lemma independently. An independent mathematical assessment has not been performed, and the prior-art examination is not an exhaustive historical-priority guarantee.

## References

[1] Y. Jiang, *Adhesive riffle shuffles: simple one-parameter models, interpolation, and parameter-dependent mixing bounds*, arXiv:2611.02092v1, first public 2026-11-01, https://arxiv.org/html/2611.02092v1 (Definitions 2.1–2.3; Sections 10, 12, and 13).

[2] J. Jonasson and B. Morris, *Rapid mixing of dealer shuffles and clumpy shuffles*, Electronic Communications in Probability **20** (2015), article 20, https://doi.org/10.1214/ECP.v20-3682.

[3] M. Sellke, J. Shi, and J. Wang, *Universality of Cutoff for Riffle Shuffling*, arXiv:2510.22783, first public 2025-10-26, https://arxiv.org/abs/2510.22783.
