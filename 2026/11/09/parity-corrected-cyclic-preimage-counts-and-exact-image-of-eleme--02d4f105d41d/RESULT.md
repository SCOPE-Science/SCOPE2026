# Parity-corrected cyclic preimage counts and exact image of elementary Rule 126

## Finding

Fix an integer \(n\geq1\). Elementary Rule 126 sends an indexed binary cyclic configuration \(x\in\{0,1\}^n\) to \(y\in\{0,1\}^n\) via
\[
y_i=0\quad\Longleftrightarrow\quad (x_{i-1},x_i,x_{i+1})\in\{(0,0,0),(1,1,1)\},
\]
with all indices modulo \(n\). Write \(d_n(y)=|\{x:F_{126,n}(x)=y\}|\), and let \(F_0=0,F_1=1\), \(F_{r+2}=F_{r+1}+F_r\), \(L_n=F_{n-1}+F_{n+1}\). For a path of \(k\) vertices define its independence polynomial \(Q_k(t)=\sum_{I\text{ independent}}t^{|I|}\); set \(Q_{-1}(t)=Q_0(t)=1\).

**Theorem.** The complete inverse-fiber formula, including every indexed output, is:

1. If \(y=0^n\), then \(d_n(y)=2\).
2. If \(y=1^n\), then
\[
 d_n(y)=L_n+\begin{cases}2,&3\mid n,\\-1,&3\nmid n.\end{cases}
\]
3. Otherwise write the cyclic maximal runs of zeros and ones as alternating blocks, and let \(q\) be the number of zeros, \(s\) the number of zero runs, and \(\ell_1,\ldots,\ell_s\) the lengths of the intervening one runs. If any \(\ell_j=1\), then \(d_n(y)=0\). If every \(\ell_j\geq2\), then
\[
 d_n(y)=\prod_{j=1}^{s} Q_{\ell_j-3}(1)
 +(-1)^{n-q-s}\prod_{j=1}^{s}Q_{\ell_j-3}(-1).
\]
In particular \(Q_{\ell-3}(1)=F_{\ell-1}\). The cyclic image consists of the two constant outputs when they have positive fiber and precisely those mixed outputs whose one runs all have length at least two, and for which either some one run has length at least four or \(n-q-s\) is even. The all-one output has no predecessor for \(n=1\); otherwise it is realizable. For \(n\geq3\), \(1^n\) is the **unique** output with the maximum predecessor count. At \(n=1\), only \(0\) attains the maximum two; at \(n=2\), both \(00\) and \(11\) attain the maximum two.

The condition is genuinely global. For example, the cyclic output \(011\) has no \(010\) factor but is nevertheless excluded by \(n-q-s\equiv1\pmod2\).

## Assumptions and scope

The alphabet is binary; every site is labeled (not quotiented by rotation or complementation); the update is synchronous; its neighborhood is the radius-one cyclic triple, including repeated indices for \(n=1,2\); and only one backward step is counted. A distinct precursor means a distinct indexed length-\(n\) configuration. The parity and run formulas refer to target \(y\), never to a free-boundary word or an infinite-lattice event.

## Proof

Define cyclic differences \(a_i=x_i\oplus x_{i+1}\) and their complements \(m_i=1-a_i\). A triple is constant exactly when both adjacent differences vanish, so
\[
 y_i=1-m_{i-1}m_i.
\]
Necessarily \(\bigoplus_i a_i=0\), equivalently \(\sum_i m_i\equiv n\pmod2\). Conversely every cyclic \(m\) of this parity integrates to exactly two binary \(x\)'s (choice of \(x_0\)), proving a two-to-one correspondence between eligible \(m\)'s and Rule-126 precursors.

For \(y=0^n\), all neighboring pairs of \(m\)'s equal \(11\), forcing \(m=1^n\). Its parity is eligible and produces exactly two precursors.

For \(y=1^n\), the \(m\)'s are independent sets of the cyclic adjacency graph, with parity \(\sum m\equiv n\pmod2\). The two-to-one integration factor cancels the projection's half, so the fiber count is \(I_n(1)+(-1)^nI_n(-1)\), with \(I_n\) the circular independence polynomial. The hard-core transfer matrix \(B(t)=\begin{pmatrix}1&1\\t&0\end{pmatrix}\) gives \(I_n(t)=\operatorname{tr}B(t)^n\), also for lengths one and two under the cyclic-neighbor convention. The eigenvalue traces are \(I_n(1)=L_n\) and \(I_n(-1)=2\cos(n\pi/3)\), hence \((-1)^n I_n(-1)=2\cos(2n\pi/3)\), equal to two or minus one by divisibility by three.

