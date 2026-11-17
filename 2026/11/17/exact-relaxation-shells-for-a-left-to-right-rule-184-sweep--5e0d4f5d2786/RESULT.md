# Exact relaxation shells for a left-to-right Rule 184 sweep

## Finding

Let \(F_n\) be the in-place elementary Rule 184 update of the labelled binary ring \(x_0,\ldots,x_{n-1}\), visiting sites \(0,1,\ldots,n-1\) once per sweep, for every integer \(n\ge3\). Let \(\tau(x)\) be the first number of complete sweeps after which the configuration is periodic (necessarily fixed). For integer \(t\ge0\), write \(G_t(z)=\sum_{n\ge1}N_{n,\le t}z^n\), where \(N_{n,\le t}\) is the number of length-\(n\) inputs with \(\tau\le t\) under this same rule. Only coefficients with \(n\ge3\) are asserted for the usual distinct-neighbor cycle.

Define \(Z=z/(1-z)\) and, for \(t\ge1\),
\[
A_t=\sum_{j=1}^t z^j,\qquad B_t=\sum_{j=2}^{t+1}(j-1)z^j,\qquad S_t=\sum_{j=3}^{t+1}\binom{j-1}{2}z^j.
\]
Then the complete first-entry census has the rational generating function
\[
\boxed{G_0(z)=\frac{2z}{1-z},\qquad G_t(z)=\frac{2z}{1-z}+Z^2+\frac{Z\,[A_t(1+Z)+B_t+S_t]}{1-A_t Z}\quad(t\ge1).}
\]
The number entering a fixed point at exactly time \(t\) is \([z^n](G_t-G_{t-1})\) for \(t\ge1\), and is \(2\) for \(t=0\). Every configuration becomes fixed by sweep \(n-1\); the unique state with \(\tau=n-1\) is \((1,\ldots,1,0)\) in scan order. The basin of \(1^n\) consists precisely of \(1^n\) and the \(n-1\) states \(0^a1^{n-a}\), \(1\le a<n\); its size is exactly \(n\), and the basin of \(0^n\) has size \(2^n-n\). For independent fair initial bits, \(\mathbb E\tau=\log_2 n+O(1)\).

## Assumptions and scope

Rule 184 is \(f(\ell,c,r)=r\) when \(c=1\) and \(f(\ell,c,r)=\ell\) when \(c=0\). The sweep is sequential, *not* the standard simultaneous particle-conserving traffic map. Site \(0\) uses the old value of site \(n-1\), and the last site uses the already updated value of site \(0\). Words and runs below are read in increasing scan index; all symbols are literal labelled bits. The conclusions concern exact full-sweep first entry, not the individual-site substeps or arbitrary update permutations.

## Proof

**One-sweep boundary and erosion lemma.** Let \(y=F_n(x)\). Direct substitution in the local rule yields
\[
 y_0=\begin{cases}x_{n-1}&x_0=0,\\x_1&x_0=1,\end{cases}\quad
 y_i=\begin{cases}y_{i-1}&x_i=0,\\x_{i+1}&x_i=1\end{cases}\ (1\le i\le n-2),\quad
 y_{n-1}=\begin{cases}y_{n-2}&x_{n-1}=0,\\y_0&x_{n-1}=1.\end{cases}
\]
If \(x_{n-1}=0\), the last consecutive zero block copies the zero produced at the immediately preceding end of a one block (or copies zero from the beginning if there are no ones), so \(y_{n-1}=0\). If \(x_{n-1}=1\), then \(y_{n-1}=y_0\). Thus every output lies in the forward-invariant set \(\{y:y_{n-1}\le y_0\}\). On this set, every one block not containing an endpoint loses its final one at each sweep. A leading one block similarly shortens. If there are leading and trailing one blocks, of lengths \(a,b\ge1\) separated by a zero, the trailing block retains its length until the leading block disappears, when its rightmost one disappears too; the remaining \(b-1\) ones then erode. Its extinction clock is \(a+b-1\). Every other one block erodes independently at unit speed.

**Closed clock for arbitrary input.** The uniform words have \(\tau=0\). For a nonuniform word with no boundary pattern \((x_0,x_{n-1})=(0,1)\), if the endpoints are both one, \(\tau\) is the maximum of \(a+b-1\) for its leading/trailing one blocks and the lengths of all strictly internal one blocks; otherwise it is the maximum length of every one block. If the endpoints are \((0,1)\), express the input as alternating positive zero and one blocks, with an initial zero block of length \(a\), first one block length \(b\), and final one block length \(d\). If there is only one one block, the first sweep fills the entire word and \(\tau=1\). If there are at least two one blocks, the first sweep turns the initial zero block and all but the last cell of the first one block into a leading one block of length \(a+b-1\), retains the final one block of length \(d\), and erodes every intermediate one block by one. Consequently
\[
\tau=\max\left(a+b+d-1,\ \max\{c:\ c\text{ is the length of an intermediate one block}\}\right).
\]
Empty inner maxima are ignored. These formulas prove convergence directly, and distinguish both basins: every state with the endpoint pattern \((0,1)\) and just one one block reaches \(1^n\) in one sweep, while every other mixed state erodes to \(0^n\). No nontrivial periodic orbit is possible.

