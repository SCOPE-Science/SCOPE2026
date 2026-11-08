# The complete 2-frugal independent-set polynomial of cycle prisms

## Finding

For each integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the cycle prism with two fixed rows and cyclically indexed columns. Let \(f_{n,k}\) be the number of independent vertex subsets \(S\subseteq V(P_n)\) of size \(k\) such that every vertex has at most two neighbours in \(S\). Define the full \(2\)-frugal independent-set polynomial \(I_n(z)=\sum_{k\ge0}f_{n,k}z^k\), including the empty set. Then
\[
\boxed{I_n(z)=1+\sum_{k=1}^{\lfloor2n/3\rfloor}z^k
 \sum_{r=\lceil k/2\rceil}^{\min(k,n-k)}
 \frac nr\binom r{k-r}\binom{n-k-1}{r-1}2^r.}
\]
Empty inner sums are zero. The maximum possible cardinality is exactly
\[
\boxed{\alpha^f_2(P_n)=\lfloor 2n/3\rfloor,}
\]
and all extremal sets are classified by the run construction in the proof. Their number \(M_n=f_{n,\lfloor2n/3\rfloor}\) is
\[
\boxed{M_{3t}=3\,2^t\ (t\ge1),\qquad M_{3t+1}=(3t+1)(t+1)2^t\ (t\ge1),\qquad M_{3t+2}=(3t+2)2^{t+1}\ (t\ge1).}
\]
For example, the exact coefficient sequences \((f_{n,0},f_{n,1},\ldots)\) begin with \((1,6,6)\) for \(n=3\), \((1,8,16)\) for \(n=4\), and \((1,10,30,20)\) for \(n=5\).

## Assumptions and scope

Graphs are finite, simple, undirected. Vertex \((i,a)\), for \(i\in\mathbb Z/n\mathbb Z\) and \(a\in\{0,1\}\), has the three neighbours \((i-1,a),(i+1,a),(i,1-a)\). An independent set has no adjacent pair. An independent set \(S\) is \(2\)-frugal when \(|N(v)\cap S|\le2\) for every vertex \(v\). Set counts use the fixed labelled vertex set; neither row-swapping nor rotation nor reflection identifies different subsets. The invariant \(\alpha^f_2\) is the maximum size of such an independent set. All identities concern every integer \(n\ge3\).

## Proof

**Exact shape of every feasible set.** Independence makes each column either empty, occupied in the first row, or occupied in the second row. Furthermore, occupied columns next to each other must lie in opposite rows. If three cyclically consecutive columns are all occupied, their row pattern must alternate. The vertex opposite the occupied vertex of the middle column then has all three of its neighbours occupied, contradicting the \(2\)-frugal condition. Conversely, when there is no run of three occupied columns and adjacent occupied columns alternate rows, independence holds and no vertex can have three occupied neighbours: three such neighbours would give exactly the forbidden alternating triple. Therefore \(2\)-frugal independent sets are in bijection with binary cyclic occupancy words avoiding \(111\), together with a freely chosen starting row for each run of occupied columns, followed by row alternation within the run.

**Polynomial counting.** For a nonempty feasible set having \(k\) occupied columns and \(r\) cyclic runs of occupied columns, every run has length one or two. Exactly \(k-r\) of the \(r\) runs have length two, giving \(\binom r{k-r}\) choices. There are \(n-k\) empty columns, whose positive gaps between successive occupied runs are counted by \(\binom{n-k-1}{r-1}\) compositions. For cyclically labelled columns, choosing a designated first occupied run and its starting column gives \(n\) possible starting positions; each finished occupancy word is obtained exactly \(r\) times from designated runs. Hence the binary occupancy count is \(\frac nr\binom r{k-r}\binom{n-k-1}{r-1}\). Each run independently admits exactly two alternating row assignments. Multiplication by \(2^r\) gives the inner summand. The necessary and sufficient range is \(\lceil k/2\rceil\le r\le\min(k,n-k)\). Adding the empty set yields the complete displayed polynomial, with each set counted exactly once.

**Sharp maximum.** Each cyclic block of three consecutive columns contains at most two occupied columns. Summing this inequality over all \(n\) choices of block start gives \(3|S|\le2n\), so \(|S|\le\lfloor2n/3\rfloor\). For \(n=3t\), repeat the occupancy block \(110\) exactly \(t\) times; for \(n=3t+1\), use \((110)^{t-1}1100\); for \(n=3t+2\), use \((110)^t10\). (Here these three strings encode occupancy words, not mathematical exponentiation of graphs.) Each pattern has exactly \(\lfloor2n/3\rfloor\) occupied columns and no three consecutive ones, including across the cyclic seam. Colour every occupied run alternately by rows, choosing either starting row. This constructs a feasible set attaining the upper bound.

**Counts of maximum sets.** Substitute \(k=\lfloor2n/3\rfloor\) in the exact polynomial. If \(n=3t\), only \(r=t\) contributes, yielding \(3\cdot2^t\). If \(n=3t+1\), the two possible run counts \(r=t,t+1\) give \((3t+1)2^t\) and \((3t+1)t2^t\), respectively. If \(n=3t+2\), only \(r=t+1\) is possible, yielding \((3t+2)2^{t+1}\). These are the three displayed formulas. All constructions and counts work at the boundary \(n=3\).

## Verification

The bundled standard-library `verify.py` independently builds the actual graph on \(2n\) vertices, checks independence and the degree-three neighbourhood requirement for every assignment of columns as empty/first-row/second-row, and compares every coefficient of the enumeration formula at \(3\le n\le10\). It also tests the three closed maximum-set-count formulas and the cardinality bound for every \(3\le n\le80\). The infinite theorem follows from the exhaustive structural bijection and cyclic-run counting proof, not these finite checks.

## Relationship to prior work

Brešar, Hu and Samadi introduce the \(2\)-frugal independence number and prove general sharp cubic-graph bounds. Their results imply general inequalities but do not give this cycle-prism size distribution or maximum-set census. Earlier work on prism dynamic chromatic numbers and homogeneous colouring addresses partitions into several colour classes, not the count of a **single** frugal independent set. Even a complete enumerator of proper conflict-free colourings counts whole colourings rather than the polynomial of individual independent sets, and it need not determine the distribution of one admissible class. These are careful distinctions between mathematical statements, not novelty conclusions based solely on different titles.

## Limitations

The complete polynomial is specific to the width-two cycle prism family and to independent sets satisfying a maximum neighbourhood multiplicity of two. It does not enumerate arbitrary 2-frugal colourings, arbitrary cubic graphs, or general width. Historical priority remains provisional, and independent mathematical audit has not been performed.

## References

1. B. Brešar, W. Hu, B. Samadi, *Frugal coloring of graphs revisited*, arXiv:2602.02876, first submitted 2026-02-02, https://arxiv.org/abs/2602.02876.
2. Dafik, D. E. W. Meganingtyas, K. Dwidja Purnomo, M. Dicky Tarmidzi, I. Hesti Agustin, *Several classes of graphs and their r-dynamic chromatic numbers*, J. Phys. Conf. Ser. 855 (2017), 012011, https://doi.org/10.1088/1742-6596/855/1/012011.
3. T. Madaras, M. Šurimová, *Homogeneous colourings of graphs*, Mathematica Bohemica 148 (2023), 105--115, https://doi.org/10.21136/MB.2022.0007-21.