For a mixed \(y\), each zero run of length \(r\) forces the corresponding \(r+1\) consecutive \(m\)-sites to one, giving \(q+s\) forced ones in total. Two zero runs separated by a one run of length one would force neighboring \(m\)'s to one across a required output one, an immediate contradiction. For a permissible one run of length \(\ell\geq2\), its two boundary-adjacent \(m\)'s must be zero; the \(\ell-3\) interior freely selected positions (none if \(\ell=2\) or three) must contain no adjacent ones. This gives the path independence factor \(Q_{\ell-3}(t)\) and the total generating polynomial
\[
 t^{q+s}\prod_{j=1}^{s} Q_{\ell_j-3}(t).
\]
Parity extraction at \(t=1,-1\), followed by the factor two for integration, proves the stated mixed-fiber formula. If every one run has length two or three, every path factor is one and the unique candidate \(m\) is eligible precisely when \(n-q-s\) is even. If any one run has length at least four, toggling its first free site exhibits both parities, proving the complete image criterion.

Finally, for any mixed output, \(Q_{\ell-3}(1)=F_{\ell-1}\leq\varphi^{\ell-2}\) for \(\varphi=(1+\sqrt5)/2\), whence
\[
 d_n(y)\leq2\prod_jF_{\ell_j-1}\leq2\varphi^{n-q-2s}\leq2\varphi^{n-3}.
\]
For \(n\geq3\), the all-one count is at least \(\varphi^n-2>2\varphi^{n-3}\), while the all-zero count is two. Thus \(1^n\) uniquely maximizes. The cases \(n=1,2\) follow directly from the first two formula cases.

## Verification

`verify_formula.py` directly enumerates all \(2^n\) cyclic sources and all \(2^n\) targets for every \(1\leq n\leq15\), compares the formula fiber by fiber, checks image total, and verifies maximizers; it prints `FORMULA_VERIFY_OK`. `verify_transfer.py` independently constructs the four-state de Bruijn transition matrices for Rule 126 and compares their product trace with a separate cyclic parity dynamic program for all targets through \(n=12\) and a reproducible selection of longer targets through \(n=64\); it prints `TRANSFER_VERIFY_OK`. Both are standard-library-only executable Python source included with this result. These finite tests support but do not replace the all-length proof.

## Relationship to prior work

Jen (1989) explicitly derives Fibonacci-product preimage formulas for Rule 126 on finite observation strings in the **infinite-lattice/free-boundary** setting (Section 3, type C). Consequently neither preimage recurrences in general nor Rule-126 Fibonacci factors are claimed new. Gómez Soto (2006) describes general de Bruijn-based finite and periodic preimage enumeration, and the standard cyclic matrix-trace identity is known. The distinct finite-ring result established here is the parity-corrected closed formula for each **cyclic** Rule-126 target, the exact image criterion including global Garden-of-Eden exclusions, and the proof of the unique maximal fiber. Generic matrix methods imply computational accessibility but the inspected texts do not state these explicit classifications. Prior-work priority remains qualified.

## Limitations

No multistep preimage tree, attractor distribution, or other rule is classified. No general result about nonperiodic or free-boundary Rule 126 is claimed. Historical priority is not independently certified; the 1989 open-boundary formulas and generic cyclic algorithms could facilitate subsequent independent derivations, and unexamined specialist tabulations may overlap. The attached software has finite test horizons, although the mathematical proof is all-length.

## References

- E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems 3 (1989), 421–456, especially Section 3: https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
- J. M. Gómez Soto, *Computation of Explicit Preimages in One-Dimensional Cellular Automata Applying the De Bruijn Diagram*, Santa Fe Institute Working Paper 2006-02-005: https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/1d/57/1d572536-1018-4d3e-9b10-6806b2e59e6c/06-02-005.pdf
- G. J. Martínez et al., *How to make dull cellular automata complex by adding memory: Rule 126 case study*, arXiv:1212.0124v1, submitted 2012-12-01: https://arxiv.org/abs/1212.0124
- *Cellular Automata/Counting Preimages*, Wikibooks, section on cyclic preimage matrix traces: https://en.wikibooks.org/wiki/Cellular_Automata/Counting_Preimages
