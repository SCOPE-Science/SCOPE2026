# A sharp upper-coskewness transition for pairwise-independent uniform ternary variables

## Finding
For each real \(t>1\), let \(X,Y,Z\) have common uniform marginal law on \(\{0,1,t\}\), and assume every two coordinates are independent. Their triple product satisfies the **sharp, attained** upper bound
\[
\sup\mathbb E[XYZ]=\begin{cases}\frac{t^2}{3},&1<t\le 2,\\[2pt]\frac{t^3+2t}{9},&t\ge 2.\end{cases}
\]
At \(1<t<2\), the optimizer is unique, and necessarily \(\mathbb P(X=Y=Z=t)=0\). At \(t>2\), every optimizer has \(\mathbb P(X=Y=Z=t)=1/9\). At the transition \(t=2\), all simultaneous-top-atom probabilities from \(0\) through \(1/9\) are attained by optimizers. These are laws with pairwise independence, not necessarily joint independence.

Writing \(\mu=(1+t)/3\), the identical sharp bound for centered third-order dependence is
\[
\sup\mathbb E[(X-\mu)(Y-\mu)(Z-\mu)]
=\begin{cases}\frac{t^2}{3}-\mu^3,&1<t\le2,\\[2pt]\frac{t^3+2t}{9}-\mu^3,&t\ge2.\end{cases}
\]

## Assumptions and scope
The statement concerns precisely three variables, each equally likely to take the three distinct real values \(0,1,t\), with \(t>1\). Independence is imposed on all three ordered pairs. No continuity, exchangeability, or joint-independence assumption is imposed. Supremums range over all joint laws on the \(27\) labeled triples with these two-coordinate margins.

## Proof
Let \(v_0=0\), \(v_1=1\), and \(v_2=t\). A joint probability mass array \(p_{ijk}\) is feasible exactly when each of its three families of two-way margins is uniform: for distinct coordinate choices, each ordered pair of digits occurs with probability \(1/9\).

**Pair-potential certificate.** For a positive parameter \(d\), define a symmetric function \(H\) on pairs of digits by
\[
H_{00}=H_{11}=H_{12}=d,\qquad
H_{01}=H_{02}=-\frac d2,\qquad H_{22}=\frac{t^3}{3}.
\]
We claim that with the choices of \(d\) given below,
\[
H_{ij}+H_{ik}+H_{jk}\ge v_i v_j v_k
\quad\text{for every }i,j,k\in\{0,1,2\}.
\]
By symmetry it suffices to check the ten sorted triples. Their differences (left minus right) are
\[
\begin{array}{c|cccccccccc}
\text{digits}&000&001&002&011&012&022&111&112&122&222\\\hline
\text{difference}&3d&0&0&0&0&t^3/3-d&3d-1&3d-t&t^3/3+2d-t^2&0.
\end{array}
\]

If \(1<t\le2\), put \(d=t^2(3-t)/6\). Then the differences for \(022\), \(111\), \(112\), and \(122\) are respectively
\[
\frac{t^2(t-1)}2,\quad \frac{t^2(3-t)}2-1,\quad
\frac{t(t-1)(2-t)}2,\quad 0.
\]
They are nonnegative because \(t^2(3-t)/2\) increases from \(1\) to \(2\) on \([1,2]\). The remaining differences are manifestly nonnegative. If \(t\ge2\), put \(d=t/3\). The same four differences are
\[
\frac{t(t^2-1)}3,\quad t-1,\quad 0,\quad
\frac{t(t-1)(t-2)}3,
\]
again nonnegative. This establishes the pointwise certificate throughout the domain.

Taking expectations of the certificate and using pairwise independence gives
\[
\mathbb E[XYZ]\le\frac{1}{3}\sum_{i,j=0}^2 H_{ij}
=\frac13\left(2d+\frac{t^3}{3}\right).
\]
For \(1<t\le2\) this expression is \(t^2/3\); for \(t\ge2\) it is \((t^3+2t)/9\).

**Exact attaining couplings.** Choose independent uniform digits \(I,J\in\{0,1,2\}\). For the first law, set \(K_A\equiv-I-J-1\pmod3\); for the second, set \(K_B\equiv I-J-1\pmod3\). Each map is a Latin square in \((I,J)\), so the three digit coordinates are pairwise independent and uniform. Assign numerical values by \((X,Y,Z)=(v_I,v_J,v_K)\). In law A, precisely three of the nine equiprobable triples have nonzero product, each of pattern \((1,2,2)\), hence \(\mathbb E_A[XYZ]=t^2/3\). In law B, the nonzero contributions are one \((2,2,2)\) triple and two \((1,1,2)\) triples, hence \(\mathbb E_B[XYZ]=(t^3+2t)/9\). The appropriate law attains each bound.

