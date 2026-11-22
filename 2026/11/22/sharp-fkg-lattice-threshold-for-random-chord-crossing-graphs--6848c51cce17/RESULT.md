# Sharp FKG lattice threshold for random chord-crossing graphs

## Finding

For every integer \(n\geq1\), independently draw \(n\) chords by sampling each chord's two endpoints independently from a common continuous uniform distribution on a circle. Label the chords \(1,\ldots,n\). Let \(X_{ij}\) be the indicator that chords \(i\) and \(j\) cross, and let \(\mu_n\) be the joint probability mass function of \(X=(X_{ij})_{i<j}\) on the Boolean edge lattice \(\{0,1\}^{\binom n2}\). This is a *random labelled circle graph*, not the uniform distribution on circle graphs.

**Theorem.** The FKG lattice condition (multivariate total positivity of order two, MTP2)
\[
 \mu_n(x\vee y)\mu_n(x\wedge y)\geq\mu_n(x)\mu_n(y)
 \qquad\text{for all }x,y\in\{0,1\}^{\binom n2}
\]
holds **if and only if** \(n\leq3\). The classification is unchanged under any positive edge-activity tilt
\[
 \mu_{n,\lambda}(x)=\frac{\mu_n(x)\prod_{i<j}\lambda_{ij}^{x_{ij}}}{\sum_z\mu_n(z)\prod_{i<j}\lambda_{ij}^{z_{ij}}},\qquad\lambda_{ij}>0.
\]
Nevertheless, for distinct crossing indicators, the covariance is \(1/45\) if their edges share a chord label and zero if their edges have disjoint chord-label sets. Thus all pairwise correlations are nonnegative for every \(n\), while the stronger FKG lattice condition fails from four chords onward.

## Assumptions and scope

The circle is fixed and labelled chords have independent endpoint pairs. Endpoints are atomless, so ties have probability zero. Two chords cross if their endpoints alternate in clockwise order. The coordinatewise lattice order is on the \(\binom n2\) potential crossing edges. All probability statements concern the induced *labelled* graph. FKG lattice/MTP2 is strictly stronger than mere positive association; failure of the lattice condition alone does **not** establish negative covariance for arbitrary increasing events.

## Proof

**One- and two-chord cases.** For \(n=1\) the vector is empty. For \(n=2\) it consists of one Bernoulli coordinate; every measure on a chain satisfies the lattice condition.

**Three chords.** There are \(15\) equally likely unlabelled perfect matchings of six ordered endpoints. Five have no crossings, six have exactly one crossing, three have exactly two crossings, and one has three crossings. By permutation symmetry of chord labels, the probability of any specific zero-, one-, two-, or three-edge graph on three labelled vertices is, respectively,
\[
 \frac13,\qquad\frac{2}{15},\qquad\frac1{15},\qquad\frac1{15}.
\]
All eight states have positive mass. The elementary square inequalities of the three-dimensional Boolean lattice reduce, by symmetry, to
\[
 \frac13\cdot\frac1{15}\geq\left(\frac2{15}\right)^2,
 \qquad
 \frac2{15}\cdot\frac1{15}\geq\left(\frac1{15}\right)^2.
\]
They hold strictly. Local elementary-square log-supermodularity is equivalent to the full lattice inequality for a strictly positive measure on a finite Boolean cube: each adjacent conditional log-odds inequality can be chained along coordinate changes. Hence \(\mu_3\) is MTP2.

**Four-chord obstruction.** Consider four labelled chords, with possible crossing edges \(12,13,14,23,24,34\). Let \(O\) denote the empty crossing graph, \(E_{12}\) the exact graph containing only edge \(12\), \(E_{34}\) the exact graph containing only edge \(34\), and \(M\) the exact graph containing both edges \(12\) and \(34\) and no others. The \(105=(8-1)!!\) underlying chord pairings, with uniform independent chord labels, give
\[
 \mu_4(O)=\frac2{15},\quad
 \mu_4(E_{12})=\mu_4(E_{34})=\frac2{45},\quad
 \mu_4(M)=\frac4{315}.
\]
For transparency, these are obtained by exhaustively enumerating the \(630=7!/(2!)^3\) two-occurrence endpoint words with first symbol \(1\): the respective counts are \(84,28,28,8\). Rotation invariance makes conditioning the first endpoint label to be \(1\) harmless. The standalone verifier also enumerates perfect matchings of all eight endpoint positions and independently assigns the four chord labels, obtaining exactly the same probabilities. Equivalently, the first three probabilities follow from the \(14\) noncrossing diagrams and \(28\) one-crossing diagrams on eight endpoints, and the final one from the four diagrams whose intersection graphs consist of two disjoint edges.

Because \(E_{12}\vee E_{34}=M\) and \(E_{12}\wedge E_{34}=O\),
\[
 \frac{\mu_4(M)\mu_4(O)}{\mu_4(E_{12})\mu_4(E_{34})}
 =\frac67<1.
\]
Thus \(\mu_4\) violates MTP2.

