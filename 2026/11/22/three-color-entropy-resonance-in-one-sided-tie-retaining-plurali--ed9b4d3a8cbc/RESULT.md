# Three-color entropy resonance in one-sided tie-retaining plurality

## Finding

For every number of named opinions \(q\ge3\) and indexed cyclic ring of \(n\ge3\) sites, define synchronous incumbent-retaining plurality using the site itself and its next two clockwise sites. Every trajectory becomes periodic within at most \(n-2\) updates, and this bound is attained for every \(q\ge3\) and \(n\ge3\). The periodic configurations partition into two disjoint classes: every proper cyclic coloring (adjacent symbols distinct) is frozen, while every cyclic coloring without singleton monochromatic runs rotates rigidly by one site on each update. No other periodic configurations exist.

Write \(P_{q,n}\) for the frozen proper-coloring count and \(S_{q,n}\) for the count of rigidly rotating configurations, including the \(q\) uniform configurations. Their exact all-size formulas are

\[
P_{q,n}=(q-1)^n+(q-1)(-1)^n,
\qquad
S_{q,n}=\lambda_+^n+\lambda_-^n+2(q-1)\cos(n\pi/3),
\qquad
\lambda_\pm=\frac{1\pm\sqrt{4q-3}}2.
\]

Consequently the entire recurrent set has size \(P_{q,n}+S_{q,n}\). For the unique integer opinion count \(q=3\), both parts have leading asymptotics \(2^n\), so the proportion of frozen states *within the recurrent set* converges to \(1/2\). For every integer \(q\ge4\), frozen configurations exponentially outnumber rotating ones; indeed \(q-1>\lambda_+\). This is a sharp three-color crossing of the two recurrent entropy rates.

More precisely, for \(q=3\),

\[
P_{3,n}=2^n+2(-1)^n,\qquad
S_{3,n}=2^n+(-1)^n+4\cos(n\pi/3),
\]

and for \(q\ge4\) the leading exponential rates are respectively \(\log(q-1)\) and \(\log\lambda_+\). A rotating configuration has least temporal period equal to its least spatial period. Its nontrivial least periods on a ring of length \(n\) are exactly the divisors of \(n\) that are at least four. For any such divisor \(d\), the exact number of primitive temporal \(d\)-orbits is \(d^{-1}\sum_{e\mid d}\mu(d/e)S_{q,e}\), with the same formula extended to \(d=1\) counting only the uniform rotating fixed points. The complete fixed-state count is \(P_{q,n}+q\).

## Assumptions and scope

Choose integers \(q\ge3\) and \(n\ge3\). The alphabet is \(\{0,1,\dots,q-1\}\), and all indices are in \(\mathbb Z/n\mathbb Z\). An update replaces the current site by the uniquely most frequent symbol in the three ballots \((x_i,x_{i+1},x_{i+2})\), keeping \(x_i\) when no symbol has unique maximum frequency. This rule simplifies exactly to

\[
(Fx)_i=\begin{cases}x_{i+1},&x_{i+1}=x_{i+2},\\ x_i,&x_{i+1}\ne x_{i+2}.\end{cases}
\]

The spatial left shift is \((\sigma x)_i=x_{i+1}\). A *proper* word has \(x_i\ne x_{i+1}\) at every site. A *thick* word has no cyclic singleton run: every site belongs to a monochromatic run of length at least two, equivalently \(x_{i-1}=x_i\) or \(x_i=x_{i+1}\) at every site. Uniform words are thick. Temporal first-entry time is the least \(t\ge0\) for which \(F^t x\) is periodic; configurations and orbits are labelled by site indices and named colors, not quotiented by rotation or relabeling.

## Proof

**1. Local dynamics and the dichotomy.** The displayed rule follows by considering whether the last two ballots agree: if they do, their common value wins; if they do not, either all three ballots differ (so the incumbent wins the tie), or the incumbent agrees with one of them (and hence wins). Every proper cyclic word is therefore fixed. On a thick cyclic word, the successor color wins precisely at the last site of each monochromatic run, and elsewhere the successor equals the incumbent; thus \(Fx=\sigma x\), including on uniform words.