**Optimizer rigidity.** When \(1<t<2\), the certificate has strictly positive slack for triple patterns \(000,022,111,112\). Consequently an optimizer may be supported only on permutations of \(001,002,011,012,122,222\). The uniform \((1,1)\) pair margin must be exhausted by the only allowed triple \((0,1,1)\), whose mass is therefore \(1/9\) in each positional permutation. These atoms exhaust the \((0,1)\) pair margins, forcing the types \(001\) and \(012\) to be absent. The \((0,0)\) and \((1,2)\) pair margins then force respectively every permutation of \(002\) and \(122\) to have mass \(1/9\); the \((2,2)\) pair margins rule out \(222\). Thus law A is the unique optimizer. In particular its all-top probability vanishes.

When \(t>2\), both types \(022\) and \(122\) have positive slack; the only zero-slack type containing a pair \((2,2)\) is \(222\). The fixed pair probability \(\mathbb P(X=Y=t)=1/9\) must therefore be concentrated at the all-top triple. At \(t=2\), laws A and B both attain the common bound. Their mixtures attain every all-top mass in \([0,1/9]\); a pairwise margin gives the reverse upper bound. This proves the stated transition.

Finally, expansion of the centered product and pairwise independence show
\(\mathbb E[(X-\mu)(Y-\mu)(Z-\mu)]=\mathbb E[XYZ]-\mu^3\), proving the centered claim.

## Verification
The accompanying standalone exact-rational program `check.py` verifies all \(27\) pointwise dual inequalities and the pairwise margins and objectives of the two Latin-square laws at twelve rational values of \(t\) on both sides of, and at, the transition. It also checks the strict-region permitted support types and the excluded two-upper-atom pattern. The run reports `PASS: 1136 exact-rational conditions for 12 thresholds`. The program is a finite consistency check; the displayed symbolic certificate and margin argument prove the continuum-in-\(t\) theorem.

Run with `python3 check.py` using the Python standard library. No external data files are needed.

## Relationship to prior work
A later comparison by Gvozdev and Kolesnikov, *On Pairwise Independent and Strongly Correlated Random Variables* (2026), treats maximization of centered triple moments under pairwise independence via \((3,2)\)-multistochastic transport, proving Sierpinski-tetrahedron optimality for a class of dyadic-digit score functions. The present three-equal-atom score with variable upper spacing is a discrete, non-dyadic family and has a sharp optimizer switch not established by the inspected results. Gladkov, Kolesnikov, and Zimin (2018) treat related continuous-uniform multistochastic product costs. Bernard, Chen, Rüschendorf, and Vanduffel (2023) treat coskewness bounds when only univariate margins are fixed; pairwise independence is a stricter constraint. None of the inspected statements implies the exact two-branch formula or its rigidity assertions.

## Limitations
The theorem concerns only equal masses at three specified support values, up to positive affine changes of the support coordinate. It does not classify unequal masses, arbitrary discrete marginals, or minimizers of centered coskewness. It does not imply universal optimization by Latin squares in larger transport problems. Historical equivalents under different terminology remain possible; independent validation has not been performed.

## References
1. C. Bernard, J. Chen, and S. Vanduffel, *Modeling coskewness with zero correlation and correlation with zero coskewness*, arXiv:2412.13362v1 (first publicly submitted 2024-12-17). https://arxiv.org/abs/2412.13362
2. D. Gvozdev and A. Kolesnikov, *On Pairwise Independent and Strongly Correlated Random Variables*, arXiv:2611.20365v1 (publicly submitted 2026-11-16; later related work). https://arxiv.org/abs/2611.20365
3. A. Gladkov, A. Kolesnikov, and A. Zimin, *On multistochastic Monge–Kantorovich problem, bitwise operations, and fractals*, arXiv:1803.10447 (2018). https://arxiv.org/abs/1803.10447
4. C. Bernard, J. Chen, L. Rüschendorf, and S. Vanduffel, *Coskewness under dependence uncertainty*, arXiv:2303.17266 (2023). https://arxiv.org/abs/2303.17266

