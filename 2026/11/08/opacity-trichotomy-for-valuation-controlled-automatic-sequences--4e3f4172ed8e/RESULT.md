# Opacity trichotomy for valuation-controlled automatic sequences

## Finding
Let \(b\ge2\) be an integer, let \(Y\) be a finite nonempty alphabet, and let \(f:\mathbb N_0\to Y\) be ultimately periodic. Its **least eventual period** is the smallest integer \(p\ge1\) for which there exists an \(a\) with \(f(t+p)=f(t)\) for every \(t\ge a\); take \(a\ge0\) minimal for this \(p\). Define \(\nu_b(m)=\max\{j\ge0:b^j\mid m\}\) for \(m\ge1\), and set \(u_{b,f}(n)=f(\nu_b(n+1))\) for \(n\ge0\).

The intrinsic minimal most-significant-digit-first base-\(b\) deterministic finite automaton with output for \(u_{b,f}\), with initial state fixed by input zero, has **exactly \(a+p\) states**. Its normalized prefix-metric opacity (as defined in [1]) is
\[
\varpi_b(u_{b,f})=
\begin{cases}
1,&b\ge3,\\
0,&b=2\text{ and }a\ge1,\\
2^{1-p},&b=2\text{ and }a=0.
\end{cases}
\]
Thus the attainable normalized-opacity spectrum within this entire valuation class is exactly \(\{0\}\cup\{2^{-j}:j\ge0\}\) in binary, but only \(\{1\}\) in every base greater than two. All binary levels are attainable even with binary-valued controllers \(f\).

## Assumptions and scope
Input digits are read from most significant to least significant. The empty input has output \(f(0)\); the initial state is fixed by leading zero, so the machine is an internal automaton in the sense of [1]. The output alphabet \(Y\) need not equal the input alphabet, because opacity is an invariant of the minimal **transition graph** and compares input paths to arbitrary input-alphabet relabelings of states [1]. The metric is the first-differing-position prefix ultrametric, not an alternative quadratic comparison metric.

## Proof
**1. State construction.** The integer \(\nu_b(n+1)\) is the number of consecutive final base-\(b\) digits equal to \(b-1\) in the base-\(b\) representation of \(n\). Thus the controller whose state is the length of the current terminal \((b-1)\)-run has transition \(r\mapsto0\) on every digit \(d\in\{0,\ldots,b-2\}\) and \(r\mapsto r+1\) on \(b-1\). Identify run-length states according to the eventual-periodic tail of \(f\), obtaining the finite states \(0,1,\ldots,a+p-1\). On input \(b-1\), advance to \(r+1\), except advance from \(a+p-1\) to \(a\). On input \(d<b-1\), reset to \(0\). Output on state \(r\) is \(f(r)\). This machine produces \(u_{b,f}\) at every nonnegative input, and its initial zero transition is a self-loop.

**2. Minimality and exact size.** Every state \(r<a+p\) is accessible, by reading \(r\) copies of \(b-1\) from the initial state. Two states \(i<j<a+p\) are distinguishable if their infinite residual sequences \((f(i+t))_{t\ge0}\) and \((f(j+t))_{t\ge0}\) differ: a distinguishing suffix is simply \((b-1)^t\). If \(i\ge a\) and these residuals coincided, the difference \(j-i\), which is strictly smaller than \(p\), would be an eventual period of \(f\), a contradiction. If \(i<a\), residual coincidence would make \(f\) periodic of period \(j-i\) beginning at \(i\). The least eventual period \(p\) divides any eventual period, so \(f\) would already be \(p\)-periodic beginning at \(i<a\), contradicting the least onset \(a\). Hence all \(a+p\) states are pairwise distinguishable. The displayed automaton is intrinsic and minimal.

**3. Base at least three.** Two distinct input digits, \(0\) and \(1\), both reset the automaton to state \(0\). The length-two path labeled \(01\) therefore enters the same state by two different labels. No path of length one can be inhomogeneous. The shortest inhomogeneous path has length \(2\), so [1, Theorems 1–2] give raw opacity \(\Omega=1/2\) and normalized opacity \(\varpi=1\).

**4. Binary base, positive preperiod.** If \(b=2\) and \(a\ge1\), every zero-labelled edge enters state \(0\). Every one-labelled edge enters a state from \(\{1,\ldots,a+p-1\}\), because the wraparound edge enters \(a\ge1\). Consequently each state receives edges of only one input label, hence every path is homogeneous. Theorem 2(a) of [1] yields \(\Omega=\varpi=0\).

**5. Binary base, purely periodic controller.** If \(b=2\) and \(a=0\), the unique state admitting differently labelled incoming edges is state \(0\): a zero always resets to \(0\), whereas a one reaches \(0\) only after traversing the full cycle of \(p\) consecutive ones since the most recent zero (or the start). A conflicting path must contain both kinds of arrival; at least \(p+1\) edges are required, and \(0 1^p\) attains this bound. Hence the minimal inhomogeneous path length is \(p+1\); [1, Theorem 2(b)] gives \(\Omega=2^{-p}\) and \(\varpi=2\Omega=2^{1-p}\). This includes \(p=1\), the constant case.

**6. Attainability.** For every \(p\ge2\), take the binary-valued controller \(f(t)=1\) exactly when \(t\equiv p-1\pmod p\). Its least period is \(p\) with onset \(0\), so its opacity is \(2^{1-p}\). A constant controller gives the level \(1\). The controller \(f(0)=0\), \(f(t)=1\) for \(t\ge1\) has least period \(1\) and onset \(1\), hence opacity zero in base two. This proves the complete spectrum.

## Verification
The standalone Python 3 checker `verify.py` independently computes the Myhill–Nerode output-residual classes, constructs each finite transition graph, and searches paths breadth-first for the first conflict in incoming labels. It also compares DFAO outputs with direct divisibility-based valuations of integer inputs. It passes 4,094 genuine period/onset/base configurations and 237,440 direct input evaluations. All such tests are finite corroboration; the preceding proof establishes the unbounded quantifiers.

## Relationship to prior work
Allouche and Yao [1] introduce the prefix-metric opacity of an automatic sequence, identify it with the opacity of its intrinsic minimal automaton, and prove the shortest-inhomogeneous-path criterion. Their Example 6 evaluates the binary period-doubling sequence \(f(t)=t\bmod2\), corresponding here to \(a=0,p=2\) and normalized opacity \(1/2\). This individual instance, the general graph criterion, and the general minimization framework are not new. The contribution is the complete valuation-controller classification, exact state complexity for arbitrary ultimately periodic \(f\), and the base-dependent opacity trichotomy. The periodic-residue-clock and finite-digit-pattern questions studied elsewhere have different underlying automatic sequences and do not give the asserted trichotomy.

## Limitations
The theorem concerns the first-differing-position prefix metric, an eventually periodic controller, and standard base-\(b\) valuation sequences. It does not classify arbitrary automatic sequences, non-ultimately-periodic controllers, other opacity metrics, or their factor complexities. The 2026 journal revision of [1] was not independently inspected in full; an equivalent unindexed treatment remains possible.

## References
[1] J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences. The general case*, arXiv:2404.13601v1, first publicly posted 2024-04-21, https://arxiv.org/html/2404.13601v1 (especially Definitions 2–3, Theorems 1–2, Example 6).
