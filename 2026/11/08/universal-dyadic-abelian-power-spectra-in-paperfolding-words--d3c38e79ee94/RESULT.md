# Universal dyadic Abelian-power spectra in paperfolding words

## Finding

Let an arbitrary infinite instruction sequence \(\mathbf b=(b_0,b_1,\ldots)\in\{-1,1\}^{\mathbb N_0}\) define the one-indexed binary paperfolding word
\[
f_{\mathbf b}(n)=(-1)^{(u-1)/2}b_v\qquad(n=2^v u,\ u\text{ odd},\ n\ge1).
\]
For a starting position \(i\ge1\) and a length \(L\ge1\), set \(S_{\mathbf b}(i,L)=\sum_{j=0}^{L-1}f_{\mathbf b}(i+j)\). For \(r\ge2\), an Abelian \(r\)-power of period \(L\) starts at \(i\) precisely when the sums \(S_{\mathbf b}(i+hL,L)\), for \(0\le h<r\), are all equal; for a binary alphabet this is equivalent to the equality of all \(r\) Parikh vectors.

**Theorem.** For every instruction sequence, every integer \(k\ge1\), and \(L=2^k\):

1. The sum \(S_{\mathbf b}(i,L)\) is always one of \(-2,0,2\). The natural densities of starting positions attaining these sums are respectively \(1/4,1/2,1/4\). Equivalently, the number of \(+1\) symbols in a length-\(L\) factor takes exactly \(L/2-1,L/2,L/2+1\), with those same densities.
2. An Abelian \(r\)-power with \(r\ge2\) starts at \(i\) if and only if all its constituent length-\(L\) blocks have sum zero.
3. The starting positions of Abelian squares have natural density \(1/4\), and those of Abelian cubes have natural density \(1/16\). There are **no** Abelian fourth or higher powers of period \(2^k\), at any starting position.

The boundary period \(L=1\) also has no Abelian fourth powers; its square and cube starting-position densities are instead \(1/2\) and \(1/8\), respectively. All densities are independent of the instruction sequence. The cube bound is attained at every dyadic period because its occurrence density is positive.

## Assumptions and scope

Indices of the paperfolding word start at \(1\), whereas instruction indices start at \(0\). A natural density of \(A\subseteq\mathbb N\) means the limit \(\lim_{N\to\infty}|A\cap\{1,\ldots,N\}|/N\); its existence is part of the conclusion, with no assumption of periodicity or convergence of the instructions. A period is the common length of adjacent blocks, not necessarily the least ordinary period of the whole factor. A dyadic period means \(2^k\) with \(k\ge0\). The theorem concerns Abelian powers only at such lengths; no restriction on Abelian powers at other periods is asserted.

Write \(T\mathbf b=(b_1,b_2,\ldots)\). The defining formula immediately gives
\[
f_{\mathbf b}(2a)=f_{T\mathbf b}(a)\ (a\ge1),\qquad
f_{\mathbf b}(2a+1)=(-1)^a b_0\ (a\ge0).
\]

## Proof

**1. Reduction of dyadic block sums.** Whenever \(N\ge2\) is even, a run of \(2N\) consecutive indices contains \(N\) odd indices. Their signs alternate and sum to zero. The even-indexed letters give exactly the length-\(N\) factor of \(f_{T\mathbf b}\) beginning at \(\lceil i/2\rceil\). Hence
\[
S_{\mathbf b}(i,2N)=S_{T\mathbf b}(\lceil i/2\rceil,N)
\quad(N\ge2\text{ even}).
\]
Repeatedly applying this identity to \(2^k\), stopping at block length two, gives, for all \(k\ge1\),
\[
S_{\mathbf b}(i,2^k)
=S_{T^{k-1}\mathbf b}\bigl(\lceil i/2^{k-1}\rceil,2\bigr).
\tag{1}
\]
For \(k=1\) this is simply the identity. A run of consecutive \(i\)'s is mapped to consecutive \(j=\lceil i/2^{k-1}\rceil\)'s, each repeated exactly \(2^{k-1}\) times away from the initial boundary; thus the map preserves all existing natural densities. Crucially,
\[
\left\lceil\frac{i+h2^k}{2^{k-1}}\right\rceil
=\left\lceil\frac{i}{2^{k-1}}\right\rceil+2h.
\tag{2}
\]

