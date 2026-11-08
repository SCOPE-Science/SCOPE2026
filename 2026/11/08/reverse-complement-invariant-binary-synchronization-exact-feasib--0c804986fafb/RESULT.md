# Reverse-complement-invariant binary synchronization: exact feasibility and full asymptotic rate

## Finding
Let \(\rho\) reverse a binary word and complement each bit. A *non-overlapping code* is a set of equal-length words in which no nonempty proper prefix of any codeword equals an equally long suffix of any codeword (including itself). For each integer \(n\ge1\), let \(M_n\) be the maximum size of a non-overlapping code \(C\subseteq\{0,1\}^n\) satisfying \(\rho(C)=C\).

**Theorem.** A nonempty such code exists **if and only if** \(n\notin\{3,5,7\}\). Furthermore, for every integer \(n\) satisfying \(n\ge 2\lceil\log_2(4n)\rceil+2\), there is an explicit reverse-complement-invariant non-overlapping binary code satisfying
\[
M_n\ge 2^{n-2\lceil\log_2(4n)\rceil-3}>\frac{2^n}{512n^2}.
\]
Consequently \(\lim_{n\to\infty}n^{-1}\log_2 M_n=1\). These are existence and rate results, **not** a formula for the exact optimum \(M_n\) at every length.

## Assumptions and scope
The alphabet is the labeled binary set \(\{0,1\}\), with bitwise complementation \(\bar0=1\), \(\bar1=0\). For \(w=w_1\cdots w_n\), define \(\rho(w)=\bar w_n\cdots\bar w_1\). A proper prefix/suffix has length \(1\le t<n\). Closure means every word is accompanied by its reverse complement; a self-reverse-complementary word counts once. There is no additional minimum Hamming distance, GC constraint, or biochemical claim.

## Proof
**1. Single orbit criterion.** For a word \(w\), the orbit \(\{w,\rho(w)\}\) is non-overlapping if and only if all three properties hold: (i) \(w\) is unbordered (no proper prefix equals a suffix); (ii) no nonempty proper prefix of \(w\) equals its own reverse complement; (iii) no nonempty proper suffix of \(w\) equals its own reverse complement. Indeed, the two self-overlap tests are equivalent because \(\rho\) exchanges prefix and suffix, and the cross-overlap tests are exactly \(p=\rho(p)\) for a prefix \(p\), and \(s=\rho(s)\) for a suffix \(s\). The equivalence includes fixed-point orbits.

**2. Endpoint restriction and excluded lengths.** In any nonempty binary non-overlapping code of length at least two, the set of first bits and the set of last bits must be disjoint by the overlap test at length one. Consequently all words start in one bit and end in its complement. Swapping the two symbols reduces the existence test to words beginning in \(0\) and ending in \(1\). For an admissible orbit at length at least four, the prefix \(01\) and suffix \(01\) are forbidden since \(\rho(01)=01\), so every representative must begin \(00\) and end \(11\). This also immediately excludes length three: its two endpoint orientations cannot fit these necessary two-bit conditions, and direct checking of \(001\) and \(011\) gives an antipalindromic suffix and prefix, respectively.

At length five the only candidates after this reduction are \(00011\) and \(00111\); the former has the reverse-complementary suffix \(0011\), the latter the reverse-complementary prefix \(0011\). At length seven the eight candidates and an explicit forbidden even-length prefix/suffix for each are:

| Candidate | Forbidden proper segment |
|---|---|
| `0000011` | suffix `0011` |
| `0000111` | suffix `000111` |
| `0001011` | suffix `001011` |
| `0001111` | prefix `000111` |
| `0010011` | suffix `0011` |
| `0010111` | prefix `001011` |
| `0011011` | prefix `0011` |
| `0011111` | prefix `0011` |

Each displayed segment has even length and equals its own reverse complement. Thus all eight have a forbidden proper segment. Therefore lengths \(3,5,7\) are impossible. This is an exhaustive finite argument using the endpoint restriction, not an inference from a bounded experiment.

**3. Existence at every other length.** At lengths one, two, four and six, respectively, use \(\{0,1\}\), \(\{01\}\), \(\{0011\}\), and \(\{000111\}\). The latter three words are self-reverse-complementary and unbordered. For every \(n\ge8\), put \(a=n-5\ge3\) and \(w_n=0^a11011\), and take \(C_n=\{w_n,\rho(w_n)\}\). It is unbordered: its only transition from an initial run of at least three zeroes to `11` occurs at position \(a+1\), whereas the corresponding first occurrence in any suffix of length at least five occurs at position \(t-4\); equality would require \(t=n\), not a proper border. For shorter candidate borders \(t\le4\), the explicit final segments `1`, `11`, `011`, `1011` differ from the initial segments. No proper prefix is self-reverse-complementary: if its length is at most \(a\), it consists solely of zeroes; if longer, its first \(a\) zeroes would force its last \(a\) bits to be ones, impossible because the longest run of ones in \(w_n\) has length two. No proper suffix is self-reverse-complementary either. Odd lengths cannot be fixed under \(\rho\) at all; for even lengths two, four and six, the suffixes are respectively `11`, `1011` and `011011`, none fixed under \(\rho\); every larger even suffix begins in at least three zeroes while ending in a word with no three consecutive ones. The criterion in step 1 proves that \(C_n\) is non-overlapping. Hence every remaining length is feasible.