**2. Persistence of long runs.** On a nonuniform cyclic word, consider a maximal run of a color \(a\) of length \(\ell\ge2\). Every site in its interior remains color \(a\), and the site immediately preceding the run changes to \(a\), because it sees the first two sites in the run. Its last site changes away from \(a\) only if the next run has length at least two (in which case it adopts the next run's color). Hence the run's updated descendant contains at least \(\ell\) consecutive \(a\)-sites, shifted left by one when both neighboring runs are long, or extended when the following run is a singleton. Adjacent descendants cannot cross: each run expands at most one site to the left, and only the last site of a run can be lost on the right. In particular, no preexisting long run creates a new singleton run; singleton runs are never created from long runs. The number of singleton *sites* cannot increase. If both a long and a singleton run occur, follow the cyclic run decomposition backward from a long run to find an immediately preceding singleton run. Its unique site is replaced by the long run's color, so at least one singleton is eliminated on that update. Thus singleton-site count strictly decreases at every update of a mixed word.

There are initially at most \(n-2\) singleton sites if a long run exists. Therefore in at most \(n-2\) updates every nonproper word becomes thick. No mixed word can be recurrent, because its positive singleton count strictly decreases until reaching zero. The proper and thick classes are invariant and consist wholly of periodic configurations, proving the classification and cutoff.

**3. Sharp clock.** For any \(n\ge3\), take the cyclic word \(00\) followed by \(n-2\) alternating colors \(1,2,1,2,\ldots\). The double zero block spreads one site left per update, deleting exactly one singleton at a time. The initial word enters the all-zero configuration after exactly \(n-2\) updates and not earlier. The same witness works for every \(q\ge3\) by using only three available colors.

**4. Counting proper cyclic words.** Proper words are proper colorings of the indexed cycle, so their count is the trace of the \(q\times q\) adjacency matrix of the complete graph without loops. This matrix has eigenvalues \(q-1\) once and \(-1\) with multiplicity \(q-1\). Taking its \(n\)-th trace power gives \(P_{q,n}\).

**5. Counting thick cyclic words.** Use the pair-state directed graph with states \((a,b)\) for ordered symbols; allow \((a,b)\to(b,c)\) exactly when \(a=b\) or \(b=c\). A cyclic closed walk of length \(n\) corresponds bijectively to a labelled thick word. Let \(M\) be this \(q^2\)-state adjacency matrix. For a vector of functions \(f(a,b)\), put \(u_a=f(a,a)\) and \(v_a=\sum_b f(a,b)\). The action of \(M\) is \((Mf)(a,b)=v_b\) if \(a=b\), and \((Mf)(a,b)=u_b\) otherwise. Consequently the induced \(2q\)-dimensional map on \((u,v)\) is

\[
(u,v)\longmapsto\bigl(v,\ v+(J-I)u\bigr),
\]

where \(J\) is the all-ones matrix. By the rectangular determinant identity, the nonzero spectrum of \(M\), with multiplicities, equals that of this induced matrix, and

\[
\det(zI-M)=z^{q(q-2)}(z^2-z-(q-1))(z^2-z+1)^{q-1}.
\]

The constant-vector sector of \(u\) has roots \(\lambda_\pm\), while its sum-zero sector has roots \(e^{\pm i\pi/3}\), each of multiplicity \(q-1\). Thus \(S_{q,n}=\operatorname{tr}(M^n)\) has the stated formula for all \(n\ge3\) (and its transfer power sum is valid also for \(n\ge1\) as a formal cyclic-word count).

**6. Entropy resonance and temporal periods.** Since \(\lambda_+>1\) and \(|\lambda_-|<\lambda_+\), the thick entropy is \(\log\lambda_+\); the proper entropy is \(\log(q-1)\). The root relation \(\lambda_+^2-\lambda_+-(q-1)=0\) implies \(\lambda_+=q-1\) exactly at integer \(q=3\) among \(q\ge3\); for larger \(q\), \(\lambda_+<q-1\). For \(q=3\) the roots are \(2,-1\), yielding the explicit counts and asymptotic half-and-half recurrent split. Every thick state follows \(\sigma\), so its least temporal period is its least spatial period. A nonconstant thick word of least spatial period \(d\) needs at least two runs of lengths at least two, forcing \(d\ge4\); conversely the word consisting of two zeros followed by \(d-2\) ones is thick and has least spatial period \(d\) for every \(d\ge4\), and repeating it gives a state on any ring whose length is a multiple of \(d\). Standard Möbius inversion of the fixed-point counts \(S_{q,e}\) gives the primitive-period formula. Proper words are fixed, and the only thick fixed words are the \(q\) uniform words.

## Verification

Two included standalone Python 3 programs use only the standard library. Run `python3 verify.py` to enumerate complete initial configuration spaces for \(q=2,3,4,5\) and selected ring lengths, check every eventual period and first-entry time, and independently compare the exact transfer-matrix traces against the closed power sums. Run `python3 check_independent.py` to compare the original three-ballot plurality specification with the derived two-case local rule, and to verify the sharp witness across lengths 3 through 29. Exact outputs are recorded in `verify.log` and `check_independent.log`. All-length conclusions rely on the arguments above, not extrapolation from finite experiments.

## Relationship to prior work

Fukś (1997) analyzes deterministic **binary centered** Rule 232, with local ballots from the left neighbor, incumbent, and right neighbor. Lemoy, Mozeika and Seki (2013) study a noisy form of the same centered binary rule. Nakar and Ron (2022) prove structural results for centered symmetric binary majority on cyclic rings and its fixed/two-periodic configurations. These methods and model families motivate the comparison, but their stated objects and update maps differ from the present one-sided, multi-opinion, incumbent-retaining plurality. In particular, the all-distinct three-color tie cannot occur in the binary centered models. The proof here supplies an exact asymmetric cyclic dynamical classification plus a color-count entropy crossing, neither of which is a direct implication of those papers. A literature search found no exact covering statement; this is not a claim of definitive bibliographic priority.

## Limitations

The theorem concerns only synchronous updates, finite indexed cyclic rings, the specified forward three-ballot neighborhood and incumbent tie retention, with at least three named opinions. It does not assert stability under stochastic updates, alternative tie rules, directed graph perturbations or infinite-lattice initial measures. The recurrent half-and-half statement conditions on recurrence, not on uniformly sampled initial states: the recurrent set is exponentially sparse relative to all \(3^n\) initial words. A bounded literature examination does not establish definitive historical priority.

## References

- Henryk Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules* (first arXiv version 1997-03-07), https://arxiv.org/abs/comp-gas/9703001 .
- Rémi Lemoy, Alexander Mozeika and Shinnosuke Seki, *Transfer matrix analysis of one-dimensional majority cellular automata with thermal noise* (first arXiv version 2013-11-18), https://arxiv.org/abs/1311.4388 .
- Yonatan Nakar and Dana Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity* (first arXiv version 2022-05-18), https://arxiv.org/abs/2205.08972 .
