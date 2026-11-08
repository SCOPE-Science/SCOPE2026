# The first two-round source-ranking reversal in synchronous pull on \(K_{a,b}\)

## Finding
Let \(T_A(a,b)\) and \(T_B(a,b)\) be the completion times of synchronous *pull-only* rumour broadcasting on the unweighted complete bipartite graph \(K_{a,b}\), started from one vertex in the part of size \(a\) and \(b\), respectively. Every still-uninformed vertex independently chooses one uniformly random neighbour each round; it becomes informed precisely when that neighbour was already informed at the start of the round. The choices of distinct vertices and rounds are independent, and informed vertices remain informed.

**Theorem (first two-round reversal and crossing).** Among all integer pairs \(1\le a<b\) with \(a+b\le 10\), the smaller-part initial source is strictly more likely to finish by the end of round two:
\[
\Pr(T_A(a,b)\le2)>\Pr(T_B(a,b)\le2).
\]
On the eleven-vertex graph \(K_{5,6}\), however, this inequality reverses at round two and reverses back at round three:
\[
\Pr(T_A(5,6)\le2)-\Pr(T_B(5,6)\le2)
=-\frac{947518181}{492075000000000}<0,
\]
\[
\Pr(T_A(5,6)\le3)-\Pr(T_B(5,6)\le3)
=\frac{949127700048257234999}{59787112500000000000000}>0.
\]
Therefore \(K_{5,6}\) is the **smallest complete bipartite graph exhibiting a reversal of the smaller-part source's two-round advantage**, and its two source-conditioned completion-time laws are incomparable in first-order stochastic order. The minimality assertion concerns the two-round reversal, not every possible type of stochastic incomparability.

## Assumptions and scope
The graph is finite, undirected, loopless and complete bipartite. An initial vertex is informed at time zero. Updates are simultaneous; no newly informed vertex can supply information within the same round. Each uninformed vertex makes exactly one uniform neighbour choice, with independent choices across vertices and rounds. This is *pull only*, not push, push-pull, asynchronous telephone contact, or a random walk. Time is counted in integer rounds. In \(K_{a,b}\), \(T_A\) denotes a source in the size-\(a\) part whether or not \(a<b\). There are no extrapolations to arbitrary graphs or other broadcasting rules.

## Proof
For a source in the size-\(a\) part, let \(J\) count informed vertices in the size-\(b\) part after one round. Every vertex on the latter side pulls the one informed neighbour with probability \(1/a\), so \(J\sim\operatorname{Bin}(b,1/a)\). Conditional on \(J=j\), in round two all \(a-1\) initially uninformed vertices on the first side must contact one of the \(j\) informed vertices opposite, independently with probability \((j/b)^{a-1}\). Simultaneously all \(b-j\) remaining uninformed vertices on the second side must contact the sole informed vertex in the size-\(a\) part, with probability \((1/a)^{b-j}\). Hence for \(a\ge2\) the exact two-round success probability is
\[
F_2(a,b):=\Pr(T_A(a,b)\le2)
=\frac{1}{a^b b^{a-1}}
\sum_{j=0}^{b}\binom{b}{j}\left(\frac{a-1}{a}\right)^{b-j}j^{a-1}.
\]
For \(a=1\), the initial source is the unique vertex on that side, so \(F_2(1,b)=1\); these values are compatible with the probabilistic derivation without needing ambiguous zero powers. By exchanging the part labels, \(\Pr(T_B(a,b)\le2)=F_2(b,a)\).

The following table supplies finite rational certificates for all \(a<b\), \(a+b=s\), with \(3\le s\le10\). In each row, the displayed pair minimizes \(F_2(a,b)-F_2(b,a)\) over every admissible pair with that total. Every minimum is positive, proving the asserted minimality. Each entry follows by direct finite substitution into the previous binomial sum.

| Total \(s\) | Minimizing \((a,b)\) | Exact minimum of \(F_2(a,b)-F_2(b,a)\) |
|---|---|---|
| 3 | (1,2) | \(1/2\) |
| 4 | (1,3) | \(2/3\) |
| 5 | (2,3) | \(115/864\) |
| 6 | (2,4) | \(35/256\) |
| 7 | (3,4) | \(29093/2239488\) |
| 8 | (3,5) | \(591106/61509375\) |
| 9 | (4,5) | \(14281061/20480000000\) |
| 10 | (4,6) | \(11305529/36691771392\) |

