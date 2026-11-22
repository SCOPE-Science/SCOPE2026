# Exact two-clock collapse of the binary floating-point Bernoulli map

## Finding

Let \(p\ge 1\) be the number of binary significand bits, including the implicit leading bit, and let \(E\ge 1\) be the magnitude of the least normal exponent. Consider the nonnegative, finite, radix-two floating-point values in \([0,1)\), with normal exponents \(-E,-E+1,\ldots,-1\), all \(p\)-bit significands, and gradual underflow (all subnormal significands). Represent positive and negative zero as the **single numerical state** zero. Call this finite set \(S_{p,E}\). The Bernoulli doubling map is \(B(x)=2x\bmod 1\), taking values in \([0,1)\). It is exact in the stated binary format, including the conditional subtraction of one.

Write \(L=E+p-1\), \(N=|S_{p,E}|\), \(\tau(x)=\min\{t\ge0:B^t(x)=0\}\), and \(K(t)=|B^t(S_{p,E})|\). Then

\[
\boxed{N=(E+1)2^{p-1},\qquad \max_{x\in S_{p,E}}\tau(x)=L.}
\]

The **complete exact first-hitting histogram** is

\[
\boxed{\#\{x\in S_{p,E}:\tau(x)=t\}=
\begin{cases}1,&t=0,\\2^{\min(t,p)-1},&1\le t\le L,\\0,&t>L.\end{cases}}
\]

The **complete image-support trajectory** and the uniform-over-representable-states first-hitting cumulative distribution are, for integer \(t\ge0\),

\[
\boxed{K(t)=\begin{cases}
(E+1-t)2^{p-1},&0\le t\le E-1,\\
2^{L-t},&E-1\le t\le L,\\
1,&t\ge L,
\end{cases}}
\]

\[
\boxed{\Pr\{\tau\le t\}=\begin{cases}
2^t/N,&0\le t\le p,\\
(t-p+2)/(E+1),&p\le t\le L,\\
1,&t\ge L.
\end{cases}}
\]

In particular, image support loses an exactly constant \(2^{p-1}\) states per step until step \(E-1\), then decreases by powers of two. In contrast, starting with the **equal-state** distribution on the entire floating-point set, absorbed probability is initially exponentially small through step \(p\), then increases by precisely \(1/(E+1)\) per step. These are distinct observable finite-precision clocks, one for geometric support and one for absorption of the equal-state ensemble.

For standard IEEE binary16, binary32, and binary64 (restricted to \([0,1)\)), the triples \((p,E,L)\) are \((11,14,24)\), \((24,126,149)\), and \((53,1022,1074)\), respectively. For binary32 there are exactly \(1{,}065{,}353{,}216\) numerical states, and, for \(24\le t\le149\), precisely \((t-22)/127\) of equal-state initial mass has reached zero. Including the endpoint \(1\) as an extra initial state adds one to \(N\) and one first-hitting event at time one; it does not affect the image supports after the first update.

## Assumptions and scope

This statement concerns the ideal mathematical numerical values of a base-two floating format with gradual underflow and exact scaling by two, not an arbitrary real-to-float quantizer or a truncated fixed-point grid. The least normal positive value is \(2^{-E}\) and the least positive subnormal value is \(2^{-(E+p-1)}\). The maximum exponent field is assumed to include exponent zero so that multiplying values less than one by two is representable before any reduction modulo one. The update may be evaluated as one exact multiplication by two followed by subtracting one if the result is at least one; those operations are exact on this state set. No sampling from Lebesgue measure is assumed: the probability formula uses the uniform distribution over **distinct representable numerical states**.

For the support formula the same state set is used for initial conditions and for iterates. We never identify distinct encodings of signed zero as distinct dynamical states. Overflow, negative values, values at the excluded right endpoint, flush-to-zero processing, and denormal-are-zero modes are outside the claim.

## Proof

**Step 1: unique reduced-dyadic encoding of the entire floating set.** Let \(L=E+p-1\). Each nonzero \(x\in S_{p,E}\) has a unique reduced fraction \(x=a/2^s\) with odd positive numerator \(a\) and integer \(s\ge1\). The floating-format definition is equivalent to

\[
S_{p,E}=\{0\}\ \cup\ \left\{\frac{a}{2^s}:1\le s\le L,\quad a\text{ odd},\quad 1\le a<2^{\min(s,p)}\right\}.
\tag{1}
\]

To see this equivalence in the forward direction, a nonzero normal has \(p\)-bit unsigned significand \(m\in[2^{p-1},2^p)\) at exponent \(e\in\{-E,\ldots,-1\}\), hence \(x=m2^{e-p+1}\). Dividing out its binary trailing zeros gives \(s\le p-1-e\le L\) and an odd numerator with at most \(p\) bits. A subnormal is \(m2^{-L}\), \(1\le m<2^{p-1}\), and has the same property. Conversely, for every fraction in (1), let \(b\) be the bit length of \(a\). Its true exponent is \(e=b-1-s\). If \(e\ge-E\), left-shifting \(a\) to a \(p\)-bit significand gives the prescribed normal value. If \(e<-E\), then \(a2^{L-s}\) is a positive integer less than \(2^{p-1}\), giving exactly a subnormal value. Thus (1) is exhaustive, with no double-counting.

