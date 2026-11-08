# Exact induced three-chord motif covariance and a 119-chord sign reversal

## Finding

For every integer \(n\ge3\), draw uniformly from all pairings of \(2n\) cyclically ordered points and construct the chord-intersection graph: its \(n\) vertices are chords, and two vertices are adjacent exactly when their chords cross. For \(j=0,1,2,3\), let \(N_j\) count unordered three-vertex subsets that span exactly \(j\) edges. Thus \(N_0\) counts independent triples, \(N_1\) single-edge triples, \(N_2\) induced three-vertex paths and \(N_3\) triangles.

With \(\mathbf N=(N_0,N_1,N_2,N_3)\), the complete mean vector and covariance matrix are
\[
\mathbb E\mathbf N=\binom n3\left(\frac13,\frac25,\frac15,\frac1{15}\right),\qquad
\operatorname{Cov}(\mathbf N)=\frac{\binom n3}{9450}\bigl(n^2 A+n B+C\bigr),
\]
where the **symmetric integer matrices** in the order \(0,1,2,3\) are
\[
A=\begin{pmatrix}235&-5&-155&-75\\-5&7&1&-3\\-155&1&103&51\\-75&-3&51&27\end{pmatrix},
\]
\[
B=\begin{pmatrix}245&-145&5&-105\\-145&275&-115&-15\\5&-115&125&-15\\-105&-15&-15&135\end{pmatrix},
\]
\[
C=\begin{pmatrix}-750&-780&750&780\\-780&1380&-420&-180\\750&-420&210&-540\\780&-180&-540&-60\end{pmatrix}.
\]
All four variances are strictly positive. All six off-diagonal covariance signs are completely determined: \(\operatorname{Cov}(N_0,N_1)\), \(\operatorname{Cov}(N_0,N_2)\), \(\operatorname{Cov}(N_0,N_3)\), and \(\operatorname{Cov}(N_1,N_3)\) are strictly negative for all \(n\ge3\). The path–triangle covariance \(\operatorname{Cov}(N_2,N_3)\) is negative for \(n=3\) and positive for \(n\ge4\). Most notably,
\[
\operatorname{Cov}(N_1,N_2)=\frac{\binom n3}{9450}\left(n^2-115n-420\right),
\]
which is strictly negative for \(3\le n\le118\), strictly positive for \(n\ge119\), and never zero for integer \(n\ge3\).

## Assumptions and scope

The \(2n\) endpoints are distinct in a fixed clockwise order. Each perfect matching on these endpoints is equally likely; the geometric straight-chord drawing determines crossings from endpoint alternation. Three-chord motifs are **induced** subgraphs, not noninduced homomorphism counts. Counts are over unordered chord triples, with no labels in the underlying matching. The formulas hold at every integer \(n\ge3\), without an asymptotic approximation. They say nothing about a different distribution on circle graphs or separately sampled chord endpoints.

## Proof

**Uniform finite restrictions.** Give the \(n\) matching chords uniformly random distinct names. Reading their names clockwise around the circle gives a length-\(2n\) word with each name occurring exactly twice. Every such word has the same probability: a fixed unlabeled perfect matching has precisely \(n!\) name assignments, whereas every labelled word uniquely specifies an endpoint matching and its names. Restricting this word to any prescribed set of \(k\) labels gives a uniform word with each of those \(k\) labels twice, of which there are \((2k)!/2^k\). For disjoint label sets, their restricted words are independent: given both restricted words, the interleaving is chosen uniformly independently of their internal orders.

**One triple.** The \(90\) uniform words on three labels split by induced crossing-edge count \(j=0,1,2,3\) into \((30,36,18,6)\) words, proving \(q=(1/3,2/5,1/5,1/15)\) and the stated means. Equivalently, this follows by enumerating the \(15\) matchings of six endpoints.

**Two triples.** Take triples \(S,T\) of chord labels sharing exactly \(r\) labels. Write \(Q_r(i,j)\) for the joint probability of \(i\) edges on \(S\) and \(j\) edges on \(T\). The uniform restriction property reduces the entire joint problem to at most five labels. Exact complete enumeration of \(113400\) words at \(r=1\), \(2520\) at \(r=2\), and \(90\) at \(r=3\), yields
\[
2835 Q_1=\begin{pmatrix}362&377&158&48\\377&455&227&75\\158&227&134&48\\48&75&48&18\end{pmatrix},
\]
\[
315 Q_2=\begin{pmatrix}56&40&9&0\\40&54&24&8\\9&24&22&8\\0&8&8&5\end{pmatrix},
\]
\[
15 Q_3=\operatorname{diag}(5,6,3,1).
\]
Every entry is computed by enumerating the uniform finite word space, checking crossing alternation for its two specified triples, and dividing by the total number of words. Complete executable enumeration is in the accompanying `check.py`; the printed integer matrices make the finite step independently inspectable. For \(r=0\), the two triple types are independent and \(Q_0=qq^{\mathsf T}\).

