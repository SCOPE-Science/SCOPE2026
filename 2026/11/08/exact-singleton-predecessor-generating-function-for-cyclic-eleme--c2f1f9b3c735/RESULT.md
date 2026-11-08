# Exact singleton-predecessor generating function for cyclic elementary Rule 54

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous elementary Rule 54 map on a **labeled** binary ring with \(n\geq1\). In cyclic indices its update is
\[
(F_n(x))_i=x_i\mathbin{\oplus}(x_{i-1}\lor x_{i+1}).
\]
Let \(u_n\) be the number of indexed targets \(y\in\{0,1\}^n\) for which \(F_n^{-1}(\{y\})\) consists of exactly one indexed input. Then for all \(n\geq1\),
\[
\sum_{n\geq1}u_nz^n=\frac{P(z)}{Q(z)},
\]
where
\[
\begin{aligned}
P(z)={}&3z^3-15z^5+24z^6-8z^7-10z^8+12z^9-10z^{10}\\
 &-7z^{11}+17z^{12}-23z^{13}+12z^{14}-3z^{15}+2z^{16},\\
Q(z)={}&1-4z+6z^2-4z^3-z^4+6z^5-7z^6+2z^7\\
 &+3z^8-3z^9+z^{10}+z^{11}-2z^{12}+2z^{13}-z^{14}.
\end{aligned}
\]
In particular, the exact values \((u_1,\ldots,u_{18})\) are
\[
(0,0,3,12,15,24,49,96,162,270,462,806,1378,2366,4105,7176,12512,21789).
\]
This is an all-length identity, not a conjecture extrapolated from these coefficients.

## Assumptions and scope

The alphabet is fixed and binary, the ring sites are individually indexed, and both input and output have the same positive length. Rotations and reflections are **not** identified. The count is for **one** simultaneous application of Rule 54; it is not a multi-step preimage count, nor the different reversible lattice-gas model sometimes also called Rule 54. For bookkeeping set \(u_0=0\), outside the theorem's positive-length domain.

## Proof

**1. Closed walks exactly encode cyclic predecessors.** Order the four length-two overlap states as \(00,01,10,11\). For \(d\in\{0,1\}\), the output-labeled de Bruijn edge matrix \(A_d\), for output digit \(d\), records a transition \(ab\to bc\) when the local Rule 54 output of \(abc\) is \(d\). Explicitly these matrices, with zero/one integer entries, are
\[
A_0=\begin{pmatrix}1&0&0&0\\0&0&0&1\\0&0&0&0\\0&0&1&1\end{pmatrix},\qquad
A_1=\begin{pmatrix}0&1&0&0\\0&0&1&0\\1&1&0&0\\0&0&0&0\end{pmatrix}.
\]
For every indexed cyclic output \(y=y_0\cdots y_{n-1}\), its number of indexed predecessors is exactly
\[
\operatorname{tr}(A_{y_0}\cdots A_{y_{n-1}}).
\]
Indeed each closed path fixes the successive length-two input windows; their overlaps reconstruct exactly one indexed input, including for \(n=1,2\), and every input determines one such closed path.

**2. Saturating at two preserves singleton detection.** Let \(\sigma(t)=\min(2,t)\) for nonnegative integers. Since \(\sigma(a+b)=\sigma(\sigma(a)+\sigma(b))\) and \(\sigma(ab)=\sigma(\sigma(a)\sigma(b))\), entrywise saturation defines a semiring matrix product \(X\star Y=\sigma(XY)\). For every output, saturating each matrix product does not change whether its diagonal sum is exactly one. Denote the finite set of matrices reachable from the identity \(I\) by successive right multiplication by \(A_0\) or \(A_1\) under \(\star\) by \(\mathcal M\). Exhaustive breadth-first closure with the explicitly given generators proves \(|\mathcal M|=410\), including \(I\). The full enumerator and closure checks are in `verify_finite_state.py`.

