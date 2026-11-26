# A truncated-exponential cycle-count transition for near-deterministic standardized permutations

## Finding

**The first-defect theorem.** Let \(n\ge1\), let \(G_1,\ldots,G_n\) be independent identically distributed letters in a totally ordered discrete alphabet with least letter \(0\), and suppose \(\mathbb P(G_i=0)=1-\varepsilon_n\), where \(0\le\varepsilon_n<1\). Conditional on \(G_i\ne0\), the other letter probabilities may be arbitrary and may depend on \(n\). Form the stable-rank permutation \(\sigma_n\): \(\sigma_n(i)\) is the position of \(G_i\) in the increasing sort of \((G_1,\ldots,G_n)\), with ties resolved in their original order. Let \(K_n\) be its total number of disjoint cycles, \(R_n=\#\{i:G_i\ne0\}\), and let \(J_n\) be the first nonzero position (\(J_n=n+1\) if every letter is zero). Then, for every realized word,

\[
J_n-1\le K_n\le J_n-1+R_n.\tag{1}
\]

For \(0<\varepsilon_n<1\) put \(\alpha_n=-n\log(1-\varepsilon_n)\), and let \(T_\lambda=\min(E_\lambda,1)\), where \(E_\lambda\) has exponential rate \(\lambda>0\); set \(T_0=1\). With \(W_1\) the Wasserstein distance on \([0,1]\), for any \(\lambda\ge0\),

\[
W_1\bigl(\mathcal L(K_n/n),\mathcal L(T_\lambda)\bigr)
\le \varepsilon_n+\frac1n+\frac{|\alpha_n-\lambda|}{2}.\tag{2}
\]

In particular, if \(n\varepsilon_n\to\lambda\in(0,\infty)\), then \(K_n/n\Rightarrow T_\lambda\), whose density on \([0,1)\) is \(\lambda e^{-\lambda t}\) and which has an atom \(e^{-\lambda}\) at \(1\). If \(\varepsilon_n=\lambda/n\), its \(W_1\)-error is \(O_\lambda(n^{-1})\). If \(n\varepsilon_n\to0\), the ratio \(K_n/n\) tends to \(1\) in probability; if \(n\varepsilon_n\to\infty\) with \(\varepsilon_n\to0\), that ratio tends to \(0\) in probability. In the intermediate window \(n\varepsilon_n\to\infty\), \(n\varepsilon_n^2\to0\), the finer scaling is \(\varepsilon_n K_n\Rightarrow\mathrm{Exp}(1)\). This is one first-defect phase theorem with finite-size control and its scaling consequences.

## Assumptions and scope

The alphabet is ordered with an atom \(0\) *strictly below all rare letters*. The other letters need not have bounded support, and no assumptions about their conditional proportions are required. The permutation is obtained by stable sorting, not by uniformly choosing among permutations with the same letter multiplicities. The result applies to the total number of cycles, not to the number of fixed points or the cycle-size vector. The asymptotic limits concern triangular arrays of independent letters, independent within each length \(n\). The critical distribution at \(\lambda=0\) is understood as a point mass at \(1\).

## Proof

**Step 1: a deterministic cycle obstruction.** If \(i<J_n\), the \(i\)th letter is zero and all preceding letters are zero, so \(\sigma_n(i)=i\). Every such \(i\) is a singleton cycle, yielding the lower bound in (1). For a zero letter at \(i\ge J_n\), let \(r(i)\ge1\) be the number of earlier nonzero letters. Stable sorting puts the zero in rank \(i-r(i)<i\), so its image under \(\sigma_n\) is strictly smaller than its index. A cycle contained entirely in zero positions at or after \(J_n\) would consist of strict decreases around a closed loop, impossible. Thus every cycle not among those first \(J_n-1\) singleton cycles contains at least one nonzero position. Different cycles have disjoint positions, so there are at most \(R_n\) such cycles, proving (1).

**Step 2: a quantitative exponential coupling.** The number \(J_n-1\) of initial zeros is a geometric waiting count truncated at \(n\), with \(\mathbb P(J_n-1\ge j)=(1-\varepsilon_n)^j\) for \(0\le j\le n\). If \(V_n\) is exponential with rate \(a_n=-\log(1-\varepsilon_n)\), then \(J_n-1\) has the same law as \(\min(\lfloor V_n\rfloor,n)\). On this coupling its normalized value differs by at most \(1/n\) from \(\min(V_n/n,1)\), which has law \(T_{\alpha_n}\). By (1), the cost of coupling \(K_n/n\) to the initial-zero fraction is at most \(R_n/n\), with mean \(\mathbb E R_n/n=\varepsilon_n\). Hence \(W_1(\mathcal L(K_n/n),\mathcal L(T_{\alpha_n}))\le\varepsilon_n+1/n\).

For positive \(a,b\), \(T_a\) and \(T_b\) are stochastically ordered, and their \(W_1\)-distance equals \(\int_0^1|e^{-at}-e^{-bt}|\,dt\), which is at most \(\tfrac12|a-b|\); the same holds when either rate is zero by continuity. The triangle inequality proves (2).

**Step 3: limiting regimes.** If \(n\varepsilon_n\to\lambda<\infty\), then \(\varepsilon_n\to0\) and \(\alpha_n=n\varepsilon_n+O(n\varepsilon_n^2)\to\lambda\); (2) proves the critical limit, including \(\lambda=0\). When \(\varepsilon_n=\lambda/n\), the bound and Taylor's formula prove the stated \(O_\lambda(n^{-1})\) rate. When \(n\varepsilon_n\to\infty\) but \(\varepsilon_n\to0\), Markov's inequality gives \(R_n/n\to0\) in probability, while \(\mathbb P(J_n/n>t)\le(1-\varepsilon_n)^{\lfloor nt\rfloor}\to0\) for every fixed \(t>0\); apply (1). In the finer intermediate window, the ordinary geometric-to-exponential limit yields \(\varepsilon_n(J_n-1)\Rightarrow\mathrm{Exp}(1)\), whereas \(\mathbb E(\varepsilon_n R_n)=n\varepsilon_n^2\to0\). The squeeze in (1) completes the argument.

## Verification

`check.py` exhaustively verifies (1) for all words of lengths \(1\) through \(8\) over alphabets with two, three and four letters, and independently verifies exact rational mean bounds for binary letters, lengths up to eight, and three distinct rational probabilities. The program reports 97,778 successful checks. These finite checks are corroboration; the all-size proof is the elementary monotonicity argument above. Exact event counts and the exponential coupling require no numerical approximation. To reproduce, run `python check.py` with Python 3.

## Relationship to prior work

Guerder's 2026 paper develops the general stable-standardization model, exact finite-length joint cycle-type formulas, fixed-bias small-cycle laws, and Gaussian total-cycle fluctuations subject to a uniform upper bound on the largest symbol probability. The present near-deterministic triangular array violates that upper bound, and the new limit concerns the cycle total at **linear**, rather than logarithmic, scale. The first-defect pathwise inequality and quantitative truncated-exponential law are not stated in its relevant inspected theorems or proofs. Fulman's 1997 biased-riffle-shuffle work provides the equivalent finite-alphabet sampling model and a full generating function for finite cycle types, but its inspected cycle and fixed-point sections do not derive the rare-packet linear-scale transition. The much earlier Diaconis–McGrath–Pitman paper likewise supplies general finite shuffle cycle-count machinery. The present law uses a deterministic monotonicity mechanism rather than claiming that those generating functions are new. A general exact finite generating function may in principle be used as a starting point for alternative asymptotic derivations; that fact is not claimed as original.

## Limitations

No universality is asserted when the dominant symbol is in the middle of the order, for non-independent letters, or for the complete cycle-length vector. The proof does not resolve the order-one correction \(K_n-(J_n-1)\) in the finite-defect window, and the intermediate-window exponential limit requires \(n\varepsilon_n^2\to0\). The result has undergone only self-review; no independent mathematical assessment has been performed. A prior unindexed analysis of near-degenerate biased riffle shuffles may predate this asymptotic law.

## References

1. A. Guerder, *Cycle structure of random standardized permutations*, arXiv:2603.24127v1, first posted 2026-03-25, https://arxiv.org/abs/2603.24127 . Relevant full-text passages: Theorems 1.1, 1.5 and 1.6; Sections 3, 5.3 and 6.
2. J. Fulman, *The combinatorics of biased riffle shuffles*, arXiv:math/9712240, 1997, https://arxiv.org/abs/math/9712240 . Relevant inspected text: Sections 1 and 3.
3. P. Diaconis, M. McGrath and J. Pitman, *Riffle shuffles, cycles, and descents*, Combinatorica 15 (1995), 11–29, https://doi.org/10.1007/BF01294457 . Publisher abstract and accessible theorem excerpt inspected; complete text not verified.
