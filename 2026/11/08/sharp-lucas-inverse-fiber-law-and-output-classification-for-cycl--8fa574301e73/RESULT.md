# Sharp Lucas inverse-fiber law and output classification for cyclic Rule 28

## Finding

Consider the synchronous elementary cellular automaton of Wolfram rule 28 on a binary ring of indexed length \(n\). Every possible output has a definite number of one-step predecessors. The maximum and all maximizing outputs admit a complete description, including the short-ring exceptions.

Define Lucas numbers by \(L_0=2\), \(L_1=1\), \(L_{j+2}=L_{j+1}+L_j\). Let \(P_n(y)\) be the number of indexed predecessors of an indexed output word \(y\in\{0,1\}^n\), and set \(M_n=\max_y P_n(y)\). Then

\[
M_n=\begin{cases}
2,&1\le n\le3,\\
L_{\lfloor n/2\rfloor},&n\ge4.
\end{cases}
\]

For \(1\le n\le3\), the all-zero word is the *only* maximizing output. For even \(n=2m\ge4\), the only maximizing outputs are the two indexed alternating words \((01)^m\) and \((10)^m\). For odd \(n=2m+1\ge5\), the maximizing outputs are exactly the \(n\) distinct rotations of \(001(01)^{m-1}\). Equivalently, their \(m\) ones are isolated, exactly one cyclic gap between them contains two zeros, and all other gaps contain one zero.

An exact formula for *every* fiber also holds. If an output \(y\) has \(k\ge1\) ones, with cyclic zero-run gaps \(r_1,\ldots,r_k\in\mathbb Z_{\ge0}\), set

\[
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
F=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
B_r=\begin{cases}E&r=0,\\F&r\ge1.\end{cases}
\]

Then

\[P_n(y)=\operatorname{tr}\bigl(B_{r_1}\cdots B_{r_k}\bigr),\qquad P_n(0^n)=2.\]

## Assumptions and scope

The state at each site belongs to \(\{0,1\}\). For input \(x\), indices are modulo \(n\), and output \(y_i=f(x_{i-1},x_i,x_{i+1})\) uses the local rule with value one exactly on the neighborhoods \(010\), \(011\), and \(100\) and zero on the other five neighborhoods. These three neighborhoods represent Wolfram number 28. All sites update simultaneously, with no stochasticity. Both inputs and outputs are **indexed** words: rotation-equivalent words are not identified in the counts. The rule is defined for every \(n\ge1\), including rings whose radius-one neighborhoods repeat indices. No assertion is made about asynchronous updates, higher-step inverse images, or inverse classes modulo rotation.

## Proof

**Step 1: the de Bruijn transfer trace.** Order two-bit states as \(00,01,10,11\). A labeled edge \((a,b)\to(b,c)\) receives label \(f(a,b,c)\). The two adjacency matrices are

\[
Z=\begin{pmatrix}
1&1&0&0\\0&0&0&0\\0&1&0&0\\0&0&1&1
\end{pmatrix},\qquad
O=\begin{pmatrix}
0&0&0&0\\0&0&1&1\\1&0&0&0\\0&0&0&0
\end{pmatrix}.
\]

For any output \(y_0\cdots y_{n-1}\), closed labeled paths of length \(n\) in the two-bit de Bruijn graph correspond bijectively to indexed predecessor words \(x\) with the indicated output, including when \(n\) equals one or two. Thus

\[P_n(y)=\operatorname{tr}(M_{y_0}\cdots M_{y_{n-1}}),\quad M_0=Z,\quad M_1=O.\]

A direct multiplication gives \(Z^3=Z^2\) and \(\operatorname{tr}(Z)=\operatorname{tr}(Z^2)=2\); hence \(P_n(0^n)=2\) for every positive \(n\).

**Step 2: reduction to gap matrices.** The trace is invariant under cyclic reorderings. For an output with at least one one, read from any one and write its cyclic label string as \(1 0^{r_1}1 0^{r_2}\cdots1 0^{r_k}\). Multiplication shows \(OZ^r=OZ\) for all \(r\ge1\). Both \(O\) and \(OZ\) have nonzero rows only among states \(01\) and \(10\). Their restrictions to these same two columns are, respectively, \(E\) and \(F\), as displayed above. In any product of such matrices the trace is exactly that of the corresponding two-dimensional restricted product. This establishes the stated exact fiber formula.

**Step 3: no adjacent output ones.** If all \(r_i\ge1\), the formula gives \(P_n(y)=\operatorname{tr}(F^k)=L_k\). The last identity follows either by Cayley–Hamilton, \(F^2=F+I\), or by its eigenvalues: the trace sequence has initial values 2 and 1 and obeys the Lucas recurrence. Since every one is followed by at least one zero, \(2k\le n\). For \(n\ge4\), the largest possible value is \(L_{\lfloor n/2\rfloor}\), achieved when the number of ones is maximal. The sequence is strictly increasing from \(L_1\) onward, since \(L_1=1\), \(L_2=3\), and subsequent terms increase.

