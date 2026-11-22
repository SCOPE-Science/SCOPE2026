# Eight positive Fourier samples suffice and are necessary on five consecutive sites of twice-prime cycles

## Finding
Let \(p\) be an odd prime, \(N=2p\), \(\zeta=\exp(2\pi i/N)\), and \(A=\{0,1,2,3,4\}\subset\mathbb Z_N\). For distinct frequency indices \(J\subset\mathbb Z_N\), write \(v_j=(1,\zeta^j,\zeta^{2j},\zeta^{3j},\zeta^{4j})^\mathsf T\). Define \(M(p)\) as the smallest number of distinct positive-weighted characters forming a Parseval frame, that is, the smallest \(|J|\) for which some \(w_j>0\) satisfy
\[
\sum_{j\in J}w_jv_jv_j^*=I_5.
\]
Then the exact minimum is
\[
\boxed{M(p)=\begin{cases}6,&p=3,\\5,&p=5,\\7,&p=7,\\8,&p\ge11.\end{cases}}
\]
Moreover, for each odd prime \(p\ge11\), the proof gives an explicit positive eight-frequency Parseval rule without an optimization search. These are *weighted* characters with strict positivity on each selected frequency. No claim is made about equal-weight rules or classification of every optimizing support.

## Assumptions and scope
All arithmetic on indices is modulo \(2p\). The underlying Hilbert space is \(\mathbb C^5\) with coordinates on the specified consecutive spatial sites. The frame vectors are restrictions of the \(2p\)-character Fourier matrix without normalization; the positive weights normalize the frame operator to the identity. Equivalently, with \(z_j=\zeta^j\), the necessary and sufficient moments are
\[
\sum_{j\in J}w_j=1,\qquad\sum_{j\in J}w_jz_j^k=0\quad(1\le k\le4).
\]
Negative moments then vanish by complex conjugation. The quantity minimized counts distinct *nonzero* weighted frequencies, not total measurements with repetitions. The result concerns odd primes only and exactly five consecutive spatial sites.

## Proof
**Moment reduction.** The \((s,t)\) entry of the frame operator is \(\sum_jw_jz_j^{s-t}\). Therefore the frame identity is equivalent to the five nonnegative-frequency conditions displayed above, together with their conjugates. The rank of the identity implies \(|J|\ge5\).

**Nodal-polynomial obstruction.** Suppose a moment-exact measure has at most \(s\) distinct nodes, with \(5\le s\le8\). For purposes of this argument, augment its node set to exactly \(s\) elements with zero-weight roots if necessary, and let
\[
Q(z)=\prod_{j=1}^s(z-z_j)=\sum_{r=0}^{s}q_rz^r.
\]
Since \(Q\) vanishes on every positive-weight node, exactness through Laurent degree four gives
\[
0=\sum_jw_jz_j^{-4}Q(z_j)=q_4,
\]
because the other powers \(r-4\) lie between \(-4\) and \(4\), are nonzero, and have zero moment. Consequently, any measure supported on at most six roots forces the elementary symmetric sum \(e_2(z_1,\ldots,z_6)=0\) after augmentation to six nodes, and any measure supported on at most seven roots forces \(e_3(z_1,\ldots,z_7)=0\) after augmentation to seven nodes. Augmentation is possible in each case since the ambient group has at least six or seven elements in the cases used below.

**Cyclotomic parity obstruction.** Since \(p\) is odd, \(\Phi_{2p}(X)=\sum_{r=0}^{p-1}(-X)^r\); modulo \(p\), the substitution \(X=-1\) annihilates this polynomial. Thus \(\mathbb Z[\zeta]\to\mathbb F_p\) given by \(\zeta\mapsto-1\) is a valid ring homomorphism. If exactly \(a\) of \(s\) distinct selected frequencies are even, their images consist of \(a\) plus signs and \(s-a\) minus signs. The elementary symmetric sum has image
\[
E_k(a,s)=\sum_{\ell=0}^{k}(-1)^{k-\ell}\binom a\ell\binom{s-a}{k-\ell}\pmod p.
\]
For six roots, the integer list \(E_2(a,6)\), as \(a\) runs from zero to six, is \((15,5,-1,-3,-1,5,15)\). None vanishes modulo seven. Thus \(M(7)\ge7\). For seven roots, \(E_3(a,7)\), as \(a\) runs from zero to seven, is \((-35,-5,5,3,-3,-5,5,35)\). No member vanishes modulo any prime \(p\ge11\). Thus \(M(p)\ge8\) for all such primes. These are infinite-family obstructions, not extrapolations from finite enumeration.

**Small-prime witnesses.** For \(p=5\) and \(p=7\), choose precisely the \(p\) even frequencies \(0,2,\dots,2p-2\), each with weight \(1/p\). They form the full cyclic group of \(p\)-th roots, so the first four nonconstant Fourier moments vanish. Rank proves optimality at \(p=5\); the parity obstruction proves it at \(p=7\). At \(p=3\), the required moments at indices one through four and their conjugates exhaust all five nonzero Fourier modes on \(\mathbb Z_6\). Fourier inversion therefore forces the uniform measure on *all six* roots, proving \(M(3)=6\).

