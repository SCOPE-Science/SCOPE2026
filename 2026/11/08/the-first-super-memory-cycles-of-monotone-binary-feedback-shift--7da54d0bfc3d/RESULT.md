# The first super-memory cycles of monotone binary feedback shift registers

## Finding

Let a binary feedback shift register of memory \(n\) update its state by
\[
T_f(x_1,\ldots,x_n)=(x_2,\ldots,x_n,f(x_1,\ldots,x_n)),
\]
where \(f:\{0,1\}^n\to\{0,1\}\) is nondecreasing in the coordinatewise order. Then the largest possible period of a periodic trajectory is exactly \(n\) for every \(1\le n\le5\), but is exactly \(9\) at \(n=6\).

At memory six, the only possible periods strictly exceeding six are \(7\) and \(9\). Counting distinct cyclic binary output words modulo rotation alone, there are precisely four realizable cycles of period seven and two of period nine. Their lexicographically least rotations are

| Period | All realizable cyclic output words (canonical rotations) |
|---|---|
| \(7\) | `0001011`, `0001101`, `0010111`, `0011101` |
| \(9\) | `001010011`, `001101011` |

No cycle of period eight, or of any period from ten through twenty, is possible at memory six. There are exactly \(28\) and \(18\) rooted cyclic words of the two respective lengths.

## Assumptions and scope

A feedback rule is *monotone* if \(x_i\le y_i\) for every coordinate implies \(f(x)\le f(y)\). A *periodic trajectory of least period* \(L\) consists of \(L\) distinct states visited cyclically by \(T_f\). The associated length-\(L\) cyclic output word is read from the first register coordinate; reversing or complementing the word is **not** identified unless it already agrees under cyclic rotation. The theorem ranges over every monotone Boolean feedback function, not just functions of a prescribed circuit size or degree.

## Proof

**1. Antichain criterion.** Associate to any cyclic word \(w=w_0\cdots w_{L-1}\) its consecutive cyclic windows
\[
v_i=(w_i,w_{i+1},\ldots,w_{i+n-1})\in\{0,1\}^n,
\qquad i\in\mathbb Z/L\mathbb Z.
\]
Such a word represents a periodic orbit of *some* monotone feedback shift register of memory \(n\) if and only if the set of its \(L\) windows is an antichain under coordinatewise comparison (including distinctness).

For necessity, \(T_f\) is an order-preserving map on the finite Boolean lattice. Suppose two distinct states of an orbit satisfy \(v_i\le v_j\). Let \(k=j-i\pmod L\), with \(1\le k<L\). Monotonicity gives
\[
v_i\le T_f^k(v_i)\le T_f^{2k}(v_i)\le\cdots\le T_f^{mk}(v_i)=v_i,
\]
where \(m=L/\gcd(L,k)\). All inequalities are equalities, contradicting distinctness.

For sufficiency, suppose the cyclic windows form an antichain. Define the explicit monotone extension
\[
f(x)=\bigvee_{\substack{0\le i<L\\w_{i+n}=1}}\ \bigwedge_{\substack{1\le j\le n\\w_{i+j-1}=1}}x_j,
\]
with the convention that an empty disjunction is false and an empty conjunction is true. This formula says \(f(x)=1\) precisely when some window whose prescribed successor is one is componentwise at most \(x\). By the antichain property it agrees with \(w_{i+n}\) at every \(v_i\); hence \(T_f(v_i)=v_{i+1}\), proving sufficiency. This also shows that all qualifying cyclic words are constructive rather than merely abstract antichains.

**2. Finite cutoff.** Sperner's bound gives
\[
L\le {n\choose\lfloor n/2\rfloor}.
\]
For completeness, count maximal chains of the Boolean lattice: a set of size \(j\) lies on exactly \(j!(n-j)!\) of the \(n!\) maximal chains, and any antichain meets a chain at most once. Thus \(\sum_{v\in A}{n\choose |v|}^{-1}\le1\), proving the bound.

**3. Exhaustive finite classification.** For every \(1\le n\le6\) and integer \(L\) with
\[
n<L\le {n\choose\lfloor n/2\rfloor},
\]
inspect every one of the \(2^L\) rooted binary words of length \(L\). For each word compute all \(L\) cyclic length-\(n\) windows. Reject the word when any two windows are comparable: for bit-mask encodings \(a,b\), this is precisely \((a\mathbin{\&}b)=a\) or \((a\mathbin{\&}b)=b\). Otherwise retain it and compute the least lexicographic rotation. No words outside these finite ranges can realize a longer-than-memory orbit, by step 2.