**Counting overlaps.** For each fixed unordered chord triple \(S\), the number of unordered triples \(T\) with exactly \(r\) labels in common is \(\binom3r\binom{n-3}{3-r}\). Decomposing the covariance of the two sums of indicator functions, cancelling the \(r=0\) contribution, gives the **exact** identity
\[
\operatorname{Cov}(N_i,N_j)=\binom n3\sum_{r=1}^3
\binom3r\binom{n-3}{3-r}\bigl(Q_r(i,j)-q_iq_j\bigr),
\]
where \(\binom ab=0\) if \(b>a\) for nonnegative integers. Substitution of the three finite tables and exact rational expansion gives the displayed matrices \(A,B,C\); there is no limiting or sampling argument in this derivation.

**Signs and sharp cutoffs.** The off-diagonal entries of \(9450\operatorname{Cov}(\mathbf N)/\binom n3\) factor as follows, listed for pairs \((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)\):
\[
-5(n^2+29n+156),\quad -5(31n^2-n-150),\quad-15(n+4)(5n-13),
\]
\[
n^2-115n-420,\quad-3(n^2+5n+60),\quad3(17n^2-5n-180).
\]
For integer \(n\ge3\), the first, second, third, and fifth expressions are negative. The last expression equals \(-126\) at \(n=3\) and \(324\) at \(n=4\), and increases thereafter. The fourth increases strictly for \(n\ge3\), and equals \(-66\) at \(n=118\) and \(56\) at \(n=119\); this proves both exact sign thresholds. The four diagonal numerators are respectively \(5(47n^2+49n-150)\), \(7n^2+275n+1380\), \(103n^2+125n+210\), and \(3(9n^2+45n-20)\), each strictly positive for \(n\ge3\).

## Verification

Run `python3 check.py` with Python 3.9 or newer; the verifier uses only the standard library and exact integers/fractions. It independently enumerates all labelled double-occurrence words on \(5,4,3\) labels to check **all 48 joint-table entries**, enumerates all perfect matchings on \(6,8,10,12,14\) endpoints (\(15,105,945,10395,135135\) matchings) to check all mean and covariance entries, checks exact overlap expansion at seven sample sizes, and checks displayed signs over integers \(3\) through \(399\). It prints `ALL CHECKS PASSED`. The all-size conclusion rests on the overlap identity and algebraic sign arguments, **not** the finite sample-size sweep.

## Relationship to prior work

Flajolet and Noy [1] developed exact and asymptotic results for the **total number of crossings** in random chord diagrams. Acan [2] studied their intersection graphs, including degrees, cores, and the expectation of independent sets of given size. Acan and Pittel [3] studied a component transition for diagrams with constrained crossing counts. Paguyo [4] gave convergence bounds for the number of crossings and simple chords. These are closely related models and statistics, but their inspected relevant results do not state the joint covariance matrix of the four **induced three-chord motif** counts, nor the precise one-edge/path sign reversal at \(119\) chords. In particular, the one-vertex motif expectation and total crossing-count variance do not by themselves determine the six pairwise three-vertex motif covariances. Earlier implicit derivability from general finite-pattern enumerators is possible.

## Limitations

No independence among motif counts is asserted; indeed \(N_0+N_1+N_2+N_3=\binom n3\) makes the covariance matrix singular. These are unconditional covariances, not conditioned on total crossing count. The finite tables are verifiable by exhaustive finite computation, but there is no unreviewed claim of a central limit theorem, a general induced-motif theory, or historical priority. The novelty comparison is based on identified and inspected primary sources and recoverable related claims, not an exhaustive mathematical-literature certification. Independent external validation has not been performed.

## References

[1] P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report 3914, dated March 4, 2000. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf

[2] H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, January 7, 2015. https://arxiv.org/abs/1501.01489

[3] H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867, 2014. https://arxiv.org/abs/1406.2867

[4] J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134. https://arxiv.org/abs/2104.01134