**Eight-node constructive witness for every \(p\ge11\).** Set
\[
a=\lfloor p/4\rfloor+1,\quad b=(p-1)/2,\quad
c=\cos(\pi a/p),\quad d=\sin(\pi/(2p)),\quad u=c^2,\quad v=d^2.
\]
One checks \(p/4<a<p/3\) for every odd prime \(p\ge11\) (directly at eleven, and using \(p/4+1<p/3\) thereafter). Consequently \(1/4<u<1/2\), while \(0<d<1/4\), so \(0<v<1/16<u\). Define
\[
D=\frac{4u-1}{8(1-v)(u-v)},\quad
C=\frac{1-4v}{8(1-u)(u-v)},\quad
E=\frac{3-4u-4v+8uv}{8(1-u)(1-v)},
\]
and
\[
\Delta_C=-\frac{d(1-v)}{c(1-u)}D,\qquad
\Delta_E=\frac{d(u-v)}{1-u}D
=\frac{d(4u-1)}{8(1-u)(1-v)}.
\]
The eight indices and weights are as follows:
\[
\begin{array}{c|c}
\text{frequency indices}&\text{weight per index}\\\hline
0&(E+\Delta_E)/2\\
p&(E-\Delta_E)/2\\
\pm a&(C+\Delta_C)/4\\
\pm(p-a)&(C-\Delta_C)/4\\
\pm b&D/2
\end{array}
\]
All signs refer to residues modulo \(2p\). The eight residues are distinct: \(0<a<b<p-a<p\), and their negatives give the other three nontrivial residues. Each weight is strictly positive. Indeed \(C,D>0\). Since \(u<1/2\), \(v<1/16\),
\[
3-4u-4v+8uv>3-2-\tfrac14=\tfrac34,
\]
while \(0<d(4u-1)<1/4\), proving \(E>\Delta_E>0\). Moreover
\[
C-|\Delta_C|=\frac{(c+d)(1-4cd)}{8c(1-u)(u-v)}>0,
\]
where \(4cd<1\) because \(c<1\) and \(d<1/4\).

To check all Fourier moments without approximations, merge conjugate frequencies into a real random variable \(X\) taking the five cosine values \(1,-1,c,-c,d\) with respective masses
\[
(E+\Delta_E)/2,\ (E-\Delta_E)/2,\ (C+\Delta_C)/2,\ (C-\Delta_C)/2,\ D.
\]
Direct substitution gives
\[
\mathbb E[1]=1,\quad\mathbb E[X]=0,\quad
\mathbb E[X^2]=\tfrac12,\quad\mathbb E[X^3]=0,\quad
\mathbb E[X^4]=\tfrac38.
\]
For example, the even equalities reduce to \(E+C+D=1\), \(E+uC+vD=1/2\), \(E+u^2C+v^2D=3/8\). The odd equalities reduce to \(\Delta_E+c\Delta_C+dD=0\) and \(\Delta_E+c^3\Delta_C+d^3D=0\). The Chebyshev identities
\[
T_1(X)=X,\quad T_2(X)=2X^2-1,\quad
T_3(X)=4X^3-3X,\quad T_4(X)=8X^4-8X^2+1
\]
show that the first four nontrivial *real* Fourier moments vanish. Conjugate pairing makes their imaginary parts vanish. Hence the frame operator is exactly \(I_5\), proving \(M(p)\le8\) and completing the classification.

## Verification
The proof is symbolic and uniform in the odd prime. The accompanying standalone `checker.py` verifies the two integer parity obstruction lists, exact moment identities using rational arithmetic, strict positivity and numerical Fourier-moment cancellation for all 91 odd primes from eleven to 501, and subgroup witnesses at the three exceptional primes. It uses only Python's standard library. Run `python checker.py` from the same folder as this document. Its finite tests are supplementary; the cyclotomic argument and the Chebyshev construction provide the infinite proof.

## Relationship to prior work
Marshall and Waldron study cyclic harmonic frames and their equivalence classes, providing the motivating finite Fourier-frame setting, but their counting results concern different optimization variables. Peherstorfer and Bultheel–Cruz-Barroso–Díaz Mendoza characterize broad classes of positive trigonometric quadratures and prescribed-node constructions; the arithmetic restriction to \(2p\)-th roots and the sharp support budget above are not established by the inspected statements. The known four-consecutive-site case concerns a smaller difference set and does not imply the five-site claim. The novelty assessment remains best-knowledge rather than a guarantee that all historical sources have been inspected.

## Limitations
Only odd-prime half-orders are classified. All weights are strictly positive, but are generally unequal. The theorem does not classify all minimizing frequency sets, optimize condition numbers beyond exact tightness, or address approximate/noisy sampling. It does not establish a broader theorem for composite half-orders. The independent mathematical audit has not been performed.

## References
- Simon Marshall and Shayne Waldron, *On the number of harmonic frames*, arXiv:1611.07121, first posted 22 November 2016, https://arxiv.org/abs/1611.07121.
- Franz Peherstorfer, *Positive trigonometric Quadrature Formulas and quadrature on the unit circle*, arXiv:1001.2451, https://arxiv.org/abs/1001.2451.
- Adhemar Bultheel, Ruymán Cruz-Barroso and Carlos Díaz Mendoza, *Zeros of quasi-paraorthogonal polynomials and positive quadrature*, arXiv:2110.10460, https://arxiv.org/abs/2110.10460.
