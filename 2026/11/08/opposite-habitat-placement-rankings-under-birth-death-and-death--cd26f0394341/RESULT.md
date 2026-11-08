# Opposite habitat-placement rankings under birth–death and death–birth fixation on a three-site path

## Finding

For every pair of positive mutant fecundities \(r,s>0\), put a single \(r\)-site and two \(s\)-sites on the undirected three-vertex path \(P_3\). Residents have fecundity exactly one at every vertex. Start from one mutant at a uniformly random vertex. Let \(\rho_C^{\mathrm{Bd}}\) and \(\rho_E^{\mathrm{Bd}}\) denote eventual mutant fixation probabilities when the unique \(r\)-site is respectively at the center and at an endpoint, under birth–death updating. Define \(\rho_C^{\mathrm{dB}},\rho_E^{\mathrm{dB}}\) analogously for death–birth updating.

**Theorem (complete placement reversal).** For every \(r,s>0\),
\[
\operatorname{sgn}(\rho_C^{\mathrm{Bd}}-\rho_E^{\mathrm{Bd}})=\operatorname{sgn}(r-s),
\qquad
\operatorname{sgn}(\rho_C^{\mathrm{dB}}-\rho_E^{\mathrm{dB}})=-\operatorname{sgn}(r-s).
\]
Both comparisons are strict when \(r\ne s\), and both tie when \(r=s\). Thus, when \(r>s\), the favorable site is optimally placed at the center for birth–death but at an endpoint for death–birth. The result covers all selection strengths, including \(r<1\) and \(s<1\), without a weak-selection approximation.

In fact, letting
\[
\begin{aligned}
P(r,s)={}&6r^2s^4+9r^2s^3+15r^2s^2+18rs^3+34rs^2\\
&+14rs+4r+8s^3+22s^2+20s,
\end{aligned}
\]
the two exact differences are
\[
\rho_C^{\mathrm{Bd}}-\rho_E^{\mathrm{Bd}}=
\frac{2(r-s)P(r,s)}{3(r+2)(s+2)(2s^2+s+2)(2rs+r+2)(2rs+s+2)}
\]
and
\[
\rho_C^{\mathrm{dB}}-\rho_E^{\mathrm{dB}}=
-\frac{2(r-s)}{9(r+1)(s+1)}.
\]
All factors in the first denominator and every monomial in \(P(r,s)\) are strictly positive on the specified domain.

## Assumptions and scope

The three vertices are \(0,1,2\) with edges \(01\) and \(12\). The mutant reproductive fecundity at position \(i\) equals a prescribed positive constant \(f_i\), independent of neighboring genotypes or population frequency; a resident always has fecundity one. The center arrangement is \((f_0,f_1,f_2)=(s,r,s)\); the endpoint arrangement is \((r,s,s)\), equivalent by symmetry to an \(r\)-site at vertex \(2\). There is no mutation after the initial introduction.

In birth–death updating, a parent is selected proportional to its fecundity among all three current individuals; one of its neighbors is then replaced uniformly. In death–birth updating, a vertex is first selected to die uniformly among all three; one of its *surviving neighbors* is selected proportional to current reproductive fecundity to fill the vacancy. No self-replacement is allowed. The initial single mutant occupies each vertex with probability \(1/3\). The target event is absorption at the all-mutant state, not an average of individual reproductive outputs or conditional fixation time.

The two-vertex connected graph is vertex-transitive, so its lone designated site has no non-equivalent center-versus-endpoint placement. The three-vertex path is the smallest connected graph with these two placement orbits.

## Proof

Represent the current mutant subset by a bit mask \(M\) between \(0\) and \(7\); \(0\) and \(7\) are absorbing and masks \(1,\ldots,6\) are transient. At a state \(M\), the occupant at vertex \(i\) has fecundity \(w_i(M)=f_i\) if \(i\in M\) and \(w_i(M)=1\) otherwise. Let \(N(i)\) be the graph-neighbor set and \(d_i=|N(i)|\). In birth–death updating the ordered parent–replacement pair \((i,j)\), for \(j\in N(i)\), has probability
\[
\frac{w_i(M)}{\sum_{k=0}^2 w_k(M)}\frac1{d_i}.
\]
In death–birth updating it has probability
\[
\frac13\frac{w_i(M)}{\sum_{k\in N(j)}w_k(M)}.
\]
The next mask is obtained by assigning vertex \(j\) its parent \(i\)'s genotype. These rules specify the full stochastic transition matrix, including self-loops. Because all fecundities are positive, every nonabsorbed state has a positive-probability directed path to an absorbing state within at most two effective changes. On this finite state space absorption therefore occurs almost surely, and the six-state Dirichlet problem has a unique solution.