**2. A two-letter sign obstruction.** Fix a tail \(\mathbf c=T^{k-1}\mathbf b\), put \(q=c_0\), \(\mathbf g=f_{T\mathbf c}\), and define \(F(j)=S_{\mathbf c}(j,2)\). For every admissible \(a\),
\[
F(2a)=g(a)+(-1)^a q\ (a\ge1),\qquad
F(2a+1)=(-1)^a q+g(a+1)\ (a\ge0).
\tag{3}
\]
Each value lies in \(\{-2,0,2\}\). For either parity of \(j\), when \(j\) is increased by \(2\), the sign of any *nonzero* \(F(j)\) changes: a nonzero value must equal twice its alternating \(q\)-term. Therefore two consecutive values along \(j,j+2,j+4,\ldots\) can be equal only if both are zero. By (1)–(2), an Abelian \(r\)-power with \(r\ge2\) at dyadic period is equivalent to vanishing of each constituent sum. This establishes the first two assertions, except their densities.

**3. One Boolean sequence controls all occurrences.** Define, for \(a\ge1\),
\[
E(a)=\mathbf1_{\{g(a)=-(-1)^a q\}}.
\]
By (3),
\[
F(2a)=0\iff E(a)=1,\qquad
F(2a+1)=0\iff E(a+1)=0.
\tag{4}
\]
Thus an Abelian \(r\)-power beginning at an even position \(j=2a\) in the reduced word means \(r\) consecutive ones in \(E\) starting at \(a\); beginning at odd \(j=2a+1\) means \(r\) consecutive zeros in \(E\) starting at \(a+1\).

Let \(t=c_1\) and \(d=f_{T^2\mathbf c}\). The paperfolding recursion yields
\[
E(2u)=\mathbf1_{\{d(u)=-q\}}\ (u\ge1),\qquad
E(2u+1)=\mathbf1_{\{(-1)^u t=q\}}\ (u\ge0).
\tag{5}
\]
In particular the values at successive *odd indices* of \(E\) alternate strictly between zero and one. Every four consecutive values of \(E\) include two odd-indexed values of opposite signs. Thus no run of four equal values of \(E\) is possible. Equation (4) proves the fourth-power exclusion and consequently excludes every larger exponent.

**4. Density lemma for arbitrary instructions.** For every instruction sequence \(\mathbf a\), both signs of \(f_{\mathbf a}(n)\) have conditional natural density \(1/2\) when \(n\) is restricted to either parity. On odd indices \(n=2v+1\), the signs \((-1)^v a_0\) alternate. On even indices, \(f_{\mathbf a}(2v)=f_{T\mathbf a}(v)\); the latter has unconditional sign densities \(1/2\). Indeed, among integers of any fixed two-adic valuation \(h\), the odd cofactors \(u\equiv1\pmod4\) and \(u\equiv3\pmod4\) occur equally often, so each contributes half of the density \(2^{-h-1}\). The total density of integers having valuation at least \(H\) is \(2^{-H}\), uniformly in the instruction signs. Truncating valuations at \(H\), taking the integer limit, and then letting \(H\to\infty\) proves the unconditional assertion and hence the conditional even-index assertion.

A second fact is that for every fixed \(\delta\in\{\pm1\}\), the event
\[
f_{\mathbf a}(u)=f_{\mathbf a}(u+1)=\delta
\tag{6}
\]
has density \(1/4\) *conditional on either parity of \(u\)*. For \(u=2v\), the two terms are \(f_{T\mathbf a}(v)\) and \((-1)^v a_0\); the second equality imposes one parity of \(v\), and on that parity the first equality occurs with conditional frequency \(1/2\). For \(u=2v+1\), use \((-1)^v a_0\) and \(f_{T\mathbf a}(v+1)\) identically. This proves (6), including existence of the densities.

**5. Exact frequencies of the runs in \(E\).** Equation (5) and the sign-density lemma give \(\Pr(E(a)=1)=1/2\). For the event \(E(a)=E(a+1)=1\), treat separately \(a=2u\) and \(a=2u+1\). In either case the odd-indexed \(E\)-value selects one parity of \(u\), and the even-indexed \(E\)-value selects one sign of \(d(u)\) or \(d(u+1)\). Conditional sign balance makes each starting parity contribute density \(1/8\) among all \(a\). Consequently,
\[
\Pr(E(a)=E(a+1)=1)=1/4.
\]
The identical argument for zeros (or the two-term identity and the density \(1/2\)) yields
\[
\Pr(E(a)=E(a+1)=0)=1/4.
\tag{7}
\]
A run of three ones must start at an even \(a=2u\), since a run starting at odd \(a\) would contain two opposing odd-indexed values. Equation (5) then requires simultaneously
\[
(-1)^u t=q,\qquad d(u)=d(u+1)=-q.
\]
The first condition selects one parity of \(u\); conditional on that parity, the pair-sign lemma (6) gives probability \(1/4\). Even starting \(a\)'s constitute half of all starting positions, so the density of runs of three ones is \((1/2)(1/2)(1/4)=1/16\). Similarly runs of three zeros require the opposite parity and \(d(u)=d(u+1)=q\), and also have density \(1/16\):
\[
\Pr(E(a)=E(a+1)=E(a+2)=1)
=\Pr(E(a)=E(a+1)=E(a+2)=0)=1/16.
\tag{8}
\]
By (4), the even and odd reduced starting positions together give dyadic Abelian-square density \((1/2)(1/4)+(1/2)(1/4)=1/4\) and cube density \((1/2)(1/16)+(1/2)(1/16)=1/16\). Formulae (1)–(2) transfer the values to every \(2^k\).