**Enumerating all first-entry layers.** For \(t\ge1\), the ordinary positive zero-block and length-at-most-\(t\) one-block generating functions are \(Z\) and \(A_t\). Starting and ending in zero gives \(ZA_tZ/(1-A_tZ)\); starting in one and ending in zero gives \(A_tZ/(1-A_tZ)\). Starting in one and ending in one, with at least one separating zero, requires the sum of the two endpoint-one lengths to be at most \(t+1\), and every intermediate one block to have length at most \(t\); it contributes \(B_tZ/(1-A_tZ)\). Starting in zero and ending in one, the states with a single one block contribute \(Z^2\), and states with at least two one blocks require the sum of the initial zero, first one, and last one lengths to be at most \(t+1\), with all intermediate one blocks bounded by \(t\). Ordered positive triples of sum \(j\) number \(\binom{j-1}{2}\), giving \(S_tZ/(1-A_tZ)\). The two uniform words contribute \(2z/(1-z)\). Summing gives the displayed exact rational expression. In particular coefficient subtraction gives every first-entry population without constructing a state transition graph.

**Sharp extremum and typical clock.** In the endpoint cases \((0,0)\), \((1,1)\), and \((0,1)\), respectively, the clock is at most \(n-2\), \(n-2\), and \(n-2\), except single-block \((0,1)\) words which enter in one sweep. The case \((1,0)\) has clock at most \(n-1\), with equality only for the solitary length-\(n-1\) one block followed by the final zero. For the expectation, let \(M_n\) be the longest noncyclic run of ones in a fair random word. Except for the \(n-1\) exceptional nonuniform inputs entering \(1^n\), the closed clock shows \(M_n\le\tau\le M_n+a+b+d\), where \(a,b,d\) are at most three terminal or first-run lengths having uniformly bounded expectations. Standard first-moment bounds give \(\Pr(M_n\ge k)\le n2^{-k}\). Conversely, count occurrences of \(01^k\) beginning after the left endpoint; their number has mean \((n-k)2^{-(k+1)}\) and variance no larger than its mean, since overlapping occurrences are mutually exclusive and disjoint ones are independent. Chebyshev's inequality and geometric summation show \(\mathbb E M_n=\log_2 n+O(1)\). The exceptional inputs contribute only \(O(n^2 2^{-n})\) to the expectation comparison, proving the assertion.

## Verification

The standalone standard-library programs `check_direct.py` and `check_census.py` are included with the evidence package. The first implements the local in-place sweep independently of the closed run clock and compares every input for each ring length from \(3\) through \(16\), a total of \(131064\) labelled configurations; it also checks basin sizes, the sharp bound and uniqueness. The second expands the rational generating functions by integer polynomial arithmetic, compares all first-entry shell coefficients against independent trajectory simulation for lengths \(3\) through \(14\), and confirms all \(102\) shell coefficients and total population counts. Their exact terminal records are retained in `direct_output.txt` and `census_output.txt`. Exhaustive finite checks supplement, but are not substituted for, the all-length proof above.

## Relationship to prior work

Wolfram's 1983 treatment introduces elementary cellular automata; standard simultaneous Rule 184 conserves particle number and has traveling patterns. Macauley, McCammond and Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360 (first public version 2007, revised 2011), prove that Rule 184 has only the two uniform periodic configurations under every simple sequential order (Proposition 6.3), but do not give the first-entry layer generating functions or a clock for this fixed scan. Donoso-Leiva, Goles, Ríos-Wilson and Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, arXiv:2509.07797 (2025), include Rule 184 among rules converging under all sequential update orders; their classification likewise does not supply these distributions. The distinct synchronous Rule-184 Catalan traffic-relaxation enumerations do not imply this sequential, nonconserving result. Previous one-sweep image enumerations for sequential Rule 184 concern the output set at one sweep, not the first time to reach a fixed point. The present contribution is the exact all-depth rational census, sharp unique extremizer, strongly asymmetric basins, and logarithmic typical clock for a fixed scan.

## Limitations

The result fixes one directional permutation and cannot be asserted for arbitrary scan permutations or the simultaneous rule. The formal series coefficients for \(n=1,2\) are bookkeeping extensions, not claims about distinct-neighbor cycles. The asymptotic expectation statement has bounded but unspecified additive error. Historical priority is conditional on the inspected sources; possible unindexed results or inaccessible papers have not been conclusively ruled out. No independent mathematical review has been carried out.

## References

1. S. Wolfram, "Statistical mechanics of cellular automata," *Reviews of Modern Physics* **55** (1983), 601–644, published 1983-07-01, https://doi.org/10.1103/RevModPhys.55.601.
2. M. Macauley, J. McCammond and H. S. Mortveit, "Order Independence in Asynchronous Cellular Automata," *Journal of Cellular Automata* **3** (2008), 37–56, https://arxiv.org/abs/0707.2360; inspected full text https://arxiv.org/html/0707.2360v2.
3. I. Donoso-Leiva, E. Goles, M. Ríos-Wilson and S. Sené, "On the Convergence of Elementary Cellular Automata under Sequential Update Modes," 2025, https://arxiv.org/abs/2509.07797.
4. B. Sethi, S. Roy and S. Das, "Experimental study on convergence time of elementary cellular automata under asynchronous update," *AUTOMATA 2013 Exploratory Papers*, 87–96, accessible abstract https://jlupub.ub.uni-giessen.de/server/api/core/bitstreams/ea2de890-0ac3-42fc-a136-11147ddc9acb/content (random asynchronous rather than a fixed sweep).
