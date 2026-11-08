# Sharp prefix-normal deficit and first richest-factor positions in the period-doubling word

## Finding

Let \(\mathbf d=d_0d_1\cdots\) be the binary fixed point of \(\sigma(0)=01\), \(\sigma(1)=00\), beginning in \(0\). For \(n\geq0\), let \(F(n)=\sum_{i=0}^{n-1}d_i\), let \(M(n)\) (respectively \(L(n)\)) denote the largest (respectively smallest) number of ones in any factor of length \(n\) of \(\mathbf d\), and define the prefix-normal deficit \(D(n)=M(n)-F(n)\).

The complete deficit sequence has the exact base-four recursion
\[
D(0)=0,\quad D(4t)=D(t),\quad D(4t+1)=D(t)+1,\quad
D(4t+2)=D(t),\quad D(4t+3)=D(t+1)+d_t.
\]
For every integer \(r\geq1\), the sharp global envelope is
\[
\max_{1\leq n<4^r}D(n)=r.
\]
Put \(N_r=(4^r-1)/3\). Then
\[
F(N_r)=L(N_r)=\frac{N_r-r}{3},\qquad
M(N_r)=\frac{N_r+2r}{3},\qquad D(N_r)=r.
\]
The factor of length \(N_r\) starting at zero-based index \(N_r\) attains \(M(N_r)\), and **no earlier starting position** attains that maximal number of ones. Consequently there is no finite binary word \(v\) for which \(v\mathbf d\) is prefix normal with respect to ones.

## Assumptions and scope

All factors are finite contiguous substrings of the one-sided infinite word \(\mathbf d\); their starting indices are nonnegative integers. A binary word is prefix normal (with respect to symbol \(1\)) if the number of ones in each length-\(n\) factor is at most the number in its length-\(n\) prefix. For the infinite word this is required for every positive \(n\). An empty factor has weight zero. The theorem includes \(r=1\) and the zero-length conventions \(F(0)=L(0)=M(0)=D(0)=0\).

## Proof

**1. Four-block structure.** The substitution gives \(d_{2j}=0\) and \(d_{2j+1}=1-d_j\). Applying this twice yields
\[
(d_{4j},d_{4j+1},d_{4j+2},d_{4j+3})=(0,1,0,d_j).
\]
The prefix weight therefore satisfies, for \(k\geq0\),
\[
F(2k)=F(2k+1)=k-F(k),\qquad
F(4k+1)=k+F(k).
\]

