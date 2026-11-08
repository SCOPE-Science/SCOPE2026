# A sharp geometric-mean connectivity criterion for periodically decorated hierarchical flowers

## Finding
For any integer \(k\geq1\), let \(p_1,\ldots,p_k\in[0,1]\) be shortcut occupation probabilities repeated periodically by hierarchical generation in a decorated \((2,2)\)-flower. Each ordinary bond is initially open with probability \(q\in[0,1]\), independently. Write \(P_n(q)\) for the probability that the two original roots are connected after \(n\) generations.

**Theorem (sharp uniform forcing criterion).** If
\[
\prod_{j=1}^k(1-p_j)\leq\left(\frac{27}{32}\right)^k
\]
and \((p_1,\ldots,p_k)\neq(5/32,\ldots,5/32)\), then
\[
\lim_{n\to\infty}P_n(q)=1\qquad\text{for every }q\in[0,1].
\]
The constant \(27/32\) is optimal for a sufficient condition based only on the geometric mean of shortcut nonoccupation probabilities. In particular, if the arithmetic mean \(\bar p=k^{-1}\sum_j p_j\) is at least \(5/32\), then the limit is one for every initial \(q\), except for the homogeneous critical profile at exact equality. Thus arbitrarily small nonconstant modulation at the critical average forces full root connectivity. At the excluded homogeneous critical profile \(p_j=5/32\), the initial condition \(q=0\) instead converges to root connectivity \(1/3\).

In particular, the two-periodic profiles \((p_1,p_2)=(3/10,0)\) and \((3/20,3/20)\) have exactly the same arithmetic mean shortcut probability \(3/20\), but starting with \(q=0\) the former has limiting root connectivity \(1\), whereas the latter converges to a value strictly between \(0\) and \(1/3\). Thus averaging the periodic shortcut probabilities can give the wrong root-connectivity phase.

## Assumptions and scope
The generation-zero graph is one ordinary edge between two designated roots, independently open with probability \(q\). To form generation \(n+1\), take four independent copies of the generation-\(n\) two-root network; join two copies in series, join another two copies in series, and place these paths in parallel between their roots. Add one independent direct shortcut between those roots, open with probability \(p_{1+(n\bmod k)}\). Shortcuts are retained and are not themselves recursively replaced. All primitive bond states are independent. Parallel edges are allowed and count as independent bonds.

Define \(f_p(x)=1-(1-p)(1-x^2)^2\) on \([0,1]\). Root connectivity obeys the exact recursion \(P_0(q)=q\) and \(P_{n+1}(q)=f_{p_{1+(n\bmod k)}}(P_n(q))\). The conclusion concerns two-root connection probability, not a giant-component density or a critical cluster exponent.

## Proof
**1. Exact reduction.** A root connection at level \(n+1\) occurs if the new shortcut is open, or either of the two disjoint two-copy series paths is connected. Each two-copy path connects with probability \(P_n(q)^2\), and the paths and shortcut are independent. Therefore the probability of disconnection is \((1-p_j)(1-P_n(q)^2)^2\), proving the recursion.

**2. Periodic fixed-point obstruction.** Let \(F=f_{p_k}\circ\cdots\circ f_{p_1}\). As a composition of continuous nondecreasing maps of \([0,1]\), \(F\) maps this interval to itself and fixes \(1\). If \(F(x_0)=x_0<1\) and any \(p_j=1\), the whole period ends at \(1\), a contradiction. Otherwise set \(x_j=f_{p_j}(x_{j-1})\), with \(x_k=x_0\). Every \(x_j<1\). Writing \(u_j=1-x_j>0\), the recurrence is
\[
\frac{u_j}{u_{j-1}}=(1-p_j)(1-x_{j-1})(1+x_{j-1})^2=(1-p_j)h(x_{j-1}),
\quad h(x)=(1-x)(1+x)^2.
\]
Multiplying the \(k\) identities around the period yields the exact constraint
\[
1=\prod_{j=1}^k(1-p_j)\prod_{j=0}^{k-1}h(x_j).
\]
The algebraic identity
\[
\frac{32}{27}-h(x)=\frac{(3x-1)^2(3x+5)}{27}\geq0\qquad(0\leq x\leq1)
\]
shows that \(h(x)\leq32/27\), with equality only at \(x=1/3\). Hence every nonunit period-fixed orbit requires
\[
\prod_{j=1}^k(1-p_j)\geq\left(\frac{27}{32}\right)^k.
\]
Equality forces \(x_j=1/3\) for all \(j\), and the original recurrence then forces \(p_j=5/32\) for every \(j\). This excludes all nonunit fixed points of \(F\) under the theorem's hypotheses.

