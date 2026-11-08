# Sharp last-entry mass in a rotating majority-feedback ring

## Finding
For every integer \(n\ge3\), consider the binary feedback map \(F_n:\{0,1\}^n\to\{0,1\}^n\) defined by
\[
F_n(x)_0=\operatorname{maj}(x_{n-2},x_{n-1},x_0),\qquad
F_n(x)_i=x_{i-1}\quad(1\le i<n),
\]
where \(\operatorname{maj}\) returns one exactly when at least two inputs are one. Put \(\mathcal A_n=\{x: x_{i-1}=x_i\text{ or }x_i=x_{i+1}\text{ for every }i\in\mathbb Z/n\mathbb Z\}\). These are exactly the circular binary words without isolated bits.

**Theorem.** The periodic configurations of \(F_n\) are precisely \(\mathcal A_n\). Every initial configuration first enters \(\mathcal A_n\) at some time \(\tau\le n\), and the last possible entrance time \(n\) is attained by exactly
\[
E_n=\#\{x:\tau(x)=n\}=\begin{cases}
(2^{n-2}+2)/3,&n\text{ even},\\
(2^{n-2}+4)/3,&n\text{ odd}.
\end{cases}
\]
In particular, for uniformly random initial configurations, \(\Pr(\tau=n)=E_n/2^n\to1/12\). The periodic-state population, useful for identifying the target set, is
\[
\lvert\mathcal A_n\rvert=L_n+2\cos(\pi n/3),
\]
where \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\) are Lucas numbers. On \(\mathcal A_n\), the map is cyclic right rotation. For any divisor \(d\mid n\), the number of primitive \(d\)-cycles is
\[
\frac1d\sum_{e\mid d}\mu(d/e)\left(L_e+2\cos(\pi e/3)\right).
\]
The exact last-entry population \(E_n\), rather than the known prohibition of singleton runs, is the principal contribution.

## Assumptions and scope
The state space consists of length-\(n\) binary words with indices modulo \(n\), and each application of \(F_n\) is counted as one clock tick. The feedback gate has three *distinct* inputs because \(n\ge3\). No random updates, noise, or asynchronous scheduling are present. The first entrance time is \(\tau(x)=\min\{t\ge0:F_n^t(x)\in\mathcal A_n\}\). Periodic means \(F_n^p(x)=x\) for some integer \(p\ge1\); a transient word is not necessarily one with a strictly decreasing disagreement count at *every* clock tick. Cyclic permutations are counted as different labelled states.

## Proof
Write \(R\) for right rotation and \(M\) for the operation that replaces the last bit of a circular word by the majority of it and its two neighbors, leaving all other bits unchanged. By direct comparison of coordinates, \(F_n=R\circ M\). In the rotating reference frame, successive ticks act on the original sites in order \(n-1,n-2,\ldots,0\), updating each exactly once in one period of \(n\) clocks.

