# The crystallographic period spectrum of a greedy rotating walk

## Finding
Let \(p,q\) be coprime integers with \(q\in\{1,2,3,4,6\}\), and set \(u_n=\exp(2\pi i pn/q)\). Starting at any \(z_{-1}\in\mathbb C\), define a greedy trajectory by choosing the point of \(z_{n-1}\pm u_n\) nearer the origin. As in the originating definition, **stop** the trajectory when these two distances are equal. Every trajectory that does not stop is eventually periodic in position, with the following **complete least-period spectrum**:

\[
\begin{array}{c|c}
q & \text{possible eventual least position periods}\\\hline
1,2&\{2\}\\
3,6&\{3,6\}\\
4&\{4\}
\end{array}
\]

Every listed period occurs. This is a result about positions, not an assertion that the recorded plus/minus signs have the same least period.

## Assumptions and scope
For \(n\ge 0\), if \(\operatorname{Re}(z_{n-1}\overline{u_n})\ne0\), the unique minimizing choice is
\[
z_n=z_{n-1}-\operatorname{sgn}\!\left(\operatorname{Re}(z_{n-1}\overline{u_n})\right)u_n.
\]
If the real part is zero, the trajectory terminates without a tie-breaking rule. The claim concerns all initial complex numbers, including those on switching boundaries, subject only to nontermination. The reduced denominator condition is essential; only the five crystallographic rational denominators are classified. The source that introduced this rule primarily studies *irrational* rotation parameters; no assertion is made here about irrational parameters or the remaining rational denominators.

## Proof
**1. The one-dimensional and orthogonal cases.** For \(q=1\) or \(2\), the set \(\{\pm u_n\}\) equals \(\{\pm1\}\) at every time. The imaginary part stays fixed, while the real part follows the greedy map \(t\mapsto t-\operatorname{sgn}(t)\). Every nonterminating orbit eventually alternates between two points. For \(q=4\), the unoriented step axes alternate between the real and imaginary coordinate axes. Each coordinate follows this same one-dimensional greedy map at alternate steps. Once both coordinates have entered their two-cycles, the full trajectory has least period four: it cannot have period two because in two steps each coordinate changes by a nonzero unit amount.

**2. A rigorous uniform absorbing disk for \(q=3,6\).** Write \(Z_j\) for the position before the \(j\)-th step of a full \(q\)-step block, with \(Z_0=Z\). At every non-tied step,
\[
|Z_{j+1}|^2-|Z_j|^2=1-2|\operatorname{Re}(Z_j\overline{u_j})|,
\qquad |Z_j-Z|\le j.
\]
Consequently, with \(c_q=\min_{|w|=1}\sum_{j=0}^{q-1}|\operatorname{Re}(w\overline{u_j})|\),
\[
|Z_q|^2-|Z|^2\le q^2-2c_q|Z|.
\]
The unoriented directions of the triangular lattice have angular separation \(\pi/3\). Equivalently, the three cosine projections have zero sum and their absolute-value sum is twice the largest projection. Thus \(c_3=\sqrt3\) and \(c_6=2\sqrt3\). Let \(h_q=q^2/(2c_q)\). Outside radius \(h_q\), the squared norm strictly decreases on each complete block.

All positions at a fixed block phase belong to a translate of the discrete Eisenstein lattice \(\mathbb Z+\mathbb Z\omega\), with \(\omega=e^{2\pi i/3}\). Therefore a strictly decreasing sequence of block radii cannot remain forever outside \(h_q\): otherwise it would visit infinitely many distinct lattice points in a compact disk. Once a block starts within \(h_q\), its next start has radius at most \(h_q+q\). Moreover, the disk of radius \(h_q+q\) is forward invariant for full blocks, since outside \(h_q\) the radius decreases and inside it the displacement of a block is at most \(q\). In particular, every nonterminating trajectory eventually enters, at block phase zero, the invariant disk of radius \(R_3=6\) or \(R_6=12\), respectively, because
\[
3+\frac{9}{2\sqrt3}<6,\qquad 6+\frac{36}{4\sqrt3}<12.
\]

**3. Exact reduction to thirty-nine rational strata.** Write \(Z=a+b\omega\), where \(a=m+r\), \(b=n+s\), \(m,n\in\mathbb Z\) and \(0\le r,s<1\). This fractional pair \((r,s)\) is unchanged by every step. For a step direction \(u+v\omega\), the sign of the real projection is the sign of
\[
2au+2bv-av-bu.
\]
For both relevant denominators, all directions, up to sign, are \(1\), \(\omega\) and \(1+\omega\). Thus every decision depends only on one of \(2r-s\), \(2s-r\), and \(r+s\), shifted by an integer. The only interior switching lines in the unit square are
\[
2r-s\in\{0,1\},\qquad 2s-r\in\{0,1\},\qquad r+s=1.
\]
Including square boundaries, these lines split the closed unit square into exactly **ten open two-dimensional faces, nineteen open edges and ten vertices**. Within each of these thirty-nine strata, every integer-offset orbit has the same symbolic transitions or ties. The closed square is deliberately used for an overcomplete partition; points with fractional coordinate one represent an equivalent coordinate-zero state with shifted integer offset.

