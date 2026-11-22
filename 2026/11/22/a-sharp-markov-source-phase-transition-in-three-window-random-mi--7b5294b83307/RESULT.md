# A sharp Markov-source phase transition in three-window random minimizer density

## Finding

Fix a width-three minimizer rule, choosing the least length-\(k\) factor in each window of three consecutive factors, with ties broken at the leftmost position. Draw the total order on binary length-\(k\) factors uniformly at random, once and for all. The binary input is a stationary Markov chain that forbids `11` and has transition probabilities \(P(0\mid0)=p\), \(P(1\mid0)=1-p\), \(P(0\mid1)=1\), for \(0<p<1\). Write \(\rho_k(p)\) for the expectation over the random order of the almost-sure limiting fraction of selected positions.

Set \(t=p(1-p)\). For \(k\ge2\), the following is an **exact** expression at every block length:

\[
\rho_k(p)=\frac12+\frac{(1+p+p^2)p^k}{6(2-p)}-\frac{T_k(p)}6,
\]

where, writing \(k=3m+r\), \(0\le r\le2\),

\[
T_k(p)=\begin{cases}
\dfrac{(1-p)(1+2p)}{2-p}\,t^m,&r=0,\\[2pt]
\dfrac{3-p}{2-p}\,t^{m+1},&r=1,\\[2pt]
t^{m+1},&r=2.
\end{cases}
\]

At the boundary \(k=1\), \(\rho_1(p)=\tfrac12+\tfrac{p^2}{2(2-p)}\).

Define \(\alpha=(\sqrt5-1)/2\). The signed finite-length correction to \(1/2\) has a **sharp asymptotic phase transition**:

- If \(0<p<\alpha\), then \(\rho_k(p)<1/2\) for all sufficiently large \(k\).
- If \(\alpha<p<1\), then \(\rho_k(p)>1/2\) for all sufficiently large \(k\).
- At \(p=\alpha\), the two exponential scales coincide. Writing \(\varphi=(1+\sqrt5)/2\), for every \(k\ge2\),

\[
\rho_k(\alpha)=\frac12+\varphi^{-k}\begin{cases}
\dfrac{4\sqrt5-5}{30},&k\equiv1\pmod3,\\[2pt]
\dfrac{5-\sqrt5}{20},&k\equiv0,2\pmod3.
\end{cases}
\]

In particular the maximal-entropy stationary golden-mean source is exactly the phase boundary, and its leading deviation has a persistent three-residue modulation. No assertion is made about the density of an individually chosen order equaling this order-average.

## Assumptions and scope

All input positions are indexed and the alphabet is the named binary alphabet \(\{0,1\}\). The source has stationary probabilities \(\pi_0=1/(2-p)\) and \(\pi_1=(1-p)/(2-p)\). The order is uniform among total orders on **all** binary \(k\)-mers; equivalently its restriction to legal factors is uniform. The source and order are independent. Stationarity and irreducibility of the finite-state chain ensure that for every fixed total order the limiting sampling density exists almost surely by the ergodic theorem. Averaging this limit over orders is equivalent to averaging the charged-context indicator of a stationary length-\((k+3)\) source block. The maximum-entropy stationary input on the golden-mean shift corresponds to \(p=\alpha\).

## Proof

**1. Charge identity.** Write the four consecutive \(k\)-mers in a context of length \(L=k+3\) as \(b_0,b_1,b_2,b_3\). The first window chooses among indices \(0,1,2\) and the second among \(1,2,3\); a newly sampled position appears exactly when the chosen indices differ. If all four factors are distinct, a uniform random order gives charged probability \(2/4=1/2\). More generally, if there are \(d\) different factors, the charge probability is \(2/d\) when the final factor \(b_3\) occurs only once and \(1/d\) when it is repeated. This is proved directly: the unique lowest factor has probability \(1/d\) of being the initial factor and another \(1/d\) of being the unique terminal factor, with the latter event impossible when the terminal factor repeats. This is the charged-context lemma of Golan--Shur, and follows as well from the tie rule. All nonexceptional contexts therefore contribute the baseline \(1/2\).

**2. Exhaustive structural classification of exceptional contexts.** Equal \(k\)-mers at positions differing by \(j\in\{1,2,3\}\) force a \(j\)-periodic interval of length \(k+j\). Because the source forbids `11`, the complete list for every \(k\ge2\) consists of exactly 13 distinct length-\(L\) strings, partitioned as follows.

Six strings with a long zero interval are
\[
0^L,\quad 0^{L-1}1,\quad 0^{L-2}10,\quad 010^{L-2},\quad10^{L-1},\quad10^{L-2}1.
\]
Their respective charge probabilities are \(1,1,2/3,1/3,1/2,2/3\).

Four further strings arise from alternation: the two pure alternating strings of length \(L\) and the two strings obtained by adding one extra zero at the left or right end of an alternating interior. The pure alternating strings have charge probability \(1/2\); the boundary-defect pair has charge probabilities \(1/3\) and \(2/3\). They are reversals, so have equal probabilities under the reversible stationary binary Markov law and their excess contributions cancel. This description includes the short boundary \(k=2\).

The final three strings are the length-\(L\) prefixes of the three cyclic shifts of the infinite period-three word `001001001...`. They are all legal, have exactly three different \(k\)-mers with the last repeating the first, and hence have charge probability \(1/3\). The period-one, -two, and -three cases exhaust all six possible pairs of repeated positions; forbidding `11` leaves no others. The six displayed zero strings, the four alternating variants and the three period-three strings are mutually distinct for \(k\ge2\).