For the one-block Parikh distribution, the zero-sum density follows from (4) and \(\Pr(E=1)=\Pr(E=0)=1/2\). In (3) each nonzero sum is twice the alternating odd-index contribution, and on each parity class of \(a\) it occurs with conditional density \(1/2\), by the sign-density lemma and (5). The positive and negative sums therefore each occur with density \(1/4\), proving assertion 1.

**6. Length-one boundary.** Two equal adjacent letters occur with density \(1/2\): on both even and odd starting positions one letter has prescribed sign and the other has conditional sign distribution \((1/2,1/2)\). Three equal adjacent letters cannot start at an odd index, because the two odd-indexed letters are opposite. Starting at \(2u\), three equal letters require \(f_{T\mathbf b}(u)=f_{T\mathbf b}(u+1)=(-1)^u b_0\). For each parity of \(u\) the pair-sign lemma gives probability \(1/4\), so the overall starting-position density is \(1/8\). Four equal letters are impossible because every length-four interval contains two successive odd-indexed letters, which are opposite. This completes the proof. \(\square\)

## Verification

Run `python3 verify.py` using Python 3 and its standard library. It checks all \(256\) configurations of the first eight folding instructions on every fully contained length-\(4\cdot2^k\) window with \(0\le k\le5\) in a finite prefix, with exact integer sums and no randomly sampled positions. It also checks six instruction patterns on \(65{,}536\) consecutive starting positions each, for every \(0\le k\le7\): the Parikh spectrum, all square/cube densities with a stated finite tolerance, the absence of fourth powers, and the reduction identity (1) at sampled finite indices. The script prints `VERIFY_OK` only if every assertion holds. These computations are finite tests and **do not replace** the infinite proof in the preceding section.

## Relationship to prior work

Rob Burns, *The appearance function for paper-folding words* (2022), studies factor appearance across general folding instructions. Its object and dependence on arbitrary instructions motivate seeking a uniform local statistic, but its appearance-function characterization does not furnish these Abelian-power densities. Holub, *Abelian powers in paper-folding words* (2012), proves that every paperfolding word admits Abelian powers of arbitrarily large exponent. The present dyadic restriction is therefore mathematically substantive: the unbounded-exponent examples must use non-dyadic periods. Madill and Rampersad, *The abelian complexity of the paperfolding word* (2012), determine the number of distinct Parikh classes of each length for the **ordinary** paperfolding word, including three classes at lengths \(2^k\), but do not give their frequencies or repeated-block occurrence densities for arbitrary folding instructions. Fici, Postic and Silva (2018) establish Abelian **antipowers** in paperfolding words, which require distinct rather than equal Parikh vectors and do not imply this theorem.

The claimed contribution is the full instruction-independent dyadic local spectrum, the exact square/cube densities, and the sharp dyadic exponent cutoff, not the definition or prior existence of arbitrary Abelian powers. Mathematical literature and indexed-result comparisons did not reveal an equivalent complete statement; the possibility of unindexed or implicit earlier coverage remains.

## Limitations

The theorem is proved only for dyadic periods. Holub's general existence theorem shows large Abelian powers at other periods; no statement about their frequencies is made here. Natural density does not imply an exact count in each finite prefix. Tests involving finitely many prefixes cannot rule out a hidden algebraic error in the infinite proof. Although the displayed proof is self-contained and the included program replays its finite consequences, no independent mathematical audit has yet been performed.

## References

- R. Burns, *The appearance function for paper-folding words*, arXiv:2210.14719 (first public version 2022-10-22). https://arxiv.org/abs/2210.14719
- Š. Holub, *Abelian powers in paper-folding words*, arXiv:1207.3585 (first public version 2012-07-16). https://arxiv.org/abs/1207.3585
- B. Madill and N. Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856 (first public version 2012-08-14). https://arxiv.org/abs/1208.2856
- G. Fici, M. Postic and M. Silva, *Abelian Anti-Powers in Infinite Words*, arXiv:1810.12275 (first public version 2018-10-29). https://arxiv.org/abs/1810.12275