Writing \(h_M\) for fixation probability from mask \(M\), solve the six exact first-step equations
\[
 h_M=\sum_{M'=0}^7 T_{M,M'}h_{M'},\quad
 h_0=0,\ h_7=1\qquad(1\le M\le6).
\]
For the endpoint and center arrangements, in this order, exact rational elimination gives the birth–death values
\[
\begin{aligned}
\rho_E^{\mathrm{Bd}}
&=\frac{s(12rs^3+20rs^2+10rs+8r+4s^3+11s^2+10s)}
 {3(s+2)(2s^2+s+2)(2rs+s+2)},\\
\rho_C^{\mathrm{Bd}}
&=\frac{r(6rs+r+8s)}{3(r+2)(2rs+r+2)}.
\end{aligned}
\]
For death–birth updating the same six-state equations instead give
\[
\rho_E^{\mathrm{dB}}=\frac{5rs+3r+3s+1}{9(r+1)(s+1)},
\qquad
\rho_C^{\mathrm{dB}}=\frac{5s+1}{9(s+1)}.
\]
Here \(\rho=(h_{\{0\}}+h_{\{1\}}+h_{\{2\}})/3\), which is the specified uniform-single-mutant initial condition. Subtracting and reducing the four rational functions gives exactly the two difference identities in the finding. The birth–death numerator is \(2(r-s)P(r,s)\), with \(P(r,s)>0\) for \(r,s>0\); the death–birth numerator has the opposite sign. Every denominator is positive, completing both universal sign and equality claims.

The death–birth mechanism is particularly transparent: fitness at the center of \(P_3\) does not influence reproduction into either leaf because each leaf has only one possible parent. With an \(r\)-site at the center, its value \(r\) consequently drops out of fixation probability entirely. By contrast, endpoint fecundity influences the competition to fill a vacant center. Under birth–death updating, a center mutant can disperse to two leaves, leading to the opposite strict comparison, which is certified by the exact positive factorization.

## Verification

The standalone `verify.py` independently reconstructs the six transient first-step equations from ordered reproduction–replacement events and checks the displayed four formulas and both difference factorizations symbolically in SymPy. It checks the strict positivity of the coefficients of \(P\). A second solver, implemented with `fractions.Fraction` and Gaussian elimination independently of the symbolic matrix inversion, checks all four probabilities for 24 positive rational parameter pairs (96 exact comparisons). To reproduce, install SymPy for Python 3 and run `python3 verify.py`. The result is an exact proof by finite-state algebra and positivity, not an inference from numerical sampling.

For example, at \(r=2,s=1\), the birth–death endpoint and center probabilities are respectively \(25/63\) and \(11/24\), while the death–birth endpoint and center probabilities are \(10/27\) and \(1/3\). These exhibit the strict reversal without using floating point.

## Relationship to prior work

Maciejewski and Puleo (2013 preprint; 2014 journal) introduced site-colored environmental evolutionary graph theory and studied both birth–death and death–birth processes. Their fecundity reward applies when an individual's type matches its site's background, so resident fecundity generally varies with position. Their discussion includes a three-vertex line with differently colored sites, but examines a distinct resident-dependent model and does not give the present single-mutant-only favorable-site center–endpoint comparison under both rules. Antal, Redner and Sood (2006) proved update-dependent effects of *initial mutant position* on graphs with type-homogeneous fitness; that is not the same intervention as fixing the random initial distribution and relocating a site-specific mutant advantage. Kaveh, McAvoy and Nowak (2017 preprint) consider environmental fitness heterogeneity with mostly well-mixed dispersal and periodic-cycle examples in an appendix; they do not state the three-path center-versus-endpoint two-rule identity here. De Souza and Neves (2020) derive star-graph fixation formulas for *frequency-dependent* type fitness, without the present position-dependent mutant-only site intervention.

The ordinary Markov-chain method is standard; the claimed contribution is the exact two-update *placement reversal* for every positive pair of site fitnesses, including its sharp strictness and equality cases, not the invention of first-step fixation equations. No inference of global priority follows merely from a search yielding no identical formula.

## Limitations

The theorem concerns only one designated mutant-favored site on the three-vertex path, residents with fixed fecundity one, a uniform single-mutant start and the precisely defined birth–death/death–birth rules. It does not extend without proof to more sites, weighted or directed graphs, type-dependent resident habitats, stochastic backgrounds, alternate mutation distributions or population-frequency effects. The priority comparison is based on inspected accessible literature and remains open to undiscovered equivalent results. The mathematical verification is an internal reproducibility check, not an independent audit or formal proof assistant certification.

## References

- W. Maciejewski and G. J. Puleo, *Environmental Evolutionary Graph Theory*, arXiv:1311.3214, first public version November 13, 2013. https://arxiv.org/abs/1311.3214
- T. Antal, S. Redner and V. Sood, *Evolutionary Dynamics on Degree-Heterogeneous Graphs*, arXiv:q-bio/0601031 (2006). https://arxiv.org/abs/q-bio/0601031
- K. Kaveh, A. McAvoy and M. A. Nowak, *Environmental Fitness Heterogeneity in the Moran Process*, arXiv:1709.03031, first public version September 10, 2017. https://arxiv.org/abs/1709.03031
- E. P. de Souza and A. G. M. Neves, *Exact Fixation Probabilities for the Birth-Death and Death-Birth Frequency-Dependent Moran Processes on the Star Graph*, arXiv:2003.05462 (2020). https://arxiv.org/abs/2003.05462