**3. Convergence for all initial values.** The product assumption implies that at least one \(p_j>0\), so \(F(0)>0\). Because \(F(1)=1\) and \(F\) has no fixed point in \([0,1)\), continuity implies \(F(x)>x\) throughout \([0,1)\). Consequently the iterates \(F^m(q)\) increase to their only possible fixed point \(1\). The finitely many intermediate phase subsequences also converge to \(1\), since every \(f_p(1)=1\). This proves the assertion for all generations.

**4. Arithmetic-mean corollary.** By the arithmetic–geometric mean inequality, \[\left(\prod_{j=1}^k(1-p_j)\right)^{1/k}\leq 1-\bar p,\qquad \bar p=\frac1k\sum_{j=1}^k p_j,\] with equality only for a constant profile. If \(\bar p>5/32\), the sharp sufficient criterion holds strictly; if \(\bar p=5/32\) and the profile is nonconstant, it again holds strictly. The equality exception is the homogeneous critical profile.

**5. Sharpness.** At \(p_j=5/32\) for every \(j\), the one-step map fixes \(x=1/3\), and
\[
f_{5/32}(x)-x=\frac{(1-x)(3x-1)^2(3x+5)}{32}.
\]
Starting with \(q=0\), the increasing iteration converges to \(1/3\), not \(1\). Moreover, for homogeneous \(p<5/32\) sufficiently close to \(5/32\), \(f_p(0)>0\) and \(f_p(1/3)<1/3\), so an attracting fixed point lies in \((0,1/3)\). Any replacement of \(27/32\) by a larger geometric-mean upper bound would admit such a homogeneous profile and give a false universal guarantee.

**6. An exact mean-matched separation.** For \((p_1,p_2)=(3/10,0)\), the product \((1-p_1)(1-p_2)=7/10<729/1024\), so all initial \(q\) converge to \(1\). For \((p_1,p_2)=(3/20,3/20)\), the exact values \(f_{3/20}(0)=3/20>0\) and \(f_{3/20}(1/3)-1/3=-2/405<0\) give a stable fixed point in \((0,1/3)\); iteration from \(q=0\) converges to its smallest fixed point. The profiles have the same arithmetic mean \(3/20\), completing the separation.

## Verification
The standalone \(\texttt{verify.py}\) reconstructs the five-independent-bond series-parallel event exactly using rational arithmetic, verifies the polynomial identity for \(h\) on a rational grid, checks the two rational threshold inequalities, and compares the long-run behavior of the mean-matched schedules. Executing \(\texttt{python3 verify.py}\) produced `PASS: 437 independent exact-rational/numerical assertions`. The all-generation and sharpness conclusions follow from the preceding analytic proof, not from finite computation.

## Relationship to prior work
Berker, Hinczewski and Netz (2009), and Hasegawa, Sato and Nemoto (2010), established the constant-shortcut renormalization framework and its homogeneous critical value \(5/32\). The latter's full-text model and results equations use one shortcut probability held constant across levels. The present finding concerns arbitrary fixed finite periodic schedules and gives a sharp geometric-mean sufficient condition and an exact failure of arithmetic averaging. A 2014 flower-network paper by Lee, Shim and Noh treats degree-ordered site percolation, rather than independently occupied period-modulated shortcut bonds. These earlier conclusions do not by themselves imply the new periodic result; they supply its exact homogeneous baseline.

## Limitations
The product criterion is sufficient, not claimed necessary for each nonuniform profile. It determines a sharp *uniform* threshold over all periodic profiles, not the full critical surface for arbitrary parameters. The result concerns root-to-root connectivity and does not assert a positive-density giant component, cluster fractal dimension, or universality class. The independent scientific literature comparison is not exhaustive, and an earlier general theorem for periodically forced hierarchical recurrences could subsume some aspects of this specialization.

## References
1. A. N. Berker, M. Hinczewski and R. R. Netz, *Critical Percolation Phase and Thermal BKT Transition in a Scale-Free Network with Short-Range and Long-Range Random Bonds*, arXiv:0907.0825 (first public 2009-07-05), Phys. Rev. E **80**, 041118 (2009). https://arxiv.org/abs/0907.0825
2. T. Hasegawa, M. Sato and K. Nemoto, *Generating-function approach for bond percolations in hierarchical networks*, arXiv:1004.5087 (first public 2010-04-28), Phys. Rev. E **82**, 046101 (2010). https://arxiv.org/abs/1004.5087
3. H. K. Lee, P.-S. Shim and J. D. Noh, *Degree-ordered percolation on hierarchical scale-free network*, arXiv:1403.2072 (first public 2014-03-09), Phys. Rev. E **89**, 062816 (2014). https://arxiv.org/abs/1403.2072
