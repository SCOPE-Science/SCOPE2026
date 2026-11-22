# Exact multilevel inverse-fiber spectrum of indexed cyclic window-sum reads

## Finding
Fix integers \(q\ge2\), \(n\ge2\), and \(1\le\ell\le n\). Define the indexed cyclic integer-sum channel on \(x\in\{0,\ldots,q-1\}^n\) by
\[
R_\ell(x)_i=\sum_{j=0}^{\ell-1}x_{(i+j)\bmod n},\quad 0\le i<n.
\]
Let \(d=\gcd(n,\ell)\) and \(m=n/d\). In residue class \(r\bmod d\), subtract the minimum entry of the length-\(m\) ordered subword to obtain its *normalized pattern* \(u^{(r)}\); set \(h_r=\max u^{(r)}\), \(w_r=q-1-h_r\), and let \(s\) be the sum of the original class minima. **Two inputs have identical indexed read vectors if and only if all their normalized patterns agree and their sums \(s\) agree.** The exact inverse-list size for that read vector is
\[
\boxed{L(u^{(0)},\ldots,u^{(d-1)},s)=[z^s]\prod_{r=0}^{d-1}(1+z+\cdots+z^{w_r}).}
\]
Every integer \(0\le s\le\sum_r w_r\) gives one distinct attainable read vector for each tuple of normalized patterns. This is a complete output-by-output inverse-fiber classification, not just a worst-case bound.

For \(h=0,\ldots,q-1\), the number of normalized length-\(m\) class patterns with maximum \(h\) is
\[
c_{m,h}=\begin{cases}1,&h=0,\\ (h+1)^m-2h^m+(h-1)^m,&1\le h\le q-1.\end{cases}
\]
Consequently the exact number \(N_j\) of output vectors having exactly \(j\) sources, for every integer \(j\ge1\), is
\[
N_j=\sum_{h_0,\ldots,h_{d-1}=0}^{q-1}\!\left(\prod_r c_{m,h_r}\right)
\sum_{s=0}^{\sum_r(q-1-h_r)}
\mathbf 1\!\left\{[z^s]\prod_r\sum_{t=0}^{q-1-h_r}z^t=j\right\}.
\]
In particular, the number of distinct read vectors, equivalently the exact largest noiseless zero-error code size, is
\[
\boxed{A_{q,n,\ell}=\bigl(q^m-(q-1)^m\bigr)^{d-1}
\bigl(q^m+(d-1)(q-1)^m\bigr).}
\]
If \(d=1\) the channel is injective. If \(d\ge2\), the sharp maximum inverse-list size is
\[
\boxed{\max_y |R_\ell^{-1}(y)|=[z^{\lfloor d(q-1)/2\rfloor}](1+z+\cdots+z^{q-1})^d.}
\]
Only constant read vectors attain this bound: exactly one does so when \(d(q-1)\) is even and exactly two when it is odd.

The nonbinary collision spectrum is already richer in the first resonant ternary case \(q=d=3\) (so \(n=3m\) and \(\gcd(n,\ell)=3\)). Write \(u=2^m-2\) and \(v=3^m-2^{m+1}+1\). Then the complete list-size distribution is
\[
\begin{aligned}
N_1={}&2u^3+6u^2v+6u^2+6uv^2+12uv+6u+v^3+9v^2+6v+2,\\
N_2={}&3v(u^2+4u+2),\\
N_3={}&2u^3+6u^2+6u+3v+2,\\
N_4={}&3u^2,\quad N_5=6u,\quad N_6=2,\quad N_7=1.
\end{aligned}
\]
All other \(N_j\) vanish. For \(m=2\) the frequencies for list sizes one through seven are respectively \(254,84,60,12,12,2,1\), totaling \(425\) outputs from \(729\) sources.

## Assumptions and scope
Symbols are integers \(0,\ldots,q-1\), not residues of a finite field. Read sums are ordinary integers, not reduced modulo \(q\). Both source positions and output coordinates are indexed, with all \(n\) wraparound windows retained. Rotations are distinct indexed sources, and the cyclic origin is known. The case \(\ell=n\) is included: the read vector is constant with its \(n\) entries all equal to the total source sum.