**Step 4: adjacent ones strictly lose.** Let \(j\ge1\) gaps be zero and \(t=k-j\) gaps be positive. If every gap is zero, the product is \(E^k\), whose trace is zero. If two zero gaps are consecutive in the cyclic order, the product contains \(E^2=0\), again giving zero. Otherwise all \(j\) zero gaps are isolated. Pair each \(E\) in the cyclic product with the following \(F\); there are at least \(j\) such \(F\) matrices. Each pair is

\[EF=G=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad 0\le G\le F\quad\text{entrywise}.\]

The trace of a product of nonnegative matrices is monotone under an entrywise increase of any factor (by expanding the trace into nonnegative monomials). Replacing all paired \(G\) by \(F\), and leaving the other \(F\) factors intact, yields

\[P_n(y)\le\operatorname{tr}(F^t)=L_t.\]

The total length satisfies \(n=k+\sum_i r_i\ge(k+t)=2t+j\). For even \(n=2m\ge4\), this implies \(t\le m-1\) and thus \(P_n(y)\le L_{m-1}<L_m\) when \(t\ge1\). For odd \(n=2m+1\ge5\), when \(j\ge2\) the same strict conclusion holds. When \(j=1\) and \(t\le m-1\), it also holds. The sole remaining possibility is \(j=1,t=m\), which forces every positive zero gap to equal one; its product has exactly one \(E\) and \(m\) copies of \(F\). The Fibonacci-matrix identity \(\operatorname{tr}(EF^m)=F_m^{\mathrm{Fib}}\) gives a strict inequality \(F_m^{\mathrm{Fib}}<L_m\) for \(m\ge2\). (Here \(F_m^{\mathrm{Fib}}\) denotes the usual Fibonacci number, not the matrix \(F\).) Thus no output containing adjacent ones can maximize. All cases with \(t=0\) were already treated separately.

**Step 5: optimizer classification and short rings.** For \(n\ge4\), a maximizing output must therefore have no adjacent ones and have exactly \(\lfloor n/2\rfloor\) ones. On an even ring these are the two alternating indexed words; on an odd ring, precisely the \(n\) rotations of the word with a single length-two zero gap, since the maximal independent sets of an odd cycle have just one such gap. For \(n=1,2,3\), the zero output has two predecessors. Direct use of the exact \(E/F\) formula shows each nonzero output has at most one, completing the proof. \(\square\)

## Verification

The self-contained, Python-standard-library program `verify_rule28.py` independently builds the one-step map directly from the Wolfram truth table. For every \(1\le n\le17\), it exhaustively enumerates all indexed source words, independently tallies their outputs, compares every one of the 262,142 output fibers with the gap-matrix formula, and checks both the maximum and the complete set of maximizers. It additionally verifies the displayed transfer-matrix reductions and 596 longer extremal profiles through length 599. Run `python3 verify_rule28.py`; successful output starts with `VERIFY_OK`. These finite checks do not constitute an infinite proof: the five algebraic steps above establish the result for all positive lengths.

## Relationship to prior work

Wolfram's 1983 foundational treatment establishes the elementary-rule setting. Jen (1989) develops general predecessor-enumeration methods for elementary automata and studies maximal-probability finite linear strings; Section 5.4 explicitly notes alternating optimizers for Rule 76, but does not give this exact **periodic Rule 28** Lucas maximum with its all-length uniqueness classification. Fukś (2003) studies sequences counting \(t\)-step preimages of fixed short blocks, distinct from a single synchronous update on \(n\)-site rings. Voorhees (1996) gives periodic predecessor computations for local-rule compositions; its discussed subfamily does not yield the present optimizer theorem. Macauley–McCammond–Mortveit study Rule 28 under asynchronous update orders, a different global transformation. Established de Bruijn and Fibonacci transfer-matrix techniques are used here, but the exact cyclic Rule 28 bound and all equality cases were not found in the inspected sources. The same combinatorial objects have been checked against published mathematical result records and accessible historical claim lists; no equal or stronger result was identified. Lack of a match does not establish historical novelty.

## Limitations

Only one synchronous update of Rule 28 on indexed binary rings is treated. We make no claim about other rules, open boundaries, iteration depth, or rotation-quotiented inverse multiplicities. Searches are not exhaustive across unindexed preimage tables, older computational surveys, or unpublished supplements to Jen's classification; a prior equivalent formula may exist. The result has been reviewed for correctness and overlap using the sources listed, but has not undergone independent mathematical audit.

## References

1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* **55** (1983), 601–644. https://doi.org/10.1103/RevModPhys.55.601
2. E. Jen, “Enumeration of Preimages in Cellular Automata,” *Complex Systems* **3** (1989), 421–456. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
3. H. Fukś, “Sequences of Preimages in Elementary Cellular Automata,” *Complex Systems* **14** (2003), 29–43. https://wpmedia.wolfram.com/uploads/sites/13/2018/02/14-1-2.pdf
4. B. Voorhees, “Computation of Predecessor States for Composite Elementary Cellular Automata,” *Complex Systems* **10** (1996), 207–217. https://content.wolfram.com/sites/13/2018/02/10-3-4.pdf
5. M. Macauley, J. McCammond, and H. S. Mortveit, “Dynamics Groups of Asynchronous Cellular Automata,” arXiv:0808.1238. https://arxiv.org/abs/0808.1238