The exact rooted counts are zero for all tested lengths at memories one through five. At memory six, the counts are

| Tested period(s) | Rooted count | Distinct rotation classes |
|---|---:|---:|
| \(7\) | 28 | 4 |
| \(8\) | 0 | 0 |
| \(9\) | 18 | 2 |
| \(10\) through \(20\) | 0 each | 0 each |

All surviving cyclic words have least period \(L\), since a smaller period would repeat a window. Each rotation class therefore contains exactly \(L\) rooted words. The six representatives displayed in the finding are the complete canonical sets. The supplied programs prove these finite counts by two different exhaustive algorithms: direct enumeration of all \(2^L\) words and independent prefix-pruned recursion that checks the cyclic boundary upon completion. The second method prunes only after two completed non-wrapping windows become comparable, a condition that no later appended bit can change.

**4. Attainment and minimality.** For every \(1\le n\le5\), the monotone pure-cycling feedback \(f(x)=x_1\) has a trajectory of period \(n\): for \(n\ge2\), start with \(0^{n-1}1\); for \(n=1\), start in either fixed state. Step 3 excludes all longer cycles. At memory six, the periodic word `001010011` is realized by the explicit monotone positive formula
\[
f(x_1,\ldots,x_6)=
(x_2\wedge x_4)\vee(x_1\wedge x_3\wedge x_6)
\vee(x_3\wedge x_4)\vee(x_1\wedge x_2\wedge x_5).
\]
Its nine successive states are `001010`, `010100`, `101001`, `010011`, `100110`, `001100`, `011001`, `110010`, `100101`, returning to `001010`; they are all distinct. Step 3 excludes every longer period. The first register width admitting a period exceeding its memory length is therefore six, with maximum nine.

## Verification

The complete finite certificate is in `verify_bruteforce.cpp` and `verify_pruned.py`; the full count table is `counts.tsv`. Each program executes the entire stated finite range rather than a sampled subset. For a standard C++17 compiler and Python 3:

```sh
c++ -std=c++17 -O2 verify_bruteforce.cpp -o verify_bruteforce
./verify_bruteforce
python3 verify_pruned.py
```

Expected final markers are `BRUTEFORCE_VERIFY_OK` and `PRUNED_VERIFY_OK`. The C++ implementation loops directly over every rooted word; the Python implementation recursively rejects completed incomparable-window violations and separately tests all wraparound windows. Both check the exact six canonical necklaces. The Python implementation additionally tests the monotone extension on all comparable input pairs of the six-dimensional Boolean cube.

## Relationship to prior work

The nonlinear feedback-shift-register model and its maximum-length cycles are classical. Çalık, Sönmez Turan and Özbudak analyze full-length registers and necessary feedback-function conditions; their results concern period \(2^n\), not the maximum attainable under coordinatewise monotonicity. Just and Enciso study general cooperative Boolean networks and recall the universal antichain/Sperner bound \({n\choose\lfloor n/2\rfloor}\), which is \(20\) at six states, but their model does not impose the single-feedback shift topology or enumerate its six-state periods. Arratia, Canfield and Hales study noncoalescing feedback registers \(f=x_1\oplus g(x_2,\ldots,x_n)\); except for pure cycling, these do not belong to the monotone subclass. The new claim is the exact small-memory threshold and complete period-seven/nine cycle classification, not the general antichain theorem or the shift-register model.

## Limitations

The result concerns binary, synchronous, deterministic feedback shift registers with a single monotone feedback function. It does not classify the number of distinct feedback functions realizing each cycle, does not assert that different cycles can coexist under one feedback function, and does not determine the maximum period for memories seven and above. The finite counts are exact because all possible lengths are bounded and exhausted; their historical priority has not been independently certified. No independent scientific audit has been performed.

## References

1. Ç. Çalık, M. Sönmez Turan, and F. Özbudak, *On Feedback Functions of Maximum Length Nonlinear Feedback Shift Registers*, IEICE Transactions on Fundamentals E93-A (2010), 1226–1231. https://doi.org/10.1587/transfun.E93.A.1226
2. W. Just and G. A. Enciso, *Ordered dynamics in biased and cooperative Boolean networks*, Advances in Difference Equations (2013), article 313. https://doi.org/10.1186/1687-1847-2013-313
3. R. Arratia, E. R. Canfield, and A. W. Hales, *Random feedback shift registers and the limit distribution for largest cycle lengths*, Combinatorics, Probability and Computing 32 (2023), 559–593. https://doi.org/10.1017/S0963548323000020