**2. Extremal factor weights.** For a length-\(2k\) window, each of the two starting parities contains exactly \(k\) odd-indexed positions; their values are the complements of a length-\(k\) factor. For a length-\(2k+1\) window the two parities yield respectively \(k-W\) for a length-\(k\) factor and \(k+1-W'\) for a length-\(k+1\) factor. For either extremal weight, increasing the factor length by one changes its value by zero or one. It follows that, for \(k\geq1\),
\[
\begin{aligned}
M(2k)&=k-L(k),&L(2k)&=k-M(k),\\
M(2k+1)&=k+1-L(k+1),&L(2k+1)&=k-M(k).
\end{aligned}
\]
The odd relations also hold at \(k=0\), with \(M(1)=1\), \(L(1)=0\); the even relations hold at \(k=0\). They are exact for all positions of the infinite word, since either parity of a window realizes every factor of the desubstituted word.

**3. Deficit recursion and sharp envelope.** Insert the preceding relations in \(D(n)=M(n)-F(n)\) and simplify separately for the four residues modulo four. This gives exactly the displayed recursion, including the term \(F(t+1)-F(t)=d_t\) for residue three. We prove \(D(n)\leq r\) whenever \(0\leq n<4^r\) by induction. The base \(r=1\) follows from \(D(0),D(1),D(2),D(3)=(0,1,0,1)\). For \(n=4t+s<4^r\), the cases \(s=0,1,2\) follow immediately from \(t<4^{r-1}\), the recursion, and the induction bound. If \(s=3\), then \(D(n)=D(t+1)+d_t\). When \(t+1<4^{r-1}\), the induction bound again gives at most \(r\). In the only boundary case \(t+1=4^{r-1}\), repeated use of \(D(4t)=D(t)\) gives \(D(t+1)=D(1)=1\) and \(d_t=d_{4^{r-1}-1}=0\), since \(d_j=1\) exactly when the \(2\)-adic valuation of \(j+1\) is odd. Thus the bound holds. Since \(N_0=0\) and \(N_r=4N_{r-1}+1\), the recursion gives \(D(N_r)=D(N_{r-1})+1=r\), proving sharpness.

**4. Exact extrema at the witness lengths.** The same relations give \(L(4t+1)=t+L(t)\) and \(F(4t+1)=t+F(t)\). Hence \(L(N_r)=F(N_r)\), by induction from zero. The recurrence \(F(4t+1)=t+F(t)\) yields \(F(N_r)=(N_r-r)/3\). Since \(D(N_r)=r\), the formulas for \(M(N_r)\) and \(L(N_r)\) follow. Furthermore \(F(2N_r)=N_r-F(N_r)\), so the length-\(N_r\) factor starting at \(N_r\) contains \(F(2N_r)-F(N_r)=F(N_r)+r=M(N_r)\) ones.

**5. The first occurrence of a richest factor.** We show by induction that for \(N=N_r\) the maximum of the window weight \(W_N(i)=\sum_{j=i}^{i+N-1}d_j\), over \(0\leq i\leq N\), occurs only at \(i=N\). For \(r=1\), the first two bits \(01\) establish this. For the step let \(N=4K+1\), where \(K=N_{r-1}\). Write \(S_K(t)=\sum_{j=t}^{t+K-1}d_j\). The four-block identity from step 1 gives, for starts whose indices occur in \([0,N]\),
\[
\begin{aligned}
W_N(4t)&=K+S_K(t),\\
W_N(4t+1)&=K+1+S_K(t),\\
W_N(4t+2)&=K+S_K(t),\\
W_N(4t+3)&=K+S_K(t)+d_{t+K}.
\end{aligned}
\]
In the first three cases \(0\leq t\leq K\) when the start remains in \([0,N]\); the last case has \(0\leq t<K\). By induction \(S_K(t)<S_K(K)=M(K)\) for \(t<K\). Thus the last case is at most \(K+M(K)\), and the first and third cases are also at most \(K+M(K)\). The second case is maximized uniquely by \(t=K\), where it equals \(K+1+M(K)=W_N(N)=M(N)\), as required. Hence no factor starting before \(N\) can attain the global maximal weight.

**6. No finite prefix repair.** If a binary word \(v\) of length \(h\) were prepended, the length-\(N_r\) prefix of \(v\mathbf d\), for \(N_r>h\), would have at most \(h+F(N_r)\) ones. The unchanged factor \(\mathbf d[N_r..2N_r-1]\) still occurs after the inserted prefix and has \(F(N_r)+r\) ones. Taking \(r>h\) gives a contradiction to prefix normality.

## Verification

Run both independent standard-library Python scripts from the embedded `verifiers` directory:

```
python verifiers/verify_direct.py
python verifiers/verify_digital.py
```

The first constructs a substitution prefix of length \(32768\), compares direct factor min/max weights with the derived recurrences for lengths \(1\) through \(512\), and checks the unique earliest maximizers for \(r=1,\ldots,7\). The second uses the independent \(2\)-adic formula for bits and checks the four residue recurrences through length \(16384\), the sharp envelope for \(r\leq7\), and the witness identities. Both scripts passed. These finite calculations test the proof but do not replace the infinite induction.

## Relationship to prior work

Burcsi, Fici, Lipták, Ruskey and Sawada introduced computational uses of prefix-normal forms and the extremal-factor weight. Parreau, Rigo, Rowland and Vandomme analyzed (\(2\)-)abelian complexity and extremal Parikh counts of the period-doubling word, including via a coding of Thue–Morse factors. Those results determine factor-count envelopes; they do not explicitly specify the prefix-normal deficit relative to the *fixed leading prefix*, its sharp all-length logarithmic envelope, or the earliest starting position of the maximizing factor at the distinguished lengths. The earlier factor-weight results are acknowledged as strong surrounding coverage, rather than treated as irrelevant. A related result for the different ordinary paperfolding sequence establishes unbounded prefix-normal deficit, but not the present position-rigid period-doubling theorem.

## Limitations

The theorem gives the exact digit recursion for the deficit and the sharp envelope, but not a closed nonrecursive digit-sum formula for every argument. The first-maximizer assertion is restricted to \(N_r=(4^r-1)/3\); it does not classify all maximizing positions for arbitrary lengths. The scientific argument is internally reviewed and computationally checked but has not undergone independent mathematical or historical-priority validation. Existing all-length abelian-extremum recurrences make the numerical portion particularly close to prior work; the explicit first-occurrence rigidity is the essential additional claim.

## References

- P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Combinatorial Generation of Prefix Normal Words*, arXiv:1401.6346v1, first publicly posted January 24, 2014. https://arxiv.org/abs/1401.6346
- A. Parreau, M. Rigo, E. Rowland and E. Vandomme, *A new approach to the 2-regularity of the ℓ-abelian complexity of 2-automatic sequences*, arXiv:1405.3532v1, first publicly posted May 14, 2014. https://arxiv.org/abs/1405.3532
- Published comparison: result concerning prefix-normal deficit of the *ordinary paperfolding word* (distinct substitution and statement), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-unbounded-prefix-normal-defect-of-the-ordinary-paperfolding-word--a7708413f1f3
