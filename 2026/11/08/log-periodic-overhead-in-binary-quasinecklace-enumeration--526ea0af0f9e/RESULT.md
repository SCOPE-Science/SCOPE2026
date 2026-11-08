# Log-periodic overhead in binary quasinecklace enumeration

## Finding

Let \(Q_2(n)\) be the number of length-\(n\) binary quasinecklaces in the sense of Gabrić and Sawada, and let \(N_2(n)\) be the number of ordinary binary necklaces (canonical representatives of cyclic rotations). For every integer \(n\geq1\), the exact quasinecklace count is

\[
Q_2(n)=2+\sum_{\ell=1}^{n-1}[z^{n-\ell-1}]\frac{1}{1-z-z^2-\cdots-z^{\ell+1}}.
\]

More significantly, with \(\theta_n=\{\log_2 n\}\),

\[
\boxed{\frac{Q_2(n)}{N_2(n)}=\Psi(\theta_n)+o(1),\qquad
\Psi(\theta)=\sum_{j\in\mathbb Z}2^{\theta-j-2}\exp(-2^{\theta-j-2}).}
\]

The function \(\Psi\) is positive, real analytic, nonconstant, and one-periodic. Its Fourier coefficients, in the convention \(\Psi(\theta)=\sum_{h\in\mathbb Z}c_h e^{2\pi i h\theta}\), are

\[
c_h=\frac{\Gamma(1-2\pi i h/\log 2)}{\log 2}.
\]

Consequently the overhead ratio has **no ordinary limit** as \(n\to\infty\). Its logarithmic-phase average is exactly \(1/\log 2=1.44269504088896\ldots\), while its first nonconstant Fourier coefficient has modulus approximately \(7.13011725975\times10^{-6}\). For any \(\theta\in[0,1)\), taking integers \(n_m=\lfloor2^{m+\theta}\rfloor\) gives \(Q_2(n_m)/N_2(n_m)\to\Psi(\theta)\). The asymptotic describes the number of quasinecklace candidates per necklace, not the exact implementation's instruction count.

## Assumptions and scope

The binary alphabet is \(\{0,1\}\) with \(0<1\). A quasinecklace \(w\) has the longest run of its minimum symbol at the beginning; any other equally long minimum-symbol run must be followed by a symbol no smaller than the one after the initial run; and a word ending in its minimum symbol must be constant. These are Definition 3(a)--(c) of Gabrić and Sawada. Ordinary necklaces use the lexicographically least rotation of each cyclic binary word. The statement concerns every positive integer \(n\) for the exact formula and the limit along every sequence \(n\to\infty\) for the asymptotic.

Write \([z^t]F(z)\) for a formal power-series coefficient. All logarithms without subscript are natural, and \(\{x\}=x-\lfloor x\rfloor\).

## Proof

**1. Binary characterization and exact count.** Every nonconstant binary quasinecklace starts with \(0^\ell1\), where \(\ell\ge1\) is its maximal zero-run length, and ends in \(1\). The comparison after another longest zero-run is automatic over a binary alphabet, since the only symbol following a maximal zero-run is \(1\). The remaining suffix has length \(t=n-\ell-1\), ends in \(1\) when nonempty, and has no zero-run longer than \(\ell\). Splitting it after every \(1\) gives a unique composition of \(t\) into parts \(1,\ldots,\ell+1\): a part of length \(s\) encodes \(0^{s-1}1\). Conversely every such composition yields an admissible quasinecklace. If the suffix is empty there is one possibility. Adding the two constant words establishes the displayed exact coefficient identity.

**2. Normalized summands.** Put \(a_r(t)=[z^t](1-z-\cdots-z^r)^{-1}\). For \(t\ge1\), \(a_r(t)=2^{t-1}p_r(t)\), where \(p_r(t)\) is the probability that a uniformly random length-\(t\) binary word conditioned to end in \(1\) contains no run of \(r\) zeros. Thus for \(\ell=n-t-1\) and \(r=\ell+1\), the contribution of this nonconstant class to \(nQ_2(n)/2^n\) is

\[
x_{n,\ell}p_{\ell+1}(n-\ell-1),\qquad x_{n,\ell}=n/2^{\ell+2}.
\]

The empty-suffix term and the two constant words contribute \(O(n2^{-n})\).

**3. Rare-run limit.** Let \(m=\lfloor\log_2 n\rfloor\), and fix an integer \(j\). Put \(\ell=m+j\), \(r=\ell+1\), and \(t=n-\ell-1\). Precede the random suffix by a fixed \(1\). Except for the event of an initial \(r\)-zero run, which has probability \(2^{-r}\), an \(r\)-zero run is detected by an occurrence of the pattern \(10^r\) starting at one of \(M=t-r-1\) internal positions. These internal pattern events each have probability \(p=2^{-(r+1)}\). Two starts at separation at most \(r\) are mutually exclusive, and starts at separation at least \(r+1\) use disjoint independent bits. Therefore the \(h\)-th inclusion-exclusion sum for the number of pattern occurrences is exactly

\[
S_h=\binom{M-r(h-1)}{h}p^h
\]

(with binomial coefficients interpreted as zero if their upper index is too small). Along any subsequence with \(\theta_n\to\theta\), for each fixed \(h\ge0\), \(S_h\to x^h/h!\), where \(x=2^{\theta-j-2}\). The even and odd Bonferroni bounds, followed by their order tending to infinity, give \(p_r(t)\to e^{-x}\). The boundary event has vanishing probability. Hence the fixed-\(j\) contribution tends to \(xe^{-x}\).