**3. Markov weights.** A legal word \(v=v_1\cdots v_L\) has probability \(\pi_{v_1}p^{N_{00}(v)}(1-p)^{N_{01}(v)}\). Relative to the baseline \(1/2\), the six long-zero words together contribute exactly
\[
Z_k=\frac{(1+p+p^2)p^k}{6(2-p)}.
\]
For example, their respective probabilities are
\[
\pi_0p^{L-1},\ \pi_0p^{L-2}(1-p),\ \pi_0p^{L-3}(1-p),\ \pi_0p^{L-3}(1-p),\ \pi_0p^{L-2}(1-p),\ \pi_0p^{L-3}(1-p)^2.
\]
Multiplying by the corresponding excess charges \((1/2,1/2,1/6,-1/6,0,1/6)\), and using \(L=k+3\), gives the stated \(Z_k\). The alternating contributions cancel as above.

The sum of probabilities of the three period-three words is \(T_k(p)\). To see this directly, set \(q=1-p\), \(t=pq\) and classify the length \(L\) modulo three. The three-word probability sum for lengths \(3h,3h+1,3h+2\), respectively, is
\[
\pi_0q(1+2p)t^{h-1},\quad \pi_0(3-p)t^h,\quad t^h.
\]
Substituting \(L=k+3\) gives the displayed three cases for \(T_k\). Since each has excess charge \(-1/6\), the all-length density identity follows. At \(k=1\), enumeration of the eight legal four-letter contexts shows that exactly `0000` and `0001` have charged probability one; all others have probability \(1/2\). Their combined Markov probability is \(\pi_0p^2\), proving the boundary formula.

**4. Sharp sign transition and golden-mean resonance.** The positive correction has exponential base \(p\). In each residue class the negative contribution has exponential base \(t^{1/3}\), and its prefactor is strictly positive for \(0<p<1\). Thus the eventual sign changes exactly where \(p^3=t\), or \(p^2=1-p\), whose only solution in \((0,1)\) is \(p=\alpha\). At this point \(t=\alpha^3\). Substituting \(p=\alpha=\varphi^{-1}\), \(\alpha^2=1-\alpha\), and simplifying gives the two positive coefficients in the claimed period-three expression. This is an exact identity, not an asymptotic guess.

## Verification

The included independent standard-library script `verify.py` enumerates every admissible context of length \(k+3\) for \(1\le k\le13\), evaluates each possible ranking of its distinct \(k\)-mers, and compares the resulting Markov-weighted density to the closed form at five exact rational transition parameters. There are 6,752 distinct input contexts in that full enumeration (each checked at five parameters). Separately the script constructs all exceptional contexts by periodic overlap, proves the observed count 13 and ten nonzero correction terms for \(2\le k\le80\), and matches the rational finite-sum formula at five parameters. It also verifies the golden-mean simplification to 70-digit decimal precision for \(2\le k\le80\). All-length validity rests on the structural proof above, not the finite checks.

Run with `python3 verify.py` using only Python's standard library.

## Relationship to prior work

Golan and Shur, *Expected Density of Random Minimizers* (arXiv:2410.16968, first public 2024-10-22), establish the charged-context formula and complete all-length densities for uniformly independent full-alphabet sources. Their Theorem 3.1 yields an exponentially small correction with no periodic variation in \(k\) when the window width is fixed and does not address stationary Markov input sources. The first charge lemma is used explicitly here; the new content is the source-dependent exact weighting, its distinct period-three collision contribution, and the sharp entropy-source sign transition.

Zheng, Kingsford and Marçais, *Improved design and analysis of practical minimizers* (Bioinformatics, 2020), prove density bounds for random orders on independent uniformly random input and motivate charged contexts. Yu, *On Minimizers and Convolutional Filters: Theoretical Connections and Applications to Genome Analysis* (2024), relates random and learned ranking schemes to repetitive data but does not give the Markov-source three-window formula.

The general previously known finite-context method can of course be applied to a weighted context distribution; applying it alone does **not** state the exact parametric formula or imply the sharp sign crossover without the periodic-context classification and calculation supplied here.

## Limitations

The claim concerns width exactly three, the stationary two-state Markov family forbidding `11`, and the expectation over uniformly random global orders. It makes no statement about real genomes, nonstationary reads, optimally chosen orders, correlations between different selected positions, or concentrations of order-specific density. There is no claim that the underlying charged-context lemma is new. A mathematically equivalent earlier Markov-weighted result not located in the inspected literature remains a priority risk; independent mathematical evaluation has not been performed.

## References

1. S. Golan and A. M. Shur, *Expected Density of Random Minimizers*, arXiv:2410.16968, originally posted 2024-10-22. https://arxiv.org/abs/2410.16968
2. H. Zheng, C. Kingsford and G. Marçais, *Improved design and analysis of practical minimizers*, Bioinformatics 36 (2020), i119–i127, doi:10.1093/bioinformatics/btaa472. https://pmc.ncbi.nlm.nih.gov/articles/PMC8248892/
3. Y. W. Yu, *On Minimizers and Convolutional Filters: Theoretical Connections and Applications to Genome Analysis*, Journal of Computational Biology 31 (2024). https://doi.org/10.1089/cmb.2024.0483
