# Fixed-value Fibonacci-partition fibers have exact affine cutoff counts

## Finding

Let \(f_1=1\), \(f_2=2\), and \(f_{i+2}=f_{i+1}+f_i\) for \(i\ge1\). For \(n\ge0\), let \(R(n)\) be the number of subsets of \(\{f_1,f_2,\ldots\}\) whose elements sum to \(n\), with \(R(0)=1\). For any fixed integer \(k\ge1\), set
\[
C_k(L)=\#\{0\le n<f_{L+1}:R(n)=k\}\qquad(L\ge0).
\]
There is an effectively computable integer polynomial \(P_k(z)\), of degree at most \(2k^2+2k+2\), for which \(P_k(1)>0\) and
\[
\boxed{\sum_{L\ge0}C_k(L)z^L=\frac{P_k(z)}{(1-z)^2}+\frac{\mathbf1_{k=1}}{1-z}.}
\]
Consequently, for all sufficiently large integers \(L\),
\[
\boxed{C_k(L)=P_k(1)(L+1)-P_k'(1)+\mathbf1_{k=1},}
\]
and, with \(\varphi=(1+\sqrt5)/2\),
\[
\boxed{\#\{0\le n<X:R(n)=k\}=\frac{P_k(1)}{\log\varphi}\log X+O_k(1)}
\qquad (X\to\infty).
\]
In particular, the complete fixed-value census at \(k=12\) has
\[
P_{12}(z)=8z^{11}+16z^{12}+8z^{13}+4z^{14}+4z^{15}+2z^{23}+2z^{24},
\]
so that \(C_{12}(L)=44L-550\) exactly for every \(L\ge24\). This is a level-set statement, not an assertion that the partition function is bounded or typical.

## Assumptions and scope

All parts are distinct; the two conventional Fibonacci occurrences of \(1\) are not treated as two different parts. The sole \(1\) is \(f_1\), while \(f_2=2\). Every positive integer has a unique Zeckendorf expansion \(n=f_{i_0}+\cdots+f_{i_s}\), where \(i_0>\cdots>i_s\ge1\) and consecutive indices differ by at least two. The cutoff \(n<f_{L+1}\) is equivalent to \(i_0\le L\). The results quantify over every fixed \(k\ge1\), every integer \(L\ge0\), and all sufficiently large real \(X\). No uniformity in a growing \(k\) is asserted.

## Proof

**1. Two-state evaluation of the partition number.** Chow and Slattery's Zeckendorf-gap formula (Theorem 1.1 of *On Fibonacci Partitions*) yields the following recurrence, which can also be obtained by substituting \(q=a_\ell-\varepsilon_\ell a_{\ell-1}\) into their recurrence. Begin with \((A,q)=(1,1)\). For each gap \(d=i_{t-1}-i_t\ge2\) between consecutive selected Zeckendorf indices, write \(d=2h\) or \(d=2h+1\), with \(h\ge1\). Replace the state as follows:
\[
\begin{array}{c|cc}
\text{gap}&A'&q'\\\hline
2h&hA+q&(h-1)A+q\\
2h+1&hA+q&hA+q
\end{array}.
\]
After processing all gaps, if the last index is \(j=i_s\), then
\[
R(n)=q+\left(\left\lfloor\frac{j+1}{2}\right\rfloor-1\right)A.
\]
The formula includes single-summand expansions (no updates), for which \(R(f_j)=\lfloor(j+1)/2\rfloor\). In all reachable states \(1\le q\le A\), and each update strictly increases \(A\).

**2. Finite polynomial recursion.** Fix \(k\). For a state \((A,q)\), define \(F_{A,q}(z)\) as the ordinary generating function, with exponent the total remaining Zeckendorf index length, of all choices of later indices and the final index that lead to final value exactly \(k\). If \(q>k\), this is zero. If \(A>k\), a final value \(k\) can occur only when \(q=k\), the final index is \(1\) or \(2\), and all subsequent gaps are exactly \(2\). Thus
\[
F_{A,q}(z)=\begin{cases}z/(1-z),&A>k,\ q=k,\\0,&A>k,\ q<k.\end{cases}
\]
All states with \(A>k\) may therefore be replaced by a single capped value \(A=k+1\) while retaining \(q\).

For \(1\le q\le A\le k\), write \(D=k-q\) and define
\[
E_{A,q}(z)=\begin{cases}z^{2t+1}(1+z),&D=tA\text{ for an integer }t\ge0,\\0,&\text{otherwise.}\end{cases}
\]
This enumerates stopping immediately, because the final index can be \(2t+1\) or \(2t+2\). The exact remaining-index recursion is
\[
\begin{split}
F_{A,q}(z)={}&E_{A,q}(z)
+\sum_{h=1}^{\lfloor D/A\rfloor+1}z^{2h}F_{\min(hA+q,k+1),(h-1)A+q}(z)\\
&+\sum_{h=1}^{\lfloor D/A\rfloor}z^{2h+1}F_{hA+q,hA+q}(z).
\end{split}
\]
These are finite sums: the first bound is precisely \((h-1)A+q\le k\), and the second precisely \(hA+q\le k\). Every noncapped successor has larger first coordinate, so this is a terminating exact algorithm.

Set \(G_{A,q}(z)=(1-z)F_{A,q}(z)\). For capped states \(G_{k+1,k}(z)=z\) and \(G_{k+1,q}(z)=0\) for \(q<k\). Multiplying the preceding recursion by \(1-z\) gives the explicit polynomial algorithm
\[
\begin{split}
G_{A,q}(z)={}&(1-z)E_{A,q}(z)
+\sum_{h=1}^{\lfloor D/A\rfloor+1}z^{2h}G_{\min(hA+q,k+1),(h-1)A+q}(z)\\
&+\sum_{h=1}^{\lfloor D/A\rfloor}z^{2h+1}G_{hA+q,hA+q}(z).
\end{split}
\]
The integer polynomial in the finding is \(P_k(z)=G_{1,1}(z)\). A noncapped transition increases \(A\) by at least one, so there are at most \(k\) transitions before stopping or capping. Every admissible gap from a noncapped state is at most \(2k\); every stopping index is at most \(2k\). In fact, the slightly loose universal bound \(\deg P_k\le 2k^2+2k+2\) follows immediately. This bounds the exact stabilization threshold without claiming it is sharp.

**3. From greatest indices to cutoffs.** Each positive integer corresponds bijectively to a nonempty Zeckendorf word. The exponent of \(z\) in \(F_{1,1}(z)\) records its greatest selected index. Hence the generating function of positive integers of multiplicity exactly \(k\), by greatest index, is \(P_k(z)/(1-z)\). Summing over all greatest indices at most \(L\), and adding \(n=0\) when \(k=1\), gives the boxed rational generating function for \(C_k(L)\). Coefficient extraction yields its eventual affine formula with no periodic term.

**4. Strictly positive logarithmic coefficient.** For any fixed \(k\), a Zeckendorf word starting with a gap of length \(2k\) moves from \((1,1)\) to \((k+1,k)\). Thereafter arbitrary repetitions of the gap \(2\), followed by final index \(1\) or \(2\), preserve final value \(k\). This contributes \(z^{2k+1}/(1-z)\) to the nonnegative coefficient series \(F_{1,1}(z)\). The eventual constant number of words at each greatest index is therefore positive, which implies \(P_k(1)>0\). Finally, \(f_{L+1}=\Theta(\varphi^L)\) and \(C_k(L+1)-C_k(L)=O_k(1)\); bracketing arbitrary \(X\) between successive Fibonacci cutoffs gives the logarithmic law with an \(O_k(1)\) error.

**5. Explicit twelve-representation specialization.** Substituting \(k=12\) into the finite polynomial recursion gives the seven-term polynomial above; the sum of its coefficients is \(44\), and the sum of degree-weighted coefficients is \(594\). Therefore for every \(L\ge24\), coefficient extraction gives \(44(L+1)-594=44L-550\). In particular \(C_{12}(24)=506\) and \(C_{12}(25)=550\).

## Verification

The included standard-library-only program `verify.py` evaluates the state recursion exactly using integer polynomial dictionaries, and separately constructs \(R(n)\) through an ordinary descending-index 0–1 knapsack dynamic program. It compares every integer \(0\le n<f_{25}=121393\) with the gap-state formula and every cutoff \(0\le L\le24\) for \(1\le k\le25\) against the independent knapsack counts. It checks the seven displayed coefficients for \(P_{12}\) and the asserted affine formula over \(24\le L<120\). This is finite reproducible corroboration; the infinite statements follow from the proofs above, not from sample checks.

Run `python3 verify.py` alongside this file. No external packages or downloads are required.

## Relationship to prior work

Chow and Slattery, *On Fibonacci Partitions* (2021), Theorem 1.1, supply the exact pointwise Zeckendorf-gap formula. The present contribution is an all-level fixed-fiber enumeration and a constructive family of rational generating functions; the pointwise formula does not itself state their degree, eventual affine behavior, logarithmic fiber law, or example for twelve representations.

Sanna, *A Note on the Power Sums of the Number of Fibonacci Partitions* (first posted 22 September 2023), proves asymptotics for \(\sum_{n<N}R(n)^p\), not the cardinality of individual fibers \(\{n:R(n)=k\}\). Kempton, *The Dynamics of the Fibonacci Partition Function* (2023), studies its rotation cocycle, local ratio patches, and global summatory distribution; its full-text theorems do not provide this fixed-fiber rational series. These are different statements; one cannot infer the fiber law merely from the moments or ratios. The classical automata of Berstel and related Fibonacci numeration work could provide alternative routes, and unindexed prior fixed-value enumerations remain possible.

## Limitations

The theorem fixes \(k\) before taking \(L\) or \(X\) large; there is no joint asymptotic for growing \(k\). The polynomial recursion is finite but may grow rapidly with \(k\), and the degree upper bound is not optimized. Scientific priority is assessed only against the cited and accessible evidence; this is not an independence or publication-priority certification. The listed program does not establish any infinite theorem independently of the written argument.

## References

1. S. Chow and T. Slattery, *On Fibonacci Partitions*, Journal of Number Theory 225 (2021), 310–326; freely accessible accepted manuscript: https://wrap.warwick.ac.uk/id/eprint/150069/1/WRAP-on-Fibonacci-partitions-Chow-2021.pdf (Theorem 1.1, Section 2).
2. C. Sanna, *A Note on the Power Sums of the Number of Fibonacci Partitions*, arXiv:2309.12724v1 (22 September 2023), later Discrete Analysis 2025:2; https://arxiv.org/abs/2309.12724 (Theorems 1.1–1.2, automata preliminaries).
3. T. Kempton, *The Dynamics of the Fibonacci Partition Function*, arXiv:2311.06006v1 (10 November 2023); https://arxiv.org/html/2311.06006v1 (Theorems 1.1–1.2, Proposition 2.2, Section 4).
4. N. H. Zhou, *On the Representation Functions of Certain Numeration Systems*, arXiv:2305.00792v1 (1 May 2023); https://arxiv.org/abs/2305.00792 (representation bounds, moments, Dirichlet series).