**4. Full-rate explicit family.** Choose \(k=\lceil\log_2(4n)\rceil\) and \(L=n-2k-2\ge0\). Let \(U\subseteq\{0,1\}^L\) consist of words which contain neither \(0^k\) nor \(1^k\), do not start with \(1^{k-1}\), and do not end with \(0^{k-1}\). Set
\[
\mathcal G_n=\{0^k 1u0 1^k:u\in U\}.
\]
Reversal and complementation send the displayed form to the same form with \(u\) replaced by \(\rho(u)\). The two run-avoidance restrictions exchange with one another, as do the two endpoint restrictions; hence \(\rho(U)=U\) and \(\rho(\mathcal G_n)=\mathcal G_n\).

Every word in \(\mathcal G_n\) has a **unique** occurrence of \(0^k\), namely its first \(k\) positions: the following `1` separates the initial run; \(u\) contains no \(0^k\); and its ending has fewer than \(k-1\) zeroes before the fixed `0` and the final ones. For an overlap of length \(t<k\), a prefix consists of \(0^t\) and a suffix of \(1^t\), so equality is impossible. For \(t\ge k\), a matching suffix would need to begin with \(0^k\), which is impossible at a positive starting position. Thus the entire family is non-overlapping.

A uniformly selected \(u\) fails the run restrictions with probability at most \(2\max(L-k+1,0)/2^k\), and fails one of the two endpoint restrictions with probability at most \(2/2^{k-1}\). Their sum is at most \((2L+4)/2^k\le 2n/2^k\le1/2\). Hence \(|U|\ge2^{L-1}\), proving the first size bound. Since \(2^k<8n\), the second bound follows. The construction is applicable at all sufficiently large lengths (for example, every \(n\ge32\)). Finally \(M_n\le2^n\), and the lower bound forces \(n^{-1}\log_2 M_n\to1\).

## Verification
The accompanying `verify.py` directly compares the orbit criterion with all prefix/suffix tests for every binary word through length fourteen; verifies the complete small-length orbit table; checks the explicit \(w_n\) construction through length eighty; enumerates the guarded construction at lengths fourteen, sixteen, twenty, twenty-four, twenty-eight and thirty-two; and checks reverse-complement closure, unique marker positions, individual admissibility and the size inequality. The independent C++ integer-bit implementation `verify_independent.cpp` enumerates all reverse-complement orbits through length nine and checks the same small-length exclusions. These finite computations check the critical boundary cases and algorithmic implementations; the all-length conclusions follow from the proof above, not extrapolation.

To reproduce: run `python verify.py`, then compile using `g++ -O2 -std=c++17 verify_independent.cpp -o verify_independent` and execute `./verify_independent`. No external libraries are needed for these two programs.

## Relationship to prior work
Cross-bifix-free (non-overlapping) codes were developed for frame synchronization by Chee, Kiah, Purkayastha and Wang (2012), and Blackburn (2013). Their constructions and bounds concern unrestricted word sets, without requiring invariance under bit reversal and complementation. The unrestricted optimal size at length five is two, but neither that fact nor unrestricted near-optimal rates imply the existence or nonexistence of a **reverse-complement-closed** code. King and Gaborit (online 2006) study binary templates for four-letter comma-free DNA codes and separation under reverse-complement comparisons, a different code alphabet, constraint and performance measure. The present assertion is restricted to the binary involution and is not a result about those DNA templates. No equivalent combination of the exact excluded-length criterion and a full-rate symmetric construction was found in the checked research records or literature. This is a best-knowledge literature comparison, not an independent priority certificate.

## Limitations
The family size lower bound is not shown to be order-optimal; it loses a polynomial factor compared to unrestricted non-overlapping coding bounds. The exact maximum \(M_n\) is not determined except implicitly by feasibility, and the construction does not provide error correction. The binary bit involution is a mathematical analogue of complementary strands and does not model the full four-letter DNA alphabet or laboratory hybridization. Historical priority has not undergone an independent audit.

## References
- Y. M. Chee, H. M. Kiah, P. Purkayastha, and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, first posted 2012-09-03, arXiv:1209.0236, https://arxiv.org/html/1209.0236v2.
- S. R. Blackburn, *Non-overlapping codes*, first posted 2013-03-05, arXiv:1303.1026, https://arxiv.org/abs/1303.1026.
- O. D. King and P. Gaborit, *Binary templates for comma-free DNA codes*, available online 2006-10-17, DOI:10.1016/j.dam.2005.07.015, https://doi.org/10.1016/j.dam.2005.07.015.
