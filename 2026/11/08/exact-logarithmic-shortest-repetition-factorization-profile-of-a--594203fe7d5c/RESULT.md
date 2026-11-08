# Exact logarithmic shortest-repetition-factorization profile of a binary automatic word

## Finding

Define the binary infinite word \(w=w(0)w(1)\cdots\) by
\[
w(n)=\lfloor\log_2(n+1)\rfloor\bmod 2,\qquad n\ge0.
\]
For a finite nonempty word \(u\), a *repetition* is a word admitting a period \(p\ge1\) with \(2p\le |u|\); a repetition factorization is a concatenation of such words. For a factor \(u\), let \(\operatorname{sw}(u)\) be its least number of repetition factors, and set it to zero if no such factorization exists. For \(L\ge2\), let
\[
M(L)=\max\{\operatorname{sw}(w[i:i+L]):i\ge0,\ \operatorname{sw}(w[i:i+L])>0\}.
\]
Then \(w\) is \(2\)-automatic and
\[
\boxed{M(L)=\lfloor\log_2 L\rfloor\quad\text{for every integer }L\ge2.}
\]
In fact, every repetition occurring in \(w\) is monochromatic. If a factor intersects \(r\) maximal constant runs of \(w\), with intersection lengths \(\ell_1,\ldots,\ell_r\), its shortest repetition-factorization width is exactly \(r\) when all \(\ell_j\ge2\), and it is unfactorizable when any \(\ell_j=1\). Consequently shortest widths of factorizable factors are unbounded, even for a binary automatic sequence.

## Assumptions and scope

Indices start at zero; \(w[i:i+L]\) is the finite consecutive factor at indices \(i,\ldots,i+L-1\). A period \(p\) of a length-\(L\) word means equality of entries at offsets \(j\) and \(j+p\) for all \(0\le j<L-p\). The width is the *shortest* number of pieces (not the maximum possible number), and unfactorizable factors do not participate in \(M(L)\). The infinite word is the alternating-run word
\[
w=0^{1}1^{2}0^{4}1^{8}0^{16}1^{32}\cdots,
\]
whose run number \(j\ge0\) has length \(2^j\) and letter \(j\bmod2\). No claim about general automatic words or decidability of the unrestricted width-boundedness problem is made.

## Proof

**1. Automaticity.** For \(n\ge1\), let \(\ell\) be the length of its canonical base-two representation. Unless the representation is \(1^\ell\), adding one preserves the binary length, so \(\lfloor\log_2(n+1)\rfloor=\ell-1\). If the representation is \(1^\ell\), adding one yields a power of two and the floor is \(\ell\). Thus a finite-state output machine need only track the parity of \(\ell\) and whether all digits so far have been one; the input zero has output zero. This is a deterministic finite automaton with output for \(w\), so \(w\) is \(2\)-automatic.

**2. No nonmonochromatic squares.** More generally, consider a binary word with strictly increasing positive lengths of consecutive maximal constant runs. Suppose it contains \(uu\) for some nonconstant \(u\). Write its maximal-run decomposition as \(u=c_1^{a_1}\cdots c_s^{a_s}\), where \(s\ge2\) and adjacent letters alternate. If \(s\ge3\), the internal run of length \(a_2\) is complete in each of the two copies and therefore produces two distinct complete ambient runs of equal length, contrary to strict increase. If \(s=2\), write \(u=c^a d^b\) with \(c\ne d\). The factor \(uu=c^a d^b c^a d^b\) has its first ambient run of length at least \(a\), followed by complete ambient runs of lengths \(b\) and \(a\). Strict increase would require \(a\le\text{first ambient length}<b<a\), a contradiction. Hence every square in \(w\) is monochromatic. If a word of length at least \(2p\) has period \(p\), its first \(2p\) letters form a square; a constant first period forces the whole periodic word to be constant. Thus every repetition factor of \(w\) is monochromatic.

**3. Exact factor widths.** A monochromatic repetition has length at least two and cannot cross a run boundary. Hence a factor meeting \(r\) runs needs at least \(r\) repetition factors and is impossible to factor if any run-intersection length is one. Conversely, if all intersections have length at least two, each constant intersection itself has period one, yielding a factorization of width exactly \(r\).