An *inverse fiber* is the set of all indexed source words with the same complete output vector. A *zero-error code* for this noiseless deterministic channel contains at most one source from each fiber, and choosing one from each fiber attains its maximum size.

## Proof
**Kernel and normalization.** Write \(a_i=x'_i-x_i\) for two source words and use the identity
\[
R_\ell(x)_{i+1}-R_\ell(x)_i=x_{i+\ell}-x_i.
\]
If read vectors agree, their difference satisfies \(a_{i+\ell}=a_i\) for every \(i\), so \(a_i\) is constant on each of the \(d\) residue classes modulo \(d\). Conversely, if \(a_i=t_r\) on the class \(r\), then every length-\(\ell\) cyclic window contains exactly \(\ell/d\) entries from each class, giving
\[
R_\ell(x')_i-R_\ell(x)_i=(\ell/d)\sum_{r=0}^{d-1}t_r.
\]
Thus equality of reads is equivalent to constant differences within each class and \(\sum_r t_r=0\). Coordinatewise constant shifts preserve and are detected by the normalized class patterns; their shift constants are exactly the changes in the class minima. Hence equality of read vectors is equivalent to equality of all normalized patterns together with equality of the sum of class minima.

**All inverse fibers.** For a fixed normalized class pattern with maximum \(h_r\), adding any class minimum \(b_r\in\{0,\ldots,q-1-h_r\}\) produces a legal source, and every legal source of that normalized type arises uniquely this way. The only remaining readout invariant is \(s=\sum_r b_r\), so the number of sources for a given output is the coefficient at \(z^s\) in the displayed product. Since each factor has all coefficients one from degree zero through \(w_r\), the product has strictly positive coefficients at every integer degree between zero and \(\sum_r w_r\), proving that no output was missed. For fixed normalized patterns, distinct \(s\) yield distinct read vectors; distinct normalized patterns also yield distinct read vectors by the equivalence already proved.

**All multiplicities and image size.** A length-\(m\) normalized pattern with maximum \(h\ge1\) must contain both zero and \(h\); inclusion–exclusion among the \((h+1)^m\) words on \(\{0,\ldots,h\}\) gives \(c_{m,h}\). For \(h=0\), the sole pattern is all zero. Summing one output per possible coefficient position \(s\) for each normalized tuple proves the formula for \(N_j\). Let \(P\) be the set of normalized length-\(m\) words, with \(|P|=q^m-(q-1)^m=:a\). For each pattern \(u\), write \(w(u)=q-1-\max u\). Each original length-\(m\) word decomposes uniquely into \(u\) and an offset \(0\le b\le w(u)\). Consequently \(\sum_{u\in P}(w(u)+1)=q^m\), or \(\sum_{u\in P}w(u)=(q-1)^m=:b\). For a \(d\)-tuple of normalized patterns, there are \(1+\sum_r w(u_r)\) outputs. Summing gives \(a^d+dba^{d-1}\), the stated image-size formula.

**Sharp list size.** Each factor \(1+\cdots+z^{w_r}\) is coefficientwise dominated by \(1+\cdots+z^{q-1}\), so each inverse list is bounded by the largest coefficient of \((1+\cdots+z^{q-1})^d\). Symmetry and unimodality of this product place its largest coefficient at the central degree(s); unimodality follows inductively because each new coefficient is a sum over a contiguous interval of a symmetric unimodal sequence. Taking every normalized pattern to be the constant zero pattern attains this bound. If \(d\ge2\) and any \(w_r<q-1\), the central coefficient strictly decreases: choose the excluded exponent \(q-1\) in that factor, and distribute the remaining central degree among the other \(d-1\) factors, possible because \(\lfloor d(q-1)/2\rfloor\ge q-1\) and the residual degree is at most \((d-1)(q-1)\). Thus all extremal normalized patterns are constant zero, and central offset sums yield exactly one or two constant read vectors according to parity. For \(d=1\), every list is singleton, as immediate from a single factor with coefficients one.

**Explicit ternary three-residue spectrum.** When \(q=d=3\), a normalized class has shift width \(2,1,0\) with respective multiplicities \(1,u,v\). For each of the \(3^3\) possible ordered width triples, expand the product of its three length-\(w_r+1\) all-one polynomials, tally its coefficients by value, and weight by the product of the respective \(1,u,v\). Collecting these finite expansions yields exactly the seven displayed polynomials. This is an exhaustive symbolic identity valid for every \(m\ge1\), not an extrapolation from numerical examples.

## Verification
Run `python3 verify.py` with Python 3 and the standard library. The independent checker directly constructs the \(n\) cyclic integer window sums for every source and groups exact output tuples by their preimage counts, without using the normalized-pattern inverse algorithm. It separately computes the proposed inverse-frequency formula from normalized-pattern widths and compares the distributions for all \(168\) parameter triples comprising \(q=2\) with lengths \(2\) through \(12\), \(q=3\) with lengths \(2\) through \(9\), \(q=4\) with lengths \(2\) through \(7\), and \(q=5\) with lengths \(2\) through \(6\), testing every permitted window length. This covers \(599{,}000\) independently enumerated source instances counting repeats across window lengths. It also checks the exact image formula, total fiber mass \(q^n\), central maximum, and specialized ternary three-residue spectrum through \(m=3\). All checks completed successfully. Finite computation corroborates but cannot substitute for the proof for arbitrary parameters.

## Relationship to prior work
Yerushalmi, Etzion and Yaakobi (2024) analyze the **noncyclic** linear weighted-read channel and its asymptotic coding capacity. Their general-alphabet reduction (Theorem 1) applies to their noncyclic model and does not supply the present cyclic inverse-fiber spectrum, nor its finite-block image sizes. Earlier work on transverse reads likewise uses linear rather than complete indexed cyclic windows.

A public 2026 study entitled *Exact fiber and constant-weight capacity laws for cyclic binary weighted reads* provides the analogous theory **only for \(q=2\)**, in which pure residue classes create binomial inverse lists. The present all-alphabet theorem does not claim that binary special case as new. Its nonbinary fibers instead have bounded-composition coefficient laws, an explicitly different central-multinomial maximum, and a seven-level ternary spectrum. A separate public 2026 study entitled *Exact capacity and ambiguity of one-erased cyclic weighted reads* treats loss of a known read coordinate. That study proves that erasure is redundant when the gcd is nontrivial, without presenting a complete nonbinary full-read inverse-fiber enumeration; its coprime, erased-coordinate formula does not determine the noncoprime list-size spectrum here.

These comparisons distinguish different models and mathematical implications, rather than using titles alone. A differently indexed result in integer circulant tomography or earlier unpublished work could still contain equivalent formulas.

## Limitations
This is an exact noiseless indexed cyclic scalar-integer-sum model, not a statement about biochemical nanopore behavior. It does not treat a multiset of unindexed reads, noisy or missing observations, nonunit read strides, general digit sets with gaps, modular sums, or arbitrary weighted kernels. The q-ary formulas specialize to previously known binary phenomena; originality attaches to the multilevel spectrum and associated exact nonbinary enumeration. No independent mathematical audit has been conducted.

## References
1. O. Yerushalmi, T. Etzion and E. Yaakobi, *The Capacity of the Weighted Read Channel*, arXiv:2401.15368v1, first posted 2024-01-27. https://arxiv.org/abs/2401.15368.
2. A. Banerjee, A. Yehezkeally, A. Wachter-Zeh and E. Yaakobi, *Correcting a Single Deletion in Reads from a Nanopore Sequencer*, arXiv:2401.15939v1, first posted 2024-01-29. https://arxiv.org/abs/2401.15939.
3. Y. M. Chee, A. Vardy, V. K. Vu and E. Yaakobi, *Transverse-Read-Codes for Domain Wall Memories*, IEEE Journal on Selected Areas in Information Theory 4 (2023), DOI:10.1109/JSAIT.2023.3334303.
4. *Exact fiber and constant-weight capacity laws for cyclic binary weighted reads*, public research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fiber-and-constant-weight-capacity-laws-for-cyclic-binary--21136e4ec91c.
5. *Exact capacity and ambiguity of one-erased cyclic weighted reads*, public research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-capacity-and-ambiguity-of-one-erased-cyclic-weighted-reads--9ee0bce770fc.