**4. Uniform tail control.** For any \(r\ge2\), consider \(B=2^{r+2}\) independent fair bits. The number \(Y\) of occurrences of \(10^r\) wholly inside this block has mean \(\mu=(B-r)2^{-(r+1)}>1\). Overlapping occurrences are incompatible, while nonoverlapping occurrences are independent; hence \(\mathbb E[Y^2]\le\mu+\mu^2\). The second-moment inequality gives \(\Pr(Y>0)\ge\mu/(1+\mu)>1/2\). Applying this to disjoint \(B\)-blocks in the \(t-1\) unrestricted bits of a word whose last bit is \(1\) yields

\[
p_r(t)\le2^{-\lfloor(t-1)/2^{r+2}\rfloor}.
\]

For \(\ell\le m-K\), we have \(t\ge n/2\) for all sufficiently large \(n\), and this bounds the normalized term by \(2x_{n,\ell}e^{-c x_{n,\ell}}\) with an absolute constant \(c>0\). Summing these terms gives a bound tending to zero as \(K\to\infty\), uniformly in large \(n\). For \(\ell\ge m+K\), the trivial bound \(p_r(t)\le1\) makes the sum at most \(2^{-K}\). These bounds also control the two tails of the proposed bi-infinite sum. Fixed-\(j\) convergence in the central window, followed by \(K\to\infty\), proves

\[
\frac{nQ_2(n)}{2^n}=\Psi(\{\log_2 n\})+o(1).
\]

**5. Necklaces and Fourier analysis.** Burnside's lemma gives

\[
N_2(n)=\frac1n\sum_{d\mid n}\varphi(d)2^{n/d}=\frac{2^n}{n}(1+o(1)),
\]

so division proves the asserted candidate-to-necklace ratio. The series for \(\Psi\) and all its derivatives converge uniformly on compact phase intervals. Periodizing \(g(u)=2^{u-2}e^{-2^{u-2}}\) and substituting \(y=2^{u-2}\) in its Fourier integral gives

\[
c_h=\int_{\mathbb R}g(u)e^{-2\pi ihu}\,du
=\frac1{\log2}\int_0^\infty e^{-y}y^{-2\pi ih/\log2}\,dy
=\frac{\Gamma(1-2\pi ih/\log2)}{\log2}.
\]

In particular \(c_0=1/\log2\), whereas \(c_1\ne0\), since \(|\Gamma(1+it)|^2=\pi t/\sinh(\pi t)>0\) for nonzero real \(t\). Thus \(\Psi\) is not constant. The fractional parts of \(\log_2 n\) approach any prescribed phase along the stated subsequences, which proves the absence of an ordinary limit.

## Verification

The included `verify.py` checks the binary definition directly by exhaustively enumerating all words of lengths \(1\) through \(16\), and independently compares the counts with both composition recurrences and a zero-run-state automaton. It evaluates the exact count and the phase function for lengths \(32,64,128,256,512,1024\), and prints `BINARY_QUASINECKLACE_ASYMPTOTIC_VERIFY_OK`. Further direct exact counts at lengths \(2048\) and \(4096\) were inspected. These tests confirm small cases and numerical consistency only; the proof of the asymptotic is the rare-run inclusion-exclusion and tail argument above.

To reproduce with Python 3 and no external packages, run `python3 verify.py` in the directory containing the script.

## Relationship to prior work

Gabrić and Sawada (2026) introduce quasinecklaces, prove the constant-factor bound \(Q_k(n)=O(N_k(n))\), and give a finite recurrence for their counts in Section 3.1. The exact coefficient formula above is a binary reformulation of that finite enumeration; **it is not presented as a new exact counting formula**. The present contribution is the explicit, nonconstant logarithmic-phase asymptotic and Fourier spectrum of the candidate-to-output overhead. Existing fixed-content exact identities likewise determine all finite counts if summed over contents but do not supply the uniform dense-content limit or its oscillations. Sawada, Williams and Wong (2017) work with a different auxiliary family, pseudonecklaces, and establish generation guarantees rather than this quasinecklace asymptotic. Classical longest-run distributions provide relevant probability background but do not directly state the quasinecklace overhead law. No claim of absolute historical priority is made.

## Limitations

The theorem is for the full binary quasinecklace family without a weight restriction, not for arbitrary alphabets, the older pseudonecklace family, or a particular implementation's exact instruction count. The error is proved to be \(o(1)\) but no sharp convergence rate is claimed. The Fourier amplitude is tiny, so finite counts at feasible lengths do not independently resolve nonconstancy. The result has not undergone independent mathematical audit. An unindexed earlier transfer of longest-run extreme-value laws to quasinecklace enumeration remains a priority risk.

## References

1. Daniel Gabrić and Joe Sawada, *Necklaces and Lyndon words in colexicographic order*, arXiv:2607.05324, first posted 2026-07-06. https://arxiv.org/abs/2607.05324 . Definition 3, Theorems 4 and 9, and Section 6.
2. Joe Sawada, Aaron Williams, and Dennis Wong, *Necklaces and Lyndon words in colexicographic and binary reflected Gray code order*, Journal of Discrete Algorithms 46–47 (2017), DOI:10.1016/j.jda.2017.10.002. https://doi.org/10.1016/j.jda.2017.10.002 . Sections 3.1–3.2.
3. Raphael Rom, *Distribution of Runs in Binary Words*, IEEE Transactions on Computers C-27 (1978), 1087–1089, DOI:10.1109/TC.1978.1675003. https://doi.org/10.1109/TC.1978.1675003 . Background on the longest-run counting problem; only abstract-level content was accessible for this comparison.