**3. A finite integer vector certificate yields the recurrence for all lengths.** Let \(T\) be the \(410\)-state adjacency operator with one edge for each of the two labeled right-multiplication transitions. Define the column \(f\) by \(f(X)=1\) exactly when the (ordinary integer) sum of the four diagonal entries of saturated \(X\) equals one, and zero otherwise. Then
\[
u_n=(T^n f)(I).
\]
Write \(Q(z)=\sum_{j=0}^{14}q_j z^j\), with its integer coefficients displayed above. The finite certificate proves the **exact vector identity**
\[
T^3\left(\sum_{j=0}^{14}q_j T^{14-j}\right)f=0
\]
on all \(410\) entries, not merely on initial coefficients. Consequently \(\sum_{j=0}^{14}q_j u_{n-j}=0\) for every \(n\ge17\). The program constructs every reachable state from scratch, verifies closure, forms each integer vector, and checks every entry of this identity.

**4. Initial terms fix the generating function.** The same exact integer transitions give
\[
(u_0,u_1,\ldots,u_{16})=(0,0,0,3,12,15,24,49,96,162,270,462,806,1378,2366,4105,7176).
\]
Multiplying the series by \(Q(z)\) and using the all-length recurrence gives precisely \(P(z)\), including coefficients through degree \(16\) and zero coefficients beyond. This proves the claimed rational identity over formal power series with integer coefficients.

## Verification

Run `python3 verify_finite_state.py` from the extracted directory. It independently builds the entire saturated matrix semigroup, checks its \(410\)-state closure, verifies the degree-\(14\) recurrence certificate on **every state** after three transition steps, and tests the first \(90\) series coefficients and the numerator identity. It prints `CERTIFICATE_OK` on success. Run `python3 verify_direct.py`; this second implementation never uses de Bruijn matrices and instead evaluates the local cellular rule directly on all \(2^n\) indexed inputs for each \(1\le n\le18\), producing `DIRECT_OK`. These experiments are auxiliary cross-checks; the finite vector identity is what proves all lengths.

## Relationship to prior work

Jen (1989) gave general one-step preimage recurrences for arbitrary finite blocks and proved that the infinite-lattice one-step Rule 54 image is a finite-forbidden-block regular language (Section 5.1 and Appendix A). That result addresses forbidden blocks and individual block multiplicities, not the number of **all periodic targets with exactly one periodic predecessor** as a function of ring size. Powley's 2009 thesis and Powley–Stepney (2010) provide cyclic de Bruijn methods and count preimages of particular, especially homogeneous, configurations; their stated target is a fixed configuration rather than the exact distribution of singleton fibers across all target words. Fukś (2003; arXiv upload 2013) primarily studies multiple-time-step preimages of elementary blocks. The present all-length singleton-fiber rational series is a separate enumeration, though it uses the established de Bruijn methodology.

## Limitations

The theorem is restricted to elementary Wolfram Rule 54, one update, labeled cyclic rings, and singleton fibers. The degree-\(14\) rational identity is computationally certified by exhaustive finite state closure and exact integer arithmetic; the supplied scripts are part of the proof. This does not classify the individual singleton targets in a simple pattern language, count higher preimage multiplicities, or extend to other rules. Priority against unindexed historical numerical tables and otherwise inaccessible related work remains a limitation; no independent scientific audit is asserted.

## References

- E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems **3** (1989), 421–456, especially pp. 444–446 and 453–454. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
- E. J. Powley, *Global properties of cellular automata*, University of York doctoral thesis (2009), Chapter 9. https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf
- E. J. Powley and S. Stepney, *Counting Preimages of Homogeneous Configurations in 1-Dimensional Cellular Automata*, Journal of Cellular Automata **5** (2010), 353–381. https://pure.york.ac.uk/portal/en/publications/counting-preimages-of-homogeneous-configurations-in-1-dimensional/
- H. Fukś, *Sequences of Preimages in Elementary Cellular Automata*, Complex Systems **14** (2003), 29–43; arXiv upload 2013-05-28, https://arxiv.org/abs/1305.6533