The lattice norm identity \(|a+b\omega|^2=a^2-ab+b^2\) gives \(|a|,|b|\le 2|Z|/\sqrt3\). Hence every phase-zero state in the radius-six disk has \(m,n\in[-8,8]\cap\mathbb Z\); every state in the radius-twelve disk has \(m,n\in[-15,15]\cap\mathbb Z\). These rectangular ranges deliberately overcover the disks uniformly over the entire stratum. It remains to inspect **all** \(39(17^2+31^2)=48{,}750\) stratum/offset combinations.

**4. Complete exact finite-state certificate.** The attached `verify.py` constructs the line arrangement using `Fraction` arithmetic. It checks area conservation at each polygon cut, independently constructs every vertex and open-edge representative from exact line intersections, and proves the 39 sign-signatures are distinct. For each stratum and each integer offset in the rigorous overcovering rectangle it follows the full three- or six-step affine return map, distinguishing ties from cycles. The entire finite search uses exact rational signs; it does not extrapolate from sampled initial points.

For \(q=3\), every non-tied recurrent block cycle has length one or two, giving original-time period three or six. For \(q=6\), every non-tied recurrent six-step block cycle is a fixed point. A further exact three-step test distinguishes original-time period three from six. No smaller positive period is possible: a nonzero step of least position period \(d\) must repeat its unoriented direction after \(d\) steps, and these directions have least forcing period three for both \(q=3\) and \(q=6\). The program checks that no finite graph trajectory escapes classification. Finally, its four explicit rational initial states show each of periods three and six actually occurs for both denominators. Reflection \(z\mapsto\overline z\) covers the other reduced numerator in each denominator. This completes the proof.

## Verification
Run `python3 verify.py` using Python 3.9 or later with no dependencies outside the standard library. The certificate returns `EXHAUSTIVE_RATIONAL_STRATA_CERTIFICATE_OK`. For both denominators, the 39 parameter strata have the same period-set histogram: all 10 faces have both periods; among 19 edges, 14 have both and five have only period three; among 10 vertices, six have only period three and four only period six. The exact checker inspects all 48,750 stratum/offset starts. Its maximum number of previously unseen block states on a traced path is six for denominator three and five for denominator six. The program's checks have been executed on the packaged source. The analytic trapping bound, rather than the finite search alone, justifies exhaustive coverage of unbounded initial positions.

## Relationship to prior work
Steinerberger and Zeng introduced the nearest-origin signed rotating walk in *A curious dynamical system in the plane*, arXiv:2409.08961, first publicly posted September 13, 2024. Their principal eventually-periodic-sign criteria explicitly assume irrational rotation and require an observed sustained sign pattern. They pose period questions in the irrational setting; those criteria do not imply unconditional periodicity for all initial points at rational angles. The present result addresses the entire crystallographic rational subfamily and establishes an exact position-period spectrum, rather than simply using periodic signs as a hypothesis. Albors, Clément, Kiami, Sodt, Yifan and Zeng, *Approximately Jumping Towards the Origin*, arXiv:2412.04284, study a stochastic model and a deterministic van der Corput direction sequence, not the periodic crystallographic direction sequences classified here. Published-results searches did not identify a covering prior classification; this is not a mathematical proof of publication priority.

## Limitations
The theorem excludes orbits terminating at exact ties, as prescribed by the original stopping convention. It gives eventual **position** periods, not exact time-to-capture for every initial point, a global sign-word census, or any claim for rational denominators outside \(\{1,2,3,4,6\}\). The finite certificate is an exact calculation conditional on the proved trapping bound and stratum completeness, not an independent formal proof checker. Equivalent statements may remain in unindexed literature. Independent mathematical audit has not been performed.

## References
1. S. Steinerberger and T. Zeng, *A curious dynamical system in the plane*, arXiv:2409.08961 (first posted 2024-09-13), https://arxiv.org/abs/2409.08961.
2. A. Albors, F. Clément, S. Kiami, B. Sodt, D. Yifan and T. Zeng, *Approximately Jumping Towards the Origin*, arXiv:2412.04284 (first posted 2024-12-05), https://arxiv.org/abs/2412.04284.