For the eleven-vertex pair \((a,b)=(5,6)\), the binomial sum yields
\[
F_2(5,6)=\frac{37053}{97656250},\qquad
F_2(6,5)=\frac{480389}{1259712000}.
\]
Their difference reduces to the stated strictly negative fraction.

For the third round, let \(X_t=(I_t,J_t)\) be the numbers informed in the respective parts after round \(t\). From \((i,j)\), independently, \(h\) new size-\(a\)-part vertices and \(k\) new size-\(b\)-part vertices are informed with transition probability
\[
Q_{a,b}((i,j),(i+h,j+k))=
\binom{a-i}{h}\left(\frac jb\right)^h
\left(1-\frac jb\right)^{a-i-h}
\binom{b-j}{k}\left(\frac ia\right)^k
\left(1-\frac ia\right)^{b-j-k},
\]
for \(0\le h\le a-i\), \(0\le k\le b-j\), and zero otherwise. As usual \(0^0=1\) in finite-binomial boundary terms. This is a complete finite Markov-chain specification: \(\Pr(T_A(a,b)\le t)=Q_{a,b}^{t}((1,0),(a,b))\) and \(\Pr(T_B(a,b)\le t)=Q_{a,b}^{t}((0,1),(a,b))\). Three rational matrix steps in the \(5\times6\) case give
\[
\Pr(T_A(5,6)\le3)=\frac{207876362387783}{4449462890625000},
\qquad
\Pr(T_B(5,6)\le3)=\frac{188835022260049}{6122200320000000}.
\]
Their difference is the stated strictly positive fraction. Because first-order stochastic domination of one completion time over the other would force a consistent CDF inequality at **all** integer times, the opposite signs at times two and three rule out domination in either direction. This completes the proof.

## Verification
Run `python3 verify_pull.py` with Python 3 (standard library only). It separately evaluates the closed two-round binomial formula and the full finite-state Markov recurrence with exact rational arithmetic; checks all unequal bipartitions on at most eleven vertices; checks the listed strict signs below eleven vertices; compares both derivations on all unequal bipartitions up to eight vertices and on \(K_{5,6}\); and asserts all four exact CDF fractions and their signed differences. The recorded execution printed `VERIFY_OK 57 exact checks`. The proof above supplies the probabilistic derivation and finite rational certificates; the checker is a reproducibility aid rather than evidence for any untested infinite statement.

## Relationship to prior work
Panagiotou and Reisser (first publicly posted 2021-10-18, arXiv:2110.09044) analyze the complete-graph synchronous pull completion-time distribution, using the same independent-neighbour model but without two inequivalent source orbits. Doerr and Kostrygin (2023, arXiv:2303.11150) develop near-sharp runtime bounds for symmetric spreading on complete networks. Acan, Collevecchio, Mehrabian and Wormald (arXiv:1411.0948) analyze asynchronous push-pull, synchronous push-pull and structural bounds, not these exact pull-only finite-round source comparisons. None of their inspected statements yields the stated pair of opposite rational inequalities or the minimal two-round cutoff under the specified update rule. Related source-dependent processes may have different directionality and cannot be substituted without proof.

## Limitations
The theorem is a finite exact cutoff and a specific source-ranking obstruction, not a classification for all part sizes. It does not assert that \(K_{5,6}\) is the smallest example of *any* failure of stochastic ordering, nor that one source minimizes expected completion time. Further literature may contain equivalent finite-round results under different terminology. Independent mathematical checking and comprehensive historical-priority certification are not part of the present result.

## References
1. K. Panagiotou and S. Reisser, *Asymptotics for Pull on the Complete Graph*, first public arXiv version 2021-10-18, https://arxiv.org/abs/2110.09044.
2. B. Doerr and A. Kostrygin, *Randomized Rumor Spreading Revisited (Long Version)*, first public arXiv version 2023-03-20, https://arxiv.org/abs/2303.11150.
3. H. Acan, A. Collevecchio, A. Mehrabian and N. Wormald, *On the push&pull protocol for rumour spreading*, first public arXiv version 2014-11-04, https://arxiv.org/abs/1411.0948.