**Projection to any larger number of chords.** We prove the finite Boolean marginal-closure fact directly. Let \(f(z,t)\geq0\) be MTP2 with \(t\in\{0,1\}\), and let \(g(z)=f(z,0)+f(z,1)\). For arbitrary \(x,y\), put \(a=x\vee y\) and \(b=x\wedge y\), and abbreviate
\[
 A=f(a,0)f(b,1),\quad B=f(a,1)f(b,0),\quad
 C=f(x,0)f(y,1),\quad D=f(x,1)f(y,0).
\]
The cross-level lattice inequalities imply \(B\geq C,D\). Multiplying the two same-level lattice inequalities yields \(AB\geq CD\). If \(B>0\), then
\[
 A+B-C-D\geq\frac{CD}{B}+B-C-D
 =\frac{(B-C)(B-D)}{B}\geq0.
\]
If \(B=0\), then \(C=D=0\), so the inequality still holds. Adding the two same-level inequalities now proves \(g(a)g(b)\geq g(x)g(y)\). Summing out Boolean coordinates one at a time therefore preserves MTP2.

For \(n>4\), discard all crossing indicators except those among chords \(1,2,3,4\). The remaining vector has law \(\mu_4\), since the corresponding four independently sampled chords are unaffected by the others. If \(\mu_n\) were MTP2, this marginal would also be MTP2, contradicting the four-chord obstruction. Hence \(\mu_n\) is not MTP2 for every \(n\geq4\).

**Positive edge-activity tilts.** Coordinatewise products satisfy \((x\vee y)_{ij}+(x\wedge y)_{ij}=x_{ij}+y_{ij}\). Therefore the product of activity factors cancels in every MTP2 lattice ratio. Every positive edgewise tilt has exactly the same MTP2 classification.

**Pairwise dependence.** Each crossing indicator has probability \(1/3\). Indicators on disjoint pairs of chord labels involve disjoint independent endpoint samples, so they are independent. For indicators on pairs \(\{1,2\}\) and \(\{1,3\}\), condition on chord \(1\). If its clockwise endpoint gap proportion is \(L\), then \(L\) is uniform on \([0,1]\), and two other independently drawn chords cross chord \(1\) with independent conditional probability \(2L(1-L)\). Hence
\[
 \operatorname{Cov}(X_{12},X_{13})
 =4\int_0^1 L^2(1-L)^2\,dL-\left(\frac13\right)^2
 =\frac2{15}-\frac19=\frac1{45}.
\]
This proves the stated covariance comparison.

## Verification

Run `python3 verify_chord_mtp2.py` using the Python standard library. Two independent exhaustive generators (multiset endpoint words and labelled perfect matchings) agree on the full probability law for every \(1\leq n\leq5\). The program independently verifies all three-chord lattice inequalities, the four-chord probabilities and exact defect ratio, adjacent/disjoint indicator covariances, and five-to-four chord projection. All computations use integers and rational fractions; no floating point or random simulation is required. The all-size conclusion additionally relies on the proved marginalization and tilt arguments, not on finite testing.

## Relationship to prior work

Acan and Pittel (2014) study random chord intersection graphs and crossing-conditioned giant-component behavior. Acan (2015) studies degrees, cores, components and graph evolution; the earlier 2013 dissertation contains enumeration of several forest and unicyclic intersection-graph classes. These works supply the random chord model and pertinent finite enumeration context, but the inspected material does not directly formulate or prove the full MTP2 threshold. Karlin and Rinott (1980) develop MTP2 and its closure properties; those general results alone do not decide the chord-graph case. The exact small-diagram counts are not claimed as new on their own: the mathematical claim is the sharp positive-dependence classification and its persistence under positive edge activities.

## Limitations

The theorem concerns the FKG *lattice condition*, not the weaker correlation inequality called positive association. In particular, it does not prove that random chord-crossing graphs with four or more chords possess negatively correlated increasing statistics. It does not address nonuniform endpoint distributions, dependence between chords, or general interaction tilts beyond one-coordinate positive edge activities. Earlier equivalent formulations or implicit deductions from older detailed chord-enumeration tables remain a priority risk.

## References

1. H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867, first posted 2014-06-11. https://arxiv.org/abs/1406.2867
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first posted 2015-01-07. https://arxiv.org/abs/1501.01489
3. H. Acan, *An Enumerative-Probabilistic Study of Chord Diagrams*, PhD dissertation, Ohio State University, 2013. https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1373310487&disposition=inline
4. S. Karlin and Y. Rinott, *Classes of orderings of measures and related correlation inequalities. I. Multivariate totally positive distributions*, Journal of Multivariate Analysis 10 (1980), 467–498. https://doi.org/10.1016/0047-259X(80)90065-2
5. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first posted 2021-04-02. https://arxiv.org/abs/2104.01134