**Step 2: exact dynamics.** For \(s\ge2\), \(2a/2^s\bmod1\) has reduced denominator exponent \(s-1\), with odd numerator equal to \(a\bmod2^{s-1}\). For \(s=1\), the image is zero. Therefore the map decreases the reduced denominator exponent by exactly one at every positive iterate until the first zero, and \(\tau(a/2^s)=s\). This also proves that the map preserves the floating set. Arithmetic evaluation is exact: multiplication by two shifts the binary exponent without changing significand, and subtraction of one when the product belongs to \([1,2)\) is exact; alternatively, the resulting reduced fraction satisfies (1).

**Step 3: histogram.** For each \(1\le s\le L\), there are exactly \(2^{\min(s,p)-1}\) admissible odd numerators in (1). Together with zero, these are all states, yielding the histogram and

\[
N=1+\sum_{s=1}^{L}2^{\min(s,p)-1}=2^p+(L-p)2^{p-1}=(E+1)2^{p-1}.
\]

The fraction with numerator one and denominator \(2^L\) exists as the smallest subnormal and has hitting time \(L\), proving sharpness.

**Step 4: complete image sets.** For \(0\le t\le L\), every positive image has reduced denominator exponent at most \(L-t\). Conversely, if \(y=a/2^s\) belongs to (1) with \(s\le L-t\), then \(x=a/2^{s+t}\) also belongs to (1) and satisfies \(B^t(x)=y\); zero has itself as a preimage. Hence

\[
B^t(S_{p,E})=\{0\}\cup\left\{\frac{a}{2^s}\in S_{p,E}:1\le s\le L-t\right\}.
\tag{2}
\]

Counting odd numerators gives \(K(t)=1+\sum_{s=1}^{L-t}2^{\min(s,p)-1}\). If \(L-t\ge p\) this is \((L-t-p+2)2^{p-1}=(E+1-t)2^{p-1}\); otherwise it is \(2^{L-t}\). The two cases agree at \(t=E-1\), and the image is \(\{0\}\) from time \(L\) onward.

**Step 5: mass of the absorbed state.** Under the equal-state initial law, \(\Pr(\tau\le t)=\frac1N(1+\sum_{s=1}^{\min(t,L)}2^{\min(s,p)-1})\). For \(t\le p\), the numerator is \(2^t\); for \(p\le t\le L\), it is \((t-p+2)2^{p-1}\). This yields the stated cumulative distribution. All claims hold for every integer \(p,E\ge1\) and time \(t\ge0\).

## Verification

`check.py` is an independent exact-integer enumerator that constructs the floating values directly from their normalized exponent/mantissa and subnormal slots, not from (1). It applies the modular doubling update on integer ticks of the least subnormal scale, computes the first-hitting time of **every** initial state, and constructs the **entire** image set at every iterate. Tests completed across all 42 pairs \(1\le p\le7\), \(1\le E\le6\), plus a full exact enumeration of all 15,360 numerical binary16 states. Altogether these cover 18,789 explicitly enumerated initial states. The checker additionally validates symbolic boundary values for binary32 and binary64, without pretending to enumerate their astronomically larger entire grids. Run `python3 check.py` with Python 3; no external package is required. Finite tests are supplementary: Steps 1–5 give the proof for arbitrary precision and exponent range.

## Relationship to prior work

Ah-Weng and Coveney (2026) analyze evolving effective state support for finite-precision chaotic maps and report eventual collapse of the binary doubling map after 149 updates in the single-precision exponent range. Their transfer-operator treatment and numerical plots motivate the present exact two-clock question, but the material inspected does not provide formulas for the entire state-count histogram, all image sizes, or the equal-state first-hitting law at arbitrary precision and exponent range. Boghosian, Coveney, and Wang (2019) establish the fundamental degenerate asymptotic invariant measure for finite-binary doubling; Klöwer, Coveney, Paxton, and Palmer (2023) compare periodic-orbit and basin behavior for finite-precision formats and already report the number 1,065,353,216 of distinct single-precision numerical initial states in \([0,1)\). That state count is prior information, not itself a claimed new result. Their available indexed material does not establish the exact parameterized transient histograms or the distinction between support and absorption clocks proved here. The known zero-attractor fact is used as a starting point, not claimed as new.

## Limitations

These are exact results for a mathematically specified binary format and exact binary shift, not empirical claims about all hardware evaluation pipelines. If subnormals are flushed to zero, the cutoff and histogram change. The equal-state initial distribution differs from a continuously uniform initial condition projected to floats; in particular the uniform plateau is not asserted for that law. It is not claimed that the scalar Bernoulli doubling map models all precision-induced chaotic failures. No independent external mathematical audit has been conducted. The literature assessment is bounded by the sources and mathematical records specifically examined; unindexed equivalent formulas remain a priority risk.

## References

1. R. Ah-Weng and P. V. Coveney, *On the statistical reliability of chaotic simulations at reduced precision*, arXiv:2611.15344v1 (first submitted 11 November 2026). https://arxiv.org/html/2611.15344v1
2. B. M. Boghosian, P. V. Coveney, and H. Wang, *A New Pathology in the Simulation of Chaotic Dynamical Systems on Digital Computers*, Advanced Theory and Simulations **2** (2019), 1900125. https://doi.org/10.1002/adts.201900125
3. M. Klöwer, P. V. Coveney, E. A. Paxton, and T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Scientific Reports **13** (2023), 11410. https://doi.org/10.1038/s41598-023-37004-4
4. M. Fasi and M. Mikaitis, *CPFloat: A C Library for Simulating Low-precision Arithmetic*, ACM Transactions on Mathematical Software (2023). https://doi.org/10.1145/3585515