**4. Upper bound.** Consider a factorizable length-\(L\) factor meeting \(r\ge2\) runs, beginning in run \(j\). The first and last intersections have length at least two, so \(j\ge1\). All \(r-2\) intervening runs appear in full. Therefore
\[
L\ge 2+\sum_{h=j+1}^{j+r-2}2^h+2
\ge4+\sum_{h=2}^{r-1}2^h=2^r.
\]
For \(r=2\), the sum is empty and the last identity still holds. For \(r=1\), factorability requires \(L\ge2\). Thus \(r\le\lfloor\log_2 L\rfloor\) in every case.

**5. Matching constructions at every length.** Let \(k=\lfloor\log_2 L\rfloor\). When \(k=1\), a constant factor of length \(L\in\{2,3\}\) inside run number \(2\) has width one. Suppose \(k\ge2\). For
\[
2^k\le L\le2^{k+1}-2,
\]
take the entirety of runs numbered \(1,2,\ldots,k-1\) followed by the first \(b=L-(2^k-2)\) symbols of run number \(k\). The first \(k-1\) runs have total length \(2^k-2\), and \(2\le b\le2^k\). This factor has \(k\) intersections, all of length at least two, so its width is \(k\). For the sole remaining length \(L=2^{k+1}-1\), take the last two letters of run number \(2\), all runs numbered \(3,\ldots,k\), and the first five letters of run number \(k+1\). The middle length is \(2^{k+1}-8\) (zero when \(k=2\)); the total is \(2+(2^{k+1}-8)+5=2^{k+1}-1\), and there are again exactly \(k\) run intersections of length at least two. This establishes both the lower bound and the asserted formula for every \(L\ge2\). \(\square\)

## Verification

The standalone \(verify.py\) reconstructs the word directly from its digit-length definition, tests 25,600 candidate squares in a finite prefix, independently computes shortest widths using exhaustive dynamic programming on 4,440 short factors, and constructs matching factors at all lengths from 2 through 1024. Running `python3 verify.py` produced `VERIFY_OK checks= 31063 max_length= 1024 dp_factors= 4440`. These finite tests are not an infinite proof; steps 1–5 above establish the all-length result.

## Relationship to prior work

Shallit and Xu, *Repetition factorization of automatic sequences*, arXiv:2311.14961 (first publicly submitted 2023-11-25), define the same shortest-width statistic. Their Theorem 1 supplies bounded-width automata for a fixed threshold, and their later sections prove finite bounds for Fibonacci, Thue–Morse and paperfolding factors while giving unbounded *longest* widths for the Rudin–Shapiro sequence. None of those assertions implies an unbounded *shortest* width for the digit-length word or the exact logarithmic maximum over all length-\(L\) factors. Inoue et al., *Factorizing Strings into Repetitions*, Theory Comput. Syst. 66 (2022), supply finite-string algorithms; those algorithms are compatible with, but do not by themselves state, an infinite all-length width formula. The latter source was accessible only at abstract level in this review, so unseen coverage remains a bibliographic risk.

## Limitations

The result concerns the particular non-uniformly recurrent binary automatic word \(w\); it does not settle whether boundedness of shortest repetition-factorization widths is decidable for arbitrary automatic sequences. The claim does not apply to longest factorizations. Novelty is assessed against the material inspected and the available mathematical-record search, not certified as globally unique. A separate independent audit has not been performed.

## References

1. J. Shallit and X. Xu, *Repetition factorization of automatic sequences*, arXiv:2311.14961v1 (2023-11-25), revised v2 (2023-11-29). https://arxiv.org/html/2311.14961v2
2. N. Rampersad, J. Shallit, and X. Xu, *Repetition Factorization of Automatic Sequences*, International Journal of Foundations of Computer Science (2024), DOI:10.1142/S0129054124430019. https://doi.org/10.1142/S0129054124430019
3. H. Inoue, Y. Matsuoka, Y. Nakashima, S. Inenaga, H. Bannai, and M. Takeda, *Factorizing Strings into Repetitions*, Theory of Computing Systems 66 (2022), 484–501, DOI:10.1007/s00224-022-10070-3. https://doi.org/10.1007/s00224-022-10070-3
