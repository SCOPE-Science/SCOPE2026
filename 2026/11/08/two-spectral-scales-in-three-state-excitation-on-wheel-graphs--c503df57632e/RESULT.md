# Two spectral scales in three-state excitation on wheel graphs

## Finding

Let \(n\ge3\) and \(W_n=K_1\vee C_n\), with one hub and \(n\) rim vertices. Under synchronous three-state Greenberg–Hastings excitation, define \(F\) by the rule \(1\to2\to0\), and let a vertex in state \(0\) advance to \(1\) exactly when an open neighbor is in state \(1\). All updates are simultaneous. Then
\[
F^7=F^4.
\]
The only periodic orbit lengths are one and three; the only fixed configuration is all-rest. The sharp largest first-entry time is \(3\) for \(n=3\) and \(4\) for every \(n\ge4\).

For uniform independent initial states, define \(E_n\) as the number of states eventually entering all-rest; define \(P_n\) as the number of distinct primitive temporal three-cycle orbits. Write
\[
S=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix},
\]
and index a \(9\)-by-\(9\) matrix \(T\) by ordered pairs \((a,b),(b',c)\in\{0,1,2\}^2\), with entries
\[
T_{(a,b),(b',c)}=\mathbf1_{\{b=b'\}}\mathbf1_{\{b=2\ \text{or}\ b+1\in\{a,c\}\}}.
\]
The following identities hold for every \(n\ge3\):
\[
E_n=3\operatorname{tr}(S^n)=3\big((1+\sqrt2)^n+(1-\sqrt2)^n+1\big),
\qquad P_n=\operatorname{tr}(T^n)-1.
\]
In particular, the number of initially periodic labelled configurations is exactly \(1+3P_n\), and the number of initial configurations eventually entering period-three orbits is \(3^{n+1}-E_n\). Moreover,
\[
\det(\lambda I-T)=\lambda^4(\lambda^2+\lambda+1)(\lambda^3-2\lambda^2-1).
\]
Let \(\rho=2.20556943040059\ldots\) be the real root greater than two of \(\lambda^3-2\lambda^2-1\). The fraction that eventually extinguishes and the fraction *already periodic* satisfy the distinct exponential laws
\[
\frac{E_n}{3^{n+1}}\sim\left(\frac{1+\sqrt2}{3}\right)^n,
\qquad
\frac{1+3P_n}{3^{n+1}}\sim\left(\frac\rho3\right)^n.
\]
Thus a random initial state eventually cycles with probability tending to one, while the probability that it starts on any recurrent orbit tends exponentially to zero, with a strictly faster exponential rate. 

## Assumptions and scope

The rim is a simple cycle with \(n\) distinctly labelled vertices (for \(n=3\), \(W_3=K_4\)); the graph is undirected, without loops. States are \(0\) (rest), \(1\) (excitation), and \(2\) (refractory). All \(3^{n+1}\) initial states are included. First-entry time is the minimum \(t\ge0\) such that \(F^t(x)\) belongs to its eventual periodic orbit. Counts distinguish labelled vertex assignments; temporal rotations of a period-three orbit are regarded as one orbit. The spectral limit is for \(n\to\infty\) and uses uniform initial states only for probability interpretations.

## Proof

**Triangle criterion and extinction.** Call a hub–rim–rim triangle *tricolored* if its three vertices initially have all three states. The three states on that triangle thereafter rotate in synchrony forever: each resting vertex sees the excited vertex on its triangle. Thus the hub rotates at every time. Conversely, suppose no such triangle occurs. If the hub starts at \(2\), the rim has no adjacent pair of colors \(0,1\). After one update no vertex is excited, and after two all vertices are at rest. If the hub starts at \(1\), the rim has no adjacent pair \(0,2\). At time one the rim colors are the images \(0\to1,1\to2,2\to0\), and a vertex initially \(2\) cannot see a neighbor initially \(0\). At time two no vertex is excited, and all rest by time three. If the hub starts at \(0\), no adjacent rim pair has colors \(1,2\). With no initial rim \(1\), all rest by time one. Otherwise the hub follows \(0,1,2,0\) through time three. Vertices initially \(1\) are at rest at time three; vertices initially \(0\) or \(2\) are either refractory or resting then. This uses the absence of adjacent initial \(1,2\) for the initial-\(1\) case. At time three no vertex is excited and the hub rests, so all rest at time four. These cases prove that extinction occurs exactly for colorings with no tricolored hub triangle, and that extinction is complete by time four.

**Exact finite-radius bound in the oscillatory case.** When a tricolored triangle exists, the hub is an imposed three-state rotor forever. For any rim vertex, its state at time \(t\) depends only on its initial radius-\(t\) rim neighborhood and the imposed hub states at times \(0,\ldots,t-1\). To establish equality of the states at times four and seven, it is therefore enough to compare the middle site of every length-15 ternary rim word under the prescribed rotating hub. The standalone C checker `checks/verify_forced_rotor.c` constructs the exact local transition table, enumerates every one of \(3^{15}=14,348,907\) words for each of the three hub phases, and checks the center at times four and seven. All \(43,046,721\) comparisons pass. The shrinking-window calculation is exactly the radius-seven light cone: there are \(15-2t\) live entries after \(t\) steps. Arbitrary cycles of smaller length are covered because their overlapping rim windows are among these words. The hub also agrees at times four and seven. Hence \(F^7=F^4\) on tricolored cases, and the earlier extinction analysis proves it in the remaining cases. The state with hub \(0\), one rim vertex \(1\), and all other rim vertices \(0\), has first-entry time exactly four for every \(n\ge4\), as a rim vertex not next to the initial excited rim vertex still has a refractory state at time three. For \(n=3\) the extinction analysis and direct four-vertex case enumeration show sharp time three; its \(81\) cases are included in the independent exact checker.

**Pell-type extinction census.** Fix the initial hub color, and relabel it \(0\) solely for counting initial tricolored triangles. A forbidden tricolored triangle consists of two adjacent rim colors \(1\) and \(2\) in either order. Thus permitted rim colorings are precisely cyclic words avoiding the adjacent pairs \(12\) and \(21\). The transfer matrix on \(\{0,1,2\}\) is \(S\). Standard closed-walk counting gives \(\operatorname{tr}(S^n)\) rim words. There are three hub colors, so \(E_n=3\operatorname{tr}(S^n)\). The characteristic polynomial of \(S\) is \((\lambda-1)(\lambda^2-2\lambda-1)\), which gives the stated closed formula.

**Primitive three-cycle census.** The proven iterate identity restricts eventual periods to divisors of three. Since \(1\to2\to0\), all-rest is the only fixed point. Any nonfixed periodic configuration must lie in a tricolored-triangle orbit, whose hub rotates. A rim vertex cannot remain forever at rest while the hub visits excitation, so in a period-three orbit every vertex rotates at each step. A coloring rotates globally if and only if each vertex of color \(a\) has a neighbor of color \(a+1\pmod3\) initially. Fix the hub color \(0\). At a rim site of color \(0\), at least one adjacent rim color must be \(1\); at a rim site of color \(1\), at least one adjacent rim color must be \(2\); at a rim site of color \(2\), the hub itself supplies the required successor \(0\). The associated allowed triple condition is precisely the adjacency rule defining \(T\), and cyclic rim words obeying it are counted by \(\operatorname{tr}(T^n)\). The unique such word containing no rim \(1\) is the all-\(2\) word, for which the hub fails its successor condition. Therefore exactly \(\operatorname{tr}(T^n)-1\) globally rotating states have hub color \(0\). There are three choices for the hub color and each primitive orbit contains three states, so \(P_n=\operatorname{tr}(T^n)-1\). Direct determinant expansion of the explicit nine-state matrix gives its displayed characteristic polynomial.

**Asymptotic spectral separation.** The Perron root of \(\lambda^3-2\lambda^2-1\) is \(\rho\). Its other two roots have modulus less than one, and the other nonzero roots of \(T\) are third roots of unity; hence \(\operatorname{tr}(T^n)=\rho^n+O(1)\). Since \(1+\sqrt2>\rho\), the stated limits hold with two strictly distinct exponential bases.

## Verification

Run `python checks/verify_wheel.py` to replay independent full-graph evolution over all initial states on wheels with rim sizes \(3\) through \(10\) (the exact per-size counts are printed by the program), confirm the transfer-matrix characteristic polynomials and compare both censuses. Run `cc -O3 -std=c11 checks/verify_forced_rotor.c -o verify_forced_rotor && ./verify_forced_rotor` to check all \(43,046,721\) radius-seven local cases. The supplied `checks/verify_wheel_output.txt` and `checks/verify_forced_rotor_output.txt` are captured outputs from these actual sources. All finite checks are exhaustive for their stated domains; only the light-cone reduction, combined with the analytic triangle argument, extends the time-bound verification to all graph orders.

## Relationship to prior work

Gravner–Lyu–Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs* (arXiv:1610.07320, publicly submitted October 24, 2016; later Annals of Applied Probability 2018), gives a general circulation/conservativity criterion for synchronization and a graph-diameter synchronization bound (Theorem 3). On wheel graphs, its criterion implies the qualitative tricolored-triangle extinction dichotomy. The present result does **not** claim that dichotomy or the existence of three-cycle activity as new. Its more specific content is the two exact transfer-matrix counts (particularly *individual primitive cycle orbit counts*), their distinct growth constants, and a sharp all-state entry identity. The general theorem does not state these explicit wheel counts or the comparison of their exponential scales. The paper's definitions, Theorem 3 and proof were inspected, not just its abstract. Earlier cyclic-excitation theory of Durrett–Griffeath (1993, arXiv:patt-sol/9303002, original submission March 22, 1993) supplies broader historical context; only its accessible abstract, not its full paper, was inspected. No priority claim is made against inaccessible or unindexed wheel-specific treatments.

## Limitations

The theorem concerns the exact three-state, contact-threshold-one rule on a wheel with a complete hub; it does not extend automatically to other graph topologies, more colors, other thresholds, or stochastic updates. The finite light-cone enumeration is supplied as verifiable mathematical evidence, not as a black-box claim of independent certification. The tested small wheels supplement rather than replace the proof for all \(n\). The originality comparison leaves a residual risk of an equivalent enumeration in unindexed literature, 

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (first submitted 2016-10-24), Theorem 3, DOI:10.1214/17-AAP1350; accessible author-hosted full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.
2. R. Durrett, D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (first submitted 1993-03-22), *Experimental Mathematics* 2 (1993), 183–208, DOI:10.1080/10586458.1993.10504277; available abstract: https://arxiv.org/abs/patt-sol/9303002.