Let \(D(x)=\#\{i:x_i\ne x_{i+1}\}\) count disagreeing circular edges. If a site is not isolated, its three-bit majority equals its current bit, so its update changes nothing. If isolated, its two neighbors agree and disagree with it; flipping removes the two disagreement edges incident to that site, decreases \(D\) by two, and cannot create any new isolated site (its neighbors gain, not lose, an agreeing neighbor). Therefore each site's isolation can only disappear during a sweep, and after its own update it remains nonisolated. By the end of the first sweep every site is nonisolated. Hence \(F_n^n(x)\in\mathcal A_n\) for every word \(x\).

On \(\mathcal A_n\), no local majority update changes a bit, hence \(F_n=R\), making every configuration there periodic with period dividing \(n\). Conversely, if a configuration outside \(\mathcal A_n\) were periodic, the eventual periodic orbit would contain an isolated site at some time; its mandatory update during a full sweep would strictly decrease the rotation-invariant \(D\), contradicting periodicity. Thus these are exactly the periodic configurations.

For the sharp last-entrance count, after \(n-1\) ticks every original site except site \(0\) has been visited and is nonisolated, so \(\tau=n\) exactly when original site \(0\) is still isolated. Complement symmetry permits setting its original bit \(a_0=0\), with a factor of two at the end. At this last visit its neighbors both must equal \(1\). In particular \(a_1=a_{n-2}=a_{n-1}=1\): the last two original sites were adjacent 1s and therefore never changed, while site \(1\) must be one. Conversely these endpoint requirements and one condition below suffice.

Put \(m=n-2\) and write the interior word as \(a_1\ldots a_m\), with \(a_1=a_m=1\). Let \(b_i\) denote the value of original site \(i\) after the descending sweep. First \(b_{n-1}=1\), and for \(2\le i\le n-2\),
\[
b_i=\operatorname{maj}(a_{i-1},a_i,b_{i+1})=\begin{cases}
a_i,&a_{i-1}=a_i,\\ b_{i+1},&a_{i-1}\ne a_i.
\end{cases}
\]
The final site \(1\) remains \(b_1=b_2\) because \(a_0=0,a_1=1\). Consequently site \(0\) is isolated just before its update if and only if the *rightmost* equal adjacent pair in \(a_1\ldots a_m\), if it exists, is \(11\); otherwise the fully alternating interior must have odd length and the incoming value is also one. If the rightmost equal pair is at indices \(i,i+1\), then the alternating suffix ending in \(a_m=1\) forces \(m-i-1\) even. With that parity, the pair is \(11\), and the interior prefix has \(2^{\max(0,i-2)}\) choices. A completely alternating interior contributes one further possibility exactly when \(m\) is odd. Therefore the number for fixed \(a_0\) is
\[
\sum_{\substack{1\le i<m\\ m-i-1\text{ even}}}2^{\max(0,i-2)}+\mathbf1_{m\text{ odd}}
=\begin{cases}(2^m+2)/6,&m\text{ even},\\(2^m+4)/6,&m\text{ odd}.
\end{cases}
\]
Multiplication by two yields the stated \(E_n\). The formula also holds at \(n=3\) by directly reading the unique one-letter interior. Since \(E_n>0\), the bound \(n\) is sharp, and division by \(2^n\) gives the limit \(1/12\).

Finally a length-\(n\) circular word is in \(\mathcal A_n\) exactly if every adjacent-pair transition \((a,b)\to(b,c)\) obeys \(a=b\) or \(b=c\). In the order \(00,01,10,11\), the transfer matrix is
\[
T=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
Its characteristic polynomial is \((\lambda^2-\lambda-1)(\lambda^2-\lambda+1)\). The trace \(\operatorname{tr}(T^n)\) counts circular admissible words and equals \(L_n+2\cos(\pi n/3)\). Since \(F_n\) rotates these words, standard Möbius inversion from fixed rotations yields the displayed primitive-cycle formula.

## Verification
The standalone Python programs `check_dynamics.py` and `check_transfer.py` use only the standard library. The former exhaustively verifies all \(32{,}760\) labelled states for \(3\le n\le14\), including actual first entrance and primitive orbit counts; the latter checks the exact transfer trace and Möbius cycle formulas for \(1\le n\le100\), and independently counts rightmost-equal-pair possibilities for \(3\le n\le16\). The exact matrix characteristic polynomial can also be verified by direct determinant expansion. These finite tests corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work
Tošić and Agha (2004) explicitly characterize fixed configurations of ordinary sequential radius-one majority automata by exclusion of isolated bits, and prove that such update sequences do not have nontrivial cycles without relabelling. Our feedback map instead includes a deterministic spatial rotation each tick, so its nontrivial clock-periodic orbits are rotations of the old stable configurations; their fixed-state criterion is not claimed as new. The new aspect is the *exact population of initial configurations attaining the sharp last entry time*, \(E_n\), in the particular rotating feedback clock, along with the induced orbit census. Tošić's later enumeration-complexity paper addresses arbitrary sparse network automata, rather than this exact finite-time count. The classical general period-two theory for parallel graph majority is different from this rotating feedback update. Some adjacent variants of majority dynamics and majority-gate feedback registers are not fully indexed; historic priority remains provisional.

## Limitations
The result does not give the full distribution of all earlier entrance times \(0\le\tau<n\), exact basin sizes of individual rotational cycles, or a stochastic robustness law. The classification is for the specified three-tap positive majority feedback, not arbitrary Boolean taps or arbitrary update permutations. The formula for admissible periodic words overlaps a classical stable-pattern characterization and should not be interpreted as independent novelty. The exact last-entry population has been verified within the inspected accessible sources, but historical uniqueness has not been independently certified.

## References
- P. T. Tošić and G. A. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004. https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf
- P. T. Tošić, *On the complexity of enumerating possible dynamics of sparsely connected Boolean network automata with simple update rules*, DMTCS Proceedings AL, pp. 125–144 (publisher records publication 2009-12-31; proceedings identify 2010). https://dmtcs.episciences.org/articles/2757 and https://dmtcs.episciences.org/en/articles/2757/download
- I. Benjamini et al., *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (2014). https://arxiv.org/abs/1405.2486
